# AutoAnimate

`RxAutoAnimate` currently runs a one-time `scale-in` animation on its root after mount.

::: warning Name vs current behavior
The current implementation does **not** observe child-list mutations, layout changes, reordering, insertion, or removal. It is not an automatic layout-animation engine despite the `AutoAnimate` name.
:::

## Import

```ts
import { RxAutoAnimate } from 'resuxjs/ui'
// Equivalent alias: ResuxAutoAnimate
```

## Basic usage

```vue
<RxAutoAnimate :duration="300">
  <div>Animated once when the wrapper mounts</div>
</RxAutoAnimate>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `duration` | `number` | `300` | No | Duration of the mount-time `scale-in` animation. |
| `unstyled` | `boolean` | `false` | No | Skips the animation. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Wrapper content. |

## Reduced motion

The component checks `isReducedMotion()` before running the Web Animation.

## SSR / resumability / hydration

SSR renders the wrapper/content. The one-time animation needs Vue mount and browser JavaScript. Changes to slot children after mount do not trigger an animation from this component.

## Need real automatic layout animation?

Use a third-party library through the [package integration](/guide/package-integration) model and choose the correct client/progressive/Vue-island boundary. Do not assume `RxAutoAnimate` supplies mutation-aware layout animation today.

## Related

- [Motion](./motion.md)
- [Reveal](./reveal.md)
- [Package Integration](/guide/package-integration)
