# Select (RxSelect)

Accessible native `<select>` wrapper supporting string arrays or `{ label, value, disabled }` option objects with a custom chevron indicator.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxSelect` looks and behaves in real time:

<RxComponentPreview component="RxSelect" title="Select (RxSelect) — Live Visual Preview" />

## Import

```ts
import { RxSelect } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxSelect } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxSelect, RxBadge } from 'resuxjs/ui'

const region = ref('eu-central-1')
const regions = [
  { label: 'Frankfurt (eu-central-1) — Low Latency', value: 'eu-central-1' },
  { label: 'London (eu-west-2)', value: 'eu-west-2' },
  { label: 'US East (us-east-1)', value: 'us-east-1' },
  { label: 'Tokyo (ap-northeast-1) — Maintenance', value: 'ap-northeast-1', disabled: true }
]
</script>

<template>
  <div class="space-y-2 max-w-md">
    <div class="flex items-center justify-between">
      <label class="text-sm font-medium">Deployment Edge Region</label>
      <RxBadge variant="primary">{{ region }}</RxBadge>
    </div>
    <RxSelect
      v-model="region"
      :options="regions"
      placeholder="Choose an edge region"
    />
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxSelect` produces the following HTML structure (`rx-select > select.rx-select-native + span.rx-select-arrow`):

```html
<div class="rx-select" data-disabled="false">
  <select class="rx-select-native">
    <option value="" disabled>Choose an edge region</option>
    <option value="eu-central-1" selected>Frankfurt (eu-central-1) — Low Latency</option>
    <option value="eu-west-2">London (eu-west-2)</option>
    <option value="us-east-1">US East (us-east-1)</option>
  </select>
  <span class="rx-select-arrow" aria-hidden="true">▾</span>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string \| number` | `''` | No | Currently selected option value (`v-model`). |
| `options` | `Array<string \| { label: string; value: string \| number; disabled?: boolean }>` | `[]` | No | List of selectable options. |
| `placeholder` | `string` | `'Select an option'` | No | Disabled empty option rendered at the top of the list. |
| `disabled` | `boolean` | `false` | No | Disables the select control and sets `data-disabled="true"`. |
| `unstyled` | `boolean` | `false` | No | Renders a bare `<select>` without the `.rx-select` wrapper or arrow span. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Emitted when the user selects a new option. |

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxSelect unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxSelect
</RxSelect>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
