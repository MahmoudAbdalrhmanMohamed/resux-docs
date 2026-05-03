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
