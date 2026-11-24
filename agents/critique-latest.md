# Critique, 2026-11-24 (HEAD f9e1a62; no site change since the last critique)

Method: ran `python3 tools/check.py` (rc=0, zero FAIL, only "images not loaded" sandbox notes), shots written to scratch. Viewed index phone-light and index desktop-dark. Edited no site files. Wix and Google Fonts are unreachable here, so photos are absent and the serif fonts render as fallbacks (environment limit, not a defect).

## Sources consulted
Research was again mostly blocked. WebFetch of web.dev (optimize-cls) and w3.org (focus-appearance) returned "permission not answered". WebSearch returned titles and links only. I read no source text, so no finding depends on one. Links surfaced, not read:
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (UX portfolios: what hiring managers look for; relevant to findings 1 to 3)
- https://interactions.acm.org/archive/view/november-december-2025/what-should-a-junior-user-experience-designer-have-in-their-portfolio
- https://www.tryexponent.com/courses/product-designer-interview/ux-storytelling-toolkit/how-hiring-managers-evaluate-portfolios
Blocked: https://web.dev/articles/optimize-cls and https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html.
Local facts: `grep -c wixstatic`: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, nanosatellite 4, landing 2, about/argus/projects/raftar/snake 1 each; index and 404 none. Resume link is still a filesusr.com PDF. Title of Home: "Karthik Karumanchi | Control of Robots and Spacecraft".

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Plain copy with real numbers. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink palette, stamps, numbered rows, flat dark theme (desktop-dark shot is coherent). Weak: ragged right column on Home (rows 01 to 03, 08, 09 have an empty slot beside stamped rows); lead project page is sparse.
- SEO: 7/10, unchanged. Unique titles, JSON-LD, sitemap, robots, absolute og:image. Weak: shared OG card, robots path (host limit), Wix images, no verified image dimensions. Indexing and social previews not verifiable offline.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
No site change since the last cycle. None found.

## Ranked findings
1. Major (UX, credibility). Home hero says "MS Mechanical Engineering, Carnegie Mellon University" in the present tense; About says 2023 to 2025; today is 2026-11-24. A recruiter cannot tell whether he has graduated or is available. Owner fact needed (STATUS slot in build.py is empty).
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads Home, "Start here" sits on row 06 (aerobraking, visible in the phone and desktop shots). The row 01 page is the thinnest. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method describes prior work in third person, so what Karthik did is unclear; "46 orbits" has no baseline; Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from a Wix filesusr.com URL in header, hero and footer. It is the artifact a recruiter wants most. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on 11 of 13 pages with no known width/height (CLS risk) and an outage dependency. Needs local files. Source not read (web.dev CLS blocked).
6. Minor (UX). Home rows 01, 02, 03, 08, 09 carry no outcome; only 04 to 07 carry a stamp, so a 30-second scan cannot rank rows. Same root as 2 and 3.
7. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Self-host WOFF2 when files exist.
8. Minor (UX). Phone header omits Resume; on project pages it is only in the footer. Designer's 360 px reasoning is acceptable; taste, do not reopen.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (visual, taste). About leaves its right third empty on wide screens; Home right column is ragged.
13. Nit (process). Findings 1 to 6 need owner facts and files. The same list has repeated for many cycles and the loop returns no-change cycles. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard shadows, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Struck-through "three weeks" highlight, stamps, numbered rows, press states, 99 s stamp, 404 joke, per-page JSON-LD, canonical and OG, skip link, one h1 per page, Fig. 1 plates, "Sheet N of 9" captions.

## Verdict
The design is coherent, finished and clearly authored: retro matte, specific copy, no AI tells, clean checks. UX stays at 6 only because of missing owner input: status and dates, a chosen lead project with real method and result, a plain statement of personal contribution on aerobraking, and local copies of the resume and images. More design cycles will return this list until those arrive. Research was blocked again, so nothing here rests on external sources.
