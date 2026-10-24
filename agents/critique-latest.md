# Critique, 2026-10-24 (after cycle 12)

## Sources
WebFetch was blocked again (permission unanswered) for all three attempts, so none were opened. They are pointers, not verified quotes:
- https://web.dev/articles/optimize-cls (font swap shift, size-adjust fallback) - blocked
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (SC 2.5.8) - blocked
- https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ (scannability) - blocked
Findings rest on what I measured and saw.

Measured: tools/check.py ran to completion (13 pages x 3 viewports x 2 themes): no failures. I looked at home (phone light, desktop light), snake-robots phone, About desktop, tethered-nanosatellite desktop dark. Repo grep: every page still references wixstatic/filesusr (2 to 9 times each; the resume PDF is one), fonts come from Google Fonts, assets/ holds only og.png, site.js, style.css. STATUS in build/build.py is still "".

## Scores
- AI-tell: 3/10 (was 4). The "Fig. N" lab-notebook plates are the first idea in the site that is a point of view, not a kit. Remaining tells: warm cream + serif + terracotta + mono labels is a common "tasteful editorial" kit; row anatomy (title, blurb, mono index, tag) is uniform; the home page would swap cleanly to another person. Praise (authored, specific): struck-through "three weeks", 99 s stamp, "failed to land on the target" 404, "Start here", Fig. 1 captions that say "Not to scale" / "illustrative".
- Looks good: 6/10. Home is calm and well-set. Project pages are now clearly better (Fig. 1 plate). But still no photograph or real result anywhere, the plates are schematic only, and some are weak (see finding 5). Long background paragraphs follow.
- SEO: 7/10. Titles, descriptions, canonical, OG/Twitter, local og.png, JSON-LD, sitemap present. Weaker: third-party render-blocking Google Fonts, no fallback metrics; robots.txt unusable on a subpath; all media is Wix hotlinks, so image alt text indexes nothing useful; og.png is text only.
- UX: 6/10. Name, field, strongest project, resume and LinkedIn are visible on one phone screen. Misses: no date or status line (today is Oct 2026, site says MS 2023-2025), contact is LinkedIn only, resume dependent on a Wix URL, no outcomes beyond a few numbers.
- Fun and personality: 6/10 (was 5). Plates and 99 s press stamp helped. Still mostly a clean resume.

## Owner critique (user-critique.md)
1. Retro, matte: met. Flat paper, ink rules, one hard-shadowed button, no blur or gradient, graph-paper plates are on-brief. Grain is barely perceptible, which is fine.
2. Not AI-looking: much improved; the remaining risk is the kit in finding 4.

## Findings (ranked)

1. Major (robustness / UX). The resume PDF, the site's main call to action (home, About, header, every footer), is still a hotlink to filesusr. A dead link would silently break the one thing a recruiter wants. Not verifiable offline whether it is live. Fix: owner drops resume.pdf into assets/; designer links to it. Ten-plus cycles of "owner files needed" is now the biggest risk to the site, and it should be raised to the owner directly, not repeated in the log.

2. Major (UX, stale content). No status or date. Home says "MS ... Carnegie Mellon University"; About says 2023 - 2025; the date is October 2026. A professor or recruiter cannot tell if he has graduated or is available. This reads as an out-of-date site. Owner needs to supply one line; the STATUS slot is ready but empty.

3. Major (looks good / UX). Project pages show no real evidence of the work. Snake-robots on phone: title, tl;dr, two fact rows, one schematic, generic field paragraph ("Snake robots are highly articulated robots ..."), pager. That background paragraph is textbook intro, not his work, and it is the longest block. Fig. 1 is helpful but illustrative only (the caption admits module count is made up). Owner media (one photo or plot per project) is the real fix; until then, shorten the generic background and put what he did first. Source: NN/g scannability (unverified).

4. Major (AI-tell, taste). The cream/terracotta/serif/mono-label combination plus numbered rows and ledger sidebar is the familiar editorial template, even though it is well done. Plates are the escape; commit further. Concrete options: give every plate the same drawing conventions (title block with sheet number "1 of 9", scale or "NTS", date), as an engineering drawing sheet; make the home index look like a drawing register (sheet no., title, rev) rather than a blog list. Trade-off: keep it light so contrast and scanning stay intact.

5. Major (looks good, plate quality). Tethered nanosatellite plate (desktop dark): the 1U/3U/tether drawing is ambiguous. The "500 m tether" label floats left of the line, the tether is broken by a stray double slash, and the 3U box sits below the Earth arc while the tether crosses the horizon line, so it reads as a satellite below the surface. Also the plate is bottom-clipped by the viewBox (the arc runs off the frame). Verify each of the nine plates for clipped or ambiguous geometry; this one needs a redraw.

6. Major (fun, borderline at 6, below 7 target). Delight sits in a few places. Ideas from facts already in the repo, no invention: (a) on Aerobraking, a small orbit-count tally "46 / 46" that fills as you scroll is decorative, so prefer a static "Fig." with the 46 orbits drawn as 46 ticks; (b) Hasselhoff page: make the 99 s counter also mark the IR beam in Fig. 1; (c) About: strike-through already used, add a margin note style (mono, rotated stamp) for the Formula Bharat podium. Keep all static or press-only for reduced motion.

7. Major (UX, About desktop). Right column is an "On this page" index with a large void beneath it, and the content column stops at 760 px while the header spans 1000 px, so the page looks left-heavy (screenshot). It is a decent fallback for the missing portrait, but once the portrait is supplied the index vanishes, so there are two layouts to keep honest. Taste; minor if photos arrive.

8. Minor (SEO / CWV). Google Fonts is render-affecting and third party with no size-adjusted fallback; self-host WOFF2 (owner or a machine with network). Source: web.dev optimize-cls (unverified). Also each page loads 3-9 Wix images that may fail; with no width/height there is CLS risk when they load.

9. Minor (SEO). robots.txt is ignored under a project subpath; the sitemap is only found if submitted in Search Console. OG card is text only. Already acknowledged by the designer.

10. Minor (UX). Phone header has no resume or contact; footers carry them. Home phone: the three actions wrap with "Contact on LinkedIn" alone on a second row, left aligned to nothing in particular (screenshot). Put the two text links on one row.

11. Minor (UX). Home and Projects both list all nine; Projects with no thumbnails adds little. Consider whether it earns a nav slot, or move filters to home.

12. Minor (content). Row blurb, page tl;dr and (previously) pager repeated the same sentence; the pager now differs, good. The Hasselhoff blurb still leads with the SpongeBob joke before what it does; fine as voice, but check the project page lead matches.

13. Nit. Dark theme footer and header rules are consistent, but muted mono tags in dark mode rely on a light tan (#d9cfba); fine on contrast, slightly flat. Taste.

14. Nit. "Contact on LinkedIn" and "message me on LinkedIn" is a single contact route; say so once on home and drop the repetition.

## Good, do not regress
- Home: name, one-line affiliation, specific lede, struck-through "three weeks to 15 minutes", ledger, "Start here".
- Flat matte system: ink rules, one hard-shadow button, no gradients, blur, glow or floating chips.
- Fig. N plates with honest "not to scale / illustrative" captions, repo-local, cannot hotlink-fail.
- Dark theme as inverted print with readable contrast.
- Unique titles and meta, canonical, JSON-LD, local og.png, sitemap, 404 with noindex.
- Graceful collapse of failed images, captions and portrait; pager with neighbour fact.
- 404 line, pressable 99 s stamp, plain colophon.

## Verdict
The site now has a voice and one real visual idea: lab-notebook plates on graph paper, set in a flat print system with no generator tells. What keeps it from being good rather than merely tidy is still substance and risk, not polish: the resume and every photo are Wix hotlinks, there is no status or date line, and project pages lack real evidence of results. Inside the repo, the next gains are to commit to the drawing-sheet idea (title blocks, sheet numbers, a drawing-register index), redraw the weak tethered plate and check the other eight for clipping, and cut the generic background paragraphs. Outside the repo, the owner must supply the resume file, one status line and one image per project; nothing else moves the scores more.
