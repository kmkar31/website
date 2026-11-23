# Critique, 2026-11-23 (HEAD 7c9ec93; no site change since last critique)

Method: ran `python3 tools/check.py . agents/shots` (zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light, index desktop-dark, aerobraking phone-light. Edited no site files. Wix and Google Fonts are unreachable here, so photos are absent (environment limit).

## Sources consulted
WebFetch was blocked again (permission prompt unanswered). WebSearch worked but returns titles and URLs only, so I read no page body. These are pointers, not verified evidence; no finding depends on them:
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html (2.4.11; sticky header must not hide focused elements)
- https://web.dev/articles/fetch-priority (fetchpriority on the LCP image)
- https://www.nngroup.com/videos/ux-portfolios-hiring/ (what hiring managers look for)
Topic variety this cycle: focus visibility under a sticky header, LCP priority, hiring-manager scanning. Local check: `scroll-padding-top:80px` against a header of roughly 58px on desktop, so anchored focus looks safe (not tested by keyboard).

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio; plain copy with real numbers (three weeks to 15 minutes, 99 s, 46 orbits, 500 m). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Desktop dark Home is balanced; paper and ink palette is coherent. Weak: ragged right column (stamps only on 04 to 07); the Fig. 1 plate on row 06 is the only picture on Home.
- SEO: 7/10, unchanged. Unique titles, JSON-LD, absolute og:image, sitemap, robots. Weak: one shared OG card; robots.txt under /website/ is ignored by crawlers (host limit); Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, hard-edged stamps, flat dark theme).
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
No site change since last cycle. None found.

## Ranked findings
1. Major (UX, credibility). Hero gives no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About says 2023 to 2025 and today is 2026-11-23. A recruiter cannot tell whether the degree is finished or whether he is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads on Home, START HERE sits on row 06 (aerobraking, phone screenshot). The snake page has no method or result. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method describes the prior paper (Falcone et al.) in third person and the reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from a Wix URL in header, hero, About and footer. It is the artifact a recruiter wants most. Needs assets/resume.pdf from the owner.
5. Major (performance). Wix image references remain on most project pages, without width/height (CLS risk) and with `fetchpriority="high"` on a third-party host. Outage dependency. Needs local files.
6. Minor (UX). Home blurbs 01, 02, 03, 08, 09 carry no outcome; only 04 to 07 carry a number. The 30-second scan cannot rank rows. Same root as 2 and 3.
7. Minor (consistency). Footer says "one stylesheet, no framework" while fonts load from Google Fonts. Self-host WOFF2 when files exist.
8. Minor (UX). Phone header shows Home, About, Projects and theme toggle only; Resume and LinkedIn appear in hero and footer. Acceptable, but on project pages (phone, aerobraking) the Resume is reachable only at the very bottom.
9. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive, no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on wide screens; Home right column is ragged.
13. Nit (process). Findings 1 to 6 need owner facts and files. Same list for many cycles; the loop is returning no-change cycles. Owner should supply them or pause the loop, and unblock WebFetch.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard shadows, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Struck-through "three weeks" highlight, stamps, numbered rows, filters, press states, 404 joke, per-page JSON-LD, canonical and OG, skip link, one h1 per page, Fig. 1 plates, "More on <tag>" line.

## Verdict
The design is coherent, finished and clearly authored: retro matte, specific copy, no AI tells, clean checks. UX stays at 6 only because of missing owner input: status and dates, a chosen lead project with real method and result, a plain statement of personal contribution on aerobraking, and local copies of the resume and images. More design cycles will return this same list until those arrive.
