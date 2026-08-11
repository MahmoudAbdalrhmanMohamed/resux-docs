# Motion

`RxMotion` wraps slot content in a configurable element and calls `useAnimate()` on that root after the Vue component mounts.

## Import

```ts
import { RxMotion } from 'resuxjs/ui'
// Equivalent alias: ResuxMotion
```

## Basic usage

```vue
<RxMotion preset="fade-up">
  <section>Animated after mount</section>
</RxMotion>
```

## Presets

`useAnimate()` recognizes:

- `fade-up`
- `fade-down`
- `scale-in`
- `slide-in-left`
- `slide-in-right`
- `pulse-glow`
- `bounce-in`

Unknown preset names fall back to the generic fade/up keyframes used by the helper's default branch.

## Timing

```vue
<RxMotion preset="scale-in" :duration="600" :delay="120" />
```

## Custom root element

```vue
<RxMotion tag="article" preset="fade-up">
  ...
</RxMotion>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `tag` | `string` | `'div'` | No | Root HTML tag passed to Vue `h()`. |
| `preset` | `string` | `'fade-up'` | No | Animation preset name. |
| `duration` | `number` | `400` | No | Duration in ms. |
| `delay` | `number` | `0` | No | Delay in ms. |
| `easing` | `string` | `'cubic-bezier(0.16, 1, 0.3, 1)'` | No | Web Animations easing. |
| `unstyled` | `boolean` | `false` | No | Skips the mount animation. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Root contents. |

## Reduced motion

Before starting, `RxMotion` checks `isReducedMotion()`. When `matchMedia('(prefers-reduced-motion: reduce)')` matches, it does not animate.

`isReducedMotion()` returns false in server/non-browser contexts.

## SSR / resumability / hydration

SSR outputs the wrapper/content without running browser animation. The animation is a Vue `onMounted` effect and therefore requires the Vue runtime boundary and the browser Web Animations API. Content remains present even when animation cannot run.

## When to use

Use `RxMotion` when a Vue island already owns the subtree. For resumable/non-Vue Resux markup, prefer the framework's normal CSS/progressive-enhancement techniques rather than adding a Vue island only for entrance animation.

## Related

- [Reveal](./reveal.md)
- [AutoAnimate](./auto-animate.md)
- [UI and Motion](/guide/ui-animations)
- [UI package reference](/reference/ui)
