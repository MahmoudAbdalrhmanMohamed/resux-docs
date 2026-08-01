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
