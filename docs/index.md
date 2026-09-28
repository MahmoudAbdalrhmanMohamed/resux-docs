---
layout: home

title: Resux Documentation
titleTemplate: false

hero:
  name: Resux
  text: Build fast, resumable web applications.
  tagline: Learn Resux with practical guides, examples, API reference, and clear explanations of how the framework behaves in the browser and on the server.
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
      text: API Reference
      link: /reference/api-index

features:
  - icon: SSR
    title: Server-rendered by default
    details: Build routes, layouts, metadata, data loading, and application UI around server-rendered HTML.
  - icon: RESUME
    title: Resume when needed
    details: Resux can keep browser startup small and load interaction code only when a page actually needs it.
  - icon: ROUTE
    title: Full application framework
    details: Routing, middleware, server APIs, plugins, modules, route rules, and deployment are part of the same framework.
  - icon: UI
    title: Clear client boundaries
    details: Use normal Resux components for the default runtime model and Vue islands when you intentionally need a Vue-owned client boundary.
  - icon: MEDIA
    title: Built-in asset tooling
    details: Images, responsive sources, video, fonts, icons, preloading, and optimization have dedicated APIs and guides.
  - icon: SOURCE
    title: Docs tied to the real framework
    details: Public APIs and examples are checked against the framework source, package exports, and tests.
---

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Public beta</p>
  <h2 class="resux-home-title">Current beta: 0.4.0-beta.2</h2>
  <p class="resux-home-lead">Resux 0.4 is available for public testing. It is a good fit for learning, demos, compatibility testing, and non-critical applications. Because Resux is still pre-1.0, pin your version and test upgrades before using it in an important production system.</p>

  <div class="resux-home-grid">
    <a class="resux-home-card" href="./reference/status">
      <span class="resux-card-kicker">Status</span>
      <strong>What “public beta” means</strong>
      <span>See what is validated today, what can still change, and how to evaluate Resux safely.</span>
    </a>
    <a class="resux-home-card" href="./reference/release">
      <span class="resux-card-kicker">Releases</span>
      <strong>Stable and beta channels</strong>
      <span>Learn how the npm latest and next channels are used and how prerelease publishing works.</span>
    </a>
  </div>
</div>

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Start building</p>
  <h2 class="resux-home-title">Pick the path that matches what you need.</h2>
  <p class="resux-home-lead">You do not need to read the documentation from top to bottom. Start with a task and move into the deeper architecture only when you need it.</p>

  <div class="resux-home-grid">
    <a class="resux-home-card" href="./guide/getting-started">
      <span class="resux-card-kicker">New project</span>
      <strong>Create your first app</strong>
      <span>Install Resux, generate a project, run the dev server, and build your first interactive page.</span>
    </a>
    <a class="resux-home-card" href="./guide/framework-tour">
      <span class="resux-card-kicker">Overview</span>
      <strong>Tour the framework</strong>
      <span>See how routing, rendering, resumability, data, server APIs, plugins, media, and deployment fit together.</span>
    </a>
    <a class="resux-home-card" href="./components/">
      <span class="resux-card-kicker">UI</span>
      <strong>Explore UI components</strong>
      <span>Browse the optional component package, props, events, slots, accessibility notes, and runtime boundaries.</span>
    </a>
    <a class="resux-home-card" href="./media/">
      <span class="resux-card-kicker">Assets</span>
      <strong>Images and video</strong>
      <span>Use responsive images, optimization, placeholders, preload strategies, and video tooling.</span>
    </a>
    <a class="resux-home-card" href="./reference/api-index">
      <span class="resux-card-kicker">Reference</span>
      <strong>Look up an API</strong>
      <span>Find package exports, composables, runtime APIs, compiler APIs, UI, i18n, Kit, Node, and configuration.</span>
    </a>
    <a class="resux-home-card" href="./guide/troubleshooting">
      <span class="resux-card-kicker">Help</span>
      <strong>Troubleshoot a problem</strong>
      <span>Work through common development, build, runtime, package, media, and deployment issues.</span>
    </a>
  </div>
</div>

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Install</p>
  <h2 class="resux-home-title">Create a Resux project.</h2>
  <p class="resux-home-lead">Resux currently requires Node.js <code>&gt;=20.19.0</code>.</p>
</div>

Stable channel:

```sh
npx create-resuxjs@latest my-app
```

Public beta:

```sh
npx create-resuxjs@next my-app
cd my-app
npm install
npm run dev
```

For repeatable beta testing, pin the exact version:

```sh
npx create-resuxjs@0.4.0-beta.2 my-app
```

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Learn the runtime</p>
  <h2 class="resux-home-title">Understand what happens from request to interaction.</h2>
  <p class="resux-home-lead">Resux starts from server-rendered HTML and adds browser execution only where the application needs it. The architecture guides explain compilation, rendering, serialized state, resumable handlers, routing, and Vue islands without hiding the trade-offs.</p>

  <div class="resux-home-grid">
    <a class="resux-home-card" href="./guide/architecture-deep-dive">
      <span class="resux-card-kicker">Architecture</span>
      <strong>Architecture deep dive</strong>
      <span>Follow the framework from source files through build output, SSR, and browser runtime behavior.</span>
    </a>
    <a class="resux-home-card" href="./guide/resumability-deep-dive">
      <span class="resux-card-kicker">Runtime</span>
      <strong>Resumability</strong>
      <span>Learn how handlers and client work are connected to server-rendered output.</span>
    </a>
    <a class="resux-home-card" href="./guide/vue-islands">
      <span class="resux-card-kicker">Vue</span>
      <strong>Vue islands</strong>
      <span>Use Vue deliberately when a feature needs a Vue-owned client runtime boundary.</span>
    </a>
  </div>
</div>

<div style="height: 56px"></div>
