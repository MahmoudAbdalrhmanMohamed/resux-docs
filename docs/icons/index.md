# Icons

`resuxjs/icons` is Resux's modular icon system with **Nuxt Icon parity**, compile-time SVG inlining, offline icon packages, CSS mode, and custom local SVG support.

## Key Features

- **Nuxt Icon Parity:** Use any icon from 200,000+ icons across 150+ icon sets using standard Iconify syntax: `<Icon name="lucide:check" />`, `<Icon name="ph:check-circle" />`, or built-in shortcuts like `<Icon name="check" />`.
- **Compile-Time Inlining:** When icons are statically named and available at build time, Resux's Vite plugin compiles them directly into static inline `<svg>` markup with **0 B runtime JavaScript**.
- **Offline Collections:** Install `@iconify-json/<collection>` packages (e.g. `@iconify-json/lucide`) to serve icons completely offline without making external network calls.
- **Pure CSS Mode:** Support for `mode="css"`, which renders icons using CSS `mask` and `background-color: currentColor`. This produces ultra-lightweight DOM nodes with zero inline SVG overhead.
- **Custom Local SVGs:** Drop custom `.svg` files into your project's `./assets/icons/` directory and use them instantly via `<Icon name="custom:my-logo" />`.
- **Universal Component:** Auto-imported `<Icon>` (with alias `<ResuxIcon>`) that renders seamlessly during server-side rendering and client interaction.

## Basic usage

```vue
<template>
  <!-- Iconify collection icon -->
  <Icon name="lucide:mail" size="1.5rem" />

  <!-- Pure CSS mask mode -->
  <Icon name="lucide:sparkles" mode="css" />

  <!-- Custom local SVG from ./assets/icons/logo.svg -->
  <Icon name="custom:logo" size="2rem" />

  <!-- Built-in shortcut alias -->
  <Icon name="check" />
</template>
```

## Enable the module

Enable `resuxjs/icons` in your `resux.config.ts`:

```ts
// resux.config.ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/icons', {
      defaultSize: '1.25rem',
      mode: 'svg', // 'svg' or 'css'
      collections: ['lucide', 'ph'],
      aliases: {
        github: 'lucide:github',
        twitter: 'lucide:twitter',
      }
    }]
  ]
})
```

## Rendering Modes: SVG vs CSS

Resux supports two distinct rendering modes:

### 1. SVG Mode (`mode="svg"`, Default)

Renders full SVG elements with paths, strokes, and fills. Ideal for multi-color icons, gradients, and precise vector geometry.

```vue
<Icon name="ph:heart" mode="svg" />
```

### 2. CSS Mode (`mode="css"`)

Renders a lightweight `<span>` using CSS `mask-image` and `background-color: currentColor`. Perfect for monochromatic UI icons where minimal DOM footprint and color inheritance are desired.

```vue
<Icon name="lucide:arrow-right" mode="css" />
```

## Offline Collections (`@iconify-json/*`)

To use icons without relying on the public Iconify API at runtime:

1. Install the collection package as a dependency:
   ```sh
   npm install -D @iconify-json/lucide
   ```
2. Resux automatically loads icon data directly from the installed package during compilation and SSR.

## Custom Local SVG Icons

Place SVG files into your project's icon directory (defaults to `./assets/icons/`):

```txt
assets/icons/
  logo.svg
  brand/
    mark.svg
```

Reference them in templates:

```vue
<Icon name="custom:logo" />
<Icon name="custom:brand/mark" />
```

Resux parses the local SVG file, preserves viewBox and clean vector attributes, and inlines it safely.

## Related

- [Usage and Registry](./usage.md)
- [Configuration](./configuration.md)
- [Runtime Loading and SSR](./runtime.md)
- [UI Icon Primitive](/components/icon)
