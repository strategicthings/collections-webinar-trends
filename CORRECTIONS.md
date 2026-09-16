# Revision record

This analysis went through four rounds of independent code review on 2026-09-16 before the figures
settled. Nineteen defects were found and fixed. This file is the provenance record; the published
page carries the final figures and the limitations that still apply.

Nothing here is a live caveat. For those, read the Method section of the page.


  08
    Corrections
    Published 2026-09-16 morning. Corrected the same day after review.
  
  
    Four rounds of independent review of the code and data found nineteen errors. All are fixed
    above. I am listing them rather than quietly editing, because the first version was public for
    several hours and a number of figures moved, including the headline.
    Round two also changed the framing. The phone verdict moved from "fails" to "not
    established," because my classifier cannot test that proposition. With only one of four claims
    cleanly holding and one untestable, the original headline, "half of it was wrong," was no longer
    accurate and has been replaced.
  

  Round four: the sponsorship negatives were adjudicated by eye
  
    A known OCR miss was still in the data, and it changed the verdict. Round three
    concluded "the effect is not there" at p = 0.064. One card that plainly reads SPONSORED BY was
    recorded as unsponsored. I then checked all 35 negatives visually and found two errors,
    one in each arm. Corrected: 88.2% against 76.3%, an 11.8-point gap, 95% CI 1.0 to 22.7,
    p = 0.035.
    I had turned an inconclusive test into evidence of absence. An interval reaching
    +21.8 points does not establish that nothing is there. Round three's "the effect is not there"
    was as much an overreach as round one's claim that it was. The page now says what the data
    supports: the magnitude is unsettled and the direction is not established.
    An event with no evidence was counted as a negative. Event 240144's image returns a
    404, and the code scored missing evidence as "no sponsor," which lets a network failure move the
    measured rate. Missing evidence is now excluded as unknown, with a matched event dropped from
    the other arm so the year matching holds.
    The shrinking sequence was not the clean story I told. I presented 20.7 to 15.2 to
    14.3 to 10.6 as measurement error coming out. Between two of those runs the baseline was about
    half resampled, so the movement mixes repairs with resampling, and one repair (restoring the
    discarded sponsored card) pushes the gap up. The sequence is revision history, not a
    finding.
    The four-stage AI narrative had wrong counts and was overstated. It said 94 of 98
    sessions; it is 98 of 101 events, with 2023 at 20 and 2026 at 36, not 15 and 37. The progression
    is also an illustrated reading rather than a coded result, and the years overlap in both
    directions. Labeled as such, with the counterexamples named. A claim that a session title proves
    something is "already on the payroll" is also gone.
  

  Round three: sample rebuilt
  
    The sample was frozen against an older classifier. After I rebuilt the AI category,
    four records in the sample no longer qualified as AI, including Problems You Can Solve with
    Robotic Process Automation, and fourteen qualifying events were missing from it entirely.
    The statistic was describing a category the page no longer used.
    Deduplication was throwing away sponsorship evidence. For event 221686 it kept the
    recording screenshot and dropped the sponsored promo card, which mechanically lowered the
    numerator. Dedup decides what an event is; it must not decide what evidence survives. Evidence
    is now unioned across every listing of an event.
    Rebuilt, the gap read 10.6 points at p = 0.064, and I wrote that up as the effect
    not being there. Round four showed that conclusion rested on an uncorrected OCR miss. See above.
    I also framed the uncertainty wrongly. I wrote that the interval "nearly touches
    zero" as though sampling noise were the main risk. It is not. Misclassification, stale group
    membership and discarded evidence were the real problems, and a confidence interval does not
    account for any of them.
    The staffing range was stale at 10.9% to 13.4% against regenerated data of 10.4% to
    14.7%, and the voice-AI note gave a 2026 percentage next to an all-years count, which reads as
    though 2026 rested on 17 events. It rests on five.
  

  Round two
  
    The withdrawn voice-AI series was still being plotted. I pulled it from the verdict
    card but left it in the chart, legend, tooltip and table, so the page said "withdrawn" while
    rendering 3.8%. Rather than delete the series I rebuilt the category: it now requires an AI
    signal and a voice or phone signal in the same title, so AI on the Phone: The Voice
    (and Final) Frontier counts and How to start with Agentic AI does not. It reads
    2.7% in 2026, which is five events out of 182, and seventeen across the whole archive.
    Too thin for a trend, and labeled as such.
    I claimed the sponsorship gap was a lower bound. It is not. Undercounting both rates
    does not bound their difference in either direction. Retracted in full.
    Six duplicate events were inflating every share. A session and its promo card can
    both be indexed. Deduplicating by title and date takes 1,309 dated records to 1,303
    events, and one of the six pairs was sitting in both arms of the sponsorship sample. Re-run
    on deduplicated, re-matched samples the figures were 85.7% against 71.4%, a 14.3-point gap.
    Round three rebuilt the sample again and the effect did not survive.
    Superseded sponsorship figures survived in two places. The method caveat still said
    21 points, and the data README still carried the old confidence interval.
    The chronology fix introduced a new unsupported claim. I called a November 2024 title
    the earliest both-sides framing. The Types of Calls that Technology Can Handle and the Types
    that Need a Human ran in March 2022.
    A sensitivity note had its direction reversed. It said treating duplicates as separate
    sessions produces 2.1% for 2021 AI. Deduplicating produces 2.1%; treating them as separate
    produced 4.0%.
    Four date-parsing defects. A length guard rejected valid short dates like "6/1/26"; a
    malformed year ("June 12, 20204") was silently truncated or replaced with the image's upload
    year; an impossible explicit date fell through to the upload year instead of being rejected; and
    the title parser had no calendar validation at all, so "(From 2/30/2026)" parsed. All fixed, with
    no change to any stored date.
  

  Round one
  
    The OCR was running in fast mode, not accurate. The Vision framework defines
    Accurate as 0 and Fast as 1; my code passed 1 with a comment claiming it was accurate. Fast mode
    misread sponsor labels, producing readings like "Spon50r:" that the match then rejected. Re-run
    in accurate mode, the sponsorship figures moved from 83.7% and 63.0% to
    85.9% and 70.7%, and the gap from 20.7 to 15.2 points. Round two's deduplication moved them
    again, to the figures now shown.
    The sponsorship section claimed more than the test could support. It said a rise from
    0.8% to 20.3% "does not come from a 21-point sponsorship gap." That compares a change in
    programming share against a difference in prevalence between two groups, which are not the same
    quantity, and the comparison cannot rule out sponsorship-driven topic selection. Removed.
    The voice-AI figure was withdrawn at 3.8%, then rebuilt in round two. See above.
    One title was attributed to the wrong year. The Human Oversight Imperative: When
    AI Needs Guardrails ran 2025-11-20, and I cited it as 2026 evidence. Worse, framing the
    change as a clean 2026 inversion was wrong on its own terms: Artificial
    Intelligence-Empowering Human Agents for Better Efficiency ran in November 2024. It is a
    shift in emphasis, not a break, and it now reads that way.
    "Portals sat between 1.1% and 2.2% in every year" was false. 2021 is 0 of 50. The
    conclusion that portals never became a theme is unaffected.
    The control chart's screen-reader description was wrong. It said staffing "stays flat
    near 12 percent throughout." The annual share holds a narrow band, but the quarterly
    line ranges from 5.6% to 24.1%. The surrounding claim has also been softened: a flat annual
    control is consistent with the AI rise being real, it does not prove it.
  
  
    Both issues flagged as unresolved in the first round are now fixed. Six pairs of records
    shared a title and date, a session and its promo card both indexed; deduplicating them takes
    2021 AI from 4.0% to 2.1% and the 2024 digital peak from 9.3% to 9.4%, and every figure on this
    page is now event-level. The phone category is still a broad keyword bucket, so its verdict is
    now "not established" rather than "fails."
  

