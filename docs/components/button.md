# Button (RxButton)

Accessible action button primitive with semantic variants, three sizes, disabled state handling, and optional unstyled mode.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxButton` looks and behaves in real time:

<RxComponentPreview component="RxButton" title="Button (RxButton) — Live Visual Preview" />

## Import

```ts
import { RxButton } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxButton } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxButton, RxBadge } from 'resuxjs/ui'
import { Icon } from 'resuxjs/icons'

const saving = ref(false)
const deployCount = ref(3)

async function triggerDeploy() {
  if (saving.value) return
  saving.value = true
  await new Promise((r) => setTimeout(r, 600))
  deployCount.value += 1
  saving.value = false
}
</script>

<template>
  <div class="flex flex-wrap items-center gap-3">
    <RxButton variant="primary" size="md" :disabled="saving" @click="triggerDeploy">
      <Icon name="lucide:rocket" size="1rem" />
      <span>{{ saving ? 'Deploying...' : 'Deploy Production' }}</span>
      <RxBadge variant="default">{{ deployCount }}</RxBadge>
    </RxButton>

    <RxButton variant="secondary" size="md">Preview Branch</RxButton>
    <RxButton variant="outline" size="sm">View Logs</RxButton>
    <RxButton variant="ghost" size="sm">Cancel</RxButton>
    <RxButton variant="primary" disabled>Locked</RxButton>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxButton` produces the following HTML structure (`rx-btn rx-btn-${variant} rx-btn-${size}`):

```html
<button type="button" class="rx-btn rx-btn-primary rx-btn-md">
  Deploy Production
</button>
<button type="button" class="rx-btn rx-btn-secondary rx-btn-md">
  Preview Branch
</button>
<button type="button" class="rx-btn rx-btn-outline rx-btn-sm">
  View Logs
</button>
<button type="button" class="rx-btn rx-btn-ghost rx-btn-sm">
  Cancel
</button>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `'primary' \| 'secondary' \| 'outline' \| 'ghost'` | `'primary'` | No | Visual button style variant. |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | No | Controls padding, height, and font size. |
| `type` | `'button' \| 'submit' \| 'reset'` | `'button'` | No | Native HTML button type attribute. |
| `disabled` | `boolean` | `false` | No | Disables pointer interaction and applies muted styling. |
| `unstyled` | `boolean` | `false` | No | Strips default `rx-btn*` classes for custom Tailwind/CSS styling. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `click` | `MouseEvent` | Forwarded native click event when not disabled. |

## Slots

| Slot | Description |
| --- | --- |
| `default` | Button label, leading/trailing icons, or status badges. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxButton unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxButton
</RxButton>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
