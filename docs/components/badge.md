# Badge

`RxBadge` is a small **non-interactive inline status/category primitive**. It renders its default slot inside a `<span>` and applies Resux badge classes unless `unstyled` is enabled.

A badge is useful when a short piece of text needs visual emphasis without becoming an action: status, category, environment, plan, release channel, count label, or compact metadata.

## When to use it

Good uses include:

```vue
<RxBadge variant="success">Active</RxBadge>
<RxBadge variant="warning">Beta</RxBadge>
<RxBadge variant="danger">Failed</RxBadge>
<RxBadge>v0.3.3</RxBadge>
```

Use a [Button](./button.md) instead when the element performs an action. Use an [Alert](./alert.md) when the message is important enough to require a larger feedback region.

## Import

```ts
import { RxBadge } from 'resuxjs/ui'
// Equivalent alias: ResuxBadge
```

## Basic usage

```vue
<RxBadge>Draft</RxBadge>
```

Conceptually the styled output is:

```html
<span class="rx-badge">Draft</span>
```

A non-default variant adds a modifier class according to the current implementation.

## Variants

The built-in stylesheet currently defines these verified variants:

```vue
<RxBadge variant="default">Default</RxBadge>
<RxBadge variant="success">Success</RxBadge>
<RxBadge variant="warning">Warning</RxBadge>
<RxBadge variant="danger">Danger</RxBadge>
<RxBadge variant="info">Info</RxBadge>
```

`variant` is implemented as a string prop, not a closed TypeScript union. That means another string can produce a modifier class, but it does **not** mean Resux ships built-in styling for that value.

If you add your own variant, own its CSS explicitly:

```vue
<RxBadge variant="premium">Premium</RxBadge>
```

```css
.rx-badge-premium {
  /* application-owned style */
}
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `string` | `'default'` | No | Selects/adds the badge modifier class. Built-in verified styles: `default`, `success`, `warning`, `danger`, `info`. |
| `unstyled` | `boolean` | `false` | No | Omits Resux-generated badge classes while preserving your own attributes/classes. |

There is no built-in `clickable`, `dismissible`, `icon`, or `size` prop in the current primitive.

## Native attributes

The root is a `<span>`, so normal attributes can be forwarded to it through the Vue component boundary:

```vue
<RxBadge
  class="release-badge"
  data-channel="canary"
  title="Canary release channel"
>
  Canary
</RxBadge>
```

Do not add interactive attributes such as `tabindex`/click handlers unless the semantics genuinely call for an interactive control—in which case a badge is usually the wrong root element.

## Events

No custom events are declared.

The badge is intentionally non-interactive. If a user must select, remove, or activate a token, compose a real button/control rather than relying on the badge's visual shape.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | Badge text/content. |

Keep the content compact. A badge containing paragraphs, forms, or large interactive regions is usually a sign that another component/semantic structure is more appropriate.

## Styling

Default styling uses the stable base class plus a variant modifier. Add your own class normally:

```vue
<RxBadge variant="info" class="release-channel">
  Nightly
</RxBadge>
```

Or use the component headlessly:

```vue
<RxBadge unstyled class="my-pill">
  Draft
</RxBadge>
```

`unstyled` does not change the `<span>` root or slot behavior.

## Accessibility

A badge is a visual `<span>`; its accessibility comes primarily from **meaningful text and surrounding context**.

### Do not rely on color alone

This is not sufficient if color is the only distinction:

```vue
<RxBadge variant="danger">●</RxBadge>
```

Prefer explicit content:

```vue
<RxBadge variant="danger">Failed</RxBadge>
```

### Repeated labels need context

A badge such as `New` or `Beta` may be understandable visually next to a heading, but ensure the reading order also makes that relationship clear.

```vue
<h2>
  Image optimizer
  <RxBadge variant="warning">Beta</RxBadge>
</h2>
```

### Live status is a separate concern

`RxBadge` does not automatically create an ARIA live region. If a status changes dynamically and must be announced, choose the correct live-region/status semantics for the application rather than assuming the badge handles announcements.

## SSR / resumability / hydration

The badge implementation has no client state, emitted events, or mount-time behavior. Its markup can therefore be server-rendered very cheaply **inside an existing Vue boundary**.

But `RxBadge` still comes from `resuxjs/ui`, whose components are Vue `defineComponent()` components. If a normal Resux page only needs a static status label, native markup can avoid introducing Vue solely for presentation:

```html
<span class="status-badge">Draft</span>
```

Use `RxBadge` when the surrounding region is already Vue-owned or when UI package consistency is worth that boundary. See [Component Anatomy](./component-anatomy.md).

## Recipe: status row

```vue
<div class="project-status">
  <span>API</span>
  <RxBadge variant="success">Operational</RxBadge>
</div>

<div class="project-status">
  <span>Image transforms</span>
  <RxBadge variant="warning">Degraded</RxBadge>
</div>
```

The surrounding markup owns the relationship between the subject and status; the badge supplies the compact visual label.

## Recipe: card metadata

```vue
<RxCard>
  <header>
    <h3>Resumability Deep Dive</h3>
    <RxBadge variant="info">Guide</RxBadge>
  </header>
  <p>Understand handlers, serialized scope, and DOM bindings.</p>
</RxCard>
```

## Common mistakes

### Making the whole badge clickable

If the label is an action such as “Remove tag,” render an actual button with an accessible name.

### Assuming arbitrary variants are built in

A string prop accepts arbitrary text; only documented variants have verified package styling.

### Using a badge for important feedback

A compact badge should not replace an alert/error message that needs explanation or action.

### Creating a Vue island for one static badge

Normal Resux/native HTML is preferable when no Vue-owned behavior is required.

## Related

- [Card](./card.md)
- [Alert](./alert.md)
- [Button](./button.md)
- [Component Anatomy](./component-anatomy.md)
