# Critique, 2026-10-28 (cycle 38, reviewing main at cecb3bb)

## Sources
- WebFetch was attempted this cycle for web.dev optimize-cls, NN/g "How users read on the web" and WCAG 2.2 target-size-minimum. All three were blocked (permission not answered). Nothing below rests on a page I read. These are pointers only:
  - https://web.dev/articles/optimize-cls (image dimensions, font swap)
  - https://www.nngroup.com/articles/how-users-read-on-the-web/ (scanning)
  - https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 px minimum; site uses 44 px)
  - https://www.w3.org/WAI/WCAG22/Understanding/non-text-content (alt text)
- Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", a sandbox limit).
- Viewed: home phone light, About tablet light, Hasselhoff desktop dark. Fonts do not load in the sandbox, so screenshots show fallback serif.
- Grepped: no wixstatic in index.html; og:image is absolute (assets/og.png); snake-robots figures are still wixstatic hotlinks with generic alt.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan. Authored specifics remain: struck-through "three weeks", "For the record" ledger, outcome stamps, Fig./Sheet N of 9 plates, honest colophon. Residual risk: cream paper + serif + terracotta + mono small caps is a recognisable editorial kit. Tells moved: none.
- Looks good: 7/10. Desktop pages are calm and well ruled. Phone home is a long list of nine evenly weighted rows and its first image is a line-drawn placeholder plate. The Hasselhoff plate and the stamp are the best moments.
- SEO: 8/10. Unique titles and descriptions, one h1, canonical, OG, JSON-LD, sitemap, 404. Sitemap and robots sit under a project subpath (owner: Search Console). Not verifiable offline: og:image fetch, Wix image weight.
- UX: 7/10. Name, specialty, strongest facts, Resume and LinkedIn are on the first phone screen. Lowered by LinkedIn-only contact, Resume as a Wix hotlink, no status or date.
- Fun and personality: 7/10. Struck "three weeks", "Time allowed: 99 s", the SpongeBob naming on Hasselhoff, 404 joke. Quiet otherwise.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, double rules, hard-shadow button, dark theme reads as inverted print.
- Not AI-looking: met at 3/10. Remaining risk is repeated marks, not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No status or date. About says CMU "2023 – 2025", today is October 2026, and nothing says graduated or available. `STATUS` in build/build.py is empty. One owner sentence fixes it.
2. Major (owner decision). "Start here" sits on row 01 (Snake), the project with the least evidence of what he did or what happened. Supply an outcome, or move the label to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and every project figure are Wix hotlinks. A dead Resume link is the worst failure for a recruiter. Figures lack width/height, so layout shift is likely. Needs local files.
4. Major (content, owner facts). Raftar says he "did the suspension and brakes" with no component, number or result; the figure is generic.
5. Minor (new, designer-fixable). UI chrome (header nav, Resume, buttons, filters, footer, pager labels, crumb) is set in `--sans: system-ui`, visible in the Hasselhoff screenshot as a modern UI sans against the DM Serif and mono print system. It is the one non-print voice on the page and renders differently per OS (San Francisco, Segoe, Roboto). The colophon names only DM Serif Display and Source Serif 4, so it is also slightly inaccurate. Option: set nav and buttons in the mono already used for labels (or Source Serif 4 semibold small caps as the crumb already does) and keep the colophon true. Taste, but it is the largest remaining coherence gap and needs no owner input. Trade-off: mono at 0.9rem on 44 px targets is fine for contrast; check the header fits one row on phone.
6. Minor (content consistency, owner). Home says "I captained the Formula SAE team", About says "contributed to" and "led the team", Education says "Captain". Pick one verb.
7. Minor (verify). The Raftar Ferrari comparison is unverifiable here. Owner should confirm wording and numbers.
8. Minor. Alt text on Wix figures is generic ("Modular snake robot, figure 1 of 3"). Owner must say what each shows.
9. Minor. Two Google font families with display=swap and no size-adjusted fallback; reflow on first load likely. Needs real font files to self-host.
10. Minor (taste). Outcome stamps appear on some home rows only (04 to 07); rows 01 to 03, 08, 09 have none. Add none without real numbers.
11. Minor. Contact is LinkedIn only (owner constraint). Conversion risk, not a defect.
12. Nit (taste). Snake placeholder plate is the first image on phone and reads as a stand-in. A real lab photo is the biggest looks-good upgrade (owner file).
13. Nit (taste). About desktop leaves the right third empty with no portrait. Accepted earlier.

Fun ideas from repo facts only: Hasselhoff tab title as the "Time allowed: 99 s" stamp; Seagate strike-through press state revealing "15 minutes". Optional taste.

Regression check: cycle 37 fix verified on About tablet: "podium finish" is one box on one line. No regressions seen.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules, one hard-shadow button with press state, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, colophon.
- Plain lede with real facts; blurbs that name the specific thing done; prev/next pager with a fact on each.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, scroll-padding for the sticky header.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The site commits to retro matte without becoming costume and does not read as generated. The one designer-fixable item is new: the system-ui sans for navigation and controls sits outside the print type system and contradicts the colophon (finding 5). Everything else that limits it needs the owner: a status sentence, local Resume and images with dimensions and real alt text, real outcomes for Snake and Raftar, one verb for his Raftar role, confirmation of the Ferrari claim, and a real photo in place of the placeholder plate.
