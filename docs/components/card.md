# Card

`RxCard` is a non-interactive content container. It renders a `<div>` around the default slot.

## Import

```ts
import { RxCard } from 'resuxjs/ui'
// Equivalent alias: ResuxCard
```

## Basic usage

```vue
<RxCard>
  <h2>Project status</h2>
  <p>All systems operational.</p>
</RxCard>
```

## Glass variant

The built-in stylesheet includes a `glass` modifier:

```vue
<RxCard variant="glass">
  Translucent card content
</RxCard>
```

The `variant` prop is a string rather than a closed union. `default` and `glass` are the variants verified in the current built-in CSS.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `string` | `'default'` | No | Non-default values add `rx-card-${variant}`. Built-in extra style: `glass`. |
| `unstyled` | `boolean` | `false` | No | Omits Resux-generated card classes. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Card content. |

## Styling

Default markup uses `rx-card`; non-default variants add a modifier class. `unstyled` leaves only your classes/attributes.

```vue
<RxCard unstyled class="surface-panel">...</RxCard>
```

## Accessibility

A card has no universal semantic role, so the component intentionally renders a generic `<div>`. Add semantic structure inside it—or native attributes on it—according to the content. Do not add `role="group"`, `region`, or `article` unless those semantics are actually correct.

## SSR / resumability / hydration

The card itself has no client behavior. When used inside a Vue island it still belongs to that Vue subtree, but it does not independently require mount-time JavaScript. For purely static Resux markup, a normal semantic HTML element may avoid creating a Vue boundary just for presentation.

## Related

- [Badge](./badge.md)
- [Avatar](./avatar.md)
- [Vue Islands](/guide/vue-islands)
