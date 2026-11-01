# Critique, 2026-11-01 (cycle 61)

Rendering: `python3 tools/check.py . agents/shots` ran; all pages x 3 viewports x 2 themes report OK (only "images not loaded" notes, a sandbox limit for Wix hotlinks). I viewed index-phone-light, index-desktop-dark and snake-robots-tablet-light. HEAD is 38636f7; recent commits changed no site files, so no regressions. No site files edited.

## Sources consulted
WebSearch worked this cycle, but WebFetch of the result pages was not attempted, so these are search-result pointers, not read-through quotations. Claims below rest mainly on repo evidence and screenshots.
- NN/g, UX design portfolios: https://nngroup.com/articles/ux-design-portfolios/ (hiring managers skim; they want clear process and outcomes per project)
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/optimize-cls/ (set width/height on images; font fallbacks cause shift)
- W3C, Understanding SC 2.4.11 Focus Not Obscured (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured (sticky headers must not hide the focused element)

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like, no glossy gradients: met. Paper tone, ink rules, hard-offset button, mono ledger, ruled stamps, dark theme as inverted print. No blur, glow or gradient in the renders.
2. Must not look AI-generated: met. First-person copy with specific numbers, a ruled list instead of a card grid, struck-through "three weeks" on a marker band.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows with a mono tag column; DM Serif + Source Serif is tasteful but common. No tells moved.
- Looks good: 7/10. Desktop dark and light are balanced and consistent. Held at 7 because only row 01 has an image (a generic line schematic) and no real photo of a robot, car, satellite or person renders anywhere. On the Snake page the large empty grid schematic is the whole visual payload.
- SEO: 7/10. Title, description, canonical, OG/Twitter with local og:image (absolute URL), JSON-LD, sitemap, robots, 404 all present. Not verifiable offline: live og:image fetch, LCP/CLS with Wix images.
- UX: 7/10. Phone first screen gives name, school, lab, advisor, one result, primary CTA, Resume, LinkedIn. Gaps: stale status, single contact route (owner constraint), thin "Start here" page.
- Fun and personality: 7/10. Strike-through highlight, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET", "500 M OF TETHER" stamps, "SHEET 1 OF 9 · NTS" caption. Nothing more to add without new facts.

## Ranked findings
1. Major, content: stale status. Home, About and Education say CMU MS 2023 to 2025; today is 2026-11-01. `STATUS = ""` at build/build.py:259, so the ledger has no Status row. A recruiter cannot tell if he has graduated, where he is, or whether he is available. NN/g notes hiring managers skim for current relevance. Needs one owner sentence.
2. Major, robustness: the primary CTA "Resume (PDF)" (header, hero, footer, every page) points at a Wix filesusr.com URL. Every page has 2 to 9 wixstatic/filesusr references (grep count: aerobraking 9, quadrotor-sysid 7, assistive-tricycle/hasselhoff/tethered 6). If Wix retires the file, the main CTA dies site-wide. Owner must supply assets/resume.pdf.
3. Major, content/UX: the "Start here" project (Snake) is the thinnest page: one short "Why snake robots" paragraph, a schematic, a Next link, no result. The strongest evidence on the site (Aerobraking 46 orbits, Hasselhoff 99 s) is not labelled. Owner to supply two or three outcome sentences, or move the label.
4. Major, visual: no real photograph survives; project figures and the About portrait are Wix hotlinks, a dependency risk and the reason Looks-good stays at 7. Owner media needed.
5. Minor, performance: hotlinked figures lack width/height (web.dev CLS guidance), so layout shifts as they load. Local images with known dimensions fix it.
6. Minor, performance: no size-adjusted fallback for the two Google fonts; needs measured metrics or self-hosted WOFF2.
7. Minor, accessibility: header is sticky and `scroll-padding-top:80px` is set (good, covers SC 2.4.11 for anchors). Worth a keyboard-tab check on long project pages with lightbox links to confirm focused figure links are never hidden under the header; not verified here.
8. Minor, visual (taste): on phone only row 01 carries a figure, above its heading, so the list opens with a different shape than the other eight. Place it after the blurb, or drop it on phone, until more thumbnails exist.
9. Minor, UX (taste): on phone the header shows only the K mark; nothing in view on long project pages names the owner. Reopen only if "Karthik" fits at 360 px.
10. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) recur with no further specifics. Add only owner-confirmed facts.
11. Nit, taste: Resume and LinkedIn repeat in hero and footer on home; harmless.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; marker-band strike-through; stamps carrying real figures; ruled index with mono numbers; inverted-print dark theme (amber on warm black reads cleanly); double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; honest caption ("Module count is illustrative"); accurate colophon; desktop header showing the name.

## Verdict
The site commits coherently to the retro matte direction and reads as authored by a person; the owner's two constraints are met. What holds it back is missing owner input, not design: a current-status sentence, a local resume PDF, outcome sentences for Snake and Raftar, and real photographs with dimensions. Designer cycles will find little to change until those arrive; the top three items are all owner-dependent.
