# Critique, 2026-11-02 (cycle 62)

Rendering: `python3 tools/check.py . agents/shots` ran to completion; all pages x 3 viewports x 2 themes report OK (only "images not loaded" notes, a sandbox limit for Wix hotlinks). I viewed index-phone-light, index-desktop-light and aerobraking-drl-tablet-dark. HEAD is 70f9836; the last commits changed no site files, so there is no regression. No site files edited.

## Sources consulted
WebFetch was blocked this cycle (permission requests unanswered), so these are search-result pointers only. I did not read them through, and nothing below rests on their wording. Findings rest on repo evidence and screenshots.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), 24 CSS px: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked, listed in search results). The site's 44 px targets already exceed it.
- Chrome, Improved font fallbacks (size-adjust, ascent-override): https://developer.chrome.com/blog/font-fallbacks (search result only)
- Chrome, Visually stable font fallbacks: https://developer.chrome.com/docs/modern-web-guidance/guides/visual-design/visually-stable-font-fallbacks (search result only)
- Recruiter portfolio review pointers (secondary, not NN/g itself): https://blog.uxfol.io/ux-portfolio-playbook/ and https://nngroup.com/articles/ux-design-portfolios/ (cited last cycle)
Topic this cycle: font fallback and CLS, target size, current-relevance of content.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper-tone ground with faint grain, ink rules, hard-offset button, mono ledger, ruled stamps, inverted-print dark theme. No blur, glow or gradient in any render I viewed.
2. Must not look AI-generated: met. First-person copy with specific numbers, a ruled list rather than a card grid, struck-through "three weeks", figure-numbered plates. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows with a mono tag column (tagline "Robotics / Controls" repeated); DM Serif + Source Serif is tasteful but common. No tells moved this cycle.
- Looks good: 7/10. Desktop home is balanced and calm; stamps give rhythm. Held at 7: no real photograph renders anywhere, only row 01 has a visual (a small schematic), and the right third of home beside the ledger/list is quiet. Aerobraking tablet dark reads well: clear h2s, two-item orbit ledger, figure plate. Long prose on that page is still dense but now scannable.
- SEO: 7/10. Unique titles on all 13 pages, canonical, OG/Twitter, local og:image, JSON-LD, sitemap, robots, noindex 404. Limits: robots.txt/sitemap sit at a project subpath (host-root robots is not possible on GitHub Pages, so submit the sitemap in Search Console); live og:image fetch and LCP/CLS with Wix images not verifiable offline.
- UX: 7/10. On the phone first screen a visitor gets name, school, lab, advisor, a result, the primary button, Resume and LinkedIn. Gaps: stale status, thin "Start here" page, a single contact route (owner constraint), Resume depends on a Wix URL.
- Fun and personality: 7/10. Marker strike-through, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET", "500 M OF TETHER", "SHEET n OF 9" captions, pressable 99 s stamp. Nothing more to add without new owner facts.

## Ranked findings
1. Major, content: stale status, now 10+ months past the stated end date. Home subtitle, About and Education still say CMU MS 2023 to 2025; today is 2026-11-02. `STATUS = ""` at build/build.py (still empty), so the ledger has no Status row. A recruiter cannot tell whether he has graduated, where he works or studies, or whether he is open to roles. This is the single biggest credibility gap and each week it grows. Needs one owner sentence; the slot is ready.
2. Major, robustness: "Resume (PDF)", the primary secondary-CTA in header, hero and footer on every page, points to a Wix filesusr URL. Hotlink counts (grep wixstatic/filesusr): aerobraking 9, quadrotor-sysid 7, assistive-tricycle/hasselhoff/tethered 6, every other page 2 to 4. If Wix retires the file the resume dies site-wide. Owner must supply assets/resume.pdf.
3. Major, content/UX: the "Start here" project (Snake robots) is the thinnest page: a one-paragraph "Why snake robots", a schematic and a pager, no result, and it is the owner's lead research. The strongest evidence (Aerobraking, 46 orbits; Hasselhoff, 99 s) is not the labelled entry. Owner to supply two or three outcome sentences for Snake, or move the label to a project that has a result.
4. Major, visual: no real photograph of a robot, car, satellite or person survives; project figures and the About portrait are Wix hotlinks. This is the main reason Looks-good stays at 7. Owner media needed (local files with known dimensions).
5. Minor, performance: hotlinked figures lack width/height, so layout shifts as they load (Chrome/web.dev CLS guidance). Resolves with local images.
6. Minor, performance: two Google web fonts with no size-adjusted fallback (size-adjust / ascent-override per the Chrome font-fallbacks article); fix needs the real font files to measure, or self-hosted WOFF2.
7. Minor, content: Raftar says "40+ students", "captained", "suspension and brakes" and nothing more; no outcome beyond the podium. Add only owner-confirmed specifics.
8. Minor, visual (taste): on phone only row 01 carries a figure, above its heading, so the list opens with a different shape from the other eight. Acceptable while it is the only visual; revisit when more thumbnails exist.
9. Minor, UX (taste): phone header shows only the K mark; on long project pages nothing in view names the owner. Reopen only if "Karthik" fits at 360 px beside the nav.
10. Nit, taste: Resume and LinkedIn repeat in hero and footer on home; harmless and aids findability.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted-print dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; honest captions ("schematic", "illustrative"); accurate colophon; desktop header showing the name; Aerobraking h2 structure and the trimmed, evidence-matched conclusion.

## Verdict
The site commits coherently to the retro matte direction and reads as the work of a person; both owner constraints are met and nothing regressed. What holds it back is missing owner input, not design: a current-status sentence (now clearly overdue), a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. Designer cycles will find nothing meaningful to change until those arrive; findings 1 to 4 are all owner-dependent.
