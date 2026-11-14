# Critique, 2026-11-14 (cycle 136)

Method: `python3 tools/check.py . agents/shots` ran to rc=0, zero FAIL, only "images not loaded, sandbox network" notes. No site files edited. I viewed 5 of 78 screenshots: index phone-light, index tablet-dark, snake-robots phone-light, raftar desktop-light, projects phone-dark. I did not open the other 73. No regression seen in the five viewed.

## Sources consulted (honest status)
- WebFetch was denied again for all three targets (permission request unanswered): Google robots.txt spec https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt , WCAG 2.2 target size https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html , web.dev CLS https://web.dev/articles/optimize-cls . No page content was read.
- WebSearch returned listings only. Pointers, not evidence: https://developers.google.com/search/reference/robots_txt , https://developer.chrome.com/docs/lighthouse/seo/invalid-robots-txt , https://support.google.com/webmasters/answer/40361 .
- The three-source rule is NOT met in substance. No finding rests on a quoted claim from a source. Every finding below comes from the repo or screenshots. The robots.txt claim in finding 7 is from my own knowledge of the spec (it applies per host root) and is unverified here.

## Scores
- AI-tell: 2/10, unchanged. Specific content (Seagate three weeks struck to 15 minutes, 99 s, 46 orbits, 500 m stamps, "Sheet n of 9" plates), plain first-person copy, honest footer, no gradient/blur/glow. Residual tells: tidy "Robotics / Controls" taxonomy tags; the "For the record" label is a mild affectation. No tell moved since last cycle.
- Looks good: 8/10, unchanged. Phone home reads as a printed index: serif name, mono ledger, ruled rows, one hard-shadow button. Dark tablet home holds the same hierarchy. Weak spots: snake page on phone ends after one short paragraph, then 150 px of empty paper before the pager; the home phone page is long (about 6200 px) with plate and "Start here" first appearing at row 06.
- SEO: 7/10, unchanged. Unique titles, canonical, og:image absolute (https://kmkar31.github.io/website/assets/og.png), JSON-LD, 12-URL sitemap, 404. Held down by robots.txt and sitemap under the /website/ subpath, all lastmod identical (2026-11-02), one og card for every page, 33 wixstatic references.
- UX: 6/10, unchanged. First phone screen answers who, what, Resume, LinkedIn. Held down by no status, two answers to "best project", thin snake and Raftar pages, a single contact route (LinkedIn).
- Fun and personality: 7/10, unchanged. Struck "three weeks", stamps, plates, Hasselhoff naming story, 404 joke.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all five screenshots viewed (flat paper and ink, hard-edged stamps, inverted-print dark mode).
2. Must not look AI-generated: met. No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status. Home says "MS Mechanical Engineering, Carnegie Mellon University" with no year; About gives 2023 to 2025; today is 2026-11-14. A recruiter cannot tell student, graduate, employed or open to roles. Owner supplies one line for `STATUS` (`build/build.py` line 262, currently empty).
2. Major (credibility). The "Start here" aerobraking page does not separate Karthik's contribution from the cited prior work (Falcone et al.). Owner fact: "I did X; they did Y".
3. Major (UX). Two answers to "strongest project". The lede and row 01 lead with snake robots, whose page is the thinnest (viewed: one question, two metadata rows, one plate, one paragraph, no result). The "Start here" mark and the only plate on the list belong to row 06, which on phone sits below five rows. Owner decides: give snake a result, or lead with aerobraking and move row 06 up.
4. Major (robustness, performance). 33 Wix hotlinks across 11 pages, Resume PDF hosted off-site and linked from header, home and footer; Google Fonts with no metric-matched fallback. Needs owner files (images with dimensions, resume.pdf, WOFF2).
5. Major (credibility). Raftar headline question (`raftar-formula-racing.html`, viewed on desktop): "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no figure or source on the page. Cite or cut. Owner fact.
6. Major (content). Raftar page: the one leadership claim ("I captained the team and did the suspension and brakes") never says what was designed or what constraint it met. The body is two generic sentences plus an outbound link. Owner fact: one concrete suspension or brake decision, or one result.
7. Minor (SEO). robots.txt and sitemap sit under a subpath, so crawlers reading the host root will not see them (unverified here, no source read); submit sitemap.xml in Search Console (owner action). Identical lastmod on all URLs; one og.png for every page.
8. Minor (UX, robustness). New this cycle. On `projects.html` the five filter chips are `<button data-filter>` with no `no-js` rule or `<noscript>` (grep found none), so without JS they render as dead controls above a list that works fine. Fix is designer-doable: hide `.filter` unless JS has added a class to `<html>`. Smaller still: the Projects page carries no "Start here" mark (0 matches), so the one editorial pointer exists only on Home.
9. Minor (UX, taste). Nine equal-weight rows; a "Selected" tier of three would help a 30-second reader. Owner picks.
10. Minor (content). Rows 02, 03, 08, 09 carry no stamp or role; the tethered page ends with no outcome beyond the 500 m setup. Owner facts.
11. Nit (looks, taste). Phone project pages end with a long empty band above the pager when the body is short (snake). Tethered body is text-only on phone. About right column is empty below the index at 1366 px.

Designer-fixable without inventing facts: finding 8 (no-JS filter chips, and optionally a Start here mark on Projects, which repeats an existing fact). Everything else needs the owner.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber (home and About); stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plates with "Sheet n of 9" captions and honest "Not to scale" notes.
- Hasselhoff page and its naming story; 404 joke.
- Plain first-person lede, no slogans; consistent "captained" wording.
- Pager with the neighbour's first fact; "All projects" link; failed images collapse; one h1 per page; unique titles; JSON-LD; canonical; skip link; focus-visible; reduced-motion; 44 px phone nav targets.

## Verdict
Authored, coherent, not generic, no regression in what I viewed. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., one answer to "best project" with a real snake result, a sourced or cut Raftar claim plus one concrete suspension detail, and local Resume, images and fonts. One small designer-fixable item exists (dead filter chips without JS). Caveats: external sources were unreadable this cycle (WebFetch denied) and only 5 of 78 screenshots were inspected.
