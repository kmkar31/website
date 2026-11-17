# Critique, 2026-11-17 (cycle 154 checkout, commit 5f0418f or later; tree clean)

Method: clean tree, no site changes since cycle 152. `python3 tools/check.py . agents/shots` finished rc=0, zero FAIL, only "images not loaded, sandbox network" notes (it needed about 4 minutes). I looked at index phone-light and desktop-light, aerobraking phone-dark, about tablet-light. Grepped the repo for wix lines per page, robots.txt and the font link. Screenshots render in fallback serif because Google Fonts is blocked in the sandbox; that is an environment limit. Site files not edited.

## Sources consulted
- Read (earlier cycle, still cited): https://web.dev/articles/optimize-cls : always set width and height on images so the browser reserves space.
- Read (earlier cycle, still cited): https://developers.google.com/search/reference/robots_txt : robots.txt is only valid at the host root.
- Not read, blocked this cycle (permission unanswered): https://web.dev/articles/optimize-lcp, https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide, https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html. A search returned only listings (web.dev fetch-priority, optimize-lcp, resource-hints), not page content. Only two sources were actually read, and both are repeats; this misses the "three sources, vary the topic" rule. No finding depends on an unread source.

## Scores
- AI-tell: 2/10, unchanged. No gradients, blur, glow, chips, stats strip or card trio. Copy is specific ("three weeks" struck to "15 minutes", "99 s", "46 orbits"). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Desktop index has a large serif name, mono credential line, ledger sidebar, ruled list and one hard-offset button. Weak spots: ragged right column (stamps only on rows 04 to 07), and the lone Fig. 1 plate on row 06, which on phone sits above the title like a stray.
- SEO: 7/10, unchanged. One shared OG card, robots.txt under /website/ (ignored by Google), undimensioned Wix images.
- UX: 6/10, unchanged. Below 7, so Major: no status or dates, LinkedIn-only contact, hotlinked Resume.
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, ledger, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). No status or dates in the hero. It says "MS Mechanical Engineering, Carnegie Mellon University" in present tense, About says 2023 to 2025, and the newest experience entry ends Aug 2024. Today is 2026-11-17, so a recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` in build/build.py is ready. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads and is thin; START HERE sits on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). Aerobraking page (long on phone) does not say what Karthik changed beyond the cited prior work (Falcone et al.). The Raftar "one-fifth the weight of a Ferrari" claim has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from Wix in header, hero, About and footer (and on the 404-free home it is the main conversion link). If Wix lapses it dies everywhere. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix-hosted images remain on 11 pages (wix lines: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, five pages 1). No width and height means CLS risk (web.dev optimize-cls) and an outage dependency. Needs local image files.
6. Minor (performance, consistency). Fonts load from Google Fonts (index.html line 25) while the footer says "one stylesheet, no framework". Self-host when files are available.
7. Minor (visual). Ragged Home right column and lone Fig. 1 plate; either caption it as the only drawn figure or drop it on Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). robots/sitemap path and single OG card; host limit, noted not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on tablet and desktop; skills lists are 5/3/3.
13. Nit (process). Findings 1 to 5 need owner facts and files: status line, lead project, snake result, aerobraking contribution, Ferrari source, resume.pdf, image files. Design-only cycles now return nothing; recommend the owner supplies them or the loop pauses.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: one-row header, Resume and LinkedIn above the fold, comfortable measure, large tap targets (check.py: zero tap-target and contrast failures).
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion block, focus ring.
- Drawn figure plates instead of stock imagery; pager with a neighbour fact; inline Resume link on About.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, UX 6, fun 7, all unchanged, with no regressions and clean automated checks. UX stays under 7 because of facts and files only the owner can supply, the sharpest being the missing status or dates against a visible gap since Aug 2024, then a local resume.pdf and the lead-project call. Research this cycle was weak (three fetches blocked, two repeat sources read), so no new best-practice findings were raised. Without owner input there is little a designer can do without inventing facts.
