# Textarea

`RxTextarea` renders a native `<textarea>` with Vue `v-model` support.

## Import

```ts
import { RxTextarea } from 'resuxjs/ui'
// Equivalent alias: ResuxTextarea
```

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxTextarea } from 'resuxjs/ui'

const bio = ref('')
</script>

<template>
  <RxTextarea v-model="bio" :rows="5" placeholder="About you" />
</template>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string` | `''` | No | Textarea value. |
| `rows` | `number` | `3` | No | Native `rows`. |
| `placeholder` | `string` | `''` | No | Native placeholder. |
| `disabled` | `boolean` | `false` | No | Native disabled state. |
| `unstyled` | `boolean` | `false` | No | Omits Resux-generated classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Emitted with `HTMLTextAreaElement.value` from the native input event. |

## Slots

No slots. The value is controlled through `modelValue`, not textarea child text.

## Native attributes

Attributes such as `name`, `required`, `maxlength`, `autocomplete`, `aria-describedby`, and event listeners are forwarded.

```vue
<RxTextarea
  v-model="message"
  name="message"
  required
  maxlength="1000"
  aria-describedby="message-help"
/>
```

## Styling

The root receives both `rx-input` and `rx-textarea` unless `unstyled` is true. The current built-in stylesheet defines the shared `rx-input` rules; use your own CSS for textarea-specific behavior such as resize policy or minimum height.

## Accessibility

Native textarea keyboard and screen-reader semantics are preserved. Provide a visible/programmatic label and expose validation messages explicitly. Placeholder text is not a replacement for a label.

## SSR / resumability / hydration

The server can render the textarea through Vue SSR, while `v-model` synchronization requires the Vue runtime boundary. For a plain HTML form that does not need reactive Vue state, a native Resux template `<textarea>` is cheaper.

## Complete example

```vue
<script setup lang="ts">
import { computed, ref } from 'vue'
import { RxTextarea } from 'resuxjs/ui'

const feedback = ref('')
const remaining = computed(() => 500 - feedback.value.length)
</script>

<template>
  <label for="feedback">Feedback</label>
  <RxTextarea
    id="feedback"
    v-model="feedback"
    :rows="6"
    maxlength="500"
    aria-describedby="feedback-count"
  />
  <p id="feedback-count">{{ remaining }} characters remaining</p>
</template>
```

## Related

- [Input](./input.md)
- [Vue Islands](/guide/vue-islands)
