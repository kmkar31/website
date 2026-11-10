# Critique, 2026-11-10 (cycle 109)

Rendering: `python3 tools/check.py . agents/shots` rc=0, only sandbox "images not loaded" notes. I viewed index phone light, aerobraking desktop dark, about tablet light. Last commit (cycle 108) only added fetchpriority="high" to the first figure on project pages (confirmed present in aerobraking-drl.html); no regression seen. No site files edited.

## Sources consulted
- Search only (titles returned, pages not readable; WebFetch permission was not answered for w3.org, web.dev preload-responsive-images, MDN color-scheme): WCAG 2.2 SC 2.5.8 Target Size (Minimum) results. I cite nothing from them beyond the known 24 px minimum; the site's 44 px targets exceed it.
- Earlier cycles, read: https://web.dev/articles/fetch-priority ; https://developers.google.com/crawling/docs/robots-txt/create-robots-txt (robots.txt cannot sit in a subdirectory).
- Topic this cycle: target size, re-check of cycle 108 change. Research was limited by the sandbox; flagging that honestly.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, hard-offset button, strike-through "three weeks", stamps, Fig. plate, mono ledger, plain first-person copy. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. Phone list reads well; desktop dark project page is calm with good measure. Weak spots: single plate (row 06) breaks list rhythm on phone; About right side empty on wide screens.
- SEO: 7/10. Unique titles/descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Open: robots.txt under subpath, one og:image, identical lastmod, unsized hotlinked figures.
- UX: 6/10. Name, field, lede, Resume and LinkedIn on the first phone screen. Held down by no current status and no result on the lead project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plate, ledger. No new idea supported by repo facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-10 with no status line (STATUS = "" in build/build.py:262). Recruiter cannot tell graduated, working or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots, whose page states no result, while "Start here" sits on row 06 (46 orbits to target). Two answers to "strongest project". Owner decision.
3. Major (robustness, CLS). Figures and Resume hotlinked from Wix, no width/height. If URLs rotate, Resume breaks in header, lede and footers. Needs owner files and real dimensions.
4. Major (credibility). raftar-formula-racing.html line 48: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo. Owner: source it or cut.
5. Minor (SEO). robots.txt is served under /website/, so crawlers ignore it and its Sitemap line is not discovered. Submit sitemap in Search Console (owner). Lastmod identical on all URLs.
6. Minor (LCP). fetchpriority fix landed. Unverifiable offline. Residual: non-first figures use loading="lazy" (fine); keep it off the first figure.
7. Minor (SEO). One og:image for every page.
8. Minor (fonts, CLS). Two Google Fonts, swap, no size-adjusted fallback; needs measured metrics or self-hosting.
9. Minor (looks, taste). Plate only on row 06.
10. Minor (looks, taste). About: empty right side on wide screens until a portrait exists. Boxed "podium finish" stamp opens a gap in its line on tablet (visible in the about-tablet shot, first line of the second paragraph is loose).
11. Minor (UX, phone). Header drops Resume and GitHub; both remain in lede and footer. Acceptable.
12. Minor (UX). Contact is LinkedIn only; single point of failure, owner's choice.
13. Nit (copy). Blurbs share a verb-led cadence; vary only with existing facts.
14. Nit (looks). Small mono labels are the faintest text on tan; pass AA (taste).

Designer-fixable this cycle: none.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent, not generic; no regression from the fetchpriority change. Everything material is still waiting on the owner: a status line, a lead-project decision or snake result, a sourced or cut Raftar claim, and local Resume and images with real dimensions. Nothing designer-fixable remains this cycle; my research this cycle was constrained by blocked page fetches.
