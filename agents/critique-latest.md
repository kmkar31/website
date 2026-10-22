# Critique, 2026-10-22 (cycle 1, after first retro matte pass)

**AI-tell score: 5/10.** The palette, borders and hard shadows are a real break from the gradient/glass look. But the structure is still the stock template: hero with portrait on the right, then a four-cell stats strip, then a grid of identical bordered cards, then a three-column "what I work on", then a "Get in touch" band. Swap the name and projects and it would look the same. The retro look is currently a skin over that skeleton.

Tells that moved since baseline:
- Gradient text, blobs, glass, pulse dot, floating badges: gone (good).
- Slogan hero: replaced by a plain, specific lede (good).
- Stats strip: still there, and cell 4 ("9 projects") is filler.
- Three-card "what I work on" row: still there, now as ruled columns with 01/02/03 numerals (an AI-template favorite).
- Card grid with identical radius, border, shadow, chip row and "Read the project" link: unchanged.
- Still present: tidy triplets ("designing, simulating, building and testing"), the "X that Y" pattern in card blurbs.

## Method and limits
- `tools/check.py` ran on all 13 pages x 3 viewports x 2 themes. It reported no overflow, no contrast failures, no tap-target failures, one h1 per page. (It needs about 3 minutes; run it in the background. It writes to `agents/shots`, which is gitignored; I wrote to the scratchpad instead.)
- I viewed the home page (desktop light, phone light), a project page (desktop dark) and the projects page (tablet dark). I did not open every screenshot.
- Wix images are blocked in the sandbox, so every image shows as a broken box. I judged layout only, not picture quality.
- Research: WebFetch to w3.org, web.dev and nngroup.com was refused for permission, and a web search returned nothing usable. The references below are cited from memory and NOT re-verified this cycle. The designer should treat them as pointers, not quotes.
  - WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
  - web.dev, Optimize Cumulative Layout Shift: https://web.dev/articles/optimize-cls
  - NN/g, portfolio and hiring-manager scanning: https://www.nngroup.com/articles/portfolios/
  - WCAG 2.2 SC 1.1.1 Non-text Content: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
  - MDN, `<img>` width/height and aspect ratio: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img

## Owner critique items
1. **Retro matte theme.** Mostly honored: flat paper tones, 2px ink borders, hard offset shadows, no blur. Still drifting: (a) the grain is only 7% alpha and invisible, so surfaces read as flat beige rather than printed paper, (b) the dark theme is a warm-brown dark mode with cream shadows, which is a generic "dark mode" rather than a retro one, (c) every element uses the same 2px border and the same shadow, so nothing feels typeset. See findings 3 and 6.
2. **Must not look AI-generated.** Partly met. Score 5/10, see above and findings 1, 2, 3.

## Ranked findings

### 1. Home page is still the stock template stack (Major, AI tell)
Where: `index.html`, all viewports. Hero, stats strip, 3x2 card grid, 3-column focus block, footer band.
Why: the layout is identical to what generators emit, so the retro skin reads as costume. The focus block repeats what the project cards and About page already say.
Fix: cut the "What I work on" block and the "9 projects" stat. Make the home page a plain index, closer to a printed table of contents: a short intro, then a numbered list of projects (year, title, one line, tag) as ruled rows rather than boxed cards. Put the Biorobotics/Seagate/Formula Bharat facts in running text, not a strip.

### 2. All images are hotlinked from Wix and none has dimensions (Major)
Where: every page (about 70 `wixstatic`/`filesusr` URLs; the og:image, the resume PDF and the portrait too).
Why: if the Wix site is taken down or changes plans, the portfolio loses every picture, the portrait and the resume at once. Images lack `width`/`height`, so layout shift on project pages is likely (project figures have no reserved space; only home/projects thumbs use `aspect-ratio`). The social card also depends on Wix. Source: web.dev CLS guide (unverified this cycle).
Fix: download everything into `assets/img/`, resize and convert to WebP, add `width`/`height` to each `<img>`, and use a local og:image (1200x630) and a local resume PDF.

### 3. Every surface has the same border, shadow and radius (Major, AI tell and retro fit)
Where: cards, stats strip, results box, timeline cards, pager, buttons, filters, portrait frame. All `2px solid ink` plus a 3 to 6px offset shadow.
Why: uniform treatment gives no hierarchy beyond size; it is the "uniform spacing and radii on everything" tell. Print-era design uses rules of different weights (hairline, 1pt, double rule) and leaves most content unboxed.
Fix: reserve boxes and shadows for the 2 or 3 interactive things (primary button, project row on hover). Turn the stats strip, timeline cards and focus block into plain text with hairline rules. Use a double rule under the header and above the footer, and a small-caps running header on project pages.

### 4. Project pages have no real content hierarchy and thin "results" (Major)
Where: `quadrotor-sysid.html` (desktop dark), `snake-robots.html`, others.
Why: the "results" box on sysid shows "4 coefficients / Grey-box ID", and on snake robots "CMU Biorobotics / Compliant control". These are labels, not results. The sysid page opens with two paragraphs of textbook explanation before saying what was done or found. A recruiter with 30 seconds sees no outcome. Some captions and alt text are generic ("Snake robot project" x several, identical alt on different images).
Fix: lead each project with role, dates, team size, tools and one concrete outcome (number or demo) that Karthik can confirm. Move background below. Write distinct alt text per figure. Do not invent figures: ask the owner for real numbers.

### 5. Missing project media and reports (Major, content)
Where: projects noted in LOG as missing videos and PDFs (Wix originals).
Why: projects about motion (snake robot, quadrotor landing, submarine) with only static pictures undersell the work. Reports/PDFs are the strongest evidence for a professor.
Fix: obtain the media from the owner, host locally (or link YouTube), and add a "Report (PDF)" link where one exists.

### 6. Dark theme is not retro (Minor, taste)
Where: all pages, dark. Dark brown with cream borders and amber accents is a standard "warm dark mode". The cream hard shadows on dark read as glow-adjacent.
Fix: either make dark an inverted-print look (black ink on dark paper with muted ochre rules, no light shadows; use a darker offset shadow instead) or drop the toggle and follow `prefers-color-scheme` only. Taste, but the owner asked for coherence.

### 7. Typography is a safe pairing (Minor, AI tell)
Where: site-wide. DM Serif Display headings + IBM Plex Sans/Mono. Plex Mono eyebrows, uppercase chips and numbered labels are a recognizable trending combination. Headings are one weight and size-only hierarchy.
Fix: pick one body serif for long text (e.g. a readable text serif) and keep mono only for dates/captions; drop the uppercase eyebrow over the h1 (it repeats the title tag).

### 8. Hero: portrait is a hotlinked image in a double frame; without it the right half is empty (Major while images are remote)
Where: `index.html` desktop. With the image missing, the frame collapses to a small box and the hero looks unbalanced. Even with it loaded, the double border plus offset shadow is the "polaroid card" pattern.
Fix: local, fixed-size image with `width`/`height`; single border or none. Consider moving the portrait to About only.

### 9. Copy: some lines are generic or slightly unsupported (Minor)
Where: `index.html` card blurbs ("A drone that finds, tracks and lands...", "a spacecraft ... on its own, using less fuel"), the focus block ("models that are accurate yet light enough to run on the robot"), About ("My goal is to push forward technological autonomy").
Why: "X that Y" rhythm and abstract claims; "using less fuel" and "40+ students" need the owner to confirm they come from the original site. LOG says the headline and focus copy are rewrites awaiting confirmation.
Fix: replace with specifics (what the controller was, what it ran on, what the result was). Mark anything unconfirmed for the owner instead of shipping it.

### 10. Contact is thin for a recruiter (Minor)
Where: footer on every page. "Get in touch. Find me on LinkedIn or GitHub." with no email, by design. The footer band repeats the hero buttons (LinkedIn/GitHub/Resume appear in header, hero and footer).
Fix: owner decision. If no email, say so honestly ("LinkedIn is the best way to reach me") and drop the duplicated Resume button; keep one resume link near the top.

### 11. Hero buttons: three equal-weight actions (Minor)
Where: `index.html`. "See the projects", "About me", "Resume" are all boxed buttons; "About me" duplicates the nav.
Fix: one primary button, resume as a text link.

### 12. Scroll-reveal animation carries no information (Minor, AI tell)
Where: all pages (`.reveal`, staggered `transition-delay`). Content starts at opacity 0 until JS runs, with a 2.5s safety net. Reduced-motion is handled, but a slow IntersectionObserver or print view can show blanks.
Fix: remove it, or limit it to nothing. Content that is visible on load is more robust and more honest.

### 13. Page titles are shortened to unhelpful strings (Minor, SEO)
Where: `<title>` of project pages: "Aerobraking", "Snake Robots", "Quadrotor Landing". Search results and tabs lose the project name; no canonical, no per-page meta description or og:image beyond the default.
Fix: use the full project name plus one descriptor; add per-page descriptions.

### 14. Lightbox and filter robustness (Nit)
Where: `assets/site.js`. The lightbox is a click handler on non-focusable images (keyboard users cannot open it; no focus trap, no return of focus). Filters change `hidden` without announcing the result count. Without JS the filter buttons do nothing (acceptable) but the lightbox `<img alt="">` is empty until used.
Fix: wrap figure images in links to the full image (works without JS, keyboard friendly); add a live region for the filter result.

### 15. Favicon and mark (Nit)
Where: header `K` tile with an amber fill and a rounded-square favicon (`rx=16`) in a sans font. Rounded app-icon shape does not match the squared, print look.
Fix: square favicon in the serif face.

## Do not regress
- Plain, specific hero lede that names the lab, advisor and podium result.
- Real, checkable facts in the About timeline (Seagate 3 weeks to 15 minutes, 30 drives; GPAs; dates).
- No gradients, blur, glow, pulse dots or floating badges.
- Mobile header (single row, headline before portrait), 44px tap targets, no horizontal overflow, contrast passing in both themes.
- Skip link, visible focus ring, one h1 per page, reduced-motion handling.
- Project pager and "question" line on project pages (a genuine point of view).

## Verdict
The designer removed the loudest AI tells and the contrast, tap-target and overflow checks pass, so the site is solid on the basics. It does not yet have a point of view: the layout is still the stock hero, stats, card grid and footer band, and every surface gets the same box. The biggest risks are practical, not stylistic: every image, the portrait, the social card and the resume depend on Wix, project pages lead with outcome-free labels and textbook background, and motion projects have no video. Next cycle should make images local with dimensions, rewrite project openings around role and result (with owner-confirmed facts), and then restructure the home page into a typeset index with varied rules instead of repeated boxed cards. Source verification for the cited guidance was not possible this cycle (fetches refused), so those references should be re-checked.
