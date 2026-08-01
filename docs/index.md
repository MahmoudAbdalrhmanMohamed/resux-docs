---
layout: home

hero:
  name: Resux
  text: Resumable web framework for HTML-first applications
  tagline: Build Vue-like server-rendered applications that serialize state and load client behavior only when interaction requires it.
  image:
    src: /logo.svg
    alt: Resux logo
  actions:
    - theme: brand
      text: Framework Tour
      link: /guide/framework-tour
    - theme: alt
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: API Reference
      link: /reference/packages

features:
  - icon: HTML
    title: HTML first, JavaScript on demand
    details: Resux renders useful HTML on the server, serializes route and component scopes, and imports the required handler only after interaction.
  - icon: SFC
    title: Focused Vue-like SFCs
    details: Use pages, layouts, components, script setup, styles, directives, and familiar reactivity within the documented Resux compiler subset.
  - icon: RX
    title: Native resumability and reactivity
    details: Resux provides its own refs, reactive objects, computed values, watchers, async data, payload serialization, and delegated resume runtime.
  - icon: SERVER
    title: Full application framework
    details: Routing, middleware, plugins, server APIs, modules, route rules, runtime config, SEO, images, videos, and deployment are included.
  - icon: PACKAGE
    title: Controlled package integration
    details: Classify third-party libraries as SSR, client-only, server-only, or progressive and inspect their bundle behavior.
  - icon: SAFETY
    title: Explicit safety and production guards
    details: Security headers, caching rules, diagnostics, Halal Core reports, signed reviews, and deployment verification have dedicated documentation.
---

## Create an application

```sh
npx create-resuxjs@latest my-app
cd my-app
npm install
npm run dev
```

Or use the main package CLI:

```sh
npx resuxjs@latest init my-app
```

This documentation intentionally does not hard-code a permanent “latest npm version.” Check the installed package or npm release page when you need release-specific behavior.

## A small Resux component

```vue
<script setup lang="ts">
const count = useState('count', () => 0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">
    Count: {{ count }}
  </button>
</template>
```

The server renders the button as HTML and serializes the `count` state. The browser keeps a small delegated runtime. When the button is clicked, Resux imports the generated handler module, restores the component scope, runs `increment`, and patches the affected output without hydrating the full application.

## Everything included in the framework

| Area | Capabilities |
| --- | --- |
| Application structure | `app.vue`, `error.vue`, pages, layouts, components, plugins, middleware, server routes, modules, assets, and public files |
| Runtime | SSR, serialized scopes, route payloads, resumable handlers, client navigation, errors, head, SEO, and runtime config |
| Data | Resux-native reactivity, `useState`, `useAsyncData`, `useFetch`, `$fetch`, and server-safe URL resolution |
| Server | API handlers, server middleware, H3-compatible helpers, route rules, health checks, image/video routes |
| Extension | Build-time modules, imports, components, plugins, middleware, templates, Vite hooks, Nitro hooks, and package adapters |
| Optional modules | i18n, icons, fonts, UI primitives, animations, security, and performance |
| Tooling | Create, prepare, dev, build, compile, preview, start, inspect, check, deploy, and Halal Core commands |
| Deployment | Node, Docker, Nitro, automatic target detection, Vercel, Netlify, Cloudflare, and static configuration |

## Read these first

- Start with the [Framework Tour](/guide/framework-tour) for the complete product map.
- Learn the request and browser sequence in [Rendering Lifecycle](/guide/rendering-lifecycle).
- Understand lazy interaction in [Resumability and Handlers](/guide/resumability-handlers).
- Use [Package Exports](/reference/packages), [Composables](/reference/composables), and [Configuration](/reference/configuration) as API references.
- Read [Third-party Packages](/guide/package-integration) before adding browser libraries.
- Read [Media and Optimization](/guide/media) before enabling image or video transforms.
- Read [Deployment](/guide/deployment) and [Halal Core](/guide/halal-core) before producing a production artifact.

## Important boundary

Resux uses `.vue` files but normal Resux components are not normal hydrated Vue components. Full Vue runtime behavior is available only through explicit [Vue Islands](/guide/vue-islands). Unsupported syntax should fail visibly rather than silently changing the runtime model.
