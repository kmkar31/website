# Critique, 2026-10-27 (cycle 30, reviewing main at 64b947f; site files unchanged since cycle 25)

## Sources
- Read: none this cycle. WebFetch of https://web.dev/articles/optimize-cls and https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html was blocked (permission request unanswered). Cited as pointers only, from background knowledge.
- WebSearch listing only (pages not opened): https://www.nngroup.com/articles/author/rachel-krause/?page=5 ; https://blog.adplist.org/post/what-is-a-hiring-manager-looking-for-in-a-design-portfolio ; https://uxplanet.org/good-ux-portfolios-never-get-interviews-6ea28fb2f9b3
- Earlier cycle read web.dev size-adjust (https://web.dev/css-size-adjust/).
- Findings rest on measurement and viewing, not on sources.

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", sandbox). Viewed: home phone light, home desktop dark, snake-robots tablet light. Repo greps: 32 wixstatic image URLs across project pages (about/projects 1 each); Raftar page still has "Raftar Formula Racing team figure" alt; at least one `<img alt="">` exists in the Raftar page markup. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stats strip, card trio or slogan copy. Specific lede, struck-through "three weeks", stamps, Fig./Sheet plates, honest colophon. Residual: cream + serif + terracotta + mono labels is a recognisable editorial kit; four stamps on nine rows edge toward a pattern. Tells moved: none.
- Looks good: 7/10. Home reads calmly on phone and desktop; the dark "inverted print" theme holds up (desktop dark is well ruled, the ledger sits cleanly beside the lede). Snake page on tablet is clean but thin: lede, one schematic, one paragraph, pager. Large dead space under the pager before the footer.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, Person JSON-LD, sitemap, noindex 404. Open: generic or empty alt on Wix figures, no image dimensions, robots.txt/sitemap at a subpath (crawlers only read robots.txt at host root; submit the sitemap manually), no fallback-font metrics.
- UX: 6/10. First phone screen answers who, where, lab, one concrete result, Resume, LinkedIn. Missing: status/date, any contact beyond LinkedIn, a Resume not on Wix.
- Fun and personality: 6/10. Strike-through, 99 s stamp, Sheet N of 9, 404 are earned. Most project pages stay neutral.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met (flat paper, ink rules, one hard-shadow button, inverted-print dark, no blur or gradient).
- Not AI-looking: met at 3/10. Remaining risk is stamp repetition and the editorial colour kit, not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No current status or date. Pages say "2023 – 2025" and the lede is present tense ("I research ...") while today is October 2026. A recruiter cannot tell if he has graduated or is open to roles. One owner sentence fixes it; the STATUS slot exists.
2. Major (owner decision). Row 01 "Start here" (snake robots) is the only row with a plate and the featured label, yet its page has no outcome: the caption even says "Module count is illustrative", and the body is one paragraph. Supply what he implemented and what happened, or move "Start here" to Aerobraking (46 orbits) or Hasselhoff (99 s), which have numbers.
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and all project figures are Wix hotlinks. A dead Resume link is the most damaging failure for a recruiter. Figures have no width/height, so layout shift when they load (unmeasured offline; web.dev CLS guidance, not read this cycle).
4. Major (content, owner facts). Few "what I did / what happened / what I would change" lines. Raftar: "suspension and brakes" with no component, number or result; its Fig. 1 is a generic car sketch, filler beside the real facts elsewhere. Do not invent.
5. Minor (verify claim). Raftar page question "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time?" is a striking, unverifiable claim. Confirm it is the original wording and accurate.
6. Minor. Alt text on Wix figures is generic, and one `<img alt="">` on the Raftar page should either be decorative on purpose or described. WCAG 1.1.1 wants text serving the same purpose; owner must say what each image shows.
7. Minor. Fonts: two Google families, display=swap, no size-adjusted local fallback. Needs real font files for metrics.
8. Minor (taste). Project pages end with a large empty band above the footer on tablet; About desktop leaves its right third empty. Accepted.
9. Minor (taste). Home stamps (podium, 99 s, 46 orbits, 500 m) on four of nine rows with two border styles. The Raftar stamp repeats the lede directly above it. Add no more.
10. Minor. Contact is LinkedIn only (owner constraint); conversion risk, not a defect.
11. Nit. "START HERE" is a small mono label under the bold "01"; easy to miss on phone; contrast passes.
12. Nit. Footer "message me on LinkedIn" sits beside a LinkedIn link; harmless.

No regression found from cycles 25 to 29.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs stating the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The design is coherent, commits to retro matte without becoming costume, and does not read as generated; checks are clean and nothing has regressed. Nothing designer-fixable of weight remains, so further visual cycles would be polish. What limits the site is substance only the owner can supply: a status sentence (pages say 2023 – 2025 in October 2026), a local Resume and local images, real outcomes for the "Start here" snake page and Raftar, and confirmation of the Ferrari claim. A metric-matched font fallback is the one designer-side task once font files are reachable. Research this cycle was blocked, so no new external sources back these findings.
