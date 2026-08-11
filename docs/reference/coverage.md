# Public API Documentation Coverage

This page maps the public package entry points declared by `resuxjs` to their primary documentation. It is a human-review coverage map; source/package exports remain the source of truth.

| Public package | Primary documentation | Coverage note |
| --- | --- | --- |
| `resuxjs` | [Public API Index](./api-index.md), [Composables](./composables.md) | Runtime/root public surface |
| `resuxjs/runtime` | [Runtime Internals](./runtime.md), [Rendering Lifecycle](/guide/rendering-lifecycle) | Runtime, SSR, templates, composables, media rendering |
| `resuxjs/reactivity` | [State and Reactivity](/guide/state), [Public API Index](./api-index.md) | Resux-native reactive APIs |
| `resuxjs/compiler` | [Compiler Internals](./compiler.md), [Template Syntax](/guide/template-syntax) | Compiler and supported template behavior |
| `resuxjs/create` | [Getting Started](/guide/getting-started), [CLI](./cli.md) | Project creation/scaffolding |
| `resuxjs/i18n` | [i18n and Localization](/guide/i18n) | Optional i18n module/runtime helpers |
| `resuxjs/ui` | [Component catalog](/components/), [UI Package API](./ui.md) | 23 components + aliases + motion/module helpers |
| `resuxjs/icons` | [Icons](/icons/), [Icon Configuration](/icons/configuration), [Runtime Loading](/icons/runtime) | Local registry, remote fetch, Vue component/module |
| `resuxjs/fonts` | [Fonts](/fonts/), [Font Configuration](/fonts/configuration) | Google Fonts loader and helper |
| `resuxjs/kit` | [Modules and Route Rules](/guide/modules-route-rules), [API Index](./api-index.md) | Module/Kit extension helpers |
| `resuxjs/core` | [Lifecycle Hooks](./hooks.md), [Configuration](./configuration.md) | Core config/hook extension surface |
| `resuxjs/halal` | [Halal Core](/guide/halal-core) | Integrity/review subsystem |
| `resuxjs/node` | [Deployment](/guide/deployment), [Runtime Internals](./runtime.md) | Node handler/deployment boundary |
| `resuxjs/globals` | [TypeScript and Generated Types](/guide/typescript-generated-types) | App-global type declarations |
| `resuxjs/package.json` | [Package Exports](./packages.md) | Package metadata export |

## Focused coverage added in this overhaul

### UI

Every public `Rx*` component and matching `Resux*` alias has a dedicated page. Component pages distinguish native semantics from missing custom-widget behavior and explicitly describe Vue island/runtime cost.

### Media

The renderer-owned `ResuxImg`, `ResuxPicture`, `ResuxVideo`, `useResuxImage()`, provider/transformation behavior, responsive generation, placeholders, preloads, caching, and media deployment/security guidance are split into dedicated pages.

### Fonts

The docs now explicitly constrain the module to its actual Google Fonts stylesheet-loader implementation instead of implying local/provider functionality that does not exist.

### Icons

The docs now distinguish local registry hits from client remote fetching, correct module defaults, distinguish module configuration from component props, and separate the SVG icon package from the UI placeholder `RxIcon`.

## Coverage maintenance rule

When a new public package export or symbol is added:

1. verify it in source/package exports;
2. add or update its focused documentation;
3. link the conceptual guide and API reference in both directions where useful;
4. include environment/runtime limitations;
5. update this map when a new package entry point is introduced.

A future CI improvement should generate an export manifest and fail when a new public symbol has no documentation mapping. Until then, this page is intentionally reviewable rather than pretending the mapping is machine-enforced.
