# Middleware

Resux has route middleware for page navigation and server middleware for HTTP requests.

## Route middleware

Create a named file:

```ts
// middleware/auth.ts
export default defineResuxRouteMiddleware((to, from) => {
  if (to.path.startsWith('/admin')) {
    return navigateTo('/login', { statusCode: 302 })
  }
})
```

Attach it to a page:

```ts
definePageMeta({ middleware: ['auth'] })
```

## Global middleware

```txt
middleware/log.global.ts
```

Global middleware runs for every page navigation.

## Route middleware modes

Suffixes and module registration can produce server, client, or all-mode route middleware.

```txt
middleware/auth.server.ts
middleware/analytics.client.ts
```

## Return values

A route middleware can return:

- nothing to continue,
- a string destination,
- `false` to abort,
- `navigateTo(...)`,
- `abortNavigation(...)`,
- `{ redirect: ... }`,
- `{ type: 'redirect', to, statusCode }`,
- `{ type: 'abort', message, statusCode }`.

## Server middleware

```ts
// server/middleware/headers.ts
export default defineServerMiddleware((event) => {
  setHeader(event, 'x-app', 'resux')
})
```

Request middleware runs before APIs, custom routes, public files, generated media, and page rendering.

Use it for:

- request logging,
- authentication checks,
- request-scoped headers,
- rate-limit integration,
- and early response handling.

## Route rules versus middleware

Use route rules for static path-based behavior such as cache, CORS, headers, redirects, and status codes. Use middleware when logic depends on request data or external state.

## Module registration

```ts
resux.addRouteMiddleware({
  name: 'module-auth',
  src: './runtime/auth.ts',
  global: true,
  mode: 'all'
})
```

## Debugging

```sh
resux inspect middleware
resux inspect middleware --json
resux dev --trace-routes
```
