# Critique, 2026-10-28 (cycle 37, reviewing main at f215fab)

## Sources
- Not fetched this cycle. I did not load WebSearch/WebFetch, so the links below are references I know, not pages I read now. Treat them as pointers, not fresh verification.
  - Hiring-manager scanning of portfolios (outcomes, role, next step): https://www.nngroup.com/articles/how-users-read-on-the-web/ and https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/
  - CLS from images without dimensions and from font swap: https://web.dev/articles/optimize-cls and https://web.dev/articles/css-size-adjust
  - Link purpose and alt text: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content and https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured
- Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", a sandbox limit). Took 2m26s.
- Viewed: home phone light, home desktop light, Aerobraking phone dark, About tablet light. Fonts do not load in the sandbox, so screenshots show the serif fallback. Live site not checked.
- Greps: one h1 per page; titles unique; robots.txt and sitemap present; scroll-padding-top:80px present in assets/style.css line 23.

## Correction to the previous critique
Last cycle's finding 5 (no scroll-padding) was wrong. `html{scroll-padding-top:80px}` exists. Withdrawn. The designer was right.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan. Authored specifics hold: struck-through "three weeks", "For the record" ledger, outcome stamps, Fig. N of 9 plates, honest colophon. Residual risk: cream paper + serif + terracotta + mono small-caps is a recognisable editorial kit, and the stamps repeat. Tells moved: none.
- Looks good: 7/10. Home desktop is calm and well ruled. Phone home is a long, evenly weighted list of nine rows, and the first image is a five-dot placeholder plate. Aerobraking phone is a very long scroll but the ledger and mono block break it up.
- SEO: 8/10. Unique titles and descriptions, one h1 per page, canonical, OG, JSON-LD, sitemap, 404. robots.txt and sitemap sit under a subpath (owner: submit sitemap in Search Console). Not verifiable offline: og:image fetch, Wix image weight.
- UX: 7/10. Name, specialty, strongest facts, Resume and LinkedIn are visible on the first phone screen. Lowered by LinkedIn-only contact, Resume as a Wix hotlink, no status or date.
- Fun and personality: 7/10. The struck-through "three weeks", stamps, "Time allowed: 99 s" and the 404 joke carry character. Quiet otherwise. Not raised: ideas below use only repo facts.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, hard-shadow button, double-ruled header and footer, no blur or gradient; dark theme reads as inverted print.
- Not AI-looking: met at 3/10. Remaining risk is repetition of marks, not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No status or date. About says CMU "2023 – 2025", it is October 2026, and the site gives no "graduated" or "available" line. A recruiter cannot tell if he is available. `STATUS` in build/build.py (line 259) is empty. One owner sentence fixes it.
2. Major (owner decision). "Start here" sits on row 01 (Snake), the page with the least evidence of what he did or what happened. Either supply an outcome or move the label to a project that has numbers (Aerobraking: 46 orbits; Hasselhoff: 99 s).
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and every project figure are Wix hotlinks (static.wixstatic.com). A dead Resume link is the worst failure for a recruiter. Figures have no width/height, so layout shift is likely (web.dev optimize-cls). Needs local files.
4. Major (content, owner facts). Raftar says he "did the suspension and brakes" with no component, number or result; the figure is a generic car. Owner should supply one concrete thing he designed.
5. Minor (new, designer-fixable). The About podium mark is a 4px double border that wraps over two lines on tablet (viewed), leaving two stacked boxes with the fragment "podium finish at / Formula Bharat 2023." The clone-decoration fix from cycle 25 works, but the wrapped result looks like two separate stickers. Options: shrink the mark to just "podium finish" so it stays on one line, or use a single-weight underline like the Seagate highlight. Taste, but it is the one visibly awkward spot I saw.
6. Minor (content consistency, owner). Home and the Raftar blurb say he "captained the team"; About says he "contributed to" Raftar and "led the team" in his senior year; the home line says "captained the Formula SAE team". All consistent in substance but three different verbs. Pick one for credibility; owner to confirm which is accurate.
7. Minor (verify). The Raftar claim about a Ferrari weight and 0-60 comparison is striking but unverifiable here. Owner should confirm wording and numbers.
8. Minor. Alt text on Wix figures is generic ("Modular snake robot, figure 1 of 3"), weak under WCAG 1.1.1. Owner must say what each image shows.
9. Minor. Two Google font families with display=swap and no fallback metric adjustment, so a reflow on first load is likely. Self-hosting with size-adjust fallbacks needs the real font files.
10. Minor (taste). Outcome stamps appear on five of nine home rows (02, 03, 08, 09 and 01 have none or a different mark). Add none. Rows 02, 03, 08, 09 look less finished beside them; if the owner has real numbers for them, add; otherwise leave.
11. Minor. Contact is LinkedIn only (owner constraint). Conversion risk, not a defect.
12. Nit (taste). Snake placeholder plate is the first image on phone and reads as a stand-in. A real lab photo is the biggest "looks good" upgrade (owner file).
13. Nit (taste). About desktop leaves the right third empty when the portrait is absent. Accepted and documented.

Fun ideas from repo facts only (no invention): turn the "Time allowed: 99 s" stamp into the tab title on the Hasselhoff page, or make the Seagate strike-through reveal "15 minutes" with a press state; neither adds motion that carries no information. Taste, optional.

Regression check: none found. No site diff since cycle 35 beyond what the log records.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules, one hard-shadow button with press state, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs that name the specific thing done.
- Aerobraking structure (hero facts, Orbit range ledger, mono action-space block, cautious conclusion); prev/next pager.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, scroll-padding for the sticky header.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The site commits to retro matte without becoming costume and does not read as generated. Only one thing I saw is designer-fixable: the wrapped double-border podium mark on About (finding 5). Everything that really limits it needs the owner: a status sentence, local Resume and images with dimensions and real alt text, real outcomes for Snake and Raftar, one consistent verb for his Raftar role, and confirmation of the Ferrari claim. A real photo in place of the placeholder plate would lift first impressions more than further CSS.
