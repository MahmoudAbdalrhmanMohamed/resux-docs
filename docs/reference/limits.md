# Current Limits and Compatibility Boundaries

Resux has a working resumable framework core, but it is not a drop-in replacement for the complete Vue or Nuxt ecosystems. This page documents the boundaries developers must design around.

Do not rely on a version number written in documentation to decide compatibility. Check the installed `resuxjs` package, its release notes, and the behavior of `resux check` for the application being deployed.

## Stable framework direction

The intended core includes:

- the documented Vue-like SFC subset
- file-system pages and layouts
- server rendering and payload serialization
- delegated resumable event handlers
- Resux-native reactivity
- route payload navigation
- plugins and route/server middleware
- server API routes
- build-time modules and route rules
- project creation, preparation, development, build, preview, start, inspect, check, and deploy commands

Compatibility outside the documented surface is not implied.

## Vue syntax is a focused subset

Normal Resux components use `.vue` files, but they are compiled into Resux component definitions and resumable handlers. They do not become normal hydrated Vue components.

Unsupported Vue syntax should fail at compile time instead of silently hydrating the application. Check [Template Syntax](/guide/template-syntax) before copying a Vue component from another project.

## No automatic hydration fallback

Resux does not automatically switch an unsupported component to full Vue hydration.

Use one of these explicit choices:

- rewrite the component using the supported Resux subset
- attach a client enhancement to server-rendered HTML
- isolate the widget in a Vue island

This makes runtime cost and execution context visible.

## Vue islands are an escape hatch

Vue islands are useful for complex Vue widgets, but they add the Vue client runtime for that island and may not share every Resux lifecycle or serialization behavior automatically.

Test island props, emitted events, routing behavior, CSS, and cleanup across client navigation.

## Serializable state only

Values stored in resumable state or async-data payloads must be JSON-compatible.

Avoid serializing:

- functions and closures
- class instances
- DOM nodes
- streams and sockets
- database clients
- `Map`, `Set`, `WeakMap`, and `WeakSet`
- cyclic objects
- request/response objects
- secret server configuration

Keep runtime-only objects in server code, mounted browser code, package instances, or island-local state.

## Browser APIs are not available during SSR

`window`, `document`, browser storage, canvas, media APIs, and many third-party libraries do not exist during server rendering.

Use:

- `onMounted`
- `.client` plugins or middleware
- `useClientPackage`
- a progressive client enhancement
- a Vue island

Do not hide browser access behind a type assertion; change the execution context.

## Event model

Resux uses delegated event listeners and resumes the associated scope when interaction occurs.

Consequences:

- handlers must be available as generated modules
- captured state must be serializable or reconstructable
- cleanup matters for observers, timers, listeners, and third-party instances
- complex native listener behavior may need a client enhancement or island
- `.capture` and `.passive` exist within the delegated model rather than creating a full Vue hydration listener tree

## Reactivity differences

Resux implements its own reactivity layer. The familiar API names do not guarantee every Vue edge case, scheduler detail, or devtools integration is identical.

Documented behavior includes refs, reactive objects, computed values, watchers, cleanup, readonly helpers, and next-tick scheduling. Library code that depends on Vue internals should run in a Vue island instead.

## Third-party package compatibility

Packages fall into four execution modes: SSR, client-only, server-only, or progressive.

A package may fail when it:

- touches browser globals at import time
- assumes Vue hydration
- mutates DOM outside its target element
- does not expose a cleanup API
- ships incompatible ESM/CJS output
- requires native binaries unavailable on the deployment provider

Use package diagnostics and explicit configuration. See [Third-party Packages](/guide/package-integration).

## Compiler and build diagnostics

The compiler can diagnose only patterns it knows. Dynamic code generation, unusual filesystem layouts, hidden package side effects, and runtime-only failures may escape static checks.

Run all of these before release:

```sh
resux prepare
resux check
resux build
resux inspect --json
```

Then exercise the built production server, not only the dev server.

## Provider-specific deployment

Nitro support provides a deployment path, not a guarantee that every provider preset and runtime behaves identically.

Common provider differences include:

- Node APIs versus worker APIs
- writable filesystem availability
- native dependencies such as `sharp`
- availability of `ffmpeg`
- request and response size limits
- streaming support
- environment variable timing
- cache behavior at the edge

Pin the deployment target/preset and test on the real provider.

## Static target limitations

Applications that depend on request-time SSR, private runtime config, authenticated route payloads, server middleware, or API routes cannot be reduced to a purely static site without changing their architecture.

Use the static target only for routes proven to be build-stable.

## Media limitations

- Image transformation requires a working `sharp` installation.
- Video transformation requires `ffmpeg` on `PATH` or through `RESUX_FFMPEG_PATH`.
- Remote media proxying must be restricted to avoid SSRF and unexpected bandwidth usage.
- Runtime-generated caches require writable storage and may not persist on serverless platforms.

## Halal Core limitations

Halal Core is automated policy tooling, not an official religious or legal decision.

- false positives and false negatives are possible
- `review_required` currently uses a manual file exchange
- no automatic email, upload, or GitHub issue is created by the framework
- HMAC signatures authenticate the configured key holder, not the reviewer’s qualifications
- optional remote AI classification still carries privacy risk after redaction
- open-source forks can change enforcement

Read [Halal Core](/guide/halal-core) before using production guards.

## Security boundaries

Framework defaults do not replace application security. Developers remain responsible for:

- authentication and authorization
- input validation
- CSRF strategy
- safe database queries
- secret management
- content security policy
- dependency and supply-chain review
- SSRF protection for remote fetch/media features
- rate limits and abuse controls
- correct CDN and cache keys

## Documentation/version drift

Documentation can move faster or slower than npm releases. To reduce drift:

- this site avoids hard-coding a permanent “latest” version
- release-specific behavior should be checked against package metadata and release notes
- source-only features should be merged and released before application teams depend on them
- examples should be tested against the same package version used by the project

## Reporting a compatibility gap

When opening an issue, include:

- installed `resuxjs` version
- Node version
- operating system and deployment provider
- the smallest reproducing component or project
- `resux check --json` output
- relevant `resux inspect ... --json` output
- the exact production error, not only a screenshot
