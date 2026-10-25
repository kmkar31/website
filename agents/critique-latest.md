# Critique, 2026-10-25 (cycle 16, reviewing commit 5dd7e20 "Cycle 15")

## Sources
WebFetch was refused by the permission layer (w3.org focus-appearance page, blocked, not retried) and I have no search tool, so I read NO source this cycle. Pointers below are from memory and UNVERIFIED; no finding depends on them.
- WCAG 2.2 SC 2.4.7 / 2.4.11 / 2.4.13 focus: https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (blocked)
- Nielsen Norman Group on portfolios and proof of results (recruiters scan for outcomes): https://www.nngroup.com/ (unverified)
- web.dev font best practices: https://web.dev/articles/font-best-practices
Topic this cycle: proof/outcome content on the featured project, and staleness. Earlier cycles covered fonts, contrast, tap targets, SEO basics, disclosure widgets.

Measured: `git log -1` = 5dd7e20 (Cycle 15). `tools/check.py . agents/shots` ran 13 pages x 3 viewports x 2 themes, every page OK (Wix images "not loaded" is the sandbox). Repo: `STATUS = ""` (build/build.py:253). Wix/filesusr hotlinks on every page (2 to 9 each; 404 has 2). Fonts still from the Google Fonts stylesheet. Aerobraking page has 3 `width=` matches, but its Wix `<img>` tags have none. sitemap 12 URLs, robots.txt names the sitemap, 1 JSON-LD block on home. Live site not checked (proxy). Viewed: home phone and desktop (light), Hasselhoff phone (light), About desktop (dark), Snake robots phone (light). Screenshots use fallback serif because Google Fonts is blocked in the sandbox; typography judged with that caveat.

## Scores
- AI-tell: 3/10 (unchanged). Moved: the Start-here plate now has a caption strip "Fig. 1 . Snake robot, schematic" (good, it reads as a figure). Not moved: cream paper + serif + terracotta + mono label kit; rows 02 to 09 identical. Authored and specific: struck-through "three weeks", 99 s stamp, Fig./Sheet N of 9 plates, pin-puller line, "no framework" colophon.
- Looks good: 6/10. Home is calm and aligned. Still no photograph; project pages are plate then prose; Snake robots page (the page the home calls "Start here") is almost bare. The Hasselhoff disclosure bar is now clearly a control (boxed +, "Show"): fixed, and it works.
- SEO: 7/10. Titles, descriptions, canonical, OG, JSON-LD, sitemap, noindex 404 in place. Weak: render-blocking Google Fonts CSS, hotlinked media with no dimensions, text-only og.png, JSON-LD only on home (I found one block in index.html; per-project CreativeWork not verified for all pages).
- UX: 6/10. Name, field, resume, LinkedIn on the first phone screen. Misses: stale-looking dates, third-party resume URL, LinkedIn-only contact, and the featured project has no result to read.
- Fun and personality: 6/10. Plates, stamps, press-to-count 99 s stamp, 404 are earned. Seven of nine pages have no moment of their own.

## Owner critique (user-critique.md)
1. Retro, matte: met. No blur, glow or gradient; hard-offset button; ink rules. Dark theme is near-black plus amber rather than paper; taste.
2. Not AI-looking: mostly met; residual risk is the kit and the uniform rows (finding 6).

## Findings (ranked)

1. Major (content/UX). The featured project is the thinnest page. Snake robots is "Start here" on home and the lede's research focus, but its page (phone) is: lab and advisor facts, a schematic zigzag, and one paragraph of generic "why snake robots". There is no result, no method sentence, no video, no repo, nothing Karthik did. Home promises "gait-based controllers I implemented"; the page never says which gaits, what was measured, or what happened. A recruiter who follows the one path we point them to hits a dead end after about 1.5 screens. Fix: owner supplies two or three facts (which gaits, what terrain/test, result, status) or a figure/video; designer must not invent. Until then, either demote "Start here" to a project with a real outcome (Aerobraking: 46 orbits, ARGUS, or Sysid) or add a visible "work in progress" honesty line. Judgment call on the demotion; it is an editorial ranking the designer has said belongs to the owner.

2. Major (UX/credibility). No statement of what Karthik is doing now; dates look stale. About says the Master's "is at Carnegie Mellon University (2023 - 2025)"; today is 25 Oct 2026. Reader cannot tell graduated, enrolled or open to roles. STATUS slot is empty. Owner needs one sentence. Highest-value content gap; open since cycle 1.

3. Major (robustness). Resume PDF, the main CTA, is a hotlink to a Wix filesusr URL in the header, hero, About and every footer (13 pages). One rotation breaks it everywhere, silently. Owner drops resume.pdf into assets/. Not verifiable offline.

4. Major (looks good, score 6). No photograph or real result image anywhere; Wix figures drop out on failure, so most project pages read as plate plus prose. A robotics portfolio is expected to show the robot. Needs owner media in assets/ with real width and height.

5. Major (performance/SEO). Google Fonts stylesheet is render-blocking and third-party; no fallback metrics. Self-host two WOFF2 with font-display: swap and preload. Needs owner files; sandbox cannot fetch.

6. Major (AI-tell: kit). Rows 02 to 09 are identical in anatomy, and now only row 01 has a plate, which reads as a "featured card" (template pattern). Either give every row its plate thumbnail at the right edge on desktop (local, cannot fail) or accept uneven rows deliberately. The designer's cycle-15 reasoning (uniform in a new way, longer phone home) is fair for phone; propose plates on desktop/tablet only. Taste.

7. Minor (UX). Hasselhoff page: the bar "Design and state machine / Show" is good now, but the hidden content (Design Methodology, State Machine Logic) is the page's only engineering substance; hiding it by default means the page's visible text is a UX narrative and a "not yet tested in a large body of water" caveat. Consider whether a recruiter wants that behind a click; the first sentence of the hidden content could sit above the fold of the details. Taste.

8. Minor (content). Education/About carry "GPA: 4.0 / 4.0" for a degree dated through 2025; consistent with finding 2. Also "Pin-puller for a 3U CubeSat, 2022" on home is under "Built" while About says "Implemented"; fine. No action beyond finding 2.

9. Minor (layout). About desktop: right column holds only the "On this page" box; from Skills down (about 2000 px) the right 28% is empty in both themes. Reads as a plain CV. Dates in a left margin column on desktop would use width. Declined as large rewrite; the void is real. Taste.

10. Minor (UX). Home and Projects list the same nine rows. Clicking "See the projects" lands on a near copy. Judgment call: home could show Start-here plus stamped rows and link "All nine projects". Phone home is about 6100 px tall (measured from screenshot).

11. Minor (UX). Contact is LinkedIn only (owner constraint, flagged only). On phone, footer "To get in touch, message me on LinkedIn" is the only contact sentence.

12. Minor (SEO). og.png is text only; a plate would make a more distinctive share card and is repo-local. Cannot verify previews offline.

13. Minor (CLS risk). Wix `<img>` tags have no width/height (verified in aerobraking-drl.html), so late-loading figures shift layout. Cannot measure offline; needs dimensions from owner files.

14. Nit (a11y). Hasselhoff stamp keyboard support was added; I did not drive it with a keyboard in this run (screenshots only). The designer states focus ring and blur-stop are in place; verify with a real tab-through before closing.

15. Nit (fun). Seven of nine project pages have no moment beyond plate and stamp. Facts already in repo that could carry one: Aerobraking "target reached in 46 orbits / terminal error 8.4 km", Tricycle "target speed 12 km/h", Tethered "500 m". A single plain aside per page, only where the page already states the fact. Designer has declined as taste; acceptable unless owner asks.

## Good, do not regress
- Struck-through "three weeks" in marker highlight (home, About).
- Fig. N plates with sheet tags, honest "schematic / NTS" captions; repo-local and robust.
- Start-here plate now captioned "Fig. 1 . Snake robot, schematic".
- Two stamp types only; pressable 99 s stamp.
- Hasselhoff disclosure: boxed +, serif label, "Show" word, native details.
- Plain lede, no slogans; "For the record" ledger; footer "no framework" line.
- Phone first screen: name, field, resume, LinkedIn without scrolling.

## Verdict
Design hygiene is now close to saturated: the checks pass, the retro/matte direction is coherent, the AI-tell score is low, and the cycle-15 disclosure fix landed. What is left is content, not layout. The strongest remaining defect is that the one project the site tells a visitor to start with has almost nothing on it, followed by the unanswered "what is he doing now" question in a year-old date range, a third-party resume link, and zero photographs. All of these need owner input (facts, files, media); further cosmetic cycles will yield little. Recommended owner-facing ask: one status sentence, resume.pdf, two or three real facts or a result for the snake-robot page, and one photo per project.
