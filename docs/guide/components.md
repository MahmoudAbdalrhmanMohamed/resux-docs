# Components

Resux components use a compiler-supported `.vue` SFC subset and render without default Vue hydration.

## Basic component

```vue
<script setup lang="ts">
const props = defineProps<{ label: string; step?: number }>()
const emit = defineEmits<{ changed: [value: number] }>()
const count = ref(0)

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

## Component events

An emitted event calls the handler written on the component tag:

```vue
<Counter label="Clicks" @changed="onChanged" />
```

```ts
function onChanged(value: number) {
  total.value = value
}
```

- The handler receives all emitted arguments. An inline handler such as `@changed="total = $event"` gets the first argument as `$event`.
- Event names match in camelCase, so `@save-item` and `emit('saveItem')` are the same event.
- Events nobody listens to are ignored.
- During the server render `emit` does nothing. The page payload carries the link from each child to its parent handler, so a resumed child, or a child created in the browser inside `v-if` / `v-for`, reaches its parent without the server running again.
- DOM events on a component tag, such as `@click`, `@input`, `@keydown` or `@submit`, fall through to the child's root element and call the parent's handler, with modifiers such as `.stop` and `.prevent`. This is plain resumable markup, so it works after resume, in `v-for` and for components created in the browser. The child needs one plain element as its root. Fragments, text roots and roots that are components, slots or `v-if` / `v-for` are skipped. If the root element already handles the same event, the parent's listener is not added. Names that are not DOM events, such as `@save`, are component events only. A child that emits an event named like a DOM event, such as `emit('click')`, runs the parent handler for both the emit and the DOM event. Modifiers on component events (`@save.once`) are not supported.

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

`onMounted()` runs on the first browser resume of that scope. It queues browser work, but a cleanup function returned from its callback is not registered for disposal. Use a client enhancement when work owns observers, event listeners, or external instances.

```ts
// enhancements/body-resize-observer.ts
export const bodyResizeObserver = defineClientEnhancement(
  'body-resize-observer',
  (target) => {
    const observer = new ResizeObserver(() => {
      console.log(target.getBoundingClientRect().width)
    })

    observer.observe(target)
    return () => observer.disconnect()
  }
)
```

```ts
onMounted(async () => {
  const enhancement = await useClientEnhancement('body-resize-observer', {
    target: 'body',
    trigger: 'immediate'
  })

  await enhancement.activate()
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
