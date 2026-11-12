# Critique, 2026-11-12 (cycle 121)

Rendering: `python3 tools/check.py . agents/shots` completed; every page OK, with only "images not loaded, sandbox network" notes. HEAD 7e8a309 is log-only, so site source is unchanged since cycle 117 and there is no regression. I viewed index (phone light, desktop light), snake-robots (phone dark), about (tablet light) and aerobraking-drl (desktop light). I also ran a Playwright WCAG text-spacing test, a no-JS load and a tap-target scan. I edited no site files.

## Sources consulted
Fetched and read:
- Nielsen Norman Group, UX design portfolios: https://nngroup.com/articles/ux-design-portfolios/ (hiring managers rarely read a whole portfolio; they want context, role, constraints and rejected options; 3 to 5 strong projects beat many weak ones)
- W3C, Understanding SC 1.4.12 Text Spacing: https://w3c.github.io/wcag/understanding/text-spacing (line height 1.5, paragraph spacing 2x, letter spacing 0.12em, word spacing 0.16em must not cause loss of content)
Search-result pointers only (not opened; page not verified):
- Google, robots.txt creation: https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt (fetch was blocked; the root-only rule is from my memory of the spec)
- WCAG 2.2 Understanding index and 1.4.10 Reflow: https://www.w3.org/WAI/WCAG22/understanding/
Topics this cycle (new versus cycle 120): portfolio project curation, text-spacing/reflow, project authorship clarity.

## Scores
- AI-tell: 2/10, unchanged. Paper tone, double rules, hard-offset button, struck-through "three weeks" on amber, stamps, mono ledger and the DM Serif/Source Serif pairing read as authored. Copy is plain first person. Remaining tell: the familiar shape (intro, ruled list, dark footer). No tell moved.
- Looks good: 8/10. Desktop home has a clear measure, rhythm and one strong accent. The aerobraking page is orderly (stat row, plate, sections, pager). Weak spots: the lone plate on row 06 and the bare rows beside it; long text-only stretches on project pages.
- SEO: 7/10, unchanged (findings 6 and 7).
- UX: 6/10. Name, field, lede, Resume and LinkedIn fit on the first phone screen. Held down by no current status, an ambiguous lead project, and nine undifferentiated projects.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, Fig. 1 plate with "Sheet n of 9", "For the record". Nothing new proposed; the repo holds no further facts.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met. No gradient, blur or glow in any screenshot.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (credibility, new angle). The "Start here" project, aerobraking-drl, mixes his work with someone else's and never separates them. Setup says "This project builds off work done by Falcone et al." and Method says "Falcone et al. simulated their agent ... required a training time of 1 week on a 50 core cluster". Then the Result says "our NN state-space model" and "the trained agent returned ... 8.4 km". A professor will ask what Karthik did. Add one plain sentence stating his contribution (for example, which parts he trained, reproduced or changed). Only the owner can supply it. NN/g wants the "role" for each case study (https://nngroup.com/articles/ux-design-portfolios/). Without it, the strongest-looking page reads as a summary of a paper.
2. Major (UX, 30-second test). The lede and row 01 lead with snake robots, whose page states no result (phone and desktop screenshots; it has a schematic, a lab and an advisor, plus a "Why snake robots" paragraph). "Start here" and the only plate sit on row 06. That gives two answers to "strongest project". Owner decision: move "Start here" to row 01, or give the snake page a result.
3. Major (UX, credibility). `STATUS = ""` in build/build.py:262. The subtitle says MS at CMU and About says 2023 to 2025. Today is 2026-11-12 and there is no status line. A visitor cannot tell whether he has graduated, is working or is looking. The owner must supply one line.
4. Major (robustness). Images and the Resume link are hotlinked from Wix (76 wixstatic references across the pages). Resume is the main recruiter action and sits in the header, lede and footer, so one Wix change breaks all three. It needs a local resume.pdf and local photos from the owner. Not verifiable offline.
5. Major (credibility). The Raftar page says "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time", with no source. Source it or cut it.
6. Minor (UX, new). Nine projects with equal weight on Home. NN/g advises 3 to 5 strong projects. The ledger format keeps the list scannable, so this is not a defect. Do consider a visible tier, for example a short "Selected" group of 3 above "Also". The owner picks which three. Taste plus the NN/g evidence.
7. Minor (SEO). robots.txt and sitemap.xml are served under the /website/ subpath. Google reads robots.txt at the host root only (from memory of the spec; I could not open the doc), so it is probably ignored. The sitemap works if submitted in Search Console. All 12 lastmod values are identical (2026-11-02). There is no per-project og:image, only the shared og.png. Wix figures lack width/height, so CLS is likely once they load. Needs the owner (custom domain or Search Console) and real image dimensions.
8. Minor (accessibility, new). Under the WCAG 1.4.12 text-spacing override at 320 px width, the header theme button overflows by 14 px (scrollWidth 334 vs 320) on every page I tested. At 390 px nothing overflows. This is a designer-fixable robustness issue: let the header wrap or hide the brand text below about 340 px, or allow the nav to shrink. Without the override I did not confirm overflow at 320 px, so treat severity as low. Source: https://w3c.github.io/wcag/understanding/text-spacing
9. Minor (looks, taste). The plate appears on row 06 only; the other rows read thin on desktop. About has an empty right area on wide screens.
10. Minor (UX). Contact is LinkedIn only (owner's choice). The phone header drops Resume and GitHub; they stay in the lede and footer.
11. Nit (copy). Row blurbs share a verb-led cadence ("Trained...", "Landed...", "Compliant..."). Vary only with facts already present.
12. Nit (looks). Small mono labels are the faintest text on tan and dark. They pass AA in check.py, so this is taste.

Designer-fixable this cycle: finding 8 only (low severity). Everything else needs the owner (status line, lead project, contribution sentence, Raftar claim, local Resume and images).

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber, and the stamps (46 orbits, 500 m, 99 s, podium).
- Fig. 1 plate with "Sheet n of 9" caption and honest "schematic" notes.
- Plain first-person lede with real specifics, no slogan copy.
- Aerobraking page structure: stat row, plate, problem/setup/method/result, and a pager that shows the neighbour's first fact.
- Failed images collapse cleanly; one h1 per page, unique titles, JSON-LD, canonical, 404 joke, skip link, focus-visible outline, reduced-motion handling, no-JS pages render fully (24 links, one h1), no overflow at 390 px.
- About's ruled, dated education and experience entries.

## Verdict
The site is authored, coherent and not generic, and nothing has regressed. The new concern is credibility on the project the site itself points to: the aerobraking page does not say what Karthik did versus Falcone et al., which matters more than polish for a professor reading it. The older owner items still stand: a status line, a decision on the lead project, a sourced or cut Raftar claim, and a local Resume and images with real dimensions. The designer can fix only the 320 px header overflow under text-spacing; the rest waits on the owner.
