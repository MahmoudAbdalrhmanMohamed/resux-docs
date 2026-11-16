# UI Icon Primitive (RxIcon & resuxjs/icons)

Covers both the lightweight `RxIcon` text placeholder primitive (`[name]`) in `resuxjs/ui` and the full `<Icon>` SVG/CSS-mask component in `resuxjs/icons` with compile-time static inlining.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxIcon` looks and behaves in real time:

<RxComponentPreview component="RxIcon" title="UI Icon Primitive (RxIcon & resuxjs/icons) — Live Visual Preview" />

## Import

```ts
import { RxIcon } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxIcon } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxIcon } from 'resuxjs/ui'
import { Icon } from 'resuxjs/icons'
</script>

<template>
  <div class="space-y-4">
    <!-- Full SVG & CSS-Mask Icon System (resuxjs/icons) -->
    <div class="flex items-center gap-4">
      <Icon name="lucide:check-circle" size="1.5rem" class="text-emerald-500" />
      <Icon name="lucide:sparkles" size="1.5rem" mode="css" class="text-indigo-500" />
      <Icon name="mail" size="1.5rem" />
      <Icon name="search" size="1.5rem" />
    </div>

    <!-- Lightweight UI Placeholder Primitive (resuxjs/ui) -->
    <div class="flex items-center gap-3 text-sm">
      <RxIcon name="check" size="1rem" color="#10b981" />
      <RxIcon name="warning" size="1rem" color="#f59e0b" />
      <RxIcon name="rocket" size="1rem" color="#6d5dfc" />
    </div>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxIcon` produces the following HTML structure (`span.rx-icon (resuxjs/ui) | svg.resux-icon / span.resux-icon--css (resuxjs/icons)`):

```html
<!-- resuxjs/icons (SVG Mode) -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1.5rem" height="1.5rem" class="inline-block shrink-0 align-middle text-emerald-500" aria-hidden="true">
  <path d="M20 6 9 17l-5-5" fill="none" stroke="currentColor" stroke-width="2"/>
</svg>

<!-- resuxjs/ui RxIcon Primitive -->
<span class="rx-icon" style="font-size: 1rem; color: #10b981;">[check]</span>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `'check'` | No | Icon identifier (`'check'` for `RxIcon`, or `'lucide:rocket'`, `'custom:logo'`, `'mail'` for `resuxjs/icons`). |
| `size` | `string \| number` | `'1.25rem'` | No | Font size (`RxIcon`) or SVG width/height (`Icon`).Numeric values append `px`. |
| `color` | `string` | `'currentColor'` | No | CSS color applied to `RxIcon`. |
| `mode` | `'svg' \| 'css'` | `'svg'` | No | (`resuxjs/icons` only) Renders full vector `<svg>` or a CSS `mask-image` `<span>`. |
| `unstyled` | `boolean` | `false` | No | (`RxIcon` only) Omits the `rx-icon` class. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxIcon unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxIcon
</RxIcon>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
