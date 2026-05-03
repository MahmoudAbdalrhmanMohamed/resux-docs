# Core Concepts

Resux combines a compiler, an SSR runtime, a small browser resume runtime, and file conventions. The key idea is that normal Resux components are rendered on the server and resumed later only where interaction or pending data requires it.

## Concept map

| Concept | What it means | Read next |
| --- | --- | --- |
| Resux component | A `.vue` file compiled by Resux, not hydrated by the Vue runtime. | [Components](/guide/components) |
| Page | A component under `pages/` that becomes a route. | [Routing](/guide/routing) |
| Layout | A wrapper from `layouts/` selected by page meta. | [Layouts](/guide/layouts) |
| App shell | `app.vue`, the outer document-level component that renders the active page/layout. | [App Shell, Errors, and Public Files](/guide/app-shell-errors) |
| Error page | `error.vue`, the fallback renderer for 404/500 states. | [App Shell, Errors, and Public Files](/guide/app-shell-errors) |
| Public file | Static asset under `public/` served from the web root. | [App Shell, Errors, and Public Files](/guide/app-shell-errors) |
| Execution context | A place where code runs: module, plugin, middleware, handler, setup, resume, or island. | [Execution Contexts](/guide/execution-contexts) |
| Payload | Serialized route, scopes, state, async data, module ids, Vue island entries, and public config. | [Rendering Lifecycle](/guide/rendering-lifecycle) |
| Scope | The resumable runtime record for one rendered component instance. | [Resumability and Handlers](/guide/resumability-handlers) |
| Handler chunk | Browser code for a component event handler, imported on first interaction. | [Resumability and Handlers](/guide/resumability-handlers) |
| Async data | A resumable data resource with `data`, `pending`, and `error` refs. | [Async Data](/guide/async-data) |
| Route payload | Fresh SSR output fetched from `/__resux/route` during client navigation. | [Rendering Lifecycle](/guide/rendering-lifecycle) |
| Route middleware | Navigation guards from `middleware/`. | [Middleware](/guide/middleware) |
| Server middleware | Request middleware from `server/middleware/`, before APIs, public files, and pages. | [Middleware](/guide/middleware) |
| Server handler | API or route handler from `server/api` or `server/routes`. | [Server API](/guide/server-api) |
| Plugin | App extension that can provide values to Resux app context. | [Plugins](/guide/plugins) |
| Module | Build-time extension that can add CSS, head entries, route rules, and runtime config. | [Modules and Route Rules](/guide/modules-route-rules) |
| Route rule | Path-based response behavior such as redirects, headers, cache, CORS, and status codes. | [Modules and Route Rules](/guide/modules-route-rules) |
| Dev server | Vite-backed development server with generated client modules and reload channel. | [Dev Server and Build Output](/guide/dev-build-output) |
| Build output | Generated `.resux` internals and `.output` production server files. | [Dev Server and Build Output](/guide/dev-build-output) |
| Security headers | Default production hardening headers and path-specific policy. | [Security and Caching](/guide/security-caching) |
| Cache rule | Route-rule cache behavior for pages, payloads, APIs, and assets. | [Security and Caching](/guide/security-caching) |
| Health endpoint | Built-in `/__resux/health` endpoint for uptime checks. | [Dev Server and Build Output](/guide/dev-build-output) |
| Vue island | Opt-in full Vue runtime widget mounted inside a Resux page. | [Vue Islands](/guide/vue-islands) |

## How the parts fit

At build time, Resux discovers files, compiles `.vue` files, validates resumability, and emits server modules plus client handler modules. The build manifest records pages, components, layouts, plugins, middleware, server handlers, route rules, public runtime config, and island entries.

At request time, Resux runs request middleware and server handlers before rendering a page. For page requests, it runs route middleware, renders the app shell, layout, and page to HTML, merges head entries, and serializes the payload into `window.__RESUX__`.

In the browser, Resux starts with the server HTML. It intercepts same-origin navigation, fetches route payloads, swaps the page slot when possible, and imports handler chunks only when a user interaction needs them.

## What to keep in mind

- Use Resux components for HTML-first pages, simple interactivity, routing, layouts, SSR data, and resumable state.
- Use `useState` and `useAsyncData` for values that must survive from server render to browser resume.
- Use `$fetch` or `apiURL()` for internal API requests that may run during SSR.
- Use plugins for app context, modules for build-time extension, and route rules for response behavior.
- Use Vue islands when a feature needs full Vue runtime behavior or browser-only libraries.
- Expect unsupported Vue features or unsafe handler captures to fail at compile time.
