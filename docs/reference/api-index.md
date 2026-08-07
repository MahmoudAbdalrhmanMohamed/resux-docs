# Public API Index

This index groups the supported package entry points. Not every exported type is intended for ordinary application code; use the narrowest subpath for your task.

## `resuxjs`

The root entry re-exports the runtime application surface:

- reactivity: `ref`, `reactive`, `computed`, `watch`, `watchEffect`, `readonly`, `toRef`, `toRefs`, `unref`, checks, `nextTick`
- state/data: `useState`, `useAsyncData`, `useFetch`, `$fetch`, `apiURL`
- routing: `useRoute`, `useRouter`, `navigateTo`, `abortNavigation`
- app/config: `useRuntimeConfig`, `useResuxApp`, config/plugin/module factories
- head/errors: `useHead`, `useSeoMeta`, `useError`, `createError`, `showError`, `clearError`
- server helpers: event and middleware factories, `readBody`, `getQuery`, `setHeader`
- packages/enhancements: lazy package and client enhancement APIs
- device, i18n, and image helpers

See [Composables and Globals](./composables.md) for the application-facing runtime surface and the [Integration Cookbook](../guide/integration-cookbook.md) for package usage patterns.

## `resuxjs/reactivity`

Focused native reactivity APIs, including lower-level `effect`, `stop`, `isComputed`, scheduler helpers, refs, reactive/readonly proxies, and watchers.

## `resuxjs/runtime`

Renderer and runtime types/functions for advanced integrations:

- component and template definitions
- server setup context
- render functions and document rendering
- route/payload types
- runtime composables
- browser runtime source generation
- client enhancement registration and disposal

## `resuxjs/node`

```ts
import { createResuxNodeHandler } from 'resuxjs/node'
```

Creates the production Node request handler and enforces authenticated production report verification.

## `resuxjs/compiler`

- `buildProject`
- `compileVueFile`
- `compileVueSource`
- `createRouteManifest`
- `ResuxCompileError`
- build, route, component, plugin, middleware, handler, and island types

## `resuxjs/create`

Programmatic application creation and create-target safety validation.

## `resuxjs/i18n`

The i18n module, configuration factories, route/path helpers, translation helpers, head generation, and i18n types.

## `resuxjs/icons`

Icon module, Vue icon component, registry, provider normalization, collection helpers, and Iconify fetching.

## `resuxjs/fonts`

Fonts module, Google font descriptor helper, and fonts option types.

## `resuxjs/ui`

UI module, tokens, animation helpers/directives, `Rx*` primitives, and matching `Resux*` aliases.

The package currently exposes the following component families:

- forms: `RxButton`, `RxInput`, `RxTextarea`, `RxSelect`, `RxDatePicker`, `RxSwitch`
- content/feedback: `RxCard`, `RxBadge`, `RxAvatar`, `RxAlert`, `RxSkeleton`, `RxDivider`, `RxKbd`
- overlays/navigation: `RxModal`, `RxDropdown`, `RxPopover`, `RxTooltip`, `RxAccordion`, `RxTabs`
- motion/icons: `RxMotion`, `RxReveal`, `RxAutoAnimate`, `RxIcon`

Every component and matching `Resux*` alias is documented in the [UI API Reference](./ui.md). The [UI and Motion guide](../guide/ui-animations.md) explains module setup and motion usage.

## `resuxjs/kit`

Nuxt-style module authoring helpers:

- component/import/plugin/middleware/server handler registration
- generated templates and type templates
- page/runtime/Vite/Nitro extension
- route rules and prerender routes

Kit helpers require active module setup context. Async module setup retains its own context across `await`; overlapping setups are isolated by the framework.

## `resuxjs/core`

Core configuration, hooks, module container, contributions, and core app creation. Intended for builders and deep integrations.

## `resuxjs/halal`

Halal Core project/runtime classification, deterministic rules, optional AI classification, reviewed decision memory, runtime guard helpers, and related types. See [Halal Core](../guide/halal-core.md).

## `resuxjs/globals`

Type-only global declarations used by generated applications. Include it through TypeScript `types`; do not import it for runtime behavior.

## Keeping this index complete

Package-level coverage must track `package.json#exports`. When a new public subpath or component is added, update its dedicated guide/reference in the same change. The 2026-08-07 audit recommends automating this check in CI so undocumented public exports cannot silently ship.
