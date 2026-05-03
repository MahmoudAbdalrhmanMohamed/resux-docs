# Layouts

Layouts wrap pages. They live in `layouts/` and use `<slot />` for page content.

## Default layout

Create `layouts/default.vue`:

```vue
<template>
  <div class="layout">
    <header>
      <ResuxLink to="/">Home</ResuxLink>
      <ResuxLink to="/about">About</ResuxLink>
    </header>

    <main>
      <slot />
    </main>
  </div>
</template>
```

## Select a layout

```vue
<script setup lang="ts">
definePageMeta({ layout: 'marketing' })
</script>

<template>
  <h1>Landing page</h1>
</template>
```

This uses `layouts/marketing.vue`.

## Disable layouts

```ts
definePageMeta({ layout: false })
```

## App shell

`app.vue` can wrap the active page:

```vue
<template>
  <ResuxLayout>
    <ResuxPage />
  </ResuxLayout>
</template>
```

For very simple apps, you can omit `app.vue` and let pages render directly.

## Same-layout navigation

The client runtime can keep the active layout DOM when the next route uses the same layout name, then swap only the page slot. This keeps persistent layout UI stable across route changes.
