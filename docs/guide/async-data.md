# Async Data and Fetching

Resux async resources expose reactive values while remaining serializable across SSR and browser resume.

## `useAsyncData`

```ts
const users = await useAsyncData('users', async ({ signal }) => {
  return $fetch<Array<{ id: number; name: string }>>('/api/users', { signal })
})
```

The resource contains:

```ts
type AsyncDataResource<T> = {
  data: Ref<T | undefined>
  value: Ref<T | undefined>
  pending: Ref<boolean>
  error: Ref<{ name: string; message: string } | null>
}
```

The resource is thenable. Awaiting it waits for the initial server-side resolution and returns the same ref-based shape.

## `useFetch`

```ts
const status = await useFetch<{ ok: boolean }>('/api/status')

if (status.error.value) {
  console.error(status.error.value.message)
}
```

`useFetch` returns an async-data resource, not a plain ref.

## `$fetch`

```ts
const result = await $fetch<{ saved: boolean }>('/api/items', {
  method: 'POST',
  body: { title: 'Example' }
})
```

`$fetch` resolves internal URLs correctly during SSR and returns parsed data directly.

## Native `fetch` and `apiURL`

```ts
const response = await fetch(apiURL('/api/status'))
```

Use `apiURL` when native `fetch` may execute during SSR. Resux resolves an absolute application origin from the route or public runtime config.

## Public origin configuration

```ts
export default defineResuxConfig({
  runtimeConfig: {
    public: {
      appOrigin: 'https://example.com'
    }
  }
})
```

Recognized public origin keys include `appOrigin`, `appURL`, `siteURL`, and `origin`.

## Cancellation and cleanup

The async-data handler receives an optional `AbortSignal`. Pass it to fetch operations so obsolete or disposed work can be cancelled.

```ts
const route = useRoute()
const record = await useAsyncData(`record:${route.params.id}`, ({ signal }) =>
  $fetch(`/api/records/${route.params.id}`, { signal })
)
```

## Error behavior

Errors are serialized into a minimal `{ name, message }` shape. Do not depend on server stacks or private error properties reaching the browser.

For fatal page errors:

```ts
if (!record.data.value) {
  throw createError({ statusCode: 404, message: 'Record not found' })
}
```

## Key design

Use stable keys that represent the data identity. Avoid using one key for unrelated resources, because the state belongs to the rendered/resumed scope.

## Avoid duplicate fetching

Await the resource during SSR when the page needs the data to render. The resolved value is serialized, so the browser can resume without repeating the initial request.
