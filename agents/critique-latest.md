# Critique, 2026-11-17 (cycle 155 checkout, HEAD 0c716a6; tree clean)

Method: `python3 tools/check.py . agents/shots` ran rc=0 with zero FAIL (only sandbox "images not loaded" notes; it needs about 5 minutes). I looked at index phone-light and desktop-light, aerobraking phone-dark, and snake-robots tablet-light. I grepped titles, wix references, robots.txt, sitemap and the font link. Fonts are blocked in the sandbox, so screenshots show fallback serif; that is an environment limit. No site files edited.

## Sources consulted
- Earlier cycles, still cited: https://web.dev/articles/optimize-cls (set width and height on images); https://developers.google.com/search/reference/robots_txt (robots.txt only valid at host root).
- Blocked this cycle (permission request unanswered, not retried): https://www.nngroup.com/articles/portfolios/, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, https://web.dev/articles/optimize-lcp. I read no new source this cycle, so the "three sources, vary the topic" rule was not met. No finding depends on an unread source.

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Large serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button. Weak spots: ragged right column (stamps on rows 04 to 07 only); the lone Fig. 1 plate on row 06 sits above the title on phone like a stray.
- SEO: 7/10, unchanged. Unique titles on all 13 pages, sitemap with 12 urls, robots.txt present. Weak: one shared OG card, robots.txt under /website/ (ignored by Google), undimensioned Wix images.
- UX: 6/10, unchanged. Below 7, so Major (findings 1, 2, 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). Hero has no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense, About says 2023 to 2025, newest experience ends Aug 2024; today is 2026-11-17. A recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` in build/build.py is ready. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads and its page is thin (a figure, one paragraph, one link; snake-robots tablet shot); START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). Aerobraking page does not say what Karthik changed beyond the cited prior work (Falcone et al.). "Target reached in 46 orbits" is the headline with no baseline. Raftar's "one-fifth the weight of a Ferrari" claim has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from Wix in header, hero, About, footer and likely the 404. If Wix lapses it dies everywhere. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix references remain on every content page (grep counts: aerobraking 9, sysid 7, tricycle 6, hasselhoff 6, tethered 6, landing 4, others 3). No width and height means CLS risk (web.dev optimize-cls) and outage dependency. Needs local image files.
6. Minor (performance, consistency). Fonts load from Google Fonts (index.html line 25) while the footer says "one stylesheet, no framework". Self-host when files exist.
7. Minor (visual). Ragged Home right column and lone Fig. 1 plate; caption it as the only drawn figure or drop it on Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). Shared OG card; robots path is a host limit. Noted, not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on wide screens; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files. Design-only cycles now return nothing; recommend the owner supplies them or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: one-row header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion block, focus ring.
- Drawn figure plates instead of stock imagery; pager with a neighbour fact; inline Resume link on About.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, UX 6, fun 7, all unchanged, no regressions, clean automated checks. UX stays under 7 because of facts and files only the owner can supply: the status line against a visible gap since Aug 2024, a local resume.pdf, image files, and the lead-project call. Research this cycle was weak (all three fetches blocked), so no new best-practice findings were raised. Without owner input the designer has little to do without inventing facts.
