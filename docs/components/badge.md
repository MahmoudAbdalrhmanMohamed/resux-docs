# Badge

`RxBadge` renders short inline status/category content in a `<span>`.

## Import

```ts
import { RxBadge } from 'resuxjs/ui'
// Equivalent alias: ResuxBadge
```

## Basic usage

```vue
<RxBadge>Draft</RxBadge>
```

## Variants

The current built-in stylesheet defines:

```vue
<RxBadge variant="default">Default</RxBadge>
<RxBadge variant="success">Success</RxBadge>
<RxBadge variant="warning">Warning</RxBadge>
<RxBadge variant="danger">Danger</RxBadge>
<RxBadge variant="info">Info</RxBadge>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `string` | `'default'` | No | Adds `rx-badge-${variant}`. Verified styles: default/success/warning/danger/info. |
| `unstyled` | `boolean` | `false` | No | Omits Resux classes. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Badge text/content. |

## Accessibility

The badge is a visual `<span>`. Status meaning must not depend on color alone. Put meaningful text in the badge, or add surrounding accessible context when the badge is decorative/redundant.

## SSR / resumability / hydration

No client logic is implemented by the badge itself. Avoid introducing a Vue island solely for a static badge when equivalent Resux template markup is sufficient.

## Related

- [Alert](./alert.md)
- [Card](./card.md)
