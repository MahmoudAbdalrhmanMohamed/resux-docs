# Icon Runtime Loading and Resolution

Resux uses a tiered resolution strategy that maximizes build-time performance and minimizes client runtime requests:

## Tiered Resolution Architecture

When resolving an icon by name:

```txt
┌────────────────────────────────────────────────────────┐
│ 1. Compile-Time Inlining (Vite Plugin)                 │
│    Transforms static <Icon name="..." /> into inline   │
│    <svg> markup with 0 B client JavaScript overhead.   │
└──────────────────────────┬─────────────────────────────┘
                           │ not static / dynamic
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Local SVG Directory (assets/icons/)                 │
│    Reads custom:* SVG files directly from disk.        │
└──────────────────────────┬─────────────────────────────┘
                           │ not custom:*
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Offline Collections (@iconify-json/*)               │
│    Reads installed npm icon packages during SSR.       │
└──────────────────────────┬─────────────────────────────┘
                           │ not installed locally
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. In-Memory Registry (iconRegistry)                   │
│    Synchronously checks pre-registered icons.          │
└──────────────────────────┬─────────────────────────────┘
                           │ not found locally
                           ▼
┌────────────────────────────────────────────────────────┐
│ 5. Client Remote Fetcher (apiProvider)                 │
│    Fetches from Iconify API, caches, and renders.      │
└────────────────────────────────────────────────────────┘
```

## Client Remote Fetching

When an icon is not available at compile-time or locally in offline collections:

1. **Eager Fetch:** If `lazy: false`, fetching starts immediately after component mount.
2. **Lazy Fetch:** If `lazy: true` or `loading="lazy"`, the component registers an `IntersectionObserver` with a positive root margin, triggering the fetch only when the icon approaches the viewport.
3. **Request Deduplication:** Concurrent requests for the same icon share a single in-flight Promise.
4. **Response Caching:** Successful SVG responses are cached in memory. Subsequent renders resolve instantly without network round-trips.
5. **Stale-Request Protection:** If a dynamic icon name changes rapidly (e.g. in a search filter), obsolete responses are discarded so they never overwrite the active icon.

## SSR Behavior & Client-Only Icons

### Server-Side Rendering

By default, any icon that resolves locally (via offline collections, local SVGs, or `iconRegistry`) renders complete SVG markup directly into the server HTML stream.

### Client-Only Rendering (`:ssr="false"`)

For icons that should only render in the browser (e.g. icons in user profile menus or dynamic theme toggles):

```vue
<Icon name="lucide:user" :ssr="false" />
```

When `ssr: false`, Resux emits a lightweight placeholder element during SSR, then resolves and swaps the icon after client hydration.

## Programmatic API

Resux exports the core resolution helpers:

```ts
import {
  resolveIconSync,
  resolveIconAsync,
  fetchIconifyIcon,
  loadOfflineIcon,
  loadLocalSvgIcon
} from 'resuxjs/icons'

// Synchronous resolution (offline, local, or registry)
const staticData = resolveIconSync('lucide:check', config)

// Asynchronous resolution (including remote fetch fallback)
const iconData = await resolveIconAsync('lucide:check', config)
```

## Related

- [Icons overview](./index.md)
- [Usage and Registry](./usage.md)
- [Configuration](./configuration.md)
