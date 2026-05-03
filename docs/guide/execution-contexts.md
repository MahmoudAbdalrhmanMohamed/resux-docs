# Execution Contexts

Resux has several places where code can run. Choosing the right context keeps apps predictable and avoids putting server-only work into resumable browser handlers.

## Context table

| Context | Where it lives | When it runs | Use it for |
| --- | --- | --- | --- |
| Module | `resux.config.ts`, module specifier, local module file | Build time | Add CSS, head entries, route rules, runtime config |
| Plugin | `plugins/*.ts` | App render/runtime setup | Provide app values and shared setup |
| Request middleware | `server/middleware/*.ts` | Every HTTP request before handlers, public files, and pages | Headers, auth gates, redirects, request logging |
| Server handler | `server/api/*.ts`, `server/routes/*.ts` | Matched HTTP request | JSON APIs, custom routes, private server work |
| Route middleware | `middleware/*.ts` | Page navigation before rendering | Page guards, redirects, aborts |
| Page/layout/component setup | `.vue` files | SSR render and later browser resume when needed | HTML, resumable state, async data, handlers |
| Resumable handler | `@click`, `@submit`, named handlers | Browser interaction | Mutate resumable refs and patch bindings |
| Mounted hook | `onMounted()` in a Resux component | First browser resume of that scope | Browser-only setup tied to a Resux component |
| Vue island | `islands/vue/*.vue` | Browser mount | Full Vue runtime widgets |

## Build time

Modules run while Resux is building or preparing the dev manifest.

```ts
export default defineResuxModule({
  setup(_options, resux) {
    resux.addCss('/module.css')
    resux.addRouteRule('/secure/**', {
      headers: { 'x-module': 'enabled' }
    })
  }
})
```

Use modules for app-wide build extension. Do not use modules for request-specific data because there is no request yet.

## Request time

Request middleware runs before public files, API routes, server routes, and page rendering.

```ts
export default defineServerMiddleware((event) => {
  setHeader(event, 'x-app', 'resux')
})
```

Server handlers run only when their route matches.

```ts
export default defineEventHandler(() => {
  return { ok: true }
})
```

Use these files for secrets, database access, private tokens, and response-level behavior.

## Navigation time

Route middleware runs for page navigation. It can redirect or abort before the page renders.

```ts
export default defineResuxRouteMiddleware((to) => {
  if (to.path.startsWith('/admin')) {
    return navigateTo('/login')
  }
})
```

Route middleware is about page access. Request middleware is about HTTP request handling.

## Render time

Page, layout, and component setup runs during SSR. It should produce serializable state and HTML.

```ts
const route = useRoute()
const config = useRuntimeConfig()
const count = useState('count', () => 0)
```

If setup code can run during SSR, avoid direct `window`, `document`, browser storage, and browser-only constructors.

## Browser resume time

Event handlers and `onMounted()` run in the browser after a scope is resumed.

```ts
onMounted(() => {
  console.log('resumed')
})

function increment() {
  count.value++
}
```

Handlers should capture resumable values. Use server APIs for private work and Vue islands for full client widgets.

## Boundary rules

- Secrets belong in server handlers, request middleware, or private runtime config.
- Serializable UI state belongs in `useState()`.
- SSR or resumable data belongs in `useAsyncData()`.
- Internal API calls in SSR-capable code should use `$fetch()` or `apiURL()`.
- Browser-only libraries usually belong in Vue islands.
- Response headers and cache behavior belong in server middleware or route rules.

## Related pages

- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [Resumability and Handlers](/guide/resumability-handlers)
- [Middleware](/guide/middleware)
- [Server API](/guide/server-api)
- [Modules and Route Rules](/guide/modules-route-rules)
