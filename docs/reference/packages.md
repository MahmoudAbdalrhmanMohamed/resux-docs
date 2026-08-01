# Package Exports

Resux is published as one npm package, `resuxjs`, with focused subpath exports. Import from the narrowest entry point that matches the environment where your code runs.

## Installation

```sh
npm install resuxjs
```

Create a new application:

```sh
npx create-resuxjs@latest my-app
# or
npx resuxjs@latest init my-app
```

Resux requires a modern Node.js runtime. Check the `engines` field of the installed package when selecting a CI or production Node version.

## Export map

| Import | Use it for |
| --- | --- |
| `resuxjs` | Normal application runtime APIs, reactivity, composables, helpers, and public types |
| `resuxjs/node` | Node server adapters such as `createResuxNodeHandler` |
| `resuxjs/globals` | Type declarations for auto-imported application globals; normally referenced by generated app types |
| `resuxjs/runtime` | Lower-level SSR/runtime APIs and types |
| `resuxjs/reactivity` | Focused Resux-native reactivity APIs |
| `resuxjs/compiler` | Compiler and project-build APIs for tooling; Node/build-time only |
| `resuxjs/create` | Programmatic application scaffolding |
| `resuxjs/i18n` | i18n module and localization helpers |
| `resuxjs/ui` | UI tokens, primitives, motion helpers, and animation support |
| `resuxjs/icons` | Icon module and icon runtime helpers |
| `resuxjs/fonts` | Font optimization module |
| `resuxjs/kit` | Module-author utilities and extension types |
| `resuxjs/core` | Lower-level framework container APIs for advanced tooling |
| `resuxjs/package.json` | Package metadata |

## Root runtime export

Use the root entry in Resux pages, components, plugins, middleware, and server files when imports are preferable to globals:

```ts
import {
  ref,
  reactive,
  computed,
  watch,
  useState,
  useAsyncData,
  useFetch,
  useRoute,
  useRouter,
  useHead,
  useSeoMeta,
  defineResuxConfig,
  defineResuxPlugin,
  defineEventHandler
} from 'resuxjs'
```

Generated applications normally include `resuxjs/globals` types, so the same APIs can be used without imports inside application files.

## Reactivity export

Use the focused entry when publishing a library or when you only need Resux reactivity:

```ts
import {
  ref,
  reactive,
  computed,
  watch,
  watchEffect,
  readonly,
  toRef,
  toRefs,
  unref,
  isRef,
  isReactive,
  isReadonly,
  nextTick
} from 'resuxjs/reactivity'
```

This is Resux-native reactivity. It does not require Vue hydration for normal Resux components.

## Node export

Use Node-only APIs from `resuxjs/node`:

```ts
import { createResuxNodeHandler } from 'resuxjs/node'

const handler = createResuxNodeHandler({
  appRoot: process.cwd(),
  securityHeaders: true
})
```

Do not import this entry into browser code.

## Runtime export

`resuxjs/runtime` exposes lower-level rendering and runtime types used by adapters, testing tools, and advanced integrations:

```ts
import {
  renderApp,
  renderDocument,
  type ComponentDefinition,
  type RouteContext,
  type ResuxPayload
} from 'resuxjs/runtime'
```

Most applications do not call these functions directly.

## Compiler export

`resuxjs/compiler` is intended for build tools and framework integrations:

```ts
import { buildProject } from 'resuxjs/compiler'

await buildProject(process.cwd(), '.resux', {
  vite: 'build'
})
```

Compiler imports belong in Node/build-time code, never in client handlers.

## Kit and module authoring

Use `resuxjs/kit` when creating a module:

```ts
import { defineResuxModule } from 'resuxjs/kit'

export default defineResuxModule({
  meta: { name: 'my-module', configKey: 'myModule' },
  defaults: { enabled: true },
  setup(options, resux) {
    if (!options.enabled) return
    resux.addCss('/my-module.css')
    resux.addHead({
      meta: [{ name: 'x-module', content: 'enabled' }]
    })
  }
})
```

The module context supports components, component directories, imports, plugins, route middleware, server handlers, server plugins, templates, type templates, page extension, Vite extension, Nitro extension, Vite plugins, and prerender routes.

## Optional first-party modules

Optional features remain tree-shakable until configured:

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/i18n', { /* options */ }],
    ['resuxjs/icons', { /* options */ }],
    ['resuxjs/fonts', { /* options */ }],
    ['resuxjs/ui', { /* options */ }]
  ]
})
```

Some built-in modules also use `resux:` aliases, such as `resux:security`, `resux:performance`, and `resux:i18n`. Prefer the form documented by the feature guide and the version installed in your project.

## Import safety

To keep client bundles small:

- Do not import `resuxjs/compiler`, `resuxjs/node`, or Node built-ins in components that can reach the browser.
- Put server-only code in `server/`, `.server` plugins/middleware, build modules, or deployment adapters.
- Put browser-only packages behind `.client` files, progressive package loading, client enhancements, or Vue islands.
- Use `import type` for types that should disappear from emitted JavaScript.
