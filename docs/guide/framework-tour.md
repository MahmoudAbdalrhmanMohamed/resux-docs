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
