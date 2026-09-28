# Resux Documentation

This repository contains the official documentation site for **Resux**, a resumable web framework with Vue-like single-file components, server rendering, file-based routing, and an HTML-first runtime model.

Resux is currently in **public beta**. The current beta release is **0.4.0-beta.2**. It is ready for evaluation, real-world testing, demos, and non-critical applications, while APIs may still change before 1.0.

## Start here

- [Getting Started](docs/guide/getting-started.md)
- [Framework Tour](docs/guide/framework-tour.md)
- [Project Status](docs/reference/status.md)
- [API Reference](docs/reference/api-index.md)
- [Examples](docs/examples/index.md)

The site also includes dedicated guides for UI components, images and video, fonts, icons, i18n, routing, data fetching, Vue islands, deployment, security, and troubleshooting.

## Documentation principles

The framework source, package exports, and tests are the source of truth. The docs should explain the public behavior developers can actually use, including important limits and runtime costs, without copying features from other frameworks that Resux does not implement.

When possible, pages should answer practical questions: what the feature does, when to use it, where it runs, how to configure it, and what to watch out for.

## Local development

```sh
npm ci
npm run dev
```

Build the site with:

```sh
npm run build
```

Additional checks:

```sh
npm run check:navigation
npm run check:framework-parity -- .framework/resux
```

## Deployment

The documentation site is built with VitePress and deployed to GitHub Pages under `/resux-docs/`.
