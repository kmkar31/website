# Critique, 2026-11-16 (cycle 149)

Method: `python3 tools/check.py . agents/shots` ran to completion (rc 0, no FAIL, only "images not loaded, sandbox network" notes). Viewed index phone-light and desktop-dark, about tablet-light, aerobraking-drl phone-dark. Repo checks: head tags, robots, Wix link counts, font loading, reduced-motion block, aerobraking and Raftar copy. No site files edited.

## Sources consulted
All three web fetches were blocked this run (permission request unanswered, not retried), so no page was read. Cited for the principle only; no finding depends on a quotation. Treat the web basis as unverified; repo and screenshot facts are verified.
- https://web.dev/articles/optimize-cls (width/height on images). Fetch blocked.
- https://www.nngroup.com/articles/portfolios/ (hiring-manager scanning). Fetch blocked.
- https://developers.google.com/search/docs/crawling-indexing/robots/intro (robots.txt must sit at host root). Fetch blocked.
Topic this cycle: CLS/third-party dependency, portfolio tiering, robots location (same as cycle 148; the fetch block prevented varying it).

## Scores
- AI-tell: 2/10, unchanged. No gradients, blur, glow, chips on photos, stats strip, card trio or sparkle. No site changes since cycle 145. Residual: identical project-page skeleton (question, three facts, figure, sections, pager); DM Serif Display plus Source Serif 4 is a common pairing (taste). Name-swap test passes because of the struck "three weeks", "Time allowed: 99 s", "500 m of tether".
- Looks good: 8/10, unchanged. Desktop-dark index has clear hierarchy, ruled ledger, flat warm tones, one hard-offset button. Held back by the ragged stamp column on Home (rows 01, 02, 03, 08, 09 have none) and by unseen Wix images (cropping cannot be judged here).
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, OG with absolute og:image, Twitter card, JSON-LD, sitemap, robots, 404. Held back by one shared OG card, robots/sitemap under /website/, and undimensioned Wix images.
- UX: 6/10, unchanged. Name, school, Resume, LinkedIn are in the first phone screen. No status or dates; LinkedIn-only contact; Resume PDF lives on Wix. Major because below 7.
- Fun and personality: 7/10, unchanged. Strike-through, stamps, ledger, 404, press states. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, flat dark theme; desktop-dark is warm with no glow).
2. Must not look AI-generated: met; AI-tell 2. Remaining risk is the repeated page template (taste).

## Ranked findings
1. Major (UX, credibility). No status or dates. Hero says "MS Mechanical Engineering, Carnegie Mellon University" with no years; lede is present tense ("I research"); About gives a closed 2023 to 2025 range and today is 2026-11-16. A recruiter cannot tell if he is available. Owner fact; `STATUS` in build/build.py is ready.
2. Major (UX). Two answers to "strongest project". Home row 01 (snake) leads, START HERE sits on row 06 (aerobraking). The snake page is thin. Owner picks the lead and supplies the snake method and result.
3. Major (credibility). Aerobraking page: "This project builds off work done by Falcone et al." and then describes Falcone's setup and result; it never says what Karthik changed or built beyond the PPO training figures. Raftar page question: "one-fifth the weight of a Ferrari but matches its 0-60" has no source. Owner contribution sentence and source, or cut.
4. Major (robustness). Resume PDF, the most-wanted asset, is hotlinked from a Wix host (filesusr.com) in header, hero, About and footer. If Wix lapses every Resume link dies. Needs the owner's PDF at assets/resume.pdf. Sandbox cannot fetch it; owner file required.
5. Major (performance). 56 Wix URL references across 13 pages (aerobraking 9, sysid 7, tricycle 6, hasselhoff 6, tethered 6, others 2 to 4; counts include Resume links), images without width/height: CLS risk and outage dependency. Lazy loading and fetchpriority already set. Needs owner files or sizes.
6. Minor (performance, consistency). Fonts load from fonts.googleapis.com on every page while the footer says "one stylesheet, no framework". Self-host two WOFF2 files when reachable. display=swap set.
7. Minor (visual). Ragged Home right column. "Stamp only where a real number exists" is right; accept.
8. Minor (content). Nine projects untiered on Home; same root as finding 2.
9. Minor (SEO). robots.txt and sitemap under /website/ (crawlers read robots.txt at the host root only); one OG card for 12 pages. Host limit.
10. Minor (content). Tricycle page passive voice, no subheads. Owner call on who did what.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint; noted, not pressed.
12. Nit (visual, taste). About desktop/tablet leaves the right side empty; skills are 5/3/3.
13. Nit (process). Cycles 139 to 148 declined the same owner-fact items. Further design-only cycles will repeat; owner must supply status, lead project, snake result, aerobraking contribution, Ferrari source, resume.pdf, image files.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy: "three weeks" struck to "15 minutes", "Time allowed: 99 s", "46 orbits to target", "500 m of tether", plain "For the record" ledger.
- Mobile index: one-row header, Resume and LinkedIn above the fold, comfortable measure, large tap targets.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD/canonical/OG, reduced-motion block, focus ring.
- Drawn figure plates ("Fig. 1", "Sheet 6 of 9 - NTS") instead of stock imagery; previous/next pager on project pages; inline Resume link on About.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, UX 6, fun 7. No regressions (no site changes since cycle 145). UX stays under 7 because of facts and files only the owner can supply; the single highest-value item is a local resume.pdf, then the status line and lead-project decision. Web research was blocked this cycle, so the sourcing is thin and should be redone when fetches work. Until the owner supplies those items there is little a design-only cycle can fix beyond self-hosting fonts.
