# Server API

Resux discovers server handlers and executes them before page rendering when their route matches.

## API routes

```ts
// server/api/users.ts -> /api/users
export default defineEventHandler(() => [
  { id: 1, name: 'Mahmoud' }
])
```

## Dynamic API routes

```ts
// server/api/users/[id].ts -> /api/users/:id
export default defineEventHandler((event) => ({
  id: event.params.id
}))
```

## Custom routes

```ts
// server/routes/robots.txt.ts -> /robots.txt
export default defineEventHandler(() => 'User-agent: *\nAllow: /')
```

## Event shape

```ts
type EventHandlerEvent = {
  path: string
  method: string
  query: Record<string, string | string[]>
  params: Record<string, string>
  node: { req: unknown; res: unknown }
}
```

## Helpers

```ts
export default defineEventHandler(async (event) => {
  if (event.method !== 'POST') {
    return new Response('Method not allowed', { status: 405 })
  }

  const query = getQuery(event)

  let body: unknown
  try {
    body = await readBody(event)
  } catch {
    return new Response('Invalid request body', { status: 400 })
  }

  if (
    !body ||
    typeof body !== 'object' ||
    Array.isArray(body) ||
    !('title' in body) ||
    typeof body.title !== 'string' ||
    !body.title.trim()
  ) {
    return new Response('Title is required', { status: 400 })
  }

  setHeader(event, 'cache-control', 'no-store')
  return { query, title: body.title.trim() }
})
```

The helpers delegate to h3 where appropriate. TypeScript annotations do not validate network input, so validate parsed bodies at runtime before reading their fields.

## Response forms

A server handler may return:

- JSON-compatible data,
- a string,
- a Web `Response`,
- `false` for a forbidden response,
- a redirect result,
- an abort result,
- or a promise of any supported result.

```ts
return new Response('Created', { status: 201 })
```

## Route rules

Server handlers receive route-rule headers, cache, CORS, and default status behavior for their matched path.

## Internal requests

```ts
const result = await $fetch('/api/users')
```

Use `$fetch`, `useFetch`, or `apiURL` for SSR-safe internal URLs.

## Module-added handlers

```ts
resux.addServerHandler({
  route: '/api/module/status',
  handler: './runtime/status.ts',
  method: 'GET'
})
```

## Security

- Validate request bodies and parameters.
- Authorize access on the server.
- Avoid returning private errors or secrets.
- Set explicit cache policy for user-specific responses.
- Apply rate limiting at middleware, reverse proxy, or hosting layer.
