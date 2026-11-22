# Critique, 2026-11-22 (HEAD efe1748; no site files changed since cycle 151)

Method: `python3 tools/check.py . agents/shots` (background run) finished rc=0 with zero FAIL; only "images not loaded" sandbox notes. I viewed index phone-light, index desktop-dark and aerobraking-drl tablet-light, and grepped titles, robots.txt, sitemap, `STATUS` in build/build.py, Wix references, skip link, theme-color, heading order. `git status` shows no site edits by me. Wix and Google Fonts are unreachable here, so photos are absent and fonts fall back (environment limit). The site is byte-identical to the last critique, so settled points are not re-argued.

## Sources consulted
I could not fetch pages this cycle (WebFetch/WebSearch not used), so these are pointers from earlier cycles, unverified here and relied on for nothing new:
- https://www.nngroup.com/articles/ux-design-portfolios/ (show your own role and outcome)
- https://web.dev/articles/font-best-practices (self-host fonts, font-display)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum (2.5.8; 44 px targets pass, no finding)
- Google robots.txt spec (root host only)

## Scores
- AI-tell: 2/10, unchanged. No gradients, glass, chips, stats strip or card trio. Copy is specific (three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m tether). Residual: nine project pages share one skeleton (taste). Tells moved: none.
- Looks good: 8/10, unchanged. Seen: serif name, mono credential line, ledger sidebar, ruled list, one hard-offset button, flat dark theme. Weak spots: stamps only on rows 04 to 07 leave the right column ragged; on phone the Fig. 1 plate sits above row 06 like a stray; on desktop the gap between blurb and metadata column is wide.
- SEO: 7/10, unchanged. Unique titles, canonical, absolute og:image, sitemap (12 urls), robots.txt, JSON-LD, one h1 and h2 order sane. Weak: one shared OG card, robots.txt under /website/ (ignored by Google, host limit), Wix images without dimensions.
- UX: 6/10, unchanged. Below 7, so Major (findings 1 to 4).
- Fun and personality: 7/10, unchanged. Strike-through highlight, stamps, "Sheet 6 of 9 NTS" captions, 404 joke, orbit plate. No new moment.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (paper tones, ink borders, double rules, hard shadow, flat dark theme). No drift.
2. Must not look AI-generated: met, AI-tell 2. Remaining risk is the repeated project template (taste).

## Ranked findings
1. Major (UX, credibility). Hero has no status or dates. "MS Mechanical Engineering, Carnegie Mellon University" reads as present tense; About says 2023 to 2025; today is 2026-11-22. A recruiter sees an unexplained gap and cannot tell availability. `STATUS = ""` (build/build.py line 266) renders a Status row once filled. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, while START HERE sits on row 06 (aerobraking). The snake page is thin by the previous critique (no method or result). Owner picks the lead and supplies the snake method and result.
3. Major (credibility). Aerobraking Method is written in third person about Falcone et al., then Result says "our NN state-space model" and "our method" (seen on the tablet screenshot). The reader cannot tell what Karthik did. "46 orbits" has no baseline. Raftar's "one-fifth the weight of a Ferrari" has no source. Owner sentence and source, or cut.
4. Major (robustness). Resume PDF is hotlinked from Wix in header, hero, About, footer and 404. Needs the owner's PDF at assets/resume.pdf.
5. Major (performance). Wix references remain on 11 pages (aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, tethered 4, landing 2, others 1). No width/height means CLS risk and an outage dependency. Confirm every `alt=""` is truly decorative; not verifiable offline.
6. Minor (UX, new angle). Previous/next pagers follow list order, so aerobraking links to Hasselhoff Submarine and the tethered satellite, but not to ARGUS, its nearest relative (Space). A "Related" link by tag would help a reader who came for space work. Design-only; no owner facts needed.
7. Minor (performance, consistency). Fonts load from Google Fonts while the footer says "one stylesheet, no framework". Self-host WOFF2 with font-display when files exist.
8. Minor (visual). Ragged Home right column and lone Fig. 1 plate on phone. Caption it as the only drawn figure or drop it from Home.
9. Minor (content). Nine projects untiered on Home; same root as 2.
10. Minor (SEO). Shared OG card; robots path is a host limit. Owner action: submit sitemap in Search Console.
11. Minor (content). Tricycle page voice is passive with no subheads; owner call.
12. Minor (UX). Contact is LinkedIn only; footer states it. Owner constraint. Phone header drops Resume, LinkedIn and GitHub icons; they appear in hero and footer, acceptable.
13. Nit (visual, taste). About leaves the right third empty on wide screens; skills lists are 5/3/3.
14. Nit (process). Findings 1 to 5 need owner facts and files; design-only cycles return nothing. Roughly the ninth consecutive cycle with no site change. Owner should supply the items or pause the loop.

## Good, must not regress
- Retro matte system: paper tones, ink borders, one hard shadow, flat dark theme.
- Specific copy and the plain ledger sidebar.
- Mobile index: compact header, Resume and LinkedIn above the fold, comfortable measure, zero tap-target and contrast failures.
- Filter buttons, numbered rows, press states, 404 joke, per-page JSON-LD, canonical and OG, skip link, light and dark theme-color, one h1 per page, project next-links, Fig. 1 plates with sheet captions, the aerobraking result block.

## Verdict
The design is finished in the sense that matters: coherent retro matte, specific copy, no AI tells, clean checks. What holds UX at 6 is missing owner input: status and dates, a chosen lead project with a real method and result, a clear statement of personal contribution on aerobraking, and local copies of the resume and images. The one new, actionable item is topical "Related" links between projects (finding 6). Until the owner supplies the rest, further design cycles will keep returning the same list.
