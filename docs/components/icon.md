# UI Icon primitive

`RxIcon` from `resuxjs/ui` is a tiny placeholder-oriented UI primitive. It renders a `<span>` containing the icon name in square brackets. It is **not** the SVG icon component exported from `resuxjs/icons`.

## Import

```ts
import { RxIcon } from 'resuxjs/ui'
// Equivalent alias in this package: ResuxIcon
```

## Basic usage

```vue
<RxIcon name="check" />
```

Conceptually this renders text like:

```html
<span>[check]</span>
```

Use the full icon package when you need actual SVG paths:

```ts
import { Icon } from 'resuxjs/icons'
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `'check'` | No | Text placed between square brackets. |
| `size` | `string | number` | `'1.25rem'` | No | Applied to `font-size`; numeric values become pixels. |
| `color` | `string` | `'currentColor'` | No | Applied to inline text color. |
| `unstyled` | `boolean` | `false` | No | Omits the `rx-icon` class. |

## Events and slots

No custom events and no slots.

## Accessibility

Because the current primitive emits visible text such as `[check]`, screen readers may encounter that text unless you provide an accessibility treatment. For decorative icons, prefer the SVG icon package (which defaults to `aria-hidden="true"`) or add `aria-hidden="true"` deliberately.

For semantic icons, pair an icon with accessible text rather than expecting an icon name to be a user-facing label.

## SSR / resumability / hydration

There is no mount-time behavior in `RxIcon`, but it is still a Vue component when imported from `resuxjs/ui`. The full `resuxjs/icons` component also requires a Vue runtime boundary for remote/lazy behavior; built-in registry icons can render their SVG immediately in that Vue rendering path.

## Do not confuse the aliases

Both packages export a symbol named `ResuxIcon`:

```ts
import { ResuxIcon as UiIcon } from 'resuxjs/ui'
import { ResuxIcon as SvgIcon } from 'resuxjs/icons'
```

Use explicit import aliases when both are needed in the same module.

## Related

- [Full Icons documentation](/icons/)
- [Button](./button.md)
