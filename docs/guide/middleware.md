# Middleware

Resux has two middleware layers:

1. Route middleware from `middleware/`, used for page navigation.
2. Request middleware from `server/middleware/`, used for every HTTP request before handlers, public files, and pages.

## Route middleware

Create a route middleware file:

```ts
// middleware/auth.ts
export default defineResuxRouteMiddleware((to, from) => {
  if (to.path.startsWith('/admin')) {
    return navigateTo('/login', { statusCode: 302 })
  }
})
```

Attach it to a page:

```vue
<script setup lang="ts">
definePageMeta({ middleware: 'auth' })
</script>
```

Use more than one:

```ts
definePageMeta({ middleware: ['auth', 'analytics'] })
```

## Global route middleware

Files ending in `.global.ts` run globally.

```ts
// middleware/analytics.global.ts
export default defineResuxRouteMiddleware((to) => {
  console.log('visiting', to.path)
})
```

## Route middleware results

A route middleware can:

| Return | Meaning |
| --- | --- |
| nothing | Continue navigation. |
| string | Redirect to that path. |
| `false` | Abort with forbidden behavior. |
| `navigateTo('/path')` | Redirect. |
| `abortNavigation('message')` | Abort navigation. |

## Request middleware

Request middleware runs before server handlers, static files, and pages.

```ts
// server/middleware/security.ts
export default defineServerMiddleware((event) => {
  setHeader(event, 'x-app', 'resux')

  if (event.path.startsWith('/private')) {
    return { type: 'redirect', to: '/login', statusCode: 302 }
  }
})
```

Request middleware can:

- Continue by returning nothing.
- Use helpers such as `setHeader(event, name, value)`.
- End the Node response directly when necessary.
- Return a `Response`.
- Return a JSON-serializable value.
- Return `false` for `403`.
- Return redirect or abort objects.

## When to use which

| Need | Middleware type |
| --- | --- |
| Protect a page route | Route middleware |
| Redirect before rendering page | Route middleware |
| Add headers to all responses | Request middleware |
| Short-circuit API/page/public requests | Request middleware |
| Inspect raw request/response | Request middleware |
