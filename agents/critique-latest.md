# Critique, 2026-11-08 (cycle 101)

Rendering: `python3 tools/check.py . agents/shots` ran to completion: 78 lines (13 pages x phone/tablet/desktop x light/dark), all OK, only "images not loaded" sandbox notes. I viewed index phone light, index desktop light, snake-robots phone dark. No site files edited. HEAD f7682ca (log-only; no site change since cycle 97). No regression seen.

## Sources consulted
Honest limit: WebFetch was blocked this cycle (permission not granted) for the three pages I tried, so none of these were read in full. I treated them as pointers only; no finding depends on them.
- Blocked, not read: https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html , https://web.dev/articles/font-best-practices , https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- Search result only (titles and snippets, not opened): https://web.dev/articles/css-size-adjust (size-adjust for fallback fonts to reduce font-swap CLS); https://developer.chrome.com/blog/framework-tools-font-fallback
- Carried from cycle 100 (read then): WCAG 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; web.dev Optimize CLS (set width/height on images); NN/g portfolio videos https://www.nngroup.com/videos/ux-portfolios-hiring/
- Topic this cycle: font loading and fallback metrics, focus visibility, reduced motion. Local evidence: build.py has a prefers-reduced-motion block (line ~743) and a JS guard (line ~848); fonts load from Google Fonts with swap.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, strike-through "three weeks" on amber, stamps, Fig./Sheet captions, mono ledger, plain first-person lede. No gradients, blur, glow, stats strip, card trio or slogan. Residual: intro / ruled list / dark footer band is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. Ruled rhythm holds in both themes; dark reads as inverted print. Weak spots: row 06 is the only row with a plate (on phone it sits above the title and breaks list rhythm); snake page is a large plate, one question, one sentence, then the pager (under-filled); About desktop right third empty.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, 404, one h1. Unchanged risks: robots.txt and sitemap under /website/ subpath, one og:image for all pages, hotlinked figures without dimensions, identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are all on the first phone screen. Held down by no current status and no result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, ledger. Home is otherwise quiet; nothing to add that is not already in the repo.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat surfaces, hard shadow, grain, inverted-print dark).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" are read against today (2026-11-08) with no status line rendered. A recruiter cannot tell graduated, working or available. Owner must supply one line; the STATUS slot is ready.
2. Major (UX, 30-second test). Lede and row 01 lead with snake robots; the page (viewed, phone dark) has a schematic, a question and a one-sentence "Why snake robots", no result. "Start here" is on row 06. Two answers to "strongest project", and the lede's answer is the thinnest. Owner: supply a snake result or choose the lead.
3. Major (robustness, CLS). Figures and Resume are hotlinked from Wix (wixstatic.com, filesusr.com; 3 references on index, about and snake each), no width/height. Unsized images shift layout; if URLs rotate, the Resume link breaks in header, lede and footers. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). Raftar question: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" (raftar-formula-racing.html) has no support in the repo. Owner: confirm with a source or cut.
5. Minor (SEO). robots.txt and sitemap sit at a project-site subpath; crawlers read robots.txt only at the host root. Submit the sitemap in Search Console (owner). Identical lastmod. Not re-verified against Google docs.
6. Minor (SEO). One og:image for every page.
7. Minor (fonts, CLS). Two Google Fonts with swap and no size-adjusted fallback (web.dev css-size-adjust pointer, unread). Needs measured metrics or self-hosted files; guessed numbers could worsen shift.
8. Minor (looks). Plate on one row only; add plates only with real figures (taste).
9. Minor (looks). About desktop empty right third until a portrait exists (taste).
10. Minor (UX, phone). Header drops Resume and GitHub on phones; both remain in lede and footer. Acceptable.
11. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
12. Nit (looks). Small mono labels are the faintest text on tan; pass AA (taste).

Designer-fixable this cycle: none I can evidence.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, color-scheme and theme-color.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local, honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets, reduced-motion handling.

## Verdict
Authored, coherent and not generic; no regression and no designer-fixable defect that I can evidence. What is open waits on the owner: a current status line, a snake result or lead-project decision, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. External research this cycle was limited by blocked fetches and added no new findings.
