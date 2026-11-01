# Critique, 2026-11-01 (cycle 58)

Rendering: `python3 tools/check.py . agents/shots` ran in the background (it exceeds a 2-minute foreground limit). Output so far shows OK on every page checked, only "images not loaded" sandbox notes. I viewed index-phone-light, index-desktop-light and about-tablet-dark. HEAD is 85438fc; the last commits changed no site files, so there are no regressions. No site files edited.

## Sources consulted
The three-source rule is only partly met.
- Blocked (permission not answered, not retried): https://web.dev/articles/optimize-cls and https://www.w3.org/WAI/WCAG22/Understanding/reflow.html. Nothing below relies on their content.
- Search listing only (result titles, no page read): Nielsen Norman Group author index https://www.nngroup.com/articles/author/rachel-krause/?page=5 and UX Design Institute https://www.uxdesigninstitute.com/blog/hiring-managers-ux-portfolio/. These are general pointers that hiring managers scan portfolios quickly; I did not verify specific claims.
- Earlier cycles (see LOG.md) covered WCAG target size and web.dev css-size-adjust.
Findings therefore rest on repo evidence and screenshots.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Paper tone, ink rules, hard-offset button, mono ledger, stamps. No blur, glow or gradient in the screenshots.
2. Not AI-generated: met. Plain first-person copy with specific numbers; the strike-through "three weeks" on a marker band and the stamps are authored.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows with a mono tag column, and the DM Serif + Source Serif pairing is tasteful but common. No tells moved since last cycle.
- Looks good: 7/10. Desktop home is balanced; the ledger sits well against the lede. Held at 7 because eight of nine index rows have no image (only Snake has a schematic thumbnail) and no photograph of a robot, car or person is visible anywhere in the screenshots.
- SEO: 7/10. Title, description, canonical, OG/Twitter with local og:image, JSON-LD, sitemap, robots and a noindex 404 are all in the repo. Not verifiable offline: live og:image fetch, LCP/CLS with Wix images, robots.txt under a project path.
- UX: 7/10. Phone first screen shows name, school, lab, advisor, one result, primary button, Resume and LinkedIn. Gaps: no current status, one contact route (owner constraint), thin "Start here" project.
- Fun and personality: 7/10. Strike-through highlight, 99 s and 46-orbit stamps, the 404 line. Nothing more to add without new facts.

## Ranked findings
1. Major, content: status is stale. Home, About and Education say CMU MS 2023 to 2025; today is 2026-11-01 and the About text says the Master's "is at" CMU. A recruiter cannot tell whether he has graduated, where he is now or whether he is available. STATUS in build/build.py is still empty. Needs one owner sentence.
2. Major, robustness: the primary CTA "Resume (PDF)" points to a Wix filesusr.com URL (header, hero, footer on every page). assets/ holds only og.png, site.js and style.css. If Wix retires the file, the main CTA dies site-wide. Owner must add assets/resume.pdf.
3. Major, content: "Start here" is Snake robots, which has the thinnest evidence (no measured result). Aerobraking (46 orbits) is stronger. Owner to supply two or three outcome sentences, or move the label.
4. Major, visual: no photograph survives; the About portrait and project figures are wixstatic hotlinks, which is both a dependency risk and the reason Looks-good stays at 7. Owner media needed.
5. Minor, performance: hotlinked figures lack width and height, so layout shifts when real images load (a placeholder box was added in cycle 47, but real ratios are unknown). Local images with known dimensions fix it.
6. Minor, performance: no size-adjusted fallback for the two Google fonts; headings may reflow on swap. Needs measured metrics or self-hosted WOFF2.
7. Minor, UX (taste): on phone the header shows only the K mark; on a long project page (Aerobraking is about 6200 px tall on phone) nothing in view says whose site it is. Previously declined for width; consider it only if "Karthik" fits at 360 px.
8. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat on home, list, About and project page with no further specifics. Add only owner-confirmed facts.
9. Nit, taste: Resume (PDF) and LinkedIn appear in hero and footer on home; harmless.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; struck-through marker highlight; stamps carrying real figures (podium, 99 s, 46 orbits, 500 m); ruled index with mono numbers; inverted-print dark theme (About dark reads cleanly, double-bordered "podium finish" mark intact); double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; accurate colophon.

## Verdict
The site commits coherently to the retro matte direction and reads as authored by a person. What holds it back is missing owner input rather than design: a current-status sentence, a local resume PDF, outcome sentences for Snake and Raftar, and real photographs with dimensions. Further designer cycles will find little to change until those arrive; the next gain is content, not styling. Caveat: this cycle's external research was limited (two sources blocked), so no new best-practice claim is made.
