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
| Now AI voice bots dominate | Partly | AI reaches 19.8% (36 of 182). Voice AI specifically reaches 2.7%, which is 5 events of 182; 17 across the whole archive. |

AI went from 0.8% of 2022 events to 19.8% of 2026 events.

Read chronologically, the AI titles suggest a shift in emphasis: mostly explainer in 2023, mostly
policy in 2024, mostly enablement in 2025, mostly workforce management in 2026. **That is an
illustrated reading of the titles, not a coded classification**, and the years overlap in both
directions: 2023 already had *What are the Best ChatGPT Prompts for Collection Operations to Use*,
and 2026 still has *AI 101: Back to the Basics*.

**The obvious objection, tested.** These are sponsored webinars, so the challenge is that a rising AI
share measures vendor spend. AI events show a sponsor label 88.2% of the time (82 of 93) against
76.3% (71 of 93) for a year-matched baseline. Gap 11.8 points, 95% CI 1.0 to 22.7, p = 0.035. Every
event reading unsponsored was checked by eye, because OCR is unreliable on these cards.

**Do not treat the magnitude as settled.** The interval spans 1 to 23 points and the estimate is
sensitive to how the sample is drawn and how a label is detected. It also says nothing about
causation. Sponsor labels were common in both samples, and because both are year-weighted to the AI
distribution, neither describes the calendar as a whole. Detail: `sponsorship-test/` in the analysis
repo.

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
