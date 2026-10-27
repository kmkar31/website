# Critique, 2026-10-27 (cycle 27, reviewing main at 92ef348 "Cycle 26", no site changes since cycle 25)

## Sources
All three WebFetch attempts were refused (PROVENANCE_REQUIRED, permission unanswered); I did not retry. No source was read this cycle, so no finding below rests on one. Unread pointers, not citations:
- web.dev, Optimize CLS (image dimensions, font fallback): https://web.dev/articles/optimize-cls (blocked)
- WCAG 2.2 SC 1.1.1 Non-text Content: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html (blocked)
- NN/G, UX design portfolios: https://www.nngroup.com/articles/ux-design-portfolios/ (blocked)

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", the sandbox). Viewed: home phone light, home desktop light, Raftar phone dark. Repo grep: `STATUS = ""` at build/build.py:257; 96 static.wixstatic URLs across the HTML; index.html and about.html contain only 3 `width=` matches each. Live site not checked. Working tree was clean.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stats strip or card trio. Specific lede, struck-through "three weeks", stamps, Fig./Sheet plates. Residual: cream + serif + terracotta + mono labels is a familiar editorial kit. Tells moved: none.
- Looks good: 7/10. Phone home is a clean single column with good rhythm; Raftar dark is coherent. Row 01 with the Fig. 1 plate is deliberately heavier. Still no photographs; project pages without working images lean on one schematic and one paragraph.
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter, JSON-LD, sitemap, noindex 404. Open: placeholder alt on Wix figures, no image dimensions, Google Fonts without a size-adjusted fallback.
- UX: 6/10. Phone first screen answers who, where, lab, advisor, a concrete result, Resume and LinkedIn. Missing: current status or date, any contact besides LinkedIn, and a Resume that is not a Wix hotlink.
- Fun and personality: 6/10. Earned touches (strike-through, 99 s stamp, 404, Sheet N of 9) exist; most project pages stay neutral. Further ideas need owner facts.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, one hard-shadow button, inverted-print dark theme (Raftar dark confirms it holds).
- Not AI-looking: met at 3/10.

## Findings (ranked)
1. Major (credibility, owner-only). No current status or date. About says "2023 - 2025" and the lede is present tense, but today is October 2026. A recruiter cannot tell whether he has graduated or is open to roles. The build already has a Status slot (STATUS is empty). Needs one owner sentence and the correct tense for "is at".
2. Major (owner decision). "Start here" (snake robots) is the thinnest page: one paragraph, one illustrative plate, no outcome, yet it is row 01 and the only row with a plate. Supply what he implemented and what happened, or move the label to Aerobraking (46 orbits) or Hasselhoff (99 s).
3. Major (robustness, owner files). Project figures and the Resume (header, hero, footer on every page) depend on Wix hotlinks (96 URLs). A dead Resume link is the most damaging single failure. No image width/height, so layout shift when images load (unmeasured here; web.dev CLS guidance, unread).
4. Major (content, owner facts). Few "what I did / learned / would change" lines. Raftar claims suspension and brakes but offers no specifics (component, number, result), and its figure is a generic car. Do not invent.
5. Minor. Alt text on Wix figures follows a placeholder pattern (e.g. "ARGUS nanosatellite mission figure"); WCAG 1.1.1 needs an equivalent. Owner must say what each image shows.
6. Minor. Fonts: two Google families, display=swap, no size-adjusted fallback; heading reflow risk (unverified offline). Needs self-hosted WOFF2.
7. Minor (taste). About desktop leaves the right third empty (portrait slot unused). Accepted.
8. Minor. Contact is LinkedIn only (owner constraint); conversion risk, not a defect.
9. Nit. "START HERE" is a small mono label under the bold "01", easy to miss on phone; contrast passes.
10. Nit. Footer says "message me on LinkedIn" beside the LinkedIn link; harmless.

No regression found from cycle 25 or 26. The podium wrap fix stays closed.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules at header and footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, stamps (46 orbits, 99 s, 500 m, podium), Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; blurbs that state the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox, no nameless Tab stops, row link name equals title, 44 px targets, reduced-motion handling.
- SEO base, clean collapse of failed images, pager without wraparound.

## Verdict
The design is coherent, retro without becoming costume, and does not read as generated; automated checks are clean and nothing has regressed. Nothing designer-fixable of weight remains, and further designer cycles will be polish. What limits the site is substance only the owner can supply: a current status sentence (the page says 2023 - 2025 in October 2026), local images and a local Resume, and real outcomes for the "Start here" snake page and Raftar. Those four items should be the next input, ahead of any more visual work.
