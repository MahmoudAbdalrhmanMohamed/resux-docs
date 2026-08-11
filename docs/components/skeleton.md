# Skeleton

`RxSkeleton` renders a visual loading placeholder `<div>` with configurable dimensions and border radius.

## Import

```ts
import { RxSkeleton } from 'resuxjs/ui'
// Equivalent alias: ResuxSkeleton
```

## Basic usage

```vue
<RxSkeleton width="12rem" height="1.25rem" />
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `width` | `string` | `'100%'` | No | Inline CSS width. |
| `height` | `string` | `'1rem'` | No | Inline CSS height. |
| `rounded` | `string` | `'0.375rem'` | No | Inline border radius. |
| `unstyled` | `boolean` | `false` | No | Omits `rx-skeleton`. |

## Events and slots

No custom events and no slots.

## Styling

The default `rx-skeleton` class uses a repeating shimmer animation.

```vue
<RxSkeleton unstyled class="my-placeholder" width="100%" height="10rem" />
```

::: warning Reduced motion
The helper-based Web Animations APIs in `resuxjs/ui` check `prefers-reduced-motion`, but the current **CSS shimmer** attached to `rx-skeleton` is an infinite animation and does not include a built-in `prefers-reduced-motion` override. Add one in application CSS when reduced-motion support is required:

```css
@media (prefers-reduced-motion: reduce) {
  .rx-skeleton { animation: none; }
}
```
:::

## Accessibility

A skeleton is visual presentation, not a loading announcement. The component does not set `aria-hidden`, `aria-busy`, or live-region attributes automatically. Mark the real region as busy or expose concise loading text when users need that state announced.

```vue
<section :aria-busy="loading ? 'true' : 'false'">
  <RxSkeleton v-if="loading" aria-hidden="true" height="6rem" />
  <article v-else>...</article>
</section>
```

## SSR / resumability / hydration

The component itself has no client state. If the parent Vue island swaps skeleton/content reactively, that parent behavior requires Vue runtime. Static SSR loading placeholders do not independently need client behavior.

## Related

- [Motion](./motion.md)
- [Accessibility/current limits](/reference/limits)
