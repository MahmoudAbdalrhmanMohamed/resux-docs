# Reveal

`RxReveal` is a mount-animation wrapper. Despite its name, the current implementation does **not** watch viewport visibility.

## Import

```ts
import { RxReveal } from 'resuxjs/ui'
// Equivalent alias: ResuxReveal
```

## Basic usage

```vue
<RxReveal preset="fade-up">
  <section>Animated once after Vue mounts</section>
</RxReveal>
```

## Actual behavior

On mount, the component calls `useAnimate()` on its root with the configured preset/duration. There is no `IntersectionObserver` in `RxReveal` itself.

For viewport-triggered behavior, `vAnime` / `vAnimate` are the package APIs that use `IntersectionObserver` where available.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `preset` | `string` | `'fade-up'` | No | Passed to `useAnimate()`. |
| `duration` | `number` | `400` | No | Duration in ms. |
| `unstyled` | `boolean` | `false` | No | Skips the mount animation. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Wrapped content. |

## Reduced motion

The component checks `isReducedMotion()` and skips animation when the browser requests reduced motion.

## SSR / resumability / hydration

The root/content can be SSR-rendered. The reveal animation starts only after Vue mount in a browser, so it is a client runtime enhancement and not resumable zero-JavaScript behavior.

## Related

- [Motion](./motion.md)
- [AutoAnimate](./auto-animate.md)
- [`vAnime` / `vAnimate`](/reference/ui#vanime-vanimate)
