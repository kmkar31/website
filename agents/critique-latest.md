# Critique, 2026-10-27 (cycle 31, reviewing main at 8d81ce4; site files unchanged since cycle 25)

## Sources
- WebFetch of https://web.dev/articles/optimize-cls was blocked (permission unanswered). Not read.
- Pointers only, from background knowledge, unverified this cycle: WCAG 2.2 SC 1.1.1 Non-text Content (https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html); web.dev on setting image width/height to avoid layout shift (https://web.dev/articles/optimize-cls); NN/g on portfolio/hiring-manager scanning (https://www.nngroup.com/articles/author/rachel-krause/).
- Earlier cycle read web.dev size-adjust (https://web.dev/css-size-adjust/).
- Findings rest on measurement and viewing, not on sources.

Measured: `python3 tools/check.py . agents/shots` (needs about 3 minutes; run in background), 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", sandbox). Viewed: home phone light, home desktop light, Raftar phone dark, Aerobraking tablet light. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogans. Specific lede, struck-through "three weeks", stamps, Fig./Sheet plates, honest colophon. Residual: cream + serif + terracotta + mono labels is a recognisable editorial kit; four stamps on nine rows edge toward a pattern. Tells moved: none.
- Looks good: 7/10. Home is calm and well ruled on phone and desktop; dark theme holds. The Aerobraking page is a long unbroken run of prose after the plate (Problem, Setup, Method, Result with no figures, callouts or pull numbers), the least designed page viewed. Raftar is thin and its plate is a generic car.
- SEO: 7/10. Unique titles/descriptions, canonical, OG/Twitter, Person JSON-LD, sitemap, noindex 404. Open: generic alt on Wix figures, no image width/height, robots.txt and sitemap sit at a subpath (crawlers read robots.txt only at host root; submit the sitemap in Search Console), no fallback-font metrics.
- UX: 6/10. First phone screen answers who, where, lab, one concrete result, Resume and LinkedIn. Missing: status/date, any contact beyond LinkedIn, a Resume not hosted on Wix.
- Fun and personality: 6/10. Strike-through, "Time allowed: 99 s" stamp, Sheet N of 9, 404 are earned. Most project pages stay neutral.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, one hard-shadow button, inverted-print dark theme, no blur or gradient.
- Not AI-looking: met at 3/10. Remaining risk is stamp repetition and the editorial colour kit, not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No current status or date. Pages say "2023 – 2025" and the lede is present tense ("I research ...") while today is October 2026. A recruiter cannot tell whether he has graduated or is open to roles. One owner sentence fixes it; the STATUS slot exists.
2. Major (owner decision). Row 01 "Start here" (snake robots) is the only row with a plate and the featured label, yet its page has no outcome ("Module count is illustrative"; one paragraph). Supply what he implemented and what happened, or move "Start here" to Aerobraking (46 orbits) or Hasselhoff (99 s), which have numbers.
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and all project figures are Wix hotlinks. A dead Resume link is the most damaging failure for a recruiter. Figures have no width/height, so layout shift is likely when they load (unmeasured offline).
4. Major (content, owner facts). Few "what I did / what happened / what I would change" lines. Raftar says "suspension and brakes" with no component, number or result; its Fig. 1 is a generic car sketch. Do not invent.
5. Minor (design, designer-fixable). Aerobraking page: about 1,000 words of undivided prose below the plate. The numbers already in the page (terminal error 8.4 km, 1.1M steps, 46 orbits, 10038 km initial apoapsis, 4906 km target) could be pulled into a small "Result" ledger beside or above the Result section, matching the home "For the record" box, and the action-space list set as a mono block. Uses only facts already present. Keep body copy as is.
6. Minor (verify claim). Raftar question "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time?" is striking and unverifiable. Confirm it is the original wording and accurate.
7. Minor. Alt text on Wix figures is generic; one `<img alt="">` on the Raftar page should be decorative on purpose or described. WCAG 1.1.1. Owner must say what each image shows. Note: the thumbnail and lightbox empty alts are intentional.
8. Minor. Fonts: two Google families, display=swap, no size-adjusted local fallback. Needs real font files for metrics.
9. Minor (taste). Home stamps on four of nine rows with two border styles; the Raftar stamp repeats the lede directly above it. Add no more.
10. Minor. Contact is LinkedIn only (owner constraint); conversion risk, not a defect.
11. Nit (taste). Empty band above the footer on tablet; About desktop leaves its right third empty. Accepted.
12. Nit. "START HERE" is a small mono label under bold "01"; easy to miss on phone; contrast passes. Footer LinkedIn repeat is harmless.

No regression found from cycles 25 to 30.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs stating the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The design is coherent, commits to retro matte without becoming costume, does not read as generated, and nothing has regressed. The one new designer-side item is the wall of prose on Aerobraking (finding 5), which can be broken up with facts already on the page. Everything else that limits the site is owner-supplied substance: a status sentence (pages say 2023 – 2025 in October 2026), a local Resume and images, real outcomes for the "Start here" snake page and Raftar, and confirmation of the Ferrari claim. Web research was blocked again, so no external source backs these findings.
