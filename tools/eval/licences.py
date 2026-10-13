"""Which photos a head may be fitted on, by the licence each photo was shared under.

The rules (the coordinator's decision of 11 October 2026, pending the owner's):
  all   every licence (the heads fitted before the rule existed)
  nc    the public domain (CC0, "no known copyright restrictions", United States Government work), CC BY and CC BY-NC.
        Photos under any licence with ND (no derivatives) or SA (share alike) are left out of fitting.
  by    the public domain and CC BY only; for comparison.

Licence strings differ between the manifests: the training manifest says `CC-BY-NC`, the evaluation manifest
`CC-BY-NC-4.0`, the COCO extras `CC-BY-NC-2.0` or `no-known-copyright-restrictions`. family() strips the version and
gives one name for each. A string it does not know is never allowed.
"""
import re

PUBLIC_DOMAIN = ("CC0", "PD", "PUBLIC-DOMAIN", "NO-KNOWN-COPYRIGHT-RESTRICTIONS", "UNITED-STATES-GOVERNMENT-WORK")
ALLOWED = {
    "all": None,
    "nc": ("public domain", "CC-BY", "CC-BY-NC"),
    "by": ("public domain", "CC-BY"),
}
SENTENCE = {
    "all": "Rows were fitted on photos under every licence their sources gave.",
    "nc": "Rows were fitted only on photos in the public domain (CC0, no known copyright restrictions, United States Government work) or shared under CC BY or CC BY-NC; photos under any licence with ND or SA terms were left out.",
    "by": "Rows were fitted only on photos in the public domain (CC0, no known copyright restrictions, United States Government work) or shared under CC BY.",
}
RULES = tuple(ALLOWED)


def family(lic):
    """`CC-BY-NC-4.0` -> `CC-BY-NC`; `CC0-1.0`, `no-known-copyright-restrictions` -> `public domain`; unknown -> the cleaned string."""
    s = (lic or "").strip().upper().replace("_", "-").replace(" ", "-")
    s = re.sub(r"-\d+(\.\d+)*$", "", s)
    if s in PUBLIC_DOMAIN:
        return "public domain"
    return s


def allowed(lic, rule):
    if rule not in ALLOWED:
        raise ValueError("unknown licence rule %r (one of %s)" % (rule, ", ".join(RULES)))
    if ALLOWED[rule] is None:
        return True
    return family(lic) in ALLOWED[rule]
