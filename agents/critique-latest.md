# Critique, 2026-11-17 (cycle 151 checkout, commit 0313384)

Method: clean tree at 0313384. `python3 tools/check.py . agents/shots` finished rc=0 (about 4 minutes), every page OK at phone, tablet and desktop in both themes, only "images not loaded, sandbox network" notes. I looked at index phone-light and desktop-light, snake-robots phone-dark, about tablet-light. Also checked the repo: Wix reference counts, robots.txt, titles. Site files not edited.

## Sources consulted
WebFetch was refused again (permission request unanswered, told not to retry) for both pages below, so no page was read and the web basis is unverified. Cited for the principle only; no finding depends on a quotation. Repo and screenshot facts are verified.
- https://web.dev/articles/optimize-cls (width/height on images). Blocked.
- https://developers.google.com/search/docs/crawling-indexing/robots/intro (robots.txt at host root). Blocked.
- https://www.nngroup.com/articles/portfolios/ and https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html were also on the list from earlier cycles. Not fetched.
Fewer than the three sources the brief asks for were actually read. Redo when fetches work.

## Scores
- AI-tell: 2/10, unchanged. No gradient, blur, glow, chips, stats strip, card trio or sparkle. Name-swap test passes ("three weeks" struck to "15 minutes", "Time allowed: 99 s", "500 m of tether", "46 orbits to target"). Residual: all nine project pages share one skeleton; DM Serif Display with Source Serif 4 is a familiar editorial pairing (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Desktop index has clear hierarchy (large name, mono credential line, ledger sidebar, ruled list, one hard-offset button). Dark theme is an inverted print, not a generic dark mode. Weak spots: ragged right column (stamps only on 04 to 07) and the lone Fig. 1 plate on row 06, which on phone sits above the title like a stray. Snake page on phone is short and sparse (tl;dr, two fact rows, one schematic, one paragraph, then a pager with large empty space), so the lead project looks unfinished.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, robots.txt, 404. Held back by one shared OG card, robots.txt under /website/ (crawlers read only the host root), undimensioned Wix images.
- UX: 6/10, unchanged. Name, school, Resume and LinkedIn are in the first phone screen. Still no status or dates in the hero, LinkedIn-only contact, Resume hotlinked. Major because below 7.
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "For the record" ledger, "Sheet 1 of 9 · NTS" captions, 404 joke. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme). No drift found.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project-page template (taste).

## Ranked findings
1. Major (UX, credibility). No status or dates in the hero. It says "MS Mechanical Engineering, Carnegie Mellon University" in present tense, About says 2023 to 2025, and the newest experience entry ends Aug 2024. Today is 2026-11-17, so a recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` at build/build.py:266 is ready. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads and is thin; START HERE is on row 06 (aerobraking). Owner picks the lead and supplies the snake method and result. NN/g portfolio guidance (unfetched): lead with the strongest work.
3. Major (credibility). The aerobraking page does not say what Karthik changed or built beyond the cited prior work. The Raftar "one-fifth the weight of a Ferrari" claim has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from Wix in header, hero, About and footer. If Wix lapses, the main conversion link dies everywhere. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix-hosted images and Resume references remain on 13 pages (grep count of lines mentioning wix: aerobraking 9, sysid 7, tricycle 6, hasselhoff 6, tethered 6, about 4, landing 4, others 2 to 3; a different method than earlier cycles, so compare trend only). Dimensions missing means CLS risk (web.dev, unfetched) plus outage dependency. Needs local image files.
6. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host when reachable.
7. Minor (visual). Ragged Home right column and lone Fig. 1 plate. Either caption the plate as the only drawn figure or drop it on Home.
8. Minor (content). Nine projects untiered on Home; same root as 2.
9. Minor (SEO). robots/sitemap path and single OG card; host limit, noted not pressed.
10. Minor (content). Tricycle page voice is passive with no subheads; owner call.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint.
12. Nit (visual, taste). About leaves the right third empty on tablet and desktop; skills lists are 5/3/3.
13. Nit (process). Many cycles have declined the same owner-fact items. Owner must supply: status line, lead project, snake result, aerobraking contribution, Ferrari source, resume.pdf, image files. Further design-only cycles return nothing.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy: struck "three weeks", "99 s", "46 orbits", "500 m of tether", plain ledger.
- Mobile index: one-row header, Resume and LinkedIn above the fold, comfortable measure, large tap targets (check.py: zero tap-target and contrast failures).
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion block, focus ring.
- Drawn figure plates instead of stock imagery; pager with a neighbour fact; inline Resume link on About.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, UX 6, fun 7. No regressions and no site changes since the last cycle; automated checks are clean. UX stays under 7 because of facts and files only the owner can supply, the sharpest being the missing status or dates against a visible gap since Aug 2024, then a local resume.pdf and the lead-project call. Web research was blocked again, so sourcing is thin. Without owner input there is little a designer can do without inventing facts.
