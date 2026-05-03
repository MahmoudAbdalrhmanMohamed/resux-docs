# Runtime Internals

This page explains Resux runtime behavior so advanced users can debug builds and production issues.

## HTML document

The rendered document includes:

- Server-rendered HTML inside `#__resux`.
- A route transition shell inside `#__resux-loading`.
- Serialized payload assigned to `window.__RESUX__`.
- The runtime client module at `/__resux/runtime-client.mjs`.

## Payload shape

The payload contains route information, component scopes, module references, Vue island references, and public config.

```ts
type ResuxPayload = {
  route: RouteContext
  scopes: Record<string, SerializedScope>
  modules: Record<string, string>
  vueIslands?: Record<string, string>
  config?: RuntimeConfig
}
```

Each scope includes:

```ts
type SerializedScope = {
  id: string
  moduleId: string
  props?: Record<string, JsonValue>
  state: Record<string, JsonValue>
  asyncData: Record<string, SerializedAsyncData>
}
```

## DOM markers

The renderer marks dynamic DOM areas so the client runtime can patch only what changed. Examples include text markers, block markers, dynamic attribute markers, HTML markers, and event markers.

These are internal implementation details. Do not rely on marker names in app code.

## Client events

The browser runtime uses delegated listeners. When an event occurs:

1. The runtime reads the event marker.
2. It imports the matching handler module if needed.
3. It rebuilds the resumable scope from serialized props, state, async data, and route data.
4. It runs the handler.
5. It patches dynamic bindings for that scope.

## Route transitions

During client navigation the runtime can move through start, fetch, swap, complete, and error phases. The built-in progress shell is rendered by the document and updated by the client.

## Assets

Common runtime endpoints and assets:

| Path | Purpose |
| --- | --- |
| `/__resux/runtime-client.mjs` | Browser resume runtime. |
| `/__resux/route` | Fresh SSR route payload for client navigation. |
| `/__resux/handlers/**` | Client handler chunks. |
| `/__resux/vue-islands/**` | Vue island chunks. |
| `/__resux/dev-events` | Dev-only update channel. |
| `/__resux/health` | Health check endpoint. |

## Security headers

Production serving enables default hardening headers unless disabled with `--no-security-headers`.
