from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dedent(content).strip() + "\n", encoding="utf-8")


write("docs/guide/what-is-resux.md", r'''
# What is Resux?

Resux is an experimental, HTML-first web framework with a custom compiler, server renderer, resumable browser runtime, file-based routing, server APIs, build-time modules, deployment adapters, and optional Vue runtime islands.

Normal Resux components are written as `.vue` files, but they are **not hydrated by Vue**. Resux compiles a focused Vue-like SFC subset into:

- server-renderable component modules,
- serializable route and component state,
- small browser handler modules,
- DOM binding metadata,
- and a route payload used for client navigation.

The browser starts from server HTML and resumes only the scope required by an interaction or client enhancement.

::: info Documentation target
These docs track the current framework source and its public `resuxjs/*` package surface. The source package may be ahead of the version currently published under npm's `latest` tag. Check the release you install with `npm view resuxjs version` and review its release notes.
:::

## The request-to-interaction flow

1. Resux discovers pages, layouts, components, plugins, middleware, server handlers, islands, and module contributions.
2. The compiler validates the supported SFC subset and resumability rules.
3. The server renders the active app shell, layout, and page to HTML.
4. State, async data, route metadata, module identifiers, client plugins, middleware, and public runtime config are serialized into the payload.
5. The browser installs a delegated runtime instead of hydrating the component tree.
6. Same-origin navigation requests a new Resux route payload.
7. Event or enhancement code is imported only when it is needed.
8. The resumed scope updates marked DOM bindings and can later be disposed cleanly.

## What Resux includes

| Area | Included capabilities |
| --- | --- |
| Application model | `app.vue`, `error.vue`, pages, layouts, components, plugins, route middleware, server middleware, server plugins |
| Rendering | SSR HTML, payload serialization, route payload navigation, scoped styles, head composition |
| Reactivity | `ref`, `reactive`, `computed`, `watch`, `watchEffect`, `readonly`, `toRef`, `toRefs`, `nextTick` |
| Data | `useState`, `useAsyncData`, `useFetch`, `$fetch`, runtime config, error APIs |
| Server | API routes, custom server routes, middleware, h3-backed helpers, Node handler export |
| Extension | modules, hooks, Resux Kit helpers, Vite/Nitro extension, generated templates and types |
| Packages | SSR, client-only, server-only, and progressive third-party package modes |
| Built-ins | links, app/page/layout rendering, responsive images, pictures, videos, icons, fonts, i18n, UI primitives |
| Tooling | create templates, prepare, check, inspect targets, build, preview, deployment generation |
| Deployment | Node, Docker, Nitro, Vercel, Netlify, Cloudflare, and static target resolution |
| Safety | local policy scanner, reports, signed production integrity, manual review workflow |

## Best fits

Resux is strongest when an app benefits from:

- server HTML and SEO,
- explicit serializable state,
- limited client JavaScript,
- interaction-triggered code loading,
- file conventions and integrated server APIs,
- progressive enhancement,
- and selective Vue islands for complex widgets.

## Important boundaries

Resux is not a drop-in replacement for the complete Vue runtime and SFC feature set. Unsupported syntax should fail during compilation rather than silently enabling hydration.

Key boundaries include:

- resumable state must be serializable,
- handler captures must be safe to reconstruct,
- normal Resux components do not run full Vue lifecycle semantics,
- browser-only libraries need a client enhancement, progressive package adapter, or Vue island,
- video transformation requires `ffmpeg`,
- image transformation requires `sharp`,
- and production Halal report verification requires a private HMAC key.

Read [Current Limits](/reference/limits) before choosing Resux for a large production system.

## Install and create

```sh
npx create-resuxjs@latest my-app
cd my-app
npm install
npm run dev
```

The main package is `resuxjs`. Public entry points are documented in [Package Exports](/reference/packages) and [API Index](/reference/api-index).
''')

write("docs/guide/getting-started.md", r'''
# Getting Started

This guide creates a Resux app, explains the generated project, and prepares it for development and production.

## Requirements

- Node.js `>=20.19.0`
- npm, pnpm, yarn, or Bun
- a modern browser for the resumable client runtime

```sh
node --version
```

## Create an application

Use either the full CLI or the create wrapper:

```sh
npx resuxjs@latest init my-app
# or
npx create-resuxjs@latest my-app
```

Then:

```sh
cd my-app
npm install
npm run dev
```

## Starter templates

```sh
npx create-resuxjs@latest my-app --template default
```

Available templates:

| Template | Intended use |
| --- | --- |
| `minimal` | Smallest app shell and page |
| `default` | General starter with common conventions |
| `full` | Broad feature demonstration |
| `i18n` | Localized routes and messages |
| `pwa` | Progressive web app starter files |
| `media` | Images, pictures, and video examples |
| `package-compatibility` | Third-party package modes and diagnostics |
| `dashboard` | Dashboard-oriented structure and UI |

## Optional features

Features can be selected independently or combined:

```sh
npx create-resuxjs@latest my-app \
  --features seo,i18n,media,tailwind,server-api,tests
```

Supported feature names:

- `seo`
- `i18n`
- `media`
- `pwa`
- `tailwind`
- `package-compatibility`
- `server-api`
- `tests`

For i18n starters:

```sh
npx create-resuxjs@latest my-app --features i18n --hreflang
```

## Other create options

```sh
npx create-resuxjs@latest my-app --no-install
npx create-resuxjs@latest my-app --package-manager pnpm
npx create-resuxjs@latest my-app --yes
```

`--force` empties a non-empty target, but Resux refuses to apply it to protected locations such as the filesystem root, home directory, current working directory, or an ancestor of the working directory.

## Generated scripts

A generated app contains scripts similar to:

```json
{
  "scripts": {
    "prepare": "resux prepare",
    "dev": "resux dev",
    "build": "resux build",
    "preview": "resux preview",
    "start": "resux start",
    "inspect": "resux inspect",
    "typecheck": "vue-tsc --noEmit"
  }
}
```

Run preparation and validation after changing framework versions or generated conventions:

```sh
npm run prepare
npx resux check
npx resux check --fix
```

## Your first page

Create `pages/index.vue`:

```vue
<script setup lang="ts">
useSeoMeta({
  title: 'Home',
  description: 'My first Resux application'
})

const count = useState('home-count', () => 0)

function increment() {
  count.value++
}
</script>

<template>
  <main>
    <h1>Hello Resux</h1>
    <button @click="increment">Clicked {{ count }} times</button>
  </main>
</template>
```

Templates auto-unwrap Resux refs. Script code uses `.value`.

## Add an API route

Create `server/api/status.ts`:

```ts
export default defineEventHandler(() => ({
  ok: true,
  framework: 'resux'
}))
```

Request it from a page:

```ts
const status = await useFetch<{ ok: boolean }>('/api/status')
```

`useFetch` returns an async-data resource with `data`, `value`, `pending`, and `error` refs.

## Inspect the project

```sh
npx resux inspect
npx resux inspect routes
npx resux inspect packages --json
npx resux inspect seo --json
```

Inspect targets include routes, plugins, enhancements, middleware, imports, components, build, images, server, packages, templates, bundles, and SEO.

## Production build

For production report authentication, configure a secret of at least 32 characters:

```sh
export RESUX_HALAL_REPORT_SIGNING_SECRET='replace-with-a-private-random-secret'
```

Then:

```sh
npm run build
npm run start
```

Build output normally includes:

```txt
.resux/   Resux compiler/runtime output
.output/  Nitro production output
```

## Recommended reading

- [Framework Tour](/guide/framework-tour)
- [Project Structure](/guide/project-structure)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [Template Syntax](/guide/template-syntax)
- [Deployment](/guide/deployment)
''')

write("docs/guide/project-structure.md", r'''
# Project Structure

Resux supports root-level application directories and matching `app/` directories for the main application conventions.

## Common structure

```txt
my-app/
  app.vue
  error.vue
  resux.config.ts
  resux.halal.config.ts
  env.d.ts
  tsconfig.json
  pages/
  components/
  layouts/
  composables/
  utils/
  shared/
  plugins/
  middleware/
  enhancements/
  client-enhancements/
  islands/vue/
  server/
    api/
    routes/
    middleware/
    plugins/
    utils/
  assets/
  public/
  types/
```

Most application directories can also live under `app/`, including pages, components, layouts, plugins, middleware, enhancements, and the app/error components.

## Root files

| File | Purpose |
| --- | --- |
| `app.vue` | Optional application shell. Usually contains `<ResuxPage />`. |
| `error.vue` | Optional error renderer for not-found and server errors. |
| `resux.config.ts` | Framework, app head, runtime config, CSS, modules, packages, deployment, media, i18n, and route rules. |
| `resux.halal.config.ts` | Safety policy, project description, evidence, review contact, and optional AI settings. |
| `env.d.ts` | Adds generated Resux globals and application types. |
| `tsconfig.json` | TypeScript project configuration. |
| `nitro.config.ts` | Nitro deployment/server configuration. |
| `.env.example` | Non-secret environment variable documentation. |

## Application directories

| Directory | Behavior |
| --- | --- |
| `pages/` | File-based routes. Dynamic and catch-all segments are supported. |
| `components/` | Auto-discovered Resux components. Modules can add more directories. |
| `layouts/` | Named layouts selected through page metadata. |
| `composables/` | Auto-imported shared functions and package-analysis input. |
| `utils/` | Auto-imported shared utilities. |
| `shared/` | Auto-imported shared modules. |
| `plugins/` | App plugins. `.client` and `.server` suffixes set execution mode. |
| `middleware/` | Named and global route middleware. `.global` marks global middleware. |
| `enhancements/` | Client enhancement plugin files. |
| `client-enhancements/` | Explicit client enhancement plugin files. |
| `islands/vue/` | Full Vue runtime island components. |
| `assets/` | Source assets and global CSS. `/assets/*` imports are served safely. |
| `public/` | Static files served from the web root. |
| `types/` | Application declarations and module augmentation. |

## Server directories

| Directory | Behavior |
| --- | --- |
| `server/api/` | Handlers mounted under `/api`. |
| `server/routes/` | Custom handlers mounted without the `/api` prefix. |
| `server/middleware/` | Request middleware before APIs, public files, and pages. |
| `server/plugins/` | Server-only setup included in package analysis and Nitro integration. |
| `server/utils/` | Server-only auto-imported utilities. |

## Generated directories

| Directory | Purpose |
| --- | --- |
| `.resux/` | Compiler manifests, server modules, browser handlers, client assets, diagnostics, generated templates, and generated types. |
| `.resux/vite-client/` | Development client sources consumed by Vite. |
| `.resux/client/` | Production browser runtime, plugins, middleware, handlers, chunks, and assets. |
| `.resux/server/` | Development/server modules and manifests. |
| `.resux/server-bundle/` | Bundled production server manifest. |
| `.resux/dev/` | Inspectable development manifests and diagnostics. |
| `.resux/types/` | Generated type declarations. |
| `.resux-nitro/` | Generated Nitro bridge files. |
| `.nitro/` | Nitro working output. |
| `.output/` | Deployable Nitro output. |
| `.resux-generated/` | Persistent generated media cache when enabled. |

Generated output should be ignored by Git and regenerated with `resux prepare`, `resux dev`, or `resux build`.

## Naming suffixes

Support TypeScript files understand suffixes such as:

```txt
plugins/analytics.client.ts
plugins/database.server.ts
middleware/auth.ts
middleware/log.global.ts
middleware/admin.server.ts
```

Modules can also register files explicitly and override their mode, global status, or public name.

See [File Conventions](/reference/file-conventions) for the complete mapping.
''')

write("docs/guide/core-concepts.md", r'''
# Core Concepts

Resux combines compile-time analysis, SSR, serialized state, delegated events, route payload navigation, progressive enhancement, and explicit extension points.

## Concept map

| Concept | Meaning |
| --- | --- |
| Resux component | A compiled `.vue` component using the documented subset, without Vue hydration. |
| Scope | One rendered component instance and its resumable state, async data, props, and module id. |
| Payload | Route, scopes, client modules, public config, plugins, middleware, page metadata, and island entries serialized for the browser. |
| Binding | A compiler-marked text, attribute, class, style, visibility, or HTML location that can be patched after resume. |
| Handler module | Client code generated for a component's event handlers. |
| Route payload | Fresh rendered output fetched for same-origin client navigation. |
| Client enhancement | Named progressive behavior attached by trigger and disposed when no longer needed. |
| Package mode | How a third-party package participates in SSR and the browser: `ssr`, `clientOnly`, `serverOnly`, or `progressive`. |
| Module | Build-time extension contributing files, config, hooks, templates, types, Vite/Nitro changes, or routes. |
| Hook | Typed lifecycle event emitted by core, compiler, Vite, Nitro, loading, and error flows. |
| Vue island | Opt-in component mounted by the full Vue runtime. |

## Compile-time responsibilities

The compiler:

- discovers project conventions,
- parses `.vue` SFCs,
- validates template and style support,
- transforms setup code,
- records bindings and handlers,
- verifies resumable captures,
- creates routes and localized route variants,
- analyzes third-party package usage,
- emits server modules and client entry points,
- and writes generated manifests and types.

## Server responsibilities

The server:

- applies request middleware and route rules,
- handles APIs and custom server routes,
- runs route middleware,
- renders the app shell, layout, and page,
- merges head entries,
- serializes state and public configuration,
- serves runtime and handler assets,
- transforms media when configured,
- and exposes `/__resux/health`.

## Browser responsibilities

The browser runtime:

- reads the serialized payload,
- delegates supported events,
- imports handlers on demand,
- resumes scopes,
- applies DOM patches,
- runs client plugins and middleware,
- handles route payload navigation,
- activates registered client enhancements,
- and disposes observers and cleanup functions.

## Choosing the correct tool

| Need | Preferred feature |
| --- | --- |
| Shared serializable UI state | `useState` |
| SSR data with pending/error refs | `useAsyncData` or `useFetch` |
| Private database or credential work | server API, middleware, plugin, or utility |
| App-wide provided value | plugin and `useResuxApp()` |
| Build-time extension | module or `resuxjs/kit` |
| Browser-only DOM behavior | client enhancement |
| Full Vue component behavior | Vue island |
| Third-party library loaded later | progressive package adapter |
| Response headers, cache, redirects, CORS | route rules |

## Serialization is architectural

Resux does not reconstruct a complete client component tree. It resumes from serialized values. Functions, class instances, sockets, DOM nodes, and other runtime-only objects should not be stored in resumable state.

Read [Resumability and Handlers](/guide/resumability-handlers) and [Execution Contexts](/guide/execution-contexts) next.
''')

write("docs/guide/execution-contexts.md", r'''
# Execution Contexts

Resux code can run during configuration, compilation, server requests, SSR, browser resume, progressive enhancement, or Vue island mounting. The same source file should not assume all contexts are available.

## Context matrix

| Context | Examples | Has request? | Has browser DOM? | May contain secrets? |
| --- | --- | ---: | ---: | ---: |
| Configuration | `resux.config.ts` | No | No | Build environment only |
| Module setup | `modules/*`, npm module | No | No | Avoid exposing through public config |
| Core hooks | build/Vite/Nitro hooks | Depends on hook | Usually no | Yes when server/build only |
| Server plugin | `server/plugins/*` | No direct request | No | Yes |
| Request middleware | `server/middleware/*` | Yes | No | Yes |
| Server handler | `server/api/*`, `server/routes/*` | Yes | No | Yes |
| Route middleware | `middleware/*` | Route context | Client mode may run in browser | Do not expose secrets |
| Plugin | `plugins/*` | SSR plugin sees app context | Client mode may run in browser | Depends on mode |
| Component setup | page/layout/component | During SSR | No during SSR | No private secrets in serialized output |
| Resumable event | `@click`, `@submit` | No server request | Yes | Never |
| `onMounted` | resumed scope | No | Yes | Never |
| Client enhancement | `enhancements/*` | No | Yes | Never |
| Vue island | `islands/vue/*` | No | Yes | Never |

## Build-time modules

Modules can add components, imports, plugins, middleware, server handlers, templates, types, route rules, prerender routes, Vite plugins, and Nitro configuration.

```ts
import { defineResuxModule, addTemplate, addTypeTemplate } from 'resuxjs/kit'

export default defineResuxModule({
  meta: { name: 'example', configKey: 'example' },
  defaults: { enabled: true },
  setup(options) {
    if (!options.enabled) return

    addTemplate({
      filename: 'example.mjs',
      getContents: () => 'export const enabled = true'
    })

    addTypeTemplate({
      filename: 'example.d.ts',
      getContents: () => 'declare const exampleEnabled: boolean'
    })
  }
})
```

Kit helpers throw when called outside active module setup.

## Server-only work

Use server handlers, middleware, server plugins, and `server/utils` for:

- database connections,
- private tokens,
- filesystem access,
- signed cookies,
- privileged network requests,
- and private runtime configuration.

```ts
export default defineEventHandler(async (event) => {
  const body = await readBody<{ name: string }>(event)
  return { saved: Boolean(body.name) }
})
```

## SSR component setup

Component setup creates HTML and resumable state. It must tolerate server execution.

```ts
const route = useRoute()
const config = useRuntimeConfig()
const result = await useAsyncData('record', () => $fetch(`/api/records/${route.params.id}`))
```

Do not read `window`, `document`, storage, or browser constructors directly during setup.

## Browser resume and cleanup

```ts
onMounted(() => {
  const onResize = () => console.log(window.innerWidth)
  window.addEventListener('resize', onResize)
  return () => window.removeEventListener('resize', onResize)
})
```

Client enhancement setup can also return a cleanup function. Resux calls disposal during navigation or explicit disposal.

## Environment boundaries

- Private `runtimeConfig` stays on the server.
- `runtimeConfig.public` is serialized.
- Plugin and middleware suffixes control server/client participation.
- `serverOnly` packages must never be imported by browser sources.
- `clientOnly` packages should not be executed during SSR.
- `progressive` packages should activate through an adapter or enhancement trigger.

Use [Third-party Packages](/guide/package-integration) and [Plugins](/guide/plugins) for concrete patterns.
''')

write("docs/guide/mental-model.md", r'''
# Mental Model

Think of Resux as a compiler and server framework that leaves a structured continuation inside the HTML response.

## Not hydration

Hydration commonly downloads component code and re-executes a client component tree to attach behavior. Resux instead serializes the minimum information needed to continue a rendered scope later.

The browser receives:

- finished HTML,
- scope identifiers,
- serializable state and async data,
- binding metadata already present in the DOM,
- module URLs,
- route and page metadata,
- public config,
- and client plugin/middleware manifests.

## A component becomes two concerns

For a resumable component, the compiler emits:

1. **Server behavior** that runs setup and renders HTML.
2. **Client handler behavior** that resumes state and runs interaction code.

This split explains several framework rules:

- event handlers cannot capture arbitrary server objects,
- state crossing the boundary must be serializable,
- direct browser APIs belong in mounted or client-only contexts,
- and unsupported template behavior is rejected instead of hydrated.

## Navigation is another server render

Same-origin navigation does not reconstruct a full client router component tree. The runtime requests a route payload, lets route middleware run, receives rendered output and metadata, updates the page region and head, then activates the new payload.

The server remains the source of truth for route matching and SSR output.

## Reactivity updates marked DOM

Resux reactivity tracks dependencies inside resumed scopes. When state changes, the runtime evaluates compiler-recorded expressions and patches only affected bindings.

This is why the supported expression and directive subset matters: the compiler must understand what can change.

## Progressive behavior is separate from component hydration

Some behavior is better represented as a DOM enhancement than a component runtime. Resux supports named enhancements with triggers:

- `visible`
- `interaction`
- `idle`
- `immediate`
- `manual`
- `page-load`

Enhancements can return cleanup functions and are disposed when needed.

## Vue islands are explicit

A Vue island creates a separate Vue runtime boundary for a widget that genuinely needs Vue component semantics or a Vue-specific library. It does not convert surrounding Resux components into hydrated Vue components.

## Rules that follow from the model

1. Prefer server work for data access and secrets.
2. Store only serializable values in resumable state.
3. Keep handlers small and capture reconstructable values.
4. Use route rules for HTTP policy.
5. Use modules for build-time extension.
6. Use progressive enhancements for DOM libraries.
7. Use Vue islands only where full Vue is necessary.
8. Treat generated output as disposable build artifacts.
''')

write("docs/guide/rendering-lifecycle.md", r'''
# Rendering Lifecycle

This page follows a Resux application from command execution to browser interaction and disposal.

## 1. Preparation

`resux prepare`, `resux check --fix`, `resux dev`, and `resux build` can scaffold required safe files and generated directories.

Preparation produces or validates items such as:

- `env.d.ts`
- `tsconfig.json`
- `nitro.config.ts`
- `.resux-nitro/handler.ts`
- generated component/import/type declarations
- ignored generated paths

## 2. Configuration and modules

Resux loads `resux.config.ts`, resolves defaults, and creates the module container. Modules contribute config and files, then lifecycle hooks run, including `config:resolved` and `app:resolve`.

## 3. Discovery

The compiler discovers:

- components and component directories,
- pages and layouts,
- `app.vue` and `error.vue`,
- plugins and client enhancements,
- route and request middleware,
- server handlers and server plugins,
- Vue islands,
- auto-import directories,
- and package usage.

## 4. SFC compilation

Each Resux `.vue` file is parsed with Vue's compiler packages but converted into Resux's own component definition.

Compilation produces:

- server source,
- browser handler source,
- template nodes,
- expression and binding ids,
- styles and scope ids,
- handler names,
- and page metadata.

Unsupported style languages, style modules, style `src`, unsupported directives, and unsafe handler captures fail with a `ResuxCompileError` and source location when available.

## 5. Manifest and generated output

The build records routes, components, layouts, plugins, enhancements, middleware, server handlers, islands, route rules, runtime config, package diagnostics, and generated type information.

Development emits Vite client entries. Production bundles client assets and a server manifest, then builds Nitro output.

## 6. Request handling

For an HTTP request, Resux applies this broad order:

1. health and internal framework endpoints,
2. request middleware,
3. route-rule matching,
4. server API/custom route matching,
5. static and generated media handling,
6. page route matching,
7. route middleware,
8. SSR rendering,
9. response headers and document output.

Redirects and aborts can stop the flow earlier.

## 7. SSR rendering

Rendering creates an app context, runs eligible plugins, executes page/layout/component setup, resolves async data, builds component scopes, renders template nodes, merges app/page/module head entries, and serializes the payload.

The result contains:

```ts
type RenderResult = {
  html: string
  payload: ResuxPayload
  head: HeadEntry
  statusCode?: number
}
```

## 8. Browser boot

The runtime reads the payload, installs delegated listeners, initializes route navigation, registers client plugins and middleware, and scans registered client enhancements.

It does not eagerly execute every handler module.

## 9. Interaction resume

When an event reaches a Resux-marked element:

1. modifiers and filters are checked,
2. the component handler module is imported if needed,
3. the serialized scope is reconstructed,
4. the handler runs,
5. reactive dependencies trigger updates,
6. marked DOM bindings are patched.

## 10. Client navigation

Internal links are intercepted when eligible. The runtime asks `/__resux/route` for the destination, handles redirect/abort results, updates the page content and head, applies the new payload, and runs page loading/finish hooks.

## 11. Cleanup

When enhancements or page content are replaced, Resux disconnects shared observers, removes pending registrations, and calls cleanup functions returned by enhancements or mounted work.

This lifecycle is why cleanup-returning setup functions are important for global listeners, observers, timers, and library instances.
''')

write("docs/guide/resumability-handlers.md", r'''
# Resumability and Handlers

Resumability lets the browser continue from server-rendered output without hydrating the full component tree.

## What is serialized

A scope may contain:

- component/module id,
- serializable props,
- `useState` values,
- resolved async data,
- pending and error state,
- and references to generated browser modules.

Only values representable by the Resux JSON payload should cross the server/browser boundary.

## Safe state

```ts
const count = useState('counter', () => 0)
const filters = useState('filters', () => ({ query: '', active: true }))
```

Good values include strings, numbers, booleans, `null`, arrays, and plain objects made from those values.

Avoid functions, class instances, DOM nodes, streams, sockets, `Map`, `Set`, and private server clients.

## Safe handler captures

```ts
const count = useState('counter', () => 0)
const step = 2

function increment() {
  count.value += step
}
```

The compiler analyzes handlers and rejects captures it cannot safely reproduce. Imports intended for browser execution must be compatible with the configured package mode.

Move private or server-only work behind an API:

```ts
async function save() {
  await $fetch('/api/save', {
    method: 'POST',
    body: { value: count.value }
  })
}
```

## Delegated events

Resux installs shared event listeners and finds handler metadata in the event path. Named and supported inline handlers compile to browser modules.

```vue
<button @click="increment">Add</button>
<form @submit.prevent="save">...</form>
<input @keydown.enter="search" />
```

Supported modifier groups include control, system, mouse, and key filters. `.capture` and `.passive` are accepted syntax but still participate in the delegated runtime model.

## Reactive patches

The compiler records dynamic text, attributes, class, style, visibility, and HTML bindings. After a handler mutates a dependency, the resumed effect evaluates the relevant expressions and updates the matching DOM nodes.

```vue
<p :class="{ active: count > 0 }">{{ count }}</p>
```

## Watch cleanup

```ts
watchEffect((onCleanup) => {
  const timer = setInterval(refresh, 5000)
  onCleanup(() => clearInterval(timer))
})
```

Watch dependencies are cleaned before re-running, which prevents stale branches from continuing to trigger effects.

## Mounted cleanup

```ts
onMounted(() => {
  const controller = new AbortController()
  window.addEventListener('resize', handleResize, { signal: controller.signal })
  return () => controller.abort()
})
```

Mounted work runs when the scope first resumes in the browser, not during SSR.

## Client enhancements

Enhancement setup receives a target and context and may return a cleanup function:

```ts
export default defineClientEnhancement('tooltip', (target, context) => {
  const instance = createTooltip(target, context.options)
  return () => instance.destroy()
})
```

Use `useClientEnhancement` for manual control and `disposeClientEnhancements` for explicit global disposal in advanced integration code.

## Debugging

```sh
resux dev --trace-resume
resux inspect enhancements --json
resux inspect bundles --json
```

If a handler fails compilation, reduce captures, move work to a server endpoint, configure the package mode, or use a client enhancement/Vue island.
''')

write("docs/guide/app-shell-errors.md", r'''
# App Shell, Errors, and Public Files

## `app.vue`

`app.vue` is the optional outer application component. A common shell renders navigation, layout selection, the active page, and global UI.

```vue
<template>
  <div class="app-shell">
    <header>My App</header>
    <ResuxLayout>
      <ResuxPage />
    </ResuxLayout>
  </div>
</template>
```

Resux also checks `app/app.vue` when a root file is absent.

## Layout and page placeholders

- `<ResuxPage />` renders the matched page.
- `<ResuxLayout />` renders the layout selected by page metadata.
- `<slot />` renders page content inside a layout.

Avoid rendering the page twice by placing both `<ResuxPage />` and a layout that already contains the page placeholder incorrectly.

## `error.vue`

`error.vue` can render not-found and server errors. It may read the current error through `useError()`.

```vue
<script setup lang="ts">
const error = useError()

function recover() {
  clearError()
}
</script>

<template>
  <main>
    <h1>{{ error?.statusCode ?? 500 }}</h1>
    <p>{{ error?.message ?? 'Unexpected error' }}</p>
    <button @click="recover">Try again</button>
  </main>
</template>
```

Related APIs:

- `createError(input)` creates a structured error.
- `showError(input)` stores and throws a fatal render error.
- `useError()` returns the current error ref.
- `clearError()` clears it and emits the error-cleared hook.

## Server error responses

Server handlers may return a `Response`, a string, JSON-compatible data, `false`, a redirect result, or an abort result. Unhandled errors produce development diagnostics and a safer production response.

## Public files

Files under `public/` are served from `/`:

```txt
public/favicon.svg  -> /favicon.svg
public/robots.txt   -> /robots.txt
```

The server applies path-boundary checks to prevent traversal.

## Source assets

Resux also serves `/assets/*` from the app's `assets/` directory because compiled imports and configured CSS may resolve there.

For optimized images and video, prefer [Media and Optimization](/guide/media).

## Loading hooks and UI

The core hook system includes:

- `page:loading:start`
- `page:loading:end`
- `page:finish`
- `app:error`
- `app:error:cleared`

Modules or advanced integrations can use these hooks to implement loading indicators and centralized error reporting.
''')

write("docs/guide/components.md", r'''
# Components

Resux components use a compiler-supported `.vue` SFC subset and render without default Vue hydration.

## Basic component

```vue
<script setup lang="ts">
const props = defineProps<{ label: string; step?: number }>()
const emit = defineEmits<{ changed: [value: number] }>()
const count = useState('button-count', () => 0)

function increment() {
  count.value += props.step ?? 1
  emit('changed', count.value)
}
</script>

<template>
  <button @click="increment">
    {{ props.label }}: {{ count }}
  </button>
</template>

<style scoped>
button { font: inherit; }
</style>
```

A Resux component requires a `<template>` block. Plain CSS and scoped CSS are supported. Style modules, style `src`, and non-CSS style languages are rejected for resumable components.

## Setup macros

The setup context provides compiler-compatible helpers including:

- `defineProps`
- `defineEmits`
- `defineExpose`
- `defineSlots`
- `defineOptions`
- `defineModel`
- `definePageMeta`

Use only the behavior documented for Resux; these helpers do not imply complete Vue SFC compatibility.

## Auto-discovery

Components are discovered from:

- `components/`
- `app/components/`
- module-added component files
- module-added component directories

Generated component declarations are written under `.resux/types` and made available during preparation.

## Pages and layouts are components

Pages may define route metadata:

```ts
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth'],
  title: 'Dashboard',
  meta: [{ name: 'robots', content: 'noindex' }]
})
```

Layouts use `<slot />` to render the page.

## Built-in tags

| Tag | Purpose |
| --- | --- |
| `<ResuxPage />` | Active page placeholder |
| `<ResuxLayout />` | Selected layout wrapper |
| `<ResuxLink>` | Same-origin navigation-aware link |
| `<ResuxImg>` | Responsive optimized image |
| `<ResuxPicture>` | Art-direction picture sources |
| `<ResuxVideo>` | Deferred/optimized video with controls modes |
| `<VueIsland>` | Full Vue runtime boundary |

## Resumable events

Named handlers and supported inline expressions are compiled into client handler modules.

```vue
<button @click="count.value++">Increment</button>
```

Prefer named handlers for complex logic and clearer compile errors.

## Browser-only component work

`onMounted()` runs on the first browser resume of that scope.

```ts
onMounted(() => {
  const observer = new ResizeObserver(updateSize)
  observer.observe(document.body)
  return () => observer.disconnect()
})
```

For library-driven DOM behavior, a [client enhancement](/guide/package-integration#client-enhancements) is often a better boundary. For complete Vue lifecycle and rendering behavior, use [Vue Islands](/guide/vue-islands).

## UI package components

`resuxjs/ui` exports both `Rx*` and `Resux*` names for primitives including:

- Button, Input, Textarea, Select, DatePicker
- Card, Badge, Avatar, Alert, Divider, Skeleton, Kbd
- Accordion, Tabs, Switch, Dropdown, Popover, Tooltip, Modal
- Motion, Reveal, and AutoAnimate

These are Vue runtime components from the optional UI subpath; use them in an appropriate Vue/client context and read [UI & Motion Primitives](/guide/ui-animations).
''')

write("docs/guide/template-syntax.md", r'''
# Template Syntax

Resux parses templates with Vue compiler packages and emits its own resumable template model. Only the documented subset should be considered supported.

## Text and interpolation

```vue
<template>
  <h1>Hello {{ user.name }}</h1>
</template>
```

Refs are auto-unwrapped in template expressions. Script code still uses `.value`.

## Attributes

```vue
<button
  id="save"
  :disabled="pending"
  :aria-label="label"
  :class="['button', { active, loading: pending }]"
  :style="{ opacity: pending ? 0.5 : 1 }"
>
  Save
</button>
```

Dynamic bindings become patch targets.

## Events

```vue
<button @click="increment">Add</button>
<button @click="count.value = 0">Reset</button>
<form @submit.prevent="save">...</form>
<input @keydown.enter.exact="search" />
```

Supported modifier groups include:

- control: `prevent`, `stop`, `self`, `once`
- delegated syntax: `capture`, `passive`
- system: `ctrl`, `shift`, `alt`, `meta`, `exact`
- mouse: `left`, `middle`, `right`
- key filters: `enter`, `tab`, `delete`, `esc`, `escape`, `space`, `up`, `down`, `left`, `right`

The browser runtime remains delegated even when capture/passive syntax is accepted.

## Conditional chains

```vue
<p v-if="status === 'loading'">Loading</p>
<p v-else-if="status === 'error'">Failed</p>
<p v-else>Ready</p>
```

Adjacent `v-if`, `v-else-if`, and `v-else` branches are compiled as one conditional block.

## `v-show`

```vue
<section v-show="open">Panel</section>
```

Resux patches visibility without removing the element.

## Lists

```vue
<li v-for="(item, index) in items" :key="item.id">
  {{ index }} — {{ item.title }}
</li>
```

List locals are tracked so expressions and inline handlers can reference the item and index.

## Text and HTML

```vue
<p v-text="message" />
<div v-html="trustedHtml" />
```

Only use `v-html` with content you trust or sanitize. Do not rely on framework rendering as a substitute for application-specific HTML sanitization policy.

## Form model

```vue
<input v-model="form.name" />
<input type="checkbox" v-model="accepted" />
```

The model expression must be assignable, such as a ref, member expression, or indexed member expression.

## Template refs

Template ref bindings can be declared in setup and referenced from supported client work. Treat actual elements as browser-only values; do not put DOM nodes into resumable state.

## Built-in application tags

- `<ResuxPage />`
- `<ResuxLayout />`
- `<ResuxLink />`
- `<ResuxImg />`
- `<ResuxPicture />`
- `<ResuxVideo />`
- `<VueIsland />`
- `<slot />`

## Styles

```vue
<style scoped>
.card { padding: 1rem; }
</style>
```

Supported:

- plain CSS
- multiple style blocks
- scoped styles

Not supported for normal resumable components:

- `<style module>`
- `<style src>`
- preprocessors through `lang` such as Sass/Less

Use global CSS, Tailwind, modules that add CSS, or Vue islands when a different style pipeline is required.

## Unsupported directives

Unknown directives and unsupported SFC behavior should fail at compile time. This is intentional: Resux does not silently fall back to whole-component hydration.
''')

write("docs/guide/state.md", r'''
# State and Reactivity

Resux includes a native reactivity layer used by resumable components and exposed through `resuxjs` and `resuxjs/reactivity`.

## Local refs

```ts
const count = ref(0)
const doubled = computed(() => count.value * 2)
```

A plain `ref` participates in reactive rendering. Use `useState` when the value must be serialized and restored as named application state.

## Resumable state

```ts
const cart = useState('cart', () => ({ items: [] as string[] }))
```

Keys should be stable and unique for the intended scope/application behavior.

## Reactive objects

```ts
const form = reactive({
  name: '',
  tags: [] as string[]
})
```

Array index changes and length-dependent effects are tracked. Mutating an array can trigger both the changed index and relevant length dependencies.

## Computed values

```ts
const fullName = computed(() => `${form.name} (${form.tags.length})`)
```

Writable form:

```ts
const normalized = computed({
  get: () => form.name.trim(),
  set: value => { form.name = value }
})
```

## `watch`

```ts
const stop = watch(
  () => form.name,
  (next, previous, onCleanup) => {
    const controller = new AbortController()
    validateName(next, controller.signal)
    onCleanup(() => controller.abort())
  },
  { immediate: true }
)
```

Watching a reactive object is deep by default. Options include `immediate`, `deep`, `flush`, and `once` where supported by the current API.

## `watchEffect`

```ts
const stop = watchEffect((onCleanup) => {
  const id = setInterval(() => console.log(form.name), 1000)
  onCleanup(() => clearInterval(id))
})
```

Dependencies from stale conditional branches are removed before the next run.

## Readonly and conversion helpers

```ts
const readonlyForm = readonly(form)
const name = toRef(form, 'name')
const fields = toRefs(form)

isRef(name)
isReactive(form)
isReadonly(readonlyForm)
unref(name)
toRaw(form)
```

## Scheduler

```ts
form.name = 'Mahmoud'
await nextTick()
```

`nextTick` waits for queued reactive work to flush.

## Low-level reactivity

The focused `resuxjs/reactivity` entry also exports lower-level APIs such as `effect`, `stop`, and `isComputed`. Application components normally need the higher-level APIs documented above.

## Serialization rules

State included in the Resux payload must be JSON-compatible. Keep runtime-only objects outside `useState` and resolved async-data values.

For private or complex server state, store an identifier and retrieve the actual resource through a server endpoint.
''')

write("docs/guide/async-data.md", r'''
# Async Data and Fetching

Resux async resources expose reactive values while remaining serializable across SSR and browser resume.

## `useAsyncData`

```ts
const users = await useAsyncData('users', async ({ signal }) => {
  return $fetch<Array<{ id: number; name: string }>>('/api/users', { signal })
})
```

The resource contains:

```ts
type AsyncDataResource<T> = {
  data: Ref<T | undefined>
  value: Ref<T | undefined>
  pending: Ref<boolean>
  error: Ref<{ name: string; message: string } | null>
}
```

The resource is thenable. Awaiting it waits for the initial server-side resolution and returns the same ref-based shape.

## `useFetch`

```ts
const status = await useFetch<{ ok: boolean }>('/api/status')

if (status.error.value) {
  console.error(status.error.value.message)
}
```

`useFetch` returns an async-data resource, not a plain ref.

## `$fetch`

```ts
const result = await $fetch<{ saved: boolean }>('/api/items', {
  method: 'POST',
  body: { title: 'Example' }
})
```

`$fetch` resolves internal URLs correctly during SSR and returns parsed data directly.

## Native `fetch` and `apiURL`

```ts
const response = await fetch(apiURL('/api/status'))
```

Use `apiURL` when native `fetch` may execute during SSR. Resux resolves an absolute application origin from the route or public runtime config.

## Public origin configuration

```ts
export default defineResuxConfig({
  runtimeConfig: {
    public: {
      appOrigin: 'https://example.com'
    }
  }
})
```

Recognized public origin keys include `appOrigin`, `appURL`, `siteURL`, and `origin`.

## Cancellation and cleanup

The async-data handler receives an optional `AbortSignal`. Pass it to fetch operations so obsolete or disposed work can be cancelled.

```ts
const record = await useAsyncData(`record:${route.params.id}`, ({ signal }) =>
  $fetch(`/api/records/${route.params.id}`, { signal })
)
```

## Error behavior

Errors are serialized into a minimal `{ name, message }` shape. Do not depend on server stacks or private error properties reaching the browser.

For fatal page errors:

```ts
if (!record.data.value) {
  throw createError({ statusCode: 404, message: 'Record not found' })
}
```

## Key design

Use stable keys that represent the data identity. Avoid using one key for unrelated resources, because the state belongs to the rendered/resumed scope.

## Avoid duplicate fetching

Await the resource during SSR when the page needs the data to render. The resolved value is serialized, so the browser can resume without repeating the initial request.
''')
