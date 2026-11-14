# Critique, 2026-11-14 (cycle 134)

Method: ran `python3 tools/check.py . agents/shots` to completion: zero FAIL, only "images not loaded, sandbox network" notes. No site files edited and none changed since cycle 133 (git clean). I viewed projects phone-dark, raftar phone-light, snake-robots desktop-light and hasselhoff tablet-dark (different from last cycle's set); I did not open the other ~74 screenshots. No regression seen.

## Sources consulted
Honest status: WebFetch was denied for every page this cycle (permission prompt unanswered, so no page was read). Only WebSearch result listings were available, i.e. titles and URLs, not content. No finding below depends on a quoted claim from them; they are pointers for the owner/designer to read.
- Google, How Google interprets the robots.txt specification: https://developers.google.com/search/reference/robots_txt (listing only; fetch of the create-robots-txt page was blocked). Used for finding 7 (robots.txt is read from the host root).
- GitHub community discussion, robots.txt in github.io pages: https://github.com/orgs/community/discussions/64865 (listing only). Same topic.
- web.dev, Font best practices: https://web.dev/articles/font-best-practices and Self-hosted fonts pattern: https://web.dev/patterns/web-vitals-patterns/fonts/font-self-hosted (listings only; fetch blocked). Pointers for finding 4.
- NN/G mobile UX article fetch was blocked.
Three-source rule NOT met in substance. Previously read NN/G portfolio guidance (cycle 133) still applies to findings 1 to 3.

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, tilted stamps, struck-through "three weeks", sheet numbers, mono labels, plain first-person copy, honest footer. Remaining tell is the overall shape (intro, list, dark footer) and the repeated figure plate template. No tell moved.
- Looks good: 8/10, unchanged. Hasselhoff tablet-dark is the strongest page: figure with labelled thrusters and IR target, stamp, state-machine disclosure, pager. Projects phone-dark list is clean and the stamps carry information. Weak: snake desktop page is bare after the figure (one two-line paragraph, then pager; roughly 200 px of dead paper above the footer); Raftar page is the same (one paragraph plus an external link).
- SEO: 7/10, unchanged. Unique titles, descriptions, canonical, og, JSON-LD, 12-URL sitemap, 404. Held down by robots.txt/sitemap under /website/ (crawlers use host-root robots.txt only; the `Sitemap:` line in a subpath file is ignored), all 12 lastmod identical (2026-11-02), one shared og card, 33 wixstatic references across 11 pages.
- UX: 6/10, unchanged. First phone screen has name, field, lede, Resume and LinkedIn. Held down by empty `STATUS` (`build/build.py:262`), two answers to "best project", thin pages (snake, Raftar), one contact route.
- Fun and personality: 7/10, unchanged. 99 s stamp, 46 orbits, 500 m tether, struck-through "three weeks", Hasselhoff SpongeBob origin line (specific and funny; keep), 404 joke.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat paper/ink, hard-edged stamps, inverted-print dark mode, no gradient/blur/glow in the screenshots viewed).
2. Must not look AI-generated: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status; stale timeline. Home says CMU MS with no year; About says 2023 to 2025; today is 2026-11-14. Student, graduated, employed or open to work is unanswerable. Owner supplies one line for STATUS.
2. Major (credibility). Aerobraking page (the "Start here" project) never separates Karthik's work from Falcone et al. Owner fact: "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project": lede and row 01 lead with snake robots, but the snake page is the thinnest in the set (schematic, one paragraph, no result, method or outcome; confirmed in the desktop screenshot) while the "Start here" mark and the richest page belong to aerobraking. Owner decision: add a snake result, or lead with aerobraking.
4. Major (robustness, performance). 33 Wix hotlinks, and Resume PDF off-site, linked from every page. Fonts come from Google Fonts with no metric-matched fallback. Needs owner files: local images, resume.pdf, WOFF2 (see web.dev font pages above, unread).
5. Major (credibility). Raftar page: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced, it is the page's headline question, and the page has no data behind it. Cite or cut. Owner fact.
6. Major (looks/UX, new emphasis). Raftar page is mostly a stamp-and-sketch around one generic paragraph ("A team of 40+ engineering students design, build, test and race...") plus an external link; "I did the suspension and brakes" appears twice (lede and caption) but never what was designed or what constraint it met. It is the owner's only leadership claim. Owner fact needed: one concrete suspension or brake decision.
7. Minor (SEO). robots/sitemap under /website/; submit the sitemap in Search Console (works for a project site); identical lastmod; one og.png for all pages.
8. Minor (UX, taste). Nine equal-weight rows on Home and Projects; no "Selected" tier. Owner picks three.
9. Minor (content). Rows 02, 03, 08, 09 on Projects have no stamp or role; tethered page has no outcome beyond the 500 m setup. Owner facts.
10. Nit (looks, taste). Text-only stretches (aerobraking Problem/Method, tethered body); About right column empty at 1366 px.

Designer-fixable this cycle: nothing without inventing facts. The loop has been a no-op since cycle 122. Owner must answer 1, 2, 3, 5, 6 and supply files for 4 before more cycles are useful.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plates with "Sheet n of 9" captions and honest "schematic"/"not to scale" notes.
- Hasselhoff page: SpongeBob-movie naming story, state-machine disclosure.
- Plain first-person lede, no slogans, consistent "captained" wording.
- Pager showing the neighbour's first fact; "All projects" back link.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible; reduced-motion; 44 px phone nav targets.

## Verdict
The site is authored, coherent and not generic, with no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project" with a real snake result, a sourced or cut Raftar claim plus one concrete suspension detail, and local Resume, images and fonts. Caveat: external sources were not readable this cycle (fetch denied), and only 4 of 78 screenshots were viewed this cycle.
