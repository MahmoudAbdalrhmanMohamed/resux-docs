# Accordion

`RxAccordion` is a small single disclosure component. It renders one button and conditionally renders its content.

## Import

```ts
import { RxAccordion } from 'resuxjs/ui'
// Equivalent alias: ResuxAccordion
```

## Basic usage

```vue
<RxAccordion title="Shipping details">
  Ships in 2–3 business days.
</RxAccordion>
```

## Initial open state

```vue
<RxAccordion title="Details" :open="true">
  Initially visible content.
</RxAccordion>
```

::: warning `open` is initialization, not controlled state
The implementation creates internal state from `props.open` during setup. It does not watch later `open` prop changes and it does not emit `update:open`. Use this primitive for simple local disclosure, not for externally controlled accordion state.
:::

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `title` | `string` | `'Accordion Title'` | No | Button label. |
| `open` | `boolean` | `false` | No | Initial internal open state. |
| `unstyled` | `boolean` | `false` | No | Omits Resux accordion classes. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Content rendered only while internal state is open. |

## Styling

Styled markup uses `rx-accordion`, `rx-accordion-trigger`, `rx-accordion-icon`, and `rx-accordion-content`. Open state also adds `open` to the root.

## Accessibility

The trigger is a native `<button type="button">`, so focus and Enter/Space activation work. The current implementation does **not** set `aria-expanded`, connect the trigger to content with `aria-controls`, assign a region role, or expose IDs for those relationships.

For a production disclosure that must follow the ARIA Accordion pattern, add/test the missing semantics or use an integration that implements the complete pattern.

## SSR / resumability / hydration

SSR output reflects the initial `open` value. Toggling is local Vue state and requires the Vue runtime boundary. Because the component does not synchronize external prop changes, parent state cannot control it after setup through the documented API.

## Related

- [Tabs](./tabs.md)
- [Current limits](/reference/limits)
- [Vue Islands](/guide/vue-islands)
