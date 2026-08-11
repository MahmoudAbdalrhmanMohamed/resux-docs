# Documentation Implementation Plan

This repository documents Resux from the framework source and tests rather than from assumptions based on other frameworks.

## 1. Source of truth

Use the `MahmoudAbdalrhmanMohamed/resux` repository and package metadata as the implementation authority.

At the time this plan was refreshed:

- Package name: `resuxjs`
- Source package version: `0.3.3`
- Node engine: `>=20.19.0`
- Public package entries include: main, node, globals, runtime, reactivity, compiler, create, i18n, ui, icons, fonts, kit, core, halal, and package metadata.
- App model: focused Vue-like SFC syntax compiled into Resux SSR/resumability artifacts, file routing, server APIs, custom reactivity, client route payload navigation, client enhancements/package adapters, and explicit Vue islands as an opt-in runtime boundary.

The npm `latest` version can temporarily differ from repository `main`. User-facing release claims must verify the published/installed release separately.

## 2. Documentation architecture

VitePress is used for a static, searchable framework documentation site.

Repository layout:

```txt
docs/
  .vitepress/
    config.ts
    theme/
  guide/
  components/
  media/
  fonts/
  icons/
  reference/
  examples/
  community/
  public/
scripts/
.github/workflows/
```

## 3. Information architecture

The site should support several reading modes instead of forcing every user through one sequence.

### Beginner / application development

- What is Resux?
- Framework Tour
- Getting Started
- Core Concepts
- Components and Template Syntax
- State and Async Data
- Routing, Layouts, SEO, Runtime Config

### Deep architecture

- Architecture Deep Dive
- Request Lifecycle
- Resumability Deep Dive
- Code to Browser
- Debugging Mental Model
- Framework Source Map

### UI/design system

- Component catalog
- Component Anatomy
- one page per public UI component
- props, events, slots, root DOM, styling, accessibility, SSR/runtime cost, recipes, current limitations

### Media/assets

- image primitives
- responsive images
- optimization/providers/cache/security
- video
- fonts
- icons

### Platform/extension

- plugins
- middleware
- server APIs
- modules/Kit/hooks
- packages/client enhancements
- CSS/Tailwind
- generated types
- testing

### Operations/reference

- deployment
- security/caching
- Halal Core
- troubleshooting
- package/public API reference
- exact CLI/config/file conventions/limits
- source map and documentation coverage

## 4. Documentation depth standard

A page about an important framework feature should not stop after naming an API or showing one code snippet.

Where relevant, it should answer all of the following.

### Purpose

- What problem does the feature solve?
- When should it be used?
- When should another feature/native platform capability be used instead?

### Runtime ownership

- Does it run at build time, server request time, normal Resux browser resume time, client-enhancement time, or inside a Vue island?
- Does it add browser JavaScript?
- Is it server-only or browser-visible?

### Exact API

- import path,
- options/props/types,
- defaults,
- events/emits,
- slots,
- return values,
- supported variants/modes,
- forwarded/native attributes where relevant.

### Behavior

- what HTML/output is produced,
- how SSR behaves,
- what is serialized,
- how navigation/resume affects it,
- cleanup/lifetime behavior,
- caching/network behavior where relevant.

### Boundaries

- accessibility requirements,
- security/privacy concerns,
- serializability requirements,
- current implementation limitations,
- external runtime/tool dependencies.

### Learning material

- basic example,
- realistic complete example,
- common recipes,
- common mistakes,
- troubleshooting guidance,
- links to adjacent concepts.

### Source alignment

- source subsystem,
- useful tests/regression tests,
- clear distinction between public contract and private implementation detail.

Not every tiny API needs every heading, but major subsystems should be taught rather than merely listed.

## 5. UI component page standard

Each public `resuxjs/ui` component should have its own page that answers:

1. What does it render?
2. When should I use it?
3. What is its Vue runtime boundary/cost?
4. What are all props and defaults?
5. Which variant strings have verified built-in CSS?
6. What custom events are emitted?
7. What native listeners/attrs fall through?
8. Which slots exist?
9. Is state controlled, initialized once, or internally managed?
10. What does `unstyled` change?
11. What accessibility behavior exists in source?
12. What accessibility behavior is *not* provided?
13. How does SSR/browser mount behave?
14. What are realistic recipes and common mistakes?
15. What are the current limitations?

Component names must never be used to imply behavior the source does not implement.

## 6. Resux vs Vue boundary

The documentation must consistently explain:

- normal Resux `.vue`-style components are compiled by Resux and are not automatically full Vue-hydrated component trees,
- Resux uses its own reactivity/runtime/resumability model for normal components,
- `resuxjs/ui` is implemented with Vue `defineComponent()` and belongs in an explicit Vue runtime boundary,
- Vue islands are an opt-in integration/escape hatch,
- renderer primitives such as `ResuxImg`, `ResuxPicture`, and `ResuxVideo` are not `resuxjs/ui` components,
- the full SVG icon system lives under `resuxjs/icons`.

This distinction should appear anywhere a user might otherwise infer the wrong runtime model.

## 7. Media documentation standard

Image/video pages should cover more than component names. They should explain:

- source types (local/public/remote),
- generated native markup,
- width/height/aspect-ratio behavior,
- responsive candidates and browser selection,
- formats/quality/fit/modifiers,
- priority/preload/fetch priority,
- lazy/deferred behavior,
- placeholders/fallbacks,
- provider/cache configuration,
- remote source security,
- transformation endpoints,
- `sharp` dependency for image transformations,
- `ffmpeg` environment requirement where video transcoding is used,
- SSR/resumability/browser enhancement behavior.

## 8. Fonts and icons documentation standard

Fonts should explain configuration, generated CSS/head output, local/remote sources, preload behavior, performance, CSP, and deployment concerns.

Icons should explain registry resolution, providers/collections, caching, lazy/runtime loading, SSR behavior, SVG/security considerations, and the difference between the full `resuxjs/icons` system and the small `RxIcon` UI primitive.

## 9. Source mapping and parity

The docs repository includes `scripts/check-framework-parity.mjs`, which checks that public package specifiers from the framework export map appear in package/coverage docs.

Parity checking should continue to improve beyond export-name presence. Future checks may validate additional machine-readable inventories, but they must not create false guarantees that prose is correct merely because a symbol name appears in a Markdown file.

`docs/reference/source-map.md` is the human-oriented bridge between public packages, source directories, tests, and docs.

## 10. Visual/brand system

Keep the original Resux brand and a polished technical-docs experience:

- Ink base for serious technical docs
- Electric violet and cyan for resumability/runtime themes
- Mint and amber accents for status/highlights
- Strong light/dark contrast
- Searchable, structured navigation
- Deep-dive pages discoverable from the top navigation/home page

## 11. Quality gates

Before merging a substantial documentation update:

- compare claims against current framework source,
- inspect tests for subtle behavior,
- run framework/docs parity checks,
- build the VitePress site,
- catch broken internal links,
- verify navigation entries point to real pages,
- ensure examples do not use invented APIs,
- ensure runtime-boundary language is accurate,
- ensure version-specific claims are clearly scoped,
- review short pages for missing practical explanation.

## 12. Ongoing maintenance

When the framework changes, update documentation in layers:

1. exact reference/API/config/CLI surface,
2. conceptual guide if architecture or ownership changed,
3. component/media pages if behavior changed,
4. examples,
5. current limits/accessibility/security notes,
6. source map/test references,
7. parity/build checks.

The goal is not to make the documentation large for its own sake. The goal is that a reader can answer **what, why, when, how, where it runs, what it costs, and what its boundaries are** without needing to reverse-engineer the framework first.
