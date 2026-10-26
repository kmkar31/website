# Critique, 2026-10-26 (cycle 22, reviewing main after "cycle 21")

## Sources
WebFetch was attempted this cycle for three primary sources and every request was refused (PROVENANCE_REQUIRED, permission not answered). None was read, so no finding below rests on them. They are listed as pointers only.
- web.dev, Optimize CLS (width/height or aspect-ratio on images): https://web.dev/articles/optimize-cls (blocked)
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
- NN/g, portfolios for hiring managers: https://www.nngroup.com/articles/portfolios/ (blocked)
Topic this cycle: freshness and credibility of content, evidence (media) dependency, UX for a 30-second reader.

Measured: `python3 tools/check.py . agents/shots` on 13 pages x 3 viewports x 2 themes, every line OK (no overflow, tap-target, contrast, alt or h1 failure). "N images not loaded" notes are the sandbox blocking Wix, not a bug. Screenshots viewed: home phone light, home desktop light, About desktop light, snake-robots phone light. Repo checks: `STATUS = ""` still at build/build.py line 257; wixstatic/filesusr references per page: 2 to 9 (404 included); robots.txt, sitemap, canonical, OG/Twitter with absolute local og.png, JSON-LD all present. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). Authored: struck-through "three weeks" in a marker highlight, "For the record" ledger, stamps with real figures, Fig. plates with sheet numbers, plain lede, honest colophon. Residual tells: cream + serif + terracotta is the current "editorial warm" kit; rows 04-09 now all carry a stamp, so the stamp is becoming the template (see 5). No gradients, glass, glow, floating chips, sparkle, stat strip or three-card grid. Moved since last cycle: stamps on rows 07-09 slightly raised sameness; nothing else.
- Looks good: 7/10. Composition, rhythm and type pairing are coherent and the paper/ink/double-rule system is committed. Held back by the one thing the screenshots cannot hide: there is not one real photograph or result image anywhere a viewer can see, so every page is text plus line drawings. The About desktop view leaves roughly a third of the width empty on the right below the first section (taste).
- SEO: 7/10. Title and description per page, one h1, canonical, OG/Twitter with absolute image, JSON-LD, sitemap, robots, 404 noindex are all in place. Open items: alt text on hotlinked figures is generic ("Modular snake robot, figure 1 of 3"), no image width/height, fonts from Google, and the project site cannot serve a host-root robots.txt (cannot verify live).
- UX: 6/10. A recruiter finds who he is and the strongest area fast on phone. Weak: no current status or date (finding 1), only LinkedIn as a contact route, project pages with no outcome or role (finding 3), and the Resume link is not in the phone header.
- Fun and personality: 6/10. Real touches exist (struck-through 3 weeks, 99 s stamp you can hold down, "failed to land on the target" 404, Fig. plates). Beyond those, About and eight of nine project pages read as tidy and neutral. Below 7, so raised as Major (finding 4).

## Owner critique (agents/user-critique.md)
- Retro, matte, flat, warm, print-like, no glossy gradients: met. Paper tones, ink borders, hard offset shadow on the one button, no blur or glow, faint grain. Dark theme is the inverted-print idea and stays coherent. Retro is not costume here: contrast and 44 px targets pass in check.py.
- Must not look AI-generated: met at 3/10. The remaining risk is the stamp pattern and the uniform row anatomy, not the palette.

## Findings (ranked)

1. Major (Blocker for credibility). Stale or missing status and dates. About says "My Master's ... is at Carnegie Mellon University (2023 - 2025)" and the education entry reads 2023 - 2025; today is October 2026 and `STATUS` is still empty, so home has no "where is he now" line. A hiring manager cannot tell if he has graduated, is available, or is still enrolled, and a stale-looking page reads as abandoned. Where: home ledger, About, phone and desktop. Fix (owner only): one sentence, e.g. "Graduated May 2025 / Seeking roles in controls and autonomy starting ..." put into `STATUS`; the slot is ready. I will not invent it. Not fixable by the designer without owner facts.

2. Major. Evidence is hotlinked from Wix and the site shows no real photographs. 2 to 9 Wix/filesusr URLs per page, including the three snake figures on the "Start here" project and the resume.pdf. If Wix reorganises, pages lose all images and the resume link dies; with the sandbox block, screenshots show the pages as they would look with broken media. Also, none of these images has width/height, so on a slow load the layout shifts (CLS risk; source blocked, standard guidance). Fix: owner supplies an assets folder (one hero photo per project, resume.pdf); designer then localises, adds dimensions and alt text. Interim designer step that needs no facts: add `width`/`height` once any image is local; until then nothing more to do.

3. Major. The "Start here" project is the thinnest page. snake-robots (phone) is: title, tl;dr, a question, Lab and Advisor, a schematic, one "Why snake robots" sentence, pager. No result, no role, no method, no number, no video. The page the home page tells people to open first has the least to say, while ARGUS, aerobraking and Hasselhoff have real figures and results. Either the owner supplies two or three sentences on what was done and what happened (preferred), or the "Start here" label should move to a project that already has outcomes (aerobraking: 46 orbits). Editorial call is the owner's; flag it plainly in the next designer response.

4. Major (axis below 7). Fun and personality is concentrated in about five spots. Grounded ideas that use only facts already in the repo, none requiring invention: (a) About: the Seagate bullet and the home highlight already do the struck-through gag; give the Formula Bharat podium the same hand-made treatment on About (the double-border stamp from the home row) so About has one authored mark; (b) the pager "Next" could show the neighbour's stamp instead of its first fact for the three stamped rows, tying the pager to the front page; (c) the 404 joke exists, a one-line equivalent on empty states (e.g. filters with zero results) would be consistent. Trade-off: each addition must stay quiet; prefer one more authored mark on About over several on every page.

5. Minor to Major. Stamp uniformity. Six of nine rows (04 to 09) now carry a stamp, row 01 has the plate, rows 02 and 03 are bare. The stamp was the cure for sameness in cycles 10 to 15 and is now the pattern: a mono pill with a number reads as a template. Two rows with none look unfinished by comparison rather than plain. Suggestion: keep stamps only where the number is the point (99 s, 46 orbits, podium, 500 m) and drop "4 unknowns, fitted" and "Four-bar pedal path", which are labels, not facts. That leaves four stamps plus a plate and removes the template feel. Taste, but evidence-based: the last two stamps do not carry a quantity a reader can use.

6. Minor. Alt text is a placeholder pattern. "Modular snake robot, figure 1 of 3" says nothing about what the image shows (WCAG 1.1.1 asks for the equivalent purpose). Owner must say what each figure shows; until then, captions carry the meaning, so this is low risk.

7. Minor. Contact is one route. Footer: "To get in touch, message me on LinkedIn." plus LinkedIn, GitHub, Resume. This is a stated owner constraint (no public email), so not a defect; note only that a recruiter with no LinkedIn account has no route, and that Resume (PDF) is hidden in the phone header (it remains in the home actions and every footer).

8. Minor. Repetition on the home page at desktop: "Resume (PDF)" appears in the header, the action row and the footer, and LinkedIn in the action row and footer. Fine for findability, but the action row on home could drop LinkedIn since the header icon and footer already carry it. Taste.

9. Minor. About desktop: the 760 px column leaves a wide empty strip to the right of Skills, Education and Experience once the "On this page" index (three links) ends after the intro. The void is documented as the portrait slot; but with no portrait, it is simply empty for about 2000 px of scroll. Option: make the index sticky so it travels with the reader, which is also useful navigation. No content invented.

10. Minor. Fonts: two Google Fonts families with display=swap and no size-adjusted fallback; a flash of different metrics is likely on first load (CLS, unverified offline). Fix needs the real WOFF2 files to self-host. Owner/environment limit.

11. Minor. Snake project phone view: after the plate and one sentence, the page ends with a lot of empty space before the pager; the Fig. 1 caption says "Module count is illustrative", which is honest but also highlights that the drawing is not the real robot. Resolved by finding 2.

12. Nit. "START HERE" is a 12 px mono label with an underline on phone, close to the row index; it is easy to miss next to "01". Contrast passes; it is a hierarchy nit.

13. Nit. Phone home: two lede paragraphs push the primary button below the first viewport at 390 wide (button begins about 1000 px down in the full-page shot). The first paragraph alone answers who/what; the Seagate paragraph could follow the button. Taste, consistent with the 30-second goal.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules under header and above footer, hard shadow on one button only, no blur or gradients, faint grain, inverted-print dark theme.
- Authored specifics: struck-through "three weeks" in marker (home, About), "For the record" ledger, stamps with real figures, Fig. plates with sheet numbers drawn from facts on each page, 99 s pressable stamp, 404 "failed to land on the target", honest colophon.
- Plain lede with real facts; no slogan copy; project titles are full names.
- Accessibility: skip link, aria-pressed filters, modal lightbox with focus return, no nameless Tab stops, row link names are the project title, 44 px targets, scroll-padding for sticky header, reduced-motion handling.
- SEO base: per-page titles and descriptions, canonical, OG/Twitter with absolute image, JSON-LD, sitemap with lastmod, 404 noindex.
- Failed images collapse instead of leaving gaps or orphan captions.

## Verdict
The design is finished enough that the remaining problems are not design problems. The site still has a point of view and avoids the AI look; what limits it now is substance only the owner can supply: a current status sentence (it is October 2026 and the page implies a 2023 to 2025 degree in progress), real images and a local resume instead of Wix hotlinks, and outcomes for the project the site tells people to open first. Designer-side work this cycle is small: trim the two label-only stamps, give About one authored mark, consider a sticky "On this page" index, and say plainly in the log that findings 1 to 3 are blocked on the owner. Sources this cycle could not be read; nothing here depends on them.
