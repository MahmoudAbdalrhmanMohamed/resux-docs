# Divider

`RxDivider` is a visual separator with an optional text label.

## Import

```ts
import { RxDivider } from 'resuxjs/ui'
// Equivalent alias: ResuxDivider
```

## Basic usage

```vue
<RxDivider />
<RxDivider label="or" />
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `label` | `string` | `''` | No | Optional divider text. |
| `orientation` | `string` | `'horizontal'` | No | Adds `rx-divider-${orientation}`. The built-in stylesheet currently defines horizontal divider styling. |
| `unstyled` | `boolean` | `false` | No | Omits Resux divider classes. |

## Events

No custom events.

## Slots

No slots; label text comes from `label`.

## Styling

Styled markup uses `rx-divider`, `rx-divider-${orientation}`, and `rx-divider-label`. Only the horizontal modifier is verified in the default CSS, so a custom vertical orientation needs application styling.

## Accessibility

The component renders a generic `<div>` and does **not** automatically set `role="separator"` or `aria-orientation`. If the line is semantically a separator, add the appropriate role/ARIA yourself and test the labeled composition:

```vue
<RxDivider role="separator" aria-orientation="horizontal" />
```

If it is purely decorative, leaving it out of the accessibility tree semantics can be appropriate.

## SSR / resumability / hydration

No interactive behavior. Prefer native markup in non-Vue Resux templates when a Vue island is otherwise unnecessary.

## Related

- [Card](./card.md)
- [Kbd](./kbd.md)
