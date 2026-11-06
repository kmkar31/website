# Critique, 2026-11-06 (cycle 91)

Rendering: `python3 tools/check.py . agents/shots` ran, 78 lines OK (13 pages x 3 viewports x 2 themes), only "images not loaded" sandbox notes. I viewed index phone light, index desktop light, about desktop dark, snake-robots phone light. Greps: `STATUS = ""` (build/build.py:262); Resume is a filesusr.com URL; wixstatic hotlinks on 11 of 13 pages (none on index and 404); the snake `<img>` tags carry no width/height. No site files edited.

## Sources consulted (honest note)
WebFetch of web.dev/articles/optimize-cls, w3.org WCAG 2.2 target-size-minimum and nngroup.com/articles/portfolio-reviews was blocked (permission not granted). One WebSearch returned only the web.dev "Optimize Cumulative Layout Shift" result links, with no page text. So I read no source body this cycle and the three-source rule is not met. Nothing below depends on a citation; all findings rest on renders and repo greps. Pointers, unverified:
- https://web.dev/articles/optimize-cls (image width/height and font fallback)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://www.nngroup.com/articles/portfolio-reviews/

## Scores
- AI-tell score: 2/10. Unchanged. Paper tone, double rules, hard-offset button, struck-through "three weeks" on an amber swatch, stamps carrying real numbers, "Fig. 1 / Sheet n of 9 / NTS" captions, authored line drawings. No gradient, blur, glow, card trio or stats strip. Residual tells: the home page is the stock "intro, ruled list, footer" index, and "Compliant, gait-based controllers I implemented..." blurbs share one cadence.
- Looks good: 8/10. Strong hierarchy and rhythm on home and project pages. Weak spots: About right third is empty below the "On this page" box; row 01 has no visual on home while row 06 does.
- SEO: 7/10. Title, description, canonical, OG/Twitter, JSON-LD, sitemap and 404 noindex are present. Risks: sitemap and robots.txt at a project-site subpath; og:image is generic; project media is hotlinked.
- UX: 6/10. Identity, projects and LinkedIn are found fast. Penalised by the stale status and the lack of a quantified top project (findings 1 and 3).
- Fun and personality: 7/10. 99 s pressable stamp, 404 game line, struck-through marker, plate figures. Home itself has little of it; all of it sits one click down.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Flat paper, grain, hard shadow only on the primary button, flat dark footer; dark theme reads as inverted print.
2. Not AI-looking: met on visuals and copy (see score). Do not regress.

## Ranked findings

1. Major (UX, content credibility). The Master's is shown as "2023 - 2025" and "is at Carnegie Mellon" (About, home h-line "MS Mechanical Engineering, Carnegie Mellon University"). Today is 2026-11-06, so a recruiter cannot tell whether he has graduated or is job-hunting. The STATUS slot (build.py:262) is still empty. Why: a recruiter's first question on a portfolio is availability and timeline. Owner-only fact; ask for one line (graduated, where now, open to roles).
2. Major (robustness, SEO, CLS). All project media is still hotlinked from static.wixstatic.com (11 pages) and Resume is a filesusr.com PDF. If Wix rotates or blocks those URLs the project pages lose every photograph and the resume link on every page breaks. Figure images have no width/height, so loading shifts layout (CLS) when they do arrive. Needs owner files in assets/ (resume.pdf, images) plus dimensions.
3. Major (UX, 30-second test). "Start here" points to Aerobraking (row 06), the only row with a plate on home, while row 01 (snake robots, the lede's subject) is the research the lede leads with. The lede names snake robots, the pointer names aerobraking, so the front page gives two answers to "strongest project". Snake page itself has no outcome, only a tl;dr and "Why snake robots"; it is the thinnest page in the set (viewed on phone: Fig. 1, one paragraph, pager). Fix is owner facts (what was done, what happened) for snake, or move the label to row 01 once it has a result. Trade-off noted by the designer: renumbering breaks Sheet n of 9; moving only the label does not.
4. Major (content). Raftar page: the "Ferrari" wording is original-site copy that is unverified. Owner to confirm a figure or cut it; claims a hiring manager can fact-check should be exact.
5. Minor (looks good). About desktop: after the intro, the right third is empty for the rest of the page (about 1800 px of dead column beside Skills, Education, Experience). The sticky-less "On this page" box ends early. Taste; the portrait slot is deliberate, but until a portrait exists this reads unfinished. Option: put the home ledger ("Built / Internships / Toolbox") there or pull the Education dates into a left margin column.
6. Minor (SEO). robots.txt and sitemap.xml live at /website/ on a project site; crawlers only read robots.txt at the host root. The sitemap is still discoverable if submitted in Search Console. Owner action. Also lastmod is 2026-11-02 for all 13 URLs, which carries no information.
7. Minor (SEO). og:image is one generic plate for every page. Per-project share cards would help LinkedIn previews; only the snake plate is used. Low priority.
8. Minor (fonts, CLS). Two Google Fonts with display=swap and no size-adjusted fallback; self-hosting needs WOFF2 from the owner. Cannot be done offline.
9. Minor (UX, phone). Phone header drops Resume and GitHub; resume is in the lede and footer, LinkedIn only. Acceptable, but the lede's second link row (Resume, LinkedIn) is small text links at 360 px; confirm tap targets stay at least 24 px (check.py passes).
10. Nit (copy). Row blurbs on home share one construction (verb-led first-person summary, "so they can ..."), noticeable in a column of nine. Vary two or three of them using facts already on each page.
11. Nit (looks good). Mono labels (01 to 09, tags) at about 13 px in muted tone on the tan ground are the lightest text on the page; contrast passes in check.py but they read faint on a phone.
12. Nit. Footer repeats LinkedIn, and home repeats it in the lede row. Harmless.

## Good, must not regress
- Retro matte system: warm paper, grain, double rules, hard-shadow primary button only, inverted-print dark theme.
- The struck-through "three weeks" on amber swatch on home and About; stamps that carry numbers (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions; repo-local, so they never hotlink-fail.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly (no orphan captions, no empty boxes).
- Pager shows neighbour's first fact; no wraparound.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic; I found no regression. What is holding it back is not design but missing owner facts: a current status line, a result for the snake work, a confirmed Raftar claim, and local copies of the resume and images. Until those arrive, the biggest risks are a stale "2023 - 2025" and Wix hotlinks that can break the Resume link and every photograph. Designer-fixable items are minor (About empty third, row-blurb cadence, per-page og:image).
