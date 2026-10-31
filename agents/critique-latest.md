# Critique, 2026-10-31 (cycle 54)

Rendering: `python3 tools/check.py . agents/shots` ran this cycle: 13 pages x 3 viewports x 2 themes, all OK (only "images not loaded" sandbox notes for Wix hosts). I viewed home phone-light, home desktop-dark and aerobraking-drl phone-light. git status is clean and no site files changed since cycle 53, so there are no new regressions. No site files edited.

## Sources consulted
Read: none this cycle. Every WebFetch (permission request unanswered) was blocked, so the three-source requirement is NOT met:
- https://web.dev/articles/optimize-cls (blocked)
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (blocked)
- https://developers.google.com/search/docs/appearance/structured-data/profile-page (blocked)
Carried over from cycle 53 (read then): WCAG 2.5.8 target size, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html; https://web.dev/articles/css-size-adjust. No finding below relies on an unread source; those that cite a principle say so as general practice.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Flat paper tone, ink rules, hard-offset button, inverted-print dark theme, no blur or glow (home desktop-dark and phone-light confirm).
2. Not AI-generated: met (see score).

## Scores
- AI-tell score: 2/10, unchanged. No gradients, glass, blobs, card trio, stats strip or floating badges. Specific and authored: struck-through "three weeks" on a highlighter band, "For the record" ledger, stamps with real numbers, Fig./Sheet tags, plain first-person prose. Faint tells: nine identically ruled rows with one mono tag column; DM Serif Display + Source Serif pairing is tasteful but common in editorial templates. No tells moved.
- Looks good: 7/10. Consistent rhythm, strong dark theme, clear hierarchy on home. Held at 7 because the site is type and schematics only: no photo of a real robot, car or person is visible anywhere, and on the aerobraking phone page (780x6246 px at 2x) the first schematic arrives after a long text-only run. Only the snake row on the index has a figure thumbnail; the other eight rows are text only, so the index looks top-heavy.
- SEO: 7/10. Title, description, canonical, OG/Twitter with local og:image 1200x630, Person and CreativeWork JSON-LD, sitemap, robots, noindex 404 are in the repo. Not verifiable offline: live og:image fetch, LCP/CLS on Wix images, whether a project-path robots.txt is honoured (it is not at host root).
- UX: 7/10. Phone first screen gives name, school, lab, advisor, one result, primary button, Resume and LinkedIn. Gaps: no current status, a single contact route (LinkedIn, owner constraint), "Start here" project is thin.
- Fun and personality: 7/10. Strike-through highlight, stamps, the 99 s pressable stamp and the 404 line are earned. Nothing new to add without new facts.

## Ranked findings
1. Major, content: status is stale and ambiguous. Home, About and Education say CMU MS "2023 - 2025"; today is 2026-10-31, so a recruiter cannot tell whether he graduated, where he is now or whether he is available. STATUS in build/build.py is empty. Owner must supply one sentence. Not designer-fixable.
2. Major, robustness: the primary CTA Resume (PDF) points to a Wix `filesusr.com` URL in the header, hero and footer on every page. assets/ holds only og.png, site.js and style.css. If Wix retires the file the main CTA dies on all pages. Owner must add assets/resume.pdf.
3. Major, content: "Start here" (Snake robots) is among the thinnest pages: schematic, question, lab, advisor, one sentence of motivation, no result and no statement of what he built or measured. Aerobraking (46 orbits) is far stronger. Owner should supply 2 to 3 outcome sentences or move the label.
4. Major, visual: no real photograph survives (about.html portrait and all figures are wixstatic hotlinks, also a dependency risk). Looks-good axis stays at 7 until owner media is local.
5. Minor, performance/CLS: hotlinked figures have no width/height, so the 220 px placeholder cannot match real ratios and shift remains on load. General CLS practice: reserve space from intrinsic size. Fix needs local images. (Source blocked this cycle.)
6. Minor, performance: no `size-adjust` fallback face for the two web fonts; headings can reflow on swap (https://web.dev/articles/css-size-adjust). Needs measured metrics or self-hosted WOFF2.
7. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat on home, list, About and project page with no further specifics. Add only owner-confirmed facts.
8. Minor, readability: aerobraking phone page is very tall, with a dense Problem section before the first figure. A split needs new subheads and owner agreement.
9. Minor, accessibility: Wix figure alt text is generic ("figure 1 of 3"). Owner must say what each shows.
10. Nit: only the first index row has a thumbnail on desktop, so rows 02-09 read as text-only against row 01. Consider it taste; local images would fix it.
11. Nit: stamps on four of nine rows; add none without real numbers.
12. Nit: phone header shows only the K mark; the name is the h1 directly beneath, so harmless.

Findings 1 to 4 move only with owner-supplied facts or files. More designer-only cycles will churn.

## Good, must not regress
Plain-prose home intro with the highlighted "three weeks to 15 minutes"; ruled project index with real-number stamps and "Start here"; "For the record" ledger; graph-paper Fig. plates with sheet tags; warm paper and inverted-print dark themes; hard-offset primary button; pressable 99 s stamp; 404 voice; honest colophon; footer with LinkedIn, GitHub and Resume on every page; previous/next links with summaries; 44 px tap targets; 3 px focus outline via :focus-visible; prefers-reduced-motion rule.

## Verdict
The site commits coherently to the retro matte direction and reads as authored by a person. Rendering is clean across 78 screenshots with no overflow or contrast failures. What holds every axis at 7 is missing owner input, not craft: a current status sentence (the 2023-2025 dates are now stale), a local resume file, results for the "Start here" project, and real photographs. The research for this cycle was blocked, so no new external findings were added. The designer has nothing substantial left to fix alone.
