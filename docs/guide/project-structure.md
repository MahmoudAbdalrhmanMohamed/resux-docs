# Project Structure

Resux discovers files from a small set of conventions. Most apps start with this shape:

```txt
my-app/
  app.vue
  error.vue
  resux.config.ts
  pages/
    index.vue
    about.vue
    post/[id].vue
    docs/[...slug].vue
  components/
    AppButton.vue
  layouts/
    default.vue
    marketing.vue
  middleware/
    auth.ts
    analytics.global.ts
  plugins/
    app.ts
  server/
    api/
      stats.ts
    routes/
      robots.txt.ts
    middleware/
      headers.ts
  public/
    favicon.svg
```

## Root files

| File | Purpose |
| --- | --- |
| `app.vue` | Optional app shell. Use `<ResuxPage />` to render the current page. |
| `error.vue` | Optional custom 404/500 error page. |
| `resux.config.ts` | App config, runtime config, CSS, head, modules, route rules. |
| `env.d.ts` | Generated starter type hook for `resuxjs/globals`. |
| `tsconfig.json` | Generated starter TypeScript config. |

## App directories

| Directory | Purpose |
| --- | --- |
| `pages/` | File-based route pages. |
| `components/` | Auto-discovered component tags. |
| `layouts/` | Layout components used by `definePageMeta({ layout })`. |
| `middleware/` | Route middleware. Files ending `.global.ts` run globally. |
| `plugins/` | App plugins created with `defineResuxPlugin`. |
| `server/api/` | API handlers under `/api`. |
| `server/routes/` | Server route handlers outside `/api`. |
| `server/middleware/` | Request middleware that runs before handlers and pages. |
| `islands/vue/` | Full Vue runtime islands. |
| `public/` | Static assets served from the web root. |

## Generated directories

| Directory | Created by | Purpose |
| --- | --- | --- |
| `.resux/` | `resux dev`, `resux build`, `resux compile` | Resux manifest, compiled server modules, handler chunks, runtime client. |
| `.output/` | `resux build` | Nitro production server output. |
| `.resux-nitro/` | `resux deploy --preset nitro` or build helper | Nitro adapter handler. |

Do not edit `.resux` or `.output` by hand. Change source files and rebuild.

## Alternative app directory

The compiler also checks `app/pages`, `app/app.vue`, and `app/error.vue`. This can help apps that prefer a nested application source directory.
