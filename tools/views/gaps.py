#!/usr/bin/env python3
"""The gap table (round 2): for each offered view, the species people meet most that borrow it, and how close the best
evidence comes to each of its rows. Rerunnable: read docs/views/gaps/README.md.

Inputs (publication branches through git; curated inputs from the working tree):
  pub/naturalist-world  rows.tsv      records through 2024 per species worldwide, and the species' group (= view)
  pub/data-alachua      regions/us-fl-alachua/species.json   the county's species, records, ranks
  evidence logs         docs/views/evidence/*.jsonl in the working tree; research branches only with --with-branches
  audit                 docs/views/audit/ALL.jsonl   records the audit retracted are dropped
  pub/lit-table         *.jsonl   the automated extraction; unverified, so it only adds a hint (lit_hint), never a grade
  rows                  docs/views/gaps/rows.json   each row of each view mapped to trait keys and carry classes
  taxonomy              docs/views/gaps/taxonomy-{gbif,extra}.tsv   genus, family, order
  synonyms              docs/views/gaps/synonyms.tsv   optional, reviewed genus aliases scoped to a view
  carry                 docs/views/carry.jsonl   proposed exceptions (reported, never counted as allowed)

Carry rules (docs/views/research/BRIEF.md, "The carry rules"): rule 1 numbers never travel; rule 2 photopigments and
receptor classes travel within an order when two or more measured families agree and no measured member disagrees;
rule 3 optics, fields, acuity, flicker, tapetum and pupil travel only within a genus; rule 5 a measured disagreement in
the range blocks the carry. The checks for agreement here are crude (see README) and are marked where they apply.

Usage: python3 -I tools/views/gaps.py [--repo .] [--out docs/views/gaps] [--world 60] [--county 20] [--with-branches]
"""
import argparse
import collections
import csv
import json
import os
import re
import subprocess
import sys

VIEWS = ("alligator bee bird cat deer dog frog hawk insect plant rabbit reptile squirrel wader").split()
ALIAS = {"pupil": "pupil_shape", "optical_sensitivity": "absolute_sensitivity",
         "optical_sensitivity_um2sr": "absolute_sensitivity"}
GRADE_RANK = {"m": 0, "g": 1, "i": 2, "x": 3}
LEVELS = ("species", "genus", "family", "order")
HIGHER_ORDER = {"Squamata", "Testudines", "Crocodylia", "Anura", "Caudata"}
ORDER_SUFFIX = ("formes", "ptera", "morpha", "odea")


def git(repo, *args, check=True):
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True)
    if check and p.returncode:
        raise RuntimeError("git %s: %s" % (" ".join(args), p.stderr.decode()[:300]))
    return p.stdout


def show(repo, ref, path):
    return git(repo, "show", "%s:%s" % (ref, path)).decode("utf-8")


# ---------------------------------------------------------------- taxonomy
VIEW_GROUP = {**dict.fromkeys(("bird", "hawk", "wader"), "Aves"),
              **dict.fromkeys(("bee", "insect"), "Insecta"),
              **dict.fromkeys(("cat", "dog", "deer", "rabbit", "squirrel"), "Mammalia"),
              "frog": "Amphibia", "reptile": "Reptilia", "alligator": "Reptilia", "plant": "Plantae"}
GROUP_ORDERS = {
    "Aves": "Accipitriformes Anseriformes Apodiformes Caprimulgiformes Charadriiformes Ciconiiformes Columbiformes Coraciiformes Cuculiformes Falconiformes Galliformes Gaviiformes Gruiformes Passeriformes Pelecaniformes Piciformes Podicipediformes Procellariiformes Psittaciformes Sphenisciformes Strigiformes Suliformes Trogoniformes",
    "Insecta": "Blattodea Coleoptera Dermaptera Diptera Ephemeroptera Hemiptera Hymenoptera Lepidoptera Mantodea Mecoptera Megaloptera Neuroptera Odonata Orthoptera Phasmatodea Plecoptera Psocodea Raphidioptera Siphonaptera Thysanoptera Trichoptera Zygentoma",
    "Mammalia": "Artiodactyla Carnivora Cetacea Chiroptera Cingulata Didelphimorphia Diprotodontia Eulipotyphla Lagomorpha Monotremata Perissodactyla Pilosa Primates Proboscidea Rodentia Scandentia Sirenia",
    "Amphibia": "Anura Caudata Gymnophiona", "Reptilia": "Crocodylia Rhynchocephalia Squamata Testudines"}


class Tax:
    """Genus plus taxonomic group: homonyms never borrow another group's placement.

    Explicit view placements (county data) teach the order/family context for the
    older TSVs, which have no view column. Ambiguous unscoped lookups stay empty.
    """
    def __init__(self):
        self.g = {}
        self.context = {o: group for group, orders in GROUP_ORDERS.items() for o in orders.split()}
        self.synonyms = {}

    def group(self, family="", order="", view="", source=""):
        if view in VIEW_GROUP:
            return VIEW_GROUP[view]
        if order in self.context:
            return self.context[order]
        for group in sorted(set(VIEW_GROUP.values())):
            if group in source:
                return group
        if order.endswith("ales"):
            return "Plantae"
        return self.context.get(family, order or family)

    def add(self, genus, family, order, force=False, view="", source=""):
        if not genus:
            return
        group = self.group(family, order, view, source)
        if not group:
            return
        if view:
            for name in (family, order):
                if name:
                    self.context.setdefault(name, group)
        key = (genus, group)
        old = self.g.get(key, ("", ""))
        if force or not old[0] or not old[1]:
            self.g[key] = (family or old[0], order or old[1])

    def canonical(self, genus, view):
        seen = set()
        while (genus, view) in self.synonyms and genus not in seen:
            seen.add(genus)
            genus = self.synonyms[genus, view]
        return genus

    def aliases(self, name, view):
        """Equivalent genus/species names in this view only; preserve the epithet."""
        genus, sep, rest = name.partition(" ")
        accepted = self.canonical(genus, view)
        genera = {genus, accepted} | {g for g, v in self.synonyms
                                       if v == view and self.canonical(g, view) == accepted}
        return {g + sep + rest for g in genera}

    def placement(self, genus, view=""):
        if view:
            accepted = self.g.get((self.canonical(genus, view), self.group(view=view)))
            if accepted:
                return accepted
        names = self.aliases(genus, view) if view else {genus}
        matches = {v for (g, group), v in self.g.items()
                   if g in names and (not view or group == self.group(view=view))}
        return next(iter(matches)) if len(matches) == 1 else ("", "")

    def family(self, genus, view=""):
        return self.placement(genus, view)[0]

    def order(self, genus, view=""):
        return self.placement(genus, view)[1]

    def load_tables(self, repo):
        base = os.path.join(repo, "docs/views/gaps")
        for name in ("taxonomy-gbif.tsv", "taxonomy-extra.tsv"):
            path = os.path.join(base, name)
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    for r in csv.DictReader(f, delimiter="\t"):
                        self.add(r["genus"], r["family"], r["order"], view=r.get("view", ""), source=r.get("source", ""))
        path = os.path.join(base, "synonyms.tsv")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                for r in csv.DictReader(f, delimiter="\t"):
                    if r.get("old_genus") and r.get("current_genus") and r.get("view"):
                        self.synonyms[r["old_genus"], r["view"]] = r["current_genus"]


def clean_order(order, cls):
    if order:
        return order
    return cls if cls in HIGHER_ORDER or cls == "Crocodylia" else ""


# ---------------------------------------------------------------- parsing a taxon string
BINOM = re.compile(r"^([A-Z][a-z]+) ([a-z][a-z-]+)")
CAP1 = re.compile(r"^([A-Z][a-z]+)\b")


def parse_taxon(taxon, rank, family, order, tax):
    """-> (level, key, extra names). level in species, genus, family, order or None."""
    t = taxon or ""
    alts = re.findall(r"\(as ([A-Z][a-z]+ [a-z-]+)", t)
    t0 = re.sub(r"\(.*?\)", "", t).strip()
    rank = (rank or "").lower()
    m = BINOM.match(t0)
    if rank in ("species", "subspecies", "") and m:
        names = [m.group(1) + " " + m.group(2)] + alts
        return "species", names, m.group(1)
    if rank == "genus" or (not rank and CAP1.match(t0) and len(t0.split()) == 1 and not t0.endswith("idae")):
        c = CAP1.match(t0)
        if c:
            return "genus", [c.group(1)], c.group(1)
    if rank == "family" or t0.split(" ")[0].endswith(("idae", "inae")) and len(t0.split()) == 1:
        return "family", [t0.split(" ")[0]], ""
    if rank == "order" or (len(t0.split()) == 1 and (t0.endswith(ORDER_SUFFIX) or t0 in HIGHER_ORDER
                                                         or t0 in ("Carnivora", "Artiodactyla", "Rodentia",
                                                                   "Lagomorpha", "Primates", "Hymenoptera",
                                                                   "Diptera", "Hemiptera", "Coleoptera",
                                                                   "Odonata", "Orthoptera", "Mantodea"))):
        return "order", [t0.split(" ")[0]], ""
    if m:
        return "species", [m.group(1) + " " + m.group(2)] + alts, m.group(1)
    return None, [], ""


# ---------------------------------------------------------------- the evidence
def load_evidence(repo, tax, retracted, with_branches=False):
    """Curated working-tree records; pending research branches are opt-in. -> list of dicts (deduplicated)."""
    seen = set()
    recs = []

    def take(unit, text, origin):
        for n, line in enumerate(text.splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except ValueError:
                continue
            key = (unit, n, r.get("taxon"), r.get("trait"), json.dumps(r.get("value")),
                   (r.get("source") or {}).get("doi"), r.get("quote"))
            if key in seen:
                continue
            seen.add(key)
            u = unit  # audit/fix ids name the file, never the record's shared unit field
            if "%s:%d" % (u, n) in retracted:
                continue
            r["_id"] = "%s#%d" % (u, n)
            r.update(fixes.get("%s:%d" % (u, n), {}))
            r["_origin"] = origin
            recs.append(r)

    fixes = {}  # "<unit>:<line>" -> fields that override the record (docs/views/fixes/*.jsonl; the evidence files stay as written)
    fxdir = os.path.join(repo, "docs/views/fixes")
    for f in sorted(os.listdir(fxdir)) if os.path.isdir(fxdir) else []:
        if f.endswith(".jsonl"):
            for line in open(os.path.join(fxdir, f), encoding="utf-8"):
                try:
                    fx = json.loads(line)
                except ValueError:
                    continue
                if fx.get("id"):
                    fixes.setdefault(fx["id"], {}).update({k: v for k, v in fx.items() if k in ("partial",)})
    evdir = os.path.join(repo, "docs/views/evidence")
    for f in sorted(os.listdir(evdir)) if os.path.isdir(evdir) else []:
        if f.endswith(".jsonl") and not f.endswith("-failed.jsonl"):
            take(f[:-6], open(os.path.join(evdir, f), encoding="utf-8").read(), "main")
    refs = git(repo, "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/research").decode().split() if with_branches else []
    for ref in refs:
        for path in git(repo, "ls-tree", "-r", "--name-only", ref, "docs/views/evidence", check=False).decode().split():
            if path.endswith(".jsonl") and not path.endswith("-failed.jsonl"):
                take(os.path.basename(path)[:-6], show(repo, ref, path), ref.replace("origin/", ""))
    index = collections.defaultdict(list)
    for r in recs:
        trait = ALIAS.get(r.get("trait"), r.get("trait"))
        r["_trait"] = trait
        lvl, names, genus = parse_taxon(r.get("taxon"), r.get("rank"), r.get("family"), r.get("order"), tax)
        if lvl is None:
            r["_lvl"] = None
            continue
        fam = r.get("family") or ""
        order = r.get("order") or ""
        if lvl == "species":
            tax.add(genus, fam, order)
        r["_lvl"] = lvl
        r["_names"] = names
        r["_genus"] = genus
        if lvl == "species":
            for nm in names:
                index[("species", nm, trait)].append(r)
            index[("genus", genus, trait)].append(r)
        elif lvl == "genus":
            index[("genus", genus, trait)].append(r)
        elif lvl == "family":
            index[("family", names[0], trait)].append(r)
        elif lvl == "order":
            index[("order", names[0], trait)].append(r)
        r["_family"] = fam if lvl != "family" else names[0]
        r["_order"] = order if lvl != "order" else names[0]
    return recs, index


def order_evidence(recs):
    """(order, trait) -> {family: [records]} for records measured at species or genus level, by their own fields."""
    d = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        if r["_lvl"] in ("species", "genus") and r.get("grade") == "m" and r["_order"] and r["_family"]:
            d[(r["_order"], r["_trait"])][r["_family"]].append(r)
    return d


def best(recs):
    return sorted(recs, key=lambda r: (GRADE_RANK.get(r.get("grade"), 9), 0 if r.get("opened") else 1))[0] if recs else None


def short_value(r):
    v = r.get("value")
    s = json.dumps(v) if not isinstance(v, str) else v
    return s if len(s) <= 40 else s[:37] + "..."


def disagree(records, trait):
    """Crude rule 5: categorical values (strings) whose first word differ, or receptor class counts that differ."""
    vals = set()
    for r in records:
        if r.get("grade") != "m":
            continue
        v = r.get("value")
        if trait == "receptor_classes" and isinstance(v, (int, float)):
            vals.add(v)
        elif isinstance(v, str) and trait in ("pupil_shape", "fovea", "tapetum", "eye_type", "eye_movement", "diel"):
            vals.add(re.sub(r"[^a-z]+", " ", v.lower()).split(" ")[0])
    return len(vals) > 1


# ---------------------------------------------------------------- one cell: species x trait
def cell(sp, trait, cls, index, ord_ev, tax, carry_exc):
    """-> dict(state m|g|i, level, rec, rule, note). Closest evidence is reported whatever its state."""
    view = sp.get("view", "")
    genus = sp["genus"]
    fam = sp["family"]
    order = sp["order"]
    def lookup(lvl, key):
        names = tax.aliases(key, view) if view and lvl in ("species", "genus") else {key}
        return [r for name in sorted(names) for r in index.get((lvl, name, trait), [])]

    def same_group(r):
        return not view or tax.group(r.get("_family", ""), r.get("_order", "")) == tax.group(view=view)

    species_names = tax.aliases(sp["sci"], view) if view else {sp["sci"]}
    found = {}
    for lvl, key in (("species", sp["sci"]), ("genus", genus), ("family", fam), ("order", order)):
        recs = lookup(lvl, key)
        if lvl == "species":
            recs = [r for r in recs if r["_lvl"] == "species"]
        elif lvl == "genus":
            recs = [r for r in recs if r["_lvl"] in ("species", "genus") and not species_names.intersection(r["_names"])]
            if True:
                recs += [r for r in lookup("genus", genus) if r["_lvl"] == "genus" and r not in recs]
        elif lvl == "family":
            fams = [r for r in index.get(("family", fam, trait), [])]
            recs = fams
        elif lvl == "order":
            recs = [r for r in index.get(("order", order, trait), [])]
        if lvl == "family" and not recs:
            recs = [r for k in [("x",)] for r in ord_family(index, fam, trait)]
        if lvl == "order" and not recs:
            recs = [r for fam_recs in ord_ev.get((order, trait), {}).values() for r in fam_recs
                    if r["_family"] != fam]
        recs = [r for r in recs if same_group(r)]
        if recs:
            found[lvl] = recs
    out = {"state": "i", "level": "none", "rec": None, "rule": "", "note": ""}
    # species measurement
    sr = found.get("species", [])
    ms = [r for r in sr if r.get("grade") == "m"]
    if ms:
        out.update(state="m", level="species", rec=best(ms), rule="measured",
                   full=any(not r.get("partial") for r in ms))  # False when only abstract-level records measure it
        return out
    # genus carry (rule 3, or rule 2 for the order class, which is wider)
    gr = found.get("genus", [])
    gm = [r for r in gr if r.get("grade") == "m"]
    if gm and cls in ("genus", "order"):
        if disagree(gm, trait):
            out.update(level="genus", rec=best(gm), note="measured members of the genus disagree (rule 5)")
        else:
            out.update(state="g", level="genus", rec=best(gm), rule="rule 3" if cls == "genus" else "rule 2")
            return out
    # order carry (rule 2 only)
    if cls == "order" and order:
        fams = {f: [r for r in rs if same_group(r)] for f, rs in ord_ev.get((order, trait), {}).items()}
        fams = {f: rs for f, rs in fams.items() if rs}
        allrecs = [r for rs in fams.values() for r in rs]
        if len(fams) >= 2 and not disagree(allrecs, trait):
            out.update(state="g", level="order", rec=best(allrecs), rule="rule 2 (%d measured families)" % len(fams))
            return out
        if allrecs:
            out.update(level="order", rec=best(allrecs),
                       note=("only %d measured family" % len(fams)) if len(fams) < 2 else "families disagree")
    # closest evidence that no rule allows
    for lvl in LEVELS:
        if lvl in found and out["rec"] is None:
            b = best(found[lvl])
            permitted = (lvl == "genus" and cls in ("genus", "order")) or (lvl == "order" and cls == "order")
            if permitted:
                out.update(level=lvl, rec=b, note="the %s record is grade %s, not a measurement" % (lvl, b.get("grade")))
            else:
                out.update(level=lvl, rec=b, note="no carry rule allows %s level for this trait" % lvl)
    if sr and out["rec"] is None:
        out.update(level="species", rec=best(sr), note="species record is not a measurement (grade %s)" % best(sr).get("grade"))
    if out["level"] == "none":
        out["note"] = "no record"
    if out["rec"] is not None and out["level"] in found:
        out["note"] = out["note"] or "not allowed"
    exc = [e for e in carry_exc if trait in e["traits"] and any(n for n in e["names"] if n and n in
                                                              (sp["sci"], genus, fam, order))]
    if exc:
        out["exception"] = "proposed: %s -> %s" % (exc[0]["from"][:40], exc[0]["to"][:40])
    return out


def ord_family(index, fam, trait):
    """Records measured in another genus of the same family (their own family field)."""
    return FAMILY_INDEX.get((fam, trait), [])


FAMILY_INDEX = {}


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--out", default="docs/views/gaps")
    ap.add_argument("--world", type=int, default=60)
    ap.add_argument("--county", type=int, default=20)
    ap.add_argument("--no-lit", action="store_true")
    ap.add_argument("--with-branches", action="store_true", help="include pending origin/research/* evidence (not for publication)")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    out = os.path.join(repo, a.out)
    os.makedirs(out, exist_ok=True)

    # counts
    rows_text = show(repo, "origin/pub/naturalist-world", "rows.tsv")
    world = [r for r in csv.DictReader(rows_text.splitlines(), delimiter="\t")]
    for r in world:
        r["records"] = int(r["records"])
    cj = json.loads(show(repo, "origin/pub/data-alachua", "regions/us-fl-alachua/species.json"))["species"]
    county = {s["sci"]: s for s in cj}

    # taxonomy
    tax = Tax()
    for s in cj:
        tax.add(s["genus"], s["family"], clean_order(s["order"], s["class"]), view=s["eyes"])
    tax.load_tables(repo)

    audit_path = os.path.join(repo, "docs/views/audit/ALL.jsonl")
    retracted = set()
    if os.path.exists(audit_path):
        for line in open(audit_path, encoding="utf-8"):
            v = json.loads(line)
            if v.get("verdict") == "retract":
                retracted.add("%s:%s" % (v["unit"], v["line"]))

    recs, index = load_evidence(repo, tax, retracted, with_branches=a.with_branches)
    FAMILY_INDEX.clear()
    for r in recs:
        if r["_lvl"] in ("species", "genus") and r.get("_family"):
            FAMILY_INDEX.setdefault((r["_family"], r["_trait"]), []).append(r)
    recs = [r for r in recs if r["_lvl"]]
    ord_ev = order_evidence(recs)
    # fill the taxonomy again now that the evidence has added its genera
    rowmap = json.load(open(os.path.join(repo, "docs/views/gaps/rows.json"), encoding="utf-8"))
    cls_of = {}
    for c, ts in rowmap["classes"].items():
        for t in ts:
            cls_of[t] = c

    carry_exc = []
    cpath = os.path.join(repo, "docs/views/carry.jsonl")
    if os.path.exists(cpath):
        for line in open(cpath, encoding="utf-8"):
            try:
                e = json.loads(line)
            except ValueError:
                continue
            names = set(re.findall(r"[A-Z][a-z]+(?: [a-z]+)?", e.get("from", "") + " " + e.get("to", "")))
            carry_exc.append({"from": e.get("from", ""), "to": e.get("to", ""), "traits": e.get("traits", []),
                              "names": names})

    # the lit table: a hint only (genus-level, unverified)
    lit = collections.defaultdict(list)
    if not a.no_lit:
        wanted_traits = {t for v in rowmap["views"].values() for ts in v.values() for t in ts}
        for path in git(repo, "ls-tree", "-r", "--name-only", "origin/pub/lit-table", check=False).decode().split():
            if not path.endswith(".jsonl"):
                continue
            for line in show(repo, "origin/pub/lit-table", path).splitlines():
                if '"taxon"' not in line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                tr = ALIAS.get(r.get("trait"), r.get("trait"))
                m = BINOM.match(r.get("taxon") or "")
                if tr in wanted_traits and m and r.get("grade") == "m":
                    lit[(m.group(1), tr)].append((m.group(1) + " " + m.group(2), path[:-6]))

    # per view
    queue = []
    cells_out = []
    summary = {}
    all_by_view = collections.defaultdict(list)
    for r in world:
        if r["group"] in VIEWS:
            all_by_view[r["group"]].append(r)
    for view in VIEWS:
        vrows = rowmap["views"][view]
        world_all = sorted(all_by_view[view], key=lambda r: -r["records"])
        total_world = sum(r["records"] for r in world_all)
        county_all = sorted([s for s in cj if s["eyes"] == view], key=lambda s: -s["n"])
        total_county = sum(s["n"] for s in county_all)
        sel = {}
        for rank, r in enumerate(world_all[:a.world], 1):
            sel[r["sci"]] = {"sci": r["sci"], "en": r["en"], "world": r["records"], "wrank": rank}
        for rank, s in enumerate(county_all[:a.county], 1):
            e = sel.setdefault(s["sci"], {"sci": s["sci"], "en": s["en"], "world": next(
                (w["records"] for w in world_all if w["sci"] == s["sci"]), 0)})
            e["crank"] = rank
        for e in sel.values():
            genus = e["sci"].split(" ")[0]
            e["view"] = view
            e["genus"] = genus
            e["family"] = tax.family(genus, view)
            e["order"] = tax.order(genus, view)
            e["county"] = county[e["sci"]]["n"] if e["sci"] in county else 0
        species = sorted(sel.values(), key=lambda e: (-e["world"], e["sci"]))
        wlist = [e for e in species if "wrank" in e]
        clist = sorted([e for e in species if "crank" in e], key=lambda e: e["crank"])

        # cells
        stats = collections.Counter()
        gap_records = 0
        gap_row_records = 0
        row_records = 0
        for e in species:
            e["cells"] = {}
            e["rows"] = {}
            for title, traits in vrows.items():
                states = []
                for t in traits:
                    if t not in e["cells"]:
                        c = cell(e, t, cls_of.get(t, "none"), index, ord_ev, tax, carry_exc)
                        h = lit.get((e["genus"], t))
                        if h and c["state"] == "i":
                            c["lit_hint"] = sorted({x[0] for x in h})[:3]
                        e["cells"][t] = c
                    states.append(e["cells"][t]["state"])
                if all(s == "m" for s in states):
                    st = "m"
                elif all(s in ("m", "g") for s in states):
                    st = "g"
                else:
                    st = "i"
                e["rows"][title] = (st, states)
                stats[st] += 1 if e in wlist else 0
            if e in wlist:
                n_i = sum(1 for t in vrows if e["rows"][t][0] == "i")
                row_records += e["world"] * len(vrows)
                gap_row_records += e["world"] * n_i
                if n_i:
                    gap_records += e["world"]
        # queue lines
        for e in species:
            for t, c in e["cells"].items():
                titles_all = [title for title, traits in vrows.items() if t in traits]
                cells_out.append({"view": view, "taxon": e["sci"], "genus": e["genus"], "family": e["family"],
                                  "order": e["order"], "en": e.get("en", ""), "trait": t, "state": c["state"], "level": c["level"],
                                  "full": bool(c.get("full", False)), "records": e["world"],
                                  "score": e["world"] * len(titles_all)})
                if c["state"] != "i":
                    continue
                titles = [title for title, traits in vrows.items() if t in traits]
                queue.append({"view": view, "taxon": e["sci"], "genus": e["genus"], "family": e["family"],
                              "order": e["order"], "trait": t, "rows": len(titles), "row_titles": titles,
                              "records": e["world"], "county_records": e["county"],
                              "closest": c["level"], "closest_record": c["rec"]["_id"] if c["rec"] else None,
                              "note": c.get("note", ""), "lit_hint": c.get("lit_hint", []),
                              "exception": c.get("exception", ""), "score": e["world"] * len(titles)})
        covered = sum(e["world"] for e in wlist)
        cov_c = sum(e["county"] for e in clist)
        summary[view] = {"species_total": len(world_all), "records_total": total_world,
                         "records_listed": covered, "share": covered / total_world if total_world else 1.0,
                         "county_total": total_county, "county_listed": cov_c,
                         "county_share": cov_c / total_county if total_county else 1.0,
                         "listed": len(wlist), "gap_records": gap_records, "gap_row_records": gap_row_records,
                         "row_records": row_records, "row_states": dict(stats),
                         "n_rows": len(vrows)}
        write_view(out, view, vrows, wlist, clist, summary[view])

    # every cell, open or closed, for the papers-wanted verdicts (tools/views/gain.py)
    with open(os.path.join(out, "cells.jsonl"), "w", encoding="utf-8") as f:
        for line in cells_out:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
    queue.sort(key=lambda q: (-q["score"], q["taxon"], q["trait"]))
    with open(os.path.join(out, "queue.jsonl"), "w", encoding="utf-8") as f:
        for q in queue:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    json.dump(summary, open(os.path.join(out, "summary.json"), "w"), indent=1)
    write_readme(out, summary, len(recs), len(retracted), len(queue))
    print("records read:", len(recs), "retracted:", len(retracted), "queue lines:", len(queue))
    for v in sorted(summary, key=lambda v: -summary[v]["gap_records"]):
        s = summary[v]
        print(v, "gap records", s["gap_records"], "listed", s["records_listed"], "of", s["records_total"])


def cell_text(c):
    if c["state"] == "m":
        r = c["rec"]
        return "m (%s)" % r["_id"]
    if c["state"] == "g":
        return "g, %s from %s (%s)" % (c["rule"], c["rec"]["taxon"].split(" (")[0][:28], c["rec"]["_id"])
    if c["rec"] is None:
        return "i, none"
    return "i, closest %s (%s), %s" % (c["level"], c["rec"]["_id"], c["note"])


def write_view(out, view, vrows, wlist, clist, s):
    L = []
    L.append("# Gap table: %s\n" % view)
    L.append("Made by `tools/views/gaps.py`. The %d species most recorded worldwide that borrow this view cover %.1f%% "
             "of its %s research-grade records; the %d most recorded in Alachua County cover %.1f%% of the county's %s. "
             "Counts are iNaturalist research-grade records through 2024. The view's own measured animal is not "
             "excluded: it shows as `m` where it was measured.\n"
             % (s["listed"], 100 * s["share"], format(s["records_total"], ","), len(clist), 100 * s["county_share"],
                format(s["county_total"], ",")))
    L.append("Row grades: `m` every trait of the row measured in that species; `g` every trait measured or carried by a "
             "rule; `i` at least one trait neither. The detail columns give the state of each trait.\n")
    L.append("Rows and their traits:\n")
    for title, traits in vrows.items():
        L.append("- **%s**: %s" % (title, ", ".join(traits)))
    L.append("")
    for heading, lst, key in (("Worldwide", wlist, "world"), ("Alachua County", clist, "county")):
        L.append("## %s\n" % heading)
        head = "| # | species | records | county | family / order | " + " | ".join(vrows) + " |"
        L.append(head)
        L.append("|" + "---|" * (5 + len(vrows)))
        for i, e in enumerate(lst, 1):
            cellsr = []
            for title in vrows:
                st, states = e["rows"][title]
                cellsr.append(st)
            L.append("| %d | %s (%s) | %s | %s | %s / %s | %s |" % (
                i, e["sci"], e["en"], format(e["world"], ","), format(e["county"], ","),
                e["family"] or "?", e["order"] or "?", " | ".join(cellsr)))
        L.append("")
        L.append("### Detail by trait (%s)\n" % heading.lower())
        L.append("Each line: species, trait, state, record behind it, and whether a carry rule allows it.\n")
        for e in lst:
            parts = []
            for t, c in e["cells"].items():
                tags = cell_text(c)
                if c.get("exception"):
                    tags += " [exception %s]" % c["exception"]
                if c.get("lit_hint"):
                    tags += " [lit table has genus: %s]" % ", ".join(c["lit_hint"])
                parts.append("%s: %s" % (t, tags))
            L.append("- *%s*: %s" % (e["sci"], "; ".join(parts)))
        L.append("")
    open(os.path.join(out, view + ".md"), "w", encoding="utf-8").write("\n".join(L))


def write_readme(out, summary, nrec, nret, nq):
    L = ["# The gap table\n",
         "For each of the fourteen offered views, the species people meet most that borrow it, and how close the best "
         "evidence comes to each row. Made by `tools/views/gaps.py`.\n",
         "## Rerun",
         "```",
         "git fetch --depth 1 origin +refs/heads/pub/naturalist-world:refs/remotes/origin/pub/naturalist-world \\",
         "  +refs/heads/pub/data-alachua:refs/remotes/origin/pub/data-alachua \\",
         "  +refs/heads/pub/lit-table:refs/remotes/origin/pub/lit-table",
         "python3 -I tools/views/gaps.py            # add --no-lit to skip the literature table",
         "```",
         "It reads the working-tree evidence logs (excluding held `*-failed.jsonl`); `--with-branches` explicitly includes "
         "pending `origin/research/*` evidence for comparison only. It drops records the "
         "audit retracted (`docs/views/audit/ALL.jsonl`), and rewrites `docs/views/gaps/<view>.md`, `queue.jsonl`, `cells.jsonl` (every cell with its state, for the papers-wanted verdicts) and "
         "`summary.json`. Add a genus to `taxonomy-extra.tsv` when a new species has no family or order; the table "
         "marks those it filled by hand as `own`, from general knowledge, unchecked against GBIF.\n",
         "## What each file holds",
         "- `<view>.md`: the 60 borrowing species most recorded worldwide and the 20 most recorded in Alachua County; "
         "for each row a grade (`m`, `g`, `i`) and below it, trait by trait, the record behind it and the rule.",
         "- `queue.jsonl`: one line per gap (a species and a trait nobody measured or may carry), with `rows` (how many "
         "of the view's rows rest on the trait), `records` (the species' worldwide records), `county_records`, the "
         "closest evidence and a `lit_hint` where the automated literature table has the genus. Ranked by `score`, "
         "records times rows.",
         "- `rows.json`: each row of each view mapped to trait keys and the carry class of each trait.",
         "- `taxonomy-extra.tsv`: genus, family, order for genera the county list and the evidence lack.\n",
         "## How the grades are decided",
         "A species is `m` for a trait when a record of grade `m` names the species. It is `g` when a measured "
         "congener exists and the trait travels within a genus (rule 3 traits, and rule 2 traits too), or when two or "
         "more measured families of its order exist and the trait is a photopigment or receptor count (rule 2). A "
         "disagreement (rule 5) is tested crudely: receptor-class counts that differ, or categorical values (pupil, "
         "fovea, tapetum, eye type, eye movement, diel) whose first word differs. Numbers are not compared. Family-level "
         "evidence never carries; a proposed exception in `docs/views/carry.jsonl` is shown beside the cell and not "
         "counted. The literature table (`pub/lit-table`) is automated and unverified: it only adds `lit_hint`.\n",
         "## Run summary\n",
         "Records read: %d (after dropping %d the audit retracted); queue lines: %d.\n" % (nrec, nret, nq),
         "| View | species in the world rows | records | share covered by the %s | county records | share covered by the county's 20 | records of listed species with a gap | gap row-records (records x rows in state i) |"
         % "listed species",
         "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for v in sorted(summary, key=lambda v: -summary[v]["gap_records"]):
        s = summary[v]
        L.append("| %s | %s | %s | %.1f%% | %s | %.1f%% | %s | %s |" % (
            v, format(s["species_total"], ","), format(s["records_total"], ","), 100 * s["share"],
            format(s["county_total"], ","), 100 * s["county_share"], format(s["gap_records"], ","),
            format(s["gap_row_records"], ",")))
    L.append("")
    open(os.path.join(out, "README.md"), "w", encoding="utf-8").write("\n".join(L))


if __name__ == "__main__":
    sys.exit(main())
