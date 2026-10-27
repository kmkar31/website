# Critique, 2026-10-27 (cycle 28, reviewing main at a9a0535 "Cycle 27", no site changes since cycle 25)

## Sources
- web.dev, CSS size-adjust for @font-face (read via WebFetch): https://web.dev/css-size-adjust/ . size-adjust plus ascent/descent/line-gap overrides on a local fallback keep a font swap from moving content; supported Chrome/Edge/Firefox 92+, Safari 17+.
- web.dev, Optimize Cumulative Layout Shift (search result only, page not read): https://web.dev/optimize-cls/
- W3C, Understanding SC 1.1.1 Non-text Content (search result only, not read): https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- NN/G portfolio advice (search returned only listings, not read): https://www.nngroup.com/articles/author/rachel-krause/?page=5
Only the first is a source I actually read. Findings 5 and 6 lean on it; the rest rest on measurement and viewing.

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", the sandbox). Viewed: home phone light, home desktop dark, About tablet light, Snake robots phone light. Repo: `STATUS = ""` still at build/build.py:257; Raftar images are Wix hotlinks with a descriptive but generic alt ("Raftar Formula Racing electric car"); no width/height on them; robots.txt and sitemap present. Live site not checked. Working tree clean.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stats strip or card trio. Specific lede, struck-through "three weeks", stamps, Fig./Sheet plates. Residual: cream, serif, terracotta and mono labels is a familiar editorial kit, and four stamp styles on the home list (podium, 99 s, 46 orbits, 500 m) start to read as a pattern. Tells moved: none.
- Looks good: 7/10. Home is calm and well ruled on phone and desktop; dark theme holds. Snake page on phone has a good title scale and a clean plate. Weak spot: with images blocked, project pages are one paragraph plus one schematic, and long pages of pure text feel thin. Cannot judge real photos here.
- SEO: 7/10. Unique titles/descriptions, canonical, OG/Twitter, JSON-LD, sitemap, robots, noindex 404. Open: generic alt on Wix figures, no image dimensions, no fallback-font metrics.
- UX: 6/10. The phone first screen answers who, where, lab, one concrete result, Resume, LinkedIn. Missing: current status/date, any contact besides LinkedIn, local Resume.
- Fun and personality: 6/10. Strike-through, 99 s stamp, Sheet N of 9, 404 are earned. Most project pages stay neutral.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met (flat paper, ink rules, one hard-shadow button, inverted-print dark).
- Not AI-looking: met at 3/10. The remaining risk is stamp repetition (finding 8), not any template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No current status or date. About says "2023 - 2025" and the lede is present tense ("At CMU's Biorobotics Lab ... I research"), but today is October 2026. A recruiter cannot tell whether he has graduated or is open to roles. The build has a Status slot (STATUS empty). Needs one owner sentence and the right tense.
2. Major (owner decision). Row 01 "Start here" (snake robots) is the thinnest page: one paragraph, one illustrative plate ("Module count is illustrative"), no outcome, yet it is the only row with a plate and the featured one. Supply what he implemented and what happened, or move the label to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Project figures and the Resume (header, hero, footer on every page) depend on Wix hotlinks. A dead Resume link is the single most damaging failure. No width/height on figures, so layout shift when they load (unmeasured here; web.dev CLS guidance, only a search result).
4. Major (content, owner facts). Few "what I did / learned / would change" lines. Raftar says "suspension and brakes" with no component, number or result, and its figure is a generic car. Do not invent.
5. Minor. Fonts: two Google families, display=swap, no size-adjusted fallback. web.dev documents `size-adjust` and metric overrides on a local fallback as the fix; the values need to be calculated from the real font files, which the designer can do once the font files are available (fonts can be downloaded in a normal environment). Possible heading reflow is unverified offline.
6. Minor. Alt text on Wix figures is generic ("... team figure"). WCAG 1.1.1 wants text that serves the same purpose; the owner must say what each image shows.
7. Minor (taste). About desktop leaves the right third empty (portrait slot unused). Accepted.
8. Minor (taste). Four of nine rows carry boxed mono stamps in three border styles (double, single, dashed-ish). It is the site's best authored device, but at four of nine it is close to a rhythm a generator could imitate. Watch, do not add more.
9. Minor. Contact is LinkedIn only (owner constraint); conversion risk, not a defect.
10. Nit. "START HERE" is a small mono label under the bold "01", easy to miss on phone; contrast passes.
11. Nit. Footer says "message me on LinkedIn" beside the LinkedIn link; harmless.

No regression found from cycles 25 to 27.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs that state the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling.
- SEO base, clean collapse of failed images, pager without wraparound.

## Verdict
The design is coherent, retro without becoming costume, and does not read as generated; automated checks are clean and nothing has regressed. Nothing designer-fixable of weight remains, so further visual cycles will be polish. What limits the site is substance only the owner can supply: a current status sentence (the pages say 2023 - 2025 in October 2026), local images and a local Resume, and real outcomes for the "Start here" snake page and Raftar. Those should be the next input, ahead of more visual work. One designer-side task is available once font files can be fetched: a metric-matched fallback for the two Google fonts.
