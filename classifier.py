"""Theme classifier for the AccountsRecovery webinar corpus.

Multi-label by design: a title can be about portals AND texting. Shares are
reported as "percent of that period's sessions that mention X", never as a
partition summing to 100.

Every pattern is word-boundary anchored. 'AI' is matched case-sensitively as a
standalone token, because a case-insensitive substring match on 'ai' hits
email, training, available, maintain, chair, and said.
"""
import re

THEMES = {
    "portals": {
        "label": "Payment portals & self-service",
        "pat": r"\b(portals?|self[- ]?serv(?:e|ice)|online payment|payment page|"
               r"consumer portal|web ?site payment|pay ?online)\b",
    },
    "digital_comms": {
        "label": "Text, email & omnichannel",
        "pat": r"\b(text(?:s|ing|ed)?|SMS|MMS|10DLC|short ?codes?|e-?mails?|"
               r"omni-?channel|digital communicat\w*|digital channel\w*|"
               r"channel stack\w*|inbox|spam)\b",
    },
    "digital_strategy": {
        "label": "Digital-first strategy",
        "pat": r"\b(digital[- ]first|digital only|digital collect\w*|"
               r"digital transformation|digital strateg\w*|digital engagement|"
               r"going digital|digital adoption)\b",
    },
    "phone_contact": {
        "label": "Phone, calls & reaching people",
        "pat": r"\b(phones?|calls?|calling|caller|dialer\w*|voice ?mail|"
               r"right[- ]part\w+ contact|RPC|answer rates?|contact rates?|"
               r"connect rates?|call ?center|reassigned numbers?|"
               r"call screening|robocall\w*)\b",
    },
    "ai_general": {
        "label": "AI (any)",
        # 'AI' stays case-sensitive; everything else is (?i:) scoped, so
        # 'Voice AI' matches but 'email' and 'training' do not.
        "pat": r"(\bAI\b|(?i:\bartificial intelligence\b|\bmachine learning\b|"
               r"\bgenerative\b|\bchat ?bots?\b|\bLLMs?\b|\balgorithms?\b|"
               r"\bautomation\b|\bautomated\b))",
    },
    "ai_voice": {
        "label": "Voice AI & agentic voice",
        "pat": r"((?i:\bvoice ?)AI\b|\bAI ?(?i:voice)\b|(?i:\bvoice ?bots?\b|"
               r"\bagentic\b|\bsynthetic voice\b|\bvirtual agents?\b)|"
               r"(?i:\bconversational )AI\b|\bAI (?i:agents?)\b|"
               r"\bAI (?i:collector\w*)\b)",
    },
    # ---- controls. if these move the same way, the "trend" is programming mix.
    "compliance": {
        "label": "Compliance & regulatory (control)",
        "pat": r"\b(Reg\.? ?F|FDCPA|CFPB|TCPA|FCRA|HIPAA|compliance|regulat\w+|"
               r"lawsuits?|litigation|statute|disclosure\w*|consent|"
               r"validation notice|MVN|audit\w*)\b",
    },
    "people": {
        "label": "Hiring, training & staffing (control)",
        "pat": r"\b(hir(?:e|ing)|train(?:ing|ed)?|coach\w*|onboard\w*|retention|"
               r"retain\w*|employees?|staff\w*|collectors?|agents? (?:performance|"
               r"experience)|burn(?:ing)? out|turnover|mentorship|recruit\w*)\b",
    },
    # ---- emergent, surfaced by an open token rise/fall pass, not hypothesized.
    # An earlier version bundled disputes WITH credit reporting and the combined
    # series fell, hiding that the two move in opposite directions. Kept apart.
    "credit_reporting": {
        "label": "Credit reporting & furnishing",
        "pat": r"\b(credit reporting|credit bureau\w*|furnish\w*|Metro ?2|"
               r"e-?OSCAR|credit repair)\b",
    },
    "disputes": {
        "label": "Disputes",
        "pat": r"\b(disputes?|disputing|frivolous|validations?)\b",
    },
}

_COMPILED = {
    k: re.compile(v["pat"], 0 if k in ("ai_general", "ai_voice") else re.I)
    for k, v in THEMES.items()
}


def classify(title: str) -> set[str]:
    """Return the set of theme keys a title matches."""
    hits = {k for k, rx in _COMPILED.items() if rx.search(title)}
    # voice AI implies AI; keep the general bucket a true superset
    if "ai_voice" in hits:
        hits.add("ai_general")
    return hits
