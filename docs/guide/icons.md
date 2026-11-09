# Icons (`resuxjs/icons`)

The deep icon documentation lives in the dedicated [Icons](/icons/) section:

- [Overview](/icons/)
- [Usage, Inlining, and Registry](/icons/usage)
- [Configuration and Aliases](/icons/configuration)
- [Runtime Loading and Resolution](/icons/runtime)

This guide URL remains as a stable entry point for existing links.

## Modern Icon System

`resuxjs/icons` provides **Nuxt Icon parity** and zero-overhead performance:

- **Nuxt Icon Parity:** Drop-in syntax compatibility (`<Icon name="lucide:check" />`, `<Icon name="ph:check-circle" />`, `<Icon name="mail" />`).
- **Compile-time Inlining:** Known static icons are transformed directly into inlined `<svg>` markup during Vite compilation with 0 B runtime JavaScript.
- **Offline Collections:** Bundles `@iconify-json/*` icon packages for offline/air-gapped rendering without external network requests.
- **CSS Mode:** Renders icons via CSS `mask` / `background` for ultra-lightweight, color-inheriting icons.
- **Custom Local SVGs:** Load custom SVG icons directly from your project's `./assets/icons` directory via `custom:*`.

```vue
<template>
  <!-- Auto-imported or explicit Icon component -->
  <Icon name="lucide:check" size="1.25rem" />
  <Icon name="ph:check-circle" mode="css" />
  <Icon name="custom:logo" />
</template>
```

See [Icon Usage and Registry](/icons/usage) for full props and syntax details.
