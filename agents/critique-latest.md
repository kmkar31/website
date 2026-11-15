# Critique, 2026-11-15 (cycle 139)

Method: `python3 tools/check.py . agents/shots` finished rc=0, 0 FAIL (only "images not loaded, sandbox network" notes; it needs about 3 minutes, run it with a long timeout). No site files edited. HEAD is fc60474 (tethered pull-out). I viewed 4 of 78 screenshots, different from last cycle: index phone-light, index desktop-light, raftar-formula-racing phone-light, about desktop-dark. The other 74 were not opened. I did not re-open the tethered page, so the cycle 138 pull-out is unreviewed by me.

## Sources consulted (honest status)
- The three-source rule is NOT met for the third cycle running. WebFetch of https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html was blocked (permission request unanswered). I read no page content.
- One WebSearch ("NN/g portfolio hiring managers") returned a listing only. Pointers, not evidence: https://www.uxdesigninstitute.com/blog/hiring-managers-portfolio , https://measuringu.com/what-hiring-managers-want-and-what-ux-practitioners-do/ , https://www.nngroup.com/topic/careers-ux/ . I did not open them.
- No finding below quotes a source. All come from the repo or the screenshots I viewed.

## Scores
- AI-tell: 2/10, unchanged. Specific facts (struck "three weeks" on amber, 99 s, 46 orbits, 500 m stamps, "Sheet n of 9" plates), plain first-person copy, honest footer, no gradient, blur or glow. Residual tells: the tidy "Robotics / Controls" taxonomy, the "For the record" label, and the rhythm of three-item lists in the sidebar ("Seagate, York University, Tube Investments"). Nothing moved.
- Looks good: 8/10, unchanged. Desktop home reads as a printed index and the amber strike is the right single accent. Weak spots: the plate and "Start here" first appear at row 06; the Raftar phone page is short and the sketch is generic; About desktop leaves the right column empty below the contents box.
- SEO: 7/10, unchanged. Held down by 12 identical lastmod values, one og card, robots.txt and sitemap under the /website/ subpath, and 96 `wixstatic` occurrences (`grep -o` over the HTML files).
- UX: 6/10, unchanged. First phone screen gives name, focus, Resume, LinkedIn. Held down by no status line, two answers to "best project", one contact route (LinkedIn only).
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all four screenshots viewed (paper, grain, double rules, hard-shadow button, inverted dark mode).
2. Must not look AI-generated: met. No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status. Home (phone and desktop, viewed) says "MS Mechanical Engineering, Carnegie Mellon University" with no year; About says 2023 to 2025. Today is 2026-11-15, so a recruiter cannot tell student, graduate, employed or open to roles. `STATUS = ""` at `build/build.py` line 263 (verified). Owner supplies one line.
2. Major (credibility). Tense split: Home "I research compliant control of snake robots" (present) against About "2023 – 2025" (past). Follows from 1.
3. Major (UX). Two answers to "strongest project". Lede and row 01 lead with snake robots (thinnest page), while the plate and "Start here" sit on row 06. Owner decides.
4. Major (credibility). Aerobraking page does not separate Karthik's contribution from cited prior work. Owner fact.
5. Major (credibility). `raftar-formula-racing.html` line 48: "one-fifth the weight of a Ferrari but matches its 0-60" has no figure or source. Seen on the phone screenshot as the page's only framing. Cite or cut. Owner fact.
6. Major (content). Raftar page is the weakest page viewed. "I did the suspension and brakes" appears in the lede, again in the figure caption, and the body is two generic sentences plus a link to the team site. Same claim three times, no design decision, no number, no result beyond "Podium". The About page has more (RFR23, "first electric racecar") than the project page. Designer-fixable only in part: the caption could drop the repeat, and the About fact "RFR23, our institution's first electric racecar" is already in the repo and could be moved onto the page. Everything else is an owner fact.
7. Major (robustness, performance). Wix hotlinks (96 occurrences), off-site Resume PDF in header, home and footer, Google Fonts with no local fallback. Needs owner files.
8. Minor (UX). Contact is "message me on LinkedIn" in every footer; no email by design (LOG). A professor who does not use LinkedIn has no route. Owner choice; say so on About at least.
9. Minor (UX). Projects page has no "Start here" mark and no tiering; nine equal rows. Owner picks three.
10. Minor (content). Rows 02, 03, 08, 09 on home carry no stamp or number. Owner facts.
11. Minor (SEO). Sitemap and robots under a subpath, identical lastmod, one og card. Hosting and owner action; not verifiable offline.
12. Nit (looks). About desktop: empty right column below the contents box; on dark, the Skills columns have uneven heights (5, 3, 3 items). Taste.

Designer-fixable without inventing facts: finding 6 in part (de-duplicate the caption; move the RFR23 fact from About). Everything else needs the owner.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow button, inverted-print dark mode (About desktop-dark is legible and coherent).
- Struck-through "three weeks" on amber (Home and About agree); stamps (46 orbits, 500 m, 99 s, podium); boxed "podium finish" on About.
- Fig. 1 plates with "Sheet n of 9" captions and honest "NTS" notes.
- Pager showing the neighbour's first fact (Raftar page: "Landing success: 100%", "Thrusters: 4 BLDC").
- Hasselhoff naming story; 404 joke; plain first-person lede; honest colophon.
- One h1, unique titles, JSON-LD, canonical, skip link, 44 px phone targets, chips hidden without JS.

## Verdict
Authored, coherent, not generic, no regression in the four screenshots viewed. The site is held back by content only the owner can supply: a status line (which also settles the tense split), a sentence separating his work from the cited aerobraking work, one answer to "best project", a sourced or cut Raftar claim with one real suspension detail, and local Resume, images and fonts. The one partly designer-side item is the thin, repetitive Raftar page. Caveats: external sources were unreadable again and only 4 of 78 screenshots were inspected.
