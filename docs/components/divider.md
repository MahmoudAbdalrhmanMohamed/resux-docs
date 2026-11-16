# Divider (RxDivider)

Horizontal or vertical visual separator line with optional centered text label.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxDivider` looks and behaves in real time:

<RxComponentPreview component="RxDivider" title="Divider (RxDivider) — Live Visual Preview" />

## Import

```ts
import { RxDivider } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxDivider } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxDivider, RxButton } from 'resuxjs/ui'
</script>

<template>
  <div class="space-y-4 max-w-md">
    <RxButton variant="primary" class="w-full">Continue with GitHub</RxButton>
    <RxDivider label="OR DEPLOY VIA CLI" />
    <code class="block text-xs p-2.5 rounded bg-black/10">npx create-resuxjs@latest my-app</code>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxDivider` produces the following HTML structure (`rx-divider rx-divider-${orientation} > [span.rx-divider-label]`):

```html
<div class="rx-divider rx-divider-horizontal">
  <span class="rx-divider-label">OR DEPLOY VIA CLI</span>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `label` | `string` | `''` | No | Optional inline label rendered inside `.rx-divider-label`. |
| `orientation` | `'horizontal' \| 'vertical'` | `'horizontal'` | No | Separator axis (`rx-divider-horizontal` or `rx-divider-vertical`). |
| `unstyled` | `boolean` | `false` | No | Removes `rx-divider*` classes. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxDivider unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxDivider
</RxDivider>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
