# Card (RxCard)

Surface container primitive for grouping metrics, forms, and settings panels with optional visual variants (`default`, `elevated`, `outlined`, `subtle`).

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxCard` looks and behaves in real time:

<RxComponentPreview component="RxCard" title="Card (RxCard) — Live Visual Preview" />

## Import

```ts
import { RxCard } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxCard } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxCard, RxBadge, RxButton } from 'resuxjs/ui'
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <RxCard variant="default">
      <div class="flex items-center justify-between mb-2">
        <span class="font-semibold">SSR Bundle Budget</span>
        <RxBadge variant="success">Passed</RxBadge>
      </div>
      <p class="text-2xl font-bold">4.8 KB <span class="text-xs font-normal opacity-70">gzipped</span></p>
      <p class="text-xs opacity-75 mt-1">Zero hydration overhead on static routes.</p>
    </RxCard>

    <RxCard variant="elevated">
      <div class="flex items-center justify-between mb-2">
        <span class="font-semibold">Fontaine Metrics</span>
        <RxBadge variant="primary">v1.0.3</RxBadge>
      </div>
      <p class="text-sm opacity-80 mb-3">Metric-adjusted fallback @font-face rules generated at build time.</p>
      <RxButton size="sm" variant="outline">Inspect CSS</RxButton>
    </RxCard>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxCard` produces the following HTML structure (`rx-card [rx-card-${variant}]`):

```html
<div class="rx-card">
  <div class="flex items-center justify-between mb-2">
    <span class="font-semibold">SSR Bundle Budget</span>
    <span class="rx-badge rx-badge-success">Passed</span>
  </div>
  <p class="text-2xl font-bold">4.8 KB</p>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `string` | `'default'` | No | Appends `rx-card-${variant}` when not `'default'` (e.g., `'elevated'`, `'outlined'`, `'subtle'`). |
| `unstyled` | `boolean` | `false` | No | Renders a plain `<div>` without `rx-card` classes. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Card header, body, metrics, and footer actions. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxCard unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxCard
</RxCard>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
