# Critique, 2026-10-27 (cycle 29, reviewing main at a129620; site files unchanged since cycle 25)

## Sources
- WebFetch was blocked in this run (permission requests unanswered): W3C SC 2.5.8 Target Size (Minimum) https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html and web.dev CLS https://web.dev/articles/cls were NOT read. Cited from background knowledge only; treat as pointers.
- WebSearch (listing only, pages not read): NN/G portfolio advice https://www.nngroup.com/articles/author/rachel-krause/?page=5 ; https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ ; https://uxdesign.cc/what-hiring-managers-look-for-in-a-product-design-portfolio-7b1837360bf9
- Previous cycle read web.dev size-adjust (https://web.dev/css-size-adjust/); not re-read.
- Nothing this cycle rests on a source I read. Findings rest on measurement and viewing.

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", sandbox). Viewed: home phone light, home desktop light, Raftar phone dark, About desktop dark. Repo greps: 96 wixstatic URLs across pages; Resume link is a filesusr (Wix) hotlink on every page; Wix figures have no width/height; STATUS still empty; Person JSON-LD, sitemap, robots present. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stats strip, card trio or slogan copy. Specific lede, struck-through "three weeks", stamps, Fig./Sheet plates, honest colophon. Residual: cream + serif + terracotta + mono labels is a recognisable editorial kit; four stamps in the list are close to a pattern. Tells moved: none.
- Looks good: 7/10. Home is calm, well ruled, good type scale on phone and desktop; dark theme is solid (Raftar phone dark reads cleanly). Weak spots: project pages are one lede + one schematic + one paragraph with images blocked; Raftar's Fig. 1 is a generic car sketch, which reads as filler next to the real stamped facts elsewhere.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, Person JSON-LD, sitemap with lastmod, noindex 404. Open: generic alt on Wix figures ("Raftar Formula Racing team figure"), no image dimensions, robots.txt at a project subpath is ignored by crawlers (sitemap must be submitted manually), no fallback-font metrics.
- UX: 6/10. Phone first screen answers who, where, lab, one concrete result, Resume, LinkedIn. Missing: status/date, any contact other than LinkedIn, a Resume that does not depend on Wix.
- Fun and personality: 6/10. Strike-through, 99 s stamp, Sheet N of 9, 404 are earned and specific. Most project pages stay neutral.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met (flat paper, ink rules, one hard-shadow button, inverted-print dark, no blur/gradient).
- Not AI-looking: met at 3/10. Remaining risk is stamp repetition and the editorial colour kit, not any template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No current status or date. About says "2023 – 2025" and the lede and About opener are present tense, but today is October 2026. A recruiter cannot tell whether he has graduated or is open to roles. Needs one owner sentence and the correct tense; the STATUS slot exists.
2. Major (owner decision). Row 01 "Start here" (snake robots) is the only row with a plate and the featured label, yet its page has no outcome ("Module count is illustrative"). Supply what he implemented and what happened, or move the label to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Resume (header, hero, footer on every page) and all project figures are Wix hotlinks (filesusr and wixstatic). A dead Resume link is the most damaging failure for a recruiter. No width/height on figures, so layout shift when they load (unmeasured offline; general CLS guidance).
4. Major (content, owner facts). Few "what I did / what happened / what I would change" lines. Raftar: "suspension and brakes" with no component, number or result; its Fig. 1 is a generic car, not his work. Do not invent.
5. Minor (verify claim). Raftar page question: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time". It is a striking specific claim on a page that otherwise has no numbers; confirm with the owner that it is the original site's wording and still accurate, since a recruiter will remember it and cannot check it.
6. Minor. Fonts: two Google families, display=swap, no size-adjusted local fallback. Needs real font files to compute metrics (networked cycle).
7. Minor. Alt text on Wix figures is generic. WCAG 1.1.1 wants text serving the same purpose; owner must say what each image shows.
8. Minor (taste). About desktop leaves the right third empty (the "On this page" index fills part of it in dark/desktop view, which helps). Accepted.
9. Minor (taste). Home stamps: podium, 99 s, 46 orbits, 500 m on four of nine rows, two border styles. The Raftar stamp repeats the lede ("podium ... Formula Bharat 2023") directly above it. Do not add more.
10. Minor. Contact is LinkedIn only (owner constraint); conversion risk, not a defect.
11. Nit. "START HERE" is a small mono label under the bold "01"; easy to miss on phone; contrast passes.
12. Nit. Footer "message me on LinkedIn" sits beside a LinkedIn link; harmless.

No regression found from cycles 25 to 28.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs stating the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox, 44 px targets, reduced-motion handling, clean collapse of failed images, pager without wraparound.
- SEO base: titles, descriptions, canonical, OG, JSON-LD, sitemap.

## Verdict
The design is coherent, commits to retro matte without becoming costume, and does not read as generated; checks are clean and nothing has regressed. Nothing designer-fixable of weight remains, so more visual cycles would be polish. What limits the site is substance only the owner can supply: a status sentence (pages say 2023 – 2025 in October 2026), a local Resume and local images, real outcomes for the "Start here" snake page and Raftar, and confirmation of the Ferrari claim. A metric-matched font fallback is the one designer-side task once font files are reachable.
