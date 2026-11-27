# Critique, 2026-11-27 (after designer cycle 214)

Method: ran `python3 tools/check.py . agents/shots` (about 2m20s, zero FAIL; only "images not loaded" sandbox notes). Viewed index phone-light, index desktop-dark and quadrotor-sysid phone-dark. Read LOG.md (tail through cycle 214; the file is 2682 lines, so I did not read all of it), user-critique.md (unchanged, two notes from 2026-10-22), the previous critique, and the repo HTML and CSS. `git status` is clean and no site file has changed since cycle 205, so no regression is possible. Wix images and Google Fonts are blocked in the sandbox (environment limit; the screenshots use fallback serif).

## Sources consulted
Source access was limited this cycle. WebFetch calls to web.dev and w3.org were blocked (permission request unanswered). Only one WebSearch returned, and it gave a result list with no page text. I quote nothing from these pages. The designer or owner should open them:
- web.dev, Font best practices: https://web.dev/articles/font-best-practices (finding 7, self-hosting and font-display)
- web.dev, Optimize web fonts: https://web.dev/learn/performance/optimize-web-fonts (finding 7)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (finding 4, image dimensions; fetch blocked)
- W3C, Understanding SC 2.4.13 Focus Appearance: https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (fetch blocked; used only to frame a check on `:focus-visible`)
- Carried over from last cycle, not re-fetched: NN/g, UX Portfolios: What Hiring Managers Look For, https://www.nngroup.com/videos/ux-portfolios-hiring/
Topic varied from last cycle: web fonts and focus styles instead of tap targets and portfolio content.

## Scores
- AI-tell: 2/10, unchanged. Ruled list, "For the record" ledger, struck-through "three weeks to 15 minutes", stamps, "Fig. 1" plates, "Sheet 8 of 9 / NTS" captions. No gradients, glass, chips, stats strip or card trio. Residual (taste): nine project pages share one skeleton. Tells moved: none.
- Looks good: 8/10, unchanged. Coherent paper-and-ink system in light and dark (viewed). The desktop Home right column is still ragged: rows 01 to 03, 08 and 09 carry no mark, and row 06 stacks stamp, "Start here" and tags beside the only thumbnail.
- SEO: 7/10, unchanged. Per-page title, description, canonical, og:image, twitter card, JSON-LD, sitemap, robots and 404 are present. Weak: one shared OG card, hotlinked images, and robots.txt under a project-site subpath is ignored by crawlers (host limit).
- UX: 6/10, unchanged. Contact, resume and next/previous links are findable. The gaps are content only the owner can supply.
- Fun and personality: 7/10, unchanged. Strike-through, "Time allowed: 99 s" stamp, "Start here" tab.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper, ink borders, hard offset shadows, no blur, both themes, viewed).
2. Must not look AI-generated: met, AI-tell 2. No new notes in the file.

## Regression check
No site file changed. Screenshots match the previous cycle. No regressions.

## Ranked findings
1. Major (UX, credibility). Home subhead reads "MS Mechanical Engineering, Carnegie Mellon University" with no dates or status (viewed, phone and desktop). The STATUS variable in build/ is empty (build line 265), so the "Status" row in the ledger never renders. About says 2023 to 2025 and today is 2026-11-27. A recruiter cannot tell if he has graduated, what he does now, or whether he is available. Owner fact needed.
2. Major (UX). Two answers to "strongest project": row 01 (snake) leads, while "Start here" sits on row 06 (aerobraking), about two phone screens down (viewed). Owner picks the lead, moves the label or reorders.
3. Major (content). The snake page is the lead project and the thinnest. It has a schematic, two sentences under "Why snake robots" and a lab link, with no method, result or number, while the blurb says "I implemented". Owner must supply what he did and what happened.
4. Major (robustness, performance). The resume PDF and nearly all project images are hotlinked from Wix, and assets/ holds only og.png, site.js and style.css. Verified by grep: in snake-robots.html the three `<img>` tags have src, alt, decoding and a loading or fetchpriority hint but no width or height (CLS risk, web.dev link above). A fourth `<img alt="">` has no src at all in the served HTML (probably filled by JS; confirm it is a decoration and not a dead element). Link liveness is not verifiable offline. Owner must supply local copies.
5. Major (credibility). Aerobraking's "46 orbits to target" has no baseline and its Method is third person, hiding his own contribution. Raftar's Ferrari comparison has no source. Owner facts.
6. Minor (consistency, performance). The footer says "no framework" and names DM Serif Display and Source Serif 4, but both load from Google Fonts with two preconnects (index.html line 25). That is a render-blocking third-party dependency on every page and a second host to fail. Self-host WOFF2 with font-display: swap once the font files exist (web.dev fonts links above). Not fixable without the files.
7. Minor (UX). Aerobraking is very long on phone with no pull-out of his own part. Add a short "My part" box once finding 5 is answered.
8. Minor (visual, taste). Desktop Home right column is uneven (row 06). Previously declined; noted only.
9. Minor (SEO). Shared OG card; sitemap submission in Search Console is an owner action.
10. Minor (content). Tricycle page voice is passive with no subheads. Owner call.
11. Nit (visual). Quadrotor-sysid phone: the "Background" section is four long paragraphs of general theory under the figure, with no result or plot of the fitted model. It reads as lecture notes, not as his work. Lead with the outcome (four fitted constants, how well they matched). Owner fact.
12. Nit (UX). Contact is LinkedIn only (GitHub and resume also linked). Owner constraint.
13. Nit (process). Findings 1 to 5 have repeated for about 20 cycles and no site change can resolve them; the last nine cycles were log-only. Owner should supply facts and files, or the loop should stop.

## Good, must not regress
- Ruled-list Home with the "For the record" ledger; no card trio, no stats strip.
- Struck-through "three weeks to 15 minutes", the 99 s stamp, "Fig. 1" plates, "Sheet N of 9" captions.
- Flat paper tones, ink borders, hard offset shadows in both themes; no blur or gradient.
- Per-page titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404.
- Next/More-on links on project pages; sticky header with scroll-padding; reduced-motion block; 3px `:focus-visible` outline (style.css line 37); theme-color metas per scheme.
- About page: dated ledger of education and internships with real numbers.

## Verdict
The design is finished as far as the repo's own material allows: retro, matte, not generated-looking, technically sound. What holds it back is content only the owner can supply: a current status and dates, one clear lead project with a real method and result for the snake work, first-person attribution and baselines on aerobraking, and local copies of the resume, images and fonts. Until those arrive, further design cycles will repeat this list. Stop the loop or send the owner the facts and files.
