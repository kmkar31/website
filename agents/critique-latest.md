# Critique, 2026-11-08 (cycle 98)

Rendering: `python3 tools/check.py . <scratchpad>/shots` completed for all 13 pages x phone/tablet/desktop x light/dark; every line OK (only "images not loaded" sandbox notes). I viewed index phone light, index desktop dark and snake-robots phone light. Repo checks: `color-scheme` meta and two `theme-color` metas are now present in index.html (cycle 97 fix verified, toggle script updates both); Wix hotlinks remain on 11 of 13 pages (aerobraking-drl 7, sysid 5, tricycle 4, hasselhoff 4, nanosat 4). No site files edited. HEAD e66b6c1, no regression seen.

## Sources consulted
Research limit this cycle: WebFetch requests were blocked (permission not answered), so these primary pages were NOT read and I draw no new claims from them:
- https://web.dev/articles/optimize-cls (blocked)
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
- https://developers.google.com/search/docs/appearance/structured-data/profile-page (blocked)
Carried over from earlier cycles and already in LOG: web.dev color-scheme article, WCAG 2.5.8, web.dev CLS/size-adjust. This cycle's research is therefore thin; treat the SEO/CLS points below as repeated, not re-verified.

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, one hard-offset button, struck-through "three weeks" on amber, stamps, Fig./Sheet captions, plain first-person lede, honest "Module count is illustrative" caption. No gradients, blur, glow, card trio, stats strip or slogans. Residual: intro / ruled list / dark footer is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. Phone and desktop dark hold: steady ruled rhythm, dark reads as inverted print. Weak: row 06 is the only row with a plate (on phone it sits above the title and breaks list rhythm); snake-robots page (the lede project) is thin: one schematic, one paragraph, one outbound link, then a large empty gap before the pager; About desktop right third empty.
- SEO: 7/10. Unique titles/descriptions, canonical, OG/Twitter with absolute og:image, JSON-LD, sitemap, 404, one h1. Risks unchanged: robots.txt/sitemap under /website/ subpath; one og:image everywhere; hotlinked figures without dimensions; identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn are on the first phone screen. Held down by no current status and no quantified result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, "For the record" ledger. Home is otherwise quiet.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met (flat surfaces, hard shadow, grain, no gradients).
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home subtitle "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" against today 2026-11-08; STATUS is empty so no status renders. Reader cannot tell graduated, studying or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede leads with snake robots (row 01), but that page is thin and has no result; "Start here" is on row 06. Two answers to "strongest project", and the lede one is weakest. Owner to supply a snake result or pick the lead.
3. Major (robustness, CLS). Figures and Resume hotlinked from Wix (wixstatic.com, filesusr.com) on 11 pages, no width/height. If URLs rotate, the Resume link breaks in header, lede and footers, and layout shifts on load. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). Raftar: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time" has no support in the repo. Owner to confirm or cut.
5. Minor (SEO). robots.txt and sitemap at a project-site subpath (crawlers only read robots.txt at the host root); submit the sitemap in Search Console (owner). lastmod identical.
6. Minor (SEO). One og:image and alt for all pages; no per-project art.
7. Minor (looks). Lopsided plates; taste. Add plates only with real figures.
8. Minor (looks). About desktop empty right third until a portrait exists. Taste.
9. Minor (fonts). Two Google Fonts, swap, no size-adjusted fallback; needs measured metrics.
10. Minor (UX, phone). Header drops Resume and GitHub on phones; kept in lede and footer. Acceptable.
11. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
12. Nit (looks). Small mono labels are the faintest text on tan; pass AA, faint on phone. Taste.

Designer-fixable this cycle: none found. Cycle 97's color-scheme/theme-color fix is in place and introduced no regression.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode, now with native color-scheme.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local, with honest "illustrative" notes.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic, with no regressions and no designer-fixable defect left that I can evidence. Everything still open waits on the owner: a current status line, a snake result or a decision on the lead project, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. Research was blocked this cycle, so no new best-practice findings were added.
