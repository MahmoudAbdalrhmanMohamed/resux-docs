# Textarea (RxTextarea)

Multi-line text input primitive with configurable row height, `v-model` binding, and shared `rx-input rx-textarea` styling.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxTextarea` looks and behaves in real time:

<RxComponentPreview component="RxTextarea" title="Textarea (RxTextarea) — Live Visual Preview" />

## Import

```ts
import { RxTextarea } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxTextarea } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref, computed } from 'resuxjs'
import { RxTextarea, RxBadge, RxButton } from 'resuxjs/ui'

const releaseNotes = ref('Feat: Added native browser View Transitions API, Fontless 1.3.4 zero-CLS metrics, and compile-time SVG icon inlining.')
const charCount = computed(() => releaseNotes.value.length)
</script>

<template>
  <div class="space-y-2 max-w-lg">
    <div class="flex items-center justify-between">
      <label class="text-sm font-medium">Release Changelog Summary</label>
      <RxBadge :variant="charCount > 280 ? 'warning' : 'default'">
        {{ charCount }} / 280 chars
      </RxBadge>
    </div>
    <RxTextarea
      v-model="releaseNotes"
      :rows="4"
      placeholder="Describe what changed in this release..."
    />
    <div class="flex justify-end gap-2">
      <RxButton variant="ghost" size="sm" @click="releaseNotes = ''">Clear</RxButton>
      <RxButton variant="primary" size="sm">Save Changelog</RxButton>
    </div>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxTextarea` produces the following HTML structure (`rx-input rx-textarea`):

```html
<textarea
  rows="4"
  placeholder="Describe what changed in this release..."
  class="rx-input rx-textarea"
>Feat: Added native browser View Transitions API...</textarea>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string` | `''` | No | Bound multi-line string value (`v-model`). |
| `rows` | `number` | `3` | No | Visible text row count. |
| `placeholder` | `string` | `''` | No | Placeholder text when empty. |
| `disabled` | `boolean` | `false` | No | Disables user input. |
| `unstyled` | `boolean` | `false` | No | Omits `rx-input rx-textarea` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Emitted on `input` with the updated textarea string. |

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxTextarea unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxTextarea
</RxTextarea>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
