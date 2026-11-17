# Critique, 2026-11-17 (cycle 150 checkout, commit 503137d)

Method: fresh checkout at origin/main 503137d (clean tree). `python3 tools/check.py . agents/shots` ran to completion, rc=0, every page OK at phone, tablet and desktop in both themes, with only "images not loaded, sandbox network" notes (it needs about 4 minutes, longer than a default 2-minute shell timeout). I looked at index phone-light, index desktop-dark, aerobraking-drl phone-light and about tablet-light. Repo checks: Wix reference counts, STATUS constant, robots.txt, sitemap, titles, img attributes. No site files edited.

## Sources consulted
WebFetch of https://web.dev/articles/optimize-cls was refused (permission request unanswered, told not to retry), so no page was read this run. The pointers below are cited for the principle only, and no finding depends on a quotation. The web basis is unverified. Repo and screenshot facts are verified.
- https://web.dev/articles/optimize-cls (width/height on images to reserve space). Not fetched.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (target size). Not fetched.
- https://www.nngroup.com/articles/portfolios/ (hiring-manager scanning). Not fetched.
- https://developers.google.com/search/docs/crawling-indexing/robots/intro (robots.txt lives at the host root). Not fetched.

## Scores
- AI-tell: 2/10, unchanged. No gradient, blur, glow, floating chip, stats strip, card trio or sparkle. The name-swap test passes: struck "three weeks", "Time allowed: 99 s", "500 m of tether", "46 orbits to target" belong to this person. Residual tells: all nine project pages share one skeleton (tl;dr, question, fact list, Fig. 1, sections, pager), and DM Serif Display with Source Serif 4 is a common editorial pairing (taste). Tells moved since last cycle: none.
- Looks good: 8/10, unchanged. Desktop index has a clear hierarchy (large name, mono credential line, ledger sidebar, ruled project list, one hard-offset button). Dark theme is a coherent inverted print, not a generic dark mode. Phone index is comfortable. Held back by the ragged right column (stamps on rows 04 to 07 only) and the lone Fig. 1 plate on row 06, which on phone sits above the title like a mistake. Real photographs are not visible in the sandbox, so project pages look text-only here (about 9 to 10 screens of prose on aerobraking phone).
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, OG and Twitter tags, JSON-LD, 12-URL sitemap, robots.txt, 404 page. Held back by one shared OG card, robots.txt under /website/ (crawlers only read the host root), and undimensioned Wix images.
- UX: 6/10, unchanged. Name, school, Resume and LinkedIn are in the first phone screen. Still no status or dates, contact is LinkedIn only, and Resume is a Wix hotlink. Major because below 7.
- Fun and personality: 7/10, unchanged. Strike-through, stamps, ledger and the 404 joke work. No new moment this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, one hard shadow, flat dark theme).
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated page template (taste).
3. Note on item 14 and 15 from the file (About right third intentionally calm; owner blockers remain): accepted. I keep the About right side as a Nit only.

## Ranked findings
1. Major (UX, credibility). No status or dates. The hero gives "MS Mechanical Engineering, Carnegie Mellon University" with no years and a present-tense lede, while About gives a closed 2023 to 2025 range and today is 2026-11-17. A recruiter cannot tell if he is available or already working. `STATUS = ""` at build/build.py:266 is ready. Owner fact needed.
2. Major (UX). Two answers to "strongest project". Row 01 (snake) leads, START HERE sits on row 06 (aerobraking). The snake page is thin (tl;dr, lab, advisor, one schematic, short paragraph, no method or result). Owner chooses the lead and supplies the snake method and result. Principle: NN/g portfolio guidance (unfetched) is to lead with the strongest work.
3. Major (credibility). The aerobraking page builds on Falcone et al. and says what the agent did, but not what Karthik changed or built. The Raftar question ("one-fifth the weight of a Ferrari but matches its 0-60") has no source. Owner contribution sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from a Wix host (filesusr.com) in the header, hero, About and footer. If Wix lapses, every Resume link dies and the main conversion goal fails. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Image `src` and Resume references to Wix hosts total 124 line occurrences across 13 pages (aerobraking 20, tricycle 18, sysid 18, hasselhoff 14, projects 11, tethered 10, snake 8; the earlier count of 56 used a different method, so compare trend, not number). Snake page images have no width/height, so CLS risk (web.dev, unfetched) and outage dependency. Lazy loading, decoding=async and fetchpriority are already set, so only dimensions and local files are missing.
6. Minor (performance, consistency). Fonts load from fonts.googleapis.com on every page while the footer claims "one stylesheet, no framework". Self-host the two families when reachable; display=swap is set.
7. Minor (visual). Ragged Home right column: stamps on 04 to 07 only. Rows 01 to 03, 08, 09 have none, and the Fig. 1 plate appears only on 06. Either give the plate a reason (caption "only drawn figure") or drop the plate on Home; stamps-only-where-a-number-exists is a sound rule.
8. Minor (content). Nine projects untiered on Home, same root as finding 2.
9. Minor (SEO). robots.txt and sitemap under /website/ (host-root limit); one OG card for 12 pages. Host limitation, noted not pressed.
10. Minor (content). Tricycle page uses passive voice with no subheads; who did what is an owner call.
11. Minor (UX). Contact is LinkedIn only; the footer states it. Owner constraint, noted.
12. Nit (visual, taste). About tablet and desktop leave the right side empty; skills are 5/3/3, which makes the three lists unequal.
13. Nit (process). Cycles 139 to 150 declined the same owner-fact items; design-only cycles now return nothing. Owner must supply: status line, lead project, snake result, aerobraking contribution, Ferrari source, resume.pdf, image files.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy: "three weeks" struck to "15 minutes", "Time allowed: 99 s", "46 orbits to target", "500 m of tether", plain "For the record" ledger.
- Mobile index: one-row header, Resume and LinkedIn above the fold, comfortable measure, large tap targets (check.py reports zero tap-target and contrast failures).
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, reduced-motion block, focus ring.
- Drawn figure plates instead of stock imagery; previous/next pager with a neighbour fact; inline Resume link on About.

## Verdict
The site has a coherent retro-print identity and does not read as generated: AI-tell 2, visual 8, SEO 7, UX 6, fun 7. No regressions; the tree has no site changes since cycle 145 and the automated checks are clean. UX stays under 7 because of facts and files only the owner can supply. The highest-value item is a local resume.pdf, then the status line and the lead-project decision. Web research was blocked again, so sourcing is thin and should be redone when fetches work. Until the owner supplies those items there is little a designer can do without inventing facts.
