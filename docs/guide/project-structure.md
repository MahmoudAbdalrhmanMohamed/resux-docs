# Project Structure

Resux supports root-level application directories and matching `app/` directories for the main application conventions.

## Common structure

```txt
my-app/
  app.vue
  error.vue
  resux.config.ts
  resux.halal.config.ts
  env.d.ts
  tsconfig.json
  pages/
  components/
  layouts/
  composables/
  utils/
  shared/
  plugins/
  middleware/
  enhancements/
  client-enhancements/
  islands/vue/
  server/
    api/
    routes/
    middleware/
    plugins/
    utils/
  assets/
  public/
  types/
```

Most application directories can also live under `app/`, including pages, components, layouts, plugins, middleware, enhancements, and the app/error components.

## Root files

| File | Purpose |
| --- | --- |
| `app.vue` | Optional application shell. Usually contains `<ResuxPage />`. |
| `error.vue` | Optional error renderer for not-found and server errors. |
| `resux.config.ts` | Framework, app head, runtime config, CSS, modules, packages, deployment, media, i18n, and route rules. |
| `resux.halal.config.ts` | Safety policy, project description, evidence, review contact, and optional AI settings. |
| `env.d.ts` | Adds generated Resux globals and application types. |
| `tsconfig.json` | TypeScript project configuration. |
| `nitro.config.ts` | Nitro deployment/server configuration. |
| `.env.example` | Non-secret environment variable documentation. |

## Application directories

| Directory | Behavior |
| --- | --- |
| `pages/` | File-based routes. Dynamic and catch-all segments are supported. |
| `components/` | Auto-discovered Resux components. Modules can add more directories. |
| `layouts/` | Named layouts selected through page metadata. |
| `composables/` | Auto-imported shared functions and package-analysis input. |
| `utils/` | Auto-imported shared utilities. |
| `shared/` | Auto-imported shared modules. |
| `plugins/` | App plugins. `.client` and `.server` suffixes set execution mode. |
| `middleware/` | Named and global route middleware. `.global` marks global middleware. |
| `enhancements/` | Client enhancement plugin files. |
| `client-enhancements/` | Explicit client enhancement plugin files. |
| `islands/vue/` | Full Vue runtime island components. |
| `assets/` | Source assets and global CSS. `/assets/*` imports are served safely. |
| `public/` | Static files served from the web root. |
| `types/` | Application declarations and module augmentation. |

## Server directories

| Directory | Behavior |
| --- | --- |
| `server/api/` | Handlers mounted under `/api`. |
| `server/routes/` | Custom handlers mounted without the `/api` prefix. |
| `server/middleware/` | Request middleware before APIs, public files, and pages. |
| `server/plugins/` | Server-only setup included in package analysis and Nitro integration. |
| `server/utils/` | Server-only auto-imported utilities. |

## Generated directories

| Directory | Purpose |
| --- | --- |
| `.resux/` | Compiler manifests, server modules, browser handlers, client assets, diagnostics, generated templates, and generated types. |
| `.resux/vite-client/` | Development client sources consumed by Vite. |
| `.resux/client/` | Production browser runtime, plugins, middleware, handlers, chunks, and assets. |
| `.resux/server/` | Development/server modules and manifests. |
| `.resux/server-bundle/` | Bundled production server manifest. |
| `.resux/dev/` | Inspectable development manifests and diagnostics. |
| `.resux/types/` | Generated type declarations. |
| `.resux-nitro/` | Generated Nitro bridge files. |
| `.nitro/` | Nitro working output. |
| `.output/` | Deployable Nitro output. |
| `.resux-generated/` | Persistent generated media cache when enabled. |

Generated output should be ignored by Git and regenerated with `resux prepare`, `resux dev`, or `resux build`.

## Naming suffixes

Support TypeScript files understand suffixes such as:

```txt
plugins/analytics.client.ts
plugins/database.server.ts
middleware/auth.ts
middleware/log.global.ts
middleware/admin.server.ts
```

Modules can also register files explicitly and override their mode, global status, or public name.

See [File Conventions](/reference/file-conventions) for the complete mapping.
