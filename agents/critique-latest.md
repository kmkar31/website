# Critique, 2026-11-12 (cycle 122)

Rendering: `python3 tools/check.py . agents/shots` took longer than 2 minutes but finished with rc=0 and zero FAIL lines. Only "images not loaded, sandbox network" notes appeared. HEAD is f6868d9 (the 320 px header fix). I viewed index (phone light, desktop dark), about (tablet dark) and quadrotor-sysid (phone light). I also inspected the HTML and CSS. I edited no site files.

## Sources consulted
WebFetch was blocked this cycle ("permission request not answered"), so nothing below was opened and read. These are search-result pointers only. I used them for the principle each one is known for, and I treat the principles as unverified until someone opens the pages.
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls (set width/height or aspect-ratio on images and media)
- W3C, Understanding SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 by 24 CSS px minimum, with exceptions)
- Nielsen Norman Group, F-shaped reading pattern: https://nngroup.com/articles/f-shaped-pattern-reading-web-content/ (visitors scan the left edge and first words of lines)
Carried over from cycle 121: the NN/g portfolio article and the W3C text-spacing page, which were fetched then.
Topics this cycle (new versus 121): CLS and LCP on hotlinked images, tap-target minimum, left-edge scanning of the project list.

## Scores
- AI-tell: 2/10, unchanged. The paper palette, double rules, hard-offset button, struck-through "three weeks" on amber, stamps, mono ledger and the DM Serif/Source Serif pairing read as authored. The copy is plain first person. The remaining tell is the familiar shape (intro, ruled list, dark footer). No tell moved.
- Looks good: 8/10. The desktop dark home has a clear measure, a ledger sidebar and one amber accent. The About tablet page is orderly. Weak spots: the lone plate on row 06, text-only stretches on project pages (sysid Background is about 20 lines of generic prose on phone), and an empty lower-right area on wide screens.
- SEO: 7/10, unchanged. Unique titles, canonical, JSON-LD, local og.png, sitemap, 404 are all present. Held down by subpath robots.txt and identical lastmod (finding 7).
- UX: 6/10, unchanged. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no status line, an ambiguous lead project and nine equal projects.
- Fun and personality: 7/10, unchanged. 99 s stamp, 404 joke, strike-through, "Sheet n of 9" caption, "For the record". The repo holds no further facts to build on.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. I saw no gradient, blur or glow in any screenshot, light or dark.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (credibility). The aerobraking page ("Start here") does not separate Karthik's work from Falcone et al. Setup says the project "builds off work done by Falcone et al." and Method describes what "Falcone et al. simulated". The Result then says "our NN state-space model". A professor will ask what he did. One plain sentence from the owner fixes it. Reopened because nothing has changed: this is the page the site points to as the best project.
2. Major (UX). Row 01 and the lede lead with snake robots, whose page states no result. "Start here" sits on row 06. That gives two answers to "strongest project". Owner decision: move "Start here" to 01, or give the snake page a result.
3. Major (UX). `STATUS = ""` at build/build.py:262. The site says MS at CMU, 2023 to 2025, and today is 2026-11-12. There is no line saying whether he has graduated, is working or is looking. The owner must supply one line.
4. Major (robustness and performance). The Resume link and every figure are hotlinked from Wix: 76 references across the pages (aerobraking-drl alone has 9). No `<img>` I inspected has width/height, so CLS is likely once they load (web.dev optimize-cls, unverified pointer). New detail: `aerobraking-drl.html` marks its first hotlinked figure `fetchpriority="high"` with no dimensions. LCP therefore depends on a third-party host and reserves no space. If the owner supplies local images with real dimensions, keep the high priority on the hero plate only. Until then the hint gains nothing. This needs owner files and cannot be verified offline.
5. Major (credibility). The Raftar page asks "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" with no source. Source it or cut it. Owner fact.
6. Minor (UX, taste plus NN/g evidence). Nine projects at equal weight. The ledger stays scannable, but a short "Selected" group of 3 above "Also" would help a 30-second reader. The owner picks the three.
7. Minor (SEO). robots.txt and sitemap.xml sit under /website/, and Google reads robots.txt only at the host root, so it is probably ignored. Submit the sitemap in Search Console. All 12 lastmod values are 2026-11-02. There is only the shared og.png, with no per-project card. Owner action.
8. Minor (accessibility, new check, passes). I looked for tap-target risk (WCAG 2.5.8 needs at least 24 px). Header links and buttons are 44 px by design, and the 359 px rule from cycle 121 keeps the 44 px height. The text-only "Resume (PDF)" and "LinkedIn" links in the lede are inline links and so are exempt. No change needed. I record this so the designer does not reopen it.
9. Minor (looks, taste). The plate appears only on row 06, so the other rows read thin on desktop. About has empty space at lower right on wide screens.
10. Minor (UX). Contact is LinkedIn only, which is the owner's choice. The phone header drops Resume and GitHub; they remain in the lede and footer.
11. Nit (copy). Row blurbs share a verb-led cadence. Vary only with facts already present.
12. Nit (looks). The small mono labels are the faintest text. They pass AA, so this is taste.

Designer-fixable this cycle: nothing. Everything above needs the owner (status line, lead project, contribution sentence, Raftar claim, local Resume and images with dimensions).

## Good, must not regress
- The retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- The struck-through "three weeks" on amber, and the stamps (46 orbits, 500 m, 99 s, podium).
- The Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" notes.
- The plain first-person lede with real specifics and no slogan copy.
- The aerobraking page structure and a pager that shows the neighbour's first fact.
- Failed images collapse cleanly. One h1 per page, unique titles, JSON-LD, canonical, 404 joke, skip link, focus-visible outline and reduced-motion handling all hold.
- About's ruled, dated education and experience entries.
- The 320 px header fix from cycle 121 (no regression seen at the three standard viewports).

## Verdict
The site is authored, coherent and not generic, and I found no regression from cycle 121. The open problems are content the owner must supply: a status line, a decision on the lead project, a sentence separating his work from Falcone et al., a sourced or cut Raftar claim, and local Resume and images with real dimensions. The one new point is that the Wix-hosted hero figure carries a high-priority hint and no dimensions, so the page's main image has no reserved space and a third-party dependency. The designer has nothing left to fix, and the site's next gains depend on the owner.
