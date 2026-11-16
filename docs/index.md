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
    - theme: brand
      text: 💼 Hire Me
      link: /#hire-me

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
  <h2 class="resux-home-title">Current beta: 0.4.0-beta.7</h2>
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

<div id="hire-me" class="resux-home-section">
  <div class="resux-hire-card">
    <div class="resux-hire-status">
      <span class="resux-hire-status-dot"></span>
      Available for Hire &amp; Consulting
    </div>
    <h2 class="resux-home-title" style="margin-top: 8px;">
      Need an Experienced Full-Stack &amp; Framework Architect?
    </h2>
    <p class="resux-home-lead">
      Hi, I’m <strong>Mahmoud Abdalrahman Mohamed</strong> — creator and lead architect of <strong>Resux</strong>. I help engineering teams and founders design and deliver ultra-fast web applications, high-performance Vue 3 &amp; Nuxt 3/4 architectures, resumable rendering pipelines, and custom developer tooling.
    </p>

    <div class="resux-hire-services">
      <div class="resux-hire-service-item">
        <strong>⚡ Full-Stack &amp; Modern Frontend</strong>
        <p>Production engineering with Vue 3, Nuxt, TypeScript, Vite, Nitro, and Tailwind CSS. Complex SPAs, SSR, and resumable architectures.</p>
      </div>
      <div class="resux-hire-service-item">
        <strong>🚀 Performance &amp; Core Web Vitals</strong>
        <p>Eliminating FOUC/CLS, sub-second TTFB, metric-adjusted font overrides, streaming SSR, bundle size reduction, and asset pipelines.</p>
      </div>
      <div class="resux-hire-service-item">
        <strong>🛠️ Frameworks &amp; Developer Tooling</strong>
        <p>Custom Vite plugins, CLI toolkits, AST transforms, compiler pipelines, design systems, and headless component libraries.</p>
      </div>
    </div>

    <div class="resux-hire-actions">
      <a class="resux-hire-btn-primary" href="mailto:mahnoudhouda5632@gmail.com?subject=Work%20Inquiry%20from%20Resux%20Docs">
        ✉️ Get in Touch (Email Me)
      </a>
      <a class="resux-hire-btn-secondary" href="https://github.com/MahmoudAbdalrhmanMohamed" target="_blank" rel="noopener noreferrer">
        🐙 GitHub Profile
      </a>
      <span class="resux-hire-meta">
        Direct: <strong>mahnoudhouda5632@gmail.com</strong> · Open to Full-time, Contract &amp; Consulting Worldwide
      </span>
    </div>
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
npx create-resuxjs@0.4.0-beta.7 my-app
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
