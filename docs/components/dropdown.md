# Dropdown

`RxDropdown` is a compact click-toggled action list. Items contain a label and an optional callback.

## Import

```ts
import { RxDropdown } from 'resuxjs/ui'
// Equivalent alias: ResuxDropdown
```

## Basic usage

```vue
<script setup lang="ts">
import { RxDropdown } from 'resuxjs/ui'

const items = [
  { label: 'Rename', action: () => rename() },
  { label: 'Archive', action: () => archive() }
]
</script>

<template>
  <RxDropdown :items="items" />
</template>
```

The built-in trigger text is `Menu`.

## Open state

```vue
<RxDropdown v-model:open="open" :items="items" />
```

Clicking the trigger emits `update:open`. Selecting an item calls its optional `action` callback and emits `update:open` with `false`.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `items` | `{ label: string; action?: () => void }[]` | `[]` | No | Action entries. |
| `open` | `boolean` | `false` | No | Current list visibility. |
| `unstyled` | `boolean` | `false` | No | Omits Resux dropdown classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:open` | `boolean` | Trigger toggles or item selection closes the dropdown. |

## Slots

No slots. The trigger label and item rendering are fixed by the current implementation.

## Styling

Styled markup uses `rx-dropdown`, `rx-dropdown-trigger`, `rx-dropdown-menu`, and `rx-dropdown-item`.

## Accessibility

The trigger is a native button, but the list is rendered as `<ul><li>…</li></ul>` without menu roles, item buttons, roving focus, Arrow-key handling, Escape handling, focus return, or `aria-expanded`. Item activation is currently attached to the `<li>` click.

::: danger Accessibility limitation
Do not represent `RxDropdown` as a complete keyboard-accessible application menu. For important actions, a visible list of native buttons/links—or a tested menu integration—is safer until the primitive grows the complete interaction contract.
:::

## SSR / resumability / hydration

Open state and action callbacks require the Vue runtime boundary. Initial closed markup can be SSR-rendered, but the dropdown is not a zero-hydration Resux control.

## Related

- [Popover](./popover.md)
- [Select](./select.md)
- [Current limits](/reference/limits)
