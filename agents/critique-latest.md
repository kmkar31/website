# Critique, 2026-10-26 (cycle 23, reviewing main at 055afe6 "Cycle 22")

## Sources
WebFetch was refused again (PROVENANCE_REQUIRED, permission not answered) for both primary pages tried; WebSearch returned only secondary pages. Nothing below rests on a source I could read. Treat all as unverified pointers:
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
- web.dev, Optimize CLS (image dimensions, web fonts): https://web.dev/articles/optimize-cls (blocked)
- WCAG 2.2 SC 1.1.1 Non-text Content (alt text): https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html (not fetched)
- Secondary, from search only: https://allaccessible.org/blog/wcag-258-target-size-minimum-implementation-guide
Topic this cycle: SVG plate legibility (a regression check on the Fig. 1 plates), About page credibility/freshness, hotlink dependency.

Measured: `python3 tools/check.py . agents/shots` (13 pages x 3 viewports x 2 themes). It was still running dark/desktop when I wrote this; every line up to that point was OK (no overflow, tap, contrast, alt or h1 failures; "images not loaded" notes are the sandbox blocking Wix). Screenshots viewed: home desktop and phone (light), About desktop (light), quadrotor-landing phone (light, plus a 2x crop of the plate). Repo read: index, about, snake-robots, argus-mission, robots.txt, sitemap. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). The two label-only stamps were removed, which was right: four stamps with quantities (podium, 99 s, 46 orbits, 500 m) now read as a handful of marks, not a template. The About podium box is the same double-border mark and is a good small echo. Residual: cream paper + serif + terracotta is the current "editorial warm" kit; the plate/stamp set is the thing that makes it Karthik's. Moved this cycle: stamp sameness down.
- Looks good: 7/10. Rhythm, rules, type pairing and the footer band are coherent. Held back by text-only pages (no photograph visible anywhere) and one newly seen defect, the label collision in the quadrotor plate (finding 2). About desktop: the right third below the intro is empty for the whole page (taste).
- SEO: 7/10. Per-page title and description, one h1, canonical, OG/Twitter with absolute og.png, Person and CreativeWork JSON-LD, sitemap, robots.txt, 404 all present. Open: generic alt text on figures, no image width/height, Google Fonts without a size-adjusted fallback; the repo robots.txt sits under /website/ on a project site, so crawlers will not read it (host-root robots only) - harmless, cannot verify live.
- UX: 6/10. Name, field, strongest lines and Resume are visible on phone within one screen. Weak spots are unchanged: no current status or date, one contact route, resume is a Wix hotlink, and phone header drops Resume (it is in the hero and footer).
- Fun and personality: 6/10 to 7/10. Struck-through "three weeks", 99 s stamp, 404 "failed to land on the target", Fig./Sheet N of 9 plates are real. Outside those, About and most project pages are neutral. Borderline; kept as a Major only because it stays tied to owner-only content (finding 4).

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like, no glossy gradients: met. Flat paper, ink rules, one hard-shadow button, grain at most, inverted-print dark. Contrast and 44 px targets pass in check.py, so retro is not costume.
- Must not look AI-generated: met at 3/10. The generic-layout tells (stats strip, three cards, gradient, glass, glow, sparkle, floating chips, slogan copy) are all absent.

## Findings (ranked)

1. Major (credibility). Status and dates are stale or absent. About: "My Master's ... is at Carnegie Mellon University (2023 - 2025)" and the timeline says 2023 - 2025; home lede says "I research compliant control of snake robots" in present tense. Today is October 2026, `STATUS` in build/build.py is still empty. A recruiter cannot tell whether he has graduated, is employed or is looking, and a past-dated "is at" reads as an unmaintained page. Owner-only fact; designer cannot fix. Smallest honest change: owner gives one sentence for STATUS and says whether "is at" should be "was at". Taste/judgment: tense in the lede is also a risk (the facts are possibly in the past).

2. Major (regression-class defect, designer can fix). Quadrotor Landing Fig. 1, phone 390 wide: the labels "origin" and "r = 0.8 m" overprint each other ("origin" runs into "r") and the radius label sits on the dashed circle. See agents/shots/quadrotor-landing-phone-light.png (crop around the plate bottom). In the SVG the texts are at x=206 and x=258, y=126 and y=122, about 52 units apart, which is less than the width of six mono characters once the SVG scales up on a narrow viewport. Screenshots here use fallback fonts (Google blocked), but the mono face is a system stack, so expect similar on real phones. Why it matters: the plates are the site's one distinctive idea and a visible collision on a project page looks unfinished (taste plus measured overlap). Fix: move "origin" to the left of the dot (text-anchor:end, x about 196) and put "r = 0.8 m" below the bar at y about 146, or shrink to the same font-size across plates; then re-check the other plates at 390 px (I only viewed this one, so others are unverified).

3. Major. The "Start here" project is still the thinnest page (snake-robots): one-line tl;dr, a question, lab and advisor, a schematic whose caption says "Module count is illustrative", one "Why snake robots" sentence, three hotlinked figures and the pager. The home page sends everyone there first while aerobraking, ARGUS, landing and Hasselhoff have real numbers. Either the owner supplies what he did and what happened (preferred), or the label moves to Aerobraking (46 orbits). Owner decision; flagged again because it is the first impression of his actual work.

4. Major (axis at the line). Personality beyond the existing five touches. Without inventing facts: (a) the 99 s stamp is the only interactive joke; the Aerobraking "46 orbits" stamp could carry a one-line plain aside about what an orbit count means, only if the owner says it is okay; (b) pager entries on pages 04 to 07 could show the neighbour's stamp text instead of its first fact so the front-page marks recur; (c) the About Seagate bullet says "3 weeks" and the home lede says "three weeks"; keep both strikes but make them match (nit-level consistency, but it is the site's best gag). I am not proposing anything new that needs facts.

5. Major (robustness, owner/environment). Every project page and Resume depend on Wix hotlinks (static.wixstatic.com and filesusr.com; about 2 to 10 per page). If the Wix site is closed or reorganised, all photos and the resume vanish; figures already collapse gracefully, but the resume link would 404 with no fallback, in the header, hero and footer. No width/height on those images means layout shift while they load (standard CLS guidance; web.dev page was blocked, so unverified here). Fix needs the owner's files. Designer-side: nothing more until local images exist.

6. Minor. Alt text is a placeholder pattern ("Modular snake robot, figure 1 of 3", "ARGUS nanosatellite mission figure"). WCAG 1.1.1 asks for an equivalent purpose; captions mostly cover it where they exist, but the Wix figures have no caption in snake-robots or ARGUS. Owner must say what the images show.

7. Minor. Snake-robots and ARGUS phone pages are short with the pager as the only next step; ARGUS has no Previous/Next facts beyond one line each. Fine, but the end of snake-robots has nothing after the one sentence. Resolved when finding 3 is.

8. Minor. About desktop: the three-link "On this page" index ends after the intro, and Skills/Education/Experience then run in a 760 px column leaving about 30% of the width empty for roughly 1800 px of scroll. Documented as a portrait slot; with no portrait it looks unbalanced (taste). The designer declined a sticky index because it sits in the intro grid; an alternative that needs no layout rewrite is to leave it and accept it, but say so in the log.

9. Minor. Contact is LinkedIn only (owner constraint). A recruiter without LinkedIn has no route; state is fine but note it stays a conversion risk. Not a defect.

10. Minor. Fonts: two Google Fonts families, display=swap, no size-adjusted fallback; the home h1 in the screenshot uses a fallback serif that is visibly different from DM Serif Display, so a font swap will reflow the h1 and lede on first load (CLS risk, unverified offline). Needs real WOFF2 files.

11. Nit. "START HERE" is a 12 px mono underlined label next to the "01" index; easy to miss next to bold "01" on phone. Contrast passes. Hierarchy only.

12. Nit. Home phone: Resume and LinkedIn are text links below the primary button, at about the same weight as body links; at 390 px the row is fine and the 44 px height passes. No change needed; noted so it is not re-raised.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rules under the header and above the footer, hard shadow on one button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks" in marker, "For the record" ledger, four quantity stamps (46 orbits, 99 s, 500 m, podium) and the matching About mark, Fig./Sheet N of 9 plates drawn from facts on each page, 404 joke, honest colophon.
- Plain lede with real facts and no slogans; full project names as titles; per-project blurbs that state the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox with focus return, no nameless Tab stops, row link name equals project title, 44 px targets, reduced-motion handling.
- SEO base: titles, descriptions, canonical, OG/Twitter, JSON-LD, sitemap lastmod, noindex 404.
- Failed images collapse instead of leaving gaps or orphan captions; no wraparound pager.

## Verdict
The design holds up: it is coherent, retro without being a costume, and nothing on the site looks generated. Cycle 22's stamp trim worked. The one thing the designer can fix now is a real visual defect: the overlapping "origin" and "r = 0.8 m" labels in the quadrotor-landing plate on phone, and that plate family deserves a pass at 390 px. Everything else that limits the site is owner-supplied substance and has been the same for many cycles: a current status sentence and tense check (it is October 2026 and the page says the Master's runs 2023 to 2025), local images and a local resume instead of Wix hotlinks, and real outcomes for the "Start here" snake page. Sources this cycle could not be read; no finding depends on them.
