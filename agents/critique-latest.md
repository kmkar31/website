# Critique, 2026-11-23 (HEAD 97586c8; one content trim since last critique)

Method: ran `python3 tools/check.py` into a scratch directory (not agents/shots, to leave the repo untouched; slow, about 3 minutes; zero FAIL in every line read, only "images not loaded" sandbox notes; run was still finishing the desktop pass when I wrote this). Viewed index phone-light, desktop-light and tablet-dark. Grepped titles, JSON-LD, og:image, robots, Wix references. Edited no site files. Wix and Google Fonts are unreachable here, so photos are absent (environment limit).

## Sources consulted
WebFetch was blocked again this cycle (permission prompt unanswered) for all three pages. I read none of them. They are pointers only; no finding depends on them:
- https://web.dev/articles/optimize-cls (explicit image width/height to reserve space; not fetched)
- https://www.nngroup.com/articles/ux-design-portfolios/ (state your role and outcome per project; not fetched)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (2.5.8; not fetched)
Because research is blocked, the topic variety requirement is not met this cycle. Owner action: allow WebFetch for these domains or the loop cannot cite sources.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Specific copy (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether, "For the record"). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Desktop-light and tablet-dark Home are balanced, hierarchy is clear, the paper and ink palette is coherent. Weak: ragged right column (stamps only on 04 to 07); the Fig. 1 plate on row 06 is the lone picture; text-only list reads austere when Wix photos fail.
- SEO: 7/10, unchanged. Unique titles, one JSON-LD block per page, absolute og:image, sitemap, robots. Weak: one shared OG card; robots.txt under /website/ is ignored by crawlers (host limit); Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper and ink tones, hard shadows, flat dark theme).
2. Must not look AI-generated: met, AI-tell 2.
No new owner notes.

## Regression check
Last change removed the repeated "To conclude" paragraph on the aerobraking page. No regression visible; the result is still stated in lede, stat strip and caption.

## Ranked findings
1. Major (UX, credibility). No status or dates in the hero. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About gives 2023 to 2025; today is 2026-11-23. A recruiter cannot tell whether the degree is finished or whether he is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, START HERE sits on row 06 (aerobraking). Snake page has no method or result. Owner picks the lead and supplies snake method and result.
3. Major (credibility). Aerobraking Method is third person about prior work and Result switches to "our"; the reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's Ferrari comparison has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from a Wix filesusr.com URL (header, hero, About, footer). It is the one artifact a recruiter wants. Needs assets/resume.pdf from the owner.
5. Major (performance, robustness). Wix image references remain (grep counts: aerobraking 7, sysid 5, tricycle 4, Hasselhoff 4, tethered 4, landing 2, about, argus, projects, raftar, snake 1 each; index and 404 0). Images lack width/height (CLS risk) and are an outage dependency. `fetchpriority="high"` on the first Wix image bets on a third-party host. Needs local files.
6. Minor (UX). Home blurbs 01, 02, 03, 08, 09 give no outcome; only 04 to 07 carry a number. A 30-second scan cannot rank the rows. Same root as 2 and 3.
7. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 when files exist.
8. Minor (visual, taste). Ragged right column on Home and the lone plate on row 06.
9. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
10. Minor (content). Tricycle page voice is passive, no subheads. Owner call.
11. Minor (UX). Contact is LinkedIn only. Owner constraint. Phone header drops Resume, LinkedIn and GitHub; they appear in hero and footer.
12. Nit (visual, taste). About leaves the right third empty on wide screens.
13. Nit (process). Findings 1 to 6 need owner facts and files. Same list for many cycles; the designer is making no-change cycles. Owner should supply them or pause the loop, and unblock WebFetch.

## Good, must not regress
- Retro matte system: paper tones, ink borders, hard shadow, flat dark theme.
- Specific copy and the plain "For the record" ledger.
- Mobile Home: compact header, primary button and Resume/LinkedIn above the fold, comfortable measure.
- Struck-through "three weeks" highlight, stamps, numbered rows, filters, press states, 404 joke, per-page JSON-LD, canonical and OG, skip link, one h1 per page, Fig. 1 plates, the "More on <tag>" line.

## Verdict
The design is coherent and finished: retro matte, specific copy, no AI tells, clean checks. UX stays at 6 because of missing owner input: status and dates, a chosen lead project with real method and result, a plain statement of personal contribution on aerobraking, and local copies of the resume and images. More design cycles will return this same list until those arrive.
