---
layout: home

hero:
  name: Resux
  text: Resumable web framework for Vue-like apps
  tagline: Build server-rendered pages that ship HTML first, serialize state, and load client handler code only when users interact.
  image:
    src: /logo.svg
    alt: Resux logo
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: Learn the Runtime
      link: /guide/mental-model
    - theme: alt
      text: API Reference
      link: /reference/composables

features:
  - icon: HTML
    title: HTML first, JS on demand
    details: Resux renders HTML on the server, serializes route and component state, and imports handler modules only after an event is triggered.
  - icon: SFC
    title: Familiar .vue files
    details: Use a focused Vue-like SFC subset with template, script setup, pages routing, layouts, and components.
  - icon: RX
    title: Resumable state
    details: useState and useAsyncData data is serialized into the payload so scopes can resume without whole-app hydration.
  - icon: ROUTE
    title: File routing
    details: Add pages, dynamic params, catch-all routes, layouts, route middleware, and client-side navigation.
  - icon: API
    title: Server API included
    details: Build API routes and request middleware with h3-backed helpers such as readBody, getQuery, and setHeader.
  - icon: ISLAND
    title: Vue islands when needed
    details: Keep Resux components zero-default-hydration, then opt into Vue runtime islands for complex client widgets.
---

## Install in one command

```sh
npx resuxjs@latest init my-app
cd my-app
npm install
npm run dev
```

## A tiny Resux component

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

The server renders the button as HTML. The browser receives the serialized `count` state and a small delegated runtime. The handler chunk is loaded only when the button is clicked.

## What should I read first?

- New to Resux: start with [What is Resux?](/guide/what-is-resux), [Core Concepts](/guide/core-concepts), and [Getting Started](/guide/getting-started).
- Understanding the runtime: read [Rendering Lifecycle](/guide/rendering-lifecycle) and [Resumability and Handlers](/guide/resumability-handlers).
- Understanding where code belongs: use [Execution Contexts](/guide/execution-contexts), [App Shell, Errors, and Public Files](/guide/app-shell-errors), and [Security and Caching](/guide/security-caching).
- Building an app: read [Project Structure](/guide/project-structure), [Routing](/guide/routing), and [Async Data](/guide/async-data).
- Looking for exact APIs: jump to [Composables and Globals](/reference/composables) and [CLI](/reference/cli).
- Deploying: use [Deployment](/guide/deployment) and [Docker Deployment](/examples/docker).
