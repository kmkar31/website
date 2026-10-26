# Critique, 2026-10-26 (cycle 24, reviewing main at 5b0f017 "Cycle 23")

## Sources
WebFetch was refused again (PROVENANCE_REQUIRED, permission not answered) for https://www.nngroup.com/articles/mobile-ux/. WebSearch returned only result lists. Nothing below rests on a page I could read. Pointers only, unverified:
- NN/G, 5 Steps to Creating a UX-Design Portfolio: https://www.nngroup.com/articles/ux-design-portfolios/ (search result only)
- NN/G, UX Portfolios: What Hiring Managers Look For: https://www.nngroup.com/videos/ux-portfolios-hiring/ (search result only)
- NN/G, mobile UX: https://www.nngroup.com/articles/mobile-ux/ (blocked)
Topic this cycle: portfolio content strategy for a 30-second reader (recruiter or professor), freshness and credibility.

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes. Every line is OK (no overflow, tap, contrast, alt or h1 failures; "images not loaded" is the sandbox). Screenshots viewed: home phone and desktop (light), snake-robots tablet (dark), raftar phone (light). Repo read: critic/LOG/user-critique, grep of titles, og tags, robots, hotlink counts. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradients, glass, glow, stats strip or card trio. Plain first-person lede with real numbers; plates and four quantity stamps are specific to him. Residual: cream paper + serif + terracotta + mono labels is a familiar "editorial" kit. Moved: nothing this cycle (cycle 23 only fixed a label).
- Looks good: 7/10. Home desktop and phone are well ordered: rules, one hard-shadow button, ruled index, dark footer band. Held back by no photographs anywhere (images blocked here, but the repo has none local), by the snake page being a large drawing plus one sentence, and by About's empty right third (taste).
- SEO: 7/10. Unique titles and descriptions, canonical, OG/Twitter with absolute og.png, JSON-LD, sitemap, 404 present. Open: placeholder alt text, no width/height on images, Google Fonts without a size-adjusted fallback. robots.txt in a /website/ subpath is not read by crawlers (host root only); harmless, cannot verify live.
- UX: 6/10. Within one phone screen: name, school, lab, advisor, the Seagate result, Resume and LinkedIn. Weak: no current status or date, LinkedIn is the only contact route, Resume is a Wix hotlink, phone header has no Resume link (it is in hero and footer).
- Fun and personality: 6/10. Struck-through "three weeks", 99 s stamp, 404 joke, Sheet N of 9 plates are real and earned. Most project pages outside those are neutral. Same score as last cycle; ideas are blocked on owner facts.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, hard shadow on one button, no blur or gradient, inverted-print dark theme (checked snake-robots tablet dark: legible, coherent).
- Not AI-looking: met at 3/10; see the AI-tell score. No generic-template tell is present.

## Findings (ranked)

1. Major (credibility, owner-only). Still no current status or date. `STATUS = ""` in build/build.py. About says the Master's is "2023 - 2025" and the home lede and hero sub-line are present tense ("I research", "MS Mechanical Engineering, Carnegie Mellon University"). Today is October 2026. A recruiter cannot tell whether he has graduated, is employed or is looking. Hiring-manager guidance generally asks portfolios to say what the person wants next (NN/G pointers above, unread). Needs: one sentence from the owner plus the tense of "is at". Not repeating the designer's reason for declining; it is sound, but the page remains the single largest UX gap.

2. Major (first impression of his actual work). "Start here" (snake-robots) is still the thinnest project page: tl;dr, question, lab/advisor strip, schematic whose caption says the module count is illustrative, one sentence on "why", and a link out. It is the first row on home and the only row with a plate. Seen at tablet dark this cycle: the plate takes most of the screen and the body is one sentence. Either the owner supplies what he implemented and what happened, or "Start here" moves to Aerobraking (46 orbits) or Hasselhoff (99 s, 4 thrusters). Owner decision.

3. Major (robustness, owner/environment). Every project page and Resume depend on Wix hotlinks (about 3 to 9 per page; 404.html also carries 2, which is the Resume link). If the Wix site changes, photos and Resume go with it, and a dead Resume link sits in the header, hero and footer of every page. No width/height on the images, so layout shift on load (standard CLS advice; web.dev page not read, unverified). Needs the owner's files; nothing designer-side remains except a reminder.

4. Major (axis at the line: UX/content). Project pages carry almost no "what I did, what I learned, what I would change" beyond one-liners; only Aerobraking, Landing and Hasselhoff have numbers. A professor or recruiter who opens Raftar (seen on phone) gets a team-size line, a sketch, two paragraphs of team description and one link. The plate there is a generic open-wheel car, not his suspension or brakes, which is what he says he did. Owner facts needed (one sentence of what he designed, one number). Do not invent them.

5. Minor (designer can act). Raftar's pager facts differ in kind: "Landing success: 100% (small pad, under 0.25 m/s)" vs "Thrusters: 4 BLDC". Fine, but the Landing fact has two conditions and is the more claim-like; check that the page body says the same thing and that "100%" is not read as a general claim. Wording is already carried in the repo; verify, do not rewrite.

6. Minor. Alt text on Wix figures is placeholder-pattern ("ARGUS nanosatellite mission figure"). WCAG 1.1.1 asks for an equivalent; owner must say what each image shows.

7. Minor. Fonts: two Google families with display=swap and no size-adjusted fallback; in the check run the h1 uses a different fallback serif, so a swap will reflow the h1 and lede (CLS risk, unverified offline). Needs WOFF2 files.

8. Minor (taste). About desktop leaves roughly the right third empty for the whole page; the portrait slot is documented but empty. Accept it and say so in the log, or put the "For the record" ledger from the home page in that column.

9. Minor. Contact is LinkedIn only (owner constraint). Conversion risk for readers without LinkedIn; not a defect.

10. Nit. "START HERE" is a small mono underlined label under the bold "01"; easy to miss on phone. Contrast passes.

11. Nit. Footer text "Set in DM Serif Display and Source Serif 4. Hand-built static pages, one stylesheet, no framework." is a good honest touch; keep. But "To get in touch, message me on LinkedIn." plus three links below repeats LinkedIn twice in the same band; harmless.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rule under header and above footer, hard shadow on one button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, four quantity stamps (46 orbits, 99 s, 500 m, podium) and the About echo, Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; per-project blurbs that state the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox, no nameless Tab stops, row link name equals title, 44 px targets, reduced-motion handling.
- SEO base: titles, descriptions, canonical, OG/Twitter, JSON-LD, sitemap, noindex 404.
- Failed images collapse cleanly; pager has no wraparound; cycle 23's quadrotor plate label fix (not re-viewed this cycle).

## Verdict
The design is coherent, retro without being costume, and does not read as generated. Cycle 23's label fix closed the last visible defect, and I found no new regression in the automated run or the four screens I viewed. What limits the site now is substance only the owner can supply: a current status sentence and tense check (it is October 2026 and the page says 2023 - 2025), local images and a local Resume, and real outcomes for the "Start here" snake page and the Raftar page (what he designed). Without those, further designer cycles will mostly be polish. Sources could not be read this cycle; no finding depends on them.
