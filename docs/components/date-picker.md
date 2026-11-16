# DatePicker (RxDatePicker)

Native HTML5 date input control (`type="date"`) with `v-model` support and consistent `rx-input rx-datepicker` styling.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxDatePicker` looks and behaves in real time:

<RxComponentPreview component="RxDatePicker" title="DatePicker (RxDatePicker) — Live Visual Preview" />

## Import

```ts
import { RxDatePicker } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxDatePicker } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxDatePicker, RxBadge } from 'resuxjs/ui'

const releaseDate = ref('2026-11-20')
</script>

<template>
  <div class="space-y-2 max-w-xs">
    <div class="flex items-center justify-between">
      <label class="text-sm font-medium">Scheduled Release Window</label>
      <RxBadge variant="default">{{ releaseDate || 'Unscheduled' }}</RxBadge>
    </div>
    <RxDatePicker
      v-model="releaseDate"
      min="2026-01-01"
      max="2027-12-31"
    />
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxDatePicker` produces the following HTML structure (`rx-input rx-datepicker`):

```html
<input
  type="date"
  value="2026-11-20"
  placeholder="Select date"
  class="rx-input rx-datepicker"
/>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string \| Date` | `''` | No | Selected ISO date string (`YYYY-MM-DD`) or Date instance. |
| `placeholder` | `string` | `'Select date'` | No | Fallback placeholder text. |
| `disabled` | `boolean` | `false` | No | Disables date selection. |
| `unstyled` | `boolean` | `false` | No | Strips `rx-input rx-datepicker` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Emitted on `input` with the selected `YYYY-MM-DD` string. |

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxDatePicker unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxDatePicker
</RxDatePicker>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
