"""Event-level deduplication.

WordPress ids are unique; events are not. A session and its sponsored promo card
can both be indexed, producing two records for one event. Review 2026-09-16 found
six such pairs. Both records are kept (R1/I6); the non-canonical one carries
`duplicate_of` pointing at the canonical id, and analysis skips it.

Canonical = the lower WordPress id, which is the earlier listing.
"""
import re, unicodedata


def norm_title(t: str) -> str:
    """Strip a leading numeric date prefix, the trailing (From ...) suffix, and punctuation."""
    t = unicodedata.normalize("NFKD", t or "")
    t = re.sub(r"\((?:from|From|FROM)\s+[^)]*\)", " ", t)   # trailing date suffix
    t = re.sub(r"^\s*\d{6,8}\s*[-–—:]?\s*", " ", t)          # leading '20250716 - '
    t = re.sub(r"[^a-z0-9]+", "", t.lower())
    return t


def mark_duplicates(rows: list[dict]) -> int:
    """Group by (normalized title, date). Mark all but the lowest id. Returns pairs found."""
    groups: dict[tuple, list[dict]] = {}
    for r in rows:
        if not r.get("date"):
            continue
        groups.setdefault((norm_title(r["title"]), r["date"]), []).append(r)
    dupes = 0
    for _, g in groups.items():
        if len(g) < 2:
            continue
        g.sort(key=lambda r: r["id"])
        canonical = g[0]["id"]
        for r in g[1:]:
            r["duplicate_of"] = canonical
            dupes += 1
    return dupes
