# Critique, 2026-11-25 (after designer cycle 200)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light and desktop-dark, snake-robots tablet-light. Read agents/LOG.md tail (cycles 196 to 200), user-critique.md, previous critique. Wix images and Google Fonts are unreachable here, so photos are absent and serifs are fallbacks (environment limit). No site files edited; regenerating agents/shots is a side effect of the required check.

## Sources consulted
Research limit persists: WebFetch for the WCAG page timed out on the permission request ("PROVENANCE_REQUIRED"), so no page was read this cycle. These are cited as the principles the findings rest on, not verified quotes:
- WCAG 2.2, Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (blocked; basis for finding 12)
- WCAG 2.2, Non-text Content 1.1.1: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content (not re-read; cycle 200 fix relates)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls (not re-read; finding 5)
- NN/g, Mobile UX: https://www.nngroup.com/articles/mobile-ux/ (not re-read; findings 1, 2)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Struck-through "three weeks to 15 minutes", stamps, orbit plate, "For the record" ledger are specific. Residual (taste): nine pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Coherent paper and ink system in both themes; Home desktop dark reads as an index. Weak: right column ragged (rows 01 to 03, 08, 09 have no mark); row 06 stacks stamp and tab; the snake page (viewed) is a schematic and two short paragraphs, visibly thinner than the lead position it holds.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, JSON-LD, sitemap, robots.txt. Weak: one shared OG card, Wix images without dimensions, robots.txt under a subpath (host limit). Not verifiable offline.
- UX: 6/10, unchanged. Findings 1 to 4 remain blocked on owner facts.
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, hard borders, hard offset shadows, no blur).
2. Must not look AI-generated: met, AI-tell 2. File has no new notes.

## Regression check
Cycle 200 changed only alt text on aerobraking. No regressions seen. Visible content unchanged.

## Ranked findings
1. Major (UX, credibility). Home subhead says "MS Mechanical Engineering, Carnegie Mellon University" in present tense; About says 2023 to 2025. Today is 2026-11-25. A recruiter cannot tell whether he has graduated or is available. Owner fact needed (for example "Class of 2025" plus current role or availability).
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads list and lede, while "Start here" sits on row 06 (aerobraking). Owner picks the lead, or reorders.
3. Major (content). The snake page, the lead project, shows (tablet-light) a schematic marked "illustrative", a "Why snake robots" paragraph and a lab link. No method, result or number about what he implemented. Lead project with the least evidence. Owner must supply method and result.
4. Major (credibility). Aerobraking Setup and Method describe Falcone et al.'s work in third person, so his contribution on the "Start here" project is unclear. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
5. Major (robustness, performance). Resume PDF and nearly all project images are hotlinked from Wix, with no width/height (CLS risk, outage dependency). Needs assets/resume.pdf and local images from the owner.
6. Minor (UX). Aerobraking has about 1,500 words with no pull-out of what Karthik did. Add a two-line "My part" box once the owner supplies it (ties to 4).
7. Minor (visual). Row 06 on Home desktop stacks stamp, tab and tags in one column beside a plate. Taste; previously declined, noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (testing). Sticky header versus focused elements (WCAG 2.2 Focus Not Obscured) and lightbox focus trap and return are untested by any cycle. The designer says not testable headlessly; it is: Playwright can press Tab repeatedly on aerobraking and compare each focused element's bounding box with the header's. Worth a script in tools/.
13. Nit (taste). Phone header omits Resume (accepted; do not reopen). Home hero shows it.
14. Nit (process). Findings 1 to 5 need owner facts and files; the list has repeated for many cycles. Owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer and dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Filled "Start here" tab as the single inverted mark, legible in dark mode.
- Orbit figure with caption and "Sheet N of 9" plate captions.
- Per-page titles, descriptions, canonical and JSON-LD; prev/next and "More on" links; project filters.
- LCP image priority handling on aerobraking; new equation text alts.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated, and the design work is essentially done. UX stays at 6 because of missing owner input: current status, the lead project (and real content for the snake page that currently leads), what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. The one designer-actionable item is an automated keyboard-focus test for the sticky header and lightbox. Until the owner supplies the rest, further design cycles are polishing a finished surface.
