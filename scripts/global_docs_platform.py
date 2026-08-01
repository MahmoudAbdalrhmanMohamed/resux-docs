from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dedent(content).strip() + "\n", encoding="utf-8")


write("docs/guide/routing.md", r'''
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
''')

write("docs/guide/layouts.md", r'''
# Layouts

Layouts wrap pages without adding whole-app hydration.

## Default layout

```vue
<!-- layouts/default.vue -->
<template>
  <div class="layout">
    <header>Site header</header>
    <main><slot /></main>
    <footer>Site footer</footer>
  </div>
</template>
```

Select it from a page:

```ts
definePageMeta({ layout: 'default' })
```

## Named layout

```txt
layouts/dashboard.vue
```

```ts
definePageMeta({ layout: 'dashboard' })
```

Layout names come from their file paths and are normalized by the compiler.

## Disable a layout

```ts
definePageMeta({ layout: false })
```

## App shell relationship

A common `app.vue` structure is:

```vue
<template>
  <ResuxLayout>
    <ResuxPage />
  </ResuxLayout>
</template>
```

The app shell is global. A layout is page-selectable. The page is the matched route component.

## Layout state

A layout is a normal Resux component and can use state, async data, head helpers, and resumable handlers. Keep state keys stable and serializable.

## Head composition

App, module, layout, and page head entries are composed rather than treated as one replace-only object. Arrays such as meta and links can accumulate; attributes are merged. Verify final output with:

```sh
resux inspect seo --json
```

## Localized layouts

Layouts do not need separate copies for each locale. Use i18n helpers and the current route locale inside the same component.
''')

write("docs/guide/head-seo.md", r'''
# Head and SEO

Resux composes global configuration, module contributions, page metadata, component head calls, and i18n alternate links into the rendered document head.

## Global head

```ts
export default defineResuxConfig({
  app: {
    head: {
      title: 'My App',
      meta: [
        { name: 'description', content: 'A Resux application' },
        { name: 'theme-color', content: '#111827' }
      ],
      link: [{ rel: 'icon', href: '/favicon.svg' }],
      htmlAttrs: { lang: 'en' },
      bodyAttrs: { class: 'app-body' }
    }
  }
})
```

Global/module head composition supports arrays such as `meta`, `link`, `script`, `style`, and `noscript`, plus merged HTML/body attributes.

## `useHead`

```ts
useHead({
  title: 'Pricing',
  meta: [{ name: 'description', content: 'Pricing options' }],
  link: [{ rel: 'canonical', href: 'https://example.com/pricing' }],
  htmlAttrs: { lang: 'en' }
})
```

Use structured entries rather than interpolating untrusted HTML into head fields.

## `useSeoMeta`

```ts
useSeoMeta({
  title: 'Product',
  description: 'Product details',
  robots: 'index,follow',
  ogTitle: 'Product',
  ogDescription: 'Product details',
  ogImage: 'https://example.com/og.png',
  twitterCard: 'summary_large_image',
  twitterImage: 'https://example.com/og.png'
})
```

The helper maps common keys to name/property meta entries.

## Page metadata

```ts
definePageMeta({
  title: 'Dashboard',
  meta: [{ name: 'robots', content: 'noindex' }]
})
```

For dynamic SEO, use `useHead` or `useSeoMeta` in setup.

## Image preload priority

The renderer can prioritize relevant head image preloads so critical images are discovered early. Use responsive media attributes and avoid preloading every image.

## i18n SEO

When enabled, i18n can add canonical and alternate `hreflang` links. Configure:

```ts
i18n: {
  seo: { hreflang: true }
}
```

## Inspect SEO

```sh
resux inspect seo
resux inspect seo --json
```

The SEO target checks route metadata and reports diagnostics such as missing canonical information in applicable test routes.

## Safety notes

- Escape or validate user-derived titles and URLs.
- Do not inject arbitrary scripts from user input.
- Keep canonical and Open Graph URLs absolute in production.
- Keep private runtime config out of head output.
''')

write("docs/guide/runtime-config.md", r'''
# Runtime Config

Runtime config separates server-only values from browser-visible public values.

## Configuration

```ts
export default defineResuxConfig({
  runtimeConfig: {
    databaseURL: process.env.DATABASE_URL,
    signingKey: process.env.SIGNING_KEY,
    public: {
      appOrigin: process.env.APP_ORIGIN,
      apiBase: '/api',
      environment: process.env.NODE_ENV ?? 'development'
    }
  }
})
```

## Read config

```ts
const config = useRuntimeConfig()
config.public.apiBase
```

Server handlers and server-mode plugins can read private values. Only `public` is serialized to the browser payload.

## Internal API origin

SSR URL resolution checks public keys such as:

- `appOrigin`
- `appURL`
- `siteURL`
- `origin`

Set an accurate production origin when internal native `fetch` calls depend on it.

## Module extension

```ts
resux.extendRuntimeConfig({
  public: {
    featureEnabled: true
  }
})
```

Nested config is merged. Resux blocks dangerous prototype keys such as `__proto__`, `prototype`, and `constructor` during deep merging.

## Environment strategy

Use environment variables for deployment-specific secrets and values. Keep a non-secret `.env.example` with names only.

```txt
DATABASE_URL=
APP_ORIGIN=
RESUX_HALAL_REPORT_SIGNING_SECRET=
```

Never commit actual keys.

## Serialization limits

Public config must be JSON-compatible. Functions, classes, symbols, open connections, and server clients cannot be serialized safely.
''')

write("docs/guide/plugins.md", r'''
# Plugins

Plugins extend the application context. They can run on the server, browser, or both depending on mode.

## Basic plugin

```ts
// plugins/01.app.ts
export default defineResuxPlugin((app) => {
  app.provide('appName', 'Resux App')
})
```

Read provided values through the app context:

```ts
const app = useResuxApp()
const appName = app.provides.appName
```

For stronger typing, augment `ResuxAppInjections` in an application declaration file.

## Execution modes

Filename suffixes:

```txt
plugins/analytics.client.ts
plugins/database.server.ts
plugins/shared.ts
```

Module-registered plugins can set `mode: 'client' | 'server' | 'all'` explicitly.

- `server`: emitted only for SSR/server setup.
- `client`: emitted only for browser runtime.
- `all`: participates in both where supported.

## Ordering

Plugins are sorted deterministically by normalized file path. Numeric prefixes are a useful way to make order obvious:

```txt
plugins/01.config.ts
plugins/02.analytics.client.ts
```

## Client enhancements

Files under `enhancements/`, `client-enhancements/`, and their `app/` equivalents are discovered as client-mode plugins and registered in the enhancement manifest.

```ts
export default defineClientEnhancement('chart', async (target, context) => {
  const chart = await createChart(target, context.options)
  return () => chart.destroy()
})
```

Use:

```ts
const enhancement = await useClientEnhancement('chart', {
  target: '#sales-chart',
  trigger: 'visible',
  options: { type: 'bar' }
})
```

## Server plugins

`server/plugins/` is reserved for server-only setup and package analysis. Use it for infrastructure initialization that should not become a browser plugin.

## Module-added plugins

```ts
resux.addPlugin({
  src: './runtime/plugin.ts',
  mode: 'client'
})
```

## Rules

- Never put server secrets in a client or all-mode plugin.
- Keep plugin setup deterministic.
- Return/attach cleanup for browser resources through enhancement APIs.
- Prefer server middleware for request-specific behavior.
- Prefer modules for build-time configuration and generated files.
''')

write("docs/guide/middleware.md", r'''
# Middleware

Resux has route middleware for page navigation and server middleware for HTTP requests.

## Route middleware

Create a named file:

```ts
// middleware/auth.ts
export default defineResuxRouteMiddleware((to, from) => {
  if (to.path.startsWith('/admin')) {
    return navigateTo('/login', { statusCode: 302 })
  }
})
```

Attach it to a page:

```ts
definePageMeta({ middleware: ['auth'] })
```

## Global middleware

```txt
middleware/log.global.ts
```

Global middleware runs for every page navigation.

## Route middleware modes

Suffixes and module registration can produce server, client, or all-mode route middleware.

```txt
middleware/auth.server.ts
middleware/analytics.client.ts
```

## Return values

A route middleware can return:

- nothing to continue,
- a string destination,
- `false` to abort,
- `navigateTo(...)`,
- `abortNavigation(...)`,
- `{ redirect: ... }`,
- `{ type: 'redirect', to, statusCode }`,
- `{ type: 'abort', message, statusCode }`.

## Server middleware

```ts
// server/middleware/headers.ts
export default defineServerMiddleware((event) => {
  setHeader(event, 'x-app', 'resux')
})
```

Request middleware runs before APIs, custom routes, public files, generated media, and page rendering.

Use it for:

- request logging,
- authentication checks,
- request-scoped headers,
- rate-limit integration,
- and early response handling.

## Route rules versus middleware

Use route rules for static path-based behavior such as cache, CORS, headers, redirects, and status codes. Use middleware when logic depends on request data or external state.

## Module registration

```ts
resux.addRouteMiddleware({
  name: 'module-auth',
  src: './runtime/auth.ts',
  global: true,
  mode: 'all'
})
```

## Debugging

```sh
resux inspect middleware
resux inspect middleware --json
resux dev --trace-routes
```
''')

write("docs/guide/server-api.md", r'''
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
  const query = getQuery(event)
  const body = await readBody<{ title: string }>(event)
  setHeader(event, 'cache-control', 'no-store')
  return { query, title: body.title }
})
```

The helpers delegate to h3 where appropriate.

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
''')

write("docs/guide/security-caching.md", r'''
# Security and Caching

Resux provides secure defaults and extension points, but application authorization, validation, dependency review, and infrastructure security remain the developer's responsibility.

## Production headers

The production Node server enables hardening headers including examples such as:

- `x-content-type-options`
- `referrer-policy`
- `x-frame-options`
- `cross-origin-opener-policy`
- restrictive `permissions-policy`

Disable them only when a trusted host or reverse proxy owns the complete policy:

```sh
resux start --no-security-headers
```

## Route rules

```ts
routeRules: {
  '/account/**': {
    cache: false,
    headers: { 'x-robots-tag': 'noindex' }
  },
  '/public-api/**': {
    cors: {
      origin: 'https://example.com',
      methods: ['GET'],
      headers: ['content-type']
    }
  },
  '/__resux/assets/**': {
    cache: { maxAge: 31536000 }
  }
}
```

`cache: false` produces `no-store`. String values are passed as cache-control. Object values support `maxAge` and `swr`.

## Default cache model

- route payloads and dynamic SSR data should not be cached accidentally,
- build-stable runtime/handler assets may use immutable caching,
- transformed media can use long-lived or configured persistent caching,
- user-specific APIs should normally use `no-store` unless carefully varied.

## Runtime config

Only `runtimeConfig.public` reaches the browser. Private keys belong in server-only config and files.

Deep config merging blocks prototype-pollution keys.

## Public files and traversal

Public, asset, generated media, and framework asset handlers resolve paths against explicit roots and reject paths outside those roots.

## Remote media

The media pipeline accepts HTTP(S) sources. Treat remote-source support as a network boundary:

- restrict sources at your application or proxy layer,
- avoid exposing unrestricted private-network fetching,
- limit payload sizes and timeouts at infrastructure level,
- and monitor transformation CPU usage.

## HTML and user content

Do not treat `v-html` as an authorization or sanitization system. Sanitize user-controlled HTML with a dedicated, well-maintained policy appropriate to your application.

## Halal Core

Halal Core scans policy categories and protects production reports with authenticated integrity when a signing secret is configured. It is an additional policy layer, not a replacement for application security review.

## Dependencies

Use package diagnostics and ordinary supply-chain tools:

```sh
resux inspect packages --json
npm audit
npm outdated
```

Pin and review sensitive server dependencies, and configure package modes so server-only code cannot leak into browser bundles.
''')

write("docs/guide/dev-build-output.md", r'''
# Dev Server, Diagnostics, and Build Output

## Development

```sh
resux dev
resux dev --host 0.0.0.0 --port 4000 --open
```

Development uses Vite middleware for generated client modules and an internal event stream for rebuild/reload notifications.

Useful diagnostics:

```sh
resux dev --debug
resux dev --trace-build
resux dev --trace-routes
resux dev --trace-resume
```

`--https` currently changes the emitted/opened URL but local transport remains HTTP; it is not a local TLS server switch.

## Preparation and checks

```sh
resux prepare
resux check
resux check --json
resux check --fix
```

Checks validate required files, generated directories, scripts, TypeScript setup, Nitro bridge files, and general build readiness.

## Compile and build

```sh
resux compile
resux build
```

- `compile` creates lower-level `.resux` output.
- `build` creates `.resux` output and deployable Nitro output.

## Preview and start

```sh
resux preview
resux start --host 0.0.0.0 --port 3000
```

Preview rebuilds when required assets are missing or stale. `start` is the production-oriented alias in the current CLI.

## Inspect targets

```sh
resux inspect routes
resux inspect plugins
resux inspect enhancements
resux inspect middleware
resux inspect imports
resux inspect components
resux inspect build
resux inspect images
resux inspect server
resux inspect packages
resux inspect templates
resux inspect bundles
resux inspect seo
```

Add `--json` for CI-friendly output.

## `.resux` map

```txt
.resux/
  client/
    runtime-client.mjs
    plugins/
    middleware/
    handlers/
    chunks/
    assets/
  server/
    manifest.mjs
    handlers/
    resux-plugins/
    resux-middleware/
    request-middleware/
  server-bundle/
  vite-client/
  templates/
  types/
  dev/
```

Exact files vary by enabled features.

## Internal endpoints

Examples include:

```txt
/__resux/health
/__resux/route
/__resux/runtime-client.mjs
/__resux/plugins/*
/__resux/middleware/*
/__resux/handlers/*
/__resux/vue-islands/*
/_resux/generated/images/*
/_resux/generated/videos/*
```

Treat internal URL shapes as framework implementation details unless documented for a specific integration.

## Tailwind automation

When `assets/css/tailwind.css` exists and a compatible Tailwind CLI is installed, development can start a Tailwind watcher and production builds generate minified CSS before bundling.

See [CSS and Tailwind](/guide/css-tailwind).
''')

write("docs/guide/vue-islands.md", r'''
# Vue Islands

Vue islands are an explicit escape hatch for widgets that need the full Vue runtime.

## When to use an island

Use a Vue island for:

- a Vue-specific component library,
- complex Vue lifecycle behavior,
- client-side rendering patterns outside the Resux compiler subset,
- or an existing Vue widget that is not practical to rewrite as a progressive enhancement.

Do not use islands by default for simple counters, forms, links, or server-rendered content.

## Create an island

```vue
<!-- islands/vue/CounterIsland.vue -->
<script setup lang="ts">
import { ref } from 'vue'
const count = ref(0)
</script>

<template>
  <button @click="count++">Vue count: {{ count }}</button>
</template>
```

Resux discovers islands and creates separate Vite client entries.

## Render an island

Use the island name through the supported island component convention in your Resux template. The surrounding page remains a Resux-rendered component; only the island subtree is mounted by Vue.

## Props

Pass JSON-compatible props so they can be represented safely in SSR output and client initialization.

## Boundaries

- Island state is Vue state, not automatically Resux resumable state.
- Island lifecycle is Vue lifecycle.
- Resux route navigation may replace the island container and mount a new instance.
- Global listeners and external library instances still require cleanup.
- Avoid sharing private server objects through props.

## Alternatives

Before using an island, consider:

- a Resux event handler,
- a client enhancement,
- a progressive package adapter,
- native HTML/CSS behavior,
- or a server-rendered interaction.

Client enhancements usually ship less framework runtime than a Vue island.
''')

write("docs/guide/troubleshooting.md", r'''
# Troubleshooting

## Run the standard diagnostic sequence

```sh
node --version
npm install
resux prepare
resux check --json
resux inspect build --json
resux build --debug --trace-build
```

Node must satisfy the framework engine requirement.

## Unsupported template or SFC syntax

Symptoms:

- `ResuxCompileError`
- unknown directive errors
- unsupported style language/module/src errors
- unsafe handler capture errors

Actions:

1. Compare the component with [Template Syntax](/guide/template-syntax).
2. Move browser-library behavior into a client enhancement or Vue island.
3. Keep normal component styles as plain CSS.
4. Reduce handler captures to serializable or browser-safe values.

## A handler works on SSR but not after clicking

Run:

```sh
resux dev --trace-resume
resux inspect bundles --json
```

Check that the handler is discoverable, its imports are browser-compatible, and the state it uses was serialized.

## A package appears in the wrong bundle

```sh
resux inspect packages --json
```

Configure `packages.mode`, `clientOnly`, `serverOnly`, `external`, `noExternal`, aliases, or a progressive adapter.

## Internal API fetch fails during SSR

Set a public app origin or use `$fetch`:

```ts
runtimeConfig: {
  public: { appOrigin: 'https://example.com' }
}
```

## `useFetch` access is incorrect

`useFetch` returns an async-data resource:

```ts
const result = await useFetch('/api/status')
console.log(result.data.value)
console.log(result.pending.value)
console.log(result.error.value)
```

## Image transforms return 501

Verify that `sharp` is installed and loadable in the server runtime. Check the requested format and source response.

## Video transforms return 501

Install `ffmpeg` or set:

```sh
export RESUX_FFMPEG_PATH=/absolute/path/to/ffmpeg
```

## Production start or deploy rejects the Halal report

Set `RESUX_HALAL_REPORT_SIGNING_SECRET` before the production build and use the same secret during production verification. Rebuild after changing the key.

## Review-required project cannot build

Generate the request:

```sh
resux halal submit-review
```

The current framework does not send it automatically. Obtain a valid signed approval file, place it at the project root, then run:

```sh
resux halal verify-review
```

## Generated files are missing

```sh
resux check --fix
resux prepare
```

Do not hand-edit `.resux` output.

## Dev changes are not visible

Check terminal build errors, then use `--trace-build`. Restart only after resolving syntax or watcher exclusions. Generated and dependency directories are intentionally ignored by the source watcher.

## Route does not match

```sh
resux inspect routes
resux dev --trace-routes
```

Verify file naming, dynamic segment placement, middleware result, localized route strategy, and route-rule redirects.
''')

write("docs/guide/css-tailwind.md", r'''
# CSS and Tailwind

Resux supports component CSS, global CSS, module-added CSS, and an integrated Tailwind CLI workflow.

## Component styles

```vue
<style scoped>
.card {
  padding: 1rem;
  border-radius: 0.75rem;
}
</style>
```

Normal Resux components support plain CSS and scoped styles. They do not currently support style modules, style `src`, or style preprocessors through `lang`.

## Global CSS

```ts
export default defineResuxConfig({
  css: [
    '/assets/css/main.css',
    '/assets/css/theme.css'
  ]
})
```

Modules can call `addCss` to contribute global styles.

## Tailwind

When the app contains `assets/css/tailwind.css` and a compatible Tailwind CLI dependency, Resux detects the pipeline.

Development starts a watcher. Production creates minified output before the Resux/Vite bundle.

A common input:

```css
@import "tailwindcss";
```

Or use the syntax required by your installed Tailwind version.

## Configuration discovery

Resux uses the available Tailwind CLI and passes a config file when one is detected. Keep Tailwind versions and syntax aligned with the package you install.

## Avoid duplicate pipelines

Do not run a second Tailwind watcher with `concurrently` unless you have intentionally disabled or bypassed the Resux-managed input. Duplicate writers can cause unnecessary rebuilds or file races.

## CSS from packages

Configure package CSS explicitly when automatic discovery is insufficient:

```ts
packages: {
  css: {
    swiper: ['swiper/css', 'swiper/css/navigation']
  }
}
```

## Performance

- Keep global CSS intentional.
- Avoid loading UI package CSS on routes that never use it.
- Prefer immutable caching for built CSS assets.
- Use critical font and media strategies rather than large blocking stylesheets.
''')

write("docs/guide/typescript-generated-types.md", r'''
# TypeScript and Generated Types

Generated applications use TypeScript declarations so Resux globals and discovered project features are available without manual imports.

## Application setup

A typical `tsconfig.json` includes:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "types": ["node", "resuxjs/globals"]
  },
  "include": [
    "**/*.ts",
    "**/*.tsx",
    "**/*.vue",
    "types/**/*.d.ts",
    "env.d.ts"
  ]
}
```

## Generate declarations

```sh
resux prepare
```

Preparation/build can generate declarations for:

- components,
- auto-imports,
- module type templates,
- build metadata,
- and framework globals.

Generated declarations live under `.resux/types` and should not be edited manually.

## App injections

Add type-safe plugin provides:

```ts
// types/app.d.ts
import 'resuxjs'

declare module 'resuxjs' {
  interface ResuxAppInjections {
    apiClient: {
      get<T>(url: string): Promise<T>
    }
  }
}
```

## Module type templates

```ts
addTypeTemplate({
  filename: 'my-module.d.ts',
  getContents: () => `declare const moduleFeatureEnabled: boolean`
})
```

## Compiler types

Tool authors can import build and compiler types from `resuxjs/compiler`. Application code should normally use `resuxjs` or focused runtime/reactivity subpaths.

## Validation

```sh
npm run typecheck
resux check
resux build
```

Type checking does not replace a framework build: the compiler also validates template support and resumability rules.
''')

write("docs/guide/testing-quality.md", r'''
# Testing and Quality

Resux applications should validate both ordinary TypeScript behavior and framework-specific compilation/build behavior.

## Recommended checks

```sh
npm run typecheck
resux check
resux build
```

`resux check` validates project structure and generated prerequisites. `resux build` validates SFC compilation, resumability rules, package modes, server output, and deployment integration.

## Starter tests

The create command can add test starter files:

```sh
npx create-resuxjs@latest my-app --features tests
```

Vitest is a natural choice for unit tests because the framework itself uses it, but applications may use another runner.

## Unit-test pure logic

Move data transforms and validation into `utils/`, `shared/`, or server utilities so they can be tested without a browser.

```ts
import { describe, expect, it } from 'vitest'
import { normalizeTitle } from '../utils/title'

describe('normalizeTitle', () => {
  it('trims titles', () => {
    expect(normalizeTitle('  Resux  ')).toBe('Resux')
  })
})
```

## Test server handlers

Handlers are ordinary functions around an event object. Test core behavior directly and add integration tests for HTTP response semantics.

## Test resumability

Important scenarios include:

- server-rendered initial state,
- first interaction module loading,
- DOM binding patches,
- conditional watcher dependency cleanup,
- route-payload navigation,
- enhancement activation and cleanup,
- and serialized async errors.

## CI example

```yaml
- run: npm ci
- run: npm run typecheck
- run: resux check --json
- run: npm run build
- run: npm test
```

## Documentation and package checks

Framework and module maintainers should also dry-run package output and inspect generated manifests. Documentation CI should build VitePress so broken internal links fail before merge.
''')

write("docs/reference/hooks.md", r'''
# Lifecycle Hooks Reference

The core hook system is available from `resuxjs/core` and through module context.

## Register a hook

```ts
export default defineResuxModule({
  setup(_options, resux) {
    const remove = resux.hook('build:done', ({ appRoot, outDir, mode }) => {
      console.log({ appRoot, outDir, mode })
    })

    // call remove() when a dynamically registered hook is no longer needed
  }
})
```

## Hook groups

### Configuration and application

- `config:resolved`
- `app:resolve`
- `app:templates`
- `app:templatesGenerated`

### Pages, imports, components, plugins, middleware

- `pages:extend`
- `pages:resolved`
- `imports:dirs`
- `imports:extend`
- `components:dirs`
- `components:extend`
- `plugins:dirs`
- `plugins:extend`
- `middleware:dirs`
- `middleware:extend`

### Vite

- `vite:extendConfig`
- `vite:serverCreated`
- `vite:compiled`

### Build

- `build:before`
- `build:manifest`
- `build:done`
- `build:error`

### Nitro

- `nitro:config`
- `nitro:init`
- `nitro:build:before`
- `nitro:build:public-assets`

### Preparation and development

- `prepare:types`
- `dev:reload`
- `dev:error`

### Page loading and errors

- `page:loading:start`
- `page:loading:end`
- `page:finish`
- `app:error`
- `app:error:cleared`

## Error behavior

Hooks run in registration order. A hook failure is wrapped with the hook name and stops the current hook call, so hook implementations should include useful context and avoid silently swallowing critical failures.

## Public core API

`resuxjs/core` exports `ResuxHooks`, `createResuxHooks`, hook payload types, the module container, config helpers, and core application creation APIs. It is intended primarily for modules, builders, and framework integrations.
''')

write("docs/reference/api-index.md", r'''
# Public API Index

This index groups the supported package entry points. Not every exported type is intended for ordinary application code; use the narrowest subpath for your task.

## `resuxjs`

The root entry re-exports the runtime application surface:

- reactivity: `ref`, `reactive`, `computed`, `watch`, `watchEffect`, `readonly`, `toRef`, `toRefs`, `unref`, checks, `nextTick`
- state/data: `useState`, `useAsyncData`, `useFetch`, `$fetch`, `apiURL`
- routing: `useRoute`, `useRouter`, `navigateTo`, `abortNavigation`
- app/config: `useRuntimeConfig`, `useResuxApp`, config/plugin/module factories
- head/errors: `useHead`, `useSeoMeta`, `useError`, `createError`, `showError`, `clearError`
- server helpers: event and middleware factories, `readBody`, `getQuery`, `setHeader`
- packages/enhancements: lazy package and client enhancement APIs
- device, i18n, and image helpers

## `resuxjs/reactivity`

Focused native reactivity APIs, including lower-level `effect`, `stop`, `isComputed`, scheduler helpers, refs, reactive/readonly proxies, and watchers.

## `resuxjs/runtime`

Renderer and runtime types/functions for advanced integrations:

- component and template definitions
- server setup context
- render functions and document rendering
- route/payload types
- runtime composables
- browser runtime source generation
- client enhancement registration and disposal

## `resuxjs/node`

```ts
import { createResuxNodeHandler } from 'resuxjs/node'
```

Creates the production Node request handler and enforces authenticated production report verification.

## `resuxjs/compiler`

- `buildProject`
- `compileVueFile`
- `compileVueSource`
- `createRouteManifest`
- `ResuxCompileError`
- build, route, component, plugin, middleware, handler, and island types

## `resuxjs/create`

Programmatic application creation and create-target safety validation.

## `resuxjs/i18n`

The i18n module, configuration factories, route/path helpers, translation helpers, head generation, and i18n types.

## `resuxjs/icons`

Icon module, Vue icon component, registry, provider normalization, collection helpers, and Iconify fetching.

## `resuxjs/fonts`

Fonts module, Google font descriptor helper, and fonts option types.

## `resuxjs/ui`

UI module, tokens, animation helpers/directives, `Rx*` primitives, and matching `Resux*` aliases.

## `resuxjs/kit`

Nuxt-style module authoring helpers:

- component/import/plugin/middleware/server handler registration
- generated templates and type templates
- page/runtime/Vite/Nitro extension
- route rules and prerender routes

Kit helpers require active module setup context.

## `resuxjs/core`

Core configuration, hooks, module container, contributions, and core app creation. Intended for builders and deep integrations.

## `resuxjs/globals`

Type-only global declarations used by generated applications. Include it through TypeScript `types`; do not import it for runtime behavior.
''')

write("docs/reference/compiler.md", r'''
# Compiler Reference

The compiler turns the Resux SFC subset and file conventions into server modules, browser modules, route records, manifests, diagnostics, and generated types.

## Main entry points

```ts
import {
  buildProject,
  compileVueFile,
  compileVueSource,
  createRouteManifest,
  ResuxCompileError
} from 'resuxjs/compiler'
```

## `buildProject`

```ts
const result = await buildProject(appRoot, outDir, {
  vite: 'build',
  server: 'bundle',
  traceBuild: false
})
```

Build options:

- `vite`: `build` or `dev`
- `server`: `bundle` or `modules`
- `hooks`: custom `ResuxHooks`
- `changedPath`: incremental development hint
- `traceBuild`: detailed diagnostics

The result includes routes, components, layouts, plugins, client enhancements, middleware, server middleware, server handlers, islands, route rules, and optional app/error components.

## Component output

A compiled component records:

- id, name, and file
- server and client source
- template nodes
- handlers
- styles and scope id
- page metadata
- expression transformation diagnostics

## Compile validation

The compiler rejects unsupported or unsafe input, including examples such as:

- missing template blocks,
- unsupported style languages,
- style modules and style `src`,
- unsupported directives,
- invalid conditional/list syntax,
- unsafe browser handler captures,
- and incompatible package usage.

`ResuxCompileError` can include file, line, and column information.

## Discovery

The build includes application conventions, module contributions, auto-import directories, client enhancements, server plugins/utilities, and package diagnostics.

## Generated outputs

Generated output includes server modules, Vite client entries, bundled client assets, manifests, diagnostics JSON, templates, and `.d.ts` files.

## Tooling guidance

Compiler APIs are intended for builders, tests, adapters, and framework tooling. Ordinary applications should use CLI commands rather than calling `buildProject` directly.
''')

write("docs/reference/runtime.md", r'''
# Runtime Reference

The runtime package contains server rendering definitions, application composables, route/payload types, and the generated browser runtime source.

## Server rendering

```ts
import { renderApp, renderDocument } from 'resuxjs/runtime'

const result = await renderApp({
  page,
  route,
  components,
  layouts,
  runtimeConfig,
  appHead,
  plugins
})

const html = renderDocument(result)
```

Advanced integrations may use `renderAppAsync`, `AsyncResuxRenderer`, template rendering helpers, and server setup context creation.

## Component model

The runtime represents compiled components with:

- a server setup function,
- template nodes,
- handlers,
- styles,
- optional page metadata,
- and stable module identifiers.

## Payload

```ts
type ResuxPayload = {
  route: RouteContext
  scopes: Record<string, SerializedScope>
  modules: Record<string, string>
  vueIslands?: Record<string, string>
  config?: RuntimeConfig
  plugins?: ClientPluginManifestRecord[]
  middleware?: ClientRouteMiddlewareManifestRecord[]
  pageMeta?: PageMeta
}
```

## Browser runtime

`getClientRuntimeSource()` generates the delegated resume runtime used by compiler output. It supports event dispatch, patches, navigation, plugins, client middleware, packages, enhancements, and cleanup.

## Client enhancements

Advanced APIs include:

- `defineClientEnhancement`
- `getClientEnhancement`
- `hasClientEnhancement`
- `scanClientEnhancements`
- `useClientEnhancement`
- `disposeClientEnhancements`

## Runtime types

The subpath exposes definitions for routes, handlers, middleware results, components, templates, bindings, app injections, package modes/adapters, media config, head/SEO input, errors, async data, and rendering.

## Stability

Runtime internals are lower-level than application composables. Generated client source shape and internal URLs may evolve; prefer documented high-level APIs for application code.
''')

write("docs/reference/file-conventions.md", r'''
# File Conventions Reference

## Resux components

| Path | Meaning |
| --- | --- |
| `app.vue` or `app/app.vue` | app shell |
| `error.vue` or `app/error.vue` | error component |
| `pages/**/*.vue` or `app/pages/**/*.vue` | routes |
| `layouts/**/*.vue` or `app/layouts/**/*.vue` | layouts |
| `components/**/*.vue` or `app/components/**/*.vue` | components |
| `islands/vue/**/*.vue` | Vue runtime islands |

## Support files

| Path | Meaning |
| --- | --- |
| `plugins/**/*.ts` | app plugins |
| `app/plugins/**/*.ts` | nested app plugins |
| `middleware/**/*.ts` | route middleware |
| `app/middleware/**/*.ts` | nested route middleware |
| `enhancements/**/*.ts` | client enhancements |
| `client-enhancements/**/*.ts` | client enhancements |
| `server/middleware/**/*.ts` | request middleware |
| `server/plugins/**/*.ts` | server plugins |
| `server/api/**/*.ts` | `/api` handlers |
| `server/routes/**/*.ts` | custom handlers |

## Auto-import directories

- `composables/`
- `utils/`
- `shared/`
- `server/utils/`
- module-added import directories

Exports from these directories contribute to generated import declarations and package analysis.

## Mode suffixes

- `.client.ts`
- `.server.ts`
- no suffix for all mode
- `.global.ts` for global route middleware

Suffixes can be combined according to the support-file parser.

## Route filenames

```txt
index.vue          index route
about.vue          static route
[id].vue           dynamic segment
[...slug].vue      catch-all segment
```

The same bracket rules apply to server handler discovery.

## Configuration and types

| File | Meaning |
| --- | --- |
| `resux.config.ts` | main app config |
| `resux.halal.config.ts` | safety policy |
| `nitro.config.ts` | Nitro configuration |
| `env.d.ts` | app/global type entry |
| `types/**/*.d.ts` | app augmentation |
| `.env.example` | environment variable names |

## Assets

- `public/` maps directly to root URLs.
- `assets/` contains source CSS/media and is served through a protected `/assets` mapping where needed.
- `assets/css/tailwind.css` activates the managed Tailwind pipeline when dependencies are available.

## Generated paths

- `.resux/`
- `.resux-nitro/`
- `.nitro/`
- `.output/`
- `.resux-generated/`

Do not commit or edit generated output unless a specific deployment workflow requires an artifact outside source control.
''')

write("docs/reference/release.md", r'''
# Release and Publishing

This page documents the framework repository's intended npm release process, not application deployment.

## CI versus publishing

Normal pushes and pull requests run validation. They do not publish npm packages.

A publish workflow should run only for an approved version tag or GitHub Release and should verify that the tag matches `package.json`.

## Required validation

Before publishing:

```sh
npm ci
npm run typecheck
npm run build
npm test
npm run pack:check
```

Package validation should verify native optional bindings, generated declarations, bundled output, templates, and `npm pack --dry-run` contents.

## Version and tag

```sh
npm version 0.3.1
git push origin main
git push origin v0.3.1
```

Use the actual intended version. Do not copy the example blindly.

## Trusted Publishing

The repository release workflow uses npm Trusted Publishing through GitHub OIDC with provenance rather than a long-lived `NPM_TOKEN`.

Configure the npm trusted publisher for:

- repository: `MahmoudAbdalrhmanMohamed/resux`
- workflow: `npm-publish.yml`
- the correct package scope/name and release environment

## One-time passwords

Automation should not attempt interactive OTP publishing. An OTP error indicates the workflow is using token/interactive authentication rather than a correctly configured trusted publisher, or the trusted publisher configuration does not match the workflow.

## Documentation coordination

Framework documentation can describe source behavior before it reaches npm only when the PR clearly states the dependency. Merge/release source changes before publishing docs that present them as generally available.

## Recovery

If a release fails:

1. inspect the exact workflow job and npm authentication mode,
2. do not reuse or move an already published version,
3. fix CI/configuration,
4. create a new patch version when package contents changed,
5. keep provenance and tag/package versions aligned.
''')
