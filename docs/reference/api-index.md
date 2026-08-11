# Public API Index

This index maps the public `resuxjs` package entry points to their focused documentation. The package exports and implementation are the source of truth; use the narrowest entry point that matches the environment and task.

## `resuxjs`

The root entry re-exports the application-facing runtime surface, including:

- reactivity: `ref`, `reactive`, `computed`, `watch`, `watchEffect`, `readonly`, conversion/check helpers, and `nextTick`;
- state/data: `useState`, `useGlobalState`, `useAsyncData`, `useFetch`, `$fetch`, and `apiURL`;
- routing: `useRoute`, `useRouter`, `navigateTo`, and `abortNavigation`;
- app/config: `useRuntimeConfig`, `useResuxApp`, and application/plugin/module factories;
- head/errors: `useHead`, `useSeoMeta`, `useError`, `createError`, `showError`, and `clearError`;
- server helpers, package/client-enhancement helpers, device/i18n helpers, and `useResuxImage()`.

Read [Composables and Globals](./composables.md), [Runtime Internals](./runtime.md), and the conceptual guides for the feature you are using.

## `resuxjs/runtime`

Advanced renderer/runtime APIs and types for component/template definitions, server setup, document rendering, routes/payloads, browser-runtime generation, client enhancements, media rendering, and runtime composables.

Primary reference: [Runtime Internals](./runtime.md).

## `resuxjs/reactivity`

Focused Resux-native reactivity without the rest of the application runtime:

- `effect()` / `stop()`;
- refs and conversion helpers;
- reactive/readonly proxies;
- computed values;
- `watch()` / `watchEffect()`;
- `nextTick()`;
- public ref/watch/effect types.

Primary reference: [Reactivity API](./reactivity.md). Conceptual usage: [State and Reactivity](/guide/state).

## `resuxjs/compiler`

Node/build-time compiler APIs:

- `buildProject()`;
- `compileVueFile()`;
- `compileVueSource()`;
- `createRouteManifest()`;
- `ResuxCompileError`;
- compile/build/result/route/plugin/middleware/handler/island types.

Primary reference: [Compiler API](./compiler.md).

## `resuxjs/create`

Node-only programmatic project creation/scaffolding and destructive-target safety validation.

Primary reference: [Project Creation API](./create.md). User workflow: [Getting Started](/guide/getting-started) and [CLI](./cli.md).

## `resuxjs/i18n`

Optional i18n module/runtime surface, including public configuration types, `useI18n()`, locale-path helpers, `defineI18nConfig()`, and `createI18nHeadEntry()`.

Primary reference: [i18n API](./i18n.md). Conceptual guide: [i18n and Localization](/guide/i18n).

## `resuxjs/ui`

Optional Vue UI/motion package:

- 23 public `Rx*` components plus matching `Resux*` aliases;
- module options and `defineUiTokens()`;
- `isReducedMotion()` and `useAnimate()`;
- `vAnime` / `vAnimate`.

Primary docs: [UI component catalog](/components/) and [UI Package API](./ui.md).

## `resuxjs/icons`

Optional Vue SVG icon package with a local path registry, Iconify-compatible client fetching, request caching/deduplication, lazy remote loading, module configuration, and helper types/functions.

Primary docs: [Icons](/icons/), [Usage and Registry](/icons/usage), [Configuration](/icons/configuration), and [Runtime Loading](/icons/runtime).

## `resuxjs/fonts`

Google Fonts stylesheet-loader module and typed `googleFont()` family helper.

Primary docs: [Fonts](/fonts/), [Configuration](/fonts/configuration), and [Performance and CSP](/fonts/performance).

## `resuxjs/kit`

Build/module-authoring helpers for components, imports, plugins, middleware, server handlers/plugins, generated templates/types, pages, runtime config, Vite/Nitro extension, route rules, and prerender routes.

Primary reference: [Resux Kit API](./kit.md). Conceptual guide: [Modules and Route Rules](/guide/modules-route-rules).

## `resuxjs/core`

Low-level configuration resolver/constants, hook registry, module contribution container, and core app factory for builders/framework integrations.

Primary references: [Core API](./core.md) and [Lifecycle Hooks](./hooks.md).

## `resuxjs/node`

Focused production Node request-handler entry point exporting `createResuxNodeHandler()` and `ResuxNodeHandlerOptions`.

Primary reference: [Node Handler API](./node.md). Operational guide: [Deployment](/guide/deployment).

## `resuxjs/halal`

Halal Core policy, scanner/evaluator, lifecycle enforcement, runtime-content guard, signed reviewed-memory, AI classifier, integrity/report/CLI utilities and their related types.

Primary reference: [Halal Core API](./halal.md). Conceptual/security guide: [Halal Core](/guide/halal-core).

## `resuxjs/globals`

Type-only app-global declarations used by generated applications. Configure them through generated TypeScript/project types rather than importing this entry for runtime behavior.

Primary guide: [TypeScript and Generated Types](/guide/typescript-generated-types).

## `resuxjs/package.json`

Package metadata export. Package-level documentation: [Package Exports](./packages.md).

## Keeping this index complete

When a public entry point or symbol changes:

1. verify the implementation/export first;
2. update or add its focused reference;
3. document parameters/types/defaults, environment and runtime/resumability limits where relevant;
4. cross-link the conceptual guide and API reference;
5. update [Documentation Coverage](./coverage.md).

The coverage map is intentionally human-reviewable today; it should not be treated as machine-enforced export coverage until CI actually implements that check.
