# Popover (RxPopover)

Floating contextual overlay with a customizable `#trigger` slot, internal open state synced with `:open`, and `update:open` emission.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxPopover` looks and behaves in real time:

<RxComponentPreview component="RxPopover" title="Popover (RxPopover) — Live Visual Preview" />

## Import

```ts
import { RxPopover } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxPopover } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxPopover, RxButton, RxBadge } from 'resuxjs/ui'

const isOpen = ref(false)
</script>

<template>
  <RxPopover :open="isOpen" @update:open="isOpen = $event">
    <template #trigger>
      <RxButton variant="outline" size="sm">
        Runtime Inspector <RxBadge variant="primary">Live</RxBadge>
      </RxButton>
    </template>
    <div class="space-y-1.5 text-xs min-w-[220px]">
      <div class="font-semibold">Active Resux Payload</div>
      <div class="flex justify-between"><span>Route:</span><code>/components/popover</code></div>
      <div class="flex justify-between"><span>View Transition:</span><code>enabled</code></div>
      <div class="flex justify-between"><span>Hydrated Islands:</span><code>0</code></div>
    </div>
  </RxPopover>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxPopover` produces the following HTML structure (`rx-popover > div (trigger) + [div.rx-popover-content]`):

```html
<div class="rx-popover">
  <div><button class="rx-btn rx-btn-outline rx-btn-sm">Runtime Inspector</button></div>
  <div class="rx-popover-content">
    <div class="font-semibold">Active Resux Payload</div>
  </div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `open` | `boolean` | `false` | No | Initial or controlled open state. |
| `unstyled` | `boolean` | `false` | No | Omits `rx-popover` and `rx-popover-content` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:open` | `boolean` | Emitted whenever the trigger toggles the popover open or closed. |

## Slots

| Slot | Description |
| --- | --- |
| `trigger` | Clickable trigger element (defaults to `<button>Toggle</button>`). |
| `default` | Floating panel content rendered inside `.rx-popover-content`. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxPopover unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxPopover
</RxPopover>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
