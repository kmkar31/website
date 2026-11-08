# Critique, 2026-11-08 (cycle 97)

Rendering: `python3 tools/check.py . <scratchpad>/shots` ran in the background; every line reported OK (only "images not loaded" sandbox notes). I viewed index phone light and aerobraking-drl phone dark. Repo greps: `STATUS = ""` (build/build.py:262); Ferrari claim raftar-formula-racing.html:48; wixstatic on 11 of 13 pages (7 on aerobraking-drl). No site files edited. HEAD b2321ab (cycle 96), no regression seen.

## Sources consulted
- web.dev, Improve dark mode default with color-scheme and a meta tag, https://web.dev/articles/color-scheme (read in full this cycle).
- WCAG 2.2 Understanding Focus Not Obscured, https://w3c.github.io/wcag/understanding/focus-not-obscured (search listing only; fetch not read).
- Nielsen Norman Group portfolio advice via search listings only (no primary page read), so no claims drawn from it.
- Carried over: WCAG 2.5.8 target size, web.dev CLS and size-adjust (earlier cycles).

## Scores
- AI-tell: 2/10, unchanged. Flat paper, double rules, hard-offset button, struck-through "three weeks" on amber, stamps, Fig./Sheet captions, plain first-person lede. No gradients, blur, glow, card trio, stats strip or slogans. Residual: intro, ruled list, dark footer is a familiar shape; blurbs share a verb-led cadence. No tell moved.
- Looks good: 8/10. Phone light and dark hold: steady ruled rhythm, dark reads as inverted print. Weak: row 06 is the only row with a plate (on phone it sits above the title and breaks the list rhythm); snake-robots (the lede project) is thin; About desktop right third empty.
- SEO: 7/10. Unique titles/descriptions, canonical, OG/Twitter with absolute og:image, JSON-LD, sitemap, 404, one h1. Risks: robots.txt and sitemap under /website/ subpath; one og:image everywhere; hotlinked figures without dimensions; identical lastmod.
- UX: 6/10. Name, field, lede, Resume and LinkedIn appear on the first phone screen. Held down by no current status and no quantified result on the lede project.
- Fun and personality: 7/10. 99 s stamp, 404 joke, strike-through, plates, "For the record" ledger. Home has little beyond the strike-through.

## Owner critique (agents/user-critique.md)
1. Retro, matte, no glossy gradients: met.
2. Not AI-looking: met on visuals and copy. Do not regress.

## Ranked findings
1. Major (UX, credibility). Home "MS Mechanical Engineering, Carnegie Mellon University" and About "2023 - 2025" against today 2026-11-08; the Status row never renders because STATUS is empty. Reader cannot tell graduated, studying or available. Owner must supply one line.
2. Major (UX, 30-second test). Lede leads with snake robots (row 01) but that page is a schematic, one paragraph and an outbound link; "Start here" sits on row 06. Two answers to "strongest project", and the lede one is thinnest. Owner to supply a snake result or pick the lead.
3. Major (robustness, CLS). Photos and Resume hotlinked from Wix (wixstatic.com, filesusr.com) on 11 pages; no width/height. If URLs rotate, Resume breaks in header, lede and footers. Needs owner files and real dimensions; do not guess ratios.
4. Major (credibility). Raftar: "one-fifth the weight of a Ferrari but matches its 0-60 acceleration time". Nothing in the repo supports it. Owner to confirm or cut.
5. Minor (dark mode, NEW, designer-fixable). No `color-scheme` meta or CSS property anywhere (grep: only two prefers-color-scheme media queries in assets/style.css). Per web.dev, `<meta name="color-scheme" content="light dark">` plus `color-scheme: light dark` on :root makes scrollbars, form controls, selection and the pre-CSS first paint follow the theme, avoiding a light flash on dark systems. Related: index.html has a single `theme-color #efe7d6`; on phones in dark mode the browser bar stays cream over the dark page. Fix: two theme-color metas with media="(prefers-color-scheme: dark)", and make the manual toggle (data-theme in site.js) update the meta and color-scheme. Low risk, no content change. Verify the dark hex against the real dark background token before using it.
6. Minor (SEO). robots.txt and sitemap at a project-site subpath; submit sitemap in Search Console (owner). lastmod identical.
7. Minor (SEO). One og:image and alt for all pages; no per-project art.
8. Minor (looks). Lopsided plates, taste; add plates only with real figures.
9. Minor (looks). About desktop empty right third until a portrait exists. Taste.
10. Minor (fonts). Two Google Fonts, swap, no size-adjusted fallback; needs measured metrics.
11. Minor (UX, phone). Header drops Resume and GitHub on phones; kept in lede and footer. Acceptable.
12. Nit (copy). Blurbs share a verb-led cadence; vary only with facts already present.
13. Nit (looks). Small mono labels are the faintest text on tan; pass AA, faint on phone. Taste.

Designer-fixable this cycle: item 5 only.

## Good, must not regress
- Retro matte system: paper, grain, double rules, one hard-shadow button, inverted-print dark mode.
- Struck-through "three weeks" on amber; stamps (46 orbits, 500 m, 99 s, podium double border).
- Fig. 1 plates with "Sheet n of 9 . NTS" captions, repo-local.
- Plain first-person lede with real specifics; no slogan copy.
- Failed images collapse cleanly; pager shows the neighbour's first fact.
- One h1 per page, JSON-LD, canonical, 404 with a joke, skip link, 44 px targets.

## Verdict
The site is authored, coherent and not generic, with no regressions. One small designer-fixable gap is new: color-scheme and a dark theme-color are missing, so native UI and the phone browser bar ignore the dark theme. Everything else still waits on the owner: a current status line, a snake result or a decision on the lead project, a confirmed or cut Raftar claim, and local Resume and images with real dimensions. Research was thin again; only one primary page (web.dev) could be read.
