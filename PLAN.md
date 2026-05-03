# Implementation Plan

This repository was prepared with the following plan.

## 1. Learn the product surface

Use the source repository and package metadata as the source of truth:

- Package name: `resuxjs`
- Current source package version used for these docs: `0.2.14`
- Runtime exports: main, node, globals, runtime, compiler
- CLI commands: `init`, `dev`, `build`, `compile`, `preview`, `start`, `inspect`, `deploy`
- App model: Vue-like SFC subset, file routing, SSR, resumable handlers, client-side route payload navigation, Vue islands as an opt-in escape hatch

## 2. Pick a docs architecture

Use VitePress because it is fast, static, familiar to Vue/Nuxt users, and fits a framework docs site.

Repository layout:

```txt
docs/
  .vitepress/
    config.ts
    theme/
  guide/
  reference/
  examples/
  public/
.github/workflows/deploy.yml
```

## 3. Build the information architecture

Create a polished docs experience similar to large framework documentation:

- Home page with hero, features, and install CTA
- Guide pages for the mental model and day-to-day usage
- Reference pages for exact CLI, file conventions, config, composables, runtime, compiler, and limits
- Example pages for common app patterns
- Brand page for logo and color palette

## 4. Design the brand

Create an original SVG logo and a consistent color system:

- Ink base for serious technical docs
- Electric violet and cyan for the resumability/runtime theme
- Mint and amber accents for status and highlights
- Dark-mode first design with high contrast

## 5. Implementation deliverables

- VitePress config and navigation
- Custom CSS theme
- Logo, mark, and Open Graph SVG assets
- Full markdown documentation
- GitHub Pages deployment workflow
- Upload-ready ZIP archive
