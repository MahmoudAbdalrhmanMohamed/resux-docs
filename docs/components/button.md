# Button

`RxButton` renders a native `<button>` with Resux UI classes. Use it for actions inside a Vue runtime boundary.

## Import

```ts
import { RxButton } from 'resuxjs/ui'
// Equivalent alias: ResuxButton
```

## Basic usage

```vue
<RxButton @click="save">Save</RxButton>
```

The default `type` is `button`, so placing an `RxButton` inside a form does not submit the form unless you request `type="submit"`.

## Variants

The built-in stylesheet defines these variants:

```vue
<RxButton variant="primary">Primary</RxButton>
<RxButton variant="secondary">Secondary</RxButton>
<RxButton variant="outline">Outline</RxButton>
<RxButton variant="ghost">Ghost</RxButton>
```

`variant` is typed by Vue as a string, not a closed TypeScript union. The four names above are the variants that currently have built-in CSS.

## Sizes

```vue
<RxButton size="sm">Small</RxButton>
<RxButton size="md">Medium</RxButton>
<RxButton size="lg">Large</RxButton>
```

The built-in stylesheet defines `sm`, `md`, and `lg`.

## Disabled

```vue
<RxButton :disabled="saving">
  {{ saving ? 'Saving…' : 'Save' }}
</RxButton>
```

`disabled` is forwarded to the native button. There is no built-in `loading` prop or spinner; model loading state explicitly in your content and application logic.

## Native attributes and events

Attributes not declared as props are forwarded to the `<button>`, so native attributes/listeners can be used:

```vue
<RxButton
  name="intent"
  value="publish"
  aria-describedby="publish-help"
  @focus="onFocus"
  @click="publish"
>
  Publish
</RxButton>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `string` | `'primary'` | No | Adds `rx-btn-${variant}` when styled. Built-in CSS: `primary`, `secondary`, `outline`, `ghost`. |
| `size` | `string` | `'md'` | No | Adds `rx-btn-${size}`. Built-in CSS: `sm`, `md`, `lg`. |
| `type` | `string` | `'button'` | No | Native button `type`. |
| `disabled` | `boolean` | `false` | No | Native disabled state. |
| `unstyled` | `boolean` | `false` | No | Omits Resux-generated button classes. |

## Events

`RxButton` declares no custom emits. Native button listeners such as `@click`, `@focus`, and `@blur` are forwarded through Vue attributes.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Button contents. |

## Exposed methods

No component methods are explicitly exposed.

## Styling

With default styles enabled the root receives `rx-btn`, `rx-btn-${variant}`, and `rx-btn-${size}` plus your own class.

```vue
<RxButton class="save-action">Save</RxButton>
<RxButton unstyled class="my-headless-button">Save</RxButton>
```

Built-in CSS uses fixed primitive values. `tokens` configured on the UI module are exposed in runtime config but are not automatically converted into arbitrary CSS variables by this component.

## Accessibility

Because the component renders a native `<button>`, browser keyboard activation, focusability, disabled semantics, and button role are inherited from the platform. Keep visible text or an accessible name when the content is icon-only.

```vue
<RxButton aria-label="Close dialog">×</RxButton>
```

Do not use the `disabled` prop when you only want a visual disabled style—the native disabled state also removes normal activation behavior.

## SSR / resumability / hydration

The button markup can be server-rendered by Vue, but `RxButton` belongs to `resuxjs/ui`, so event listeners such as `@click` need the Vue island/runtime that owns the component. It is not a zero-JavaScript Resux event primitive.

For a navigation action that does not require Vue state, prefer an ordinary Resux link/template pattern rather than hydrating a button only to navigate.

## Complete example

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxButton } from 'resuxjs/ui'

const saving = ref(false)

async function save() {
  saving.value = true
  try {
    await fetch('/api/profile', { method: 'POST' })
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <RxButton
    variant="primary"
    :disabled="saving"
    :aria-busy="saving ? 'true' : 'false'"
    @click="save"
  >
    {{ saving ? 'Saving…' : 'Save profile' }}
  </RxButton>
</template>
```

## Related

- [Icon](./icon.md)
- [Vue Islands](/guide/vue-islands)
- [UI package reference](/reference/ui)
