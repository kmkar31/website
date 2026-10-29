# Critique, 2026-10-29 (cycle 39, reviewing main at 51f3513)

## Sources
- WebFetch of web.dev optimize-cls and WCAG 2.2 focus-appearance was blocked (permission not answered). WebSearch returned only titles for an NN/g portfolio query; no page was read. Nothing below rests on a page I read. Pointers only:
  - https://web.dev/articles/optimize-cls (explicit image dimensions, font swap shift)
  - https://www.nngroup.com/videos/ux-portfolios/ (what hiring managers scan for in portfolios)
  - https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html (focus indicator)
  - https://www.w3.org/WAI/WCAG22/Understanding/non-text-content (alt text)
- Measured: `python3 tools/check.py . agents/shots`, 13 pages x 3 viewports x 2 themes, 0 failures (only "images not loaded", a sandbox limit).
- Viewed: home phone light, home desktop dark, Raftar tablet light. Grepped HTML for hotlinks, Resume href, og:image, titles, reduced-motion and focus-visible rules.
- Topic this cycle (varied): portfolio content depth for a 30-second reader, plus resume and media dependency risk.

## Scores
- AI-tell: 3/10 (unchanged). No gradient, glass, glow, stat strip, card trio or slogan. Authored: struck-through "three weeks", ledger, outcome stamps, Fig./Sheet N of 9 plates, honest colophon. Residual risk is the cream + serif + terracotta + mono small-caps kit. Tells moved: none. Last cycle's change (UI chrome now Source Serif 4) removed the one non-print voice; nav and buttons now read as one family.
- Looks good: 7/10. Desktop dark home is calm, ruled and well aligned. Phone home is a long list of nine evenly weighted rows with a line-drawn placeholder as the first image. Project pages are mostly plate plus two short paragraphs.
- SEO: 8/10. Unique titles and descriptions, one h1, canonical, absolute og:image (https://kmkar31.github.io/website/assets/og.png), JSON-LD, sitemap, 404. Sitemap and robots sit under a project subpath. Not verifiable offline: og:image fetch, Wix image weight.
- UX: 7/10. Name, specialty, strongest facts, Resume and LinkedIn are visible on the first phone screen. Held down by LinkedIn-only contact, Resume on a Wix file host, no status or date.
- Fun and personality: 7/10. Struck "three weeks", "Time allowed: 99 s" stamp, the 404 joke, numbered sheets. Quiet elsewhere.

## Owner critique (agents/user-critique.md)
- Retro, matte, warm, print-like: met. Flat paper, ink rules, double rules, hard-shadow button, dark theme reads as inverted print.
- Not AI-looking: met at 3/10. Remaining risk is repeated marks, not a template tell.

## Findings (ranked)
1. Major (credibility, owner-only). No status or date. About says CMU "2023 - 2025"; today is October 2026 and nothing says graduated, working or available. `STATUS` in build/build.py:259 is empty. One owner sentence fixes it.
2. Major (robustness, owner files). Resume (header, hero, footer, every page) points to a filesusr.com Wix URL; 40 wixstatic figures remain across eight project pages, and snake-robots figures have no width/height (CLS risk, web.dev optimize-cls). A dead Resume link is the worst failure for a recruiter. Needs assets/resume.pdf and local images from the owner.
3. Major (owner decision). "Start here" is on row 01, Snake robots, the page with the least evidence of what he did or what happened (placeholder plate, generic figures, "figure 1 of 3" alt). Supply an outcome or move the label to Aerobraking (46 orbits) or Hasselhoff (99 s).
4. Major (content, owner facts). Raftar page, seen in the screenshot, is a tl;dr, a question, one sketch and two sentences. "Did the suspension and brakes" has no component, number or result, and the sketch is a generic car. For a captain claim this is the thinnest credibility spot. Needs owner facts.
5. Minor (consistency, owner). Raftar role verbs differ: home "I captained the team", About "contributed to"/"led", Education "Captain". Pick one.
6. Minor (verify). Raftar "one-fifth the weight of a Ferrari but matches its 0-60" is unverifiable here. Owner to confirm wording and numbers.
7. Minor. Alt text on Wix figures is generic. Owner must say what each shows (WCAG non-text content).
8. Minor. Two Google font families, display=swap, no size-adjusted fallback; first-load reflow likely. Needs real font files to self-host.
9. Minor (taste). Stamps on home rows 04 to 07 only; rows 01 to 03, 08, 09 have none. Add none without real numbers.
10. Minor. Contact is LinkedIn only (owner constraint). Conversion risk, not a defect.
11. Nit (taste). The snake placeholder plate is the first image on phone and reads as a stand-in; a real lab photo is the largest looks-good upgrade (owner file).
12. Nit (taste). About desktop leaves the right third empty without a portrait. Accepted earlier.

No designer-fixable defect found this cycle; no regression from the cycle 38 font change (header fits one row on phone, tap targets intact).

## Good, must not regress
- Retro matte system: paper, ink rules, double rules, hard offset shadow on the one button, inverted-print dark theme.
- Home lede with the struck "three weeks" and "For the record" ledger; honest colophon.
- Outcome stamps only where a real number exists (99 s, 46 orbits, 500 m, podium).
- Fig./Sheet N of 9 plates drawn from facts on each page; pager with neighbour facts.
- Local og.png, canonical, JSON-LD, sitemap, 404 with a joke; keyboard-operable 99 s stamp; focus ring (3px outline); reduced-motion rule present.
- No invented facts: STATUS slot left empty rather than guessed.

## Fun ideas from repo facts only (optional taste)
Hasselhoff tab title as the "Time allowed: 99 s" stamp; Seagate strike-through press state revealing "15 minutes".

## Verdict
The design is coherent, plain and clearly authored, and the cycle 38 type change closed the last non-print voice. What holds the site back is no longer design: it is five owner inputs (a status sentence, a local resume.pdf, local images with alt text, what he did and achieved on Snake robots and Raftar, a decision on "Start here"). Until those arrive, further designer cycles will return diminishing results.
