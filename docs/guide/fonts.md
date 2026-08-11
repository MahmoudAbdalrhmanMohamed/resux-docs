# Fonts (`resuxjs/fonts`)

The deep font documentation now lives in the dedicated [Fonts](/fonts/) section:

- [Overview](/fonts/)
- [Configuration and TypeScript API](/fonts/configuration)
- [Performance, privacy and CSP](/fonts/performance)

This guide URL remains available so existing links continue to work.

## Current first-party scope

`resuxjs/fonts` is a **Google Fonts stylesheet loader**. It supports family names, weight/range normalization, `font-display`, preconnect, eager/preload/lazy strategies, per-family strategy overrides, and public runtime metadata.

It does **not** currently provide local/self-host font discovery, provider plugins, generated `@font-face`, fallback metric generation, CSS-variable generation, or downloaded font caching.

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      google: [
        { name: 'Inter', weights: ['100..900'], display: 'swap' }
      ]
    }]
  ]
})
```

See [Performance and CSP](/fonts/performance) before using deferred loading.
