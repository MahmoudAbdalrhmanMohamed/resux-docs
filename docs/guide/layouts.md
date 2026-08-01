# Layouts

Layouts wrap pages without adding whole-app hydration.

## Default layout

```vue
<!-- layouts/default.vue -->
<template>
  <div class="layout">
    <header>Site header</header>
    <main><slot /></main>
    <footer>Site footer</footer>
  </div>
</template>
```

Select it from a page:

```ts
definePageMeta({ layout: 'default' })
```

## Named layout

```txt
layouts/dashboard.vue
```

```ts
definePageMeta({ layout: 'dashboard' })
```

Layout names come from their file paths and are normalized by the compiler.

## Disable a layout

```ts
definePageMeta({ layout: false })
```

## App shell relationship

A common `app.vue` structure is:

```vue
<template>
  <ResuxLayout>
    <ResuxPage />
  </ResuxLayout>
</template>
```

The app shell is global. A layout is page-selectable. The page is the matched route component.

## Layout state

A layout is a normal Resux component and can use state, async data, head helpers, and resumable handlers. Keep state keys stable and serializable.

## Head composition

App, module, layout, and page head entries are composed rather than treated as one replace-only object. Arrays such as meta and links can accumulate; attributes are merged. Verify final output with:

```sh
resux inspect seo --json
```

## Localized layouts

Layouts do not need separate copies for each locale. Use i18n helpers and the current route locale inside the same component.
