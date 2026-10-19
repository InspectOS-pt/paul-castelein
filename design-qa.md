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

The 1240px container, 24/32px gutters, 42/64/74px hero scale, 1.2/.8 hero split, two-by-two portfolio, three cooperation columns, dark Thesis, nested third figure, framed flywheel, economics cards, Memos rows and About/contact placement match the source structure. The five original 1920×1280 posters are byte-identical to the supplied reference assets. Stone palette, borders, radii and source figure shadows are retained.

## Intentional practical differences

- EN/PT/ES navigation and translated body copy from Paul's final attachments.
- Keyboard-operable mobile menu, Escape/selection dismissal, skip link and reduced-motion handling. The menu breakpoint accommodates the language switcher without overlap.
- Real rounded Paul portrait replaces the reference's PC placeholder.
- Original English diagrams have localized captions, alt text and full descriptions. Caption text is concise; image pixels remain the supplied originals.
- Source copy's lost compound hyphens stay corrected. The unwanted credentials comparison remains removed as Paul requested.
- Homepage contact action leads to the existing introduction form with an accurate action label. The form prepares a local email draft; it does not submit an enquiry.
- Venture titles preserve working project destinations. Existing deep URLs, review privacy notice and preview indexing restrictions remain available.
- Fonts and figures are self-hosted rather than importing a third-party runtime or font service.

## Functional checks and resolved findings

- Build validates all 21 content pages, 3 error pages, 16 legacy destinations, resource paths, one H1, language alternates and metadata.
- Homepage anchors resolve in all three languages.
- Widths 360, 390, 900, 1024 and 1440 checked. No horizontal overflow or duplicated desktop/mobile navigation in the tested home/contact layouts.
- Sticky header remains at y=0 after scrolling to About; real 400px source portrait loads normally.
- Mobile menu opens, follows a section and closes. Capital contact starting point is selected correctly. Empty required fields show localized errors. Valid local inputs generate the expected mailto draft without a server form action.
- No app-origin JavaScript console errors observed.
- Fixed during review: malformed removal of the external font import, inaccurate homepage draft label, inherited tablet menu breakpoint, Spanish description punctuation and formal contact-note register.

No unresolved P0, P1 or P2 design or functional findings in this scope. Formal company-account deployment, DNS and missing privacy-controller facts remain separately deferred as previously agreed.
