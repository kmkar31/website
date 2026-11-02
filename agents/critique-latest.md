# Critique, 2026-11-02 (cycle 65)

Rendering: `python3 tools/check.py . agents/shots` ran to completion, every page x 3 viewports x 2 themes OK; only "images not loaded" notes (sandbox, Wix hotlinks). I viewed index-phone-light, index-desktop-dark and aerobraking-drl-tablet-light. Working tree was clean before the run, so no site change since cycle 64 and no regression. No site files edited.

## Sources consulted
Search results were retrieved; page bodies were not fetched, so these are pointers to primary pages, not quoted text.
- W3C, Understanding SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev / Chrome, fetchpriority and LCP image priority: https://web.dev/fetch-priority and https://developer.chrome.com/docs/modern-web-guidance/guides/performance/optimize-preload-priority
- NN/g portfolio guidance (author listing, search result only): https://www.nngroup.com/articles/author/rachel-krause/?page=5
Topics this cycle: tap targets, LCP image priority, hiring-manager portfolio content.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground, ink rules, hard-offset primary button, mono ledger, ruled stamps, inverted-print dark theme. No blur, glow or gradient in any screenshot.
2. Must not look AI-generated: met. Plain first-person copy with real numbers, ruled index instead of a card grid, struck-through "three weeks", "Fig. 1" and "Sheet 6 of 9" captions. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows; DM Serif Display plus Source Serif is tasteful but familiar. Nothing moved.
- Looks good: 7/10. Calm and coherent; stamps give rhythm; Aerobraking page is well paced with a drawn figure and ruled result block. Held back because no real photograph renders anywhere, and only row 01 on the index has a visual.
- SEO: 7/10. Unique titles, canonical, OG with absolute local og:image (1200x630, alt), JSON-LD, sitemap, robots, 404, one h1. Not verifiable offline: live og:image fetch, real LCP/CLS with Wix images. Sitemap and robots sit under the /website/ subpath, so submit the sitemap in Search Console by hand.
- UX: 7/10. Phone first screen gives name, school, lab, advisor, a concrete result, primary button, Resume and LinkedIn. Gaps: stale status, one contact route (owner constraint), Resume on a Wix URL.
- Fun and personality: 7/10. Marker strike-through, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET", "500 M OF TETHER", sheet captions. More needs owner facts.

## Ranked findings
1. Major, content: stale status, now worse in wording. about.html:47 says "My Master's ... is at Carnegie Mellon University (2023 - 2025)", present tense, with an end year that is already past (today 2026-11-02). Home subtitle still reads "MS Mechanical Engineering, Carnegie Mellon University" with no graduation or current-role line. `STATUS = ""` (build/build.py:259) so the "For the record" ledger has no Status row (confirmed in the desktop render: Built, Internships, Toolbox). A recruiter cannot tell whether he has graduated, where he is, or whether he is open to roles. Needs one owner sentence; the slot exists. At minimum the designer can change "is at" to a tense-neutral form without inventing facts. Biggest credibility gap.
2. Major, robustness: Resume (PDF) links to one Wix filesusr URL (3 occurrences in index.html alone); assets/ holds only og.png, site.js, style.css. If Wix retires it the resume breaks on every page. Owner must supply assets/resume.pdf.
3. Major, content/UX: "Start here" (Snake robots, row 01) is the thinnest page and carries no result or number, while the strongest evidence (Aerobraking 46 orbits, Hasselhoff 99 s) sits further down. NN/g-style hiring-manager guidance is to lead with the strongest outcome. Owner to supply 2-3 outcome sentences for Snake, or move the label.
4. Major, visual: no photograph of a robot, car, satellite or person renders; figures and the About portrait are Wix hotlinks. Main reason Looks-good stays at 7, and the same dependency risk as finding 2. Needs owner media.
5. Minor, performance: hotlinked figures lack width/height (web.dev CLS guidance). Needs real dimensions; do not guess. Also, when local images exist, keep loading="lazy" off the first visible one and consider fetchpriority="high" for it (web.dev fetch-priority); currently the Aerobraking page lazy-loads 7 images, fine for below-fold ones.
6. Minor, performance: two Google web fonts, no size-adjusted fallback; self-hosted WOFF2 would also remove the third-party connection.
7. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and nothing more. Add only owner-confirmed specifics.
8. Minor, visual (taste): desktop index list: tag column far right with a dead gutter, and nine rows of identical weight, so no focal row apart from the thumbnail. Taste; low priority.
9. Nit, UX: phone header shows only the K mark; on long project pages nothing in view names the owner. Taste, reopen only if the name fits at 360 px.
10. Nit, a11y: tap targets met (44 px, well above the 24 px of SC 2.5.8); sticky header vs SC 2.4.11 covered by scroll-padding-top. Confirm by tabbing a long page.
11. Nit, taste: Resume and LinkedIn repeat in hero and footer; harmless.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted-print dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; honest "schematic" captions; accurate colophon; desktop header showing the name; Aerobraking page structure and sheet captions.

## Verdict
The site commits coherently to the retro matte direction and reads as a person's work; both owner constraints are met and nothing regressed. What holds it back is missing owner input rather than design: a current-status sentence (overdue, and the present-tense "is at CMU (2023 - 2025)" on About is now plainly wrong-looking), a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. Findings 1 to 4 depend on the owner; the one designer-side fix available now is the tense on About (finding 1).
