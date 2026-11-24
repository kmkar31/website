# Critique, 2026-11-24 (HEAD f9f05e5; no site file changed since the last critique)

Method: ran `python3 tools/check.py . <scratch>/shots` in the background (zero FAIL; only "images not loaded" sandbox notes; shots went to scratch so no non-critique file was edited). Viewed index phone-light and projects desktop-light; the other screenshots were not re-viewed because no site file changed. Edited no site files. Wix and Google Fonts are unreachable here, so photos are absent and serifs are fallbacks (environment limit).

## Sources consulted
- WebSearch surfaced https://www.nngroup.com/videos/ux-portfolios-hiring/ (NN/g, what hiring managers look for). Only the result listing was available, no page text, so no finding depends on it beyond the general point that reviewers scan fast.
- WebFetch of https://web.dev/articles/optimize-cls was blocked ("permission not answered"); not retried. Finding 5 rests on the long-standing web.dev guidance to set width/height on images, which I could not re-read this cycle.
- This misses the three-source rule; it is an environment limit. Unread, for a cycle that can fetch: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html and https://web.dev/articles/optimize-cls.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. The struck-through "three weeks" on a highlighter is specific. Residual (taste): nine project pages share one skeleton; the Fig. 1 plate appears once. Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink palette, stamps, numbered rows, flat dark footer. Weak: Home's right column is ragged (rows 01 to 03, 08, 09 have no stamp); on phone the Fig. 1 plate sits tight under the Hasselhoff row.
- SEO: 7/10, unchanged. Unique titles and descriptions, one h1, canonical, JSON-LD, sitemap, robots, absolute og:image. Weak: one shared OG card, Wix images without dimensions, robots.txt under a subpath (host limit). Indexing and previews not verifiable offline.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Highlighter strike, stamps and the 99 s press-and-hold are earned. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
No site change since the last cycle (last three commits touch only logs). No regression. Confirmed in the shots: phone Home has primary button and Resume/LinkedIn above the fold; Projects desktop is clean and consistent.

## Ranked findings
1. Major (UX, credibility). Home and the meta description say "MS Mechanical Engineering at Carnegie Mellon" in the present tense; About says 2023 to 2025; today is 2026-11-24. A recruiter cannot tell whether he has graduated or is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads Home while "Start here" sits on row 06 (aerobraking). Verified: "Start here" appears in index.html and not in projects.html, so the Projects page gives no signal at all. Row 01's page is the thinnest. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method describes Falcone et al.'s work in third person, so Karthik's contribution is unclear; "46 orbits" has no baseline; Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). The resume PDF is hotlinked from a Wix filesusr.com URL in header, hero and footer. It is the artifact a recruiter wants most. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on most pages with no known width/height (CLS risk) and an outage dependency. Needs local files.
6. Minor (UX). Only rows 04 to 07 carry a stamp, so a 30-second scan cannot rank the other rows. Same root as 2 and 3.
7. Minor (consistency). The footer says "one stylesheet, no framework" while fonts load from Google Fonts; self-host WOFF2 when files exist.
8. Minor (UX, taste). The phone header omits Resume; on project pages it is only in the footer. The 360 px reasoning is acceptable; do not reopen.
9. Minor (SEO). Shared OG card; robots.txt at a project subpath is a host limit. Owner action: submit the sitemap in Search Console.
10. Minor (content). The tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (visual, taste). About leaves its right third empty on wide screens; Home's right column is ragged.
13. Nit (process). Findings 1 to 5 need owner facts and files. The same list has repeated for over ten cycles and the loop returns no-change cycles. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard offset shadows, flat dark footer and theme.
- Specific copy with real numbers; the plain "For the record" ledger; the struck-through "three weeks to 15 minutes".
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Stamps tied to real figures; 99 s press-and-hold on the Hasselhoff page.
- Per-page titles, descriptions, canonical and JSON-LD; "More on <tag>" related link; prev/next on project pages.

## Verdict
The site is coherent, plainly written and clearly authored; it does not look generated. What holds it back is missing owner input: current status, the lead project (and a consistent "Start here" signal on Projects), what he personally did on aerobraking, a sourced Ferrari claim, a local resume.pdf and local images. Until those arrive, design cycles have almost nothing to improve and UX stays at 6.
