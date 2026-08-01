# Resux Framework Tour

This page is the map of the complete Resux framework. Use it to understand what each subsystem does, where code runs, and which guide to read next.

## The framework in one sentence

Resux compiles a focused Vue-like single-file component format into server-rendered HTML, serialized state, and small event-handler modules that the browser imports only when interaction requires them.

Normal Resux components do **not** hydrate through the Vue runtime. Vue is available as an explicit island escape hatch for widgets that need full Vue behavior.

## End-to-end request lifecycle

1. The compiler discovers pages, layouts, components, plugins, middleware, server handlers, modules, and route rules.
2. `.vue` files are parsed into Resux component definitions and resumable handlers.
3. The server matches the request route and runs server middleware, route middleware, plugins, page setup, async data, layouts, and rendering.
4. The response contains HTML plus a serialized Resux payload describing route state, component scopes, async data, runtime config, plugins, middleware, and handler modules.
5. A small delegated browser runtime observes navigation and events.
6. When a user interacts, Resux imports only the required handler module, restores the associated scope, executes the handler, and patches the affected DOM.

Read [Rendering Lifecycle](/guide/rendering-lifecycle) and [Resumability and Handlers](/guide/resumability-handlers) for the detailed sequence.

## Framework subsystems

| Subsystem | Responsibility | Main documentation |
| --- | --- | --- |
| Compiler | Parses the supported SFC subset, discovers routes, emits manifests and handler modules | [Compiler Internals](/reference/compiler) |
| SSR runtime | Executes page setup, plugins, middleware, layouts, async data, and document rendering | [Runtime Internals](/reference/runtime) |
| Resume runtime | Restores serialized scopes and loads handlers on demand | [Resumability](/guide/resumability-handlers) |
| Reactivity | `ref`, `reactive`, `computed`, `watch`, `watchEffect`, readonly helpers, and scheduling | [Composables](/reference/composables) |
| Router | File routing, dynamic params, catch-all routes, route payload navigation, and middleware | [Routing](/guide/routing) |
| Server | API routes, request middleware, H3-compatible helpers, health checks, images, and videos | [Server API](/guide/server-api) |
| Modules | Build-time extensions for CSS, head entries, routes, imports, components, Vite, and Nitro | [Modules](/guide/modules-route-rules) |
| Package integration | SSR/client-only/progressive package modes and client enhancements | [Third-party Packages](/guide/package-integration) |
| Media | Responsive images, image transforms, cacheable generated assets, and video transforms | [Media](/guide/media) |
| Optional modules | i18n, icons, fonts, UI tokens, motion, security, and performance | [Package Exports](/reference/packages) |
| Deployment | Node server, Docker, Nitro output, Vercel, Netlify, Cloudflare, and static target selection | [Deployment](/guide/deployment) |
| Halal Core | Local policy scanning, reports, review approvals, integrity verification, and production guards | [Halal Core](/guide/halal-core) |
| CLI | Project creation, preparation, development, build, checks, inspection, deployment, and Halal commands | [CLI Reference](/reference/cli) |

## Public package entry points

The npm package is `resuxjs`. It exposes focused entry points so browser code does not accidentally import compiler or Node-only code:

```ts
import { ref, useState, useFetch } from 'resuxjs'
import { createResuxNodeHandler } from 'resuxjs/node'
import { renderApp } from 'resuxjs/runtime'
import { ref as runtimeRef } from 'resuxjs/reactivity'
import { defineResuxModule } from 'resuxjs/kit'
```

See [Package Exports](/reference/packages) for every published subpath and when to use it.

## Application directories

A complete application can use these conventions:

```txt
app.vue                 optional application shell
error.vue               optional error page
pages/                  file-system routes
layouts/                named page layouts
components/             reusable Resux components
plugins/                app plugins; .client and .server modes supported
middleware/             route middleware; .global, .client, and .server supported
server/api/             API routes
server/routes/          explicit server routes
server/middleware/      request middleware
modules/                local build-time modules
assets/                 source CSS and application assets
public/                 files served at the site root
locales/                optional i18n catalogs
resux.config.ts         framework configuration
resux.halal.config.ts   optional Halal Core project policy
```

Generated directories such as `.resux`, `.resux-nitro`, `.nitro`, and `.output` must not be edited manually.

## Execution contexts

Resux code can run in several different environments:

- **Build time:** compiler, module setup, templates, Vite and Nitro extension hooks.
- **Server request:** plugins, server middleware, route middleware, page setup, async data, SSR, and API handlers.
- **Browser resume:** delegated events, route payload navigation, client plugins and middleware, `onMounted`, and resumed handlers.
- **Vue island:** full Vue client runtime for an explicitly isolated widget.

Do not access `window` or `document` during SSR. Put browser-only work in `onMounted`, a client enhancement, a `.client` plugin, or a Vue island.

## Stable core and experimental boundaries

The documented compiler subset, SSR pipeline, payload format, resume model, routing conventions, native reactivity APIs, and core CLI workflow are the intended framework core.

Areas that require extra testing include broad Vue syntax compatibility, complex third-party browser libraries, provider-specific Nitro behavior, and Vue islands. Unsupported syntax should fail visibly rather than silently switching the entire application to hydration.

## Recommended reading order

1. [Getting Started](/guide/getting-started)
2. [Core Concepts](/guide/core-concepts)
3. [Rendering Lifecycle](/guide/rendering-lifecycle)
4. [Components](/guide/components) and [Template Syntax](/guide/template-syntax)
5. [State](/guide/state), [Async Data](/guide/async-data), and [Routing](/guide/routing)
6. [Configuration](/reference/configuration) and [Composables](/reference/composables)
7. The specialized guide for modules, packages, media, deployment, or Halal Core
