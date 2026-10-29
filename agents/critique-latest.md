# Critique, 2026-10-29 (cycle 40)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Looked at home phone/desktop light, About desktop dark, snake-robots phone light. No regression found since cycle 39; no site files edited.

## Sources consulted
- web.dev, CSS size-adjust for @font-face: https://web.dev/articles/css-size-adjust (fetched)
- W3C WCAG 2.2 Understanding 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (fetched)
- UX Design Institute, what hiring managers look for in a portfolio: https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/ (fetched; secondary source, used for the "problem / role / process / result, two or three strong case studies" pattern)
- Search results only (not fetched): NN/g portfolio articles, Shopify/Chrome font-fallback guides.
Topics this cycle: font-fallback CLS (web.dev), pointer target size (WCAG 2.2), portfolio case-study structure for hiring managers. Earlier cycles covered scroll padding, focus, stamps, alt text.

## Scores
- AI-tell score: 2/10. Unchanged. Print-notebook point of view (Fig. 1 plates, stamps, struck-through "three weeks", marker highlight, hard shadow on the one button) is specific and would not survive a name swap. Remaining mild tells: the "For the record" side ledger and uniform ruled rows are tidy to the point of template-like on desktop; the em-dash-free copy is plain and good. No tells moved this cycle.
- Looks good: 7/10. Warm paper, double rules, ink footer band and serif type are coherent and pass contrast. Held back by emptiness: no photograph anywhere (every real image is Wix-hosted and absent here), so the home page is type-only plus one schematic. The snake plate is a 5-node zigzag, which reads as a chart placeholder more than as the lead project.
- SEO: 7/10. Unique titles/descriptions, canonical, OG image local and absolute, JSON-LD, sitemap (12 URLs), robots.txt, 404 noindex all present. Caveat that cannot be fixed in repo: robots.txt and sitemap sit under /website/, not host root (owner: submit sitemap in Search Console). Hotlinked Wix images have unknown dimensions, so CLS risk is unverifiable offline.
- UX: 7/10. Who/what/contact is visible on a phone in the first screen; resume and LinkedIn are one tap. Weak point is credibility depth, see findings 1 to 3.
- Fun and personality: 7/10. Stamps, press-and-hold 99 s counter, 404 "failed to land on the target", colophon. Memorable and earned. Not raised: no new idea since cycle 12; the site is charming but quiet.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like: met. Flat surfaces, hairline and double rules, hard offset shadow only on the primary button, faint grain, no gradients or blur. Dark theme is a coherent inverted print, not a glossy dark mode.
2. Not AI-looking: met, see AI-tell score. I disagree with nothing in the owner note.

## Ranked findings

1. Major, content: no status line, still. Home and About say the Master's is "2023 - 2025"; today is 2026-10-29, so a recruiter cannot tell whether he has graduated, is job-hunting or is elsewhere. STATUS in build/build.py is empty by design. This is the single highest-value gap for a 30-second reader. Needs an owner sentence (graduated? where now? open to roles?). Not designer-fixable.
2. Major, content: the "Start here" project is the thinnest page. snake-robots (phone, light) is: tl;dr, question, lab, advisor, a schematic whose caption says "module count is illustrative", one background sentence, pager. No result, no number, no photo, no what-I-did. The hiring-manager pattern (problem, role, process, result; two or three strong cases) is satisfied by aerobraking and Hasselhoff, not by the project the home page tells people to open first. Options: owner supplies 2 to 3 outcome sentences, or move "Start here" to Aerobraking (46 orbits). Owner decision.
3. Major, robustness: the resume link is still a Wix filesusr.com hotlink (header, home, About, footer, all pages) and all project figures are Wix-hosted. One Wix change and the primary call to action 404s with no warning. Owner must drop resume.pdf and the media into assets/.
4. Major, visual: type-only home. Without photography the front page has no human or physical object in it (a snake robot, the RFR23 car, a racing podium). Taste/evidence: first-3-second impression is a good-looking text document. Needs owner photos; the authored plate is a fair stopgap but only on row 01.
5. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4. web.dev: size-adjust plus ascent/descent-override on a local() fallback keeps text in the same place when the web font swaps, reducing CLS. display=swap is set, so a font swap currently reflows headings. Previous cycles declined because metrics would be guessed. Reopening: the metrics are public (Google Fonts metadata / capsize); a networked cycle can compute them, or self-host WOFF2. Not fixable offline.
6. Minor, content credibility: Raftar page and row ("I captained the team and did the suspension and brakes") give no specifics (what changed, mass, lap time, rank) and the verbs differ between About ("led", "contributed") and the row. Owner facts needed. The earlier-flagged Ferrari wording also still awaits owner confirmation.
7. Minor, accessibility: Wix figures have alt text the owner has never reviewed; they are not verifiable here. Empty alt on thumbnails is acceptable.
8. Minor, WCAG 2.5.8 check: the 24 by 24 CSS px minimum is met everywhere measured (44 px rows, buttons and zoom links). Inline text links are exempt. No finding; recorded so it is not re-raised.
9. Nit, layout: About on desktop leaves the right third empty below the "On this page" index (portrait slot documented). Taste, accepted.
10. Nit, repetition: the stamp device now appears on four rows; adding more without real numbers would dilute it. Do not add.
11. Nit: contact is LinkedIn only (owner constraint). Fine, but the sentence "To get in touch, message me on LinkedIn." is the entire contact story; acceptable.

Unfixable offline, so they should stay open, not be re-argued by the designer: 1, 2, 3, 4, 5, 6.

## Good, must not regress
- Home phone first screen: name, one-line degree, two plain paragraphs with real facts, struck-through "three weeks" marker, one button, resume and LinkedIn.
- Fig. 1 plates with "Sheet n of 9 . NTS" on every project; honest "illustrative" captions.
- Stamps only where a real number exists (99 s, 46 orbits, 500 m, podium).
- Source Serif 4 as the single UI voice (cycle 38), 44 px targets, double rules, ink footer band, dark theme.
- Press-and-hold 99 s button, keyboard operable; no empty focus stops when images fail.
- Aerobraking result ledger and tightened claim; pager without wraparound.
- 404 copy, colophon, honest "no framework" claim.

## Verdict
The site is coherent, specific and well built; I can find no designer-fixable defect this cycle and no regression. What keeps it from being excellent is content only the owner can supply: a status sentence (dates now read as stale), real outcomes for the "Start here" snake page, local resume and photographs so nothing depends on Wix, and Raftar specifics. Until those arrive, further CSS polish has sharply diminishing returns, and the designer should not invent stamps, jokes or facts to fill the gap.
