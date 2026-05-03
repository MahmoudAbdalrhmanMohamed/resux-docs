# App Shell, Errors, and Public Files

Resux apps can define a small set of top-level files that shape every rendered page: the app shell, layouts, the error page, and static public assets.

## App shell

`app.vue` is the outer component for page rendering. It is optional, but most apps use it for global structure such as skip links, providers, global navigation, and layout placement.

```vue
<template>
  <ResuxLayout>
    <ResuxPage />
  </ResuxLayout>
</template>
```

`<ResuxPage />` renders the matched page component. `<ResuxLayout />` renders the selected layout and passes the page into the layout slot.

## Layout placement

Use the app shell when every page should pass through the same layout pipeline:

```vue
<template>
  <div class="app-shell">
    <ResuxLayout>
      <ResuxPage />
    </ResuxLayout>
  </div>
</template>
```

Use page meta to choose a layout:

```ts
definePageMeta({ layout: 'dashboard' })
```

Set `layout: false` for a page that should render without a layout.

## Layout slots

Layouts live in `layouts/` and render their page content with `<slot />`.

```vue
<!-- layouts/default.vue -->
<template>
  <main>
    <slot />
  </main>
</template>
```

Layouts are still Resux components. Keep their state serializable and use Vue islands for complex browser-only layout widgets.

## Error page

`error.vue` or `app/error.vue` customizes 404 and 500 rendering. Use it for branded error pages and recovery links.

```vue
<script setup lang="ts">
defineProps<{
  statusCode?: number
  message?: string
}>()
</script>

<template>
  <main>
    <h1>{{ statusCode || 500 }}</h1>
    <p>{{ message || 'Something went wrong.' }}</p>
    <ResuxLink to="/">Go home</ResuxLink>
  </main>
</template>
```

Keep the error page defensive. It may render when normal page data, route middleware, or server handlers have failed.

## Public files

Files under `public/` are served from the web root.

```txt
public/favicon.svg -> /favicon.svg
public/robots.txt  -> /robots.txt
public/images/card.png -> /images/card.png
```

Use `public/` for static files that do not need compilation. Use normal component imports or CSS references for assets that should be processed by the app toolchain.

## Nested app directory

The compiler also checks nested app conventions:

```txt
app/pages/
app/app.vue
app/error.vue
```

This is useful when an app wants repository files at the root and application source under `app/`.

## Related pages

- [Project Structure](/guide/project-structure)
- [Layouts](/guide/layouts)
- [File Conventions](/reference/file-conventions)
