# Critique, cycle 6 (2026-10-23)

Method: ran `tools/check.py` (13 pages, 3 viewports, 2 themes; zero failures, only "images not loaded" notes from the sandbox). Looked at home desktop light, home phone light, About desktop dark, snake-robots phone light. Read about.html and build for SEO. Wix media is blocked in the sandbox; I count the hotlink dependency, not the broken boxes.

Sources: WebSearch returned only result titles this cycle (page text not fetched), so these are pointers, not verified quotes.
- NN/g portfolio and hiring-manager material (search: nngroup.com/articles, uxdesign.cc "What hiring managers look for in a portfolio"): https://uxdesign.cc/what-hiring-managers-look-for-in-a-product-design-portfolio-7b1837360bf9
- WCAG 2.2 Reflow and Text Spacing: https://w3c.github.io/wcag/understanding/reflow and https://tabnav.com/academy/wcag/success-criterion-1.4.12
- fetchpriority / LCP image: https://developer.mozilla.org/docs/Web/HTML/Reference/Attributes/fetchpriority and https://addyosmani.com/blog/fetch-priority/
Topic this cycle (varied): hiring-manager scanning, reflow/text spacing, LCP and image priority.

## Scores
AI-tell: **3 / 10** (unchanged). Moved: stamps are now varied (double, dashed, tilted, improvement); portrait fallback added; description trimmed. Still generic: warm cream / DM Serif / terracotta / amber is the current "editorial" look; every project row has the same anatomy; no person in the copy beyond the first paragraph; nothing would break if another engineer's facts were swapped in. Authored and specific: struck-through "three weeks", the 99-second stamp, the Hasselhoff blurb, the 404.

| Axis | Score | Evidence |
|---|---|---|
| Looks good | **6** | Home is well set and calm. But there is not one picture on the site that loads from the repo; About with the portrait collapsed is a text document; project pages (snake, phone) are a headline, two fact rows and one paragraph, then a pager: bare. |
| SEO | **6** | Titles, meta, canonical, OG, JSON-LD, sitemap are good. Gaps: 13 pages carry Wix hotlinks (about 32 references), no image dimensions, home h1 is the name only, Google Fonts third party, og.png is text. |
| UX | **6** | Contact, resume, projects reachable in one phone screen. But status/dates stale, resume on Wix, no start-here project, project pages thin. |
| Fun | **6** | Real touches exist but are static; nothing tactile or discoverable. |

All four are below 7, so each has a Major finding (1, 2, 3, 4, 5).

## Owner critique (agents/user-critique.md)
1. Retro, matte, print-like: **met.** Flat fills, ink rules, double rule under header, hard shadow only on primary button, ink footer, faint grain, no gradient or blur in any screenshot I viewed. Dark mode is coherent. Gap: it is "warm editorial", not "retro print object" (see 8).
2. Not AI-looking: **mostly met**. The residual tell is the absence of a human and any imagery, not the layout. Further CSS tinkering will not move this; real media and 1-2 first-person specifics will.

## Findings, ranked

**1. Major (Looks good / UX). Project pages are bare and visually dead.** snake-robots phone: after a good tl;dr, two fact rows (Lab, Advisor) and one generic paragraph about snake robots (not about his work), there is nothing: no figure, no result, no method. A recruiter opening the lead project (row 01) finds the least content on the site. Source of concern: hiring managers look for the process and outcome of a project, not a description of the field (uxdesign.cc piece above; applies equally to engineering). Designer: if a page has no media and under ~120 words of specifics, reorder so the tl;dr and the facts carry it and drop the generic field paragraph below a "Background" label, or fold it. Owner: supply 2-3 sentences of "what I did and what happened" and one image per project.

**2. Major (Looks good / AI-tell / UX). Zero images that load.** Home text-only; About portrait slot depends on Wix; every figure depends on Wix. A robotics portfolio is judged on seeing the robot. Owner: supply a media folder (originals, true dimensions). This remains the single highest-value item.

**3. Major (UX / credibility). Status and dates stale.** Today is 2026-10-23; About says "I'm pursuing a Master's", "2023 - 2025"; home says "I research". `STATUS` in build is still empty (`STATUS = ""`). A recruiter cannot tell whether he has graduated or is available. Owner must supply one line; designer must not invent. Until then, "MS Mechanical Engineering, Carnegie Mellon University" under the h1 should not carry a tense that may be wrong.

**4. Major (Fun / personality). Still only typographic.** Grounded ideas, no invented facts: (a) Hasselhoff page: lay out "99 seconds" as a printed ticket with a punched edge in CSS only, static; (b) the About timeline already contains "3 weeks to 15 minutes": give that line the same struck-through marker treatment as the home page so the motif recurs; (c) 404 joke reused as the title of the footer colophon only if it is short. Trade-off: static and reduced-motion safe; no decorative motion.

**5. Major (SEO / performance / robustness). All media and the resume are Wix hotlinks, with no dimensions.** Resume link rot is the worst failure on a job page; no width/height means layout shift when images load (CLS). Designer cannot download. Designer can: set `fetchpriority="high"` on nothing (no hero), keep `loading=lazy`; add `aspect-ratio` only when dimensions are known. Owner: files into `assets/`.

**6. Minor (SEO). Home h1 is only the person's name.** The descriptive phrase ("MS Mechanical Engineering, CMU") is a mono subtitle, not in the h1 or the first heading text; the descriptive text sits in the meta description only. Consider h1 "Karthik Karumanchi" plus a visible line naming "robotics and controls" (the lede does, fine), so mostly Nit unless you want the h1 to include the role. Taste.

**7. Minor (UX). Index rows: tag column floats at the far right on desktop** (index-desktop-light): blurbs run to ~920px and the 150px tag column sits ~100px further right, with index numbers aligned to the title. At 1366px the eye has to jump across a gap to find "01". Tighten: put number before the title (left gutter) and tags under the blurb, as on phone, where it reads better. Taste, low risk.

**8. Minor (AI-tell / retro, taste). Retro is palette and rules, not object.** Ideas inside the repo's palette: a registration-mark or a "Plate 01" caption style on figures, a printer's ornament (a plain rule with a small centered glyph) between About sections, mono page numbers in the footer. Keep contrast and no motion.

**9. Minor (UX). No "start here".** Row 01 is the default, but weak (see 1). Owner to choose; a "Start here" tag on one row is cheap.

**10. Minor (Accessibility). Dark theme: About bullets and prose line length.** About intro measure is fine (about 68ch). Muted dark text is now fine in checks. Not reopening, but verify text-spacing override (WCAG 1.4.12) with the user-style test; I did not test it and cannot verify offline.

**11. Minor (Content). About says "I'm also taking courses in robot learning and AI"** next to "Courses" in Education that list Advanced Control Systems Integration and Intro to Robot Learning: redundant, and tense again stale. Cut one.

**12. Nit (SEO). Google Fonts third-party** and swap shift on the h1. Self-host WOFF2 (owner/dev machine) with a `size-adjust` fallback.

**13. Nit (SEO). robots.txt on a project path is ignored.** Owner: submit sitemap.xml in Search Console. Do not reopen.

## Good, must not regress
- Ruled index with numbered rows and the hairline / heavy / double rule vocabulary; varied stamps.
- Struck-through "three weeks" in the amber marker; "For the record" ledger.
- tl;dr-first project pages; pager with one-line neighbour summaries.
- Ink footer band; dark theme as inverted print; one primary button only.
- Figures and portrait that collapse cleanly when the image fails; skip link; 44px targets.
- Plain, specific copy (no "I build X that Y" slogans); the 99-second 404.

## Verdict
The site no longer looks generated: it has a consistent printed-index voice, accurate specific copy and clean semantics, and automated checks are all green. What holds it at 6 on every axis is not styling but substance: no image loads, status and dates are stale, and the lead project pages say less than the home page does. The designer has run out of work that can be done without owner input; the next gain requires Karthik's media, one status line, and two or three sentences of outcomes per project. In the meantime the most useful designer moves are to make thin project pages lead with specifics, repeat the struck-through motif on About, and tidy the desktop row layout.
