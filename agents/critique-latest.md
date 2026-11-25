# Critique, 2026-11-25 (after designer cycle 201)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light and desktop-light, quadrotor-landing phone-dark. Read agents/LOG.md tail (cycles 190 to 201), user-critique.md and the previous critique. Wix images and Google Fonts are unreachable here, so photos are absent and serifs are fallbacks (environment limit). No site files edited; regenerating agents/shots is a side effect of the required check.

## Sources consulted
Research limit persists: WebFetch on w3.org timed out on the permission request (PROVENANCE_REQUIRED) this cycle too, so no page was read. These are the principles the findings rest on, not verified quotes:
- WCAG 2.2, Target Size (Minimum) 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (fetch blocked; phone 44 px targets look fine in shots)
- WCAG 2.2, Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (cycle 201 added tools/focus_check.py; finding closed)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls (finding 5)
- NN/g, Mobile UX: https://www.nngroup.com/articles/mobile-ux/ (findings 1, 2)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Struck-through "three weeks to 15 minutes", stamps, orbit plate, "For the record" ledger are specific. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink system is coherent in both themes; Home desktop reads as an index. Weak: Home right column is ragged (rows 01 to 03, 08, 09 carry no mark); row 06 stacks stamp and tab; on phone the "Start here" row is the sixth of nine, below the fold of two screens.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, JSON-LD, sitemap, robots.txt. Weak: one shared OG card, Wix images without dimensions, robots.txt under a subpath (host limit). Not verifiable offline.
- UX: 6/10, unchanged. Findings 1 to 5 remain blocked on owner facts.
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, hard borders, hard offset shadows, no blur, subtle grain).
2. Must not look AI-generated: met, AI-tell 2. The file has no new notes.

## Regression check
Cycle 201 added only tools/focus_check.py; no site file changed. No regressions seen in the shots.

## Ranked findings
1. Major (UX, credibility). Home subhead reads "MS Mechanical Engineering, Carnegie Mellon University" in present tense; About says 2023 to 2025. Today is 2026-11-25. A recruiter cannot tell if he has graduated or is available. Owner fact needed (for example "Class of 2025" plus current role or availability).
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads the list and the hero lede, while "Start here" sits on row 06 (aerobraking). On phone, a skimmer sees the snake row first and the tab only after about two screens. Owner picks the lead, or reorders.
3. Major (content). The snake page, the lead project, offers a schematic marked "illustrative", a "Why snake robots" paragraph and a lab link. No method, result or number about what he implemented. Lead project with the least evidence. Owner must supply method and result.
4. Major (credibility). Aerobraking Setup and Method describe Falcone et al.'s work in third person, so his contribution on the "Start here" project is unclear. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
5. Major (robustness, performance). Resume PDF and nearly all project images are hotlinked from Wix, with no width/height (CLS risk, outage dependency). The Resume link appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner.
6. Minor (UX). Aerobraking has about 1,500 words with no pull-out of what Karthik did. A two-line "My part" box once the owner supplies it (ties to 4).
7. Minor (visual). Row 06 on Home desktop stacks stamp, tab and tags in one column beside a plate. Taste; previously declined, noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (process). Findings 1 to 5 need owner facts and files; the list has repeated for 12+ cycles with no site change. Owner should supply them or pause the loop. (The earlier focus-testing finding is resolved by tools/focus_check.py; not reopened.)

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer and dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Filled "Start here" tab as the single inverted mark, legible in dark mode.
- Orbit figure with caption and "Sheet N of 9" plate captions (quadrotor page figure with real numbers reads well on phone dark).
- Per-page titles, descriptions, canonical and JSON-LD; prev/next and "More on" links; project filters.
- LCP image priority on aerobraking; equation text alts; keyboard focus test.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated, and the design work is essentially done. UX stays at 6 because of missing owner input: current status, the lead project (and real content for the snake page that currently leads), what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Until the owner supplies those, further design cycles are polishing a finished surface.
