# Five Years of Collections Webinars

I had a theory about how debt-collection industry messaging evolved: payment portals first, then
texting and email, then "nobody answers the phone," then AI voice bots. I tested it against 1,309
webinar titles and half of it was wrong.

**Read the analysis: https://strategicthings.github.io/collections-webinar-trends/**

## What it found

| Claim | Verdict | Evidence |
|---|---|---|
| Payment portals were a hype wave | Fails | 1.1% to 2.2% of sessions in every year. 22 of 1,309. |
| Then texting, email and omnichannel | Holds | 3.0% (2022) to a 9.3% peak (2024), down to 5.5% (2026). |
| Then "nobody answers the phone" | Fails | Flat, 4.5% to 4.9%, and it rebounded in 2026. |
| Now AI voice bots dominate | Partly | AI reaches 20.3%. Voice AI specifically, 3.8%. |

AI went from 0.8% of 2022 sessions to 20.3% of 2026 sessions. Read chronologically the AI sessions
move through four stages: explainer (2023), policy (2024), enablement (2025), workforce management
(2026).

**The caveat that matters.** These are sponsored webinars. AI sessions carry a sponsor 83.7% of the
time (77 of 92) against 63.0% (58 of 92) for a year-matched non-AI baseline. Gap 20.7 points, 95% CI
8.2 to 33.1, p = 0.0015. The AI surge is more vendor-funded than the rest of the calendar. Roughly
two thirds of everything on the calendar is sponsored, so this is a tilt rather than a different
kind of content, but read the curve accordingly.

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
