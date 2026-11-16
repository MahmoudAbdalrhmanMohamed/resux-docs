# Dropdown (RxDropdown)

Action menu overlay driven by an `items` array of `{ label, action }` objects that automatically closes and invokes `item.action()` on selection.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxDropdown` looks and behaves in real time:

<RxComponentPreview component="RxDropdown" title="Dropdown (RxDropdown) — Live Visual Preview" />

## Import

```ts
import { RxDropdown } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxDropdown } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxDropdown, RxButton, RxBadge } from 'resuxjs/ui'

const lastAction = ref('None')
const menuItems = [
  { label: 'Run Check: Framework Parity', action: () => (lastAction.value = 'Parity Verified') },
  { label: 'Export Static Bundle', action: () => (lastAction.value = 'Bundle Exported') },
  { label: 'Purge Route Cache', action: () => (lastAction.value = 'Cache Purged') }
]
</script>

<template>
  <div class="flex items-center gap-4">
    <RxDropdown :items="menuItems">
      <template #trigger>
        <RxButton variant="secondary" size="sm">Project Actions ▾</RxButton>
      </template>
    </RxDropdown>
    <span class="text-xs opacity-80">Last action: <RxBadge>{{ lastAction }}</RxBadge></span>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxDropdown` produces the following HTML structure (`rx-dropdown > div (trigger) + [ul.rx-dropdown-menu > li.rx-dropdown-item]`):

```html
<div class="rx-dropdown">
  <div><button class="rx-btn rx-btn-secondary rx-btn-sm">Project Actions ▾</button></div>
  <ul class="rx-dropdown-menu">
    <li class="rx-dropdown-item">Run Check: Framework Parity</li>
    <li class="rx-dropdown-item">Export Static Bundle</li>
    <li class="rx-dropdown-item">Purge Route Cache</li>
  </ul>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `items` | `Array<{ label: string; action?: () => void }>` | `[]` | No | Menu items rendered inside `.rx-dropdown-menu`. |
| `open` | `boolean` | `false` | No | Initial open state. |
| `unstyled` | `boolean` | `false` | No | Removes `rx-dropdown*` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:open` | `boolean` | Emitted when toggled or when an item selection closes the menu. |

## Slots

| Slot | Description |
| --- | --- |
| `trigger` | Custom menu trigger button (defaults to `<button>Menu</button>`). |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxDropdown unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxDropdown
</RxDropdown>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
