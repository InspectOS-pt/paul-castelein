# Personal-site reference fidelity check

Date: 2026-10-19

Final result: passed

## Scope and reference

Primary: https://www.meta.ai/share/a/da152857-a176-45d3-980d-4aa4c59501a1

Earlier personal reference: https://www.meta.ai/share/a/93609441-8480-48d2-b351-268c26975023

Supplemental Skaler reference: https://www.meta.ai/share/a/856073c5-7749-4574-914e-06e4d908a09c. Its venture relationships inform the explanation; Skaler itself is outside this repository's change scope.

The user's latest direction is to retain approved copy and practical functions while closely following Paul's chosen layout. No business results or capabilities were added by the implementation.

## Visual evidence

Source and implementation screenshots were inspected together at 1440px and 390px. The live source's iframe was cropped below Meta's 68px toolbar for the first-screen comparison. A passive local rendering of captured source markup was also used for normalized section comparisons, with the same original posters and fonts. No source JavaScript was executed in the site. QA-only source markup was removed by the final public build.

Local evidence, excluded from release:

- `qa/faithful-reference-desktop.jpg` and `qa/faithful-implementation-desktop.jpg`
- `qa/faithful-reference-mobile.jpg` and `qa/faithful-implementation-mobile.jpg`
- `qa/source-section-{2,3,4,5,6}.jpg` and `qa/implementation-section-{2,3,4,5,6}.jpg`
- `qa/faithful-about-live.jpg`: real portrait loaded after scrolling, header still at viewport top
- `qa/faithful-pt-mobile.jpg` and `qa/faithful-es-mobile.jpg`
- `qa/responsive-faithful.json`
- `qa/faithful-final-home-desktop.jpg`

The 1240px container, 24/32px gutters, 42/64/74px hero scale, 1.2/.8 hero split, two-by-two portfolio, three cooperation columns, dark Thesis, nested third figure, framed flywheel, economics cards, Memos rows and About/contact placement match the source structure. The initial five posters were byte-identical to that reference; their later editorial replacements are documented below. Stone palette, borders, radii and source figure shadows are retained.

## Intentional practical differences

- EN/PT/ES navigation and translated body copy from Paul's final attachments.
- Keyboard-operable mobile menu, Escape/selection dismissal, skip link and reduced-motion handling. The menu breakpoint accommodates the language switcher without overlap.
- Real rounded Paul portrait replaces the reference's PC placeholder.
- Original English diagrams have localized captions, alt text and full descriptions. Caption text is concise; image pixels remain the supplied originals.
- Source copy's lost compound hyphens stay corrected. The unwanted credentials comparison remains removed as Paul requested.
- Homepage contact action leads to the existing introduction form with an accurate action label. The form prepares a local email draft; it does not submit an enquiry.
- Venture titles preserve working project destinations. Existing deep URLs and preview indexing restrictions remain available. The completed privacy notice is available in all three languages.
- Fonts and figures are self-hosted rather than importing a third-party runtime or font service.

## Functional checks and resolved findings

- Build validates all 21 content pages, 3 error pages, 16 legacy destinations, resource paths, one H1, language alternates and metadata.
- Homepage anchors resolve in all three languages.
- Widths 360, 390, 900, 1024 and 1440 checked. No horizontal overflow or duplicated desktop/mobile navigation in the tested home/contact layouts.
- Sticky header remains at y=0 after scrolling to About; real 400px source portrait loads normally.
- Mobile menu opens, follows a section and closes. Capital contact starting point is selected correctly. Empty required fields show localized errors. Valid local inputs generate the expected mailto draft without a server form action.
- No app-origin JavaScript console errors observed.
- Fixed during review: malformed removal of the external font import, inaccurate homepage draft label, inherited tablet menu breakpoint, Spanish description punctuation and formal contact-note register.

No unresolved P0, P1 or P2 design or functional findings in this scope. Formal company-account deployment and DNS remain with the company deployment owner.

## Privacy notice completion

The October 19 update replaces the provisional review notice in English, European Portuguese and Spanish with a dated notice. It names Pieter Paul Castelein and his public contact email, describes the verified local-only form behavior, and sets purpose-based enquiry retention without claiming a made-up automatic deletion period. Recipient categories cover relevant helpers and email/IT providers; the website-level absence of CRM/AI processing is not presented as a claim about mailbox settings. Vercel's provider notices and the CNPD are linked. Following Pieter's instruction to use the company address, postal contact now lists Pieter c/o Skaler at Rua Salvador Martins 3A, 2740-315 Porto Salvo, Portugal, verified against RealOS's official contact page. No unconfirmed change of legal controller has been made.

Verification: all 63 public files built successfully; only the three privacy pages differ from the previously checked preview bundle. All non-privacy locale copy is unchanged. The three language versions have matching structure and links. The updated notice was inspected in the browser at desktop and 390px mobile width, including language switching and the contact/provider links. No horizontal overflow or browser errors were found.

## Later editorial figures and company postal address

Sources: Paul's [five editorial concepts](https://meta.ai/share/c/JS2R2WLPPa) and [three variants per concept](https://meta.ai/share/c/LhSSMKcb18). Fifteen source images were inspected. Selection follows visible content, not the generated option labels, which sometimes point to another concept. The exact five selected files and unchanged-pixel hashes are recorded in `content/editorial-figure-provenance-2026-10-19.json`.

The chosen source originals are 1920×1280: Trust/Proof columns, the 2030 Venn model, the information-verification funnel, the circular four-venture flywheel, and five nested rectangular layers. The existing site layout and Paul's final business copy are retained. English, Portuguese and Spanish alt text, captions and long descriptions now describe these actual pictures.

Source and implementation are shown together at matching scale in `qa/editorial-comparison-1.png`, `qa/editorial-comparison-3.png` and `qa/editorial-comparison-5.png`. Each capture is 1024×900 CSS and image pixels at 1× density. The source images fit the left column; the same original pixels appear in the implemented figure in the right column, within the site's existing border, radius and shadow. All five full figures were compared; the full-size originals were also opened to inspect small lettering. Actual-page evidence includes `qa/editorial-home-desktop.png`, `qa/editorial-memos-desktop.png` and `qa/company-address-mobile.png`.

Required surfaces: raster typography and fine line weights remain unchanged; source proportions and uncropped content match; off-white paper, warm stone and black ink replace the earlier blue graphics; original image quality is preserved with no re-encoding; app captions match the displayed content in three languages. The added company postal-address paragraph is the only locale-copy change. The page structure, navigation and contact form remain as previously verified.

No actionable P0/P1/P2 findings. P3 source-art labels remain as supplied: the small Trust illustration footer says 2024 and the model/funnel include variation labels. These are illustration labels, not website publication dates or research claims. No source-image text has been edited or hidden.

Final result: passed


## Latest Swiss Bold / terracotta figures

Source: https://meta.ai/share/c/NJl6fhF6MQ. The Swiss Grid / Bold Editorial group replaces the preceding thin-ink illustrations; the approved editorial page layout and all business/privacy locale copy remain unchanged. The related links https://meta.ai/share/c/lRh7eHhn25, https://meta.ai/share/c/VcZe4iF1Gp and https://meta.ai/share/c/TYcEcdu5LC concern Skaler illustration variants and are outside the personal-site implementation.

All five source files are served byte-for-byte, with content-based mapping: Trust/Proof columns, two-panel 2030 model, three-panel information asymmetry, the four-venture data flywheel and the portrait Five Moats poster. Meta's business-model/five-moats response labels are reversed; filenames follow the actual image titles. Provenance records source IDs, dimensions and SHA256 hashes. The four landscape images retain 1920×1280; Five Moats retains 1344×1792 and uses a 680px maximum display width. English pixels are preserved, with updated EN/PT/ES captions, alt text and long descriptions.

Source versus implementation at matching scale was inspected in `qa/swiss-comparison-1.png`, `qa/swiss-comparison-3.png` and `qa/swiss-comparison-5.png`. Actual-page checks include `qa/swiss-home-desktop.png`, `qa/swiss-memos-pt-mobile.png` and `qa/swiss-memos-pt-mobile-full.png`. At 1024px desktop and 390px mobile, images retain their proportions without clipping or horizontal overflow. The portrait figure and translated caption fit on the mobile display. Spanish Thesis retains three figures and the correct locale, with no horizontal overflow. No browser errors were observed.

The build validates all 24 content/error pages, 16 legacy destinations and 63 public files. Only nine figure-bearing pages and five figure assets change in the preview bundle. An independent review checked all 27 rendered figure occurrences, dimensions, provenance and the release allowlist. No form, privacy, tracking, backend or unrelated business-copy changes were made.

No actionable P0/P1/P2 findings remain in this scope.

Final result: passed


## Final native figure system

Latest visual truth: https://www.meta.ai/share/a/19d0d284-7e7b-49a4-8740-c8db183b536e. Supporting final illustration reference: https://meta.ai/share/c/hhkUckNd5X. This replaces the preceding raster sets, while retaining the existing site layout and Paul's approved business/privacy manuscripts. Only the personal-site section of the supplied two-site artifact is used.

The live Meta artifact was opened and all five native cards inspected. Captured source DOM, compiled styles and desktop screenshots are stored privately under `qa/native-source-*` and `qa/native-reference-desktop-{1,2,3,4,5}.png`. The five cards were also rendered locally from that captured static DOM and styles, without source scripts, runtime, external fonts or account data. All source SVG shapes are retained; three copied arrowheads support the narrow flywheel sequence. Source fonts are self-hosted.

### Comparison evidence and normalization

- `qa/native-comparison-desktop-{1,2,3,4}.png` and `qa/native-comparison-desktop-5-fixed.png` compare source and implementation in the same image, in two 1000px-wide iframe viewports at 1× density. Full-view screenshots are 2040×1461 pixels.
- `qa/native-comparison-mobile-{1,2,3,4,5}.png` compares two 390px-wide iframe viewports at 1× density. Focused captures for 1/2/3/5 are 840px wide, retaining both full component columns. The flywheel full-view capture is 1280×1861. These fixed iframe viewports provide reproducible responsive source/implementation widths independently of the outer browser window.
- The source and implementation use the same locally hosted Instrument Serif, Inter and JetBrains Mono. Plain source card markup preserves the source media-query behavior; implemented styles use container queries to accommodate existing narrow homepage columns.
- `qa/native-responsive-matrix.json` records 45 rendered checks: all five diagrams × EN/PT/ES × 360/454/1000px. Every case has no horizontal overflow, no flywheel-node overlap, and decorative SVGs hidden from screen readers.

### Required fidelity surfaces

Fonts/typography: source families, weights, thin serif hierarchy, mono labels and editable/selectable HTML text are retained. Copy is translated throughout each diagram rather than being embedded in English pixels. The rest of the site continues to use its existing Playfair Display and Instrument Sans.

Spacing/layout: source desktop composition, thin dividers, SVG geometry, 16px card radii and generous whitespace are retained. Narrow cards use 20–24px padding; long labels wrap. The flywheel becomes a sequential four-pill diagram on narrow containers because the source circular arrangement overlaps at 390px. The source circle remains on sufficiently wide cards. Moat marker icons stack at narrow sizes to make room for text. Technical source footers, token annotations and line-width labels are intentionally omitted from public diagrams; concise translated captions remain. Figure numbers follow existing site order.

Colors/tokens: paper #FAFAF8, ink #111, stone #E8E2D9 and alternating #F2EEE6 strata are preserved. No blue or terracotta is introduced. Heavy figure shadows are removed. The source's deliberately faded Trust column remains visually distinct from Proof.

Asset quality: figures contain static HTML and original SVG paths, no figure raster images. Fonts load from local WOFF2 assets with license files. Source React code, dynamic scripts, iframes and remote imports are excluded from the release.

Copy/content: all 108 source text nodes are translated for EN/PT/ES with escaped substitutions. Design-only phrases and the source's illustration-generation notes are removed; no business locale dictionaries, privacy details, form behavior or project states are changed.

### Comparison history and verification

The first desktop comparison found one P2 mismatch: source inline row fills had been removed during sanitization, leaving Five Moats without alternating stone layers. Explicit odd/even scoped backgrounds restore #FAFAF8/#F2EEE6; `qa/native-comparison-desktop-5-fixed.png` confirms the correction. Source h3 headings converted to in-figure h4 are included in the component reset to prevent host heading margins.

The actual homepage was opened separately at 1280px; body typography remained unchanged, five native diagrams rendered, no old infographic image references remained, and no app-origin console errors or horizontal overflow appeared. A 390px iframe of the actual Portuguese homepage also showed all five diagrams without horizontal overflow; the mobile menu opened/closed, and switching to Spanish preserved the Thesis anchor and changed the native diagram copy.

The build validates 24 content/error pages, 16 legacy destinations and 71 public files. An independent review confirms all native CSS selectors are scoped, templates contain no unsafe active elements/events/external links, SVG geometry matches the source, substitutions are escaped, and the five old rasters plus source/provenance/QA remain outside the release. After formal-origin regeneration, only the nine diagram-bearing HTML pages differ.

No actionable P0/P1/P2 findings remain.

Final result: passed


## Later minimal flywheel refinement — 19 October 2026

Source visual truth: Paul's later `https://meta.ai/share/c/2apkDwXuH5?utm_source=ios_cl`, supplied screenshot saved as `qa/minimal-flywheel-source.png` (3456 × 2234). The selected card is normalized through a browser crop to 1000 × 667 CSS px. This is a composition adaptation to the existing personal site, preserving its paper/ink/stone palette and fonts. The blue arrow color belongs to the Skaler reference and intentionally becomes ink here.

Implementation: native `scripts/templates/native-figures/flywheel.html`, scoped `assets/native-figures.css`, localized `content/native-figure-copy.json`. Source and implementation are rendered together in `qa/minimal-flywheel-comparison-final.jpg`, each in a fixed 1000px iframe at 1× density. Final mobile/tablet evidence: `qa/minimal-flywheel-mobile-tablet.jpg`, with 360px PT, 390px ES and 720px ES fixed-width frames. No mobile source was supplied; the narrow linear reading order is an intentional responsive adaptation.

Comparison history:
- Initial comparison: [P2] heading sat against the right edge instead of centered over the loop. Evidence: `qa/minimal-flywheel-comparison.jpg`.
- Fix: centered the desktop heading in a three-column grid, bounded role text to 24ch and preserved the labels outside the loop.
- Post-fix comparison: `qa/minimal-flywheel-comparison-final.jpg`; heading centered, four dots and arrows visible, labels clear. No actionable P0/P1/P2 differences remain.

Required fidelity surfaces:
- Fonts/typography: self-hosted Instrument Serif italic heading, JetBrains Mono 12px labels and 11px center, Inter 12–13px roles. Native text is crisp; the source's baked-in raster text is intentionally not reused.
- Spacing/layout rhythm: one paper card, generous whitespace, open center, no nested pills or icon badges. Grid cells bound translated side labels; mobile follows 01–04 in source order.
- Colors/tokens: #FAFAF8 paper, #111111 ink, #E8E2D9 stone lines, 16px corner radius. No blue or heavy shadows introduced.
- Image quality/assets: native circle, dots and arrows remain sharp at all tested widths; decorative SVG is hidden from assistive technology. Other four original native illustrations retain their approved structures.
- Copy/content: four role descriptions follow the final manuscript and latest reference in EN/PT/ES. No business locale, privacy or form behavior changes.

Browser geometry checks: `qa/minimal-flywheel-responsive-matrix.json` records 36 cases, EN/PT/ES at 320, 360, 390, 454, 640, 719, 720, 739, 740, 768, 1000 and 1280px. All passed horizontal overflow, card containment, header overlap, pairwise label/center overlap and decorative SVG checks. Full 1000px source/implementation regions make every label, dot and center text readable, so no additional focused crop is needed.

Independent review: no active code, external asset references, unsafe substitutions, duplicate marker IDs or unscoped CSS changes. All 15 flywheel text tokens resolve in every language. Build validation passed all 71 public files and 24 content/error pages.

Final result: passed


Final integration check found and fixed [P2] square paper corners around rounded cards in the dark Thesis section. The native wrapper now has the same 16px radius as the inner card; layout dimensions and label positions are unaffected. Final live evidence is `qa/minimal-flywheel-live-proof.jpg`. The fresh formal-site browser reported no warnings or errors. The official domain and stable preview both served all seven changed public files with exact SHA1 matches (`qa/minimal-live-verification.json`).

Final result: passed

## Owner-marked text cleanup and operator wording · 2026-10-20

Removed the header identity subtitle, Architect/location hero badge, standalone Skaler/Venture Studio principle sublabel, and all five external diagram captions with their FIG number badges. The shared header and figure renderer apply these removals to English, Portuguese and Spanish, including standalone Thesis and Memos pages. Internal diagram headings, SVGs and substantive diagram text remain. The portrait caption remains separate.

Changed the About profile descriptor and repeated introduction from Dutch founder to Operator in English and Operador in Portuguese/Spanish, on the homepage and standalone About pages. Other approved business copy, metadata, privacy text, forms and navigation are preserved.

Validation: the build passed 24 content/error pages, 16 legacy destinations and the 71-file release allowlist. Browser checks covered all 21 content pages at 1280px and 390px (42 cases), with no removed labels/captions, superseded profile wording, WhatsApp/Meta AI references or horizontal overflow. All six home/About pages display Operator/Operador at both widths. Evidence: `qa/red-block-operator-browser-checks.json`, earlier hero captures `qa/red-block-home-desktop.jpg` and `qa/red-block-home-mobile.jpg`.

Build guards reject reintroduced identity/badge/sublabel markup, external native-diagram captions and superseded profile wording. Negative injection checks confirmed rejection, followed by a clean build (`qa/red-block-regression-check.json`, `qa/operator-regression-check.json`). `AGENTS.md` records the owner's presentation constraints for future changes. The native-copy provenance now records the caption removal; no private source or QA files are published.
