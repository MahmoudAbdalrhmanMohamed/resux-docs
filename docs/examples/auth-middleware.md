# Authentication Middleware Example

Authentication must be enforced on the server. Client route middleware improves navigation UX but is not the security boundary.

## Request middleware

```ts
// server/middleware/session.ts
export default defineServerMiddleware((event) => {
  const authorization = event.node.req.headers?.authorization
  if (event.path.startsWith('/api/private') && !authorization) {
    return new Response('Unauthorized', { status: 401 })
  }
})
```

Adapt request-header access to the concrete Node/h3 event type used in your application and use signed sessions rather than this simplified header example.

## Protected API

```ts
// server/api/private/profile.ts
export default defineEventHandler(() => ({
  id: 'user-1',
  name: 'Authenticated user'
}))
```

## Page route middleware

```ts
// middleware/auth.ts
export default defineResuxRouteMiddleware((to) => {
  const app = useResuxApp()
  const loggedIn = Boolean(app.provides.session)

  if (!loggedIn && to.path.startsWith('/account')) {
    return navigateTo('/login', { statusCode: 302 })
  }
})
```

```ts
// pages/account.vue
definePageMeta({ middleware: ['auth'] })
```

## Route rules

```ts
routeRules: {
  '/account/**': {
    cache: false,
    headers: { 'x-robots-tag': 'noindex' }
  },
  '/api/private/**': { cache: false }
}
```

Always authorize each private server operation even when page middleware already redirected unauthenticated users.
