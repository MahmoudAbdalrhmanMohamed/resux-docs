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

## Learn by area

| Goal | Read |
| --- | --- |
| See how authored code reaches the browser | [Code to Browser](/guide/code-to-browser) |
| Understand the architecture | [Framework Tour](/guide/framework-tour) and [Mental Model](/guide/mental-model) |
| Build Resux components and routes | [Components](/guide/components), [Template Syntax](/guide/template-syntax), [Routing](/guide/routing) |
| Use the optional UI package | [UI Components](/components/), [UI Package API](/reference/ui), [Vue Islands](/guide/vue-islands) |
| Load data and manage state | [State](/guide/state), [Async Data](/guide/async-data) |
| Build APIs and middleware | [Server API](/guide/server-api), [Middleware](/guide/middleware) |
| Integrate libraries | [Third-party Packages](/guide/package-integration), [Integration Cookbook](/guide/integration-cookbook) |
| Extend the framework | [Modules](/guide/modules-route-rules), [Hooks](/reference/hooks), [API Index](/reference/api-index) |
| Optimize assets | [Images and Media](/media/), [Fonts](/fonts/), [Icons](/icons/), [CSS/Tailwind](/guide/css-tailwind) |
| Check public API coverage | [Documentation Coverage](/reference/coverage), [Package Exports](/reference/packages) |
| Deploy safely | [Deployment](/guide/deployment), [Security](/guide/security-caching), [Halal Core](/guide/halal-core) |

## Source and release alignment

The documentation is maintained against the framework source and tests. The published npm version can temporarily lag `main`, so check the installed/published `resuxjs` version before relying on a feature that has not been released yet. Living docs should never invent an API just because another framework exposes one.
