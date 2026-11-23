# Critique, 2026-11-23 (HEAD a327b28; no site change since the last critique)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL, only "images not loaded" sandbox notes). Viewed index phone-light, index desktop-dark, aerobraking phone-light and about tablet-light. Edited no site files. Wix and Google Fonts are unreachable here, so photos are absent (environment limit).

## Sources consulted
WebFetch of w3.org, web.dev and nngroup.com was blocked this cycle (permission not answered), and WebSearch returned only titles and links. I therefore read no source text, and no finding depends on one. Links surfaced by search, relevant to finding 8 (not read):
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://dequeuniversity.com/rules/axe/4.8/target-size
- https://smashingmagazine.com/2024/07/getting-bottom-minimum-wcag-conformant-interactive-element-size/
Blocked, not read: https://web.dev/articles/optimize-cls and https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/.
Local fact: Wix image references (`grep -c wixstatic`): aerobraking 7, quadrotor-sysid 5, tricycle 4, hasselhoff 4, nanosatellite 4, quadrotor-landing 2, about/argus/projects/raftar/snake 1 each; index and 404 none. Resume link is a Wix (filesusr.com) URL.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is plain with real numbers. Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Paper and ink palette, stamps, numbered rows, flat dark theme. Weak: ragged right column on Home (stamps only on 04 to 07, visible in the desktop screenshot where 01 to 03, 08, 09 have an empty slot); the lead project's page is sparse.
- SEO: 7/10, unchanged. Unique titles, JSON-LD, sitemap, robots, absolute og:image. Weak: shared OG card, robots.txt path (host limit), Wix images without dimensions. Not verifiable offline: indexing and social previews.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
No site change since last cycle. None found.

## Ranked findings
1. Major (UX, credibility). Hero gives no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense, while About says 2023 to 2025 and today is 2026-11-23. A recruiter cannot tell whether he has graduated or is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads on Home, START HERE sits on row 06 (aerobraking). The lead row has the thinnest page (no method or result). Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method (phone-light screenshot) describes Falcone et al.'s work in third person, so the reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from a Wix URL in header, hero, About and footer. It is the artifact a recruiter wants most. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on 11 of 13 pages, without width/height (CLS risk), with `fetchpriority="high"` on a third-party host. Outage dependency. Needs local files.
6. Minor (UX). Home blurbs 01, 02, 03, 08, 09 carry no outcome; only 04 to 07 carry a stamp, so a 30-second scan cannot rank rows. Same root as 2 and 3.
7. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Self-host WOFF2 when files exist.
8. Minor (UX). Phone header has Home, About, Projects and the theme toggle; Resume is only in the hero and footer, so on project pages it is at the very bottom. The designer's no-room reasoning at 360px is acceptable. Taste: do not reopen.
9. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive, no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on wide screens; Home right column is ragged.
13. Nit (process). Findings 1 to 6 need owner facts and files. The same list has repeated for many cycles and the loop returns no-change cycles. Owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard shadows, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Struck-through "three weeks" highlight, stamps, numbered rows, press states, 99 s stamp, 404 joke, per-page JSON-LD, canonical and OG, skip link, one h1 per page, Fig. 1 plates, "More on <tag>" line, "Sheet 6 of 9 · NTS" figure captions.

## Verdict
The design is coherent, finished and clearly authored: retro matte, specific copy, no AI tells, clean checks. UX stays at 6 only because of missing owner input: status and dates, a chosen lead project with real method and result, a plain statement of personal contribution on aerobraking, and local copies of the resume and images. More design cycles will return this list until those arrive. Research this cycle was blocked, so nothing here rests on external sources.
