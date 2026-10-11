"""Seen Back naturalist: names the species in a photo with BioCLIP 2, scored against one region's species list.

A Gradio app. On a ZeroGPU Space the image encoder runs on a GPU inside @spaces.GPU; anywhere else it runs on
the processor. One API endpoint, `identify`, takes [photo as a base64 JPEG string, month 1-12, region, top]
and returns one JSON object. A browser calls it in Gradio's two steps:
    POST /gradio_api/call/identify  {"data": [...]}        -> {"event_id": "..."}
    GET  /gradio_api/call/identify/<event_id>               -> server-sent events; `complete` carries [result]
GET /v1/health answers at once with a small JSON object.

Photos are decoded in memory and never written to disk. The log holds a running count and the time taken, nothing else.
Label rows, species table and settings are read from heads/<region>/ (manifest.json, raw little-endian float16 rows).
"""
import os

try:  # on ZeroGPU, `spaces` must be imported before torch
    import spaces
except ImportError:  # anywhere without the package the decorator is simply not applied
    spaces = None

import base64
import binascii
import io
import json
import math
import pathlib
import threading
import time
from collections import deque
from urllib.parse import urlsplit

import numpy as np
import torch
import open_clip
from PIL import Image, ImageOps
from starlette.middleware import Middleware

import gradio as gr
import gradio.route_utils as gr_route_utils

HERE = pathlib.Path(__file__).resolve().parent
HEADS = pathlib.Path(os.environ.get("SB_HEADS", str(HERE / "heads")))
ZERO_GPU = os.environ.get("SPACES_ZERO_GPU", "").strip().lower() in ("1", "true", "yes")
DEVICE = "cuda" if ZERO_GPU else ("cuda" if os.environ.get("SB_DEVICE") == "cuda" else "cpu")

MAX_B64 = 2_000_000          # characters of base64: about 1.5 MB of photo
MAX_BYTES = 1_500_000        # bytes of photo after decoding
MAX_PIXELS = 4096 * 4096     # refuse anything larger before decoding the pixels
MAX_TOP = 10
RATE_PER_MINUTE = int(os.environ.get("SB_RATE_PER_MINUTE", "30"))

ALLOWED_ORIGINS = {"https://jampotful.github.io"}
LOCAL_HOSTS = {"localhost", "127.0.0.1"}
SPACE_HOST = (os.environ.get("SPACE_HOST") or "").strip().lower()  # set by Hugging Face on a Space: <sub>.hf.space

Image.MAX_IMAGE_PIXELS = MAX_PIXELS * 2
torch.set_num_threads(int(os.environ.get("SB_THREADS", str(os.cpu_count() or 2))))


# ---------------------------------------------------------------- heads: rows, table, settings, prior

class Head:
    def __init__(self, d: pathlib.Path):
        m = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
        sp = m["species"]
        w = int(m["width"])
        self.manifest = m
        self.region = m.get("region", d.name)
        self.rows = np.fromfile(d / sp["url"], dtype="<f2").astype(np.float32).reshape(-1, w)
        self.bias = np.fromfile(d / sp["bias_url"], dtype="<f4").astype(np.float64) if sp.get("bias_url") else None
        t = json.loads((d / sp["table"]).read_text(encoding="utf-8"))
        table = t["species"]
        self.keys = t.get("keys") or [None] * len(table)
        if not (len(table) == len(self.keys) == self.rows.shape[0]):
            raise ValueError("head %s: %d rows, %d table entries, %d keys" % (d, self.rows.shape[0], len(table), len(self.keys)))
        self.sci = [r[0] or "" for r in table]
        self.en = [r[1] or "" for r in table]
        self.eyes = [r[2] or "other" for r in table]
        f = m["fusion"]
        self.t = float(f["t_species"])
        self.alpha = float(f.get("alpha_prior", 0.0))
        floor = float(f.get("prior_floor", 1e-6))
        W = np.array([[max(0.0, float(x or 0)) for x in r[3]] if isinstance(r[3], list) and len(r[3]) == 12 else [0.0] * 12
                      for r in table], dtype=np.float64)                       # species x 12
        tot = W.sum(0)                                                         # 12
        share = np.divide(W, tot, out=np.zeros_like(W), where=tot > 0)
        lp = np.log(np.maximum(share, floor))
        lp[:, tot <= 0] = 0.0                                                  # a month with no records adds nothing
        self.logprior = lp.T.copy()                                            # 12 x species
        self.kind_names = sorted(set(self.eyes))
        self.kind_index = np.array([self.kind_names.index(k) for k in self.eyes])
        self.model = m["id"]
        self.provisional = bool(m.get("provisional", False))


def load_heads():
    heads = {}
    for d in sorted(p for p in HEADS.iterdir() if (p / "manifest.json").exists()):
        h = Head(d)
        heads[h.region] = h
    if not heads:
        raise RuntimeError("no heads under %s" % HEADS)
    return heads


HEAD_BY_REGION = load_heads()
DEFAULT_REGION = "us-fl-alachua" if "us-fl-alachua" in HEAD_BY_REGION else sorted(HEAD_BY_REGION)[0]
_first = HEAD_BY_REGION[DEFAULT_REGION]
MODEL_NAME = _first.model
MODEL_SOURCE = _first.manifest.get("source", "hf-hub:imageomics/bioclip-2")

# ---------------------------------------------------------------- the model, placed at module level (ZeroGPU wants this)

_t_load = time.perf_counter()
model, _, preprocess = open_clip.create_model_and_transforms(MODEL_SOURCE)
model.eval()
model.to(DEVICE)
LOAD_SECONDS = round(time.perf_counter() - _t_load, 1)
print("model loaded in %.1f s on %s, %d threads" % (LOAD_SECONDS, DEVICE, torch.get_num_threads()), flush=True)


def _embed(x):
    with torch.no_grad():
        e = model.encode_image(x.to(DEVICE))
        e = e / e.norm(dim=-1, keepdim=True)
    return e.float().cpu().numpy()[0]


embed = spaces.GPU(duration=20)(_embed) if spaces is not None else _embed

# ---------------------------------------------------------------- manners: rate limit, counting

_lock = threading.Lock()
_count = 0
_recent = {}


class Refusal(Exception):
    def __init__(self, code, sentence):
        super().__init__(sentence)
        self.code = code


def _address(request):
    if request is None:
        return "-"
    try:
        fwd = request.headers.get("x-forwarded-for") or ""
        if fwd:
            return fwd.split(",")[0].strip()
        return request.client.host if request.client else "-"
    except Exception:
        return "-"


def _rate_ok(addr):
    now = time.monotonic()
    with _lock:
        q = _recent.setdefault(addr, deque())
        while q and now - q[0] > 60:
            q.popleft()
        if len(q) >= RATE_PER_MINUTE:
            return False
        q.append(now)
        if len(_recent) > 5000:  # forget quiet addresses
            for a in [a for a, v in _recent.items() if not v]:
                _recent.pop(a, None)
        return True


def _decode(image):
    if not isinstance(image, str) or not image.strip():
        raise Refusal("no_image", "No photo was sent; send a JPEG as a base64 string.")
    s = image.strip()
    if s.startswith("data:"):
        s = s.split(",", 1)[-1]
    if len(s) > MAX_B64:
        raise Refusal("too_large", "The photo is larger than 1.5 MB; send a JPEG whose longest side is at most 512 pixels.")
    try:
        raw = base64.b64decode(s, validate=False)
    except (binascii.Error, ValueError):
        raise Refusal("not_image", "The photo could not be read: it is not valid base64.")
    if len(raw) > MAX_BYTES:
        raise Refusal("too_large", "The photo is larger than 1.5 MB; send a JPEG whose longest side is at most 512 pixels.")
    try:
        im = Image.open(io.BytesIO(raw))
        if im.format not in ("JPEG", "PNG", "WEBP"):
            raise Refusal("not_image", "The photo must be a JPEG, PNG or WebP image.")
        if im.size[0] * im.size[1] > MAX_PIXELS:
            raise Refusal("too_large", "The photo has too many pixels; send one whose longest side is at most 512 pixels.")
        im.load()
        im = ImageOps.exif_transpose(im).convert("RGB")
    except Refusal:
        raise
    except Exception:
        raise Refusal("not_image", "The photo could not be opened as an image.")
    return im


def _int(v, name, lo, hi):
    try:
        f = float(v)
    except (TypeError, ValueError):
        raise Refusal("bad_" + name, "The %s must be a whole number from %d to %d." % (name, lo, hi))
    if not math.isfinite(f) or f != int(f) or not lo <= int(f) <= hi:
        raise Refusal("bad_" + name, "The %s must be a whole number from %d to %d." % (name, lo, hi))
    return int(f)


def identify(image, month, region, top, request: gr.Request = None):
    """Name the species in a photo. Returns one JSON object; a refusal has `error` (a plain sentence) and `code`."""
    global _count
    t0 = time.perf_counter()
    try:
        if not _rate_ok(_address(request)):
            raise Refusal("rate_limited", "Too many photos from one address in a minute; wait a little and try again.")
        region = (region or "").strip() if isinstance(region, str) or region is None else None
        if region is None or (region and region not in HEAD_BY_REGION):
            raise Refusal("unknown_region", "The region must be one of %s, or empty." % ", ".join(sorted(HEAD_BY_REGION)))
        m = _int(month, "month", 1, 12)
        try:
            k = int(float(top)) if top not in (None, "") else 5
        except (TypeError, ValueError):
            k = 5
        k = max(1, min(MAX_TOP, k))
        im = _decode(image)
        head = HEAD_BY_REGION[region or DEFAULT_REGION]
        x = preprocess(im).unsqueeze(0)
        del im
        e = embed(x).astype(np.float64)
        e /= (np.linalg.norm(e) or 1.0)
        z = head.t * (head.rows.astype(np.float64) @ e)
        if head.bias is not None:
            z = z + head.bias
        if region:
            z = z + head.alpha * head.logprior[m - 1]
        z -= z.max()
        p = np.exp(z)
        p /= p.sum()
        order = np.argsort(-p, kind="stable")[:k]
        species = [{"key": head.keys[j], "sci": head.sci[j], "en": head.en[j], "eyes": head.eyes[j], "p": round(float(p[j]), 4)}
                   for j in order]
        q = np.bincount(head.kind_index, weights=p, minlength=len(head.kind_names))
        kinds = [{"key": head.kind_names[i], "p": round(float(q[i]), 4)} for i in np.argsort(-q, kind="stable") if q[i] >= 0.0005]
        out = {"model": head.model, "region": region, "ms": 0, "species": species, "kinds": kinds,
               "device": DEVICE, "provisional": head.provisional}
        if not region:
            out["note"] = ("No region was given, so the answer is drawn from the %s list without the season's weights."
                           % head.manifest.get("region_name", DEFAULT_REGION))
    except Refusal as r:
        out = {"error": str(r), "code": r.code}
    out["ms"] = int(round((time.perf_counter() - t0) * 1000))
    with _lock:
        _count += 1
        n = _count
    print("identify %d %d ms" % (n, out["ms"]), flush=True)
    return out


def health():
    return {"ok": True, "ready": True, "model": MODEL_NAME, "species": int(_first.rows.shape[0]),
            "regions": sorted(HEAD_BY_REGION), "device": DEVICE, "zero_gpu": ZERO_GPU,
            "threads": torch.get_num_threads(), "load_seconds": LOAD_SECONDS, "provisional": _first.provisional,
            "gradio": gr.__version__}


# ---------------------------------------------------------------- who may call: the Seen Back page, this computer, this Space

def origin_allowed(origin, host):
    if not origin:
        return True
    o = origin.strip().lower().rstrip("/")
    if o in ALLOWED_ORIGINS:
        return True
    try:
        u = urlsplit(o)
    except ValueError:
        return False
    name = (u.hostname or "")
    if u.scheme == "http" and name in LOCAL_HOSTS:
        return True
    if u.scheme == "https" and SPACE_HOST and name == SPACE_HOST:
        return True
    h = (host or "").strip().lower()
    if h and name and name == h.split(":")[0] and h.split(":")[0] not in LOCAL_HOSTS:
        return True  # the Space's own page calling itself
    return False


def _gradio_origin_rule(self, request_headers):
    return origin_allowed(request_headers.get("origin"), request_headers.get("host"))


# Gradio's own CORS layer decides whether Access-Control-Allow-Origin is sent; give it this service's rule.
gr_route_utils.CustomCORSMiddleware.is_valid_origin = _gradio_origin_rule


async def _send_json(send, status, obj):
    body = json.dumps(obj).encode("utf-8")
    await send({"type": "http.response.start", "status": status,
                "headers": [(b"content-type", b"application/json"), (b"content-length", str(len(body)).encode()),
                            (b"cache-control", b"no-store")]})
    await send({"type": "http.response.body", "body": body})


class OriginGate:
    """Inside Gradio's CORS layer: answers /v1/health, and refuses any request from a page it does not serve."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope.get("type") == "http":
            hdr = {k.decode("latin-1").lower(): v.decode("latin-1") for k, v in scope.get("headers") or []}
            origin = hdr.get("origin")
            if origin and not origin_allowed(origin, hdr.get("host")):
                await _send_json(send, 403, {"error": "This service answers only the Seen Back page and pages on this computer.",
                                             "code": "origin"})
                return
            if scope.get("path") == "/v1/health" and scope.get("method") in ("GET", "HEAD"):
                await _send_json(send, 200, health())
                return
        await self.app(scope, receive, send)


# ---------------------------------------------------------------- the page on the Space, and the API

ABOUT = """
# Seen Back naturalist

Names the species in a photo for [Seen Back](https://jampotful.github.io/seen-back/), using BioCLIP 2 scored against
the species recorded in Alachua County, Florida (iNaturalist research-grade observations through GBIF), weighted by
the month. The page calls it only when the person says so. Photos are not kept: each is read in memory, answered,
and dropped.

This page is the service's API. Paste a photo as a base64 JPEG to try it by hand.
"""

with gr.Blocks(title="Seen Back naturalist", analytics_enabled=False) as demo:
    gr.Markdown(ABOUT)
    with gr.Row():
        with gr.Column():
            in_image = gr.Textbox(label="Photo as a base64 JPEG (longest side at most 512 pixels)", lines=4, max_lines=8)
            in_month = gr.Number(label="Month (1-12)", value=time.gmtime().tm_mon, precision=0)
            in_region = gr.Textbox(label="Region (us-fl-alachua, or empty)", value=DEFAULT_REGION)
            in_top = gr.Number(label="How many species (at most 10)", value=5, precision=0)
            go = gr.Button("Identify", variant="primary")
        with gr.Column():
            out_json = gr.JSON(label="Answer")
    go.click(identify, [in_image, in_month, in_region, in_top], out_json, api_name="identify", concurrency_limit=2)

demo.queue(max_size=8, default_concurrency_limit=2)

if __name__ == "__main__":
    demo.launch(
        server_name=os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0"),
        server_port=int(os.environ.get("GRADIO_SERVER_PORT", "7860")),
        ssr_mode=False,
        show_error=False,
        app_kwargs={"middleware": [Middleware(OriginGate)]},
    )
