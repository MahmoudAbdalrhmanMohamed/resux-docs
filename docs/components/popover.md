# Popover

`RxPopover` is a click-toggled content container with a `trigger` slot and default content slot.

## Import

```ts
import { RxPopover } from 'resuxjs/ui'
// Equivalent alias: ResuxPopover
```

## Basic usage

```vue
<RxPopover>
  <template #trigger>
    More options
  </template>
  <p>Popover content</p>
</RxPopover>
```

The component always renders its own `<button type="button">` around the `trigger` slot. Put button **content**, not another `<button>`, in that slot.

## Controlled open prop

```vue
<RxPopover v-model:open="open">
  <template #trigger>Toggle details</template>
  Details
</RxPopover>
```

The rendered visibility follows `open`, and clicking the trigger emits `update:open` with the opposite value.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `open` | `boolean` | `false` | No | Current visible state. |
| `unstyled` | `boolean` | `false` | No | Omits Resux popover classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:open` | `boolean` | Emitted when the built-in trigger toggles. |

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `trigger` | None | Content inside the built-in trigger button. |
| `default` | None | Popover content rendered while `open` is true. |

## Styling

Styled markup uses `rx-popover`, `rx-popover-trigger`, and `rx-popover-content`.

## Accessibility and focus

The trigger is a native button, but the current implementation does **not** add `aria-expanded`, `aria-controls`, popover/dialog role semantics, focus movement, focus return, Escape handling, or outside-click dismissal.

Use it for simple non-critical toggled content only when those limitations are acceptable. For menus/dialog-like popovers, use a pattern/integration that implements the expected focus and keyboard behavior.

## SSR / resumability / hydration

If `open` is true during SSR, content can be in the server output. Toggling requires Vue event handling. The popover is therefore a Vue-island interaction rather than a resumable Resux template primitive.

## Related

- [Dropdown](./dropdown.md)
- [Tooltip](./tooltip.md)
- [Modal](./modal.md)
- [Current limits](/reference/limits)
