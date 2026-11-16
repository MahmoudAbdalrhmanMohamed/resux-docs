# Switch (RxSwitch)

Accessible WAI-ARIA toggle switch (`role="switch"`) with `aria-checked`, `data-state="checked|unchecked"`, and animated thumb element.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxSwitch` looks and behaves in real time:

<RxComponentPreview component="RxSwitch" title="Switch (RxSwitch) — Live Visual Preview" />

## Import

```ts
import { RxSwitch } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxSwitch } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxSwitch, RxCard, RxBadge } from 'resuxjs/ui'

const viewTransitions = ref(true)
const preloadCss = ref(true)
const strictHalalGuard = ref(false)
</script>

<template>
  <RxCard class="space-y-4 max-w-md">
    <div class="flex items-center justify-between">
      <div>
        <div class="font-medium text-sm">Router View Transitions</div>
        <div class="text-xs opacity-70">Animate page swaps via document.startViewTransition</div>
      </div>
      <RxSwitch v-model="viewTransitions" />
    </div>

    <div class="flex items-center justify-between">
      <div>
        <div class="font-medium text-sm">Preload Route CSS</div>
        <div class="text-xs opacity-70">Warm destination stylesheets before DOM swap</div>
      </div>
      <RxSwitch v-model="preloadCss" />
    </div>

    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="font-medium text-sm">Strict Halal Production Guard</span>
        <RxBadge :variant="strictHalalGuard ? 'success' : 'default'">
          {{ strictHalalGuard ? 'Enforced' : 'Optional' }}
        </RxBadge>
      </div>
      <RxSwitch v-model="strictHalalGuard" />
    </div>
  </RxCard>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxSwitch` produces the following HTML structure (`rx-switch [checked] > span.rx-switch-thumb`):

```html
<button
  type="button"
  role="switch"
  aria-checked="true"
  data-state="checked"
  class="rx-switch checked"
>
  <span class="rx-switch-thumb" aria-hidden="true"></span>
</button>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `boolean` | `false` | No | Checked state bound via `v-model`. |
| `disabled` | `boolean` | `false` | No | Prevents toggling and dims the control. |
| `unstyled` | `boolean` | `false` | No | Omits `rx-switch` and `rx-switch-thumb` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `boolean` | Emitted with `!modelValue` when clicked. |

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxSwitch unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxSwitch
</RxSwitch>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
