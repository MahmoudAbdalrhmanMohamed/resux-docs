---
layout: home

title: Resux Documentation
titleTemplate: false

hero:
  name: Resux
  text: Build for resumability, not hydration.
  tagline: Source-aligned documentation for the Resux HTML-first framework—covering application development, runtime architecture, UI boundaries, media, fonts, icons, deployment, and every public package surface.
  image:
    src: /logo.svg
    alt: Resux logo
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: Explore the Framework
      link: /guide/framework-tour
    - theme: alt
      text: API Reference
      link: /reference/api-index

features:
  - icon: SSR
    title: HTML first
    details: Render routes, layouts, head metadata, state, async data, and first-party media on the server.
  - icon: RESUME
    title: Resume on demand
    details: Keep interaction code addressable and load generated handlers when the browser actually needs them.
  - icon: ROUTE
    title: Application platform
    details: File routing, middleware, server APIs, plugins, modules, hooks, route rules, and deployment work as one system.
  - icon: UI
    title: Explicit runtime boundaries
    details: Know when Resux owns the template, when Vue owns an island, and what that choice costs in browser JavaScript.
  - icon: MEDIA
    title: First-party assets
    details: Images, picture sources, video strategies, fonts, icons, preloading, providers, and optimization have dedicated guides.
  - icon: SOURCE
    title: Source-aligned reference
    details: Public APIs, limits, accessibility behavior, runtime ownership, and source locations are documented explicitly.
---

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Start with the right path</p>
  <h2 class="resux-home-title">Learn Resux by what you are trying to accomplish.</h2>
  <p class="resux-home-lead">The documentation separates practical application guides, architecture deep dives, package reference, and production examples so you can move from a task to the exact implementation details without reading the entire site in order.</p>

  <div class="resux-home-grid">
    <a class="resux-home-card" href="./guide/getting-started">
      <span class="resux-card-kicker">New to Resux</span>
      <strong>Create your first application</strong>
      <span>Install the framework, understand the generated project, run development mode, and build the first route.</span>
    </a>
    <a class="resux-home-card" href="./guide/architecture-deep-dive">
      <span class="resux-card-kicker">Architecture</span>
      <strong>Understand the runtime model</strong>
      <span>Trace compiler output, SSR, serialized state, resumable handlers, browser ownership, and Vue islands as one system.</span>
    </a>
    <a class="resux-home-card" href="./components/">
      <span class="resux-card-kicker">Interface</span>
      <strong>Build application UI</strong>
      <span>Choose between normal Resux templates, the optional Vue UI package, media primitives, icons, motion, and native HTML.</span>
    </a>
    <a class="resux-home-card" href="./media/">
      <span class="resux-card-kicker">Performance</span>
      <strong>Ship images and video well</strong>
      <span>Use responsive sources, optimization, placeholders, preloads, video loading strategies, and production media patterns.</span>
    </a>
    <a class="resux-home-card" href="./reference/api-index">
      <span class="resux-card-kicker">Reference</span>
      <strong>Look up an exact API</strong>
      <span>Jump directly to package exports, composables, reactivity, compiler, runtime, UI, i18n, kit, node, and configuration APIs.</span>
    </a>
    <a class="resux-home-card" href="./guide/debugging-mental-model">
      <span class="resux-card-kicker">Troubleshooting</span>
      <strong>Find the failing subsystem</strong>
      <span>Separate compiler, route, SSR, serialization, resumability, reactivity, navigation, package, media, and deployment failures.</span>
    </a>
  </div>
</div>

<div class="resux-home-section">
  <p class="resux-home-eyebrow">The mental model</p>
  <h2 class="resux-home-title">From authored component to interactive browser.</h2>
  <p class="resux-home-lead">Resux does not treat client startup as a requirement to recreate the whole application. The framework compiles server output and browser-addressable behavior so the page can start from HTML and resume the interaction that is actually requested.</p>

  <div class="resux-pipeline">
    <div class="resux-pipeline-step">
      <strong>Author</strong>
      <span>Vue-like SFCs, routes, layouts, state, handlers, server APIs, and configuration.</span>
    </div>
    <div class="resux-pipeline-arrow">→</div>
    <div class="resux-pipeline-step">
      <strong>Compile</strong>
      <span>Generate SSR code, handler modules, bindings, route metadata, and runtime artifacts.</span>
    </div>
    <div class="resux-pipeline-arrow">→</div>
    <div class="resux-pipeline-step">
      <strong>Render</strong>
      <span>Send HTML, head output, serialized application data, and resumability metadata from the server.</span>
    </div>
    <div class="resux-pipeline-arrow">→</div>
    <div class="resux-pipeline-step">
      <strong>Resume</strong>
      <span>Load and execute the specific browser behavior required by navigation, state, or user interaction.</span>
    </div>
  </div>
</div>

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Application platform</p>
  <h2 class="resux-home-title">One documentation system for the whole framework.</h2>
  <p class="resux-home-lead">Each area has its own focused navigation now, so component documentation does not compete with compiler internals and deployment reference in the same sidebar.</p>

  <div class="resux-home-grid">
    <a class="resux-home-card" href="./guide/routing">
      <span class="resux-card-kicker">Core</span>
      <strong>Routing, layouts and data</strong>
      <span>Build pages with file routing, layouts, middleware, state, async data, metadata, and runtime configuration.</span>
    </a>
    <a class="resux-home-card" href="./fonts/">
      <span class="resux-card-kicker">Assets</span>
      <strong>Fonts</strong>
      <span>Configure font families, loading behavior, generated CSS, performance, and content-security-policy requirements.</span>
    </a>
    <a class="resux-home-card" href="./icons/">
      <span class="resux-card-kicker">Assets</span>
      <strong>Icons</strong>
      <span>Use the SVG registry, aliases, lazy or runtime loading, Iconify-compatible sources, and cache behavior.</span>
    </a>
    <a class="resux-home-card" href="./guide/i18n">
      <span class="resux-card-kicker">Optional feature</span>
      <strong>Internationalization</strong>
      <span>Configure locales, localized route behavior, translation lookup, browser language handling, and the i18n package API.</span>
    </a>
    <a class="resux-home-card" href="./guide/package-integration">
      <span class="resux-card-kicker">Extension</span>
      <strong>Third-party packages</strong>
      <span>Decide whether a dependency belongs on the server, in progressive enhancement, in the resumable runtime, or in a Vue island.</span>
    </a>
    <a class="resux-home-card" href="./guide/deployment">
      <span class="resux-card-kicker">Production</span>
      <strong>Deploy safely</strong>
      <span>Understand build output, Node and serverless targets, caching, runtime dependencies, and production verification.</span>
    </a>
  </div>
</div>

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Install</p>
  <h2 class="resux-home-title">Create a Resux project.</h2>
  <p class="resux-home-lead">The current framework source requires Node.js <code>&gt;=20.19.0</code>.</p>
</div>

```sh
npx create-resuxjs@latest my-app
cd my-app
npm install
npm run dev
```

<div class="resux-home-section">
  <p class="resux-home-eyebrow">Documentation standard</p>
  <h2 class="resux-home-title">Every important page should answer more than “what is this symbol?”</h2>
  <p class="resux-home-lead">Where relevant, the docs describe why a feature exists, when to use it, where it runs, its complete API and defaults, generated HTML or network behavior, resumability implications, browser-JavaScript cost, accessibility and security responsibilities, current limitations, source evidence, realistic examples, and common failure modes.</p>

  <div class="resux-home-grid">
    <a class="resux-home-card" href="./reference/source-map">
      <span class="resux-card-kicker">Evidence</span>
      <strong>Framework source map</strong>
      <span>Connect public features to the framework source and the tests that verify their behavior.</span>
    </a>
    <a class="resux-home-card" href="./reference/coverage">
      <span class="resux-card-kicker">Coverage</span>
      <strong>Documentation coverage</strong>
      <span>Track which framework surfaces have guides, reference, examples, source links, and known limitations documented.</span>
    </a>
    <a class="resux-home-card" href="./reference/limits">
      <span class="resux-card-kicker">Honesty</span>
      <strong>Current limits</strong>
      <span>See the boundaries that matter before adopting an API or relying on behavior the framework does not yet implement.</span>
    </a>
  </div>
</div>

<div style="height: 56px"></div>
