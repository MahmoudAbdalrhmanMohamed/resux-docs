# Resux Documentation

VitePress documentation for the complete Resux framework surface.

The site covers:

- architecture, compiler, SSR, resumability, routing, layouts, state, async data, and errors,
- plugins, middleware, server APIs, modules, Kit, hooks, generated templates/types, and route rules,
- third-party package modes, client enhancements, Vue islands, UI, icons, fonts, i18n, media, CSS, and Tailwind,
- create templates/features, CLI commands, targeted inspection, diagnostics, testing, deployment, release automation, security, and Halal Core,
- examples for counters, routes, APIs, authentication, progressive packages, media, and Docker.

## Source alignment

Documentation changes must identify the framework source or release used as the source of truth. The current global audit is aligned with `MahmoudAbdalrhmanMohamed/resux` branch `audit/full-history-correctness` at commit `35f00b0ddb68b098cb1def4c59356f722c5db72b`.

Some documented changes depend on the corresponding framework pull request being merged and released.

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
