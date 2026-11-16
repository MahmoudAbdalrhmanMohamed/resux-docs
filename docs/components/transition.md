# Transition (Built-in Framework Primitive)

Built-in `<Transition>` primitive applying CSS enter/leave classes (`{name}-enter-from`, `{name}-enter-active`, `{name}-leave-to`) when child elements are inserted/removed via `v-if` or have their display state toggled via `v-show`.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `Transition` looks and behaves in real time:

<RxComponentPreview component="Transition" title="Transition (Built-in Framework Primitive) — Live Visual Preview" />

## Import

```vue
<!-- Built-in Resux template primitive (no import required in .vue templates) -->
<Transition>...</Transition>
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxButton, RxCard, RxBadge } from 'resuxjs/ui'

const visible = ref(true)
</script>

<template>
  <div class="space-y-3">
    <RxButton size="sm" variant="secondary" @click="visible = !visible">
      Toggle Transition ({{ visible ? 'Visible' : 'Hidden' }})
    </RxButton>

    <Transition name="fade" mode="out-in">
      <RxCard v-if="visible" key="active">
        <div class="flex items-center justify-between">
          <span class="text-sm font-medium">Active Panel (v-if DOM insertion/removal)</span>
          <RxBadge variant="success">Mounted</RxBadge>
        </div>
      </RxCard>
    </Transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.22s ease, transform 0.22s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(6px);
}
</style>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `Transition` produces the following HTML structure (`${name}-enter-active / ${name}-leave-active`):

```html
<div class="rx-card fade-enter-active">
  <div class="flex items-center justify-between">
    <span class="text-sm font-medium">Active Panel (v-if DOM insertion/removal)</span>
    <span class="rx-badge rx-badge-success">Mounted</span>
  </div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `'v'` | No | Prefix for generated CSS transition classes (`fade-enter-from`, `fade-leave-to`, etc.). |
| `mode` | `'in-out' \| 'out-in' \| 'default'` | `'default'` | No | Controls timing sequence between outgoing and incoming elements. |
| `appear` | `boolean` | `false` | No | Applies the enter transition on initial client mount. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `before-enter` | `Element` | Called before enter transition starts. |
| `after-enter` | `Element` | Called when enter transition completes. |
| `after-leave` | `Element` | Called when leave transition completes. |

## Slots

| Slot | Description |
| --- | --- |
| `default` | Single root element controlled by `v-if` (DOM insertion/removal) or `v-show` (display state toggle). |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<Transition unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled Transition
</Transition>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
