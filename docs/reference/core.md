# Core API (`resuxjs/core`)

`resuxjs/core` exposes Resux's low-level configuration resolver, lifecycle hook system, module contribution container, and core app factory. It is intended for builders, framework modules, adapters, tests, and deep integrations rather than ordinary page/component code.

## Import surface

The entry point re-exports:

- `config.ts`
- `hooks.ts`
- `module-container.ts`
- `resux.ts`

```ts
import {
  createResux,
  createResuxHooks,
  ResuxHooks,
  ResuxModuleContainer,
  resolveResuxConfig,
  normalizeResuxGeneratedPath,
  DEFAULT_RESUX_BUILD_DIR,
  RESUX_CLIENT_ASSET_DIR
} from 'resuxjs/core'
```

## Configuration constants

```ts
const DEFAULT_RESUX_BUILD_DIR = '.resux'
const RESUX_CLIENT_ASSET_DIR = '__resux'
```

These are framework-owned generated path names, not application asset-directory configuration by themselves.

## `normalizeResuxGeneratedPath()`

```ts
function normalizeResuxGeneratedPath(value: string): string
```

Normalizes framework-owned legacy Nuxt-style generated path segments:

- `.nuxt` path segments become `.resux`;
- `_nuxt` client-asset path segments become `__resux`.

The replacement operates on path segments, not arbitrary substrings inside unrelated names.

## `resolveResuxConfig()`

```ts
interface ResuxResolvedConfig extends ResuxConfigInput {
  builder: string
  serverBuilder: string
  buildDir: string
  compatibilityDate: string
}

function resolveResuxConfig(
  input: Record<string, unknown>
): ResuxResolvedConfig
```

Current core defaults:

| Field | Default |
| --- | --- |
| `builder` | `'vite'` |
| `serverBuilder` | `'nitro'` |
| `buildDir` | `'.resux'` |
| `compatibilityDate` | `'2026-05-20'` when the input is not `YYYY-MM-DD` |

`buildDir` is passed through `normalizeResuxGeneratedPath()`.

This low-level resolver does not replace the full application configuration/build pipeline; use the normal `resux.config.ts` path for applications.

## `ResuxHooks`

```ts
class ResuxHooks {
  hook<K extends ResuxHookName>(
    name: K,
    handler: ResuxHookHandler<ResuxHookPayloads[K]>
  ): () => void

  addHooks(handlers: Partial<...>): void

  callHook<K extends ResuxHookName>(
    name: K,
    payload: ResuxHookPayloads[K]
  ): Promise<void>
}

function createResuxHooks(): ResuxHooks
```

See the complete [Lifecycle Hooks Reference](./hooks.md) for every public hook payload and dispatch behavior.

## Module contribution types

### `ResuxSupportMode`

```ts
type ResuxSupportMode = 'all' | 'server' | 'client'
```

Used by component/plugin/middleware module contributions to express runtime ownership.

### Main contribution inputs

`resuxjs/core` exports these public input types:

- `ResuxTemplateInput`
- `ResuxTypeTemplateInput`
- `ResuxComponentInput`
- `ResuxComponentsDirInput`
- `ResuxImportInput`
- `ResuxPluginInput`
- `ResuxRouteMiddlewareInput`
- `ResuxServerHandlerInput`
- `ResuxPrerenderRouteInput`
- `PagesExtender`
- `ViteConfigExtender`
- `NitroConfigExtender`
- `ResuxModuleContributions`
- `ResuxModuleContext`

The field-level contracts are documented in [Resux Kit API](./kit.md), which is the preferred authoring surface for most modules.

## `ResuxModuleContainer`

```ts
class ResuxModuleContainer {
  readonly contributions: ResuxModuleContributions

  createContext(
    config: Record<string, unknown>,
    rootDir: string,
    buildDir: string,
    hooks: ResuxHooks
  ): ResuxModuleContext
}
```

The contribution registry includes arrays for components, component directories, imports/import directories, plugins, route middleware, server handlers/plugins, generated templates/type templates, page extenders, runtime-config extensions, Vite/Nitro extenders, Vite plugins, route rules, and prerender routes.

### Context merge behavior

Important verified behaviors:

- duplicate CSS hrefs are not added twice by `addCss()`;
- `addHead()` appends `meta`, `link`, `style`, `script`, and `noscript` arrays and merges `htmlAttrs` / `bodyAttrs`;
- `addRouteRule()` requires an absolute `/` path and merges nested headers;
- `extendRuntimeConfig()` deep-merges objects and rejects unsafe keys `__proto__`, `prototype`, and `constructor`;
- string plugins normalize to mode `all`;
- prerender route strings are stored as `{ route }` contribution records.

These are module-container contracts, not generic object-merge guarantees for every Resux API.

## `createResux()`

```ts
interface ResuxCoreOptions {
  rootDir: string
  buildDir: string
  config: Record<string, unknown>
}

interface ResuxCoreApp {
  rootDir: string
  buildDir: string
  options: ResuxResolvedConfig
  hooks: ResuxHooks
  hook: ResuxHooks['hook']
  callHook: ResuxHooks['callHook']
  modules: ResuxModuleContainer
}

function createResux(options: ResuxCoreOptions): ResuxCoreApp
```

The factory:

1. creates a fresh hook registry;
2. resolves the supplied config through `resolveResuxConfig()`;
3. creates a fresh `ResuxModuleContainer`;
4. exposes bound `hook` / `callHook` methods plus the underlying objects.

It does **not** build or start an application by itself. Builders/compiler code use the returned core objects as infrastructure.

## Environment

Treat the Core entry point as framework/tooling infrastructure. Application runtime code should normally import from `resuxjs` / `resuxjs/runtime`, and module authors should prefer `resuxjs/kit`.

Keeping these boundaries narrow helps prevent build/compiler concerns from leaking into browser code.

## Related

- [Resux Kit API](./kit.md)
- [Lifecycle Hooks](./hooks.md)
- [Configuration](./configuration.md)
- [Compiler](./compiler.md)
