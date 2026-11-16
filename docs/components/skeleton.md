# Skeleton (RxSkeleton)

Animated shimmer placeholder block with configurable `width`, `height`, and `rounded` radius for async loading states.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxSkeleton` looks and behaves in real time:

<RxComponentPreview component="RxSkeleton" title="Skeleton (RxSkeleton) — Live Visual Preview" />

## Import

```ts
import { RxSkeleton } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxSkeleton } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxSkeleton, RxCard, RxAvatar, RxButton } from 'resuxjs/ui'

const loading = ref(true)
</script>

<template>
  <div class="space-y-3 max-w-md">
    <RxCard>
      <div v-if="loading" class="flex items-center gap-3">
        <RxSkeleton width="2.75rem" height="2.75rem" rounded="9999px" />
        <div class="flex-1 space-y-2">
          <RxSkeleton width="65%" height="0.9rem" />
          <RxSkeleton width="40%" height="0.75rem" />
        </div>
      </div>
      <div v-else class="flex items-center gap-3">
        <RxAvatar alt="Mahmoud Abdelrahman" status="online" />
        <div>
          <div class="font-semibold text-sm">Mahmoud Abdelrahman</div>
          <div class="text-xs opacity-70">Creator of Resux Framework</div>
        </div>
      </div>
    </RxCard>
    <RxButton size="sm" variant="secondary" @click="loading = !loading">
      {{ loading ? 'Simulate Data Loaded' : 'Show Skeleton State' }}
    </RxButton>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxSkeleton` produces the following HTML structure (`rx-skeleton`):

```html
<div
  class="rx-skeleton"
  style="width: 65%; height: 0.9rem; border-radius: 0.375rem;"
></div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `width` | `string` | `'100%'` | No | CSS width applied via inline style. |
| `height` | `string` | `'1rem'` | No | CSS height applied via inline style. |
| `rounded` | `string` | `'0.375rem'` | No | CSS `borderRadius` applied via inline style. |
| `unstyled` | `boolean` | `false` | No | Omits `rx-skeleton` shimmer class. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxSkeleton unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxSkeleton
</RxSkeleton>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
