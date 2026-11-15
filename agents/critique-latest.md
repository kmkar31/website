# Critique, 2026-11-15 (cycle 140)

Method: `python3 tools/check.py . agents/shots` finished rc=0, 0 FAIL (only "images not loaded, sandbox network" notes). No site files edited. HEAD is ce45603 (Raftar caption de-duplication). I viewed 4 of 78 screenshots, chosen to differ from last cycle where possible: raftar-formula-racing phone-light (re-checked because cycle 139 changed it), tethered-nanosatellite phone-dark, projects tablet-light, index tablet-dark. The other 74 were not opened. Cycle 139's Raftar change IS reviewed this time.

## Sources consulted (honest status)
- The three-source rule is NOT met, again. WebFetch of https://web.dev/articles/optimize-cls and https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ were both blocked (permission request unanswered, "do not retry"). I read no page content from either.
- No WebSearch was run this cycle. No finding below quotes or relies on an external source; each rests on the repo files or on the screenshots I viewed. Pointers only, unread: web.dev CLS guide (image dimensions, font loading), NN/g on scanning.

## Scores
- AI-tell: 2/10, unchanged. Specific facts (struck "three weeks" on amber, stamps with real values, "Sheet n of 9" plates), plain first-person copy, no gradient, blur or glow, honest footer. Residual tells: the "For the record" label, the three-item sidebar lists ("Seagate, York University, Tube Investments"), and the new pull-out device (finding 5). Nothing moved down.
- Looks good: 8/10, unchanged. The Projects page at tablet is the best single screen: stamps, index numbers and the hard-shadow filter buttons read as one printed system. Weak spots: the Raftar plate (the cockpit trapezoid floats above the body like a lamp, not a halo or cockpit; taste) and the tethered page's wall of text.
- SEO: 7/10, unchanged. Unique titles, canonical, og tags, JSON-LD, sitemap present. Held down by 96 `wixstatic` references (counted by grep), one og card, subpath robots/sitemap, and lastmod (finding 9).
- UX: 6/10, unchanged. A phone visitor gets name, focus, Resume, LinkedIn quickly, but still no status or year on the home line, and one contact route.
- Fun and personality: 7/10, unchanged.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met in all four screenshots viewed (paper, grain, double rules, hard shadows, inverted-print dark mode).
2. Must not look AI-generated: met. No new owner notes.

## Ranked findings
1. Major (UX, credibility). No status. Home (tablet-dark viewed) reads "MS Mechanical Engineering, Carnegie Mellon University" with no years; About says 2023 to 2025; today is 2026-11-15. `STATUS = ""` at `build/build.py` line 264 (verified). A recruiter cannot tell student, graduate or available. Owner supplies one line. Unchanged for many cycles.
2. Major (credibility). Tense split follows from 1: Home "I research compliant control of snake robots" (present) against About's past-tense date range.
3. Major (UX). Two answers to "strongest project". The lede names snake robots and row 01 is snake, but "Start here" and the plate sit on row 06 (aerobraking), seen on index tablet-dark. A reader who follows the explicit pointer lands on a different project than the one the lede sells. Owner decides.
4. Major (credibility). Aerobraking page does not separate Karthik's contribution from the cited prior work. Owner fact.
5. Major (regression from cycles 138/139, designer-fixable). Repetition has moved, not gone.
   a. Raftar (phone-light, viewed): the claim "I captained the team and did the suspension and brakes" now appears in the tl;dr (line 47), and again in the new body paragraph "My part was modeling, designing and manufacturing the suspension and brakes ... I captained the team to a podium finish" (line 56); the "Result: Podium, Formula Bharat 2023" row restates the podium a third time, and the home row blurb a fourth. Cycle 139 removed it from the caption only to add it to the body. The new paragraph adds "modeling, designing and manufacturing" and "first electric racecar", which are real, but the rest is a copy of the tl;dr. Fix: cut the tl;dr to the team and the car, and let the body carry the personal part once.
   b. Tethered (phone-dark, viewed): the cycle 138 pull-out "98% of space debris is shrapnel no larger than 1 cm" sits directly under the paragraph that says exactly that ("Shrapnel ... no larger than 1 cm and accounts for 98%"). It is aria-hidden for that reason, but sighted readers read it twice within one screen. It also pulls emphasis to a textbook fact about debris, not to what he built, and the page still has three dense paragraphs after it with no result stated. Fix: move the pull-out so it replaces the sentence in the paragraph, or use a number that is about the project (500 m tether, 3U + 1U) and is not already in the fact strip.
6. Major (credibility). `raftar-formula-racing.html`: "one-fifth the weight of a Ferrari but matches its 0-60" is the only framing question on the page and has no figure or source. Cite or cut. Owner fact.
7. Major (robustness, performance). 96 Wix hotlinks; the Resume PDF (header, home, footer) is a `filesusr.com` URL; Google Fonts with no local fallback. Needs owner files; cannot verify dimensions offline.
8. Minor (UX). LinkedIn is the only contact route, in every footer. Owner constraint; the About page could at least say so in a line so a professor without LinkedIn knows it is deliberate.
9. Minor (SEO, accuracy). All 12 sitemap entries carry `lastmod` 2026-11-02 while pages changed on 11-14 and 11-15 (git log). A uniform and stale lastmod is ignored or distrusted by crawlers. Designer-fixable if build.py derives it per file from git, or drop `lastmod`; honest absence beats a wrong date. Verify only offline.
10. Minor (UX). Projects page: five of nine rows (01, 02, 03, 08, 09) have no stamp, and there is no tier or "Start here" mark, so nine near-equal rows. Owner picks three.
11. Minor (content). Tethered and ARGUS state aims and method but no outcome. If there is none, say "design and simulation; not flown" only if that is true. Owner fact.
12. Nit (looks). Raftar plate: floating trapezoid; the dashed ground line runs under the whole car including the front wing, reading as a track marker. Taste.

Designer-fixable without inventing facts: 5a, 5b, 9. Everything else needs the owner.

## Good, must not regress
- Retro matte system: paper, grain, double rules, hard-shadow buttons, inverted-print dark mode (index tablet-dark is legible, accent used sparingly).
- Struck-through "three weeks" on amber, stamps with real values, boxed "podium finish" on About.
- Fig. 1 plates with "Sheet n of 9 . NTS" captions; honest "Not to scale" notes.
- Pager showing the neighbour's first fact; no wraparound at ends.
- Projects filter chips (hidden without JS); one h1, unique titles, JSON-LD, canonical, skip link, 44 px phone targets.
- Plain first-person lede; honest colophon; 404 joke.

## Verdict
Still authored, coherent and not generic, and the last two cycles introduced no layout or contrast regression in the screens I viewed. The designer's recent "fixes" for thin pages have started to add repetition: the Raftar claim now appears four times, and the tethered pull-out repeats the sentence above it. Those, plus a stale uniform sitemap lastmod, are the only items the designer can fix honestly. The rest is the same owner list: status line, aerobraking contribution, one answer to "best project", a sourced or cut Ferrari claim, and local Resume, images and fonts. Caveats: external sources were unreadable again and only 4 of 78 screenshots were inspected.
