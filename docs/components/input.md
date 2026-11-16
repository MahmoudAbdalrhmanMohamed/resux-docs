# Input (RxInput)

Two-way bound single-line input control (`v-model`) supporting text, email, password, number, search, and url types with `inheritAttrs: false`.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxInput` looks and behaves in real time:

<RxComponentPreview component="RxInput" title="Input (RxInput) — Live Visual Preview" />

## Import

```ts
import { RxInput } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxInput } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref, computed } from 'resuxjs'
import { RxInput, RxButton, RxBadge } from 'resuxjs/ui'

const email = ref('mahmoud@resux.dev')
const projectSlug = ref('resux-cloud-app')
const isValidEmail = computed(() => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value))
</script>

<template>
  <div class="space-y-4 max-w-md">
    <div class="space-y-1.5">
      <label class="text-sm font-medium flex items-center justify-between">
        <span>Developer Email</span>
        <RxBadge :variant="isValidEmail ? 'success' : 'warning'">
          {{ isValidEmail ? 'Valid' : 'Check format' }}
        </RxBadge>
      </label>
      <RxInput
        v-model="email"
        type="email"
        placeholder="you@example.com"
        autocomplete="email"
      />
    </div>

    <div class="space-y-1.5">
      <label class="text-sm font-medium">Project Slug</label>
      <RxInput
        v-model="projectSlug"
        placeholder="my-resux-app"
      />
      <p class="text-xs opacity-75">Preview URL: https://{{ projectSlug || 'app' }}.resux.dev</p>
    </div>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxInput` produces the following HTML structure (`rx-input`):

```html
<input
  type="email"
  value="mahmoud@resux.dev"
  placeholder="you@example.com"
  class="rx-input"
/>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string \| number` | `''` | No | Bound input value (`v-model`). |
| `type` | `string` | `'text'` | No | Native HTML input type (`text`, `email`, `password`, `number`, `search`). |
| `placeholder` | `string` | `''` | No | Placeholder hint shown when empty. |
| `disabled` | `boolean` | `false` | No | Disables editing and form submission. |
| `unstyled` | `boolean` | `false` | No | Removes `rx-input` class so custom utility classes control appearance. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Emitted on every `input` event with the current target value. |

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxInput unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxInput
</RxInput>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
