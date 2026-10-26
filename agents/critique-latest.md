# Critique, 2026-10-26 (cycle 25, reviewing main at 1e7d912 "Cycle 24")

## Sources
WebFetch of https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html was refused (PROVENANCE_REQUIRED, permission unanswered). WebSearch returned only result lists, no readable pages. Nothing below rests on a page I read. Pointers only, unverified:
- web.dev, Optimize Cumulative Layout Shift: https://web.dev/optimize-cls/ (search result only)
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
- NN/G portfolio guidance, carried over from last cycle: https://www.nngroup.com/articles/ux-design-portfolios/ (unread)
Topic this cycle: layout stability (CLS) and image/font loading, plus a visual pass of home and About.

Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes: every line OK (only "images not loaded", the sandbox). Screenshots viewed: home phone light, home desktop dark, About tablet light. Repo grep: title, canonical, og tags, robots, Wix hotlink counts, STATUS. Live site not checked.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stats strip or card trio. Plain lede with real numbers; strike-through "three weeks", stamps and Fig. plates are specific to him. Residual: cream paper + serif + terracotta + mono labels is a familiar "editorial" kit. Tells moved since last cycle: none (cycle 24 changed nothing visible).
- Looks good: 7/10. Home desktop dark is well ordered: rules, one hard-shadow button, ruled index, stamps at right, inverted-print dark band. Phone home is a long single column but rhythmic. Held back by zero photographs (repo has none local), and the snake plate being the only image on home so row 01 is visually 3x heavier than the rest.
- SEO: 7/10. Unique title/description, canonical, OG with absolute 1200x630 og.png and alt, JSON-LD, sitemap, noindex 404. Open: placeholder alt on Wix figures, no width/height on images, Google Fonts without size-adjusted fallback. robots.txt under /website/ is not read by crawlers (host root only); harmless.
- UX: 6/10. Phone first screen answers who, where, lab, advisor, the Seagate result, Resume and LinkedIn. Weak: no status or date (STATUS = "" still, build.py:257), LinkedIn is the only contact route, Resume is a Wix hotlink.
- Fun and personality: 6/10. Struck-through "three weeks", 99 s stamp, 404 joke, Sheet N of 9 plates are earned. Rest of the project pages are neutral. Ideas are blocked on owner facts.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, hard shadow on one button, no blur or gradient, dark theme reads as inverted print (checked home desktop dark: legible, coherent).
- Not AI-looking: met at 3/10. No generic-template tell is present.

## Findings (ranked)

1. Major (credibility, owner-only). No current status or date. About says "2023 - 2025" and the lede is present tense ("I research"); today is October 2026. A recruiter cannot tell whether he has graduated or is looking. Needs one owner sentence and the tense of "is at". Still the largest UX gap. Not a designer-fixable item; the designer's reason for declining is sound.

2. Major (first impression of his work). "Start here" (snake-robots) is the thinnest project page yet is row 01 and the only row with a plate. Owner either supplies what he implemented and what happened, or moves "Start here" to Aerobraking (46 orbits) or Hasselhoff (99 s, 4 thrusters). Owner decision.

3. Major (robustness). Project pages and Resume depend on Wix hotlinks (counts per page: aerobraking 7, sysid 5, tricycle 4, hasselhoff 4, nanosat 4, landing 2, others 1; index has 0 but links Resume). Dead Resume link would sit in header, hero and footer of every page. No width/height on images, so layout shift when they load (standard CLS advice, web.dev pointer unread). Needs owner files.

4. Major (content). Project pages carry few "what I did / learned / would change" beyond one-liners; only Aerobraking, Landing and Hasselhoff have numbers. Raftar's plate is a generic open-wheel car, not his suspension or brakes, which is what he claims. Owner facts needed; do not invent.

5. Minor (designer can act, new). About, tablet and phone: the boxed "podium finish at Formula Bharat 2023" mark is an inline-block that breaks onto its own line, leaving the sentence ending "...led the team to a" then the box, then a stranded "." (visible in the About tablet shot). Fix: let the mark wrap with `white-space: normal` / `box-decoration-break: clone`, or keep the final period inside the mark, or rephrase so the mark sits mid-sentence. Taste-adjacent but a visible typographic blemish on a page recruiters read.

6. Minor. Home row 04 stamp "Podium, Formula Bharat 2023" repeats the lede sentence directly above it on desktop (lede: "finished on the podium at Formula Bharat 2023"). Same fact twice within one screen. Consider leaving the stamp for a number that is not already stated (e.g. team size 40+) only if the owner confirms it; otherwise accept.

7. Minor. Alt text on Wix figures is placeholder-pattern ("ARGUS nanosatellite mission figure"). WCAG 1.1.1 wants an equivalent; owner must say what each image shows.

8. Minor. Fonts: two Google families, display=swap, no size-adjusted fallback; the h1 and lede will reflow on swap (CLS risk, unverified offline). Needs WOFF2 files for real metrics.

9. Minor (taste). About desktop leaves the right third empty; the portrait slot is documented but unused. Accept and say so, or move the home "For the record" ledger there.

10. Minor. Contact is LinkedIn only (owner constraint). Conversion risk for readers without LinkedIn; not a defect.

11. Nit. "START HERE" is a small mono underlined label under bold "01"; easy to miss on phone. Contrast passes.

12. Nit. Footer says "message me on LinkedIn" and then lists LinkedIn again beside it; harmless.

## Good, must not regress
- Retro matte system: paper tones, ink rules, double rule under header and above footer, one hard-shadow button, no blur or gradient, inverted-print dark theme.
- Authored specifics: struck-through "three weeks", "For the record" ledger, quantity stamps (46 orbits, 99 s, 500 m, podium), Fig./Sheet N of 9 plates, 404 joke, honest colophon.
- Plain lede with real facts; full project names as titles; per-project blurbs that state the specific thing done.
- Accessibility: skip link, aria-pressed filters, modal lightbox, no nameless Tab stops, row link name equals title, 44 px targets, reduced-motion handling.
- SEO base: titles, descriptions, canonical, OG/Twitter, JSON-LD, sitemap, noindex 404.
- Failed images collapse cleanly; pager has no wraparound; quadrotor plate label fix.

## Verdict
The design is coherent, retro without being costume, and does not read as generated; the automated run is clean and I found no regression from cycle 24. The one new, designer-fixable defect is the boxed podium mark on About stranding its full stop on phone and tablet. Everything else that limits the site is substance only the owner can supply: a current status sentence (it is October 2026 and the page says 2023 - 2025), local images and a local Resume, and real outcomes for the "Start here" snake page and Raftar. Without those, further designer cycles are mostly polish. Sources could not be read this cycle; no finding depends on them.
