# Icons Module (`resuxjs/icons`)

The `resuxjs/icons` module provides high-performance icon resolution, dynamic SVG fetching, and viewport visibility lazy loading for Resux applications.

## Overview

- **Zero-hydration icon rendering**: Icons are rendered as native `<svg>` elements on the server during SSR and patched efficiently in the client DOM.
- **Dynamic Iconify API Integration**: Supports resolution of 150,000+ icons from open icon sets via `https://api.iconify.design/{prefix}/{name}.svg`.
- **Pre-populated Icon Registry**: Common UI icons are bundled directly in memory for zero-latency initial renders.
- **Viewport IntersectionObserver Lazy Loading**: Off-screen icons can defer dynamic vector fetching until scrolled into view.

## Quick Start

Enable the icons module in `resux.config.ts`:

```ts
export default defineResuxConfig({
  modules: [
    ["resuxjs/icons", {
      component: "Icon",
      mode: "svg",
      collections: [
        "material-symbols",
        "mdi",
        "mingcute",
        "cib",
        "uil",
        "line-md",
        "solar",
        "ph",
        "gg"
      ],
      lazy: true
    }]
  ]
})
```

## Built-in `<Icon>` and `<ResuxIcon>` Component

Use `<Icon>` or `<ResuxIcon>` directly in Vue SFC templates without manual imports:

```vue
<template>
  <div class="flex items-center gap-2">
    <!-- Eager / Pre-registered Icon -->
    <Icon name="material-symbols:call" size="1.5rem" class="text-blue-500" />
    
    <!-- Dynamic Iconify Icon -->
    <Icon name="ph:check-circle-thin" size="2rem" />
    
    <!-- Viewport Visibility Lazy Loaded Icon -->
    <Icon name="solar:leaf-outline" size="2rem" lazy />
  </div>
</template>
```

## Component Props

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `string` | **Required** | Icon name specifier in `{prefix}:{name}` or short format (e.g. `material-symbols:call`, `ph:check-circle-thin`). |
| `size` | `string \| number` | `"1.25rem"` | Width and height of the SVG element (number values are converted to `px`). |
| `mode` | `"svg" \| "css"` | `"svg"` | Rendering mode. |
| `lazy` | `boolean` | `false` | When `true`, defers fetching dynamic SVG paths until element enters viewport. |
| `loading` | `"eager" \| "lazy"` | `"eager"` | Loading priority strategy. |
| `class` | `string` | `""` | Utility CSS classes forwarded to the SVG element. |

## Dynamic Fetching

When an icon name is requested that is not yet in the in-memory `iconRegistry`, `resuxjs/icons` invokes `fetchIconifyIcon(name)`:

```ts
import { fetchIconifyIcon } from "resuxjs/icons"

// Fetch SVG icon definition dynamically
const iconData = await fetchIconifyIcon("ph:flower-lotus-thin")
```

Fetches are deduped globally so duplicate requests across components share a single inflight request.
