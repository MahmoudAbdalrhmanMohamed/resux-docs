# Transition

Resux includes a built-in resumable `<Transition>` component that coordinates CSS enter and leave animations when elements enter or leave the DOM conditionally (e.g. via `v-if` or `v-show`).

Resux's `<Transition>` uses standard Vue-compatible CSS transition classes and integrates with the resumable runtime to manage CSS transitions without requiring the full Vue runtime.

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'resux'

const isVisible = ref(true)
</script>

<template>
  <button type="button" @click="isVisible = !isVisible">
    Toggle Content
  </button>

  <Transition name="fade">
    <p v-if="isVisible" class="content-box">
      This element fades in and out smoothly.
    </p>
  </Transition>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
```

## Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `string` | `'v'` | Used to automatically generate transition CSS class names. For example, `name="fade"` generates `.fade-enter-active`, etc. |

Custom per-phase class overrides (Vue's `enterActiveClass` / `enterFromClass` / `enterToClass` / `leaveActiveClass` / `leaveFromClass` / `leaveToClass`) and the `appear` prop are not implemented; class names always derive from `name`.

## Transition lifecycle CSS classes

For `<Transition name="fade">`, Resux applies the following classes during state changes:

1. **Enter phase**:
   - `fade-enter-from`: Added before the element is inserted, removed one frame after insertion.
   - `fade-enter-active`: Applied throughout the entire entering phase; use this to configure CSS `transition` properties.
   - `fade-enter-to`: Added one frame after insertion (when `fade-enter-from` is removed); removed when the transition completes.
2. **Leave phase**:
   - `fade-leave-from`: Added immediately when a leave transition is triggered.
   - `fade-leave-active`: Applied throughout the entire leave phase; use this to configure CSS `transition` properties.
   - `fade-leave-to`: Added one frame after a leave transition is triggered; element is removed from the DOM when the transition completes.

## Accessibility: Reduced Motion

Resux's transition runtime automatically respects user motion preferences:

```css
@media (prefers-reduced-motion: reduce) {
  .fade-enter-active,
  .fade-leave-active {
    transition: none !important;
  }
}
```

When `(prefers-reduced-motion: reduce)` matches, DOM insertions and removals complete immediately without waiting for transition events, ensuring an accessible experience.
