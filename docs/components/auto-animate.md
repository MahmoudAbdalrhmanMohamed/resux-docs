# AutoAnimate (RxAutoAnimate)

Zero-config mount & list container animation wrapper (`scale-in` on mount) for dynamic queues, tag lists, and notification stacks.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxAutoAnimate` looks and behaves in real time:

<RxComponentPreview component="RxAutoAnimate" title="AutoAnimate (RxAutoAnimate) — Live Visual Preview" />

## Import

```ts
import { RxAutoAnimate } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxAutoAnimate } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxAutoAnimate, RxButton, RxBadge } from 'resuxjs/ui'

const items = ref(['resuxjs/runtime', 'resuxjs/ui', 'resuxjs/icons', 'resuxjs/fonts'])

function addModule() {
  const next = `resuxjs/module-${items.value.length + 1}`
  items.value = [...items.value, next]
}

function removeItem(mod: string) {
  items.value = items.value.filter((i) => i !== mod)
}
</script>

<template>
  <div class="space-y-3">
    <div class="flex gap-2">
      <RxButton size="sm" variant="primary" @click="addModule">+ Add Module</RxButton>
    </div>
    <RxAutoAnimate :duration="300" class="flex flex-wrap gap-2">
      <RxBadge
        v-for="mod in items"
        :key="mod"
        variant="default"
        class="cursor-pointer"
        @click="removeItem(mod)"
      >
        {{ mod }} ×
      </RxBadge>
    </RxAutoAnimate>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxAutoAnimate` produces the following HTML structure (`<div> (scale-in animation wrapper)`):

```html
<div>
  <span class="rx-badge rx-badge-default">resuxjs/runtime ×</span>
  <span class="rx-badge rx-badge-default">resuxjs/ui ×</span>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `duration` | `number` | `300` | No | Duration in milliseconds for the `scale-in` animation. |
| `unstyled` | `boolean` | `false` | No | Consistency prop. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Dynamic list or container items. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxAutoAnimate unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxAutoAnimate
</RxAutoAnimate>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
