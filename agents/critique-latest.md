# Critique, 2026-11-26 (after designer cycle 208)

Method: ran `python3 tools/check.py . agents/shots` (finished, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light, desktop-light and tablet-dark. Read LOG.md (through cycle 208), user-critique.md (unchanged, two notes from 2026-10-22) and the previous critique. Cycles 206 to 208 changed no site files, so nothing new can have regressed. Wix images and Google Fonts are blocked in the sandbox, so photos are absent and serifs render as fallbacks (environment limit, not a bug). wixstatic references per page (grep): aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, quadrotor-landing 2, one each on about, projects, raftar, snake, argus; index and 404 none. The resume link points to a Wix filesusr.com PDF.

## Sources consulted
Direct page fetches (WebFetch) were blocked by a permission timeout again for W3C, web.dev and MDN, so I did not read those pages. WebSearch returned result listings only. Nothing below is quoted from a source; these are pointers that surfaced in searches. This is below the three-source minimum, as in earlier cycles, and I am saying so rather than implying otherwise.
- W3C, WCAG 2.2 Understanding Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (listing only; relevant to the sticky header, topic not yet covered; not checked in a browser this cycle)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (listing only; finding 5)
- web.dev, Key performance issues with images: https://web.dev/learn/images/performance-issues (listing only)
- Nielsen Norman Group, UX Portfolios: What Hiring Managers Look For: https://www.nngroup.com/videos/ux-portfolios-hiring/ (listing only; findings 1 to 4)
Topic this cycle: focus visibility under a sticky header, CLS, hiring-manager scanning.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. The home is a plain ruled list with a ledger sidebar. Authored touches: struck-through "three weeks to 15 minutes", real-figure stamps, "For the record", "Fig. 1" plate. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink system is coherent in both themes (viewed). Desktop right column is ragged: rows 01 to 03, 08 and 09 carry no mark, while row 06 stacks stamp, "Start here" tab and tags beside the only thumbnail. The tablet-dark thumbnail is small and floats left of a wrapped title with an uneven gap.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, absolute 1200x630 og:image with alt, twitter card, sitemap, robots. Weak: one shared OG card for every page; the lead project page hotlinks its images; robots.txt under a project subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and project navigation are easy. The weak points need owner content (findings 1 to 5).
- Fun and personality: 7/10, unchanged. The strike-through, the 99 s stamp and the "Start here" tab are the memorable moments.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, both themes (viewed).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed in cycles 206 to 208. Screenshots match the previous cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead reads "MS Mechanical Engineering, Carnegie Mellon University" with no dates and no current status. About gives 2023 to 2025, and today is 2026-11-26. A recruiter cannot tell whether he has graduated, what he does now, or whether he is available. STATUS in build/ is still empty. Owner fact needed (class year, current role or availability).
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads the list, but "Start here" is on row 06 (aerobraking), about two phone screens down (seen in the phone screenshot). Owner picks the lead, moves the label, or reorders.
3. Major (content). The snake page, the lead project, has the least evidence: a schematic captioned "Module count is illustrative", a one-sentence "Why snake robots" and a lab link. No method, result or number for what he implemented. Owner must supply these.
4. Major (credibility). Aerobraking quotes "46 orbits to target" with no baseline; its Method text is third person ("Falcone et al. ... Our method"), which hides his own contribution; Raftar's Ferrari comparison has no source. Owner facts. The designer's point that 46 orbits and 8.4 km are both labelled on the page is accepted; the baseline and attribution remain open.
5. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix. Verified in the repo: the snake page hero `<img>` (fetchpriority=high) has no width or height, and the others on that page have none either, so they can shift layout when they load (CLS risk, per web.dev; page not read). The resume link appears in header, hero and footer, so one dead link breaks three entries. Needs assets/resume.pdf and local images from the owner. Link liveness cannot be verified offline.
6. Minor (UX). Aerobraking is very long with no pull-out of his own part. Add a two-line "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Accurate; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card for every page; submitting the sitemap in Search Console is an owner action.
10. Minor (accessibility, unverified). The header is sticky; WCAG 2.2 Focus Not Obscured (Minimum) asks that a focused control not be fully hidden by author content. tools/focus_check.py exists, but I did not confirm it scrolls focused links under the sticky bar. Check with scroll-padding-top on html and a test that tabs through a long page (aerobraking).
11. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
12. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
13. Nit (process). Findings 1 to 5 have repeated for about 15 cycles and no site change can resolve them. The last three cycles were log-only. The owner should supply facts and files, or the loop should pause.

## Fun ideas grounded in the repo (not applied; only if the owner wants them)
- A one-line aside on the Hasselhoff page about how the 99 s clock starts, only if the owner confirms the detail.
- Reuse the hard-shadow press state from "See the projects" on the "Start here" tab.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer, readable dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; the 99 s stamp; the tightened spec strip.
- Filled "Start here" tab as the single inverted mark.
- Fig. 1 plates with "Sheet N of 9" captions.
- Per-page titles, descriptions, canonical, JSON-LD; prev/next links; "More on" links; project filters; absolute og:image with dimensions and alt.
- LCP image priority on aerobraking; equation text alts; reduced-motion rule; keyboard focus test (tools/focus_check.py).

## Verdict
The site is coherent, plainly written and clearly authored, and does not look generated. Design work is essentially done. UX stays at 6 because of missing owner input: current status and dates, the lead project, real content for the snake page, his own part in aerobraking, a sourced Ferrari claim, a local resume.pdf and local, dimensioned images. The one thing I can add that a designer could act on without owner facts is finding 10 (sticky header versus focus), which needs checking. Research was below the three-source minimum because page fetches were blocked, so the cited sources are unverified pointers.
