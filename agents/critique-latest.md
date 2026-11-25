# Critique, 2026-11-25 (after designer cycle 198)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes; it needs about 5 minutes, longer than the default 2-minute tool timeout). Viewed index phone-light and desktop-dark, aerobraking-drl tablet-light. Wix images and Google Fonts are unreachable here, so photos are absent and serifs are fallbacks (environment limit). Edited no site files; regenerating agents/shots is a side effect of the required check.

## Sources consulted
Research limit this cycle: WebFetch permission requests for the three pages below timed out, so none were read. I cite them as the principles the findings rest on, not as verified quotes.
- WCAG 2.2, Focus Not Obscured (Minimum) (sticky header vs focus; not tested this cycle): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (blocked)
- web.dev, Optimize LCP (image priority, third-party origins; basis for finding 5): https://web.dev/articles/optimize-lcp (blocked)
- NN/g, Mobile UX (scanning, front-loading content; basis for finding 7): https://www.nngroup.com/articles/mobile-ux/ (blocked)
- Carried from earlier cycles, not re-read: WCAG 2.2 Target Size (Minimum) https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum ; web.dev Optimize CLS https://web.dev/articles/optimize-cls

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. The struck-through "three weeks to 15 minutes", stamps and the orbit plate are specific. Residual (taste): nine pages share one skeleton. Tells moved: none.
- Looks good: 8/10. Coherent paper and ink system in both themes; Home reads as an index, not a template. Weak: Home desktop right column is ragged (rows 01 to 03, 08, 09 have no mark); row 06 stacks stamp and tab; the aerobraking page is three screens of undifferentiated prose after the figure.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, JSON-LD, sitemap. Weak: one shared OG card, Wix images without dimensions, robots.txt under a subpath (host limit). Not verifiable offline.
- UX: 6/10, unchanged (Major findings 1 to 4 are blocked on owner facts).
- Fun and personality: 7/10, unchanged. No new moment since the "Start here" tab.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, hard borders, hard offset shadows, no blur).
2. Must not look AI-generated: met, AI-tell 2. No new owner notes.

## Regression check
Cycle 198 changed no site content. No regressions seen in the screenshots viewed.

## Ranked findings
1. Major (UX, credibility). Home subhead says "MS Mechanical Engineering, Carnegie Mellon University" in the present tense and About says 2023 to 2025; today is 2026-11-25. A recruiter cannot tell whether he has graduated or is available. Owner fact needed (for example "Class of 2025" plus current role or availability).
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads the list and the lede, while "Start here" sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result, or reorders.
3. Major (credibility). Aerobraking Setup and Method describe Falcone et al.'s work in third person ("the authors required a training time of 1 week on a 50 core cluster"), so Karthik's own contribution on the "Start here" project is unclear. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is still hotlinked from Wix (header, hero, footer). It is the artifact a recruiter most wants. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix images remain on most pages (aerobraking has 7 references, plus about 3 to 10 per other page) with no known width/height: CLS risk and outage dependency. Needs local files and dimensions.
6. Minor (visual). Row 06 on Home desktop stacks stamp, tab and tags in one column beside a plate. Taste; designer declined, so not reopened beyond noting it.
7. Minor (UX, new angle). The aerobraking page puts a labelled "The question" and three stats above the fold, then runs about 1,500 words with no pull-out of what Karthik did. Add a two-line "My part" box under the stats once the owner supplies it (ties to finding 3).
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (UX, taste). Phone header omits Resume (360 px reasoning accepted; do not reopen).
13. Nit (process). Findings 1 to 5 need owner facts and files; the list has repeated for many cycles and the designer has made no content changes in several. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer and dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Filled "Start here" tab as the single inverted mark.
- Orbit figure with caption and "Sheet 6 of 9" on the aerobraking page.
- Per-page titles, descriptions, canonical and JSON-LD; prev/next and "More on space" links on project pages.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated, and the design work is essentially done. What holds UX at 6 is missing owner input: current status, the lead project, what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Until those arrive, further design cycles are polishing a finished surface; the useful next step is the owner's.
