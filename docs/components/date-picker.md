# DatePicker

`RxDatePicker` is a thin Vue wrapper around native `<input type="date">`. Use it when you need a standard single-date field and do not need a custom calendar, range selection, time selection, or advanced disabled-date logic.

## Import

```ts
import { RxDatePicker } from 'resuxjs/ui'
// Equivalent alias: ResuxDatePicker
```

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxDatePicker } from 'resuxjs/ui'

const birthday = ref('')
</script>

<template>
  <RxDatePicker v-model="birthday" />
</template>
```

## `Date` input values

The prop accepts `string | Date`. A valid `Date` is rendered as the UTC ISO date portion (`YYYY-MM-DD`). An invalid `Date` renders as an empty value instead of throwing.

```vue
<RxDatePicker :model-value="new Date('2026-08-11T12:00:00Z')" />
```

When the user edits the field, the component emits the native input's **string** value; it does not emit a `Date` object.

## Native constraints

Undeclared attributes are forwarded to the `<input>`, so native date constraints work:

```vue
<RxDatePicker
  v-model="date"
  min="2026-01-01"
  max="2026-12-31"
  required
/>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string | Date` | `''` | No | Date input value. Valid `Date` values are formatted as `YYYY-MM-DD`. |
| `placeholder` | `string` | `'Select date'` | No | Forwarded placeholder. Browser date inputs may not display placeholders consistently. |
| `unstyled` | `boolean` | `false` | No | Omits `rx-input rx-datepicker`. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Native date input value, normally `YYYY-MM-DD` or empty. |

## Slots

No slots.

## Styling

The styled input receives `rx-input rx-datepicker`. The current default CSS is primarily inherited from `rx-input`.

## Accessibility

Native date-input semantics and browser keyboard/calendar behavior are preserved. Always provide a label. Remember that the browser's date-picker UI and date presentation vary by platform and locale even though the submitted value format is normalized by HTML.

## SSR / resumability / hydration

Initial markup/value can be server-rendered in the Vue island. `v-model` synchronization requires Vue runtime JavaScript. If a native date field can submit directly with an HTML form, using a plain Resux template input avoids the Vue island cost.

## When not to use

Use another tested integration for:

- date ranges
- multiple dates
- date + time
- locale-specific custom calendars
- complex disabled-date rules
- calendar popovers that require a complete accessible dialog/grid pattern

See the [Integration Cookbook](/guide/integration-cookbook#date-pickers).

## Related

- [Input](./input.md)
- [Integration Cookbook](/guide/integration-cookbook)
