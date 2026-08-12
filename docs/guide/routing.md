# Routing

Files under `pages/` and `app/pages/` become routes. The generated route manifest is the source of truth for SSR matching and client route-payload navigation.

## Basic routes

```txt
pages/index.vue       -> /
pages/about.vue       -> /about
pages/blog/index.vue  -> /blog
```

## Dynamic parameters

```txt
pages/users/[id].vue  -> /users/:id
```

```ts
const route = useRoute()
route.params.id
```

## Catch-all parameters

```txt
pages/docs/[...slug].vue -> /docs/:slug*
```

Catch-all values are exposed through route params according to the generated matcher.

## Route context

```ts
const route = useRoute()

route.path
route.params
route.query
route.origin
route.userAgent
```

Repeated query keys may become string arrays.

## Page metadata

```ts
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth', 'audit'],
  title: 'Account',
  meta: [{ name: 'robots', content: 'noindex' }]
})
```

## Programmatic navigation

```ts
const router = useRouter()

await router.push('/account')
await router.replace('/login')
router.back()
router.forward()
router.go(-2)
```

## Links and prefetch

```vue
<ResuxLink to="/about">About</ResuxLink>
```

Eligible same-origin page links may prefetch their route payload on useful pointer/focus interaction. External URLs, `mailto:`, `tel:`, downloads, fragment-only navigation, API/framework-internal endpoints, unsupported targets, and browser-owned modifier clicks are not sent to `/__resux/route`.

Managed image/video asset links keep their media-specific browser/runtime behavior and are not mistaken for page routes.

## One shared route loader

Prefetch and intentional navigation converge on the same internal route-loading primitive. It owns:

- canonical cache keys,
- an in-memory success cache,
- one in-flight Promise per route key,
- speculative failure state/cooldown,
- navigation recovery,
- invalidation,
- deployment build compatibility checks.

This avoids separate hover/focus/click loaders drifting into different behavior.

## Route payload cache lifecycle

The route cache lives in JavaScript memory for the current browser document.

```txt
new document
  ↓
cache empty
  ↓
hover /media
  ↓
GET /__resux/route?path=/media
  ↓
success cached
  ↓
hover/focus /media again
  ↓
cache hit (no network)
  ↓
click /media
  ↓
reuse prefetched payload
```

A real reload creates a new browser document and therefore a fresh route cache. Resux does not persist this prefetch cache to `localStorage` or IndexedDB.

## Concurrent request deduplication

Concurrent loads for one canonical key share the same in-flight Promise:

```txt
prefetch('/media') ─┐
prefetch('/media') ─┼─> one network request
navigate('/media') ─┘
```

The request entry is removed when it settles. Successful payloads move into the memory cache.

## Cache keys

Route-payload keys are normalized from pathname plus query string. A trailing slash does not create a second key where router semantics are equivalent, and the fragment is excluded because a hash-only change does not require new server-rendered route HTML.

```txt
/media
/media/
/media#intro
```

reuse one route payload identity.

Queries stay in the key because they can affect server-rendered data:

```txt
/search?q=resux
/search?q=vue
```

are different entries. Dynamic path values are naturally distinct as well:

```txt
/products/1
/products/2
```

Localized paths are also distinct:

```txt
/en/media
/ar/media
```

so a payload rendered for one locale is never reused as the other locale.

## Failed speculative prefetch

A failed hover/focus prefetch enters a short failure cooldown. Repeated pointer events during that period do not create a 500 request storm.

An intentional navigation is authoritative: it can retry after a speculative failure rather than permanently inheriting the prefetch error. Shared route fetches also have a bounded timeout so an unresolved speculative request cannot remain pending forever.

## Invalidation and development

Resux can invalidate an individual route entry or the current document cache internally. Development/HMR invalidates the route-payload cache and in-flight/failure state when generated output changes, so prefetched content cannot hide source edits.

A production browser reload also resets the cache naturally because it creates a new runtime instance.

## Client navigation lifecycle

For an internal navigation Resux:

1. resolves/normalizes the target page route,
2. runs eligible client route middleware,
3. reuses or loads the route payload through the shared cache,
4. lets server middleware and route middleware run,
5. handles redirect/abort results,
6. verifies route-payload build compatibility,
7. updates document head and page content,
8. installs the new payload/resumability state,
9. scans client enhancements,
10. emits loading and page-finish hooks.

Route payload HTTP responses remain private/navigation data and are not turned into a globally shared CDN cache by the client-memory optimization.

## Deployment build compatibility

Each generated build carries a compatibility identifier derived from runtime/compiler and resumable application output. When an old browser document receives a route payload from a different deployment build, Resux clears the route memory state and performs a controlled full reload instead of attempting to resume incompatible handler/expression modules.

This protects long-lived tabs from stale-runtime/new-payload combinations that would otherwise surface as errors such as missing resumable handlers or missing generated expressions.

## Route cache vs asset HTTP cache

These are separate systems:

**Route payload cache**

- browser memory,
- per document,
- query/locale-aware,
- navigation reuse,
- speculative failure cooldown.

**Runtime/static assets**

- HTTP/browser/CDN caching,
- fingerprinted Vite JS/CSS may be long-lived,
- stable resumability endpoints such as `/__resux/runtime-client.mjs`, `/__resux/handlers/**`, and `/__resux/vue-islands/**` receive framework-owned revalidation/no-store safety so a new deployment cannot silently mix stable URLs from different builds.

Do not disable caching globally to solve a route-prefetch bug.

## Localized routes

When `resuxjs/i18n` is enabled, localization happens after base page route generation and page-extension hooks, before the final manifest is written. `prefix`, `prefix_except_default`, and `no_prefix` therefore affect real SSR/client route records, not only URL helper strings.

See [i18n and Localization](/guide/i18n).

## Route rules

```ts
export default defineResuxConfig({
  routeRules: {
    '/old': { redirect: { to: '/new', statusCode: 301 } },
    '/admin/**': {
      headers: { 'x-robots-tag': 'noindex' },
      cache: false
    }
  }
})
```

Exact patterns, single-segment wildcards, and recursive `/**` patterns are matched by specificity.

## Extending pages from a module

```ts
import { defineResuxModule, extendPages } from 'resuxjs/kit'

export default defineResuxModule({
  setup() {
    extendPages((pages) => {
      pages.push({
        id: 'module-page',
        path: '/module-page',
        file: '/absolute/path/to/page.vue'
      })
    })
  }
})
```

Prefer normal page files unless a module genuinely owns the route. The same extension point lets framework modules participate in route generation without application-specific rewrites.
