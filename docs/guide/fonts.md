# Fonts (`resuxjs/fonts`)

The deep font documentation lives in the dedicated [Fonts](/fonts/) section:

- [Overview](/fonts/)
- [Configuration and TypeScript API](/fonts/configuration)
- [Performance, Zero-CLS, and CSP](/fonts/performance)

This guide URL remains available so existing links continue to work.

## Modern Font Engine Scope

`resuxjs/fonts` provides:

- **Zero-config automatic scanning (`autoScan: true`):** Discovers `font-family` declarations across CSS and templates via `fontless`.
- **Zero-CLS fallback metric overrides:** Calculates and emits `@font-face` rules with `size-adjust`, `ascent-override`, and `descent-override` using `fontaine`.
- **Multi-provider font delivery:** Native support for Google Fonts, local self-hosted files, and custom font providers.
- **Semantic named weights & variable axes:** Weight normalization from `'thin'` to `'black'` and variable axis declarations (`axes: { wght: 700 }`).
- **Flexible loading strategies:** `eager`, `preload`, and `lazy` loading with automatic preconnect hints.

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      autoScan: true,
      families: [
        {
          name: 'Inter',
          weights: ['regular', 'bold'],
          fallbacks: ['Arial'],
          variable: '--font-inter',
        }
      ]
    }]
  ]
})
```

See [Font Performance and Zero-CLS](/fonts/performance) for best practices on Core Web Vitals and layout stability.
