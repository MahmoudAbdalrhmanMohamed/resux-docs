# Components

Resux components use `.vue` files with a focused single-file component subset.

## Basic shape

```vue
<script setup lang="ts">
const props = defineProps<{ label: string }>()
const clicked = useState('clicked', () => false)

function markClicked() {
  clicked.value = true
}
</script>

<template>
  <button @click="markClicked">
    {{ props.label }}
    <span v-if="clicked">done</span>
  </button>
</template>
```

A component needs a `<template>` block. The `<script setup lang="ts">` block can define state, handlers, props, meta, and helper values.

## Pages

Files in `pages/` become routes. A page is still a component, but it can also use `definePageMeta`.

```vue
<script setup lang="ts">
definePageMeta({
  layout: 'marketing',
  title: 'Pricing'
})
</script>

<template>
  <section>
    <h1>Pricing</h1>
  </section>
</template>
```

## Components directory

Files in `components/` are discovered and can be used as PascalCase tags.

```txt
components/AppButton.vue
```

```vue
<template>
  <AppButton label="Save" />
</template>
```

## Props

Use `defineProps()` inside script setup:

```vue
<script setup lang="ts">
const props = defineProps<{
  title: string
  count?: number
}>()
</script>

<template>
  <article>
    <h2>{{ props.title }}</h2>
    <p>{{ props.count ?? 0 }}</p>
  </article>
</template>
```

Props should be JSON-serializable when they need to be resumed.

## Events

Use named handlers or resumability-safe inline expressions.

```vue
<script setup lang="ts">
const count = useState('count', () => 0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">{{ count }}</button>
  <button @click="count.value = 0">Reset</button>
</template>
```

Handlers must only capture resumable values such as refs returned from `useState` or data that can be recreated safely.

## Lifecycle

`onMounted()` runs when a component scope is first resumed in the browser, not during the first server render.

```vue
<script setup lang="ts">
onMounted(() => {
  console.log('scope resumed in the browser')
})
</script>
```

## Components are not Vue runtime components

Normal Resux components do not use Vue hydration. For full Vue runtime behavior, use [Vue Islands](/guide/vue-islands).

## Built-in Resux Elements

Resux provides zero-hydration built-in elements for media, navigation, and UI primitives:

### `<ResuxVideo>`
High-performance resumable video component supporting lazy loading and deferred initial frame strategies:

```vue
<template>
  <ResuxVideo
    src="/hero.webm"
    poster="/poster.webp"
    load-strategy="page-ready"
    autoplay
    muted
    loop
    playsinline
    controls-mode="none"
  />
</template>
```

- **`loadStrategy`**: `"eager"` | `"lazy"` | `"visible"` | `"page-ready"`. Under `"page-ready"`, Resux renders the initial poster frame immediately in SSR and emits ZERO video network requests until full document `window.load`, eliminating network congestion during critical page rendering.
- **`controlsMode`**: `"custom"` | `"native"` | `"none"`.

### `<ResuxImg>` & `<ResuxPicture>`
Resumable responsive image elements with automatic placeholders, IntersectionObserver lazy loading, and error handling.

### `<ResuxLink>`
Route-aware resumable link element replacing native internal `<a>` tags for client-side SPA payload transitions.

### UI & Motion Primitives
For the complete suite of UI & Motion Primitives (`ResuxSelect`, `ResuxDatePicker`, `ResuxPopover`, `ResuxIcon`, `ResuxReveal`, `ResuxAutoAnimate`, `RxButton`, `RxCard`, `RxAvatar`, `RxAlert`, `RxAccordion`, `RxTooltip`, `RxDropdown`, `RxTabs`, `RxSwitch`, `RxSkeleton`, `RxDivider`, `RxKbd`), see the [UI & Motion Primitives (`resuxjs/ui`)](/guide/ui-animations) guide.


