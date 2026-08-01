# Authentication Middleware Example

Authentication must be enforced on the server. Client route middleware improves navigation UX but is not the security boundary.

## Request middleware

Request middleware can apply shared policy, but it must not treat the presence of an `Authorization` header as proof of identity.

```ts
// server/middleware/private-cache.ts
export default defineServerMiddleware((event) => {
  if (event.path.startsWith('/api/private')) {
    setHeader(event, 'cache-control', 'private, no-store')
  }
})
```

## Signed-session verification

Keep token verification in a server-only utility. `verifySignedSessionToken` below represents your session provider or cryptographic verifier; it must verify the signature and claims such as expiry, issuer, and audience.

```ts
// server/utils/auth.ts
import { verifySignedSessionToken } from './session-provider'

export async function requireSession(event) {
  const authorization = event.node.req.headers?.authorization
  const token = typeof authorization === 'string' && authorization.startsWith('Bearer ')
    ? authorization.slice('Bearer '.length).trim()
    : ''

  const session = token
    ? await verifySignedSessionToken(token)
    : null

  if (!session) {
    return new Response('Unauthorized', { status: 401 })
  }

  return session
}
```

Adapt request-header access to the concrete Node/h3 event type used in your application. Never decode a token without verifying its signature and required claims.

## Protected API

```ts
// server/api/private/profile.ts
export default defineEventHandler(async (event) => {
  const session = await requireSession(event)

  if (session instanceof Response) {
    return session
  }

  return {
    id: session.userId,
    name: session.displayName
  }
})
```

Every protected handler must authorize the verified session for the requested operation. Authentication alone does not prove that a user may access every resource.

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

Route middleware is a navigation aid only. A client-visible session hint may be missing, stale, or manipulated, so private server operations still require verified credentials.

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
