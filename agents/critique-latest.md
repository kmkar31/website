# Critique, 2026-11-09 (cycle 108)

Rendering: `python3 tools/check.py . agents/shots` completed: 78 OK, 0 FAIL, only sandbox "images not loaded" notes. I viewed index phone light and index desktop light. `git status` was clean and the last commit touched only logs, so no regression is possible. No site files edited.

## Sources consulted
- Read: https://web.dev/articles/fetch-priority (fetchpriority="high" on the LCP image starts it at High instead of Low; Google Flights LCP 2.6 s to 1.9 s).
- Read: https://developers.google.com/crawling/docs/robots-txt/create-robots-txt (robots.txt must sit at the host root; "It cannot be placed in a subdirectory").
- Blocked: https://web.dev/articles/optimize-cls (permission not answered). I cite it only from earlier cycles. The NN/g portfolio search returned titles only, so I cite nothing from it.
- Topic this cycle: LCP priority and robots.txt placement, now with sources actually read.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, strike-through "three weeks" on amber, stamps, Fig. caption, mono ledger, plain first-person copy. No gradient, blur, glow, stats strip, card trio or slogan. Residual: intro / ruled list / dark footer is a familiar shape. No tell moved.
- Looks good: 8/10. The ruled list holds on phone and desktop. Weak spots: one plate (row 06) in nine rows, so on phone it sits above the title and breaks the list rhythm; the lead project has no real image; About has an empty right side on wide screens.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Open: robots.txt at a subpath (now confirmed ineffective, see 5), one og:image, unsized hotlinked figures, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plate, ledger. Home is otherwise quiet. I have no new idea that the repo's facts support.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read on 2026-11-09 with no status line. A recruiter cannot tell graduated, working or available. Owner must supply one line; the STATUS slot is ready.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result, while "Start here" sits on row 06 (aerobraking, "46 orbits to target"). Two answers to "strongest project"; the lede's is the thinnest. Owner decision: supply a snake result or pick the lead.
3. Major (robustness, CLS). Figures and Resume are hotlinked from Wix with no width/height. If the Wix URLs rotate, Resume breaks in header, lede and both footers. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). raftar-formula-racing.html: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo. Owner: confirm with a source or cut.
5. Minor (SEO), source now read. Google says robots.txt "cannot be placed in a subdirectory". Here it is served under /website/, so crawlers ignore it. This is harmless, since `Allow: /` is the default, but the Sitemap line in it is also not discovered. Fix: submit the sitemap in Search Console (owner) or move to a user-site root. Lastmod is identical on every URL.
6. Minor (LCP), source now read. aerobraking-drl.html: the first figure has `decoding="async"` but no `fetchpriority="high"` and no width/height. On project pages with a Wix first image, adding `fetchpriority="high"` to the first figure is a safe, fact-free designer change per web.dev; the attribute does not need dimensions. Not verifiable offline because Wix images do not load here. Check that no above-the-fold image carries `loading="lazy"`.
7. Minor (SEO). One og:image for every page.
8. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback. Needs measured metrics or self-hosted files.
9. Minor (looks). Plate on row 06 only; add plates only with real figures (taste).
10. Minor (looks). About on wide screens: empty right side until a portrait exists (taste). The boxed "podium finish" stamp in running text opens a gap in its line (taste).
11. Minor (UX, phone). Header drops Resume and GitHub on phones; both remain in lede and footer. Acceptable.
12. Minor (UX). Contact is "message me on LinkedIn" only; single point of failure, owner's choice.
13. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
14. Nit (looks). Small mono labels are the faintest text on tan; they pass AA (taste).

Designer-fixable this cycle: item 6 only (add `fetchpriority="high"` to the first above-the-fold figure on project pages that have one; do not add dimensions without real values).

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plate with "Sheet n of 9" caption, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent and not generic; no regression. Almost everything open waits on the owner: a current status line, a snake result or lead-project decision, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. This cycle's research did produce one small designer-fixable item (fetchpriority on the first figure) and confirmed that the robots.txt subpath placement is ineffective, so the sitemap should be submitted by hand.
