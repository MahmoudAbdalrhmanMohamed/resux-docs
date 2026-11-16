# Badge (RxBadge)

Compact inline status pill for version tags, build states, and metric indicators.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxBadge` looks and behaves in real time:

<RxComponentPreview component="RxBadge" title="Badge (RxBadge) — Live Visual Preview" />

## Import

```ts
import { RxBadge } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxBadge } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxBadge } from 'resuxjs/ui'
</script>

<template>
  <div class="flex flex-wrap items-center gap-2">
    <RxBadge variant="default">v0.4.0-beta.7</RxBadge>
    <RxBadge variant="primary">Resumable SSR</RxBadge>
    <RxBadge variant="success">Quality Gate Passed</RxBadge>
    <RxBadge variant="warning">Pre-release Beta</RxBadge>
    <RxBadge variant="error">Breaking Change</RxBadge>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxBadge` produces the following HTML structure (`rx-badge rx-badge-${variant}`):

```html
<span class="rx-badge rx-badge-default">v0.4.0-beta.7</span>
<span class="rx-badge rx-badge-primary">Resumable SSR</span>
<span class="rx-badge rx-badge-success">Quality Gate Passed</span>
<span class="rx-badge rx-badge-warning">Pre-release Beta</span>
<span class="rx-badge rx-badge-error">Breaking Change</span>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `'default' \| 'primary' \| 'success' \| 'warning' \| 'error'` | `'default'` | No | Semantic color tone applied via `rx-badge-${variant}`. |
| `unstyled` | `boolean` | `false` | No | Removes `rx-badge*` classes. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Badge text or icon content. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxBadge unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxBadge
</RxBadge>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
