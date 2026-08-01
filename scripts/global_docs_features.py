from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dedent(content).strip() + "\n", encoding="utf-8")


write("docs/guide/icons.md", r'''
# Icons (`resuxjs/icons`)

The icons package provides a build-time module and a Vue runtime icon component backed by a local registry and optional Iconify-compatible HTTP provider.

::: warning Runtime boundary
`Icon` and `ResuxIcon` are Vue components. Use them inside a Vue island or another Vue/client runtime context. Registering the module can expose configuration and a named component, but it does not turn normal Resux components into hydrated Vue components.
:::

## Module configuration

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/icons', {
      component: 'Icon',
      mode: 'svg',
      apiProvider: 'https://api.iconify.design',
      collections: ['material-symbols', 'mdi', 'ph'],
      lazy: true
    }]
  ]
})
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `collections` | `string[]` | built-in/default list | Collections intended for the app. |
| `component` | `string` | `Icon` | Registered component name. |
| `mode` | `'css' | 'svg'` | `'svg'` | Rendering mode metadata. Current component renders SVG. |
| `apiProvider` | `string` | Iconify API | Base URL used for dynamic icon fetching. |
| `lazy` | `boolean` | `true` | Defer fetching until the icon becomes visible where supported. |

The normalized provider is stored in public runtime config so client instances use the same endpoint.

## Use in a Vue island

```vue
<script setup lang="ts">
import { ResuxIcon } from 'resuxjs/icons'
</script>

<template>
  <ResuxIcon
    name="ph:check-circle"
    size="1.5rem"
    color="currentColor"
    lazy
  />
</template>
```

## Local registry

Frequently used icons are available from `iconRegistry`. Registry records can contain one path or multiple paths with optional opacity and a custom `viewBox`.

```ts
import { iconRegistry } from 'resuxjs/icons'

iconRegistry['company:logo'] = {
  viewBox: '0 0 32 32',
  paths: [
    { d: '...', opacity: '0.7' },
    { d: '...' }
  ]
}
```

Use a stable application initialization point when extending the registry.

## Dynamic fetching

```ts
import { fetchIconifyIcon } from 'resuxjs/icons'

const data = await fetchIconifyIcon(
  'ph:check-circle',
  'https://api.iconify.design'
)
```

Dynamic behavior includes:

- provider URL normalization,
- cache keys that include provider and icon name,
- concurrent request deduplication,
- multi-path SVG parsing,
- safe fallback when a request fails,
- and stale-request protection when the component's name/provider changes before a request finishes.

## Lazy loading

When lazy mode is enabled and `IntersectionObserver` exists, the component waits until it approaches the viewport. Without observer support it loads immediately.

## Custom providers

Use HTTPS for public providers. Only configure a provider you trust because the client requests SVG data from it. Apply CSP and network allow-lists appropriate to your application.

```ts
['resuxjs/icons', {
  apiProvider: 'https://icons.example.com'
}]
```

## Helper

```ts
import { defineIconCollections } from 'resuxjs/icons'

const options = defineIconCollections(['mdi', 'ph'])
```

## Troubleshooting

- Confirm the icon name uses `collection:name` format.
- Confirm the provider returns Iconify-compatible JSON/SVG data.
- Check CSP `connect-src`.
- Check the element actually intersects the viewport when `lazy` is active.
- Use a local registry entry for critical icons that must not depend on a remote service.
''')

write("docs/guide/fonts.md", r'''
# Fonts (`resuxjs/fonts`)

The fonts module generates Google Fonts links, optional preconnects, and eager, preload, or page-load-deferred stylesheet behavior.

## Configuration

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      preconnect: true,
      strategy: 'eager',
      google: [
        {
          name: 'Inter',
          weights: [400, 500, 600, 700],
          display: 'swap',
          strategy: 'preload'
        },
        {
          name: 'Alexandria',
          weights: [300, 400, 500, 600, 700],
          display: 'swap',
          strategy: 'lazy',
          deferUntilPageLoad: true
        }
      ]
    }]
  ]
})
```

## Module options

| Option | Type | Default |
| --- | --- | --- |
| `google` | `ResuxFontFamilyInput[]` | `[]` |
| `preconnect` | `boolean` | `true` |
| `strategy` | `'eager' | 'preload' | 'lazy'` | `'eager'` |
| `deferUntilPageLoad` | `boolean` | `false` |

## Family options

| Property | Type | Behavior |
| --- | --- | --- |
| `name` | `string` | Required family name. Control characters are removed and URL encoding is applied. |
| `weights` | `(number | string)[]` | Values from 1–1000 or ranges such as `'100..900'`. Invalid entries are ignored. |
| `display` | Google font-display value | Invalid values fall back to `swap`. |
| `strategy` | eager/preload/lazy | Overrides the module default for the family. |
| `deferUntilPageLoad` | `boolean` | Explicitly controls deferred loading. |

## Strategies

### Eager

Adds a stylesheet link immediately.

### Preload

Adds a stylesheet preload and the stylesheet link. Preload does not replace the stylesheet.

### Lazy/page-load deferred

Adds a style preload and a small inline script that appends the stylesheet after `window.load`, or immediately if the document is already complete.

## Grouping

Families are partitioned into eager and lazy groups. Each group receives one Google Fonts CSS URL containing its normalized families.

## Public runtime metadata

The module exposes non-secret family configuration under `runtimeConfig.public.fonts`, including provider, names, strategy, and whether each family is deferred.

## Helper

```ts
import { googleFont } from 'resuxjs/fonts'

const inter = googleFont({
  name: 'Inter',
  weights: ['100..900'],
  display: 'swap'
})
```

## CSP

Google-hosted fonts usually require policy entries similar to:

```txt
style-src https://fonts.googleapis.com
font-src https://fonts.gstatic.com
```

The deferred mode uses an inline script, so a strict CSP may require a nonce/hash or a different loading strategy. Do not weaken CSP globally just to support one font loader.

## Performance guidance

- Use eager/preload only for genuinely critical families.
- Avoid downloading weights that are not used.
- Prefer `swap` or `optional` based on your typography requirements.
- Consider self-hosting when privacy, CSP, reliability, or regional performance requires it.
''')

write("docs/guide/i18n.md", r'''
# i18n and Localization (`resuxjs/i18n`)

Resux i18n provides localized route strategies, message loading, runtime translation helpers, text direction, locale switching, and optional canonical/`hreflang` head entries.

## Enable the module

Configuration can live under top-level `i18n` while the module is registered separately:

```ts
export default defineResuxConfig({
  modules: ['resuxjs/i18n'],
  i18n: {
    defaultLocale: 'en',
    fallbackLocale: 'en',
    strategy: 'prefix_except_default',
    locales: [
      { code: 'en', name: 'English', dir: 'ltr' },
      { code: 'ar', name: 'العربية', dir: 'rtl' }
    ],
    messages: {
      en: './locales/en.json',
      ar: () => import('./locales/ar.json')
    },
    seo: { hreflang: true }
  }
})
```

Options may also be passed inline in the module tuple; inline values override/merge with top-level configuration.

## Message sources

Each locale accepts:

- an inline plain object,
- a path string,
- a function returning a message object,
- or a dynamic import function.

JSON paths are read during module setup. Import failures resolve to an empty catalog rather than exposing a private stack to the client.

## Route strategies

| Strategy | Default locale | Other locales |
| --- | --- | --- |
| `prefix_except_default` | `/about` | `/ar/about` |
| `prefix` | `/en/about` | `/ar/about` |
| `no_prefix` | `/about` | `/about` |

The compiler localizes the route manifest and the runtime resolves the active locale from the path.

## `useI18n`

```ts
const {
  locale,
  dir,
  locales,
  defaultLocale,
  fallbackLocale,
  strategy,
  t,
  tm,
  resolveLocalized,
  localePath,
  switchLocalePath,
  setLocale
} = useI18n()
```

Examples:

```ts
const title = t('product.title', { name: 'Resux' })
const section = tm('navigation')
const localized = resolveLocalized({ en: 'Hello', ar: 'مرحبا' })
const arabicAbout = localePath('/about', 'ar')
await setLocale('ar')
```

## Global helpers

- `useLocalePath()`
- `useSwitchLocalePath()`
- `$t(key, params)`
- `$tm(key)`

## Nested lookup safety

Translation lookup reads own properties only and rejects dangerous prototype keys such as `__proto__`, `prototype`, and `constructor`. Message catalogs are still application input and should be reviewed like other content.

## Direction

```vue
<html :dir="dir" :lang="locale">
```

For the document root, prefer i18n-generated head attributes or `useHead` so SSR output has the correct language/direction before JavaScript.

## SEO

When `seo.hreflang` is enabled, Resux creates localized alternate links and canonical information from the route origin and configured locales.

## Missing keys

Translation falls back to the configured fallback locale, then to the key when no message can be resolved. Keep key naming stable and include fallback catalogs in tests.

## Direct utilities

The package also exports route, normalization, direction, translation, localized-value, and head-building utilities for module/tool authors.
''')

write("docs/guide/ui-animations.md", r'''
# UI and Motion (`resuxjs/ui`)

The optional UI package exports a Resux build-time module, design-token helpers, Web Animations API utilities, Vue directives, and Vue runtime components.

::: warning Vue runtime package
The UI components are implemented with Vue `defineComponent`, `ref`, and `onMounted`. Use them in Vue islands or an explicit Vue/client runtime integration. They are not zero-hydration Resux template primitives.
:::

## Module configuration

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/ui', {
      css: ['/assets/css/ui-overrides.css'],
      defaultStyles: true,
      tokens: {
        accent: '#03c8bf',
        radius: '12px'
      },
      animations: {
        enabled: true,
        defaultPreset: 'fade-up'
      }
    }]
  ]
})
```

The module can add CSS and public token/animation configuration. Component imports remain explicit in Vue code.

## Tokens

```ts
import { defineUiTokens } from 'resuxjs/ui'

export const tokens = defineUiTokens({
  accent: '#03c8bf',
  surface: '#0f172a'
})
```

## Animation helper

```ts
import { useAnimate } from 'resuxjs/ui'

const animation = useAnimate(element, {
  type: 'fade-up',
  duration: 400,
  delay: 100,
  easing: 'ease-out',
  fill: 'forwards'
})
```

Built-in presets:

- `fade-up`
- `fade-down`
- `scale-in`
- `slide-in-left`
- `slide-in-right`
- `pulse-glow`
- `bounce-in`

`useAnimate` returns `null` when there is no browser element, Web Animations support is missing, or reduced motion is requested.

## Directive

`vAnime` and `vAnimate` are aliases. They trigger when an element enters the viewport when `IntersectionObserver` is available.

```vue
<div v-anime="{ type: 'fade-up', duration: 500 }">Content</div>
```

## Components

Both `Rx*` and matching `Resux*` aliases are exported:

### Forms

- `RxButton` / `ResuxButton`
- `RxInput` / `ResuxInput`
- `RxTextarea` / `ResuxTextarea`
- `RxSelect` / `ResuxSelect`
- `RxDatePicker` / `ResuxDatePicker`
- `RxSwitch` / `ResuxSwitch`

### Content and feedback

- `RxCard`, `RxBadge`, `RxAvatar`, `RxAlert`
- `RxSkeleton`, `RxDivider`, `RxKbd`

### Overlays and navigation

- `RxModal`, `RxDropdown`, `RxPopover`, `RxTooltip`
- `RxAccordion`, `RxTabs`

### Motion and icons

- `RxMotion`, `RxReveal`, `RxAutoAnimate`, `RxIcon`

## Example island

```vue
<script setup lang="ts">
import { RxButton, RxModal } from 'resuxjs/ui'
import { ref } from 'vue'

const open = ref(false)
</script>

<template>
  <RxButton @click="open = true">Open</RxButton>
  <RxModal v-if="open" @close="open = false">
    Modal content
  </RxModal>
</template>
```

## Accessibility

The primitives provide structure and defaults, but application code must still test keyboard navigation, labels, focus management, contrast, reduced motion, and screen-reader behavior for the exact composition used.
''')

write("docs/guide/framework-tour.md", r'''
# Framework Tour

This tour maps the complete Resux framework surface and where to learn each part.

## 1. Create and validate

The create system offers eight templates and composable feature flags. Generated projects use `prepare`, `check`, TypeScript declarations, Nitro output, deployment files, and optional tests/Tailwind/media/i18n examples.

Start with [Getting Started](/guide/getting-started) and [Project Structure](/guide/project-structure).

## 2. Compiler and SFC subset

The compiler discovers application conventions, parses `.vue` files, validates resumability, emits server modules and browser handlers, analyzes package usage, and generates manifests/types.

Read [Components](/guide/components), [Template Syntax](/guide/template-syntax), and [Compiler Reference](/reference/compiler).

## 3. SSR and resumability

The server renders HTML and serializes route/scope data. The browser resumes handlers and patches compiler-marked bindings instead of hydrating the whole app.

Read [Rendering Lifecycle](/guide/rendering-lifecycle), [Mental Model](/guide/mental-model), and [Resumability and Handlers](/guide/resumability-handlers).

## 4. Routing and data

Pages become routes; layouts wrap pages; route middleware can redirect or abort; route payloads power same-origin navigation. State and async resources are serialized for browser continuation.

Read [Routing](/guide/routing), [State](/guide/state), [Async Data](/guide/async-data), and [Head and SEO](/guide/head-seo).

## 5. Server platform

Resux includes request middleware, APIs, custom routes, server utilities/plugins, route rules, security headers, media endpoints, and a Node handler/Nitro integration.

Read [Server API](/guide/server-api), [Middleware](/guide/middleware), [Security and Caching](/guide/security-caching), and [Deployment](/guide/deployment).

## 6. Modules, hooks, and Kit

Modules can contribute components, imports, plugins, middleware, server handlers, templates, types, route rules, prerender routes, Vite plugins, and Nitro config. Core hooks expose configuration, build, Vite, Nitro, loading, and error lifecycles.

Read [Modules and Route Rules](/guide/modules-route-rules), [Lifecycle Hooks](/reference/hooks), and [Package Exports](/reference/packages).

## 7. Progressive client behavior

Third-party packages can be SSR, client-only, server-only, or progressive. Named client enhancements support visibility, interaction, idle, page-load, immediate, and manual triggers with cleanup.

Read [Third-party Packages](/guide/package-integration) and [Progressive Package Example](/examples/progressive-package).

## 8. Optional feature packages

- [Media and Optimization](/guide/media)
- [Icons](/guide/icons)
- [Fonts](/guide/fonts)
- [i18n](/guide/i18n)
- [UI and Motion](/guide/ui-animations)
- [CSS and Tailwind](/guide/css-tailwind)

## 9. Vue islands

Use a Vue island where a widget needs full Vue behavior. The rest of the app remains server-rendered and resumable.

Read [Vue Islands](/guide/vue-islands).

## 10. Safety and integrity

Halal Core performs local policy scanning, writes human/machine reports, supports optional remote classification with redaction, and requires authenticated production reports. Review submission is currently manual.

Read [Halal Core](/guide/halal-core).

## 11. Operations

`prepare`, `check`, targeted `inspect`, trace flags, build output, health checks, and deployment generators support development and CI.

Read [Dev Server and Build Output](/guide/dev-build-output), [CLI Reference](/reference/cli), [Testing and Quality](/guide/testing-quality), and [Troubleshooting](/guide/troubleshooting).
''')

write("docs/examples/counter.md", r'''
# Counter Example

A counter demonstrates SSR state, resumable events, computed values, and reactive DOM patches.

```vue
<script setup lang="ts">
const count = useState('example-counter', () => 0)
const doubled = computed(() => count.value * 2)

function increment() {
  count.value++
}

function reset() {
  count.value = 0
}
</script>

<template>
  <section>
    <h1>Counter</h1>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubled }}</p>
    <button @click="increment">Increment</button>
    <button @click="reset" :disabled="count === 0">Reset</button>
  </section>
</template>
```

The server renders the initial values. The browser imports the generated handler module after the first relevant click, reconstructs the state, and patches the three dynamic bindings.

Use a stable state key and keep its value serializable.
''')

write("docs/examples/blog.md", r'''
# Blog Routes Example

## Files

```txt
pages/blog/index.vue
pages/blog/[slug].vue
server/api/posts/index.ts
server/api/posts/[slug].ts
```

## Blog list

```vue
<script setup lang="ts">
useSeoMeta({ title: 'Blog', description: 'Latest posts' })

const posts = await useFetch<Array<{ slug: string; title: string }>>('/api/posts')
</script>

<template>
  <main>
    <h1>Blog</h1>
    <p v-if="posts.pending">Loading…</p>
    <p v-else-if="posts.error">Could not load posts.</p>
    <ul v-else>
      <li v-for="post in posts.data" :key="post.slug">
        <ResuxLink :to="`/blog/${post.slug}`">{{ post.title }}</ResuxLink>
      </li>
    </ul>
  </main>
</template>
```

## Post page

```vue
<script setup lang="ts">
const route = useRoute()
const post = await useFetch<{ title: string; body: string }>(
  `/api/posts/${route.params.slug}`
)

if (!post.data.value) {
  throw createError({ statusCode: 404, message: 'Post not found' })
}

useSeoMeta({
  title: post.data.value.title,
  description: post.data.value.body.slice(0, 150)
})
</script>

<template>
  <article>
    <h1>{{ post.data.title }}</h1>
    <p>{{ post.data.body }}</p>
  </article>
</template>
```

Do not put unsanitized user HTML into `v-html`. Render structured content or sanitize it with an application policy.
''')

write("docs/examples/api-and-fetch.md", r'''
# API and Fetch Example

## Handler

```ts
// server/api/tasks.ts
export default defineEventHandler(async (event) => {
  if (event.method === 'GET') {
    return [{ id: 1, title: 'Learn Resux', done: false }]
  }

  if (event.method === 'POST') {
    const body = await readBody<{ title: string }>(event)
    if (!body.title?.trim()) {
      return new Response('Title is required', { status: 400 })
    }

    setHeader(event, 'cache-control', 'no-store')
    return { id: Date.now(), title: body.title.trim(), done: false }
  }

  return new Response('Method not allowed', { status: 405 })
})
```

## Page

```vue
<script setup lang="ts">
const tasks = await useFetch<Array<{ id: number; title: string; done: boolean }>>('/api/tasks')
const title = useState('new-task-title', () => '')
const saving = ref(false)

async function addTask() {
  if (!title.value.trim() || saving.value) return
  saving.value = true
  try {
    const created = await $fetch<{ id: number; title: string; done: boolean }>('/api/tasks', {
      method: 'POST',
      body: { title: title.value }
    })
    tasks.data.value = [...(tasks.data.value ?? []), created]
    title.value = ''
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <form @submit.prevent="addTask">
    <input v-model="title" />
    <button :disabled="saving">Add</button>
  </form>

  <p v-if="tasks.pending">Loading…</p>
  <p v-else-if="tasks.error">{{ tasks.error.message }}</p>
  <ul v-else>
    <li v-for="task in tasks.data" :key="task.id">{{ task.title }}</li>
  </ul>
</template>
```

`useFetch` returns refs for resource state. `$fetch` returns the parsed response directly.
''')

write("docs/examples/auth-middleware.md", r'''
# Authentication Middleware Example

Authentication must be enforced on the server. Client route middleware improves navigation UX but is not the security boundary.

## Request middleware

```ts
// server/middleware/session.ts
export default defineServerMiddleware((event) => {
  const authorization = event.node.req.headers?.authorization
  if (event.path.startsWith('/api/private') && !authorization) {
    return new Response('Unauthorized', { status: 401 })
  }
})
```

Adapt request-header access to the concrete Node/h3 event type used in your application and use signed sessions rather than this simplified header example.

## Protected API

```ts
// server/api/private/profile.ts
export default defineEventHandler(() => ({
  id: 'user-1',
  name: 'Authenticated user'
}))
```

## Page route middleware

```ts
// middleware/auth.ts
export default defineResuxRouteMiddleware((to) => {
  const app = useResuxApp()
  const loggedIn = Boolean(app.provides.session)

  if (!loggedIn && to.path.startsWith('/account')) {
    return navigateTo('/login', { statusCode: 302 })
  }
})
```

```ts
// pages/account.vue
definePageMeta({ middleware: ['auth'] })
```

## Route rules

```ts
routeRules: {
  '/account/**': {
    cache: false,
    headers: { 'x-robots-tag': 'noindex' }
  },
  '/api/private/**': { cache: false }
}
```

Always authorize each private server operation even when page middleware already redirected unauthenticated users.
''')

write("docs/examples/progressive-package.md", r'''
# Progressive Package Example

This example loads a DOM library only when a target becomes visible and disposes it when the page changes.

## Configure package mode

```ts
export default defineResuxConfig({
  packages: {
    mode: {
      'chart-library': 'progressive'
    },
    css: {
      'chart-library': ['chart-library/styles.css']
    },
    diagnostics: true
  }
})
```

## Enhancement

```ts
// enhancements/sales-chart.client.ts
export default defineClientEnhancement('sales-chart', async (target, context) => {
  const library = await useClientPackage<typeof import('chart-library')>('chart-library')
  const instance = library.createChart(target, context.options)

  return () => {
    instance.destroy()
  }
})
```

## Activate from a component

```vue
<script setup lang="ts">
onMounted(async () => {
  await useClientEnhancement('sales-chart', {
    target: '#sales-chart',
    trigger: 'visible',
    options: {
      labels: ['Jan', 'Feb', 'Mar'],
      values: [10, 18, 25]
    }
  })
})
</script>

<template>
  <div id="sales-chart" aria-label="Sales chart"></div>
</template>
```

## Debug

```sh
resux inspect enhancements --json
resux inspect packages --json
resux inspect bundles --json
```

The actual package API is illustrative. Follow the cleanup API provided by the package you integrate.
''')

write("docs/examples/media-optimization.md", r'''
# Media Optimization Example

## Responsive image

```vue
<ResuxImg
  src="/images/hero.jpg"
  alt="Product preview"
  width="1200"
  height="675"
  sizes="(max-width: 768px) 100vw, 1200px"
  format="webp"
  quality="80"
  cache="7d"
  loading="eager"
  fetchpriority="high"
/>
```

The image builder creates a deterministic generated route for the transform. `sharp` performs resizing/format conversion on the server.

## Art direction

```vue
<ResuxPicture
  :sources="[
    { media: '(max-width: 640px)', src: '/images/hero-mobile.jpg', width: 640 },
    { media: '(min-width: 641px)', src: '/images/hero.jpg', width: 1200 }
  ]"
  src="/images/hero.jpg"
  alt="Product preview"
/>
```

## Deferred video

```vue
<ResuxVideo
  src="/videos/demo.mp4"
  poster="/images/demo-poster.jpg"
  load-strategy="page-ready"
  controls-mode="custom"
  format="webm"
  quality="720"
  cache="7d"
/>
```

Video transforms require `ffmpeg` in `PATH` or `RESUX_FFMPEG_PATH`.

## Operational safeguards

- Keep source media under trusted origins.
- Limit transform dimensions and cache duration.
- Monitor CPU, memory, source size, and request rates.
- Pre-generate popular variants when traffic is high.
- Use CDN/reverse-proxy caching in front of deterministic generated URLs.
''')

write("docs/examples/docker.md", r'''
# Docker Deployment Example

Generate the maintained Docker files:

```sh
resux deploy . --preset docker
```

Review the generated `Dockerfile`, `.dockerignore`, and `DEPLOYMENT.md` before deploying.

## Build

```sh
export RESUX_HALAL_REPORT_SIGNING_SECRET='private-random-secret-at-least-32-characters'
docker build \
  --build-arg RESUX_HALAL_REPORT_SIGNING_SECRET="$RESUX_HALAL_REPORT_SIGNING_SECRET" \
  -t resux-app .
```

Avoid baking long-lived secrets into image layers. Prefer your CI platform's secret mounts/build secrets and pass the same report verification secret securely at runtime when required by the generated production guard.

## Run

```sh
docker run --rm \
  -p 3000:3000 \
  -e PORT=3000 \
  -e RESUX_HALAL_REPORT_SIGNING_SECRET="$RESUX_HALAL_REPORT_SIGNING_SECRET" \
  resux-app
```

## Health check

```txt
GET /__resux/health
```

## Production checklist

- run as a non-root user where practical,
- use a read-only filesystem except required cache/temp paths,
- set memory/CPU limits,
- terminate TLS at a trusted proxy or platform,
- configure logs and graceful shutdown,
- protect environment variables,
- and scan the final image and dependency tree.
''')

write("docs/community/contributing.md", r'''
# Contributing to the Documentation

Documentation changes should be checked against the actual Resux source, package export map, tests, generated templates, and CLI help.

## Local setup

```sh
npm ci
npm run dev
```

## Validate

```sh
npm run build
```

The VitePress build validates rendering and internal links.

## Source-of-truth order

1. Current framework source and public export map.
2. Tests that assert behavior.
3. Generated starter templates and CLI help.
4. Released package behavior for release-specific claims.
5. Existing documentation only after comparison with the above.

## Writing rules

- Do not hard-code npm `latest` as permanent.
- Distinguish source-branch behavior from published behavior.
- State whether an API is server, browser, Vue, build-time, or resumable.
- Use complete runnable examples with correct return shapes.
- Document security and cleanup boundaries.
- Do not claim automatic email/upload/review behavior that does not exist.
- Prefer links to dedicated guides over duplicating long explanations.

## Pull requests

Include:

- the framework source/ref used,
- pages changed,
- behavior corrected or added,
- validation commands and results,
- and any dependency on an unmerged framework PR.
''')

write("docs/index.md", r'''
---
layout: home

hero:
  name: Resux
  text: HTML-first resumable framework
  tagline: Compile Vue-like SFCs into server-rendered HTML, serialized state, and interaction-loaded browser modules—with routing, server APIs, modules, deployment, and optional Vue islands.
  image:
    src: /logo.svg
    alt: Resux logo
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: Framework Tour
      link: /guide/framework-tour
    - theme: alt
      text: API Index
      link: /reference/api-index

features:
  - icon: SSR
    title: Server HTML first
    details: Render app shells, layouts, pages, head metadata, state, and async data on the server.
  - icon: RESUME
    title: Resume on interaction
    details: Import generated handler code only when an event or progressive enhancement needs it.
  - icon: ROUTE
    title: Full application platform
    details: File routes, middleware, APIs, plugins, modules, hooks, route rules, and Nitro deployment are integrated.
  - icon: PACKAGE
    title: Controlled package compatibility
    details: Declare SSR, client-only, server-only, or progressive third-party package behavior and inspect diagnostics.
  - icon: MEDIA
    title: Optimized media
    details: Responsive images, persistent generated variants, video deferral, sharp transforms, and ffmpeg support.
  - icon: SAFE
    title: Explicit boundaries
    details: Compiler errors, serializable state, production report integrity, security defaults, and documented experimental limits.
---

## Create a project

```sh
npx create-resuxjs@latest my-app
cd my-app
npm install
npm run dev
```

Node.js `>=20.19.0` is required by the current framework source.

## Learn by area

| Goal | Read |
| --- | --- |
| Understand the architecture | [Framework Tour](/guide/framework-tour) and [Mental Model](/guide/mental-model) |
| Build components and routes | [Components](/guide/components), [Template Syntax](/guide/template-syntax), [Routing](/guide/routing) |
| Load data and manage state | [State](/guide/state), [Async Data](/guide/async-data) |
| Build APIs and middleware | [Server API](/guide/server-api), [Middleware](/guide/middleware) |
| Integrate libraries | [Third-party Packages](/guide/package-integration), [Vue Islands](/guide/vue-islands) |
| Extend the framework | [Modules](/guide/modules-route-rules), [Hooks](/reference/hooks), [API Index](/reference/api-index) |
| Optimize assets | [Media](/guide/media), [Fonts](/guide/fonts), [Icons](/guide/icons), [CSS/Tailwind](/guide/css-tailwind) |
| Deploy safely | [Deployment](/guide/deployment), [Security](/guide/security-caching), [Halal Core](/guide/halal-core) |

## Important release note

The documentation follows the current source work referenced by its pull request. The npm `latest` tag may temporarily expose an older feature set. Check `npm view resuxjs version` and the framework release notes before relying on a source-only capability.
''')

write("README.md", r'''
# Resux Documentation

VitePress documentation for the complete Resux framework surface.

The site covers:

- architecture, compiler, SSR, resumability, routing, layouts, state, async data, and errors,
- plugins, middleware, server APIs, modules, Kit, hooks, generated templates/types, and route rules,
- third-party package modes, client enhancements, Vue islands, UI, icons, fonts, i18n, media, CSS, and Tailwind,
- create templates/features, CLI commands, targeted inspection, diagnostics, testing, deployment, release automation, security, and Halal Core,
- examples for counters, routes, APIs, authentication, progressive packages, media, and Docker.

## Source alignment

Documentation changes must identify the framework source or release used as the source of truth. The current global audit is aligned with `MahmoudAbdalrhmanMohamed/resux` branch `audit/full-history-correctness` at commit `35f00b0ddb68b098cb1def4c59356f722c5db72b`.

Some documented changes depend on the corresponding framework pull request being merged and released.

## Local development

```sh
npm ci
npm run dev
```

## Validate

```sh
npm run build
```

The repository includes Documentation CI for pushes and pull requests.

## Deployment

The VitePress site is configured for GitHub Pages under `/resux-docs/`.
''')

write("docs/public/llms.txt", r'''
# Resux Documentation Index

Resux is an HTML-first experimental web framework with a custom Vue-like SFC compiler, SSR renderer, serialized resumable state, delegated event runtime, route payload navigation, server APIs, modules, hooks, package modes, media optimization, deployment adapters, optional Vue islands, and a local safety/integrity subsystem.

Framework source: https://github.com/MahmoudAbdalrhmanMohamed/resux
Documentation source: https://github.com/MahmoudAbdalrhmanMohamed/resux-docs
Package: resuxjs
Node requirement in current source: >=20.19.0

Do not assume the npm latest version permanently matches the source documentation. Check the package version and release notes.

Start:
- /guide/framework-tour
- /guide/what-is-resux
- /guide/getting-started
- /guide/project-structure
- /guide/mental-model

Core:
- /guide/rendering-lifecycle
- /guide/resumability-handlers
- /guide/components
- /guide/template-syntax
- /guide/state
- /guide/async-data
- /guide/routing
- /guide/layouts
- /guide/head-seo
- /guide/runtime-config

Platform:
- /guide/plugins
- /guide/middleware
- /guide/server-api
- /guide/modules-route-rules
- /guide/package-integration
- /guide/css-tailwind
- /guide/typescript-generated-types
- /guide/testing-quality

Features:
- /guide/media
- /guide/icons
- /guide/fonts
- /guide/i18n
- /guide/ui-animations
- /guide/vue-islands

Operations and safety:
- /guide/security-caching
- /guide/halal-core
- /guide/dev-build-output
- /guide/deployment
- /guide/troubleshooting

Reference:
- /reference/packages
- /reference/api-index
- /reference/cli
- /reference/composables
- /reference/configuration
- /reference/file-conventions
- /reference/hooks
- /reference/runtime
- /reference/compiler
- /reference/release
- /reference/limits

Important facts:
- Normal Resux components do not hydrate through Vue.
- resuxjs/ui and resuxjs/icons export Vue runtime components; use them in appropriate Vue/client contexts.
- useFetch returns an AsyncDataResource with data/value/pending/error refs.
- review_required creates a local manual review bundle; it is not automatically emailed or uploaded.
- production server/deployment report verification requires RESUX_HALAL_REPORT_SIGNING_SECRET.
- image transforms require sharp; video transforms require ffmpeg.
''')

write("docs/.vitepress/config.ts", r'''
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Resux',
  description: 'Complete documentation for the Resux compiler, SSR and resumable runtime, application platform, modules, packages, media, deployment, and safety tooling.',
  base: '/resux-docs/',
  cleanUrls: true,
  lastUpdated: true,
  metaChunk: true,
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/resux-docs/logo-mark.svg' }],
    ['meta', { name: 'theme-color', content: '#111827' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Resux Documentation' }],
    ['meta', { property: 'og:description', content: 'Learn the complete Resux framework: compiler, resumability, routing, server APIs, modules, packages, media, deployment, and safety.' }],
    ['meta', { property: 'og:image', content: 'https://mahmoudabdalrhmanmohamed.github.io/resux-docs/og-image.png' }],
    ['meta', { property: 'og:image:type', content: 'image/png' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:image', content: 'https://mahmoudabdalrhmanmohamed.github.io/resux-docs/og-image.png' }]
  ],
  themeConfig: {
    logo: '/logo-mark.svg',
    siteTitle: 'Resux',
    search: { provider: 'local' },
    nav: [
      { text: 'Guide', link: '/guide/framework-tour' },
      { text: 'Reference', link: '/reference/api-index' },
      { text: 'Examples', link: '/examples/counter' },
      { text: 'Brand', link: '/brand' },
      {
        text: 'Links',
        items: [
          { text: 'npm package', link: 'https://www.npmjs.com/package/resuxjs' },
          { text: 'Source repo', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux' },
          { text: 'Docs repo', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux-docs' }
        ]
      }
    ],
    sidebar: [
      {
        text: 'Start Here',
        collapsed: false,
        items: [
          { text: 'Framework Tour', link: '/guide/framework-tour' },
          { text: 'What is Resux?', link: '/guide/what-is-resux' },
          { text: 'Core Concepts', link: '/guide/core-concepts' },
          { text: 'Getting Started', link: '/guide/getting-started' },
          { text: 'Execution Contexts', link: '/guide/execution-contexts' },
          { text: 'Project Structure', link: '/guide/project-structure' },
          { text: 'Mental Model', link: '/guide/mental-model' }
        ]
      },
      {
        text: 'Application Guide',
        collapsed: false,
        items: [
          { text: 'Rendering Lifecycle', link: '/guide/rendering-lifecycle' },
          { text: 'Resumability and Handlers', link: '/guide/resumability-handlers' },
          { text: 'App Shell and Errors', link: '/guide/app-shell-errors' },
          { text: 'Components', link: '/guide/components' },
          { text: 'Template Syntax', link: '/guide/template-syntax' },
          { text: 'State and Reactivity', link: '/guide/state' },
          { text: 'Async Data', link: '/guide/async-data' },
          { text: 'Routing', link: '/guide/routing' },
          { text: 'Layouts', link: '/guide/layouts' },
          { text: 'Head and SEO', link: '/guide/head-seo' },
          { text: 'Runtime Config', link: '/guide/runtime-config' }
        ]
      },
      {
        text: 'Platform and Extension',
        collapsed: false,
        items: [
          { text: 'Plugins', link: '/guide/plugins' },
          { text: 'Middleware', link: '/guide/middleware' },
          { text: 'Server API', link: '/guide/server-api' },
          { text: 'Modules and Route Rules', link: '/guide/modules-route-rules' },
          { text: 'Third-party Packages', link: '/guide/package-integration' },
          { text: 'CSS and Tailwind', link: '/guide/css-tailwind' },
          { text: 'TypeScript and Generated Types', link: '/guide/typescript-generated-types' },
          { text: 'Testing and Quality', link: '/guide/testing-quality' }
        ]
      },
      {
        text: 'Optional Features',
        collapsed: false,
        items: [
          { text: 'Media and Optimization', link: '/guide/media' },
          { text: 'Icons', link: '/guide/icons' },
          { text: 'Fonts', link: '/guide/fonts' },
          { text: 'i18n and Localization', link: '/guide/i18n' },
          { text: 'UI and Motion', link: '/guide/ui-animations' },
          { text: 'Vue Islands', link: '/guide/vue-islands' }
        ]
      },
      {
        text: 'Operations and Safety',
        collapsed: false,
        items: [
          { text: 'Security and Caching', link: '/guide/security-caching' },
          { text: 'Halal Core', link: '/guide/halal-core' },
          { text: 'Dev Server and Build Output', link: '/guide/dev-build-output' },
          { text: 'Deployment', link: '/guide/deployment' },
          { text: 'Troubleshooting', link: '/guide/troubleshooting' }
        ]
      },
      {
        text: 'Reference',
        collapsed: false,
        items: [
          { text: 'Package Exports', link: '/reference/packages' },
          { text: 'Public API Index', link: '/reference/api-index' },
          { text: 'CLI', link: '/reference/cli' },
          { text: 'Composables and Globals', link: '/reference/composables' },
          { text: 'Configuration', link: '/reference/configuration' },
          { text: 'File Conventions', link: '/reference/file-conventions' },
          { text: 'Lifecycle Hooks', link: '/reference/hooks' },
          { text: 'Runtime Internals', link: '/reference/runtime' },
          { text: 'Compiler Internals', link: '/reference/compiler' },
          { text: 'Release and Publishing', link: '/reference/release' },
          { text: 'Current Limits', link: '/reference/limits' }
        ]
      },
      {
        text: 'Examples',
        collapsed: false,
        items: [
          { text: 'Counter', link: '/examples/counter' },
          { text: 'Blog Routes', link: '/examples/blog' },
          { text: 'API and Fetch', link: '/examples/api-and-fetch' },
          { text: 'Auth Middleware', link: '/examples/auth-middleware' },
          { text: 'Progressive Package', link: '/examples/progressive-package' },
          { text: 'Media Optimization', link: '/examples/media-optimization' },
          { text: 'Docker Deployment', link: '/examples/docker' }
        ]
      },
      {
        text: 'Project',
        collapsed: false,
        items: [
          { text: 'Brand System', link: '/brand' },
          { text: 'Contributing to Docs', link: '/community/contributing' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux' }
    ],
    footer: {
      message: 'Complete Resux source-aligned documentation with stable and experimental boundaries documented explicitly.',
      copyright: 'Copyright (c) 2026 Resux contributors'
    },
    editLink: {
      pattern: 'https://github.com/MahmoudAbdalrhmanMohamed/resux-docs/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    }
  },
  markdown: {
    theme: { light: 'github-light', dark: 'github-dark' },
    lineNumbers: true
  }
})
''')

# Remove date/version claims from untouched prose without changing code examples.
for target in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
    if not target.exists():
        continue
    lines = target.read_text(encoding="utf-8").splitlines()
    cleaned = []
    for line in lines:
        lowered = line.lower()
        if "checked on 2026-05-07" in lowered or "latest npm release (checked" in lowered:
            continue
        if "currently resolves to `0.2.23`" in lowered or "current npm `latest`" in lowered:
            continue
        cleaned.append(line)
    target.write_text("\n".join(cleaned).rstrip() + "\n", encoding="utf-8")

# Keep FILES.md truthful after adding pages and before deleting the staging scripts.
ignored = {".git", "node_modules", "docs/.vitepress/cache", "docs/.vitepress/dist"}
files = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():
        continue
    relative = path.relative_to(ROOT).as_posix()
    if any(relative == item or relative.startswith(item + "/") for item in ignored):
        continue
    if relative.startswith("scripts/global_docs_") or relative == ".github/workflows/one-time-global-docs-refresh.yml":
        continue
    files.append(relative)
write("FILES.md", "# Repository Files\n\n" + "\n".join(f"- `{name}`" for name in files))
