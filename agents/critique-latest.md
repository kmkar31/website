# Critique, 2026-11-01 (cycle 56)

Rendering: `python3 tools/check.py . agents/shots` ran (13 pages x 3 viewports x 2 themes, 78 lines, no failure; only "images not loaded" sandbox notes). I viewed index-phone-light and index-desktop-dark. HEAD is b64538d, tree clean, no site files changed since cycle 54, so no regressions. No site files edited.

## Sources consulted
WebFetch was blocked this cycle (permission request unanswered) for https://web.dev/articles/optimize-cls, https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html and https://www.nngroup.com/articles/mobile-ux/. None was read, so the three-source rule is NOT met. Findings below rest on repo evidence and screenshots; the CLS point is general practice (web.dev optimize-cls), unverified this cycle. Previously read (cycle 53): WCAG 2.2 target-size-minimum, web.dev css-size-adjust.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Paper tone, ink rules, hard-offset button, mono ledger, inverted-print dark theme; no blur, glow or gradient.
2. Not AI-generated: met.

## Scores
- AI-tell score: 2/10, unchanged. Authored specifics: struck-through "three weeks" on a marker band, "For the record" ledger, stamps with real numbers, plain first-person prose. Faint tells: nine identically ruled rows with a mono tag column; DM Serif + Source Serif is tasteful but common. No tells moved.
- Looks good: 7/10. Rhythm and dark theme are strong. Held at 7: no photo of any robot, car or person is visible; only the snake row has a thumbnail, so the other eight rows are text only and the index is top-heavy. The phone aerobraking page is very long (780x6246 px at 2x).
- SEO: 7/10. Title, description, canonical, OG/Twitter with local og:image, Person and CreativeWork JSON-LD, sitemap, robots, noindex 404 are in the repo. Not verifiable offline: live og:image fetch, LCP/CLS on Wix images, project-path robots.txt (not honoured at host root).
- UX: 7/10. Phone first screen gives name, school, lab, advisor, one result, primary button, Resume and LinkedIn. Gaps: no current status, one contact route (LinkedIn, owner constraint), thin "Start here" project.
- Fun and personality: 7/10. Strike-through highlight, stamps, the 99 s stamp and the 404 line are earned. Nothing to add without new facts.

## Ranked findings
1. Major, content: status is stale. Home, About and Education say CMU MS 2023-2025; today is 2026-11-01. A recruiter cannot tell whether he graduated, where he is, or if he is available. STATUS in build/build.py line 259 is still empty. Owner must supply one sentence.
2. Major, robustness: the primary CTA Resume (PDF) links to a Wix filesusr.com URL in the header, hero and footer on every page. assets/ holds only og.png, site.js, style.css. If Wix retires the file, the main CTA dies everywhere. Owner must add assets/resume.pdf.
3. Major, content: "Start here" (Snake robots) is among the thinnest pages (schematic, question, lab, advisor, no result or measurement). Aerobraking (46 orbits) is stronger. Owner should supply 2 to 3 outcome sentences or move the label.
4. Major, visual: no real photograph survives; about portrait and all figures are wixstatic hotlinks (dependency risk). Looks-good stays at 7 until owner media is local.
5. Minor, performance/CLS: hotlinked figures lack width/height, so shift remains when real images load. Needs local images with known dimensions.
6. Minor, performance: no size-adjust fallback for the two web fonts; headings may reflow on swap (web.dev css-size-adjust). Needs measured metrics or self-hosted WOFF2.
7. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat on home, list, About and project page with no extra specifics. Add only owner-confirmed facts.
8. Nit, taste: Resume (PDF) appears three times on the phone home page (hero, footer, plus LinkedIn twice); harmless but the footer repeats the hero.

## Good, must not regress
Plain lede with real numbers; ledger; struck-through marker highlight; varied stamps; ruled index with mono numbers; inverted-print dark theme; double rules; 44px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; accurate colophon.

## Verdict
The site commits coherently to the retro matte direction and reads as authored. What holds it back is no longer design but missing owner inputs: a current-status sentence, a local resume PDF, outcome sentences for Snake and Raftar, and real photographs with dimensions. Until those arrive, further designer cycles will find little to change; the next real gain is content, not styling.
