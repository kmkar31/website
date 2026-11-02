# Critique, 2026-11-02 (cycle 63)

Rendering: `python3 tools/check.py . agents/shots` completed; every page, viewport and theme reports OK (only "images not loaded" notes, a sandbox limit for Wix hotlinks). I viewed index-phone-light, index-desktop-light and about-desktop-dark. The repo is clean and no site files changed since the last critique, so there is no regression. No site files edited.

## Sources consulted
No web source was fetched this cycle: I did not run WebSearch/WebFetch, so the three-source requirement is not met. The pointers below are carried over from the last cycle and are unverified. Nothing in the findings rests on their wording; findings rest on the repo and the screenshots.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (the site's 44 px targets exceed 24 px).
- Chrome, Improved font fallbacks (size-adjust, ascent-override): https://developer.chrome.com/blog/font-fallbacks
- NN/g, UX design portfolios: https://nngroup.com/articles/ux-design-portfolios/
Topics this cycle: content currency, hotlink fragility, CLS.

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper ground with faint grain, ink rules, hard-offset button, mono ledger, ruled stamps, inverted-print dark theme. No blur, glow or gradient in the renders I viewed.
2. Must not look AI-generated: met. First-person copy with specific numbers, a ruled index instead of a card grid, struck-through "three weeks", figure-numbered plates. No new owner notes since 2026-10-22.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows with a repeated mono tag column; DM Serif Display plus Source Serif is tasteful but common. No tells moved.
- Looks good: 7/10. Desktop home is balanced and calm and the stamps give rhythm. No real photograph renders anywhere. Only row 01 has a visual (a small schematic). The right third of About is empty when the portrait is missing, apart from an "On this page" list.
- SEO: 7/10. Unique titles, canonical, OG and Twitter tags, local og:image, JSON-LD, sitemap, robots, noindex 404, one h1. Not verifiable offline: LCP and CLS with Wix images, and live og:image fetch. robots.txt sits at a project subpath, so submit the sitemap in Search Console.
- UX: 7/10. The phone first screen gives name, school, lab, advisor, a concrete result, the primary button, Resume and LinkedIn. Gaps: stale status, thin "Start here" page, one contact route (owner constraint), Resume on a Wix URL.
- Fun and personality: 7/10. Marker strike-through, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET", "500 M OF TETHER", sheet-number captions, pressable 99 s stamp. More needs owner facts.

## Ranked findings
1. Major, content: stale status. The home subtitle, home meta description, About intro ("is at Carnegie Mellon University (2023 - 2025)") and Education all present the MS as current or ending 2025. Today is 2026-11-02. `STATUS` in build/build.py is still empty, so the ledger has no Status row. A recruiter cannot tell whether he has graduated, where he is now, or whether he is open to roles. This is the largest credibility gap. It needs one owner sentence and the slot is ready.
2. Major, robustness: "Resume (PDF)" in the header, hero and footer on every page points to a Wix filesusr URL (confirmed in index.html). If Wix retires it, the resume breaks site-wide. The owner must supply assets/resume.pdf.
3. Major, content/UX: the labelled "Start here" project (Snake robots) is the thinnest page: one short paragraph, a schematic and a pager, with no result. The strongest evidence on the site (Aerobraking, 46 orbits; Hasselhoff, 99 s) is not the labelled entry. The owner should supply 2 to 3 outcome sentences for Snake, or move the label.
4. Major, visual: no real photograph of a robot, car, satellite or person survives in the sandbox render. Figures and the About portrait are Wix hotlinks. This is the main reason Looks-good stays at 7. Owner media with known dimensions is needed. Hotlinking is also a dependency risk (same as finding 2).
5. Minor, performance: hotlinked figures lack width/height, so layout can shift on load. It resolves with local images.
6. Minor, performance: two Google web fonts with no size-adjusted fallback. A fix needs the real font files to measure, or self-hosted WOFF2.
7. Minor, content: Raftar says "40+ students", "captained" and "suspension and brakes" and nothing more. Add only owner-confirmed specifics.
8. Minor, visual (taste): on phone only row 01 carries a figure, above its heading, so the list opens with a different shape from the other eight. Acceptable while it is the only visual.
9. Minor, UX (taste): the phone header shows only the K mark. On long project pages nothing in view names the owner. Reopen only if the name fits at 360 px.
10. Nit, taste: Resume and LinkedIn repeat in the hero and the footer. Harmless, and it aids findability.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps only where the number is the point; ruled index with mono numbers; inverted-print dark theme; double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; honest "schematic" captions; accurate colophon; desktop header showing the name; Aerobraking h2 structure.

## Verdict
The site commits coherently to the retro matte direction and reads as the work of a person. Both owner constraints are met and nothing regressed. What holds it back is missing owner input, not design: a current-status sentence (overdue), a local resume PDF, outcome sentences for Snake and Raftar, real photographs with dimensions, and font files. Designer cycles will find little to change until those arrive. Findings 1 to 4 all depend on the owner. This critique did no fresh web research, so treat its citations as unverified.
