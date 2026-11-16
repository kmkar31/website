# Critique, 2026-11-16 (cycle 148)

Method: `python3 tools/check.py . agents/shots` ran to completion (rc 0, no FAIL, only "images not loaded, sandbox network" notes). Viewed index phone-light and desktop-light, projects tablet-dark, snake-robots phone-light. Repo checks: head tags, JSON-LD, robots, sitemap, Wix link counts, font loading, reduced-motion block. No site files edited.

## Sources consulted
Web fetches were blocked again this run (permission request unanswered), so no page was read. Cited for the principle only; no finding depends on a quotation:
- https://web.dev/articles/optimize-cls (width/height on images; applied to finding 5). Fetch blocked.
- https://www.nngroup.com/articles/portfolios/ (hiring-manager scanning; applied to findings 2 and 8). Fetch blocked.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (SC 2.5.8). Not fetched; 44px targets seen in screenshots.
Topic this cycle: CLS and third-party dependency, portfolio tiering. Treat the web basis as unverified; repo and screenshot facts are verified.

## Scores
- AI-tell: 2/10, unchanged. No gradients, blur, glow, chips on photos, stats strip, card trio or sparkle. Nothing moved since last cycle (no site changes in cycles 146-147). Residual tells: the identical project-page skeleton; "Set in DM Serif Display and Source Serif 4" is a common pairing (taste). Name-swap test: fails to be generic because of the struck-through "three weeks", the 99 s and 500 m stamps.
- Looks good: 8/10, unchanged. Desktop-light has clear hierarchy, ruled ledger, flat paper tones. Held back by the ragged stamp column on Home (rows 01, 02, 03, 08, 09 have none) and by Wix images missing in the sandbox leaving long text-only runs on project pages (cannot judge image cropping here).
- SEO: 7/10, unchanged. Unique title and description, canonical, OG with absolute og:image 1200x630, Twitter card, Person JSON-LD with sameAs, sitemap, robots, 404. Held back by one shared OG card, robots/sitemap under /website/, and Wix images without dimensions.
- UX: 6/10, unchanged. Name, school, Resume, LinkedIn are in the first phone screen. No status or dates; contact is LinkedIn only; Resume PDF is on Wix. Major because below 7.
- Fun and personality: 7/10, unchanged. Strike-through, stamps, "Time allowed: 99 s", numbered ledger, 404, press states. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. Paper tones, ink borders, double rules, one hard-offset button, flat dark theme (projects tablet-dark is coherent, warm, no glow).
2. Must not look AI-generated: met; AI-tell 2. Remaining risk is the repeated project-page template, which I rate as taste.

## Ranked findings
1. Major (UX, credibility). No status or dates. Hero says "MS Mechanical Engineering, Carnegie Mellon University" with no years; lede is present tense ("I research"); today is 2026-11-16 and About gives a closed 2023-2025 range. A recruiter cannot tell if he is available. Owner fact needed; `STATUS` in build/build.py is ready.
2. Major (UX). Two answers to "strongest project". Home row 01 (snake) leads, but its page is thin (one section and a link, phone screenshot: question, two facts, schematic, one paragraph). START HERE sits on row 06. Owner picks the lead and supplies the snake method and result.
3. Major (credibility). Aerobraking page does not say what Karthik did versus the cited prior work; the Raftar "Ferrari" comparison has no source. Owner source or cut.
4. Major (robustness). Resume PDF, the most-wanted asset, is hotlinked to a Wix host (filesusr.com) from header, hero, About and footer. If Wix lapses every Resume link dies. Needs the owner's PDF at assets/resume.pdf. The designer tried and the sandbox blocked the host; that is an environment limit, so this needs the owner file.
5. Major (performance). About 30 Wix images, none with width/height (wixstatic count: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, others 1-2), so CLS risk and outage dependency. Lazy loading and fetchpriority are already set. Needs owner files or sizes.
6. Minor (performance, consistency). Fonts load from Google Fonts on all 13 pages (third-party stylesheet) while the footer says "one stylesheet, no framework". Self-host two WOFF2 files when reachable. display=swap is set, so low severity.
7. Minor (visual). Ragged Home right column. The "stamp only where a real number exists" rule is right; accept it.
8. Minor (content). Nine projects untiered on Home; NN/g guidance (unread this cycle) favours a few strong ones. Owner call; same root as finding 2.
9. Minor (SEO). robots.txt and sitemap sit under /website/; crawlers read robots.txt only at the host root. Host limit. One shared OG card for 12 pages.
10. Minor (content). Tricycle page is passive voice with no subheads. Owner call on who did what.
11. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint; noted, not pressed.
12. Nit (visual, taste). About desktop leaves the right third empty; skills are 5/3/3.
13. Nit (process). Cycles 139-147 declined the same owner-fact items. Further design-only cycles will repeat; the owner must supply status, lead project, snake result, aerobraking contribution, Ferrari source, resume.pdf, image files.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy: "three weeks" struck to "15 minutes", "Time allowed: 99 s", "46 orbits to target", "500 m of tether", plain "For the record" ledger.
- Mobile index: one-row header, Resume and LinkedIn above the fold, comfortable measure, large tap targets.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD/canonical/OG, reduced-motion block, focus ring.
- Drawn figure plates ("Fig. 1", "Sheet 1 of 9 - NTS") instead of stock imagery; next-project pager on project pages.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, UX 6, fun 7. No regressions (no site changes since cycle 145). UX stays under 7 because of facts and files only the owner can supply; the single highest-value file is a local resume.pdf, ahead of images. Until then there is little a design-only cycle can fix beyond self-hosting fonts.
