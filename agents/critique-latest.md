# Critique, 2026-11-25 (after designer cycle 199)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light and desktop-light, projects phone-dark, about tablet-light. Read agents/LOG.md tail, user-critique.md, and grepped the HTML for images, resume links and focus styles. Wix images and Google Fonts are unreachable here, so photos are absent and serifs are fallbacks (environment limit). No site files edited; regenerating agents/shots is a side effect of the required check.

## Sources consulted
Research limit again this cycle: all three WebFetch permission requests timed out, so none were read. They are cited as the principles the findings rest on, not as verified quotes. Blocked URLs:
- WCAG 2.2, Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (blocked; sticky header vs focus, still untested)
- web.dev, Optimize LCP: https://web.dev/articles/optimize-lcp (blocked; basis for finding 5)
- NN/g, Mobile UX: https://www.nngroup.com/articles/mobile-ux/ (blocked; basis for findings 2 and 7)
- Carried from earlier cycles, not re-read: WCAG 2.2 Target Size (Minimum) https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum ; web.dev Optimize CLS https://web.dev/articles/optimize-cls ; WCAG 1.1.1 Non-text Content https://www.w3.org/WAI/WCAG22/Understanding/non-text-content (basis for the new finding 6, not re-read)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Struck-through "three weeks to 15 minutes", stamps, the orbit plate and the "For the record" ledger are specific. Residual (taste): nine pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Coherent paper and ink system in both themes. Home desktop reads as an index. Weak: the right-hand column is ragged (rows 01 to 03, 08, 09 have no mark); row 06 stacks stamp and tab; About is a long single column of uniform rows.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, JSON-LD, sitemap, robots.txt. Weak: one shared OG card, Wix images without dimensions, robots.txt under a subpath (host limit). Not verifiable offline.
- UX: 6/10, unchanged. Findings 1 to 4 are blocked on owner facts.
- Fun and personality: 7/10, unchanged. No new moment since the "Start here" tab.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, hard borders, hard offset shadows, no blur).
2. Must not look AI-generated: met, AI-tell 2. File has no new notes; the line "13 process note: agreed; loop is blocked on owner input" is a leftover reply, not an instruction, and still means the owner has not supplied facts.

## Regression check
Cycle 199 changed no site content (sitemap lastmod churn reverted). No regressions seen in the screenshots viewed.

## Ranked findings
1. Major (UX, credibility). Home subhead says "MS Mechanical Engineering, Carnegie Mellon University" in the present tense; About says 2023 to 2025. Today is 2026-11-25. A recruiter cannot tell whether he has graduated or is available. Owner fact needed (for example "Class of 2025" plus current role or availability).
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads the list and the lede, while "Start here" sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result, or reorders. NN/g mobile guidance on front-loading applies (not read).
3. Major (credibility). Aerobraking Setup and Method describe Falcone et al.'s work in third person, so his own contribution on the "Start here" project is unclear. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is still hotlinked from Wix (header, hero, footer, About). It is the artifact a recruiter most wants. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix images remain on most pages (grep counts: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, others 1 to 2) with no width/height: CLS risk and outage dependency. The first aerobraking figure does carry fetchpriority="high" and the rest are lazy, which is correct. Needs local files and dimensions.
6. Minor (accessibility, new angle). On aerobraking, figures that are equations or plots carry short alts ("Continuous reward function definition", "Terminal reward function formulation", "PPO agent action selection frequency") and several have no caption. A screen-reader user and a search engine get the label, not the content. Add one-sentence text equivalents or captions stating what each shows (WCAG 1.1.1). The captions for the validation plot and action-use plot are a good model.
7. Minor (UX). Aerobraking runs about 1,500 words after the stats with no pull-out of what Karthik did. Add a two-line "My part" box once the owner supplies it (ties to finding 3).
8. Minor (visual). Row 06 on Home desktop stacks stamp, tab and tags in one column beside a plate. Taste; designer declined, noted only.
9. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
10. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
11. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
12. Nit (UX). Contact is LinkedIn only. Owner constraint.
13. Nit (UX, taste). Phone header omits Resume (360 px reasoning accepted; do not reopen). The Home hero does show it.
14. Nit (testing). Sticky header versus focused elements (WCAG 2.2 Focus Not Obscured) and lightbox focus trap and return have still not been tested by any cycle; the :focus-visible outline is 3px with offset, which is good. Test with Tab and Shift+Tab on aerobraking.
15. Nit (process). Findings 1 to 5 need owner facts and files; the list has repeated for many cycles and the designer has made no content changes in most. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer and dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Filled "Start here" tab as the single inverted mark, legible in dark mode.
- Orbit figure with caption and "Sheet 6 of 9" on the aerobraking page.
- Per-page titles, descriptions, canonical and JSON-LD; prev/next and "More on space" links; project filters on Projects.
- LCP image priority handling on aerobraking (fetchpriority high on first figure, lazy after).

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated, and the design work is essentially done. What holds UX at 6 is missing owner input: current status, the lead project, what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. The one new, designer-actionable item is text equivalents for the equation and plot images on aerobraking. Until the owner supplies the rest, further design cycles are polishing a finished surface.
