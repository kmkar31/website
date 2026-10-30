# Critique, 2026-10-30 (cycle 46)

Rendered with tools/check.py (13 pages x 3 viewports x 2 themes: all OK, only sandbox image-load notes). Screenshots written to the session scratchpad, not agents/shots. Looked at home phone light, home desktop dark and Aerobraking tablet light. HEAD 4165eab is a log-only commit, so the site is unchanged since cycle 41 and there is no regression. No site files edited.

## Sources consulted
Source fetching is still blocked by the permission layer ("do not retry"): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html was refused this cycle, as were the WCAG focus-appearance page in cycle 45 and earlier. Nothing was fetched, so these are from prior knowledge and unverified:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 px minimum; the site's 44 px targets exceed it)
- https://web.dev/articles/optimize-cls (image dimensions, font swap)
- https://www.nngroup.com/articles/mobile-ux/ (short scannable mobile content)
Repo checks: titles unique (home "Karthik Karumanchi | Control of Robots and Spacecraft"); og:image tags present; resume still a filesusr.com (Wix) hotlink; project figures still static.wixstatic.com with lazy loading and meaningful but short alt text.

## Scores
- AI-tell score: 2/10, unchanged. Authored voice: Fig. 1 plate with sheet tag, stamps tied to real numbers (46 orbits, 500 m, 99 s), struck-through "three weeks" on a highlighter band, "For the record" ledger, colophon. No tells moved. Faint remaining tell: very even ruled rows with a right-hand index/tag column.
- Looks good: 7/10. Warm paper palette, double rules, dark theme as inverted print, steady rhythm on all viewports. Held back by no photograph of a real object or person, and rows 02 to 09 being text-only beside one plated row.
- SEO: 7/10. Unique titles, descriptions, canonical, OG, JSON-LD, sitemap, robots, 404. Wix image dimensions unknown, so CLS is unverifiable offline.
- UX: 7/10. Phone first screen answers who, where, what, with a button, resume and LinkedIn. No status line; LinkedIn is the only contact route.
- Fun and personality: 7/10. Stamps, 99 s press-and-hold, 404, colophon. Quiet but earned.

## Owner critique (agents/user-critique.md)
1. Retro matte, print-like, no glossy gradients: met (flat surfaces, rules, one hard-shadow button, faint grain, no gradients or blur).
2. Must not look AI-generated: met; scored 2/10.

## Ranked findings
1. Major, content: no status line. Home and About say Master's 2023 - 2025 and today is 2026-10-30; a recruiter cannot tell if he has graduated, where he is, or if he is available. Needs one owner sentence (STATUS slot in build.py is ready). Not designer-fixable.
2. Major, content: "Start here" (Snake robots) is the thinnest project: illustrative schematic, a question and a link out, no result or number. Aerobraking (46 orbits) is stronger. Owner supplies outcomes or moves the label.
3. Major, robustness: the resume and all real project figures are Wix hotlinks. One Wix change silently breaks the primary call to action. Owner must add assets/resume.pdf and media.
4. Major, visual: no photograph of a real object or person (snake robot, RFR23 car, podium). First impression is type and drawings only (confirmed in screenshots).
5. Minor, content: Raftar facts repeat (40+ students, captained, suspension and brakes) across home, About and project page with no specifics; the Ferrari weight / 0-60 claim awaits owner confirmation.
6. Minor, readability: Aerobraking (tablet screenshot) is a long run of dense paragraphs whose text points to figures ("as shown below") that sit in Wix images. A reward-function pull-out only if the owner agrees.
7. Minor, performance: no size-adjusted fallback for DM Serif Display / Source Serif 4, so font swap can reflow headings. Needs real metrics or self-hosted WOFF2.
8. Minor, accessibility: alt text on Wix figures is short ("Aerobraking maneuver definition"); cannot judge adequacy without the images.
9. Nit, contact: LinkedIn only (owner constraint).
10. Nit: stamps on four rows; add none without real numbers.
11. Nit: on desktop About leaves the right third empty (documented taste).

Items 1 to 5, 7 and 8 need owner facts or files. I found nothing designer-fixable.

## Good, must not regress
- Home phone first screen: name, degree line, two plain real-fact paragraphs, struck-through "three weeks", one button, resume and LinkedIn.
- Fig. 1 plate with honest caption; stamps tied to real numbers.
- Ruled project index with 44 px targets; Previous/Next pager on project pages.
- Dark theme as inverted print; ink footer; 404 and colophon voice.
- Type: DM Serif Display, Source Serif 4, mono for metadata.
- Aerobraking page: key-results row, orbit diagram, sheet tag.

## Verdict
The site is at a fixed point: a coherent retro matte direction, specific plain copy, clean checks and no regressions. The 7s are held by missing owner material (a status sentence, a real resume PDF and photos, outcomes for the "Start here" project, Raftar specifics), not by craft. More designer cycles will only churn until the owner supplies those facts and files.
