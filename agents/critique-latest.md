# Critique, 2026-11-12 (cycle 126)

Rendering: `python3 tools/check.py . agents/shots` ran to completion (rc=0, zero FAIL; only "images not loaded, sandbox network" notes) after about 8 minutes. I viewed index phone-light and desktop-light, and about phone-dark. I did not open the other 60-odd screenshots; no site source has changed since cycle 121 (cycles 122 to 125 were no-ops), so those pages are as judged before. I edited no site files except this one.

## Sources consulted
I opened none of these pages this cycle (web fetch was not used). They are pointers from prior cycles and general knowledge, unverified:
- NN/g, About-us information on websites: https://www.nngroup.com/articles/about-us-information-on-websites/
- web.dev, Font best practices: https://web.dev/articles/font-best-practices
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls
- Google Search Central, robots.txt: https://developers.google.com/crawling/docs/robots-txt/create-robots-txt
This falls short of the three-sources-per-cycle rule. The findings below rest on the repo and screenshots, not on these sources.

## Scores
- AI-tell: 2/10, unchanged. Paper palette, ruled list, stamps, struck-through "three weeks" on amber, mono "For the record" sidebar, graph-paper plate, plain first-person copy. Remaining tell is the familiar shape (intro, list, dark footer). No tell moved.
- Looks good: 8/10. Desktop home is calm and well measured; phone home reads cleanly and the stamps give it rhythm. Weak spots: one plate on the whole list (row 06); rows 02, 03, 08, 09 carry no mark; About's Skills list is a plain stack of lines with a lot of empty space on wide screens.
- SEO: 7/10. Unique titles, canonical, JSON-LD, local og.png, 12-URL sitemap, 404 present. Held down by subpath robots.txt, identical lastmod, and one shared og card.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are in the first phone screen. Held down by no status line, two answers to "best project", and several pages with no stated role or outcome.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, sheet numbers.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in the screenshots I viewed, light or dark.
2. Not AI-looking: met in visuals and copy. Do not regress.
No new owner notes.

## Ranked findings
1. Major (UX, credibility). Stale dates, no status. `STATUS = ""` (build/build.py:262), so the "For the record" sidebar omits it. Home says "MS Mechanical Engineering, Carnegie Mellon University" and About says the Master's runs 2023 to 2025; today is 2026-11-12. A recruiter cannot tell if he is a student, graduated, employed or open to work. This is the biggest lost conversion on the site. Owner supplies one line.
2. Major (credibility). Aerobraking, the page marked "Start here", reads as Falcone et al.'s work (Setup "builds off work done by Falcone et al."; Method "Falcone et al. simulated their agent"), then Result says "our NN state-space model". It never states what Karthik did. Owner fact: one sentence, "I did X; Falcone et al. did Y".
3. Major (UX). Two answers to "strongest project". Lede and row 01 lead with snake robots (its page has no result); the "Start here" label and the only plate sit on row 06. A 30-second reader sees 01 first. Owner decision: move the label to 01 only if the snake page gains a result; otherwise move plate and label to the top.
4. Major (robustness, performance). Wix hotlinks remain: about 26 `wixstatic` lines across the pages (aerobraking 7, sysid 5, tricycle 4, submarine 4, nanosat 4) plus the Resume PDF. The aerobraking hero `<img>` has `fetchpriority="high"` and no width/height, so layout shift and a third-party LCP are likely (unverified without a live run). Fonts come from Google Fonts with no metric-matched fallback. Needs owner files: local images with real dimensions, resume.pdf, WOFF2.
5. Major (credibility). Raftar page line 48: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no source. Cite it or cut it. Owner fact.
6. Minor (UX, taste). Nine projects at equal weight is the whole front page. A "Selected" group of three above "Also" would help a skim reader; the owner picks.
7. Minor (SEO). robots.txt and sitemap.xml live under /website/, where Google ignores robots.txt; submit the sitemap in Search Console. All lastmod values are the same date. One og.png for every page.
8. Minor (content). Rows 02 ARGUS, 03 Landing, 08 Grey-box, 09 Tricycle have no number or role. Needs owner facts.
9. Minor (looks, taste). Long text-only stretches in the aerobraking Problem and Setup sections. A pull-quote or figure break needs real content.
10. Nit (looks). About has empty space at lower right on wide screens; the small mono labels are the faintest text (they pass AA in check.py).
11. Nit (copy). Row blurbs share a verb-led cadence.

Designer-fixable this cycle: nothing without inventing facts. Findings 1 to 5 are unchanged and remain owner decisions or owner files.

## Good, must not regress
- The retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" captions and honest "schematic" notes.
- Plain first-person lede with real specifics; no slogans.
- Aerobraking structure (four headings, facts strip, orbit-range ledger) and pager showing the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page; unique titles; JSON-LD; canonical; 404 joke; skip link; focus-visible and reduced-motion handling.
- 320 px header fix from cycle 121.

## Verdict
The site is authored, coherent and not generic, and I found no regression. What holds it back is content only the owner can supply: a status line, a sentence separating his work from Falcone et al., a single answer to "best project", a sourced or cut Raftar claim, and local Resume, images and fonts with real dimensions. The designer has nothing left to fix without inventing facts. Caveat: this cycle's research was thin (no pages opened) and I viewed three of the 72 screenshots.
