# Critique, 2026-11-14 (cycle 138)

Method: `python3 tools/check.py . agents/shots` finished rc=0 with 0 FAIL (only "images not loaded, sandbox network" notes). No site files edited. I viewed 4 of the 78 screenshots, different from last cycle: index tablet-dark, projects phone-light, snake-robots desktop-light, tethered-nanosatellite phone-dark. The other 74 were not opened. No regression seen in those four. HEAD is 6bd24c7 (no source change in cycle 137).

## Sources consulted (honest status)
- The three-source rule is NOT met again. WebFetch was blocked ("permission request not answered") for all three attempts: https://web.dev/articles/optimize-cls , https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img , https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html . I read no page content.
- One WebSearch returned only a listing (web.dev optimize-cls, web.dev learn/images performance-issues, shopify.dev prevent-image-layout-shift). Pointers, not evidence: https://web.dev/articles/optimize-cls , https://web.dev/learn/images/performance-issues .
- No finding below quotes a source. Every finding comes from the repo or the screenshots I viewed. Treat the CLS point as my prior knowledge, unverified here.

## Scores
- AI-tell: 2/10, unchanged. Specific facts (struck "three weeks" on amber, 99 s, 46 orbits, 500 m stamps, "Sheet n of 9" plates), plain first-person copy, honest footer, no gradient, blur or glow. Residual tells: the tidy "Robotics / Controls" taxonomy and the "For the record" label. Nothing moved.
- Looks good: 8/10, unchanged. Tablet home reads as a printed index; snake desktop page has strong title, ruled spec table and a plate. Weak spots: plate and "Start here" first appear at row 06; the snake page is short with large empty space above the pager; tethered page on phone is a ~5700 px wall of four dense paragraphs after the plate.
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, 12-URL sitemap. Held down by 12 identical lastmod values (2026-11-02), one og card, robots.txt and sitemap under the /website/ subpath, and Wix hotlinks (96 `wixstatic` occurrences across the HTML files by `grep -o`; last cycle said 31 references, likely counted differently).
- UX: 6/10, unchanged. First phone screen gives name, focus, Resume and LinkedIn. Held down by no status line, two answers to "best project", thin snake and Raftar pages, one contact route (LinkedIn only).
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all four screenshots viewed.
2. Must not look AI-generated: met. No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status. Home says "MS Mechanical Engineering, Carnegie Mellon University" with no year (tablet-dark home confirms). About says 2023 to 2025. Today is 2026-11-14, so a recruiter cannot tell student, graduate, employed or open to roles. `STATUS = ""` still at `build/build.py` line 262 (verified). Owner supplies one line.
2. Major (credibility). Tense disagrees between Home ("I research compliant control of snake robots", present) and About (Master's "2023 – 2025", past). Fix follows from finding 1.
3. Major (UX). Two answers to "strongest project". Lede and row 01 lead with snake robots, whose page is the thinnest (viewed: one schematic, one paragraph, no result, no outcome). The only plate and "Start here" sit on row 06 (aerobraking). Owner decides which leads.
4. Major (credibility). Aerobraking page does not separate Karthik's contribution from cited prior work. Owner fact.
5. Major (credibility). `raftar-formula-racing.html`: the "Ferrari" weight and 0-60 claim (1 occurrence, verified) has no figure or source on the page. Cite or cut. Owner fact.
6. Major (content). Raftar says he did "the suspension and brakes" with no design decision or result. Owner fact: one concrete detail.
7. Major (robustness, performance). Wix hotlinks, off-site Resume PDF (header, home, footer), Google Fonts with no metric-matched fallback. Images without owner-supplied dimensions risk CLS (prior knowledge, source unread this cycle). Needs owner files.
8. Minor (content, reading comfort). Tethered nanosatellite page on phone: four unbroken paragraphs of about 5 to 8 lines each below the plate, with the 500 m / 3U+1U facts only in the header. The stamp-and-plate language used elsewhere stops. A pull-out of one fact already in the text (for example the 40,000 tracked objects, or "98% of debris is shrapnel under 1 cm") would break it without inventing anything. Taste, but it is the longest page.
9. Minor (UX). Projects page on phone has no "Start here" mark and no plate; all nine rows are equal weight. A "Selected" tier of three would help a 30-second reader. Owner picks.
10. Minor (SEO). Robots and sitemap under a subpath (my own knowledge of the spec, unverified here); submit the sitemap in Search Console. Identical lastmod, single og card.
11. Minor (content). Rows 02, 03, 08, 09 carry no stamp or role. Tethered outcome beyond the 500 m setup is missing. Owner facts.
12. Nit (looks). Snake page: large empty band between the last paragraph and the pager on desktop; About desktop right column empty below the index.

Designer-fixable without inventing facts: finding 8 only (reordering or pulling out an existing sentence on the tethered page). Everything else needs the owner.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow button, inverted-print dark mode (tablet-dark home is coherent and legible).
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium); podium box on About.
- Fig. 1 plates with "Sheet n of 9" captions and honest "NTS" and "Not to scale" notes.
- Hasselhoff naming story; 404 joke.
- Plain first-person lede, no slogans; honest footer and colophon.
- Pager with the neighbour's first fact; failed images collapse; one h1 per page; unique titles; JSON-LD; canonical; skip link; 44 px phone targets; filter chips hidden without JS.

## Verdict
Authored, coherent, not generic, no regression in the four screenshots viewed. The site is held back by content only the owner can supply: a status line (which also settles the Home versus About tense split), a sentence separating his work from the cited aerobraking work, one answer to "best project" with a real snake result, a sourced or cut Raftar claim with one concrete suspension detail, and local Resume, images and fonts. The one designer-side item is breaking up the tethered page text. Caveats: external sources were unreadable again (WebFetch blocked) and only 4 of 78 screenshots were inspected.
