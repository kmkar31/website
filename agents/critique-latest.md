# Critique, 2026-11-27 (after designer cycle 213)

Method: ran `python3 tools/check.py . agents/shots` (rc=0, zero FAIL; only "images not loaded" sandbox notes; it takes about 3 minutes). Viewed index phone-light, index desktop-dark, about tablet-light, snake-robots phone-light. Read LOG.md (through cycle 213), user-critique.md (unchanged: two notes from 2026-10-22), the previous critique and the repo HTML. `git status` is clean and cycles 206 to 213 changed no site files, so no regression is possible. Wix images and Google Fonts are blocked in the sandbox (environment limit).

## Sources consulted
WebSearch ran this cycle. It returned result lists (titles and URLs) only; WebFetch was not used, so I quote no page text. The pages below are the ones the findings lean on, and the designer or owner should open them.
- Nielsen Norman Group, "UX Portfolios: What Hiring Managers Look For": https://www.nngroup.com/videos/ux-portfolios-hiring/ (findings 1 to 4: say what you did and what the result was; keep it scannable)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (finding 5: set width and height on images)
- W3C, Understanding SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (tap targets, checked below)
- web.dev Learn Images, key performance issues: https://web.dev/learn/images/performance-issues (finding 5, third-party image dependency)
Caveat: the NN/g item is aimed at UX designers; I apply it to an engineering portfolio by analogy and label that as judgment.

## Scores
- AI-tell: 2/10, unchanged. Ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", stamps, "Fig. 1" plates with "Sheet 1 of 9 / NTS" captions. No gradients, glass, chips, stats strip, card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Coherent paper-and-ink system in both themes (viewed). Desktop Home right column is ragged: rows 01 to 03, 08, 09 carry no mark; row 06 stacks stamp, "Start here" and tags beside the only thumbnail.
- SEO: 7/10, unchanged. Per-page title, description, canonical, og:image, twitter card, JSON-LD, sitemap, robots, 404. Weak: one shared OG card; hotlinked images; robots.txt under a project-site subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and next/previous links are easy to find. The gaps are content only the owner can supply.
- Fun and personality: 7/10, unchanged. Strike-through, "Time allowed: 99 s" stamp, "Start here" tab.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, ink borders, hard offset shadows, no blur, both themes, viewed).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed since cycle 205. Screenshots match the previous cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead reads "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status; About says 2023 to 2025 and today is 2026-11-27 (viewed). A recruiter cannot tell whether he has graduated, what he does now or whether he is available. Owner fact needed. Source: NN/g link above.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, while "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead, moves the label or reorders.
3. Major (content). The snake page, the lead project, is the thinnest (viewed, phone): a schematic captioned "illustrative", two sentences under "Why snake robots", a lab link, nothing else. No method, result or number, yet the blurb says "I implemented". With the Wix photos unloaded in the sandbox it is even barer; in production it depends entirely on hotlinks. Owner must supply what he did and what happened.
4. Major (credibility). Aerobraking's "46 orbits to target" has no baseline and its Method is third person, hiding his own contribution. Raftar's Ferrari comparison has no source. Owner facts.
5. Major (robustness, performance). Resume PDF and nearly all project images are hotlinked from Wix. Verified by grep: snake-robots.html `<img>` tags carry src, alt, loading and decoding but no width or height, which is a standard CLS risk (web.dev link above); one stray `<img alt="">` remains in snake-robots.html (confirm it is decoration). assets/ holds only og.png, site.js and style.css, so no local copy exists. Needs assets/resume.pdf and local images from the owner. Link liveness is not verifiable offline.
6. Minor (UX). Aerobraking is very long on phone with no pull-out of his own part. Add a short "My part" box once finding 4 is answered.
7. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
8. Minor (consistency). Footer says "no framework" and names DM Serif Display and Source Serif 4, but fonts load from Google Fonts. Self-host WOFF2 when files exist.
9. Minor (SEO). Shared OG card; sitemap submission in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
12. Nit (process). Findings 1 to 5 have repeated for about 20 cycles and no site change can resolve them; the last eight cycles were log-only. Owner should supply facts and files, or the loop should pause.

## Good, must not regress
- Ruled-list Home with the "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plates, "Sheet 1 of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links on project pages; sticky header with scroll-padding; reduced-motion block.
- About page: dated ledger of education and internships with real numbers, readable at tablet width (viewed).

## Verdict
The design is finished as far as the repo's own material allows: retro, matte, not generated-looking, technically sound. What holds it back is content only the owner can supply: a current status and dates, one clear lead project with a real method and result for the snake work, first-person attribution and baselines on aerobraking, and local copies of the resume and images. Until those arrive, further design cycles will repeat this list. Pause the loop or send the owner the five facts.
