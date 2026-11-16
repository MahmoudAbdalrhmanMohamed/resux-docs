# Tabs (RxTabs)

Controlled horizontal tab bar (`v-model`) that renders `.rx-tab-btn` triggers from an `items` array of `{ label, key }` objects.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxTabs` looks and behaves in real time:

<RxComponentPreview component="RxTabs" title="Tabs (RxTabs) — Live Visual Preview" />

## Import

```ts
import { RxTabs } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxTabs } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxTabs, RxCard } from 'resuxjs/ui'

const activeTab = ref('ssr')
const tabItems = [
  { label: 'SSR & Resumability', key: 'ssr' },
  { label: 'View Transitions', key: 'vt' },
  { label: 'Fontless Engine', key: 'fonts' }
]
</script>

<template>
  <div class="space-y-3 max-w-lg">
    <RxTabs v-model="activeTab" :items="tabItems" />
    <RxCard>
      <p v-if="activeTab === 'ssr'" class="text-sm">
        Server-rendered HTML streams immediately while serialized handlers resume on interaction.
      </p>
      <p v-else-if="activeTab === 'vt'" class="text-sm">
        Native browser View Transitions coordinate with route CSS preloading before DOM swaps.
      </p>
      <p v-else class="text-sm">
        Fontless 1.3.4 &amp; Fontaine 1.0.3 compute metric-adjusted fallback faces to reduce font-induced CLS.
      </p>
    </RxCard>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxTabs` produces the following HTML structure (`rx-tabs > div.rx-tabs-header > button.rx-tab-btn [.active]`):

```html
<div class="rx-tabs">
  <div class="rx-tabs-header">
    <button class="rx-tab-btn active">SSR &amp; Resumability</button>
    <button class="rx-tab-btn">View Transitions</button>
    <button class="rx-tab-btn">Fontless Engine</button>
  </div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `items` | `Array<{ label: string; key: string }>` | `[]` | No | Tab definitions with display `label` and unique `key`. |
| `modelValue` | `string` | `''` | No | Active tab key (`v-model`). |
| `unstyled` | `boolean` | `false` | No | Strips `rx-tabs*` and `rx-tab-btn` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Emitted with `item.key` when a tab button is clicked. |

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxTabs unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxTabs
</RxTabs>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
