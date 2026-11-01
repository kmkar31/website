# Critique, 2026-11-01 (cycle 57)

Rendering: `python3 tools/check.py . agents/shots` ran in the background (it exceeds a 2-minute foreground limit); 13 pages x 3 viewports x 2 themes, no failures, only "images not loaded" sandbox notes. I viewed index-phone-light and index-desktop-light. HEAD is 71a1151; no site files changed since cycle 54, so no regressions. No site files edited.

## Sources consulted
No web source was read this cycle. WebFetch/WebSearch were not loaded in this run, so the three-source rule is NOT met. Findings rest on repo evidence and screenshots. Previously read (earlier cycles, see LOG.md): WCAG 2.2 target-size-minimum, web.dev css-size-adjust. Unverified general practice: web.dev optimize-cls (explicit width/height on images).

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Paper tone, ink rules, hard-offset button, mono ledger, stamps; no blur, glow or gradient.
2. Not AI-generated: met. Plain first-person copy with real numbers.

## Scores
- AI-tell score: 2/10, unchanged. Authored: struck-through "three weeks" on a marker band, "For the record" ledger, stamps carrying real numbers. Faint tells: nine identically ruled rows with a mono tag column; DM Serif + Source Serif is tasteful but common. No tells moved.
- Looks good: 7/10. Desktop is balanced; the ledger sits well against the lede. Held at 7: eight of nine index rows have no image (only Snake has a schematic thumbnail), so the list is a wall of text, and no photograph of a robot, car or person is visible anywhere.
- SEO: 7/10. Title, description, canonical, OG/Twitter with local og:image, JSON-LD, sitemap, robots, noindex 404 are in the repo. Not verifiable offline: live og:image fetch, LCP/CLS with Wix images, robots.txt under a project path.
- UX: 7/10. Phone first screen: name, school, lab, advisor, one result, primary button, Resume, LinkedIn. Gaps: no current status, one contact route (owner constraint), thin "Start here" project.
- Fun and personality: 7/10. Strike-through highlight, 99 s and 46-orbit stamps, 404 line are earned. Nothing more to add without new facts.

## Ranked findings
1. Major, content: status is stale. Home, About and Education say CMU MS 2023-2025; today is 2026-11-01. A recruiter cannot tell if he has graduated, where he is, or whether he is available. STATUS in build/build.py is still empty. Owner must supply one sentence.
2. Major, robustness: the primary CTA Resume (PDF) points to a Wix filesusr.com URL in header, hero and footer. assets/ holds no resume. If Wix retires it, the main CTA dies on every page. Owner must add assets/resume.pdf.
3. Major, content: "Start here" is Snake robots, one of the thinnest pages (no result or measurement). Aerobraking (46 orbits) is stronger evidence. Owner to supply 2 to 3 outcome sentences or move the label.
4. Major, visual: no real photograph survives; about portrait and figures are wixstatic hotlinks (dependency risk). Looks-good stays at 7 until owner media is local.
5. Minor, performance/CLS: hotlinked figures lack width/height, so layout shifts when real images load. Needs local images with known dimensions.
6. Minor, performance: no size-adjust fallback for the two web fonts; headings may reflow on swap. Needs measured metrics or self-hosted WOFF2.
7. Minor, UX (taste): on phone the sticky header shows only the K mark, with the name only in the H1 below. Acceptable on home; on deep project pages (aerobraking is about 6200 px tall on phone) nothing in view says whose site it is. Previously declined for width; consider a short "Karthik" next to the mark only if it fits at 360 px.
8. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat on home, list, About and project page without extra specifics. Add only owner-confirmed facts.
9. Nit, taste: Resume (PDF) appears in hero and footer on home, and LinkedIn twice; harmless.

## Good, must not regress
Plain lede with real numbers; ledger; struck-through marker highlight; varied stamps with real figures; ruled index with mono numbers; inverted-print dark theme; double rules; 44px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; accurate colophon.

## Verdict
The site commits coherently to the retro matte direction and reads as authored. What holds it back is missing owner input, not design: a current-status sentence, a local resume PDF, outcome sentences for Snake and Raftar, and real photographs with dimensions. Further designer cycles will find little to change until those arrive; the next gain is content, not styling.
