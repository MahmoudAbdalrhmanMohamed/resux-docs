# Routing

Files under `pages/` and `app/pages/` become routes. The server route manifest remains the source of truth for SSR and client route-payload navigation.

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
pages/docs/[...slug].vue -> /docs/:slug(.*)
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

## Links

```vue
<ResuxLink to="/about">About</ResuxLink>
```

Eligible same-origin links are intercepted. External links, downloads, modifier-clicks, unsupported targets, and links explicitly handled by the browser continue normally.

## Client navigation lifecycle

For an internal navigation, Resux:

1. runs eligible client route middleware,
2. requests a route payload from the server,
3. lets server middleware and route middleware run,
4. handles redirect or abort responses,
5. updates document head and page content,
6. installs the new payload,
7. scans client enhancements,
8. emits loading and page-finish hooks.

Route payload responses use `cache-control: no-store` by default.

## Localized routes

When i18n is enabled, the compiler expands or resolves routes according to `prefix_except_default`, `prefix`, or `no_prefix` strategy. Use `localePath` and `switchLocalePath` instead of constructing locale prefixes manually.

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

Prefer normal page files unless a module genuinely owns the route.
