# Fonts Module (`resuxjs/fonts`)

The `resuxjs/fonts` module manages web font optimization, Google Fonts URL normalization, preconnect headers, and deferred font loading after page load for maximum Core Web Vitals performance.

## Overview

- **Automatic Preconnect Optimization**: Injects `<link rel="preconnect">` for Google Fonts domains.
- **Configurable Priority Strategies**: Choose between `eager`, `preload`, or `lazy` font loading globally or per font family.
- **Per-Font Granular Control**: Load critical primary fonts as fast as possible (`eager` or `preload`) while lazy-loading non-critical secondary fonts post page load.
- **Post-PageLoad Font Deferral**: Defer non-critical font stylesheets until after `window.onload` or `requestIdleCallback` to improve initial First Contentful Paint (FCP) and Largest Contentful Paint (LCP).

## Configuration

Add font families to `resux.config.ts`. You can specify global defaults and optionally override loading strategies per font:

```ts
export default defineResuxConfig({
  modules: [
    ["resuxjs/fonts", {
      preconnect: true,
      strategy: "lazy",
      deferUntilPageLoad: true,
      google: [
        // Critical font: loads eagerly as fast as possible without page-load deferral
        { name: "Inter", weights: [400, 500, 600, 700, 800], display: "swap", strategy: "eager" },
        // Secondary font: inherits module default (lazy / deferred until window load)
        { name: "Alexandria", weights: [300, 400, 500, 600, 700], display: "swap" }
      ]
    }]
  ]
})
```

## Options Reference

### Module Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `google` | `ResuxFontFamilyInput[]` | `[]` | Array of Google Font family descriptors (`name`, `weights`, `display`, `strategy`, `deferUntilPageLoad`). |
| `preconnect` | `boolean` | `true` | Injects preconnect hints for `https://fonts.googleapis.com` and `https://fonts.gstatic.com`. |
| `strategy` | `"eager" \| "preload" \| "lazy"` | `"eager"` | Default loading strategy for stylesheet loading. |
| `deferUntilPageLoad` | `boolean` | `false` | Default flag deferring font stylesheet injection until window load on the client. |

### Per-Font Options (`ResuxFontFamilyInput`)

| Property | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `string` | *(Required)* | Name of the Google Font family (e.g. `"Inter"`). |
| `weights` | `(number \| string)[]` | `[]` | Font weight variants to request (e.g. `[400, 700]`). |
| `display` | `"auto" \| "block" \| "swap" \| "fallback" \| "optional"` | `"swap"` | `font-display` CSS descriptor. |
| `strategy` | `"eager" \| "preload" \| "lazy"` | Inherited | Per-font override for loading strategy. |
| `deferUntilPageLoad` | `boolean` | Inherited | Per-font override for post-load deferral. |

## How Per-Font Loading & Deferral Work

When mixing eager and lazy font configurations:

1. **Font Grouping**: Resux automatically partitions configured fonts into **eager/critical** and **lazy/deferred** groups.
2. **Eager Group (Fastest Load)**: Fonts configured with `strategy: "eager"` or `strategy: "preload"` generate an immediate `<link rel="stylesheet">` or `<link rel="preload">` in `<head>` so the browser downloads critical text fonts immediately during page render.
3. **Lazy Group (Deferred Load)**: Deferred fonts receive a non-blocking `<link rel="preload" as="style">` in `<head>` and a lightweight inline controller script attaches full `<link rel="stylesheet">` after window load (`window.onload`).
4. **Preconnect Reuse**: Single shared `<link rel="preconnect">` hints are attached once, serving both eager and lazy font groups without duplicate HTTP handshakes.

