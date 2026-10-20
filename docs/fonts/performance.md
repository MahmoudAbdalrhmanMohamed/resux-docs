# Font Performance, Zero-CLS, and CSP

Font loading affects Core Web Vitals (specifically Cumulative Layout Shift and Largest Contentful Paint), render timing, privacy, and Content Security Policy. `resuxjs/fonts` provides built-in tools to achieve zero-CLS layout stability and fast delivery.

## Zero-CLS with Fontaine Metric Overrides

When web fonts load, the browser initially renders text using a local fallback font (such as Arial or Georgia). Because fallback fonts have different character widths, ascents, and descents, swapping to the loaded web font causes the page layout to shift—negatively impacting **Cumulative Layout Shift (CLS)**.

Resux solves this by integrating **`fontaine`**. When you declare `fallbacks` on a font family:

```ts
// resux.config.ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      families: [
        {
          name: 'Inter',
          weights: [400, 700],
          fallbacks: ['Arial', 'sans-serif'],
          variable: '--font-inter',
        }
      ]
    }]
  ]
})
```

At build time, Resux analyzes the exact metrics of `Inter` and emits a metric-adjusted fallback `@font-face`:

```css
@font-face {
  font-family: 'Inter fallback: Arial';
  src: local('Arial');
  ascent-override: 90.49%;
  descent-override: 22.62%;
  line-gap-override: 0%;
  size-adjust: 107.41%;
}
```

Because the fallback font occupies the exact same bounding box as the web font, **Cumulative Layout Shift is virtually eliminated (CLS = 0)**.

## Self-Hosting with `fontless` (`autoScan`)

By default, `autoScan: true` is enabled via `fontless`. It automatically scans your components and CSS for `font-family` references, downloads web fonts into your build assets, and generates local `@font-face` definitions.

Benefits of local self-hosting:
- Eliminates third-party network connections and DNS lookups to external font providers.
- Fully GDPR / privacy compliant (no user IP addresses leaked to external CDNs).
- Works completely offline and in air-gapped environments.
- Protects against external CDN downtime.

## Loading strategies

### `eager` (default)

Adds a standard stylesheet link or `@font-face` declaration:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?...">
```

Use eager for families needed by the initial viewport when early availability matters.

### `preload`

Preloads the font file or stylesheet with high priority:

```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?...">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?...">
```

Preloading tells the browser to fetch the resource immediately, reducing the time before the primary web font is rendered.

### `lazy`

Defers font stylesheet attachment until after the `window.load` event. Use this exclusively for secondary or below-the-fold typography.

## Preconnect hints

When remote Google fonts are used, Resux automatically adds preconnect resource hints:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

This establishes early TCP and TLS connections to Google's font servers before stylesheet requests begin.

## Content Security Policy (CSP)

If using remote Google fonts, your CSP must permit connections to Google domains:

```txt
style-src https://fonts.googleapis.com
font-src https://fonts.gstatic.com
```

With `autoScan: true` or local self-hosting (`provider: 'local'`), all font assets are served directly from your application's origin, allowing strict `self` CSP rules:

```txt
style-src 'self'
font-src 'self'
```

## Checklist for Optimal Font Performance

1. **Use Fontaine Fallbacks:** Specify `fallbacks: ['Arial', ...]` on all key families to eliminate layout shifts (CLS).
2. **Self-Host Production Fonts:** Rely on `autoScan: true` or `provider: 'local'` for maximum privacy and zero third-party latency.
3. **Limit Weights:** Specify only the weights your designs actually utilize (`['regular', 'bold']`).
4. **Use `font-display: swap`:** Ensure text remains readable immediately while web fonts load.
5. **Preload Critical Fonts:** Use `strategy: 'preload'` for your hero or primary heading typography.

## Related

- [Fonts overview](./index.md)
- [Configuration](./configuration.md)
- [CSS and Tailwind](/guide/css-tailwind)
