# UI and Motion (`resuxjs/ui`)

`resuxjs/ui` is Resux's optional Vue UI/motion package. Use this guide for the runtime model and animation APIs; use the [Component catalog](/components/) for per-component contracts.

::: warning Vue runtime package
The package's components and directives are Vue-owned. Put them inside a [Vue island](./vue-islands.md) or another explicit Vue runtime boundary. Normal Resux components remain resumable and do not become Vue-hydrated just because the optional package exists.
:::

## Module setup

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/ui', {
      css: ['/assets/css/ui-overrides.css'],
      defaultStyles: true,
      tokens: { accent: '#03c8bf' },
      animations: {
        enabled: true,
        defaultPreset: 'fade-up'
      }
    }]
  ]
})
```

`tokens` are public configuration metadata/typed values. The current primitive CSS does not automatically map every token key to CSS variables.

## Imperative animation

```vue
<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useAnimate } from 'resuxjs/ui'

const element = ref<HTMLElement | null>(null)
let animation: Animation | null = null

onMounted(() => {
  animation = useAnimate(element.value, {
    type: 'fade-up',
    duration: 400,
    delay: 100,
    fill: 'forwards'
  })
})

onBeforeUnmount(() => animation?.cancel())
</script>

<template>
  <div ref="element">Animated content</div>
</template>
```

`useAnimate()` returns `null` when animation cannot/should not run, including reduced-motion requests.

## Viewport-triggered directive

`vAnime` and `vAnimate` are aliases. This is the package API that uses `IntersectionObserver` where available:

```vue
<div v-anime="{ type: 'fade-up', duration: 500 }">Content</div>
```

It is a Vue directive, not a native Resux template directive.

## Motion components

- [`RxMotion`](/components/motion) runs its configured animation after mount.
- [`RxReveal`](/components/reveal) also runs after mount. **It is not viewport-observed in the current implementation.**
- [`RxAutoAnimate`](/components/auto-animate) runs a one-time `scale-in` after mount. **It does not observe child/layout changes in the current implementation.**

These names should not be used to promise behavior the source does not implement.

## Reduced motion

`isReducedMotion()` checks `prefers-reduced-motion: reduce` in browsers. `useAnimate`, `RxMotion`, `RxReveal`, and `RxAutoAnimate` skip their Web Animations path when reduced motion is requested.

The default CSS skeleton shimmer is separate CSS animation and currently needs an application-level reduced-motion override; see [Skeleton](/components/skeleton).

## Component catalog

The package currently exports 23 `Rx*` components plus matching `Resux*` aliases. Browse the [component catalog](/components/) for forms, feedback, overlays, navigation, motion, and accessibility/runtime notes.

## When to choose a Vue UI component

Use the optional Vue package when the widget naturally needs Vue-owned local state/composition or you are integrating a Vue component tree. Prefer normal Resux HTML/templates when native/resumable behavior is enough.

That keeps Vue an explicit boundary rather than turning the whole framework into Vue hydration.

## Related

- [Component catalog](/components/)
- [UI package API](/reference/ui)
- [Vue Islands](./vue-islands.md)
- [Execution Contexts](./execution-contexts.md)
