# Alert

`RxAlert` renders a feedback block with `role="alert"`, optional title, default content, and an optional dismiss button.

## Import

```ts
import { RxAlert } from 'resuxjs/ui'
// Equivalent alias: ResuxAlert
```

## Basic usage

```vue
<RxAlert variant="info" title="Heads up">
  Your profile is still incomplete.
</RxAlert>
```

## Variants

The built-in stylesheet defines `info`, `success`, `warning`, and `danger`.

```vue
<RxAlert variant="success">Saved successfully.</RxAlert>
<RxAlert variant="warning">Check the values before continuing.</RxAlert>
<RxAlert variant="danger">The operation failed.</RxAlert>
```

## Dismissible alerts

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxAlert } from 'resuxjs/ui'

const visible = ref(true)
</script>

<template>
  <RxAlert v-if="visible" dismissible @dismiss="visible = false">
    This alert is controlled by the parent.
  </RxAlert>
</template>
```

::: info Dismiss does not hide automatically
The built-in close button only emits `dismiss`. `RxAlert` does not change its own visibility. The parent must remove/hide it.
:::

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `string` | `'info'` | No | Adds `rx-alert-${variant}`. Built-in styles: info/success/warning/danger. |
| `title` | `string` | `''` | No | Optional title text. |
| `dismissible` | `boolean` | `false` | No | Renders a close button that emits `dismiss`. |
| `unstyled` | `boolean` | `false` | No | Omits Resux alert classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `dismiss` | None | Emitted when the built-in dismiss button is clicked. |

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Alert body content. |

## Accessibility

The root uses `role="alert"`, which is assertive live-region semantics. Reserve it for information that should be announced promptly; not every static informational box needs an alert role.

The current dismiss button renders the visible character `×` but does not add an explicit `aria-label`. If the symbol is not announced clearly in your target assistive-technology/browser combinations, prefer a non-dismissible alert or augment/test the accessible naming in your application.

Meaning must not rely on the variant color alone.

## SSR / resumability / hydration

Static alert content can be SSR-rendered. Dismiss handling needs Vue runtime JavaScript and parent state. If the alert is not dismissible and is static, a normal semantic Resux block may avoid Vue runtime cost.

## Related

- [Badge](./badge.md)
- [Button](./button.md)
- [Current limits](/reference/limits)
