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
      text: Code to Browser
      link: /guide/code-to-browser
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
| See how authored code reaches the browser | [Code to Browser](/guide/code-to-browser) |
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
