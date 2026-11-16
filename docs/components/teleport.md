# Teleport (Built-in Framework Primitive)

Nuxt/Vue-compatible `<Teleport to="#selector">` primitive that injects server-rendered HTML into target containers (`body`, `#modals`, `#notifications`) and resumes event handlers across DOM boundaries.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `Teleport` looks and behaves in real time:

<RxComponentPreview component="Teleport" title="Teleport (Built-in Framework Primitive) — Live Visual Preview" />

## Import

```vue
<!-- Built-in Resux template primitive (no import required in .vue templates) -->
<Teleport>...</Teleport>
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxButton, RxBadge } from 'resuxjs/ui'

const showBanner = ref(true)
const disableTeleport = ref(false)
</script>

<template>
  <div class="space-y-3">
    <div class="flex gap-2">
      <RxButton size="sm" variant="primary" @click="showBanner = !showBanner">
        {{ showBanner ? 'Unmount Teleported Toast' : 'Mount Teleported Toast' }}
      </RxButton>
      <RxButton size="sm" variant="outline" @click="disableTeleport = !disableTeleport">
        disabled={{ disableTeleport }}
      </RxButton>
    </div>

    <Teleport to="#teleport-demo-target" :disabled="disableTeleport">
      <div v-if="showBanner" class="p-3 rounded-lg border border-indigo-500/40 bg-indigo-500/10 flex items-center justify-between text-xs">
        <span>Teleported into <code>{{ disableTeleport ? 'inline container' : '#teleport-demo-target' }}</code></span>
        <RxBadge variant="primary">SSR + Resumable</RxBadge>
      </div>
    </Teleport>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `Teleport` produces the following HTML structure (`data-rx-teleport-start / data-rx-teleport-end markers`):

```html
<!-- Inside #teleport-demo-target -->
<div class="p-3 rounded-lg border border-indigo-500/40 bg-indigo-500/10">
  <span>Teleported into <code>#teleport-demo-target</code></span>
  <span class="rx-badge rx-badge-primary">SSR + Resumable</span>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `to` | `string` | `'body'` | Yes | Target CSS selector or `'body'` where slot content is rendered. |
| `disabled` | `boolean` | `false` | No | When `true`, renders slot children inline at the component's original DOM position. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Elements to teleport into the target container while keeping parent component state and handlers. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<Teleport unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled Teleport
</Teleport>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
