# Fonts

`resuxjs/fonts` is Resux's modern font engine. It combines zero-config automatic font scanning, local self-hosting, Fontaine-powered zero-CLS fallback metric overrides, semantic named weights, variable font axes, and multi-provider font delivery.

## Key Capabilities

- **Zero-CLS Metric Overrides:** Integrates `fontaine` to calculate and emit fallback `@font-face` rules with `size-adjust`, `ascent-override`, and `descent-override` so your fallback font occupies the exact same dimensions as your web font—eliminating Cumulative Layout Shift (CLS).
- **Zero-Config Scanning (`autoScan`):** Integrates `fontless` to automatically discover `font-family` declarations in your CSS and templates, downloading and self-hosting the necessary font files during the Vite build.
- **Semantic Named Weights:** Normalizes semantic weight strings (e.g. `'thin'`, `'light'`, `'regular'`, `'semibold'`, `'bold'`, `'black'`) alongside numeric values (100–900) and range strings (`'100..900'`).
- **Variable Font Axes:** Full support for arbitrary variable font axes (`axes: { wght: 700, wdth: 100 }`).
- **Multi-Provider Architecture:** Seamlessly supports Google Fonts, local self-hosted files, and provider integrations (Google, Bunny, Fontshare, Fontsource, local).

## Enable the module

```ts
// resux.config.ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      autoScan: true, // Automatically scan and self-host fonts with fontless
      families: [
        {
          name: 'Inter',
          weights: ['regular', 'bold'], // Semantic named weights
          fallbacks: ['Arial', 'sans-serif'], // Fontaine zero-CLS metrics
          variable: '--font-inter',
        },
        {
          name: 'CustomBrand',
          provider: 'local',
          src: '/fonts/custom-brand.woff2',
          weight: 'normal',
          style: 'normal',
        }
      ]
    }]
  ]
})
```

Then use the family in normal CSS:

```css
:root {
  font-family: var(--font-inter, 'Inter', 'Inter fallback: Arial', system-ui, sans-serif);
}
```

## Fontaine Zero-CLS Fallbacks

When `fallbacks` are specified on a font family:

```ts
{
  name: 'Inter',
  weights: [400, 700],
  fallbacks: ['Arial']
}
```

Resux invokes `fontaine` at build time to inspect the font metrics of the primary font and generate an adjusted fallback `@font-face` rule:

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

This prevents layout shifts and content jumping while web fonts load over the network.

## Semantic Named Weights

You can specify font weights using numbers, range strings, or semantic names:

| Semantic Name | Numeric Weight |
| --- | --- |
| `'thin'`, `'hairline'` | `100` |
| `'extralight'`, `'extra-light'`, `'ultralight'` | `200` |
| `'light'` | `300` |
| `'normal'`, `'regular'` | `400` |
| `'medium'` | `500` |
| `'semibold'`, `'semi-bold'`, `'demibold'` | `600` |
| `'bold'` | `700` |
| `'extrabold'`, `'extra-bold'`, `'ultrabold'` | `800` |
| `'black'`, `'heavy'` | `900` |

## Loading strategies

For remote and Google fonts, the module supports:

| Strategy | Result |
| --- | --- |
| `eager` | Adds stylesheet/font links immediately into server head output. Default. |
| `preload` | Emits `rel="preload" as="style"` alongside normal links for high-priority delivery. |
| `lazy` | Defers font stylesheet attachment until after `window.load` (or immediately if already loaded). |

## Type-safe family helpers

Resux exports helper functions for type safety when defining families:

```ts
import { googleFont, localFont } from 'resuxjs/fonts'

const inter = googleFont({
  name: 'Inter',
  weights: ['regular', 'bold'],
  display: 'swap',
  fallbacks: ['Arial']
})

const branding = localFont({
  name: 'BrandHeading',
  src: '/fonts/brand.woff2',
  weight: 'bold'
})
```

## Related

- [Configuration](./configuration.md)
- [Performance and Zero-CLS](./performance.md)
- [CSS and Tailwind](/guide/css-tailwind)
