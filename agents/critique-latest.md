# Critique, 2026-10-23 (cycle 3, after SEO files, JSON-LD, marker highlight, 404 copy)

## Scores
- **AI-tell score: 3/10** (unchanged). Plain intro plus ruled index is authored, and the amber marker on "three weeks to 15 minutes" is a real print move. Tells that remain: the DM Serif + Source Serif + Plex Sans/Mono kit (the standard "print revival" stack), nine rows with identical anatomy (title, grey blurb, mono tag), evenly polished copy, and a colophon line that explains the stack. Nothing moved this cycle except the marker highlight (a point for human). The site would still look nearly identical with another name and nine other projects, because nothing on it is a picture or a voice.
- **Looks good: 5/10** (was 6; judged more harshly because it has now been two cycles with the same finding). Calm and legible, double-rule masthead is good, dark theme is solid. But: no image of any kind on home or on the first screen of any page; every project page is a stack of 3 to 9 broken-image boxes (sandbox limit, but see finding 2 for the production risk); a 20px left misalignment between masthead and content on desktop (finding 8); About h1 sits left of its 760px column (finding 9).
- **SEO and discoverability: 7/10** (was 4). Unique titles and descriptions, canonical, OG and Twitter tags with a local 1200x630 og:image, sitemap.xml, robots.txt, Person JSON-LD on home and about, CreativeWork on 9 projects, one h1 per page, landmarks. Held back by: no image width/height or local images (CLS/LCP), render-blocking Google Fonts, no JSON-LD on projects.html, `/index.html` canonical rather than the clean root, stale content signals (finding 3). Not verifiable offline: whether og.png renders as intended in Slack/LinkedIn, Search Console indexing.
- **UX: 5/10** (was 6). Name, school, lab, resume and the best number are findable in 3 seconds on phone. But contact is a sentence pointing at LinkedIn, the phone header drops the LinkedIn/GitHub icons, nothing signals the strongest project, and every project page is a long wall with no outcome, role or date up top. Dead-end risk: the resume and every figure live on Wix.
- **Fun and personality: 3/10** (was 3). One 404 joke that almost nobody sees, one marker highlight. Hover and press states on rows are good but carry no character.

Axes below 7: looks (finding 4), UX (findings 1, 3, 5), fun (finding 7). SEO is at 7, so no Major raised for it beyond findings 2 and 10.

## Method and limits
- `tools/check.py` ran on all 13 pages, 3 viewports, 2 themes (check run is slow here, about 4 minutes; use a background job). No overflow, contrast, tap-target or console failures reported; only "images not loaded" notes. I opened: index phone light, index tablet dark, index desktop light, snake-robots phone light, about desktop light. Not every screenshot was opened.
- Wix images and Google Fonts are blocked in the sandbox, so serif headings render in the Georgia/Times fallback; type pairing is judged from CSS, not seen.
- **Sources: WebFetch to w3.org, web.dev and developer.mozilla.org was refused again this cycle (permission request unanswered). I could NOT verify any source. The following are pointers from memory only; nothing in this critique depends on their exact wording:**
  - WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
  - web.dev, Optimize Largest Contentful Paint (third-party origin and resource load delay): https://web.dev/articles/optimize-lcp (blocked)
  - MDN, font-display: https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display (blocked)
  - Also relevant, not fetched: Google Search Central ProfilePage structured data; NN/g on portfolios; WCAG 1.4.3 contrast.
  - Topic this cycle: image/CLS/LCP and third-party dependency risk, font loading, content freshness, desktop alignment. Owner should enable web access for the critic if source verification is wanted.

## Owner critique items
1. **Retro matte theme.** Honored in surfaces, rules, shadows, palette. Still reads as "plain beige page" more than "printed object" (finding 4): no second surface, no ink-colour element besides rust links, grain nearly invisible at 1x. The marker highlight is the first real step; repeat that kind of move.
2. **Not AI-generated.** 3/10. The structure is human. What would push it to 2 is a voice (first-person specifics) and real pictures, both owner-supplied. See findings 5 and 7. I disagree with the designer's reading that the About slogan "push forward technological autonomy" is fine because it is original-site wording: it is still the single most generic sentence on the site ("technological autonomy").

## Ranked findings

### 1. Status and dates are still stale; the first paragraph is ambiguous (Major, credibility/UX)
Where: `index.html` subhead and lede ("I research compliant control"), `about.html` ("I'm pursuing a Master's", "I'm also taking courses", Education "2023 – 2025"). Today is October 2026, so either he graduated 17 months ago or the dates are wrong. Raised in cycle 2 and declined as "only the owner can say"; that is correct for the fix but means this is an open blocker on credibility, not a closed item.
Why: a recruiter cannot tell if he is available, a student or an alumnus; "stale" is the most damaging first impression for a 30-second visitor.
Fix: owner to answer one question: current status and location. Then one line under the name, in plain words ("MS, CMU, graduated May 2025. Now at ..." or the true expected date), and past tense on About.

### 2. All media, the resume and the portrait are hotlinked from Wix (Major, robustness/performance)
Where: 12 of 13 pages (about 30 wixstatic URLs counted by grep; the resume is a `filesusr.com` link used on home and About). In production the first-screen of every project page depends on a third-party host; no `width`/`height` on any `<img>`, so each image that loads shifts content (CLS) and the LCP element is a third-party fetch with a late discovery. One Wix plan lapse removes every picture and the resume together. (web.dev LCP/CLS guidance, unverified this cycle.)
Fix: owner supplies a media folder; host in `assets/img/` as WebP/JPEG with width/height and `fetchpriority="high"` on the first figure. Minimum: put the resume PDF in `assets/` today; it is the most clicked asset and a single file.

### 3. Projects have no outcome, role, date or team up top, and the lead is a rhetorical question (Major, UX/content)
Where: every project page; clearest on `quadrotor-sysid.html` and `snake-robots.html` phone. The `.question` heading ("How do we coordinate the motion of hyper-redundant snake robots ...?") is larger than the page's own summary and states the problem in the abstract; the `.tldr` under it is the useful sentence and is smaller. The facts list holds method labels ("Tests: Hover and sinusoidal rotation") or just Lab/Advisor. Phone length: snake page is 3 broken figure boxes after one paragraph, then the pager.
Fix: demote `.question` below the tldr or drop it; make the tldr the h1's subhead at the larger size; add a Role / When / Team / Result row only with owner-confirmed facts (from the repo I can support: snake = CMU Biorobotics Lab, advisor Choset; Raftar = captain, suspension and brakes, Formula Bharat 2023 podium; Seagate = 30 drives, 3 weeks to 15 minutes). Do not invent the rest.

### 4. Retro direction is a theme, not yet an object (Major, looks good, taste)
Where: all pages. One beige field, rust links, one button shadow. The nine rows are text-only; no figure numbers, no rule variations beyond hairline/double, no ink-block anywhere. The "K" mark in an amber box is the only graphic.
Fix (taste, keep contrast): (a) give each row a right-aligned mono index number ("01" to "09") or a small figure label "Fig. 1" once images exist, like a contents page; (b) one solid ink band (dark paper block) for the footer or the masthead date line, so there is a second surface in light mode; (c) put a 1px-bordered image with a "Figure 1." caption in the right 35% of the home intro (see 6). Raise grain alpha slightly only if text contrast still passes.

### 5. Copy is accurate but has one voice-less register (Major, AI-tell/content)
Where: row blurbs on home and `projects.html`: "A PPO agent trained to choose the burns...", "A tricycle for riders with one working leg...", "A nanosatellite concept for finding its own position ... without GPS." Each is "A X that Y." in the same cadence; the home lede has a tidy triplet ("modeling, designing and manufacturing" on About) and "My CMU GPA is 4.0" lands as a bolt-on. "Push forward technological autonomy" (About) is a slogan.
Why: real portfolios are plain and a bit uneven; this reads as evenly polished. Fix: vary the blurbs by what actually happened ("Landed a CrazyFlie on a balancing robot driving in a circle. It took an MPC and a state machine to stop it chasing the platform."), only using facts already on the project pages; delete the slogan; move the GPA to the education block or after the Seagate line with a reason. Owner can add one honest sentence about what went wrong on one project; that is the most human thing available.

### 6. Home right column is empty and no image anywhere above the fold (Minor to Major, looks good)
Where: `index.html` desktop 1366: lede measure about 650px of a 1000px frame, nothing beside it. Phone: no image before the project list either. Needs owner media; until then, tighten rather than pad: constrain `.index` rows to the same measure as the lede or put the "Seagate" and "Formula Bharat" facts in a two-line aside in that column set in mono as a ledger (3 weeks to 15 minutes / 30 drives / podium, Formula Bharat 2023). Facts exist in the repo.

### 7. Fun: one joke on a page nobody visits (Major, fun)
Where: only the 404 ("failed to land on the target") and the marker. Earned, specific ideas from repo facts:
- Hasselhoff Submarine: the "99 seconds" is already on its blurb; show a 99 second countdown stamp style counter on that row's hover that stops at 0 (no-JS safe: static text). 
- Replace the generic "Previous / Next" pager labels with the project's own detail ("Next: lands a drone on a balancing robot driving in circles").
- Seagate: set "3 weeks" struck through in ink next to "15 minutes" in the marker (a visible edit, a proofreader's mark), which carries the meaning and is on-direction.
- Footer: "To get in touch, message me on LinkedIn." is fine; a plain aside like "No email form. LinkedIn answers faster." only if true.
Trade-off: keep motion off under `prefers-reduced-motion` (already present) and keep all of it static-readable.

### 8. Desktop masthead and body do not share a left edge (Minor, craft)
Where: desktop 1366: header brand starts x=163, home heading, rows and the footer text start x=183 (the section has 20px padding inside the 1040px frame; the header and footer use `max(20px, (100vw - 1040px)/2)` padding without it). In the screenshots the brand mark sits 20px left of "Karthik Karumanchi" h1, and the footer copy starts left of the Projects rule. Fix: give header, footer and `.section` the same inner padding rule (one wrapper width). Nit-level to anyone else, but a printed page lives on its margins.

### 9. About: h1 hangs left of its column; skills list leaves holes (Minor, craft)
Where: `about.html` desktop and tablet: `.page-head` is 1040 wide while content is `.narrow` 760 wide, so "About" is about 95px left of the text. The two-column skills lists with 3, 2 and 2 items leave empty right cells and a lopsided block; the portrait floats top-right with no top alignment to the first line. Fix: put the page-head inside the narrow measure on About, set skills in one column or a single comma-separated line per group.

### 10. Render-blocking fonts and a 4-family load (Minor, performance)
Where: every `<head>`: one Google Fonts request with four families, two of them used for tiny text (IBM Plex Mono, IBM Plex Sans 500/600). `display=swap` is set (good), but each page waits on a third-party CSS request, and the fallback swap changes line breaks in the big serif headings (CLS risk). The colophon claims "one stylesheet" which is true of the first-party CSS only. Fix: self-host two WOFF2 files if owner supplies/permits, drop Plex Mono to a system mono (the tags and dates are tiny), `size-adjust` fallback metrics. Not downloadable in the sandbox.

### 11. Phone header drops LinkedIn and GitHub; contact is buried in the footer (Minor to Major, UX)
Where: phone screenshots: nav has Home/About/Projects and the theme toggle only; LinkedIn is at the very bottom of a long page. A professor on a phone must scroll past nine rows to learn how to reach him. Fix: a "Contact" text link (LinkedIn) in the home actions row next to the resume; keep the header lean.

### 12. Canonical and home URL use `/index.html` (Nit, SEO)
Where: canonical, og:url, sitemap, JSON-LD `url` mix `.../website/` (JSON-LD) and `.../website/index.html` (canonical). Pick one; `https://kmkar31.github.io/website/` is the cleaner shareable URL. Also add an `ItemList` or leave projects.html without JSON-LD deliberately. `robots.txt` is at the project path `/website/robots.txt`, which crawlers do not read (they look at the host root `kmkar31.github.io/robots.txt`); the Sitemap line there is not discoverable this way. Submit the sitemap in Search Console instead. (Reasoning from how GitHub Pages project sites are served; not tested offline.)

### 13. Lightbox and zoom links are fine, but there is no caption or full-resolution fallback when images fail (Nit, robustness)
Where: broken figures show a bordered box with underlined alt text, which is decent, but the alt strings are labels ("Modular snake robot, figure 1 of 3") that give nothing if the image never loads. Make alt say what the figure shows once the owner confirms what each is.

## Good and must not regress
- Plain home: intro in running prose, the amber marker on the Seagate number linked to `about.html#seagate`, ruled project index with a 44px+ row.
- Double-rule masthead and footer, hairline/heavy rule hierarchy; no boxes around prose.
- Dark theme as inverted print (tan ink rules, shadows darker than paper), hard offset shadow only on the primary button and filters, press states.
- Accessibility basics: skip link, `aria-current`, focus-visible outline, filter `aria-pressed` and live count, figure images as real links, modal lightbox with focus return, reduced-motion block, tap targets pass.
- SEO scaffolding added in cycle 2 (titles, descriptions, OG/Twitter, local og.png, sitemap, JSON-LD, 404). Keep `build/build.py` as the single source so it stays in sync.
- Specific, un-invented facts (Seagate numbers, Formula Bharat 2023, 99 seconds, 500 m tether, CrazyFlie/Tumbller). Keep the rule of not inventing facts.

## Verdict
The site has stopped looking generated: it is a quiet, honest, well-built index with a sound retro skeleton. It is not yet good enough: it is bare (no images, nothing to remember), its dates say he is still a student in a year when he is not, and every picture and the resume still depend on a Wix account. The designer can fix craft items (4, 8, 9, 11, 12), copy variety (5) and the pager/marker/ledger touches (6, 7) without the owner; findings 1, 2 and 3 need the owner to supply status, a media folder and confirmed role/date facts, and they are now the ceiling on every score. Until they land, expect the Looks, UX and Fun axes to stay under 7.
