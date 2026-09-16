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
               r"channel stack\w*|inbox|spam folder\w*)\b",
    },
    "digital_strategy": {
        "label": "Digital-first strategy",
        "pat": r"\b(digital[- ]first|digital only|digital collect\w*|"
               r"digital transformation|digital strateg\w*|digital engagement|"
               r"going digital|digital adoption)\b",
    },
    "phone_contact": {
        "label": "Phone & call-center operations",
        "pat": r"\b(phones?|calls?|calling|caller|dialer\w*|voice ?mail|"
               r"right[- ]part\w+ contact|RPC|answer rates?|contact rates?|"
               r"connect rates?|call ?center|reassigned numbers?|"
               r"call screening|robocall\w*)\b",
    },
    "ai_general": {
        "label": "AI (any)",
        # 'AI' stays case-sensitive; everything else is (?i:) scoped, so
        # 'Voice AI' matches but 'email' and 'training' do not.
        # 2026-09-16: added spelled-out "large language model" and product names,
        # which the LLM-acronym-only pattern missed. Removed bare "automation" and
        # "algorithms": "Problems You Can Solve with Robotic Process Automation" is
        # not evidence of AI. Titles carrying both still match on the AI token.
        "pat": r"(\bAI\b|\bGPT\b|\bLLMs?\b|(?i:\bartificial intelligence\b|"
               r"\bmachine learning\b|\blarge language models?\b|\bgenerative\b|"
               r"\bchat ?bots?\b|\bChatGPT\b|\bco-?pilot\b|\bagentic\b))",
    },
    "ai_voice": {
        "label": "Voice AI",
        # Rebuilt 2026-09-16. The old pattern matched 'agentic' on its own, so
        # "How to start with Agentic AI" counted as voice, and it missed
        # "AI on the Phone: The Voice (and Final) Frontier" entirely. Now a title
        # must carry BOTH an AI signal and a voice/phone signal. Handled in
        # classify() because it is a conjunction, not one alternation.
        "pat": r"(?!x)x",   # never matches directly; see classify()
        "conjunction": (
            r"(\bAI\b|(?i:artificial intelligence|machine learning|generative|"
            r"conversational|voicebots?|voice ?bots?))",
            r"(?i)\b(voice|phone|call|calling|dialer|speech|spoken|IVR|voicebots?)\w*\b",
        ),
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
        # 2026-09-16: "train" no longer matches when the object is a model, and
        # bare "agent(s)" now counts EXCEPT where it is an AI/virtual/digital agent.
        "pat": r"\b(hir(?:e|ing)|train(?:ing|ed)?(?! +(?:your +)?(?:AI|LLM|model))|"
               r"coach\w*|onboard\w*|retention|retain\w*|employees?|staff\w*|"
               r"collectors?|(?<!AI )(?<!virtual )(?<!digital )(?<!agentic )agents?|"
               r"burn(?:ing)? out|turnover|mentorship|recruit\w*|workforce)\b",
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


_CONJ = {k: (re.compile(v["conjunction"][0]), re.compile(v["conjunction"][1]))
         for k, v in THEMES.items() if "conjunction" in v}


def classify(title: str) -> set[str]:
    """Return the set of theme keys a title matches."""
    hits = {k for k, rx in _COMPILED.items()
            if k not in _CONJ and rx.search(title)}
    for k, (a, b) in _CONJ.items():
        if a.search(title) and b.search(title):
            hits.add(k)
    # voice AI implies AI; keep the general bucket a true superset
    if "ai_voice" in hits:
        hits.add("ai_general")
    return hits
