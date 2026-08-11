# Avatar

`RxAvatar` displays an image when `src` is present and otherwise renders two-character fallback initials. It can also show a small status dot.

## Import

```ts
import { RxAvatar } from 'resuxjs/ui'
// Equivalent alias: ResuxAvatar
```

## Image avatar

```vue
<RxAvatar
  src="/people/ada.jpg"
  alt="Ada Lovelace"
  size="lg"
/>
```

When `src` is non-empty the component renders a native `<img>` with `class="rx-avatar-img"` unless unstyled.

## Fallback initials

```vue
<RxAvatar alt="Mahmoud Abdalrahman" />
```

Without `src`, the fallback is the first two characters of `alt`, upper-cased. This is a simple character slice; it does not derive first/last-name initials.

## Status

```vue
<RxAvatar src="/people/user.jpg" alt="User" status="online" />
<RxAvatar src="/people/user.jpg" alt="User" status="offline" />
```

The built-in stylesheet provides `online` and `offline` status colors. The status indicator is visual only.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `src` | `string` | `''` | No | Native image source. |
| `alt` | `string` | `'Avatar'` | No | Image alternative text and fallback-initial source. |
| `size` | `string` | `'md'` | No | Adds size class. Built-in CSS: `sm`, `md`, `lg`. |
| `status` | `string` | `''` | No | Optional visual status class. Built-in CSS: `online`, `offline`. |
| `unstyled` | `boolean` | `false` | No | Omits Resux avatar classes. |

## Events

No custom events. Native image listeners/attributes can flow through the component root rather than directly targeting the nested image, so do not assume every arbitrary image-only attribute lands on `<img>`.

## Slots

No slots.

## Styling

Styled markup uses `rx-avatar`, `rx-avatar-${size}`, `rx-avatar-img`, and status classes.

## Accessibility

Choose `alt` based on meaning:

- If the avatar identifies a person and that identity is not already stated next to it, use a meaningful name.
- If adjacent text already names the person and the image is redundant, an empty alt may be more appropriate—but note that the fallback text will then also be empty when no image exists.
- The status dot has no text/ARIA semantics. If online/offline state matters, expose it as text or an accessible label separately.

## Images and optimization

`RxAvatar` uses the `src` directly; it does **not** route the image through `ResuxImg` automatically. For responsive/optimized application images, see [Images](/media/images) and decide whether an optimized URL should be supplied as the avatar `src`.

## SSR / resumability / hydration

Avatar rendering is non-interactive. It can be SSR-rendered inside a Vue island, but there is no avatar-specific client behavior. Do not create a Vue island only to render a static avatar when native Resux markup is enough.

## Related

- [Images](/media/images)
- [Card](./card.md)
