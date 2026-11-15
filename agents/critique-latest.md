# Critique, 2026-11-15 (cycle 141)

Method: `python3 tools/check.py . agents/shots` finished rc=0, 0 FAIL (it needs more than 2 minutes; only "images not loaded, sandbox network" notes). No site files edited. HEAD is cca7aa4. I viewed 4 of 78 screenshots, chosen to differ from last cycle: index phone-light, about desktop-light, aerobraking-drl phone-dark, snake-robots tablet-light. The other 74 were not opened. Cycle 140's changes (Raftar tl;dr, tethered pull-out, sitemap lastmod) were checked in source and in the sitemap, not by eye on those pages (I did not open the Raftar or tethered shots this cycle).

## Sources consulted (honest status)
- Read: NN/g, "5 Steps to Creating a UX-Design Portfolio", https://www.nngroup.com/articles/ux-design-portfolios/ (WebFetch). It says each case study should state the outcome and the author's specific responsibilities, and that "the final screenshots only tell part of the story". Finding 1 relies on it. It is about UX portfolios, so it transfers to an engineering portfolio by analogy only.
- Ran one WebSearch (portfolio and recruiter query); I read no result pages beyond the NN/g one above.
- Blocked, unread: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img, https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap (permission requests unanswered). The three-source rule is NOT met: one source read. Findings 5 and 6 rest on repo evidence, not on those pages.

## Scores
- AI-tell: 2/10, unchanged. Specific facts (struck "three weeks" on amber, stamps with real values, "Sheet n of 9" plates, "For the record" ledger), plain first-person copy, no gradient, blur or glow. Residual tells: the three-item lists ("Seagate, York University, Tube Investments"; "MPC, PPO, system ID, STM32, ANSYS"), and every project page using the same template (question line, fact strip, Fig. 1, headed sections), which would look the same with other projects swapped in. Nothing moved this cycle.
- Looks good: 8/10, unchanged. About desktop is calm and well ruled; Home phone has a clear order (name, one paragraph, button, ledger, rows). Weak spots: the snake page at tablet (finding 1) is mostly empty paper, and About has a blank right column below the sidebar and uneven skill columns (5, 3, 3), taste only.
- SEO: 7/10, unchanged. Unique titles and descriptions, canonical, og and twitter tags, JSON-LD (CreativeWork on projects), absolute og:image, sitemap and robots present. Held down by Wix hotlinks (grep counts of lines: 33 across 11 pages; aerobraking 7, sysid 5), one shared og card, subpath robots.txt and sitemap (they sit under /website/, so crawlers will not treat robots.txt as the site's), and weak alt text (finding 5).
- UX: 6/10, unchanged. In 30 seconds on a phone I get name, focus, advisor, Resume and LinkedIn. I do not get status or year, and the flagship project page gives no result.
- Fun and personality: 7/10, unchanged. The struck "three weeks" and the stamps are the memorable parts; nothing new in the pages I viewed.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all four screenshots (paper, grain, double rules, hard-shadow button, inverted-print dark).
2. Must not look AI-generated: met. No new owner notes. Taste caveat: the identical project-page template (see AI-tell).

## Ranked findings
1. Major (UX, credibility; designer-fixable in part). The page for the project the home lede sells is the thinnest on the site. snake-robots.html (tablet-light viewed) has a tl;dr, a one-line question, a schematic, three Wix images that did not load in the sandbox, and one 40-word paragraph ("Why snake robots") ending in a link to the lab page. It has no method, no result, no "what I did". Aerobraking (phone-dark viewed) runs six sections. A recruiter who clicks row 01 gets less than from row 06. NN/g (above) says each case study should state outcome and the author's responsibilities. Designer can restructure only with facts already in the repo (the lab, advisor, "implemented ... compliant gait-based controllers", question line); the result and method are owner facts. Do not invent them.
2. Major (UX, credibility). No status. Home (phone-light viewed) says "MS Mechanical Engineering, Carnegie Mellon University" with no years; About (desktop-light viewed) says 2023 to 2025; today is 2026-11-15. `STATUS = ""` in `build/build.py`. A reader cannot tell student, graduate or available. Owner supplies one line.
3. Major (credibility). Tense split from 2: Home "I research compliant control of snake robots" and "At CMU's Biorobotics Lab ... I research" (present) against About's closed date range. Owner fact.
4. Major (UX). Two answers to "strongest project". The lede names snake robots and row 01 is snake, but the "START HERE" mark and plate sit on row 06 (aerobraking), as seen on index phone-light. Combined with finding 1 the pointer is defensible (row 06 is the fuller page), but then the lede should say so or the lede project should be rewritten to match. Owner decides.
5. Major (accessibility, SEO). Image alt text is generic where images exist: "Modular snake robot, figure 1 of 3" and so on (snake-robots.html line 55). It says nothing a non-sighted reader or a search engine can use, and "figure 1 of 3" repeats position, not content. Designer-fixable without inventing facts only if the alt is limited to what is visible, which I cannot verify offline because the Wix images did not load. Owner should supply a one-clause description per image, or the designer can state "Photograph" less specifically and drop the numbering.
6. Major (robustness, performance). Wix hotlinks remain, the Resume PDF is a third-party URL, Google Fonts have no local fallback, and `<img>` dimensions cannot be checked offline. Needs owner files. I could not verify CLS (web.dev page not read).
7. Major (credibility). Aerobraking page does not separate Karthik's contribution from the cited prior work ("Falcone et al."). The Setup and Method sections describe the prior agent in the past tense and the result as "the trained agent"; a reader cannot tell what he built. Owner fact.
8. Major (credibility). Raftar: the "one-fifth the weight of a Ferrari but matches its 0-60" framing is unsourced. Cite or cut. Owner fact.
9. Minor (UX). LinkedIn is the only contact route in every footer. Owner constraint (no email). Unchanged.
10. Minor (UX). Projects: rows 01, 02, 03, 08, 09 have no stamp and there is no tier, so nine near-equal rows; the home phone list shows the same unevenness (stamps on 04 to 07 only). Owner picks.
11. Minor (content). Tethered and ARGUS state aims and method but no outcome; owner fact.
12. Minor (SEO). Sitemap now has per-file lastmod (2026-11-14 for About, 2026-11-15 for Home and Projects), which is an improvement and closes last cycle's item 9. It is derived from git and "today if changed", so it will still move on every edit; fine.
13. Nit (looks, taste). About: right column is empty below the "On this page" box and the skill columns are uneven. The calm measure is deliberate; I would leave it.

Designer-fixable without inventing facts: finding 1 (structure only, e.g. an explicit "What I did" line built from the existing tl;dr, and removing filler like "Read more on" in favour of a labelled link), part of 5. Everything else needs the owner.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow buttons, inverted-print dark mode.
- Struck "three weeks" on amber, stamps with real values, boxed "podium finish" on About.
- Fig. 1 plates with "Sheet n of 9 . NTS" captions and honest "illustrative" notes.
- Pager showing the neighbour's first fact; "All projects" back link on every page.
- Plain first-person lede, "For the record" ledger, honest colophon, 404 joke.
- Unique titles, canonical, JSON-LD, skip link, filter chips hidden without JS, 44 px phone targets.

## Verdict
The site is still authored, coherent and not generic, and I found no regression in the four screens I opened. The most useful finding this cycle is one the previous critiques did not raise: the flagship snake-robots page is the thinnest project page while the home page sells it first, which works against the 30-second test more than any styling issue. The remaining blockers are the same owner list: a status line, one answer to "best project", the aerobraking contribution, a sourced or cut Ferrari claim, and local Resume, images and fonts. Caveats: only one external source was readable, and 4 of 78 screenshots were inspected.
