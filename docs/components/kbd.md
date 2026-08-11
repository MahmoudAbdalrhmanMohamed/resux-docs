# Kbd

`RxKbd` renders the semantic HTML `<kbd>` element with Resux styling.

## Import

```ts
import { RxKbd } from 'resuxjs/ui'
// Equivalent alias: ResuxKbd
```

## Basic usage

```vue
<p>Press <RxKbd>Ctrl</RxKbd> + <RxKbd>K</RxKbd> to search.</p>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `unstyled` | `boolean` | `false` | No | Omits the `rx-kbd` class. |

## Events

No custom events.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Key name/content. |

## Styling

The built-in `rx-kbd` style provides compact monospace key-cap presentation.

## Accessibility

`<kbd>` is appropriate for user input/keyboard notation. It does not make a key interactive; do not attach click behavior merely because it looks button-like.

## SSR / resumability / hydration

No client behavior. In a Resux template that does not otherwise need Vue, native `<kbd>` is equivalent and cheaper.

## Related

- [Button](./button.md)
