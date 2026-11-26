# Critique, 2026-11-26 (after designer cycle 209)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes; it needs about 4 minutes). Viewed index phone-light, index desktop-light, aerobraking phone-dark and about tablet-light. Read LOG.md (through cycle 209), user-critique.md (unchanged, two notes from 2026-10-22) and the previous critique. Cycles 206 to 209 changed no site files (HEAD is log-only commits), so nothing new can have regressed. Wix images and Google Fonts are blocked in the sandbox, so photos are absent and serifs render as fallbacks (environment limit, not a bug). Repo grep of wixstatic references per page: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, quadrotor-landing 2, one each on about, argus, projects, raftar, snake; index and 404 none. Counts of `<img>` tags lacking a `width=` attribute (single-line grep, approximate): aerobraking 10, tricycle 9, sysid 9, hasselhoff 7, tethered 5, snake 4, landing 3, raftar 3, argus 2, about 1.

## Sources consulted
Direct fetches (WebFetch) of W3C WCAG 2.2 Target Size (Minimum), web.dev Optimize CLS and NN/g mobile UX all failed again with a permission timeout this cycle. I read none of them and quote nothing. This is below the three-source minimum; I am saying so rather than implying otherwise. Pointers (unread, from earlier cycles' listings):
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
- https://web.dev/articles/optimize-cls (blocked; relevant to finding 5)
- https://www.nngroup.com/articles/mobile-ux/ (blocked)
Topic this cycle: tap targets, CLS, mobile scanning.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Home is a plain ruled list with a "For the record" ledger. Authored touches: struck-through "three weeks to 15 minutes", figure stamps, "Fig. 1" plate. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink system is coherent in both themes (viewed). Desktop right column is ragged: rows 01 to 03, 08 and 09 carry no mark, while row 06 stacks stamp, "Start here" tab and tags beside the only thumbnail. Only one project in nine shows any image on Home. Aerobraking phone-dark is a long text column with one plate; the sandbox cannot show its photos.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, absolute og:image (https://kmkar31.github.io/website/assets/og.png), twitter card, sitemap, robots. Weak: one shared OG card for all pages; sitemap lastmod values are uneven (several dates, differing from real change dates after log-only cycles, harmless); lead project hotlinks images; robots.txt under a project-site subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and project navigation are easy; the gaps all need owner content (findings 1 to 5).
- Fun and personality: 7/10, unchanged. Strike-through, 99 s stamp and "Start here" tab remain the memorable moments.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Flat paper, ink borders, hard offset shadows, no blur, both themes (viewed).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed since the last critique. Screenshots match. check.py and (per LOG) focus_check pass. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead reads "MS Mechanical Engineering, Carnegie Mellon University" with no dates and no status. About says 2023 to 2025; today is 2026-11-26. A recruiter cannot tell if he has graduated, what he does now, or whether he is available. STATUS in build/ is empty. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead, moves the label, or reorders.
3. Major (content). The snake page, the lead project, has the thinnest evidence: an illustrative schematic, a short "Why snake robots" and a lab link; no method, result or number for what he implemented. Owner must supply.
4. Major (credibility). Aerobraking's headline "46 orbits to target" has no baseline; its Method is third person ("Falcone et al. ... Our method"), which hides his own contribution; Raftar's Ferrari comparison has no source. Owner facts.
5. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix, and most project-page `<img>` tags have no width/height (approximate grep above), so they can shift layout on load (CLS risk; web.dev source blocked, so this is from general knowledge, not a quote). Resume link appears in header, hero, About and footer, so one dead link breaks four entries. Needs assets/resume.pdf and local images from the owner. Link liveness cannot be verified offline. If the owner supplies files, add dimensions in the same change.
6. Minor (UX). Aerobraking is very long (about 9000 px tall on phone) with no pull-out of his own part. Add a two-line "My part" box after finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
8. Minor (consistency). Footer says "one stylesheet, no framework" and names DM Serif Display and Source Serif 4, but fonts load from Google Fonts. Accurate; self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; sitemap submission in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for about 16 cycles and no site change can resolve them; the last four cycles were log-only. The owner should supply facts and files, or the loop should pause. The sticky-header focus item from the last critique is closed (scroll-padding-top plus focus_check passes, per LOG).

## Fun ideas grounded in the repo (not applied; only if the owner wants them)
- A one-line aside on the Hasselhoff page about how the 99 s clock starts, only if the owner confirms the detail.
- Reuse the hard-shadow press state from "See the projects" on the "Start here" tab.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer, readable dark theme.
- Specific copy with real numbers; "For the record" ledger; struck-through "three weeks to 15 minutes".
- Mobile Home: compact one-row header, primary button and Resume/LinkedIn above the fold, comfortable measure, 44 px targets.
- Stamps tied to real figures; the 99 s stamp; filled "Start here" tab as the single inverted mark.
- Fig. 1 plates with "Sheet N of 9" captions.
- Per-page titles, descriptions, canonical, JSON-LD; prev/next and "More on" links; project filters; absolute og:image.
- LCP image priority on aerobraking; equation text alts; reduced-motion rule; tools/focus_check.py.
- About page: plain, dated, specific Education and Experience entries.

## Verdict
The site is coherent, plainly written and clearly authored, and does not look generated. Design work is essentially done. UX stays at 6 because of missing owner input: current status and dates, the lead project, real content for the snake page, his own part in aerobraking, a sourced Ferrari claim, a local resume.pdf and local, dimensioned images. No new site-actionable defect turned up this cycle. Research was below the three-source minimum because page fetches were blocked, so the cited sources are unverified pointers.
