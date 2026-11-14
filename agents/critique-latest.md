# Critique, 2026-11-14 (cycle 135)

Method: `python3 tools/check.py . agents/shots` ran to completion (log: every page OK, only "images not loaded, sandbox network" notes; I read the tail of the log, which showed no FAIL). No site files edited; git tree clean at start. I viewed index phone-light, index desktop-light, about desktop-light and tethered-nanosatellite phone-dark. I did not open the other ~74 screenshots. No regression seen in the four viewed.

## Sources consulted (honest status)
- WebFetch was blocked again this cycle (permission request unanswered, W3C WCAG 2.2 target-size page: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). No page content was read.
- WebSearch returned listings only (titles, URLs). Pointers, not evidence: https://www.nngroup.com/topic/careers-ux/ , https://measuringu.com/what-hiring-managers-want-and-what-ux-practitioners-do/ , https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ (these concern UX portfolios, only loosely applicable to an engineering portfolio).
- Prior-cycle sources (robots.txt spec, web.dev font pages) remain unread pointers. The three-source rule is NOT met in substance. No finding below rests on a quoted claim from any source; findings 1 to 9 are from the repo and screenshots.

## Scores
- AI-tell: 2/10, unchanged. Specific content (Seagate 3 weeks struck to 15 minutes, 99 s stamp, 46 orbits, sheet-numbered plates), plain first-person copy, honest footer. Residual tells: the intro / ruled list / dark footer shape, and the identical plate-and-stamp template across pages. No tell moved.
- Looks good: 8/10, unchanged. Home desktop is composed: name, ledger column, one button, ruled rows, one plate. Tethered phone-dark reads well; the plate is legible. Weak: tethered page on phone is about 60% three unbroken prose paragraphs after the plate (taste-level, text is the owner's).
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, og, JSON-LD, 12-URL sitemap, 404. Held down by robots.txt and sitemap under /website/ (verified file content: the `Sitemap:` line sits in a subpath file, which crawlers do not read as the host robots.txt; per Google's spec, unverified this cycle), all 12 lastmod identical (2026-11-02), one shared og card, 33 wixstatic references.
- UX: 6/10, unchanged. First phone screen answers who, what, Resume, LinkedIn. Held down by the empty STATUS slot, two answers to "best project", thin snake and Raftar pages, a single contact route.
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper and ink, hard-edged stamps, no gradient, blur or glow in the screenshots viewed).
2. Must not look AI-generated: met. No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status. Home shows "MS Mechanical Engineering, Carnegie Mellon University" with no year; About shows "2023 – 2025" and "I did my Master's"; today is 2026-11-14. A recruiter cannot tell student, graduate, employed or open to roles. Owner supplies one line for STATUS (`build/build.py`).
2. Major (credibility). The "Start here" aerobraking page does not separate Karthik's contribution from the cited prior work (Falcone et al.). Owner fact: "I did X; they did Y".
3. Major (UX). Two answers to "strongest project". Lede and row 01 lead with snake robots, whose page is the thinnest; the "Start here" mark, the plate and the richest page belong to row 06. On the phone home screenshot the plate and START HERE sit mid-list at row 06, below five rows, so the one visual cue is hard to see in the first scroll. Owner decides: give snake a result, or lead with aerobraking and move row 06 up.
4. Major (robustness, performance). 33 Wix hotlinks across 11 pages, Resume PDF hosted off-site and linked from header, home, footer; Google Fonts with no metric-matched fallback. Needs owner files (images with dimensions, resume.pdf, WOFF2).
5. Major (credibility). Raftar headline question (`raftar-formula-racing.html` line 48): "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced and unsupported by any figure on the page. Cite or cut. Owner fact.
6. Major (content). Raftar page: the owner's only leadership claim ("I captained the team and did the suspension and brakes") never says what was designed or what constraint it met. Owner fact: one concrete suspension or brake decision, or one result.
7. Minor (SEO). robots.txt and sitemap under a subpath; submit sitemap.xml in Search Console (owner action); identical lastmod on all URLs; one og.png for every page.
8. Minor (UX, taste). Nine equal-weight rows; a "Selected" tier of three would help a 30-second reader. Owner picks.
9. Minor (content). Rows 02, 03, 08, 09 carry no stamp or role; tethered page ends with no outcome beyond the 500 m setup. Owner facts.
10. Nit (looks, taste). About right column empty below the "On this page" index at 1366 px; tethered body is text-only on phone.

Designer-fixable without inventing facts: nothing. The loop has been a no-op since cycle 122. Owner answers to 1, 2, 3, 5, 6 and files for 4 are what is needed.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber (home and About); stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plates with "Sheet n of 9" captions and honest "Not to scale" notes.
- Hasselhoff page and its naming story; 404 joke.
- Plain first-person lede, no slogans; consistent "captained" wording.
- Pager with neighbour's first fact; "All projects" link; failed images collapse; one h1 per page; unique titles; JSON-LD; canonical; skip link; focus-visible; reduced-motion; 44 px phone nav targets.

## Verdict
Authored, coherent, not generic, no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project" with a real snake result, a sourced or cut Raftar claim plus one concrete suspension detail, and local Resume, images and fonts. Caveat: external sources were unreadable this cycle and only 4 of 78 screenshots were inspected.
