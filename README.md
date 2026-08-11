# Resux Documentation

**Resux** stands for **Resumability + User Experience (UX)**.

This repository contains the VitePress documentation for the Resux framework. The documentation site is the deep reference; the framework README is an introduction and entry point.

## Documentation structure

The site covers the full public framework surface, including:

- getting started, project structure, compiler/template behavior, SSR, resumability, routing, layouts, state, async data and errors;
- plugins, middleware, server APIs, modules, Kit, hooks, configuration, generated templates/types and package integration;
- a dedicated [UI component catalog](docs/components/index.md) with one page per public `resuxjs/ui` component;
- dedicated [images/media](docs/media/index.md), [fonts](docs/fonts/index.md) and [icons](docs/icons/index.md) sections;
- i18n, CSS/Tailwind, Vue islands, testing, security, deployment, release behavior and troubleshooting;
- examples and API/package references.

## Source alignment

The framework implementation is the source of truth. Documentation must be verified against `MahmoudAbdalrhmanMohamed/resux` source, exports and tests before a prop, event, default, slot, behavior, runtime boundary or configuration option is documented.

Do not pin this README to a historical feature branch or old pull request. Date-stamped audit pages may preserve historical evidence, but living documentation should track the current framework implementation.

The [Public API Documentation Coverage](docs/reference/coverage.md) page maps package entry points to their primary documentation and records focused coverage expectations.

## Documentation conventions

- Explain why/when, not only syntax.
- Keep Resux resumability and explicit client/runtime boundaries visible.
- Do not describe Vue UI components as zero-hydration Resux primitives.
- Do not invent functionality to match another framework's documentation.
- Document limitations explicitly when the implementation does not provide a complete behavior.
- Prefer dedicated pages and cross-links over one giant catch-all reference.

## Local development

```sh
npm ci
npm run dev
```

## Validate

```sh
npm run build
npm run check:links
```

`check:links` currently uses the VitePress production build, so broken internal routes/anchors discovered by VitePress fail the same build path.

## Deployment

The VitePress site is configured for GitHub Pages under `/resux-docs/`.
