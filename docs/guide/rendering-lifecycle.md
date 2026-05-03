# Rendering Lifecycle

Resux has separate phases for compile time, request time, browser boot, client navigation, and interaction. Understanding those phases explains why the framework can ship HTML first without hydrating the whole page.

## Compile time

When you run `resux dev` or `resux build`, Resux discovers the app and creates a manifest.

The compiler records:

- Routes from `pages/`.
- Components from `components/`.
- Layouts from `layouts/`.
- App and error shells from `app.vue` and `error.vue`.
- Route middleware from `middleware/`.
- Request middleware from `server/middleware/`.
- Server handlers from `server/api` and `server/routes`.
- Plugins from `plugins/`.
- Vue islands from `islands/vue`.
- Runtime config, route rules, and modules from `resux.config.ts`.

For each supported `.vue` file, the compiler emits a server module for SSR and a client handler module for resumable events. It also validates template syntax and handler captures so unsupported patterns fail before the app silently falls back to hydration.

## Request time

For a normal page request, Resux follows this order:

1. Apply built-in security headers and matching route-rule headers.
2. Run request middleware from `server/middleware/`.
3. Match server API and server route handlers.
4. Match the page route and params.
5. Run global and page-selected route middleware.
6. Render plugins, app shell, layout, and page.
7. Resolve awaited `useAsyncData()` calls.
8. Collect `definePageMeta()`, `useHead()`, and `useSeoMeta()` entries.
9. Serialize the payload into the HTML document.

Server middleware can continue, redirect, abort, return JSON, return a `Response`, or write directly to the Node response. Server handlers are matched before page rendering, so `/api/...` requests do not pass through the page renderer.

## Payload shape

The browser receives a payload assigned to `window.__RESUX__`. Conceptually it contains:

```ts
type ResuxPayload = {
  route: RouteContext
  scopes: Record<string, SerializedScope>
  modules: Record<string, string>
  vueIslands?: Record<string, string>
  config?: RuntimeConfig
}
```

`runtimeConfig.public` is the only config section serialized to the browser. Keep secrets outside `public`.

## Browser boot

The browser starts with server-rendered HTML and the small Resux runtime.

It does not hydrate the whole component tree. Instead, it installs delegated listeners, keeps the serialized scopes available, and waits until a route change, pending async data, mounted hook, or user event needs runtime work.

## Client navigation

For same-origin links and router calls, Resux can:

- Prefetch route payloads on hover or focus.
- Fetch fresh SSR route output from `/__resux/route`.
- Show the built-in transition progress shell.
- Keep matching layout DOM in place.
- Swap only the page slot.
- Update `<head>` and browser history.
- Clear resumed page scopes that are no longer active.

This means navigation still uses server-rendered output, but avoids a full document reload when the runtime can safely swap the route.

## Interaction

When the user triggers a resumable event:

1. The delegated runtime reads the element metadata.
2. It finds the serialized scope and handler module id.
3. It imports the client handler chunk if it has not been loaded yet.
4. It recreates the resumable scope from serialized state and async data.
5. It runs the handler.
6. It patches marked text, attributes, HTML, and conditional/list blocks.

Only the affected bindings are patched. The rest of the page remains server-rendered HTML.
