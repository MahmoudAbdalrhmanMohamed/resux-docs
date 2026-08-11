# Tabs

`RxTabs` renders a row/list of buttons and emits the selected item key. It does **not** render tab panels for you.

## Import

```ts
import { RxTabs } from 'resuxjs/ui'
// Equivalent alias: ResuxTabs
```

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxTabs } from 'resuxjs/ui'

const tab = ref('overview')
const tabs = [
  { label: 'Overview', key: 'overview' },
  { label: 'Activity', key: 'activity' }
]
</script>

<template>
  <RxTabs v-model="tab" :items="tabs" />
  <section v-if="tab === 'overview'">Overview panel</section>
  <section v-else-if="tab === 'activity'">Activity panel</section>
</template>
```

## Selection

Each button receives `active` when its key exactly equals `modelValue`. Clicking a button emits that item's key.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `items` | `{ label: string; key: string }[]` | `[]` | No | Tab-button definitions. |
| `modelValue` | `string` | `''` | No | Selected key. |
| `unstyled` | `boolean` | `false` | No | Omits Resux tab classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Selected item's key. |

## Slots

No slots are declared. Panel content is application-owned.

## Styling

Styled markup uses `rx-tabs` on the root, `rx-tabs-header` on the button container, and `rx-tab-btn` on each button. The selected button additionally receives `active`.

## Accessibility

The buttons retain native button semantics, but the current implementation does **not** implement the ARIA Tabs pattern: there is no `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`, roving tab index, Arrow Left/Right handling, Home/End handling, or built-in `tabpanel` relationship.

::: danger Accessibility limitation
`RxTabs` is currently a selection-button primitive, not a complete accessible tabs widget. If you present its UI as tabs, application code must implement/test the missing relationships and keyboard behavior, or choose another accessible integration.
:::

## SSR / resumability / hydration

Initial active classes can be SSR-rendered. Selection and parent panel switching require Vue runtime JavaScript.

## Complete example with explicit panel semantics

The component cannot generate tab IDs/panel relationships itself. If you need a standards-complete tab interface, prefer a component that owns those relationships. For a lightweight button-driven content selector, label the resulting content plainly instead of claiming full tabs semantics.

## Related

- [Accordion](./accordion.md)
- [Current limits](/reference/limits)
- [Integration Cookbook](/guide/integration-cookbook)
