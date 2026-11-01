# Critique, 2026-11-01 (cycle 59)

Rendering: `python3 tools/check.py . agents/shots` completed. All 13 pages x 3 viewports x 2 themes report OK; the only notes are "images not loaded" (sandbox, Wix hotlinks). I viewed index-phone-light, index-desktop-dark and snake-robots-tablet-light. HEAD is 7fe0ed0; recent commits changed no site files, so no regressions. No site files edited.

## Sources consulted
Research was again limited. WebFetch was blocked (permission not answered, not retried) for https://www.nngroup.com/articles/hiring-managers-portfolios/, https://web.dev/articles/optimize-cls and https://developers.google.com/search/docs/appearance/structured-data/profile-page. A WebSearch returned only listings, which I did not read: https://www.nngroup.com/articles/ux-design-portfolios/ and https://blog.opendoorscareers.com/p/how-recruiters-and-hiring-managers-actually-look-at-your-portfolio. No best-practice claim below relies on their content; findings rest on repo evidence and screenshots. The three-source rule is not met this cycle.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Paper tone, ink double rules, hard-offset button, mono ledger, stamps; no blur, glow or gradient visible.
2. Must not look AI-generated: met. Plain first-person copy with specific numbers; the struck-through "three weeks" on a marker band is authored.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows with a mono tag column; DM Serif + Source Serif is tasteful but common. No tells moved.
- Looks good: 7/10. Desktop dark home is balanced and consistent. Held at 7: eight of nine index rows have no image, and the only visual on the Snake page is a generic schematic (captioned "Module count is illustrative"); no photo of a robot, car or person is visible anywhere.
- SEO: 7/10. Title, description, canonical, OG/Twitter with local og:image, JSON-LD, sitemap, robots, noindex 404 are in the repo. Not verifiable offline: live og:image fetch, LCP/CLS with Wix images.
- UX: 7/10. Phone first screen gives name, school, lab, advisor, one result, primary button, Resume and LinkedIn. Gaps: stale status, one contact route (owner constraint), weak "Start here" page.
- Fun and personality: 7/10. Strike-through highlight, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET" stamps, 404 line. Nothing more to add without new facts.

## Ranked findings
1. Major, content: status is stale. Home, About and Education say CMU MS 2023 to 2025; today is 2026-11-01. A recruiter cannot tell whether he has graduated, where he is now or whether he is available. STATUS in build/build.py is empty. Needs one owner sentence.
2. Major, robustness: the primary CTA "Resume (PDF)" (header, hero, footer, every page) points to a Wix filesusr.com URL (confirmed in index.html). assets/ holds only og.png, site.js and style.css. If Wix retires the file the main CTA dies site-wide. Owner must supply assets/resume.pdf.
3. Major, content/UX: the "Start here" project is the weakest page. On the Snake page the whole body is one two-sentence "Why snake robots" paragraph, a schematic and a Next link; no result, method or outcome. The strongest evidence on the site (Aerobraking, 46 orbits; Hasselhoff, 99 s) is not the one labelled. Owner to supply two or three outcome sentences, or move the label.
4. Major, visual: no real photograph survives; the About portrait and project figures are wixstatic hotlinks, both a dependency risk and the reason Looks-good stays at 7. Owner media needed.
5. Minor, performance: hotlinked figures lack width/height, so layout shifts when images load. Local images with known dimensions fix it.
6. Minor, performance: no size-adjusted fallback for the two Google fonts; needs measured metrics or self-hosted WOFF2.
7. Minor, UX (taste): on phone the header shows only the K mark; on very long project pages (Aerobraking about 6200 px tall on phone) nothing in view names the site owner. Previously declined for width; reopen only if "Karthik" fits at 360 px.
8. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat across four places with no further specifics. Add only owner-confirmed facts.
9. Nit, taste: Resume (PDF) and LinkedIn repeat in hero and footer on home; harmless.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; struck-through marker highlight; stamps carrying real figures; ruled index with mono numbers; inverted-print dark theme (amber on warm black reads cleanly); double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; honest figure caption ("Module count is illustrative"); accurate colophon.

## Verdict
The site commits coherently to the retro matte direction and reads as authored by a person. What holds it back is missing owner input, not design: a current-status sentence, a local resume PDF, outcome sentences for Snake and Raftar, and real photographs with dimensions. Further designer cycles will find little to change until those arrive. Caveat: external research was blocked again, so no new best-practice claim is made.
