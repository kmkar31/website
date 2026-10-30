# Critique, 2026-10-30 (cycle 45)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Looked at home phone light, home desktop light, home tablet dark and Snake robots phone light. HEAD edbd2a0 is a log-only commit, so there is no site change since cycle 41 and no regression. No site files edited.

## Sources consulted
WebFetch of https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html was blocked by the permission layer ("do not retry"), as in cycle 44. Nothing was fetched, so these are from prior knowledge and unverified:
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (the site's 3 px offset focus outline is consistent with it)
- https://web.dev/articles/optimize-cls (image dimensions, font swap)
- https://www.nngroup.com/articles/mobile-ux/ (short scannable mobile content)
Repo checks: global :focus-visible outline 3 px, prefers-reduced-motion block present, resume link is still a filesusr.com (Wix) hotlink with target=_blank and an sr-only "opens in a new tab" note.

## Scores
- AI-tell score: 2/10, unchanged. Authored voice: Fig. 1 plate with sheet tag, stamps tied to real numbers, struck-through "three weeks" on a highlighter band, "For the record" ledger, honest colophon. No tells moved. Faint remaining tell: very even ruled rows with a right-hand index/tag column.
- Looks good: 7/10. Warm paper palette, double rules, ink footer, dark theme as inverted print, clean rhythm on all three viewports. Held back by no photograph of a real object or person and rows 02 to 09 being text-only beside one plated row.
- SEO: 7/10. Unique titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404 present. Wix image dimensions unknown, so CLS unverifiable offline.
- UX: 7/10. Phone first screen answers who, where, what, with a button, resume and LinkedIn. No status line; LinkedIn is the only contact route.
- Fun and personality: 7/10. 99 s press-and-hold stamp, stamps, 404, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met (flat surfaces, rules, one hard-shadow button, faint grain, no gradients or blur).
2. Must not look AI-generated: met; I score it 2/10.

## Ranked findings
1. Major, content: no status line. Home and About say Master's 2023 - 2025 and today is 2026-10-30. A recruiter cannot tell whether he has graduated, where he is now, or whether he is available. Needs one owner sentence (STATUS slot in build.py is ready). Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project. The page has only an illustrative schematic ("Module count is illustrative"), a question and a link out, with no result or number. Aerobraking (46 orbits) is far stronger. Owner supplies outcomes, or moves the label.
3. Major, robustness: the resume and the real project figures are Wix hotlinks. One Wix change silently breaks the primary call to action. Owner must add assets/resume.pdf and media.
4. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium). The first impression is type and drawings only (screenshots confirm).
5. Minor, content: Raftar facts repeat (40+ students, captained, suspension and brakes) across home, About and project page with no specifics. The Ferrari weight / 0-60 claim still awaits owner confirmation.
6. Minor, readability: Aerobraking is a long run of dense paragraphs; a pull-out of the reward function only if the owner agrees.
7. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4, so font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
8. Minor, accessibility: alt text for Wix figures cannot be checked offline.
9. Nit, contact: LinkedIn only (owner constraint).
10. Nit: stamps are on four rows; add no more without real numbers.
11. Nit: on desktop About leaves the right third empty (documented taste).

Items 1 to 5, 7 and 8 need owner facts or files. I found nothing designer-fixable.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through "three weeks", one button, resume and LinkedIn.
- Fig. 1 plate with honest caption; stamps tied to real numbers.
- Ruled project index with 44 px targets; Next pager on project pages.
- Dark theme as inverted print; ink footer; 404 and colophon voice.
- Type: DM Serif Display, Source Serif 4, mono for metadata.
- About: single-line "podium finish" mark, ruled skills and experience lists.

## Verdict
The site is at a fixed point: a coherent retro matte direction, specific plain copy, clean checks and no regressions. The 7s are held by missing owner material (a status sentence, a real resume PDF and photos, outcomes for the "Start here" project, Raftar specifics), not by craft. More designer cycles will only churn until the owner supplies those facts and files.
