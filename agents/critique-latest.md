# Critique, 2026-11-01 (cycle 60)

Rendering: `python3 tools/check.py . agents/shots` completed (run in background; it exceeds the 2-minute foreground limit). All pages x 3 viewports x 2 themes report OK; the only notes are "images not loaded" (sandbox, Wix hotlinks). I viewed index-phone-light, index-desktop-light and about-tablet-dark. HEAD is 1e2a69c; the last several commits changed no site files, so there are no regressions. No site files edited.

## Sources consulted
Research was blocked again. WebFetch returned "permission request not answered" for https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, https://web.dev/articles/optimize-cls and https://www.nngroup.com/articles/ux-design-portfolios/ (not retried). I did not run a WebSearch. No best-practice claim below relies on those pages; findings rest on repo evidence and screenshots. The three-source rule is not met this cycle. Note for the owner: the sandbox cannot get web permission approvals, so this rule will keep failing until URLs are pre-approved.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met. Paper tone, ink double rules, hard-offset button, mono ledger, ruled stamps, dark theme as inverted print. No blur, glow or gradient visible in the screenshots.
2. Must not look AI-generated: met. Plain first-person copy with specific numbers; the struck-through "three weeks" on a marker band is authored. The index is a ruled list, not a card grid.

## Scores
- AI-tell score: 2/10, unchanged. Faint tells: nine identically ruled rows with a mono tag column; the DM Serif + Source Serif pairing is tasteful but common. No tells moved.
- Looks good: 7/10. Desktop light home is balanced: heavy rule, ledger sidebar, even row rhythm. Held at 7 because eight of nine index rows have no image and the one that does is a generic line-drawing schematic; on phone that figure sits above the title of row 01 only, so row 01 has a different shape from the other eight. No photograph of a robot, car, satellite or person is visible anywhere in the render.
- SEO: 7/10. Title, description, canonical, OG/Twitter with local og:image, JSON-LD, sitemap, robots and a 404 are in the repo. Not verifiable offline: live og:image fetch, LCP/CLS with Wix images.
- UX: 7/10. Phone first screen gives name, school, lab, advisor, one result, primary button, Resume and LinkedIn. Gaps: stale status, one contact route (owner constraint), weak "Start here" page.
- Fun and personality: 7/10. Strike-through highlight, "TIME ALLOWED: 99 S", "46 ORBITS TO TARGET", "500 M OF TETHER" stamps, 404 line. Nothing more to add without new facts.

## Ranked findings
1. Major, content: status is stale. Home, About and Education say CMU MS 2023 to 2025; today is 2026-11-01. `STATUS = ""` in build/build.py:259, so the ledger shows no Status row. A recruiter cannot tell whether he has graduated, where he is now, or whether he is available. Needs one owner sentence.
2. Major, robustness: the primary CTA "Resume (PDF)" (header, hero, footer, every page) points at a Wix filesusr.com URL (index.html still has 3 wix hotlinks). If Wix retires the file the main CTA dies site-wide. Owner must supply assets/resume.pdf.
3. Major, content/UX: the "Start here" project is the weakest page, while the strongest evidence on the site (Aerobraking, 46 orbits; Hasselhoff, 99 s) is not the one labelled. Snake body is a short "Why snake robots" paragraph, a schematic and a Next link; no result or outcome. Owner to supply two or three outcome sentences, or move the label.
4. Major, visual: no real photograph survives; the About portrait and project figures are wixstatic hotlinks, both a dependency risk and the reason Looks-good stays at 7. Owner media needed.
5. Minor, performance: hotlinked figures lack width/height, so layout shifts when images load. Local images with known dimensions fix it.
6. Minor, performance: no size-adjusted fallback for the two Google fonts; needs measured metrics or self-hosted WOFF2.
7. Minor, visual (taste): on phone only row 01 has a figure, placed above its heading, so the list starts with a different pattern than the other eight. Consider placing the figure after the blurb, or omit it on phone, until real thumbnails exist for more rows.
8. Minor, UX (taste): on phone the header shows only the K mark; on very long project pages nothing in view names the site owner. Previously declined for width; reopen only if "Karthik" fits at 360 px.
9. Minor, content: Raftar claims (40+ students, captained, suspension and brakes) repeat across several places with no further specifics. Add only owner-confirmed facts.
10. Nit, taste: Resume (PDF) and LinkedIn repeat in hero and footer on home; harmless.

## Good, must not regress
Plain lede with real numbers; "For the record" ledger; struck-through marker highlight; stamps carrying real figures; ruled index with mono numbers; inverted-print dark theme (amber on warm black reads cleanly on About); double rules; 44 px tap targets; no-JS figure links; local og:image; JSON-LD; 404 line; honest figure caption ("Module count is illustrative"); accurate colophon.

## Verdict
The site commits coherently to the retro matte direction and reads as authored by a person. What holds it back is missing owner input, not design: a current-status sentence, a local resume PDF, outcome sentences for Snake and Raftar, and real photographs with dimensions. Further designer cycles will find little to change until those arrive. Caveat: external research was blocked again, so no new best-practice claim is made.
