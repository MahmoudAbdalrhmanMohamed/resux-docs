# Public API Documentation Coverage

This page maps each public `resuxjs` package entry point to the documentation that owns its public contract. Source code, package exports, and tests remain the source of truth.

| Public package | Primary documentation | Coverage responsibility |
| --- | --- | --- |
| `resuxjs` | [Public API Index](./api-index.md), [Composables and Globals](./composables.md) | Application-facing runtime surface |
| `resuxjs/runtime` | [Runtime Internals](./runtime.md), [Rendering Lifecycle](/guide/rendering-lifecycle) | Renderer, SSR, templates, composables, payload/client runtime |
| `resuxjs/reactivity` | [Reactivity API](./reactivity.md), [State and Reactivity](/guide/state) | Refs, proxies, computed, watch/effect, scheduler and types |
| `resuxjs/compiler` | [Compiler API](./compiler.md), [Template Syntax](/guide/template-syntax) | Compiler entry points, build/result types and SFC limits |
| `resuxjs/create` | [Getting Started](/guide/getting-started), [CLI](./cli.md) | Project creation/scaffolding |
| `resuxjs/i18n` | [i18n and Localization](/guide/i18n) | Module config, translation/path/head runtime helpers |
| `resuxjs/ui` | [Component catalog](/components/), [UI Package API](./ui.md) | 23 components + aliases + module/motion APIs |
| `resuxjs/icons` | [Icons](/icons/), [Usage](/icons/usage), [Configuration](/icons/configuration), [Runtime Loading](/icons/runtime) | Registry, SVG component, remote/lazy loading and module config |
| `resuxjs/fonts` | [Fonts](/fonts/), [Configuration](/fonts/configuration), [Performance](/fonts/performance) | Google Fonts loader/helper and loading strategies |
| `resuxjs/kit` | [Resux Kit API](./kit.md), [Modules and Route Rules](/guide/modules-route-rules) | Module registration/extension helpers and public input types |
| `resuxjs/core` | [Core API](./core.md), [Lifecycle Hooks](./hooks.md) | Config resolver, hooks, module container and core app factory |
| `resuxjs/halal` | [Halal Core](/guide/halal-core) | Integrity/review/runtime-guard subsystem |
| `resuxjs/node` | [Deployment](/guide/deployment), [Runtime Internals](./runtime.md) | Production Node handler/deployment boundary |
| `resuxjs/globals` | [TypeScript and Generated Types](/guide/typescript-generated-types) | Generated app-global declarations |
| `resuxjs/package.json` | [Package Exports](./packages.md) | Package metadata export |

## Focused coverage completed in this overhaul

### UI

Every public `Rx*` component and its matching `Resux*` alias now has a dedicated page. Pages document verified props, events, slots, styling hooks, native/custom accessibility behavior, and the Vue island/runtime cost. Names are not used to imply behavior the source does not implement—for example, `RxReveal` is mount-triggered and `RxAutoAnimate` currently performs one mount animation rather than mutation-aware layout animation.

### Media

The renderer-owned `ResuxImg`, `ResuxPicture`, `ResuxVideo`, `useResuxImage()`, responsive candidate generation, placeholders, preloads, providers/transforms, caching, Sharp/FFmpeg deployment constraints, security, accessibility and progressive-enhancement behavior now live in dedicated media pages.

### Fonts

The docs constrain `resuxjs/fonts` to its verified Google Fonts stylesheet-loader implementation, including strategy precedence, URL grouping, CSP/privacy/performance trade-offs, and unsupported local/provider features.

### Icons

The docs distinguish local registry SVG data from client-side remote fetching, correct module defaults, distinguish module metadata from component props, and separate `resuxjs/icons` from the UI package's placeholder `RxIcon`.

### Low-level public packages

Focused references now cover:

- `resuxjs/reactivity`: every exported function and public type family;
- `resuxjs/compiler`: public entry points, result records and environment/compile limits;
- `resuxjs/kit`: every exported module helper and its input contract;
- `resuxjs/core`: config constants/resolution, hooks, module contributions and `createResux()`;
- lifecycle hook names with their exact public payload types and dispatch behavior.

## Coverage maintenance rule

When a new public package export or symbol is added:

1. verify it in source/package exports;
2. document it directly or in a clearly appropriate parent reference;
3. document environment, server/client and resumability implications where material;
4. add conceptual/reference cross-links;
5. update this map when a package entry point or ownership area changes.

A future CI improvement should generate an export manifest and fail when a new public symbol has no documentation mapping. Until that check exists, this page is a review aid—not a claim of machine-enforced completeness.
