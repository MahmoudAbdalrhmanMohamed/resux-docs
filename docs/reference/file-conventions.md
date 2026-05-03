# File Conventions

## Routes

```txt
pages/index.vue       -> /
pages/about.vue       -> /about
pages/post/[id].vue   -> /post/:id
pages/docs/[...slug].vue -> /docs/:slug*
```

## Components

```txt
components/AppButton.vue -> <AppButton />
```

Component names are inferred from filenames and paths.

## Layouts

```txt
layouts/default.vue
layouts/dashboard.vue
```

Use from pages:

```ts
definePageMeta({ layout: 'dashboard' })
```

## App shell

```txt
app.vue
app/app.vue
```

Use `<ResuxPage />` and `<ResuxLayout />` inside the app shell.

## Error page

```txt
error.vue
app/error.vue
```

Use for custom 404/500 rendering.

## Middleware

```txt
middleware/auth.ts
middleware/analytics.global.ts
```

- Normal files run when referenced by page meta.
- `.global.ts` files run for every route.

## Plugins

```txt
plugins/app.ts
```

Export `defineResuxPlugin`.

## Server handlers

```txt
server/api/stats.ts
server/routes/robots.txt.ts
```

- `server/api` maps under `/api`.
- `server/routes` maps from the root.

## Request middleware

```txt
server/middleware/headers.ts
```

Runs before server handlers, public files, and page rendering.

## Vue islands

```txt
islands/vue/CounterIsland.vue
```

Use with:

```vue
<VueIsland name="CounterIsland" :props="{ start: 1 }" />
```

## Static public files

```txt
public/favicon.svg -> /favicon.svg
public/robots.txt  -> /robots.txt
```

## Build output

```txt
.resux/
.output/
```

Do not commit these unless you intentionally deploy generated output.
