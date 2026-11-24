# Critique, 2026-11-24 (HEAD 72417c6; no site change since the last critique)

Method: ran `python3 tools/check.py` (rc=0, zero FAIL, only "images not loaded" sandbox notes; first attempt into agents/shots timed out at the tool limit, rerun wrote shots to scratch). Viewed index phone-light, index desktop-light, projects tablet-dark. Edited no site files. Grepped titles, descriptions, h1 counts, canonical, JSON-LD, sitemap, robots, og:image across all pages. Wix and Google Fonts are unreachable here, so photos are absent and serif fonts render as fallbacks (environment limit).

## Sources consulted
Research was blocked again this cycle: web fetches of web.dev and w3.org were refused in earlier cycles and I did not retry. I did not read any source text, so no finding depends on one. This misses the "three sources" rule; it is an environment limit, not a choice. Links worth reading next cycle, none read:
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (what hiring managers look for; findings 1 to 3)
- https://web.dev/articles/optimize-cls (explicit image dimensions; finding 5)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (target size; finding 8)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. The struck-through "three weeks" with a highlighter is specific and human. Residual (taste): nine project pages share one skeleton; the "Fig. 1" plate appears once. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink palette, stamps, numbered rows, flat dark theme. Weak: the right column on Home is ragged (rows 01 to 03, 08, 09 carry no stamp); on phone the Fig. 1 plate sits tight under the Hasselhoff rule and above row 06's title, breaking the otherwise even rhythm.
- SEO: 7/10, unchanged. All 12 pages have unique titles, 119 to 156 char descriptions, one h1, canonical, JSON-LD (404 has none, correct). Sitemap and robots present, og:image is absolute. Weak: one shared OG card, robots.txt under a project subpath (host limit), Wix images, unverified image dimensions. Indexing and previews are not verifiable offline.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Highlighter strike, stamps, 99 s press-and-hold are earned. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Must not look AI-generated: met, AI-tell 2.
Note: the file also contains designer response blocks appended below the owner's two lines. The owner notes are unchanged and nothing new was asked.

## Regression check
No site change since the last cycle. No regression found.

## Ranked findings
1. Major (UX, credibility). Home hero says "MS Mechanical Engineering, Carnegie Mellon University" in the present tense; About says 2023 to 2025; today is 2026-11-24. A recruiter cannot tell whether he has graduated or is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads Home, "Start here" sits on row 06 (aerobraking). The Projects page shows no "Start here" at all, so the signal also disagrees between pages. The row 01 page is the thinnest. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method describes prior work in third person, so Karthik's own contribution is unclear; "46 orbits" has no baseline; Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from a Wix filesusr.com URL in header, hero and footer. It is the artifact a recruiter wants most. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on 11 of 13 pages (about 100 tags in total) with no known width/height (CLS risk) and an outage dependency. Needs local files.
6. Minor (UX). Only rows 04 to 07 carry a stamp, so a 30-second scan cannot rank rows 01 to 03, 08, 09. Same root as 2 and 3.
7. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts; fine claim, but self-host WOFF2 when files exist.
8. Minor (UX). Phone header omits Resume (only Home, About, Projects and theme toggle); on project pages Resume is only in the footer. The 360 px reasoning is acceptable; taste, do not reopen.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only ("message me on LinkedIn"). Owner constraint.
12. Nit (visual, taste). About leaves its right third empty on wide screens; Home right column is ragged; Fig. 1 plate crowds the row above on phone.
13. Nit (process). Findings 1 to 5 need owner facts and files. The same list has repeated for about ten cycles and the loop returns no-change cycles. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark theme.
- Specific copy with real numbers; the plain "For the record" ledger; the struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Per-page titles, descriptions, canonical and JSON-LD; "More on <tag>" related link.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated. What holds it back is not design but missing owner inputs: current status, the lead project, what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Until those arrive, further design cycles have almost nothing to improve, and UX stays at 6.
