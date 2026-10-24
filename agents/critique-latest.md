# Critique, 2026-10-24 (after cycle 11)

## Sources
WebFetch was blocked this cycle (permission request unanswered), so none of these could be opened. They are pointers from background knowledge, not verified quotes:
- web.dev optimize CLS (font swap shift, size-adjust fallback): https://web.dev/articles/optimize-cls (blocked)
- NN/g portfolio guidance: https://www.nngroup.com/articles/portfolios/ (blocked)
- WCAG 2.2 SC 2.5.8 target size: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (blocked)
Findings below rest on what I measured and saw in the repo.

Measured: tools/check.py timed out at 2 min in my run, but screenshots were regenerated. I looked at home (desktop light, phone light and dark), About desktop, snake-robots phone. Repo grep: every page still hotlinks wixstatic/filesusr (3 to 9 references per page), the resume PDF is on filesusr, fonts come from Google Fonts, assets/ holds only og.png, site.js, style.css.

## Scores
- AI-tell score: 4/10. Down from the gradient and card-stack era. Remaining tells: warm-cream editorial palette with serif display plus terracotta accent is itself a 2025 template look; the numbered list with mono index, stamps and a mono "for the record" sidebar is a well-worn "editorial" kit; one-line hero + lede + ledger is tidy. Moved since last cycle: "Start here" label added (human, useful); stamps now consistent (less accidental, slightly more systematic). Praise: struck-through "three weeks" highlight, 99 s stamp, "failed to land on the target" 404 are specific.
- Looks good: 6/10. Typographic hierarchy is clear and the home page is calm and scannable. But there is no image anywhere. Every page is text on cream; project pages are a title, a tl;dr, two fact rows and a paragraph (snake-robots page ends after about 1.2 screens with nothing visual). Project pages look unfinished, not minimal.
- SEO: 7/10. Unique titles and descriptions, canonical, OG, local og.png, JSON-LD, sitemap, robots present. Weaknesses: robots.txt cannot work on a project subpath; the og card is text only; render depends on Google Fonts (no size-adjusted fallback); no image alt content to index because media is broken.
- UX: 6/10. Name, field, strongest project, resume, LinkedIn within one phone screen: good. Problems: contact is only LinkedIn (and a hotlinked PDF that may die), no status or date line, Resume hidden in the phone header, project pages have no outcome section.
- Fun and personality: 5/10. Three good touches (strike-through, 99 s stamp, 404). Everything else is plain. Site is tidy, not memorable.

## Owner critique (user-critique.md)
1. Retro, matte: committed (flat paper, ink rules, hard shadow on one button, no blur or gradient). Grain is barely visible; fine. Fit is good. Drift risk: it reads "warm editorial blog" more than "retro print"; see finding 6.
2. Not AI-looking: improved; see score and finding 6.

## Findings (ranked)

1. Major (UX, looks good). Project pages have no visual evidence and a thin, generic body. Snake-robots phone page: tl;dr, two fact rows, a background paragraph taken from the field, then pager. A recruiter gets no proof of the work. Whole site depends on owner-supplied media (images, videos, report PDFs), which has been deferred for 10 cycles. Recommendation: stop waiting. Ask the owner for one image per project, or have the designer draw a flat diagram per project from facts already on the page (tether length 500 m, four thrusters, elliptical four-bar linkage, 46 orbits). Authored line art in ink fits the print direction and cannot hotlink-fail. Source: NN/g portfolio guidance (unverified).

2. Major (robustness). Every page still hotlinks Wix, including the resume PDF the home page, About page and footer point to. If that URL rots, the main call to action is dead. Not verified offline. Copy the PDF into the repo; this is the single highest-value owner action.

3. Major (UX). No status or date: Home says "MS ... Carnegie Mellon" and About says 2023 to 2025 and today is October 2026. A reader cannot tell whether he has graduated or is available. The STATUS slot has been empty since cycle 4. Owner needs to answer one question. Flag as stale-looking content, not a design bug.

4. Major (fun, below 7). The personality is concentrated in three details; the rest is a clean resume. Ideas grounded in repo facts only: (a) Hasselhoff page: a small index-card with "target: IR beam, 99 s" as the first thing on the page; (b) pager text on a project page could carry the stamp of the neighbour; (c) a real colophon line with true constraint ("one stylesheet, no framework", already stated elsewhere); (d) a visible ruler or tolerance mark on the snake/tricycle pages. Trade-off: keep each static or press-only (reduced-motion safe) to avoid decorative-motion penalty.

5. Major (UX, About). About page desktop has a large empty right column beside the intro and Skills (the portrait slot is empty after the portrait collapse), so the page looks left-heavy and unfinished. The portrait is missing because it is hotlinked. Either supply the portrait or lay out for its absence; the designer has declined this repeatedly, but a missing image is the current state, not a hypothetical.

6. Major (AI-tell). Palette and kit: cream background, near-black brown text, one terracotta accent, one amber highlight, DM Serif Display, mono labels. It is competent and also the most common "tasteful" generator output. Concrete alternative: commit harder to print. Pick one real reference (an engineering lab notebook, graph paper, a patent drawing plate, or a Letterpress specimen sheet) and let it dictate one non-default thing: for example a faint grid rule on the project index, figure numbers ("Fig. 1") on every project, or a two-ink (black plus one spot colour) rule applied consistently to stamps, buttons and links. Taste, but I label the sameness risk as the biggest remaining tell.

7. Minor (SEO and CWV). Google Fonts is render-affecting and third-party; no fallback metric adjustment. Not verifiable offline. Self-hosted WOFF2 is the fix and needs real font files. Source: web.dev CLS guidance (unverified).

8. Minor (SEO). robots.txt in a project subpath is ignored by crawlers; sitemap is only discoverable if submitted. Harmless; the designer already said so. OG image is a text card, so shares carry no project visual.

9. Minor (UX). Phone header hides Resume; reaching it needs the home lede or the footer. Acceptable, but on phone project pages there is no resume or contact link until the footer.

10. Minor (looks good). Home phone view: three actions (button, Resume, Contact on LinkedIn) wrap to two rows with the third link alone on the second row and unaligned. Group them or give the third a clear row.

11. Minor (UX). Home and Projects both list all nine projects; the filtered Projects page adds little with no thumbnails (they fail to load). Consider whether it earns its nav slot.

12. Nit. Row blurbs on home are close to the project tl;dr text; the same sentence appears on three surfaces (row, page tl;dr, pager). Vary or shorten.

13. Nit. Stamps are boxed capitals in the same face; the double-border, tilt and solid variants are inconsistent in a way that reads as arbitrary rather than authored. Pick two stamp types max.

14. Nit. The "Resume↗" in the header uses an arrow glyph but the same link in the body reads "Resume (PDF)"; unify the label.

## Good, do not regress
- Home: name, one-line affiliation, specific lede, struck-through "three weeks to 15 minutes", ledger sidebar, "Start here".
- Flat matte surfaces, hard shadow on one button only, no gradients, blur or glow.
- Dark theme as inverted print with readable contrast.
- Unique titles and meta per page, clean canonical, JSON-LD, local og.png, sitemap.
- Graceful collapse of failed images and captions.
- The 404 line and the pressable 99 s stamp.
- Pager shows neighbour summaries, giving a next step on every project page.

## Verdict
The site has moved from template to something with a voice: plain copy, real numbers, a coherent flat print system and no obvious AI gradients. What holds it back is no longer polish but substance and risk. There are no images, no outcomes beyond one or two numbers, no status line, and the resume, portrait and project media are all fragile Wix hotlinks. The visual system is tasteful and, for that reason, still close to a stock editorial look. The next cycle should stop declining "needs owner files" and either extract the files from the owner or produce authored, repo-local line illustrations and a self-hosted resume, then push one non-default print idea consistently.
