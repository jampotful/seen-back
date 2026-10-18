"""Decrypt the texts the oa job returned. Usage: python3 ci/oa/decrypt.py <private key pem> <dir with .bin files> <out dir>
Writes <out dir>/<batch>-<entry>.txt for each file and checks it against text_sha256 in lookup.jsonl when that file is beside the .bin dir.
Keep the output outside the repository: it is paper text."""
import gzip, hashlib, json, pathlib, sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = serialization.load_pem_private_key(pathlib.Path(sys.argv[1]).read_bytes(), password=None)
src, out = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
sums = {}
lk = src.parent / "lookup.jsonl"
if lk.exists():
    for l in open(lk):
        r = json.loads(l)
        sums["%s-%s" % (r["batch"], r["entry"])] = r.get("text_sha256")
n = bad = 0
for f in sorted(src.glob("*.bin")):
    b = f.read_bytes()
    k = int.from_bytes(b[:2], "big")
    aes = key.decrypt(b[2:2 + k], padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    text = gzip.decompress(AESGCM(aes).decrypt(b[2 + k:14 + k], b[14 + k:], None)).decode("utf-8")
    if sums.get(f.stem) and hashlib.sha256(text.encode("utf-8")).hexdigest() != sums[f.stem]:
        bad += 1
        print("checksum mismatch", f.stem)
    (out / (f.stem + ".txt")).write_text(text)
    n += 1
print(n, "decrypted,", bad, "mismatched")
