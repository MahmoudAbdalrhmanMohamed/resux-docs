# Modal

`RxModal` conditionally renders a backdrop and content shell. It is a small overlay primitive, not a complete accessible dialog system.

## Import

```ts
import { RxModal } from 'resuxjs/ui'
// Equivalent alias: ResuxModal
```

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxModal, RxButton } from 'resuxjs/ui'

const open = ref(false)
</script>

<template>
  <RxButton @click="open = true">Open</RxButton>
  <RxModal v-model:open="open" title="Delete item">
    Confirm the destructive action.
  </RxModal>
</template>
```

## Closing behavior

The current component closes when:

- the backdrop itself is clicked;
- the built-in `×` button is clicked.

Content clicks stop propagation so they do not close through the backdrop handler.

It does **not** currently close on Escape.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `open` | `boolean` | `false` | No | Whether modal markup is rendered. |
| `title` | `string` | `''` | No | Optional heading text. |
| `unstyled` | `boolean` | `false` | No | Omits Resux modal classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:open` | `false` | Emitted when the built-in close behavior runs. |
| `close` | None | Emitted at the same time as `update:open(false)`. |

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Modal body content. |

## Styling

Styled markup uses `rx-modal-backdrop`, `rx-modal`, `rx-modal-header`, and `rx-modal-close`.

## Accessibility

::: danger Dialog semantics are not built in
The current source does not set `role="dialog"`, `aria-modal="true"`, `aria-labelledby`, or `aria-describedby`. It also does not trap focus, move initial focus into the modal, restore focus on close, make the background inert, or handle Escape.
:::

The built-in close button displays `×` without an explicit `aria-label`.

For production dialogs—especially forms, destructive confirmations, and anything blocking the rest of the page—use an implementation that provides and tests the complete focus/ARIA/keyboard contract, or extend this primitive in application code and verify it across keyboard and screen-reader scenarios.

## SSR / resumability / hydration

If `open` is true at SSR time, modal markup can be present in Vue SSR output. All closing behavior and open-state synchronization require the Vue island/runtime. This is not a resumable Resux overlay primitive.

## Complete controlled example

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxButton, RxModal } from 'resuxjs/ui'

const open = ref(false)

function onClosed() {
  console.log('modal closed')
}
</script>

<template>
  <RxButton @click="open = true">Show details</RxButton>
  <RxModal v-model:open="open" title="Details" @close="onClosed">
    <p>This example demonstrates the implemented control flow only.</p>
  </RxModal>
</template>
```

## Related

- [Popover](./popover.md)
- [Button](./button.md)
- [Current limits](/reference/limits)
- [Vue Islands](/guide/vue-islands)
