# Alert (RxAlert)

Accessible status callout banner (`role="alert"`) with semantic variants (`info`, `success`, `warning`, `error`), optional title, and dismiss button.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxAlert` looks and behaves in real time:

<RxComponentPreview component="RxAlert" title="Alert (RxAlert) — Live Visual Preview" />

## Import

```ts
import { RxAlert } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxAlert } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxAlert, RxButton } from 'resuxjs/ui'

const showNotice = ref(true)
</script>

<template>
  <div class="space-y-3">
    <RxAlert
      v-if="showNotice"
      variant="info"
      title="View Transitions API Enabled"
      dismissible
      @dismiss="showNotice = false"
    >
      Route changes now use <code>document.startViewTransition</code> with automatic CSS preloading.
    </RxAlert>

    <RxAlert variant="success" title="Build Verification Complete">
      All 31 public export specifiers in <code>resuxjs@0.4.0-beta.7</code> passed parity checks.
    </RxAlert>

    <RxButton v-if="!showNotice" size="sm" variant="outline" @click="showNotice = true">
      Restore Info Alert
    </RxButton>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxAlert` produces the following HTML structure (`rx-alert rx-alert-${variant} > [.rx-alert-title] + .rx-alert-content + [button.rx-alert-close]`):

```html
<div class="rx-alert rx-alert-info" role="alert">
  <div class="rx-alert-title">View Transitions API Enabled</div>
  <div class="rx-alert-content">
    Route changes now use document.startViewTransition with automatic CSS preloading.
  </div>
  <button class="rx-alert-close">×</button>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `'info' \| 'success' \| 'warning' \| 'error'` | `'info'` | No | Visual tone and border/background accent. |
| `title` | `string` | `''` | No | Optional bold heading rendered inside `.rx-alert-title`. |
| `dismissible` | `boolean` | `false` | No | Renders a close button (`×`) that emits `dismiss` when clicked. |
| `unstyled` | `boolean` | `false` | No | Removes `rx-alert*` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `dismiss` | `void` | Emitted when the close button is clicked. |

## Slots

| Slot | Description |
| --- | --- |
| `default` | Alert body description or inline action links. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxAlert unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxAlert
</RxAlert>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
