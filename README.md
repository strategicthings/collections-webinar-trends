# Five Years of Collections Webinars

I had a theory about how debt-collection industry messaging evolved: payment portals first, then
texting and email, then "nobody answers the phone," then AI voice bots. I tested it against 1,303
webinar sessions. One part cleanly held.

**Read the analysis: https://strategicthings.github.io/collections-webinar-trends/**

## What it found

| Claim | Verdict | Evidence |
|---|---|---|
| Payment portals were a hype wave | Fails | 0% in 2021, then 1.1% to 2.2% a year. 22 of 1,303. |
| Then texting, email and omnichannel | Holds | 3.0% (2022) to a 9.4% peak (2024), down to 5.5% (2026). |
| Then "nobody answers the phone" | **Not established** | My phone category is a keyword bucket that counts call-center staffing and misses the avoidance framing. It shows no trend but cannot test the claim. |
| Now AI voice bots dominate | Partly | AI reaches 19.8%. Voice AI specifically reaches 2.7%, on 17 sessions. |

AI went from 0.8% of 2022 sessions to 19.8% of 2026 sessions. Read chronologically the AI sessions
move through four stages: explainer (2023), policy (2024), enablement (2025), workforce management
(2026).

**The obvious objection, tested and not supported.** These are sponsored webinars, so the obvious
challenge is that a rising AI share measures vendor spend. I tested it: AI events show a readable
sponsor label 86.2% of the time (81 of 94) against 75.5% (71 of 94) for a year-matched baseline.
Gap 10.6 points, **95% CI -0.5 to 21.8, p = 0.064**. The interval crosses zero, so this is not
distinguishable from chance and I am not claiming the effect.

The gap shrank on every run as measurement defects came out: 20.7, then 15.2, then 14.3, then 10.6.
What survives is unremarkable. Roughly three quarters of the whole calendar carries a sponsor label.
Sponsored programming is the normal condition here, not something particular to AI.

## Corrections, 2026-09-16

Two rounds of independent code review found thirteen errors between them. All are fixed and listed
in full in section 08 of the page. Round two changed the headline: the phone verdict moved from
"fails" to "not established," so "half of it was wrong" was no longer accurate.

Round three:

- **The sponsorship finding is withdrawn.** Its sample had been frozen against an older classifier:
  four members no longer qualified as AI and fourteen qualifying events were missing. Deduplication
  was also discarding a sponsored promo card while keeping a recording screenshot for the same
  event, lowering the numerator. Rebuilt at event level with evidence unioned across all listings,
  the gap is 10.6 points with a CI that crosses zero.
- **Staffing range was stale** (10.9-13.4% against a regenerated 10.4-14.7%), and the voice-AI note
  paired a 2026 percentage with an all-years count. 2026 rests on five events, not seventeen.

Round two:

- **Six duplicate events inflated every share.** A session and its promo card can both be indexed.
  Deduplicating by title and date gives 1,303 events from 1,309 dated records. One pair sat in both
  arms of the sponsorship sample; re-run deduplicated, the gap is 14.3 points (was 15.2).
- **The voice-AI series was still being plotted** after the card said it was withdrawn. Rebuilt
  instead: a title now needs an AI signal *and* a voice or phone signal. Reads 2.7% for 2026 on 17
  sessions.
- **"Lower bound" on the sponsorship gap was wrong** and is retracted. Bounds on two rates do not
  bound their difference.
- **Four date-parsing defects**, including a length guard that rejected valid short dates and a
  malformed year that borrowed the image's upload year. No stored date changed.

Round one:

- **OCR ran in fast mode, not accurate.** Vision defines Accurate=0, Fast=1; the code passed 1 with a
  comment claiming accurate. Fast mode misread sponsor labels ("Spon50r:"). Corrected figures moved
  the sponsorship gap from 20.7 to 15.2 points and p from 0.0015 to 0.012.
- **A causal claim was removed.** The page said a rise from 0.8% to 20.3% "does not come from a
  21-point sponsorship gap." That compares a change in share against a between-group prevalence
  difference. It cannot rule out sponsorship-driven topic selection.
- **The voice-AI figure (3.8%) is withdrawn.** The classifier matched "How to start with Agentic AI"
  and missed "AI on the Phone: The Voice (and Final) Frontier". No stable replacement exists.
- **A title was misdated.** "The Human Oversight Imperative" ran 2025-11-20, cited as 2026.

Unresolved and flagged rather than fixed: six record pairs share a title and date (likely a session
and its promo card both indexed), and the phone category is a broad keyword bucket that catches
call-center staffing content.

## Data

| File | Contents |
|---|---|
| `data/corpus.json` | 1,311 sessions, 1,309 dated, 2021-10-22 to 2026-09-15. `id`, `title`, `date`, `date_precision`, `date_rule`, `url`. |
| `data/analysis.json` | Quarterly and annual theme shares, example titles per theme per year. |
| `classifier.py` | The keyword classifier. Multi-label. Every pattern is word-boundary anchored. |

Sixteen records carry `date_precision: month` rather than `day`. Those were dated from the promo
image's upload path because the image showed only a year. Do not read them as day-accurate.

## Method

Source: the AccountsRecovery.net premium-content archive. Titles were pulled from the publication's public WordPress search index (`sfwd-courses` post type).
Session recordings are paywalled and were not accessed.

Two things are worth knowing if you reproduce this:

**Do not filter the archive on the word "webinar."** That token is a title convention the site
changed partway through its history. Filtering on it returns 0 of 49 sessions for 2021 and 89 of 258
for 2023, while missing nothing from 2024 on. Any year-over-year trend built on the filtered set
shows growth that is an artifact of the naming change.

**Recent sessions carry no date in the title.** The site appends a `(From M/D/YYYY)` suffix only
once a session is archived as a recording. For those, the date is rendered on the promo image and
was read off it with OCR.

Classification is keyword-based and multi-label, so shares do not sum to 100. `AI` is matched
case-sensitively as a standalone token so that *email*, *training* and *available* do not register
as artificial intelligence. Each theme was audited on random samples.

## Limits

This is one trade publication's event calendar. It is an influential one, and it programs several
sessions a week, but it is one editorial viewpoint with one sponsor base. Nothing here measures what
any individual agency does, and it measures programming rather than practice.

## Independence

Not affiliated with, commissioned by, or endorsed by AccountsRecovery.net or any sponsor whose
sessions are counted. No sponsor is identified individually. Built from publicly available data.

## How this was built

The hypothesis is mine and it was mostly wrong. I built the scraper and the classifier with Claude,
checked the numbers against the raw index, and ran the sponsorship test because the vendor objection
was the first thing I expected to hear.

Josh Allen, 2026-09-16.
