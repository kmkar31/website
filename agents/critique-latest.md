# Critique, 2026-11-23 (HEAD 3bf6664; no site change since cycle 186)

Method: ran `python3 tools/check.py . agents/shots` (background; partial output read: zero FAIL in 40+ lines, only "images not loaded" sandbox notes; the run was still going when I wrote this). Viewed index phone-light, index desktop-dark, aerobraking-drl phone-light. Counted wixstatic/filesusr references per page with grep. Edited no site files. Wix and Google Fonts are unreachable here, so photos are absent (environment limit).

## Sources consulted
WebFetch was blocked for all three pages I tried (permission prompt unanswered), so I did not read them. WebSearch returned a result list only. These are pointers, not evidence; no finding depends on them:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (2.5.8; found via search; the phone screenshots show comfortable targets)
- https://web.dev/articles/optimize-cls (set width/height on images; not fetched)
- https://www.nngroup.com/articles/ux-design-portfolios/ (role and outcome in project work; not fetched)
Topic this cycle: target size (no problem seen) plus carried-over CLS and portfolio content.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Desktop-dark Home is balanced; phone Home is tidy. Weak: right column of Home is ragged (stamps on 04 to 07 only); Fig. 1 plate on row 06 is the lone picture on Home; the aerobraking phone page is a long wall of text with images missing here.
- SEO: 7/10, unchanged. Unique titles, canonical, og:image, sitemap, robots, JSON-LD, one h1. Weak: single shared OG card; robots.txt under /website/ (host limit); Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper and ink tones, hard shadow, flat dark theme in screenshots).
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
No site change since the last critique ("More on <tag>" label). Visible at the bottom of the aerobraking phone page as "MORE ON SPACE ARGUS Mission" above the pager; reads as a topical link. No regression.

## Ranked findings
1. Major (UX, credibility). No status or dates in the hero. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About gives 2023 to 2025; today is 2026-11-23. Recruiter cannot tell availability or whether the degree is finished. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, START HERE sits on row 06 (aerobraking), on every viewport. Snake page has no method or result. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method is third person about prior work ("the authors") and Result switches to "our"; the reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut. New observation: the 46-orbit result appears three times on the aerobraking page (lede, stat strip, Result) while his own contribution appears zero times; repeat less, attribute once.
4. Major (robustness). Resume PDF is hotlinked from a Wix filesusr.com URL (header, hero, About, footer, 404). It is the one artifact a recruiter wants. Needs assets/resume.pdf from the owner.
5. Major (performance, robustness). Wix references remain on every page (grep counts: aerobraking 9, sysid 7, tricycle 6, Hasselhoff 6, tethered 6, about 4, landing 4, argus 3, index 3, projects 3, raftar 3, snake 3, 404 2; these include resume links). Images lack width/height, a CLS risk (web.dev link above) and an outage dependency. Needs local files. Also `fetchpriority="high"` on the first aerobraking Wix image is a bet on a third-party host.
6. Minor (UX). Home blurbs 01, 02, 03, 08 give no outcome; only 04 to 07 carry a number. A 30-second scan cannot rank the rows. Same root as 2 and 3.
7. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
8. Minor (visual, taste). Ragged right column on Home and the lone plate on row 06.
9. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive, no subheads. Owner call.
11. Minor (UX). Contact is LinkedIn only (footer says so). Owner constraint. Phone header drops Resume, LinkedIn and GitHub icons; they appear in hero and footer.
12. Nit (visual, taste). About leaves the right third empty on wide screens.
13. Nit (process). Findings 1 to 6 need owner facts and files; this is the same list as many cycles ago. The owner should supply them or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Struck-through "three weeks" highlight, stamps, numbered rows, filters, press states, 404 joke, per-page JSON-LD, canonical and OG, skip link, one h1 per page, Fig. 1 plates, the "More on <tag>" line.

## Verdict
The design is coherent and finished: retro matte, specific copy, no AI tells, clean checks. UX stays at 6 because of missing owner input: status and dates, a chosen lead project with real method and result, a plain statement of personal contribution on aerobraking, and local copies of the resume and images. Until those arrive, more design cycles will return the same list.
