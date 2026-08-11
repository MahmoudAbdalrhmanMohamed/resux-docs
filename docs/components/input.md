# Input

`RxInput` renders a native `<input>` and implements Vue `v-model` through `modelValue` / `update:modelValue`.

## Import

```ts
import { RxInput } from 'resuxjs/ui'
// Equivalent alias: ResuxInput
```

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxInput } from 'resuxjs/ui'

const email = ref('')
</script>

<template>
  <RxInput v-model="email" type="email" placeholder="you@example.com" />
</template>
```

## Input types

`type` is passed to the native input. The component does not implement type-specific validation logic.

```vue
<RxInput v-model="query" type="search" />
<RxInput v-model="email" type="email" autocomplete="email" />
<RxInput v-model="count" type="number" min="0" />
```

::: warning Number values
The declared `modelValue` prop accepts `string | number`, but the current input handler emits `HTMLInputElement.value`, which is a **string**. It does not use `valueAsNumber`. Parse numeric values in application code if you need a number.
:::

## Labels and validation

`RxInput` does not render a label, error message, or form-field wrapper. Use native labeling and ARIA attributes explicitly.

```vue
<label for="email">Email</label>
<RxInput
  id="email"
  v-model="email"
  type="email"
  :aria-invalid="hasError ? 'true' : 'false'"
  aria-describedby="email-error"
/>
<p v-if="hasError" id="email-error">Enter a valid email address.</p>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string | number` | `''` | No | Controlled input value. Input events emit strings. |
| `type` | `string` | `'text'` | No | Native input type. |
| `placeholder` | `string` | `''` | No | Native placeholder. Do not use it as the only label. |
| `disabled` | `boolean` | `false` | No | Native disabled state. |
| `unstyled` | `boolean` | `false` | No | Omits the `rx-input` class. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` at runtime | Emitted from the native `input` event. |

Other native listeners such as `@change`, `@focus`, and `@blur` can be passed as attributes/listeners.

## Slots

`RxInput` renders a void `<input>` element and has no slots.

## Exposed methods

No methods are explicitly exposed. If you need direct focus control, keep a Vue template ref to the rendered component/element according to your island setup rather than relying on an undocumented exposed API.

## Styling

The styled component receives `rx-input`. The default CSS supplies width, padding, background, border, text color, radius, and a focus border color.

```vue
<RxInput unstyled class="app-input" v-model="value" />
```

## Accessibility

The native input preserves standard semantics and keyboard behavior. Application code remains responsible for a programmatic label, validation messaging, autocomplete hints, input purpose, and any `aria-*` state appropriate to the form.

## SSR / resumability / hydration

The input can be included in Vue SSR output, but `v-model` is Vue-owned runtime behavior. A user can see the server-rendered control before Vue starts, but synchronization back to Vue state requires the Vue island/runtime.

For forms that can submit through normal HTML without Vue state, consider a native Resux template form to preserve the lowest runtime cost.

## Complete example

```vue
<script setup lang="ts">
import { computed, ref } from 'vue'
import { RxInput } from 'resuxjs/ui'

const username = ref('')
const invalid = computed(() => username.value.length > 0 && username.value.length < 3)
</script>

<template>
  <div>
    <label for="username">Username</label>
    <RxInput
      id="username"
      v-model="username"
      autocomplete="username"
      :aria-invalid="invalid ? 'true' : 'false'"
      aria-describedby="username-help"
    />
    <p id="username-help">
      {{ invalid ? 'Use at least 3 characters.' : 'Choose your public name.' }}
    </p>
  </div>
</template>
```

## Related

- [Textarea](./textarea.md)
- [Select](./select.md)
- [Switch](./switch.md)
- [Vue Islands](/guide/vue-islands)
