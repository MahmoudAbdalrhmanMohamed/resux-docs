# Components

Resux components use a compiler-supported `.vue` SFC subset and render without default Vue hydration.

## Basic component

```vue
<script setup lang="ts">
const props = defineProps<{ label: string; step?: number }>()
const emit = defineEmits<{ changed: [value: number] }>()
const count = useState('button-count', () => 0)

function increment() {
  count.value += props.step ?? 1
  emit('changed', count.value)
}
</script>

<template>
  <button @click="increment">
    {{ props.label }}: {{ count }}
  </button>
</template>

<style scoped>
button { font: inherit; }
</style>
```

A Resux component requires a `<template>` block. Plain CSS and scoped CSS are supported. Style modules, style `src`, and non-CSS style languages are rejected for resumable components.

## Setup macros

The setup context provides compiler-compatible helpers including:

- `defineProps`
- `defineEmits`
- `defineExpose`
- `defineSlots`
- `defineOptions`
- `defineModel`
- `definePageMeta`

Use only the behavior documented for Resux; these helpers do not imply complete Vue SFC compatibility.

## Auto-discovery

Components are discovered from:

- `components/`
- `app/components/`
- module-added component files
- module-added component directories

Generated component declarations are written under `.resux/types` and made available during preparation.

## Pages and layouts are components

Pages may define route metadata:

```ts
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth'],
  title: 'Dashboard',
  meta: [{ name: 'robots', content: 'noindex' }]
})
```

Layouts use `<slot />` to render the page.

## Built-in tags

| Tag | Purpose |
| --- | --- |
| `<ResuxPage />` | Active page placeholder |
| `<ResuxLayout />` | Selected layout wrapper |
| `<ResuxLink>` | Same-origin navigation-aware link |
| `<ResuxImg>` | Responsive optimized image |
| `<ResuxPicture>` | Art-direction picture sources |
| `<ResuxVideo>` | Deferred/optimized video with controls modes |
| `<VueIsland>` | Full Vue runtime boundary |

## Resumable events

Named handlers and supported inline expressions are compiled into client handler modules.

```vue
<button @click="count.value++">Increment</button>
```

Prefer named handlers for complex logic and clearer compile errors.

## Browser-only component work

`onMounted()` runs on the first browser resume of that scope.

```ts
onMounted(() => {
  const observer = new ResizeObserver(updateSize)
  observer.observe(document.body)
  return () => observer.disconnect()
})
```

For library-driven DOM behavior, a [client enhancement](/guide/package-integration#client-enhancements) is often a better boundary. For complete Vue lifecycle and rendering behavior, use [Vue Islands](/guide/vue-islands).

## UI package components

`resuxjs/ui` exports both `Rx*` and `Resux*` names for primitives including:

- Button, Input, Textarea, Select, DatePicker
- Card, Badge, Avatar, Alert, Divider, Skeleton, Kbd
- Accordion, Tabs, Switch, Dropdown, Popover, Tooltip, Modal
- Motion, Reveal, and AutoAnimate

These are Vue runtime components from the optional UI subpath; use them in an appropriate Vue/client context and read [UI & Motion Primitives](/guide/ui-animations).
