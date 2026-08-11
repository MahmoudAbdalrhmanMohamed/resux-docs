# AutoAnimate

`RxAutoAnimate` is a **Vue mount-animation wrapper**. The current implementation runs a one-time `scale-in` Web Animation on its root after mount.

::: warning Name vs current behavior
The current component does **not** watch child-list mutations, item reordering, insertion/removal, or layout changes. It is not a mutation-aware automatic layout-animation engine despite the `AutoAnimate` name.
:::

Understanding that boundary is important because “auto animate” is a name commonly associated with libraries that continuously observe DOM/layout changes. `RxAutoAnimate` currently does something much smaller and more predictable.

## When to use it

Use it when:

- you are already inside a Vue island/UI subtree,
- a wrapper should animate once when that Vue component mounts,
- the built-in `scale-in` effect and duration are sufficient,
- reduced-motion behavior should suppress the effect.

Do not use it when you need:

- list insertion/removal animation,
- FLIP/layout transition calculation,
- drag-and-drop reorder animation,
- repeated animation whenever children change,
- viewport-triggered reveal,
- normal Resux zero-Vue animation behavior.

For those cases, choose a different motion API or third-party enhancement boundary.

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

The wrapper renders its slot content inside a root `<div>`. After Vue mounts the component, the current implementation calls the UI animation helper with the `scale-in` preset.

## What happens step by step

Conceptually:

```text
SSR / initial render
  ↓
<div> with slot content exists
  ↓
Vue mounts the component in the island
  ↓
component checks `unstyled`
  ↓
component checks reduced-motion preference
  ↓
`useAnimate(root, { preset: 'scale-in', duration })`
  ↓
Web Animations API runs once
```

There is no ongoing MutationObserver/ResizeObserver/child-list watcher in `RxAutoAnimate` itself.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `duration` | `number` | `300` | No | Duration in milliseconds for the mount-time `scale-in` animation. |
| `unstyled` | `boolean` | `false` | No | Skips the built-in mount animation. |

`unstyled` is worth noticing here: unlike a purely visual component where it only removes classes, this motion primitive uses it as a **behavior gate**. Setting it to true disables the animation.

## Events

No custom events are declared. The current component does not emit animation-start/animation-end events.

If application logic needs to coordinate with a Web Animation object directly, use the lower-level [UI animation API](/reference/ui#useanimate-element-options) rather than assuming `RxAutoAnimate` exposes the animation instance.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Content rendered inside the wrapper. |

Children can still change because normal Vue rendering changes them, but **those later changes do not cause this component to run a new automatic layout animation**.

## Reduced motion

The component checks `isReducedMotion()` before running the mount animation. The helper uses the browser media query:

```css
(prefers-reduced-motion: reduce)
```

When reduced motion is requested, the component skips its animation rather than forcing the visual effect.

That behavior improves accessibility, but your surrounding Vue/application animation code must still respect reduced motion if it adds other effects.

## SSR behavior

The wrapper/content can be server-rendered. The animation itself cannot run during SSR because the Web Animations API is a browser feature.

So the lifecycle is:

```text
server: render wrapper + content
browser before Vue mount: content is already visible/present
browser after Vue mount: optional one-time scale animation
```

Do not hide critical content waiting for the animation unless your own CSS/application deliberately does so.

## Resumability / hydration boundary

`RxAutoAnimate` belongs to `resuxjs/ui`, which is a Vue package. Its `onMounted` behavior requires the Vue runtime boundary that owns it.

It is **not** a normal Resux resumable template primitive. If a normal Resux page only needs a small progressive animation, consider whether a client enhancement is more appropriate than introducing a Vue island.

Read [Component Anatomy](./component-anatomy.md) and [Package Integration](/guide/package-integration).

## Difference from `RxMotion`

Both are mount-time animation wrappers.

- `RxMotion` lets you choose a preset and duration.
- `RxAutoAnimate` currently fixes the preset to `scale-in` and exposes only duration/disable behavior.

If you need `fade-up`, `slide-in-left`, or another built-in preset, use [Motion](./motion.md).

## Difference from `RxReveal`

`RxReveal` also animates once after mount and allows a preset. Despite its name, it is not itself viewport-observed.

Therefore current behavior overlaps more than the names suggest:

| Component | Trigger | Preset control | Ongoing child/layout observation |
| --- | --- | --- | --- |
| `RxMotion` | Vue mount | Yes | No |
| `RxReveal` | Vue mount | Yes | No |
| `RxAutoAnimate` | Vue mount | Fixed `scale-in` | No |

## Difference from `vAnime` / `vAnimate`

`vAnime` / `vAnimate` are Vue directive APIs that use `IntersectionObserver` where available. They are the current UI-package option when the desired trigger is viewport intersection rather than mount.

That is still Vue/browser behavior, but the trigger is different.

## Need real automatic layout animation?

For mutation-aware animation, use a package designed for that job and put it behind the correct runtime boundary.

A progressive pattern can look conceptually like:

```text
server renders useful list HTML
  ↓
client enhancement / Vue island activates when appropriate
  ↓
third-party animation library owns layout animation for that region
  ↓
cleanup destroys observers/listeners on route disposal
```

See [Third-party Packages](/guide/package-integration) and [Integration Cookbook](/guide/integration-cookbook).

## Recipe: mount a dashboard panel

```vue
<RxAutoAnimate :duration="220">
  <RxCard>
    <h2>Deployment status</h2>
    <RxBadge variant="success">Ready</RxBadge>
  </RxCard>
</RxAutoAnimate>
```

This animates the wrapper once when the Vue subtree mounts. Changing `Ready` to another badge later does not make `RxAutoAnimate` automatically animate the layout change.

## Recipe: disable animation conditionally

```vue
<RxAutoAnimate :unstyled="disableMotion" :duration="250">
  <section>...</section>
</RxAutoAnimate>
```

The component also checks the user's OS/browser reduced-motion preference independently.

## Common mistakes

### Expecting new list items to animate automatically

They will not. The current component does not observe list mutations/layout changes.

### Expecting viewport reveal

Mount is the trigger. Use the documented directive path for IntersectionObserver-based Vue behavior.

### Expecting repeated animation

The mount hook runs once for that component instance. A new mount can animate again; ordinary slot updates do not.

### Using it outside a Vue boundary

It is a Vue component and needs the Vue runtime owner that renders/mounts it.

### Assuming `unstyled` only changes CSS

For this component it skips the animation behavior.

## Related

- [Motion](./motion.md)
- [Reveal](./reveal.md)
- [Component Anatomy](./component-anatomy.md)
- [`useAnimate()`](/reference/ui#useanimate-element-options)
- [`vAnime` / `vAnimate`](/reference/ui#vanime-vanimate)
- [Package Integration](/guide/package-integration)
