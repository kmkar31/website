# Critique, 2026-11-15 (cycle 142)

Method: `python3 tools/check.py . agents/shots` ran to completion: 0 FAIL, only "images not loaded, sandbox network" notes. No site files edited (git status clean after the run). HEAD is e8da946 (cycle 141). I opened 7 of 78 screenshots: index phone-light, index desktop-dark, projects desktop-light, raftar phone-light, tethered tablet-dark, snake-robots desktop-light, about phone-dark. The other 71 were not opened. I read source for the Wix-image count, alt text, STATUS, sitemap and font loading.

## Sources consulted
Read (WebFetch, content actually retrieved):
- web.dev, Optimize Cumulative Layout Shift, https://web.dev/articles/optimize-cls : "Always include width and height size attributes on your images and video elements"; if you cannot, reserve space with CSS `aspect-ratio`. Web fonts: fallback swap and invisible text both cause shifts; choose a fallback whose metrics match, preload critical fonts.
- W3C, Understanding SC 2.5.8 Target Size (Minimum), https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html : 24 by 24 CSS px, with spacing, equivalent, inline, user-agent and essential exceptions.
- NN/g, UX design portfolios, https://nngroup.com/articles/ux-design-portfolios/ : hiring managers "don't have a lot of time", "very rarely" read a portfolio word for word; case studies should state outcome and "your specific role in the project". It is about UX portfolios, so it applies by analogy.
Searched but not read beyond titles: portfolio and hiring-manager query results other than the NN/g page.
Not met: variety. This is the third cycle in a row covering portfolio content, CLS and target size; no new topic (for example dark-mode design, reduced motion, social cards) was researched.

## Scores
- AI-tell: 2/10, unchanged. Reasons for the low score: struck "three weeks" on amber, stamps carrying real numbers ("500 M OF TETHER", "TIME ALLOWED: 99 S"), "Sheet n of 9 . NTS" plates, plain first-person lede, no gradient, blur or glow. Residual tells: every project page has the same skeleton (question line, two-cell fact strip, Fig. 1 on graph paper, short body), and the tidy triplets in the ledger ("Seagate, York University, Tube Investments"; "MPC, PPO, system ID, STM32, ANSYS"). Nothing moved since last cycle.
- Looks good: 8/10, unchanged. Home phone-light has a clear order (name, role line, two paragraphs, one hard-shadow button, ledger, rows). Weak: snake-robots desktop-light is about 40 percent empty paper below the plate (Wix photos not loading here, but the page is thin even with them); About phone-dark has big dead gaps (about 70 px) between the section blocks.
- SEO: 7/10, unchanged. Unique titles, canonical, OG, JSON-LD, absolute og:image, sitemap present. Held down by 33 wixstatic references across 11 pages, none of the `<img>` tags I inspected (snake-robots) has width and height, one shared OG card, sitemap and robots under the `/website/` subpath, and the font swap with no matched fallback (all as web.dev above). I could not verify LCP or CLS offline.
- UX: 6/10, unchanged. 30-second phone test: name, subject (control of robots and spacecraft), advisor, Resume, LinkedIn, yes. Status, graduation year, "available or not": no. The page behind row 01 gives no result.
- Fun and personality: 7/10, unchanged. Stamps, struck text, 99 s pressable stamp, 404 joke. No new moment of delight this cycle.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all seven screenshots (paper tone, grain, double rules, hard-shadow button, amber-on-umber dark mode, no blur or gradient anywhere).
2. Must not look AI-generated: met. Caveat is taste only: the repeated project-page skeleton. No new owner notes.

## Ranked findings
1. Major (UX, credibility). The flagship page is still the thinnest. snake-robots.html (desktop-light viewed) is: tl;dr, one-line question, Lab and Advisor strip, a schematic, one two-sentence section "Why snake robots", a link. The home lede and row 01 sell it first; the page that opens has no method, result, duration or role beyond "I implemented". NN/g (above): state outcome and your specific role. Designer-fixable part is exhausted (cycle 141 tried a "What I did" section and reverted it as a duplicate of the tl;dr). Owner supplies 2 to 3 sentences: what was implemented, on what hardware, what happened.
2. Major (UX, credibility). No status or dates on Home. Home says "MS Mechanical Engineering, Carnegie Mellon University" (phone-light and desktop-dark) with no years; About says 2023 to 2025; today is 2026-11-15. `STATUS = ""` at build/build.py:266. A recruiter cannot tell student, graduate or available. Owner supplies one line.
3. Major (credibility). Tense mismatch with 2: Home uses the present ("I research compliant control of snake robots"), About's range is closed. Owner fact; tense follows the status.
4. Major (UX). Two answers to "strongest project". The lede names snake robots; the START HERE mark and plate are on row 06, Aerobraking (index phone-light and desktop-dark). Defensible because row 06 is the fuller page, but the page then tells the reader the featured project is not the one in the lede. Owner decides which, then the other signal changes.
5. Major (performance, robustness). Wix hotlinks: 33 references over 11 pages (aerobraking 7, sysid 5), the Resume PDF is also third-party hosted, and `<img>` tags lack width and height (web.dev above). If Wix changes URLs, all figures and the resume vanish silently, and in my sandbox every project figure was absent, leaving pages like snake-robots and Raftar (phone-light viewed) with one drawing and no photograph. Owner supplies files; a designer cannot guess dimensions.
6. Major (credibility). Aerobraking does not separate his contribution from the cited prior work; the text describes "the trained agent" without saying what he built. Owner fact.
7. Major (credibility). Raftar question line (raftar phone-light viewed): "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" is unsourced and sits as the page's second sentence. Cite or cut. Owner fact.
8. Minor (credibility, clarity). Tethered page (tablet-dark viewed): "nearly 40,000 objects" and "98% shrapnel" carry no source or date, and "cars, hubcaps and shrapnel" is unexplained jargon for a first-time reader (cars presumably means car-sized objects; I will not assume). The 98 percent pull-out gives an unsourced figure prominence. A source link and a date from the owner would fix it; alternatively soften "98%" in the pull-out to attribute it ("per the project text").
9. Minor (UX). LinkedIn is the only contact route, repeated in the footer of every page. Owner constraint, unchanged.
10. Minor (UX, IA). Home and Projects list the same nine rows in the same order (projects desktop-light has filters, otherwise identical). Rows 02, 03, 08, 09 have no stamp, and "Build" as a tag covers a car, a submarine and a tricycle, so filtering by it does not say much. Taste plus owner facts.
11. Minor (content). Tethered and ARGUS state aims and method but no outcome. Owner fact.
12. Minor (accessibility, SEO). Image alt text is now content-based on snake ("Photograph of a modular snake robot", "second view", "third view"), which is better, but the second and third are still near-identical for search and screen readers. I cannot see the images, so I will not propose wording.
13. Nit (looks). About phone-dark: section gaps (Skills to Education to Experience) are about 70 px against about 24 px inside blocks; it reads loose compared with the tight Home phone. Taste.
14. Nit (looks, taste). About desktop leaves the right third empty (carried from earlier cycles, not re-viewed this cycle; the designer has accepted it).
15. Nit (process). Findings 1 to 8 have been the same list for well over 100 cycles and are all owner-blocked. Further designer cycles will not move the scores until the owner supplies the status line, the snake outcome, the Ferrari source, the aerobraking contribution, and files for the resume and images.

## Good, must not regress
- Retro matte system (paper, grain, double rules, hard offset shadows, inverted-print dark mode).
- Struck "three weeks" on amber, stamps that carry a real number, boxed "podium finish" on About.
- Fig. 1 plates with "Sheet n of 9 . NTS" and honest "not to scale / illustrative" captions; the tethered plate with the bracket is clear.
- Pager showing the neighbour's first fact; no wraparound; "All projects" back link.
- Plain first-person lede, "For the record" ledger, honest colophon, 404 joke.
- Unique titles, canonical, JSON-LD, skip link, 44 px phone targets (well above the 24 px minimum), filter chips hidden without JS.
- Raftar page after cycles 139 and 140: the "My part" paragraph now states his role once.

## Verdict
The site is authored, coherent and clearly not a template, and I saw no regression in the seven screens I opened. Scores are flat because every remaining weakness is a missing owner fact or file: no status line, a bare flagship page, an unsourced Ferrari claim, an unseparated aerobraking contribution, and Wix-hosted media and resume. Two things are new this cycle and small: the tethered page's unsourced debris figures now get a pull-out that gives them extra weight, and the research here again covered familiar ground rather than a new topic. Caveats: 7 of 78 screenshots viewed; no measurement of real LCP or CLS; Wix images never loaded, so photographic quality is unjudged.
