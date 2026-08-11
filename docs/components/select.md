# Select

`RxSelect` is a small **custom** select primitive. It does not render a native `<select>`; it renders a focusable `<div>`, a trigger, and a conditional listbox.

Use it only when its current interaction model is sufficient. For forms that need the browser's complete native select behavior and accessibility, a native `<select>` is often the better Resux-first choice.

## Import

```ts
import { RxSelect } from 'resuxjs/ui'
// Equivalent alias: ResuxSelect
```

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxSelect } from 'resuxjs/ui'

const role = ref('')
const options = [
  { label: 'Admin', value: 'admin' },
  { label: 'Editor', value: 'editor' }
]
</script>

<template>
  <RxSelect v-model="role" :options="options" placeholder="Choose a role" />
</template>
```

String options are normalized to `{ label, value }` using the same string for both:

```vue
<RxSelect v-model="region" :options="['Africa', 'Europe', 'Asia']" />
```

## Controlled value

The selected value comes from `modelValue`; choosing an option emits `update:modelValue` and closes the internal open state.

```vue
<RxSelect v-model="choice" :options="options" />
```

## Keyboard behavior

The root is focusable when enabled. The implementation currently handles:

- `Enter`: toggle open/closed
- `Space`: toggle open/closed
- `Escape`: close

It **does not** currently implement Arrow Up/Down option navigation, Home/End, typeahead, active-descendant management, or focus movement into the list.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string | number` | `''` | No | Selected option value. |
| `options` | `(string | { label: string; value: string | number })[]` | `[]` | No | Available options. |
| `placeholder` | `string` | `'Select an option'` | No | Text when no matching value is selected. |
| `disabled` | `boolean` | `false` | No | Prevents toggling and sets root `tabindex` to `-1`. |
| `unstyled` | `boolean` | `false` | No | Omits most Resux classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string | number` | Emitted when an option is clicked. |

## Slots

No slots are declared. Labels come from `options`.

## Markup and ARIA

When open, the list uses `role="listbox"` and each item uses `role="option"`. The current implementation does **not** set `aria-selected`, `aria-expanded`, a combobox/select trigger role, `aria-controls`, or active-descendant state.

::: danger Accessibility limitation
`RxSelect` is not a complete ARIA Listbox/Combobox implementation. Do not document or assume full keyboard/screen-reader parity with a native `<select>`. If the control is critical to an accessible form today, prefer native HTML or supply/test the missing interaction semantics in your application.
:::

## Styling

Styled markup uses `rx-select`, `rx-select-trigger`, `rx-select-arrow`, `rx-select-dropdown`, and `rx-select-option`; the selected item also gets `selected`.

## SSR / resumability / hydration

SSR can output the initial custom-select markup, but open/close state, keyboard handling, and option selection are Vue runtime behavior. The component therefore needs a Vue island/runtime boundary.

## Complete example

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxSelect } from 'resuxjs/ui'

const plan = ref('starter')
const plans = [
  { label: 'Starter', value: 'starter' },
  { label: 'Team', value: 'team' },
  { label: 'Enterprise', value: 'enterprise' }
]
</script>

<template>
  <div>
    <span id="plan-label">Plan</span>
    <RxSelect
      v-model="plan"
      :options="plans"
      aria-labelledby="plan-label"
    />
    <p>Selected: {{ plan }}</p>
  </div>
</template>
```

## Related

- [Input](./input.md)
- [Dropdown](./dropdown.md)
- [Current limits](/reference/limits)
- [Vue Islands](/guide/vue-islands)
