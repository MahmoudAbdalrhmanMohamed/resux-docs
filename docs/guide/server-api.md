# Server API

Resux apps can define server handlers under `server/api` and `server/routes`.

## API handler

```ts
// server/api/stats.ts
export default defineEventHandler(() => {
  return {
    response: 'ok',
    time: Date.now()
  }
})
```

This is available under `/api/stats`.

## Read query

```ts
// server/api/search.ts
export default defineEventHandler((event) => {
  const query = getQuery(event)

  return {
    q: query.q ?? ''
  }
})
```

## Read body

```ts
// server/api/messages.ts
export default defineEventHandler(async (event) => {
  const body = await readBody<{ message: string }>(event)

  return {
    saved: true,
    message: body.message
  }
})
```

## Set headers

```ts
export default defineEventHandler((event) => {
  setHeader(event, 'cache-control', 'no-store')
  return { ok: true }
})
```

## Fetch from pages

Use `$fetch` in code that may run during SSR:

```vue
<script setup lang="ts">
const { data } = await useAsyncData('stats', ({ signal }) => {
  return $fetch<{ response: string }>('/api/stats', { signal })
})
</script>
```

## Event shape

Server handlers receive an event with this practical shape:

```ts
type EventHandlerEvent = {
  path: string
  method: string
  query: Record<string, string | string[]>
  params: Record<string, string>
  node: {
    req: unknown
    res: unknown
  }
}
```

## Health endpoint

Production and dev servers expose:

```txt
/__resux/health
```

Use it for uptime checks and host probes.
