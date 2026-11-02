# Critique, 2026-11-02 (cycle 64)

Rendering: `python3 tools/check.py . agents/shots` gave 78 OK lines (13 pages x 3 viewports x 2 themes), no failures; only "images not loaded" notes (sandbox limit for Wix hotlinks). I viewed index-phone-light, snake-robots-phone-dark and projects-desktop-light. Repo clean, no site files changed since last cycle, so no regression. No site files edited.

## Sources consulted
Search was run this cycle; only search result listings were retrieved (page bodies not fetched), so the citations below point to the primary pages found, not to quoted text.
- web.dev, Optimize Cumulative Layout Shift (set width/height on images): https://web.dev/articles/optimize-cls
- W3C, Understanding SC 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured.html
- NN/g portfolio guidance (search results only; NN/g author listing): https://www.nngroup.com/articles/author/rachel-krause/?page=5
- Carried over: Chrome font fallbacks https://developer.chrome.com/blog/font-fallbacks
Topics this cycle: CLS from unsized images, sticky header vs focus, hiring-manager portfolio content.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground, ink rules, hard-offset button, mono ledger, ruled stamps, inverted-print dark theme. No blur, glow or gradient seen.
2. Must not look AI-generated: met. Specific first-person copy, ruled index not a card grid, struck-through "three weeks", figure and sheet captions. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled project rows; DM Serif Display plus Source Serif is tasteful but common; the desktop Projects list leaves a wide empty gutter between description and the tag column. Nothing moved.
- Looks good: 7/10. Calm, coherent, stamps give rhythm. But no real photograph renders anywhere; only row 01 has a visual (a schematic); the Snake page is mostly empty space below the figure (phone dark: paragraph, large gap, pager).
- SEO: 7/10. Unique titles, canonical, OG/Twitter, local og:image, JSON-LD, sitemap, robots, 404, one h1. Unverifiable offline: live og:image fetch, LCP/CLS with Wix images. robots.txt and sitemap live under a project subpath, so submit the sitemap in Search Console.
- UX: 7/10. Phone first screen gives name, school, lab, advisor, a concrete result, primary button, Resume and LinkedIn. Gaps: stale status, thin "Start here" page, one contact route (owner constraint), Resume on a Wix URL.
- Fun and personality: 7/10. Marker strike-through, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET", "500 M OF TETHER", sheet-number captions. More needs owner facts.

## Ranked findings
1. Major, content: stale status. Home subtitle, meta description, About intro ("2023 - 2025") and Education still read as a current or just-ending MS; today is 2026-11-02. `STATUS = ""` in build/build.py:259, so the ledger shows no Status row (confirmed in the home render: Built, Internships, Toolbox only). A recruiter cannot tell whether he graduated, where he is, or whether he is open to roles. Needs one owner sentence; slot is ready. Biggest credibility gap.
2. Major, robustness: Resume (PDF) on every page links to one Wix filesusr URL (3 occurrences in index.html alone; assets/ holds only og.png, site.js, style.css). If Wix retires it the resume breaks site-wide. Owner must supply assets/resume.pdf.
3. Major, content/UX: the "Start here" project (Snake robots, row 01) is the thinnest page: one question, one paragraph ("Why snake robots"), a schematic, a pager; no result or number, while the strongest evidence (Aerobraking, 46 orbits; Hasselhoff, 99 s) is elsewhere. Owner to supply 2-3 outcome sentences for Snake, or move the label. NN/g-style guidance for hiring managers is to lead with the strongest outcome; this page leads with the weakest.
4. Major, visual: no real photograph of a robot, car, satellite or person renders; figures and About portrait are Wix hotlinks. Main reason Looks-good stays at 7. Needs owner media with dimensions; hotlinking is also the same dependency risk as finding 2.
5. Minor, performance: hotlinked figures lack width/height (web.dev CLS guidance: reserve space with width/height or aspect-ratio). Needs the real dimensions; do not guess.
6. Minor, performance: two Google web fonts with no size-adjusted fallback. Needs the font files to measure, or self-hosted WOFF2.
7. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and nothing more. Add only owner-confirmed specifics.
8. Minor, visual (taste): desktop Projects list: the tag column sits far right with a wide dead gutter, and all nine rows have identical height and structure, so the page has no focal row. Pulling the number and tag nearer the text, or giving row 01 more weight, would help. Taste.
9. Minor, UX (taste): phone header shows only the K mark; on long project pages nothing in view names the owner. Reopen only if the name fits at 360 px.
10. Nit, a11y: sticky header vs WCAG 2.2 SC 2.4.11; scroll-padding-top already covers anchors and the header is 44 px, so likely fine; confirm by tabbing a long page.
11. Nit, taste: Resume and LinkedIn repeat in hero and footer; harmless and aids findability.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted-print dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; honest "schematic" captions; accurate colophon; desktop header showing the name; Aerobraking h2 structure.

## Verdict
The site commits coherently to the retro matte direction and reads as a person's work. Both owner constraints are met and nothing regressed. What holds it back is missing owner input, not design: a current-status sentence (overdue), a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. Findings 1 to 4 all depend on the owner; the only designer-side idea is finding 8 (taste).
