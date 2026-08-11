# Tooltip

`RxTooltip` shows supplemental text while the pointer is over its wrapper.

## Import

```ts
import { RxTooltip } from 'resuxjs/ui'
// Equivalent alias: ResuxTooltip
```

## Basic usage

```vue
<RxTooltip text="Copy to clipboard">
  <span aria-hidden="true">⧉</span>
</RxTooltip>
```

The default slot is always rendered. Tooltip content is conditionally rendered after mouse enter and removed after mouse leave.

## Placement

```vue
<RxTooltip text="Top" placement="top">...</RxTooltip>
<RxTooltip text="Bottom" placement="bottom">...</RxTooltip>
```

`placement` is a free-form string used in a class name. Verify/application-style any placement you use; the source does not enforce a closed set.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `text` | `string` | `''` | No | Tooltip text. |
| `placement` | `string` | `'top'` | No | Adds `rx-tooltip-${placement}`. |
| `unstyled` | `boolean` | `false` | No | Omits Resux tooltip classes. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Hover target content. |

## Accessibility

::: danger Hover-only behavior
The current implementation listens to `mouseenter` and `mouseleave` only. It does not show on keyboard focus, set `role="tooltip"`, create `aria-describedby`, support Escape dismissal, or keep the tooltip available when moving the pointer into it.
:::

Therefore:

- never put required instructions only in `RxTooltip`;
- make the wrapped control independently accessible;
- do not use it as the only label for an icon button;
- prefer always-visible helper text or an accessible tooltip integration for critical information.

## SSR / resumability / hydration

The wrapper/default slot can be SSR-rendered. Tooltip visibility is Vue state driven by pointer events, so it requires Vue runtime JavaScript.

## Related

- [Popover](./popover.md)
- [Button](./button.md)
- [Current limits](/reference/limits)
