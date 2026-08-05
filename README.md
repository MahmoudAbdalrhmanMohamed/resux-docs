# Resux Documentation

VitePress documentation for the complete Resux framework surface.

The site covers:

- architecture, compiler, SSR, resumability, routing, layouts, state, async data, and errors,
- the `rx-*` template language, official `@event` / `:binding` shortcuts, and `v-*` migration compatibility,
- how Resux uses Vue compiler packages without hydrating normal Resux components,
- plugins, middleware, server APIs, modules, Kit, hooks, generated templates/types, and route rules,
- third-party package modes, client enhancements, Vue islands, UI, icons, fonts, i18n, media, CSS, and Tailwind,
- create templates/features, CLI commands, targeted inspection, diagnostics, testing, deployment, release automation, security, and Halal Core,
- examples for counters, routes, APIs, authentication, progressive packages, media, and Docker.

## Source alignment

The `rx-*` documentation update is aligned with `MahmoudAbdalrhmanMohamed/resux` branch `feat/rx-directive-branding` at commit `ac6fcdf29c58051fe553801e3393124f51bcd888` and pull request `#9`.

The framework change must be merged and released before the new syntax is considered available in a published `resuxjs` version. `@event` and `:binding` are first-class shortcuts for `rx-on:event` and `rx-bind:binding`; existing `v-*` syntax remains documented as migration compatibility.

Documentation changes should identify the framework branch, commit, pull request, or release used as the source of truth.

## Local development

```sh
npm ci
npm run dev
```

## Validate

```sh
npm run build
```

The repository includes Documentation CI for pushes and pull requests.

## Deployment

The VitePress site is configured for GitHub Pages under `/resux-docs/`.
