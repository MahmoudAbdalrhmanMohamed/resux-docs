# Example: Auth Middleware

Protect pages with route middleware.

## Middleware file

```ts
// middleware/auth.ts
export default defineResuxRouteMiddleware((to) => {
  const loggedIn = false

  if (!loggedIn && to.path.startsWith('/dashboard')) {
    return navigateTo('/login', { statusCode: 302 })
  }
})
```

## Protected page

```vue
<script setup lang="ts">
definePageMeta({ middleware: 'auth', layout: 'dashboard' })
</script>

<template>
  <h1>Dashboard</h1>
</template>
```

## Global middleware

```ts
// middleware/log.global.ts
export default defineResuxRouteMiddleware((to, from) => {
  console.log(`${from.path} -> ${to.path}`)
})
```

For request-level auth that should run before APIs, static files, and pages, use `server/middleware` instead.
