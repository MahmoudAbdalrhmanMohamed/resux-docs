# Font Performance and CSP

Font loading affects render timing, layout stability, privacy, and Content Security Policy. `resuxjs/fonts` gives you explicit loading strategies, but choosing a strategy still requires understanding the browser/network trade-off.

## `eager` (default)

The module adds a normal stylesheet link:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?...">
```

Use eager for families needed by the initial page when simplicity and early availability matter.

## `preload`

The module adds both:

```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?...">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?...">
```

The preload hints that the stylesheet is important; the stylesheet link still applies the CSS. Do not describe `preload` as deferred loading.

Use it selectively. Preloading too many styles competes with critical CSS, images, and scripts.

## `lazy`

The lazy/deferred path adds a stylesheet preload and an inline script that installs the stylesheet after the window `load` event. If the document is already complete, it attaches immediately.

This can keep non-critical fonts out of the initial critical path, but it has consequences:

- it requires browser JavaScript;
- text will initially use fallback fonts;
- font swapping can change metrics/layout;
- strict CSP can block the inline loader;
- a failure after page load can leave the fallback in use.

Use lazy for genuinely secondary typography, not as a blanket optimization.

## Weight budget

Request only weights you use:

```ts
{ name: 'Inter', weights: [400, 600, 700] }
```

Variable ranges such as `100..900` can be appropriate when the family/provider returns an efficient variable font, but “one range” is not automatically smaller than a carefully selected set for every family/browser/provider response. Measure real transfer sizes.

## `display`

For many interfaces, `swap` is a reasonable default because text remains visible while the web font loads. `optional` can be useful when avoiding late swaps matters more than always using the web font. The right choice depends on typography and product requirements.

## CSP

Google-hosted fonts usually require policy access comparable to:

```txt
style-src https://fonts.googleapis.com
font-src https://fonts.gstatic.com
```

The lazy/deferred strategy also relies on an inline script. Under a strict CSP, use a nonce/hash-compatible setup or choose an eager/preload path that does not require the inline loader. Do **not** weaken the entire application's CSP with a broad `unsafe-inline` just for fonts.

## Privacy and offline use

This module's current design makes browser requests to Google-hosted font infrastructure. If policy requires no third-party requests:

1. self-host the font files as application assets;
2. declare your own `@font-face` in CSS;
3. preload only the critical local files you actually need;
4. do not enable the Google Fonts module for those families.

That is an application pattern today, not an undocumented local-provider feature of `resuxjs/fonts`.

## Layout stability

The module does not currently generate fallback font metrics. If font swapping causes visible layout changes, choose fallback fonts with similar metrics, consider local/self-hosted strategies, and measure CLS on real pages.

## Checklist

- Configure only used families/weights.
- Keep `preconnect` unless you already manage it or do not use Google families.
- Use eager for initial typography unless measurement supports another choice.
- Preload selectively.
- Use lazy only for secondary typography.
- Set a deliberate `display` value.
- Verify CSP in production, not just dev mode.
- Measure font transfer, FCP/LCP, and CLS.
- Self-host when privacy/offline/reliability requirements demand it.

## Related

- [Fonts overview](./index.md)
- [Configuration](./configuration.md)
- [CSS and Tailwind](/guide/css-tailwind)
- [Security and Caching](/guide/security-caching)
