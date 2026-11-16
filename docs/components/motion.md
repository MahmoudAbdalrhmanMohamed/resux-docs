# Motion (RxMotion)

Web Animations API wrapper component that animates its root tag on mount using `useAnimate` presets (`fade-in`, `fade-up`, `fade-down`, `slide-left`, `slide-right`, `zoom-in`, `zoom-out`) while respecting `prefers-reduced-motion`.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxMotion` looks and behaves in real time:

<RxComponentPreview component="RxMotion" title="Motion (RxMotion) — Live Visual Preview" />

## Import

```ts
import { RxMotion } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxMotion } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxMotion, RxCard, RxButton } from 'resuxjs/ui'

const preset = ref<'fade-up' | 'zoom-in' | 'slide-left'>('fade-up')
const runKey = ref(1)

function replay(nextPreset: 'fade-up' | 'zoom-in' | 'slide-left') {
  preset.value = nextPreset
  runKey.value += 1
}
</script>

<template>
  <div class="space-y-3">
    <div class="flex gap-2">
      <RxButton size="sm" variant="outline" @click="replay('fade-up')">Fade Up</RxButton>
      <RxButton size="sm" variant="outline" @click="replay('zoom-in')">Zoom In</RxButton>
      <RxButton size="sm" variant="outline" @click="replay('slide-left')">Slide Left</RxButton>
    </div>

    <RxMotion :key="runKey" :preset="preset" :duration="450">
      <RxCard>
        <div class="font-semibold text-sm">Animated with RxMotion ({{ preset }})</div>
        <div class="text-xs opacity-75">Uses native Web Animations API with automatic reduced-motion fallback.</div>
      </RxCard>
    </RxMotion>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxMotion` produces the following HTML structure (`<tag> (animated via Web Animations API)`):

```html
<div style="opacity: 1; transform: translateY(0px);">
  <div class="rx-card">Animated with RxMotion (fade-up)</div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `tag` | `string` | `'div'` | No | HTML tag name rendered as the animated container. |
| `preset` | `AnimationPreset` | `'fade-up'` | No | Preset keyframe animation (`fade-in`, `fade-up`, `fade-down`, `slide-left`, `slide-right`, `zoom-in`, `zoom-out`). |
| `duration` | `number` | `400` | No | Animation duration in milliseconds. |
| `delay` | `number` | `0` | No | Start delay in milliseconds. |
| `easing` | `string` | `'cubic-bezier(0.16, 1, 0.3, 1)'` | No | CSS timing function passed to `Element.animate()`. |
| `unstyled` | `boolean` | `false` | No | Reserved for consistency across `resuxjs/ui`. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Content inside the animated element. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxMotion unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxMotion
</RxMotion>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
