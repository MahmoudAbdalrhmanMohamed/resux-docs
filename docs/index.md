---
layout: home

hero:
  name: Resux
  text: HTML-first resumable framework
  tagline: Compile Vue-like SFCs into server-rendered HTML, serialized state, and interaction-loaded browser modules—with routing, server APIs, modules, first-party media, optional Vue islands, and documented runtime boundaries.
  image:
    src: /logo.svg
    alt: Resux logo
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: Architecture Deep Dive
      link: /guide/architecture-deep-dive
    - theme: alt
      text: Components
      link: /components/
    - theme: alt
      text: API Index
      link: /reference/api-index

features:
  - icon: SSR
    title: Server HTML first
    details: Render app shells, layouts, pages, head metadata, state, async data, and first-party media on the server.
  - icon: RESUME
    title: Resume on interaction
    details: Import generated handler code only when an event or progressive enhancement needs it.
  - icon: ROUTE
    title: Full application platform
    details: File routes, middleware, APIs, plugins, modules, hooks, route rules, and deployment are integrated.
  - icon: UI
    title: Explicit UI boundaries
    details: Dedicated docs distinguish optional Vue UI components from native/resumable Resux template primitives.
  - icon: MEDIA
    title: First-party media
    details: Responsive images, placeholders, preloads, providers, generated transforms, video loading strategies, and controls are documented in depth.
  - icon: SAFE
    title: Source-aligned limits
    details: Public APIs, accessibility behavior, server/client cost, security boundaries, and current limitations are documented explicitly.
---

## Create a project

```sh
npx create-resuxjs@latest my-app
cd my-app
npm install
npm run dev
```

Node.js `>=20.19.0` is required by the current framework source.

## Choose a learning path

The docs are intentionally split into **task guides**, **deep conceptual guides**, and **exact reference**. You do not need to read every page in order.

### I am new to Resux

Read these in sequence:

1. [What is Resux?](/guide/what-is-resux) — the product boundary in plain language.
2. [Framework Tour](/guide/framework-tour) — the main application pieces.
3. [Getting Started](/guide/getting-started) — create and run an app.
4. [Core Concepts](/guide/core-concepts) — the essential vocabulary.
5. [Components](/guide/components) and [Template Syntax](/guide/template-syntax) — author normal Resux UI.
6. [State](/guide/state), [Async Data](/guide/async-data), and [Routing](/guide/routing) — build a real application.

### I know the APIs but want to understand how Resux works

Read the new deep-dive path:

1. [Architecture Deep Dive](/guide/architecture-deep-dive) — compiler, server, browser, reactivity, Vue islands, packages, media, and deployment as one system.
2. [Request Lifecycle](/guide/request-lifecycle) — trace one URL from route matching to SSR, payload serialization, browser bootstrap, interaction, and navigation.
3. [Resumability Deep Dive](/guide/resumability-deep-dive) — delegated events, generated handlers, serializable scope, bindings, and runtime ownership.
4. [Code to Browser](/guide/code-to-browser) — follow authored SFC code into generated runtime artifacts.
5. [Framework Source Map](/reference/source-map) — connect every public package area to source and tests.

### I am building UI

Start with [UI Components](/components/) and read [Component Anatomy](/components/component-anatomy) before assuming behavior from a component name.

The central UI distinction is:

- normal Resux templates are compiler/resumability-owned,
- `resuxjs/ui` exports Vue `defineComponent()` components and belongs inside an explicit Vue runtime boundary,
- `ResuxImg`, `ResuxPicture`, and `ResuxVideo` are Resux renderer/template primitives rather than `resuxjs/ui` components,
- the full SVG icon system lives in `resuxjs/icons`, not in the small `RxIcon` UI placeholder primitive.

### I am integrating a library

Read:

1. [Execution Contexts](/guide/execution-contexts),
2. [Third-party Packages](/guide/package-integration),
3. [Integration Cookbook](/guide/integration-cookbook),
4. [Vue Islands](/guide/vue-islands) when the package is truly Vue-owned.

The important question is not “can npm install this package?” but **which runtime should own it: server, SSR, client-only, progressive enhancement, or Vue island?**

### Something is broken

Use [Debugging Mental Model](/guide/debugging-mental-model) to identify the failing subsystem before changing code. It separates compiler, routing, SSR/data, serialization, resumable handlers, reactivity/bindings, navigation, Vue islands, packages, media, fonts/icons, deployment, and cleanup failures.

## Learn by area

| Goal | Read |
| --- | --- |
| See how authored code reaches the browser | [Code to Browser](/guide/code-to-browser) |
| Understand the full architecture | [Architecture Deep Dive](/guide/architecture-deep-dive), [Request Lifecycle](/guide/request-lifecycle) |
| Understand resumability precisely | [Resumability Deep Dive](/guide/resumability-deep-dive), [Resumability and Handlers](/guide/resumability-handlers) |
| Build Resux components and routes | [Components](/guide/components), [Template Syntax](/guide/template-syntax), [Routing](/guide/routing) |
| Use the optional UI package | [UI Components](/components/), [Component Anatomy](/components/component-anatomy), [UI Package API](/reference/ui), [Vue Islands](/guide/vue-islands) |
| Load data and manage state | [State](/guide/state), [Async Data](/guide/async-data) |
| Build APIs and middleware | [Server API](/guide/server-api), [Middleware](/guide/middleware) |
| Integrate libraries | [Third-party Packages](/guide/package-integration), [Integration Cookbook](/guide/integration-cookbook) |
| Extend the framework | [Modules](/guide/modules-route-rules), [Hooks](/reference/hooks), [API Index](/reference/api-index) |
| Optimize assets | [Images and Media](/media/), [Fonts](/fonts/), [Icons](/icons/), [CSS/Tailwind](/guide/css-tailwind) |
| Debug by subsystem | [Debugging Mental Model](/guide/debugging-mental-model), [Troubleshooting](/guide/troubleshooting) |
| Verify docs against implementation | [Framework Source Map](/reference/source-map), [Documentation Coverage](/reference/coverage), [Package Exports](/reference/packages) |
| Deploy safely | [Deployment](/guide/deployment), [Security](/guide/security-caching), [Halal Core](/guide/halal-core) |

## How the documentation is written

A useful framework page should explain more than a symbol name. Where relevant, the docs aim to answer:

- **Why does this feature exist?**
- **When should I use it—and when should I not?**
- **Where does it run: build, server, resumable browser runtime, client enhancement, or Vue island?**
- **What is the full API?** Props/options/types/defaults/events/slots/return values.
- **What HTML/network/runtime behavior does it produce?**
- **How does SSR/resumability affect it?**
- **What does it cost in browser JavaScript?**
- **What are its accessibility and security responsibilities?**
- **What are the current limitations?**
- **Which source/test area proves the behavior?**
- **What realistic examples and failure modes should a user know?**

This is the standard used by the deeper component and architecture pages. Short reference tables are still useful, but they should not be the only explanation of an important subsystem.

## Source and release alignment

The documentation is maintained against the framework source and tests. The published npm version can temporarily lag `main`, so check the installed/published `resuxjs` version before relying on a feature that has not been released yet.

The framework `package.json`, public entry points, implementation, generated declarations, and regression tests are the source of truth. Living docs should never invent an API just because another framework exposes one.

For maintainers and advanced users, [Framework Source Map](/reference/source-map) documents where each public subsystem lives and which tests are useful when verifying a docs claim.
