# Critique, 2026-11-26 (after designer cycle 207)

Method: ran `python3 tools/check.py . agents/shots` (finished, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light, index desktop-dark, snake-robots tablet-light. Read LOG.md (through cycle 207), user-critique.md and the previous critique. Cycle 207 changed no site files (log only), so there is nothing new to regress. Wix images and Google Fonts are blocked here, so photos are absent and serifs render as fallbacks (environment limit, not a bug). I counted wixstatic references per page: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, quadrotor-landing 2, one each on about, argus, projects, raftar, snake.

## Sources consulted
Research was limited again. WebFetch calls to web.dev (optimize-cls), MDN (prefers-reduced-motion) and W3C (target-size-minimum) were blocked by a permission timeout, so I read none of them. One WebSearch returned links only. Nothing below is quoted from a source; these are pointers.
- W3C, WCAG 2.2 Understanding Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (search listing only; the site's 44 px targets exceed the 24 px minimum, so no finding)
- web.dev, Optimize CLS: https://web.dev/articles/optimize-cls (blocked; finding 5)
- MDN, prefers-reduced-motion: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion (blocked; not checked this cycle)
- NN/g, UX Design Portfolios: https://nngroup.com/articles/ux-design-portfolios/ (carried from earlier cycles, unread)
Topic this cycle: target size, CLS. Fewer than three sources were actually read, which is a process gap.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Authored touches: struck-through "three weeks to 15 minutes", real-figure stamps, "For the record" ledger, "Fig. 1 / Sheet N of 9" plates. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink system holds in both themes. Desktop dark Home is clean, but the right column of the list is ragged: rows 01 to 03, 08 and 09 carry no mark, and row 06 is the only row with a thumbnail and stacks stamp, tab and tags.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, absolute og:image, JSON-LD, sitemap, robots. Weak: one shared OG card; 31 wixstatic references across 11 pages; robots.txt under a subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and project navigation are easy. The weak points need owner content (findings 1 to 5).
- Fun and personality: 7/10, unchanged. The 99 s stamp, the strike-through and the "Start here" tab remain the memorable moments.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, both themes.
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed in cycle 207. Screenshots match the previous cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead says "MS Mechanical Engineering, Carnegie Mellon University" with no date. About says 2023 to 2025, and today is 2026-11-26. A recruiter cannot tell whether he has graduated, what he does now, or whether he is available. STATUS in build/ is still `""`. Owner fact needed (class year, current role).
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads, but "Start here" sits on row 06 (aerobraking), about two phone screens down. Owner picks the lead, moves the label, or reorders.
3. Major (content). The snake page, the lead project, has the least evidence. At tablet it shows a schematic captioned "Module count is illustrative", a one-sentence "Why snake robots" and a lab link. No method, result or number for what he implemented. Owner must supply these.
4. Major (credibility). Aerobraking quotes "46 orbits to target" with no baseline; its Method text is third person ("Falcone et al. ... Our method"), which hides his own contribution; and Raftar's Ferrari comparison has no source. Owner facts. (Designer already noted the 8.4 km figure is labelled on the page; accepted.)
5. Major (robustness, performance). Resume PDF and nearly all project images are hotlinked from Wix, mostly without width and height (CLS risk, outage dependency). The resume link appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner. Link liveness cannot be verified offline.
6. Minor (UX). Aerobraking is very long with no pull-out of his own part. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven; row 06 stacks stamp, tab and tags. Previously declined; noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Accurate; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card for every page; submitting the sitemap in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for about 15 cycles and no site change can resolve them. The last several cycles were log-only. The owner should supply facts and files, or the loop should pause.

## Fun ideas grounded in the repo (not applied; only if the owner wants them)
- A one-line aside on the Hasselhoff page about how the 99 s clock starts, only if the owner confirms the detail.
- Reuse the hard-shadow press state from "See the projects" on the "Start here" tab.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer, readable dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; 99 s stamp; tightened spec strip.
- Filled "Start here" tab as the single inverted mark.
- Fig. 1 plates with "Sheet N of 9" captions.
- Per-page titles, descriptions, canonical, JSON-LD; prev/next links; "More on" links; project filters.
- LCP image priority on aerobraking; equation text alts; keyboard focus test (tools/focus_check.py).

## Verdict
The site is coherent, plainly written and clearly authored, and does not look generated. Design work is essentially done. UX stays at 6 because of missing owner input: current status and dates, the lead project, real content for the snake page, his own part in aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Research was again below the three-source minimum because page fetches were blocked, so the cited sources are unverified pointers.
