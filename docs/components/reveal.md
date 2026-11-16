# Reveal (RxReveal)

Scroll-triggered viewport entrance wrapper powered by `IntersectionObserver` (`threshold: 0.1`) that hides content (`opacity: 0`) until scrolled into view and then plays the configured preset.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxReveal` looks and behaves in real time:

<RxComponentPreview component="RxReveal" title="Reveal (RxReveal) — Live Visual Preview" />

## Import

```ts
import { RxReveal } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxReveal } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxReveal, RxCard, RxBadge } from 'resuxjs/ui'
</script>

<template>
  <div class="space-y-3">
    <RxReveal preset="fade-up" :duration="500">
      <RxCard class="flex items-center justify-between">
        <span class="text-sm font-medium">1. Server renders static HTML</span>
        <RxBadge variant="success">0ms Blocking</RxBadge>
      </RxCard>
    </RxReveal>
    <RxReveal preset="fade-up" :duration="650">
      <RxCard class="flex items-center justify-between">
        <span class="text-sm font-medium">2. IntersectionObserver triggers RxReveal</span>
        <RxBadge variant="primary">Threshold 0.1</RxBadge>
      </RxCard>
    </RxReveal>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxReveal` produces the following HTML structure (`<div> (IntersectionObserver + useAnimate)`):

```html
<div>
  <div class="rx-card">1. Server renders static HTML</div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `preset` | `AnimationPreset` | `'fade-up'` | No | Animation preset triggered when the element intersects the viewport. |
| `duration` | `number` | `400` | No | Animation duration in milliseconds. |
| `unstyled` | `boolean` | `false` | No | Consistency prop. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Content revealed when scrolled into the viewport. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxReveal unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxReveal
</RxReveal>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
