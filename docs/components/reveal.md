# Reveal

`RxReveal` is a **Vue mount-animation wrapper**. It runs a selected Resux UI animation preset on its root after the component mounts.

::: warning “Reveal” does not currently mean viewport reveal
The current `RxReveal` implementation does **not** use `IntersectionObserver` and does not wait for the element to enter the viewport. It animates on Vue mount. For the current viewport-observed UI-package behavior, use `vAnime` / `vAnimate`.
:::

## When to use it

Use `RxReveal` when:

- the content is already inside a Vue island/UI subtree,
- you want a one-time entrance animation when that subtree mounts,
- you want to choose one of the UI package's animation presets,
- you want reduced-motion preference to suppress the effect.

Do not choose it because you need “animate when scrolled into view.” The current trigger is mount, not intersection.

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

The component renders a root `<div>` around the default slot.

## Actual lifecycle

Conceptually:

```text
server / render creates wrapper + slot content
        ↓
Vue mounts RxReveal in the browser
        ↓
component checks `unstyled`
        ↓
component checks reduced-motion preference
        ↓
`useAnimate(root, { preset, duration })`
        ↓
Web Animations API runs once
```

There is no viewport observer in `RxReveal` itself.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `preset` | `string` | `'fade-up'` | No | Animation preset name passed to `useAnimate()`. |
| `duration` | `number` | `400` | No | Animation duration in milliseconds. |
| `unstyled` | `boolean` | `false` | No | Skips the built-in mount animation. |

The preset prop is implemented as a string. Use documented built-in preset names when you want verified framework behavior.

## Built-in preset choices

The UI source currently defines presets including:

- `fade-up`,
- `fade-down`,
- `scale-in`,
- `slide-in-left`,
- `slide-in-right`,
- `pulse-glow`,
- `bounce-in`.

Example:

```vue
<RxReveal preset="slide-in-left" :duration="500">
  <aside>Filters</aside>
</RxReveal>
```

If you need full imperative control or need to know the returned `Animation`, use [`useAnimate()`](/reference/ui#useanimate-element-options) directly.

## Events

No custom events are declared. `RxReveal` does not currently emit animation-start or animation-end events.

Use the lower-level animation helper if application logic needs direct animation lifecycle control.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Content rendered inside the reveal wrapper. |

Changing slot content after mount does not automatically replay the reveal animation.

## Reduced motion

Before animating, the component checks `isReducedMotion()`, which reads the browser preference:

```css
(prefers-reduced-motion: reduce)
```

When the user requests reduced motion, the component skips its mount animation.

Your own CSS/transitions and other third-party animations remain your responsibility; `RxReveal` cannot suppress unrelated motion outside its implementation.

## SSR behavior

The wrapper and content can be server-rendered. The Web Animation only starts in the browser after Vue mount.

That means important content should not depend on the animation in order to exist:

```text
server HTML: content is present
browser: Vue mounts
browser: optional visual entrance animation runs
```

This is a progressive visual enhancement inside a Vue-owned boundary, not server-only behavior.

## Resumability / hydration boundary

`RxReveal` comes from the Vue-based `resuxjs/ui` package. Its `onMounted` animation behavior requires the Vue runtime boundary that owns the component.

It is **not** the normal Resux resumable interaction model. If a normal Resux page needs a small browser animation and does not otherwise need Vue, consider a client enhancement or application CSS/WAAPI behavior rather than introducing a Vue island solely for `RxReveal`.

Read [Component Anatomy](./component-anatomy.md) and [Architecture Deep Dive](/guide/architecture-deep-dive).

## `RxReveal` vs `RxMotion`

The current implementations are similar because both animate on mount and accept a preset/duration.

Use the docs and source rather than assuming the names imply different triggers.

| Feature | `RxMotion` | `RxReveal` |
| --- | --- | --- |
| Vue component | Yes | Yes |
| Trigger | Mount | Mount |
| Preset prop | Yes | Yes |
| Duration prop | Yes | Yes |
| Reduced-motion check | Yes | Yes |
| Viewport observation inside component | No | No |

The separate names can still be useful for design intent/readability, but they do not currently create a viewport-vs-mount distinction.

## `RxReveal` vs `vAnime` / `vAnimate`

Use the directive path when viewport intersection is what you actually mean by reveal.

Conceptually:

```text
vAnime/vAnimate
  ↓
mounted element is observed
  ↓
IntersectionObserver reports intersection
  ↓
animation runs
  ↓
element is unobserved / observer cleaned up
```

That behavior is documented in the [UI package API](/reference/ui#vanime-vanimate).

## `RxReveal` vs CSS animation

If the animation is a simple styling concern and does not need Vue state/lifecycle, CSS may be enough:

```css
@media (prefers-reduced-motion: no-preference) {
  .intro {
    animation: intro-fade 300ms ease both;
  }
}
```

Choose `RxReveal` when you are already in the Vue UI system and want the shared UI animation presets/helper behavior.

## Recipe: reveal a dashboard section

```vue
<RxReveal preset="fade-up" :duration="320">
  <RxCard>
    <h2>Runtime metrics</h2>
    <p>Interactive runtime loaded only where required.</p>
  </RxCard>
</RxReveal>
```

The card content is present in rendered markup; the visual effect runs after the Vue boundary mounts.

## Recipe: stagger several regions

`RxReveal` itself does not expose a delay/stagger prop in the current component API. If you need a coordinated timeline, use lower-level `useAnimate()` calls, CSS, or an appropriate animation package rather than inventing unsupported props.

## Common mistakes

### Expecting scroll/viewport reveal

`RxReveal` does not currently observe viewport visibility.

### Expecting the animation to replay on slot updates

The trigger is the component mount hook, not arbitrary child updates.

### Expecting custom animation events

No custom animation lifecycle events are emitted by the component.

### Ignoring the Vue boundary

The mount hook requires Vue runtime ownership. Normal Resux markup does not automatically execute this component outside an island/runtime boundary.

### Assuming `unstyled` only removes classes

For this motion component, `unstyled` skips the animation behavior.

## Related

- [Motion](./motion.md)
- [AutoAnimate](./auto-animate.md)
- [Component Anatomy](./component-anatomy.md)
- [`useAnimate()`](/reference/ui#useanimate-element-options)
- [`vAnime` / `vAnimate`](/reference/ui#vanime-vanimate)
- [Vue Islands](/guide/vue-islands)
