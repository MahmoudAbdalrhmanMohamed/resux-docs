# Routing

Resux uses file-based routing from `pages/`.

## Basic routes

```txt
pages/index.vue       -> /
pages/about.vue       -> /about
pages/blog/index.vue  -> /blog
pages/blog/post.vue   -> /blog/post
```

## Dynamic params

Use square brackets:

```txt
pages/post/[id].vue -> /post/:id
```

Read params with `useRoute()`:

```vue
<script setup lang="ts">
const route = useRoute()
</script>

<template>
  <h1>Post {{ route.params.id }}</h1>
</template>
```

## Catch-all params

```txt
pages/docs/[...slug].vue -> /docs/:slug*
```

Catch-all params are exposed on `route.params`.

## Query strings

```ts
const route = useRoute()
const search = route.query.search
```

Query values are strings or string arrays.

## Links

Use `<ResuxLink>` for internal navigation:

```vue
<template>
  <ResuxLink to="/about">About</ResuxLink>
</template>
```

`ResuxLink` renders an anchor and is intercepted by the client runtime for same-origin navigation.

## Router composable

```vue
<script setup lang="ts">
const router = useRouter()

function goHome() {
  router.push('/')
}
</script>
```

Available methods:

```ts
router.push('/path')
router.replace('/path')
router.back()
router.forward()
router.go(-1)
```

On the server, router methods are no-ops. They become meaningful in the browser after resume.

## Client navigation model

For same-origin links, the browser runtime can:

- Prefetch route payloads on hover or focus.
- Fetch a fresh SSR route payload from `/__resux/route`.
- Show the built-in transition progress shell.
- Keep same-layout DOM in place.
- Swap the page slot.
- Update `<head>` and history.
- Clear non-persistent resumed page scopes.

## Route middleware

Use [Middleware](/guide/middleware) to redirect or abort navigation before rendering a page.
