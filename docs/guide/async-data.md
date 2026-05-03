# Async Data

`useAsyncData` gives Resux a Nuxt-like async resource with resumable `data`, `pending`, and `error` refs.

## Return shape

```ts
const resource = useAsyncData('key', async ({ signal }) => {
  return { ok: true }
})

resource.data
resource.value
resource.pending
resource.error
```

`data` and `value` point at the same ref. `value` exists as a compatibility alias.

## SSR-first data

Await `useAsyncData` when you want data to be resolved during server rendering.

```vue
<script setup lang="ts">
type Stats = { response: string }

const { data, pending, error } = await useAsyncData('stats', ({ signal }) => {
  return $fetch<Stats>('/api/stats', { signal })
})
</script>

<template>
  <p v-if="pending">Loading</p>
  <p v-if="error">{{ error.message }}</p>
  <strong v-if="data">{{ data.response }}</strong>
</template>
```

## Skeleton-first data

Do not await when you intentionally want the server to render a skeleton and let the browser resume the pending scope.

```vue
<script setup lang="ts">
type Stats = { response: string }

const { data, pending, error } = useAsyncData('stats', ({ signal }) => {
  return $fetch<Stats>('/api/stats', { signal })
})
</script>

<template>
  <div v-if="pending" class="skeleton">Loading...</div>
  <p v-if="error">{{ error.message }}</p>
  <strong v-if="!pending && !error && data">{{ data.response }}</strong>
</template>
```

## Abort signal

The handler receives an optional `signal`. Pass it to `$fetch` or native `fetch` so pending browser requests can be aborted if the user leaves the route.

```ts
const { data } = useAsyncData('profile', ({ signal }) => {
  return $fetch('/api/profile', { signal })
})
```

## Error handling

`error` is a ref with a normalized shape:

```ts
type AsyncDataError = {
  name: string
  message: string
}
```

Always render errors while prototyping. It makes skeleton problems obvious:

```vue
<p v-if="error" role="alert">{{ error.message }}</p>
```

## Internal API URLs

During SSR, native `fetch('/api/test')` can fail because Node needs an absolute URL. Resux provides two helpers:

```ts
await $fetch('/api/test')
await fetch(apiURL('/api/test'))
```

On the server, Resux resolves internal `/api/...` paths against the current request origin, configured public origins, or `http://localhost:3000`. In the browser, internal URLs stay relative.
