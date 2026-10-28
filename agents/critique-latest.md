# Critique, 2026-10-28 (cycle 36, reviewing main)

## Sources
- WebSearch worked this cycle but WebFetch was not used, so I read result titles and links, not full pages. Cited for the points below:
  - Portfolio content for hiring managers (outcomes, role clarity): https://uxdesign.cc/what-hiring-managers-look-for-in-a-product-design-portfolio-7b1837360bf9 and https://www.nngroup.com/articles/author/rachel-krause/
  - Web font layout shift (size-adjust / fallback metrics): https://web.dev/learn/performance/optimize-web-fonts and https://web.dev/blog/font-size-adjust
  - WCAG 2.2 Focus Not Obscured (sticky header vs. focus and anchors): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured and https://adrianroselli.com/2023/10/2-4-11-adversarial-conformance.html
- Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", a sandbox limit). It takes more than 2 minutes; run it with a long timeout.
- Viewed: home phone light, home desktop light, Snake phone light. Fonts do not load in the sandbox, so screenshots show the serif fallback. Live site not checked. Grepped repo HTML and CSS.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan copy. Authored specifics: struck-through "three weeks", the "For the record" ledger, outcome stamps, Fig./Sheet N of 9 plates. Residual risk: cream paper, serif, terracotta accent and mono small-caps is a recognisable editorial kit. Tells moved: none.
- Looks good: 7/10. Home is calm, well ruled, with clear hierarchy on phone and desktop. Held back by the placeholder schematic standing in for a real image (Snake plate is a five-dot line on a grid) and a tall, uniform nine-row list. The phone list repeats the same row shape nine times.
- SEO: 8/10. Titles, descriptions, canonical, OG with absolute og:image, JSON-LD (Person, CreativeWork), sitemap and 404 exist. robots.txt and sitemap sit under a subpath, so crawlers will not read robots.txt (owner: submit sitemap in Search Console). Not verifiable offline: og:image fetch, Wix image weight.
- UX: 7/10. Contact, resume and the strongest project are findable in 30 seconds on phone. Lowered by LinkedIn-only contact, Resume depending on a Wix hotlink, and no status or date.
- Fun and personality: 7/10. The struck-through "three weeks", the Ferrari question, the stamps and the 404 joke carry character. The button has a press state. Quiet otherwise.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, one hard-shadow button, no blur or gradient; dark theme is inverted print.
- Not AI-looking: met at 3/10. The remaining risk is repeated marks (stamps, mono labels), not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No status or date. Pages say CMU "2023 – 2025" and today is October 2026, so it reads as stale or graduated with no next step; a recruiter cannot tell if he is available. STATUS in build/build.py (line 259) is empty. One owner sentence fixes it. Hiring-manager guidance stresses clear role and next step (uxdesign.cc link above).
2. Major (owner decision). "Start here" (row 01, Snake) leads to the page with the least evidence: the Snake page (viewed) says what a snake robot is and the question, but not what he implemented or what happened. Supply an outcome, or move the label to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and every project figure are Wix hotlinks (static.wixstatic.com, filesusr.com). A dead Resume link is the worst failure for a recruiter. Figures have no width/height, so layout shift is likely (web.dev CLS guidance). Needs local files.
4. Major (content, owner facts). Raftar says "did the suspension and brakes" with no component, number or result. The figure is a generic car sketch. Do not invent; the owner should supply one concrete thing he designed.
5. Minor (a11y, designer-fixable, new). No `scroll-padding-top` or `scroll-margin-top` in assets/style.css while the header is `position:sticky`. The home hero link to `about.html#seagate` and any in-page anchor will land with the target under the header, and keyboard focus can be hidden behind it (WCAG 2.2 Focus Not Obscured, links above). Add scroll-padding-top equal to the header height (about 60 px phone, plus a little) on `html`. Verify by loading about.html#seagate on phone.
6. Minor (verify). The Raftar claim (one-fifth the weight of a Ferrari, matching its 0-60 time) is striking but unverifiable here. Owner should confirm wording and numbers.
7. Minor. Alt text on Wix figures is generic ("Modular snake robot, figure 1 of 3"), which is weak under WCAG 1.1.1. The owner must say what each image shows.
8. Minor. Two Google font families with display=swap and no fallback metric adjustment; a text reflow when the web fonts swap in is likely on first load (not measurable offline). Self-hosting with `size-adjust` fallbacks (web.dev links above) needs the real font files.
9. Minor (taste). Outcome stamps appear on five of nine home rows in two border styles; rows 02, 03, 08, 09 look less finished next to them. Add none; consider none.
10. Minor. Contact is LinkedIn only (owner constraint). Conversion risk, not a defect. The footer line "message me on LinkedIn" is honest.
11. Nit (taste). On the home phone view the Snake placeholder plate is the first image a visitor sees and it is a five-dot schematic; it reads as a stand-in. A real photo from the lab would be the single biggest "looks good" upgrade (owner file).
12. Nit (taste). About desktop leaves the right third empty beside Skills, Education and Experience when the portrait is absent. Accepted and documented.

Regression check: none found (no site diff since cycle 35). check.py is clean.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button with a press state, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, the 404 joke, the honest colophon.
- Plain lede with real facts; full project names as titles; blurbs that state the specific thing done.
- Aerobraking structure and mono action-space block; Snake page has a clear Next link.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The site commits to retro matte without turning into costume and does not read as generated. One designer-fixable item remains: add scroll-padding for the sticky header (finding 5). Everything else that limits it needs the owner: a status sentence (2023 – 2025 in October 2026), a local Resume and images with dimensions and real alt text, real outcomes for the Snake and Raftar pages, and confirmation of the Ferrari claim. A real photo in place of the placeholder plate would lift the first impression more than any further CSS work.
