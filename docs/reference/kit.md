# Resux Kit API (`resuxjs/kit`)

`resuxjs/kit` is the build/module-authoring helper package. It lets a module contribute components, imports, plugins, middleware, server handlers, templates, pages, Vite/Nitro configuration, route rules, and prerender routes without reaching into compiler internals.

::: warning Build/server context
The package uses Node's `AsyncLocalStorage` to keep module setup context isolated across async work. Treat `resuxjs/kit` as build/module tooling, not a browser runtime dependency.
:::

## Define a module

```ts
import {
  defineResuxModule,
  addComponent,
  addImports,
  addRouteRule
} from 'resuxjs/kit'

export default defineResuxModule({
  meta: {
    name: 'resux-example',
    configKey: 'example'
  },
  defaults: {
    enabled: true
  },
  setup(options) {
    if (!options.enabled) return

    addComponent({
      file: './runtime/Example.vue',
      name: 'Example'
    })

    addImports({
      from: './runtime/composables',
      name: 'useExample'
    })

    addRouteRule('/private/**', {
      headers: { 'cache-control': 'private, no-store' }
    })
  }
})
```

## `defineResuxModule()`

```ts
interface ResuxModuleMeta {
  name?: string
  configKey?: string
}

interface ResuxModuleDefinition<TOptions = Record<string, unknown>> {
  meta?: ResuxModuleMeta
  defaults?: TOptions
  setup: (
    options: TOptions,
    resux: ResuxModuleContext
  ) => void | Promise<void>
}

function defineResuxModule<TOptions = Record<string, unknown>>(
  module: ResuxModuleDefinition<TOptions>
): ResuxModuleDefinition<TOptions>
```

It is an identity-style definition helper: the module container/compiler owns when setup is executed and supplies the active context.

## Context requirement

All global Kit helpers below call the currently active module context. Calling them outside module setup (or an explicitly installed Kit context) throws an error naming the helper.

Async setup retains the correct context across `await`, and overlapping module setups remain isolated through `AsyncLocalStorage`.

## Component registration

### `addComponent()`

```ts
function addComponent(component: ResuxComponentInput | string): void

interface ResuxComponentInput {
  file: string
  name?: string
  global?: boolean
  mode?: 'all' | 'server' | 'client'
  lazy?: boolean
}
```

String input is normalized to `{ file }`.

### `addComponentsDir()`

```ts
function addComponentsDir(dir: ResuxComponentsDirInput | string): void

interface ResuxComponentsDirInput {
  path: string
  global?: boolean
  mode?: 'all' | 'server' | 'client'
  pathPrefix?: boolean
}
```

## Auto-import registration

### `addImports()`

```ts
function addImports(
  imports: ResuxImportInput | ResuxImportInput[]
): void

interface ResuxImportInput {
  from: string
  name: string
  as?: string
}
```

### `addImportsDir()`

```ts
function addImportsDir(dir: string): void
```

## Plugins and middleware

### `addPlugin()`

```ts
function addPlugin(plugin: ResuxPluginInput | string): void

interface ResuxPluginInput {
  src: string
  mode?: 'all' | 'server' | 'client'
}
```

String plugin input is normalized to mode `all`.

### `addRouteMiddleware()`

```ts
function addRouteMiddleware(
  middleware: ResuxRouteMiddlewareInput
): void

interface ResuxRouteMiddlewareInput {
  name: string
  src: string
  global?: boolean
  mode?: 'all' | 'server' | 'client'
}
```

### `addServerHandler()`

```ts
function addServerHandler(handler: ResuxServerHandlerInput): void

interface ResuxServerHandlerInput {
  route: string
  handler: string
  middleware?: boolean
  method?: string
}
```

### `addServerPlugin()`

```ts
function addServerPlugin(plugin: string): void
```

## Generated templates

### `addTemplate()`

```ts
function addTemplate(template: ResuxTemplateInput): void

interface ResuxTemplateInput {
  filename: string
  getContents: () => string | Promise<string>
  write?: boolean
}
```

### `addTypeTemplate()`

```ts
function addTypeTemplate(template: ResuxTypeTemplateInput): void
```

`ResuxTypeTemplateInput` currently extends the same template input contract. Use it for generated type declarations so the framework can treat type-template output separately from ordinary generated templates.

## Pages

### `extendPages()`

```ts
type PagesExtender = (
  pages: Array<Record<string, unknown>>
) => void | Promise<void>

function extendPages(extender: PagesExtender): void
```

The extender participates in the compiler's page-resolution pipeline. Mutate/extend only fields understood by the current page manifest pipeline; avoid inventing Nuxt-specific page-record fields unless Resux source supports them.

## Runtime config

### `extendRuntimeConfig()`

```ts
function extendRuntimeConfig(config: Record<string, unknown>): void
```

The module container deep-merges runtime config. Unsafe object keys `__proto__`, `prototype`, and `constructor` are rejected during the deep-merge path.

Do not put secrets under public runtime config.

## Vite and Nitro

### `extendViteConfig()`

```ts
type ViteConfigExtender = (
  config: Record<string, unknown>
) => void | Promise<void>

function extendViteConfig(extender: ViteConfigExtender): void
```

### `extendNitroConfig()`

```ts
type NitroConfigExtender = (
  config: Record<string, unknown>
) => void | Promise<void>

function extendNitroConfig(extender: NitroConfigExtender): void
```

### `addVitePlugin()`

```ts
function addVitePlugin(plugin: unknown): void
```

The plugin is added to the compiler's Vite client configuration. Prefer a real Vite plugin object and keep Node/build-only dependencies out of browser code emitted by that plugin.

## Route rules

### `addRouteRule()`

```ts
function addRouteRule(
  path: string,
  rule: Record<string, unknown>
): void
```

Module-context route-rule registration requires an absolute path beginning with `/`. Existing rule fields and nested headers are merged by the module container.

Use the [Modules and Route Rules guide](/guide/modules-route-rules) for the supported application-level route-rule shape.

## Prerender routes

### `addPrerenderRoutes()`

```ts
function addPrerenderRoutes(route: string | string[]): void
```

Each supplied route is stored as a prerender contribution for the build/deployment pipeline.

```ts
addPrerenderRoutes([
  '/',
  '/about',
  '/docs/getting-started'
])
```

## `withResuxKitContext()`

```ts
function withResuxKitContext<T>(
  context: ResuxModuleContext,
  run: () => Promise<T> | T
): Promise<T> | T
```

This is the low-level context installer used by framework/module execution. Most modules should not call it directly; use `defineResuxModule()` and let Resux install the setup context.

## `ResuxModuleContext`

The context passed directly to module setup includes:

- `rootDir`, `buildDir`, and full resolved `options`;
- `addCss()` and `addHead()`;
- `hook()`;
- all registration/extension methods represented by the Kit helpers;
- `extendRuntimeConfig()` and route-rule/prerender contributions.

Use the direct context or global Kit helpers consistently within a module. The global helpers are convenient for Nuxt-style module authoring; the explicit context makes ownership easier to see in low-level tooling.

## Runtime/resumability implications

Kit executes while configuring/building the app. A Kit call itself is not shipped as browser runtime JavaScript. What you register **can** affect browser cost:

- client-mode plugins/components can create client runtime work;
- server-only handlers/plugins stay server-side;
- generated templates may affect both output sides;
- Vite plugins can change browser bundles;
- route rules/prerender settings change server/deployment behavior.

Document the resulting runtime boundary in any third-party module built on Kit.

## Related

- [Modules and Route Rules](/guide/modules-route-rules)
- [Hooks](./hooks.md)
- [Core API](./core.md)
- [TypeScript and Generated Types](/guide/typescript-generated-types)
