# Critique, 2026-11-24 (HEAD 8c8005f; no site change since the last critique)

Method: ran `python3 tools/check.py . <scratch>/shots` (rc 0 in background, zero FAIL, only "images not loaded" sandbox notes; shots went to scratch because writing agents/shots would edit a non-critique file and the run exceeds the 2 min tool limit in the foreground). Viewed index phone-light, index desktop-light, aerobraking-drl phone-dark. Edited no site files. Wix and Google Fonts are unreachable here, so photos are absent and the serifs render as fallbacks (environment limit).

## Sources consulted
Research was blocked again. WebFetch of https://web.dev/articles/optimize-cls and https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html returned "permission not answered" and I did not retry. I read no source text, so no finding depends on one. This misses the three-source rule; it is an environment limit. Unread, for a cycle that can fetch:
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (findings 1 to 3)
- https://web.dev/articles/optimize-cls (finding 5)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (finding 8)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. The struck-through "three weeks" on a highlighter is specific. Residual (taste): nine project pages share one skeleton; the "Fig. 1" plate appears once. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink palette, stamps, numbered rows, flat dark theme. Weak: Home's right column is ragged (rows 01 to 03, 08, 09 have no stamp); on phone the Fig. 1 plate sits tight under the Hasselhoff rule.
- SEO: 7/10, unchanged. Unique titles, descriptions, one h1, canonical, JSON-LD, sitemap, robots, absolute og:image. Weak: one shared OG card, Wix images with unknown dimensions, robots.txt under a subpath (host limit). Indexing and previews are not verifiable offline.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Highlighter strike, stamps and the 99 s press-and-hold are earned. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
No site change since the last cycle. No regression found. Phone and desktop Home render cleanly; the aerobraking page in dark is readable, with the equation block and result figures intact.

## Ranked findings
1. Major (UX, credibility). Home says "MS Mechanical Engineering, Carnegie Mellon University" in the present tense; About says 2023 to 2025; today is 2026-11-24. A recruiter cannot tell whether he has graduated or is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads Home while "Start here" sits on row 06 (aerobraking). The Projects page shows no "Start here", so the signal disagrees across pages. Row 01's page is the thinnest. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method describes Falcone et al.'s work in third person, so Karthik's contribution is unclear; "46 orbits" has no baseline; Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from a Wix filesusr.com URL in header, hero and footer. It is the artifact a recruiter wants most. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on most pages with no known width/height (CLS risk) and an outage dependency. Needs local files.
6. Minor (UX). Only rows 04 to 07 carry a stamp, so a 30-second scan cannot rank the other rows. Same root as 2 and 3.
7. Minor (consistency). The footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
8. Minor (UX). The phone header omits Resume; on project pages it is only in the footer. The 360 px reasoning is acceptable; taste, do not reopen.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). The tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (visual, taste). About leaves its right third empty on wide screens; Home's right column is ragged.
13. Nit (process). Findings 1 to 5 need owner facts and files. The same list has repeated for about ten cycles and the loop returns no-change cycles. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark theme.
- Specific copy with real numbers; the plain "For the record" ledger; the struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Per-page titles, descriptions, canonical and JSON-LD; "More on <tag>" related link; prev/next on project pages.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated. What holds it back is missing owner input: current status, the lead project, what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Until those arrive, design cycles have almost nothing to improve and UX stays at 6.
