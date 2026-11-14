# Critique, 2026-11-14 (cycle 137)

Method: `python3 tools/check.py . agents/shots` finished with 0 FAIL (only "images not loaded, sandbox network" notes). No site files edited. I viewed 4 of the 62 screenshots: index phone-light, index desktop-light, about desktop-light, raftar phone-dark. The rest were not opened. No regression seen in those four. The latest commit (hide filter chips without JS) is not visible in them; I checked it in the log only.

## Sources consulted (honest status)
- WebFetch was denied again for WCAG 2.2 target size (https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html). The permission request went unanswered, so I read no page content.
- One WebSearch ("hiring managers portfolio") returned a listing only. Pointers, not evidence: https://www.nngroup.com/topic/careers-ux/ , https://measuringu.com/what-hiring-managers-want-and-what-ux-practitioners-do/ , https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ .
- The three-source rule is NOT met. No finding quotes a source. Every finding comes from the repo or the screenshots I viewed.

## Scores
- AI-tell: 2/10, unchanged. Specific facts (struck "three weeks" on amber, 99 s, 46 orbits, 500 m stamps, "Sheet n of 9" plates), plain first-person copy, honest footer, no gradient, blur or glow. Residual tells: the tidy "Robotics / Controls" tag taxonomy and the "For the record" label. Nothing moved.
- Looks good: 8/10, unchanged. Desktop home is a clear printed index with one hard-shadow button, ruled rows and one plate. Weak spots: the plate and "Start here" first appear at row 06; the About desktop right column is empty below the index; the phone home page is long.
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, 12-URL sitemap. Held down by robots.txt and sitemap under the /website/ subpath, 12 identical lastmod values (2026-11-02), a single og.png for every page, and 31 wixstatic references across 11 pages.
- UX: 6/10, unchanged. The first phone screen gives name, focus, Resume and LinkedIn. Held down by no status, two answers to "best project", thin snake and Raftar pages, and one contact route.
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all four screenshots viewed.
2. Must not look AI-generated: met. No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status. Home says "MS Mechanical Engineering, Carnegie Mellon University" with no year. About says 2023 to 2025. Today is 2026-11-14, so a recruiter cannot tell student, graduate, employed or open to roles. `STATUS` in `build/build.py` line 262 is still "". Owner supplies one line.
2. Major (credibility). The tense is inconsistent. Home says "I research compliant control of snake robots" (present). About says "I did my Master's ... (2023 – 2025)" (past) and "I've implemented these algorithms". The two pages disagree about whether he is still at CMU. This is partly designer-visible, but the fix depends on owner fact 1.
3. Major (UX). Two answers to "strongest project". The lede and row 01 lead with snake robots, whose page is the thinnest. The only plate and the "Start here" mark sit on row 06 (aerobraking). Owner decides which leads.
4. Major (credibility). The aerobraking page does not separate Karthik's contribution from the cited prior work. Owner fact.
5. Major (credibility). `raftar-formula-racing.html` line 48: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no figure or source on the page. Cite or cut. Owner fact.
6. Major (content). Raftar says "I captained the team and did the suspension and brakes" but never says what was designed or what constraint it met. The body is two generic sentences plus an outbound link. Owner fact: one concrete decision or result.
7. Major (robustness, performance). Wix hotlinks remain (31 references), the Resume PDF is off-site and linked from header, home and footer, and the fonts come from Google Fonts with no metric-matched fallback. Needs owner files (images with dimensions, resume.pdf, WOFF2).
8. Minor (SEO). robots.txt and sitemap sit under a subpath; this is from my own knowledge of the spec and is unverified here. Submit the sitemap in Search Console. All lastmod values are identical and one og card serves every page.
9. Minor (UX, taste). Nine equal-weight rows; a "Selected" tier of three would help a 30-second reader. Owner picks.
10. Minor (content). Rows 02, 03, 08 and 09 carry no stamp or role. The tethered page has no outcome beyond the 500 m setup. Owner facts.
11. Nit (looks). The About desktop right column is empty below the index. Short project pages leave a long empty band above the pager on phone.

Designer-fixable without inventing facts: none beyond a tense check once the owner answers 1.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber (home and About); stamps (46 orbits, 500 m, 99 s, podium); the podium box on About.
- Fig. 1 plates with "Sheet n of 9" captions and honest "NTS" notes.
- Hasselhoff naming story; 404 joke.
- Plain first-person lede, no slogans, consistent "captained" wording; honest footer and colophon.
- Pager with the neighbour's first fact; failed images collapse; one h1 per page; unique titles; JSON-LD; canonical; skip link; 44 px phone targets.

## Verdict
Authored, coherent, not generic, with no regression in what I viewed. The site is held back by content only the owner can supply: a status line (which also settles the present versus past tense split between Home and About), a sentence separating his work from the cited aerobraking work, one answer to "best project" with a real snake result, a sourced or cut Raftar claim with one concrete suspension detail, and local Resume, images and fonts. Caveats: external sources were unreadable this cycle and only 4 of 62 screenshots were inspected.
