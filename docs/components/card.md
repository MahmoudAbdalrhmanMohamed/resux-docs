# Card

`RxCard` is a **non-interactive visual container**. It renders a `<div>` around the default slot and applies Resux card classes unless `unstyled` is enabled.

The component deliberately does not choose document semantics for you. A “card” in a design can represent an article, product, settings group, dashboard tile, navigation target, or pure visual surface; those are not the same semantic object.

## When to use it

Use `RxCard` when you are already inside a Vue UI boundary and want a consistent Resux UI surface around content such as:

- dashboard metrics,
- settings groups,
- product summaries,
- profile information,
- callouts that do not need alert semantics,
- grouped content in a grid.

Use native semantic markup instead when the content has a stronger element available—for example `<article>`, `<section>`, `<aside>`, or `<fieldset>`.

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

Conceptually:

```html
<div class="rx-card">
  <h2>Project status</h2>
  <p>All systems operational.</p>
</div>
```

## Glass variant

The current built-in stylesheet includes a `glass` modifier:

```vue
<RxCard variant="glass">
  <h2>Preview</h2>
  <p>Translucent card content.</p>
</RxCard>
```

`variant` is implemented as a string prop. `default` and `glass` are the variants verified in current built-in CSS. Another string can create a modifier class without automatically receiving a framework style.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `variant` | `string` | `'default'` | No | Non-default values add `rx-card-${variant}`. Current built-in extra style: `glass`. |
| `unstyled` | `boolean` | `false` | No | Omits Resux-generated card classes while preserving application attributes/classes. |

There is no built-in `href`, `clickable`, `header`, `footer`, `title`, or `elevation` prop in the current primitive. Compose those needs with normal markup.

## Native attributes

The component root is a `<div>`, and attributes can be forwarded to it:

```vue
<RxCard
  id="billing-summary"
  class="billing-card"
  data-plan="pro"
>
  ...
</RxCard>
```

Because the root is generic, adding attributes does not automatically make it an interactive or semantic region.

## Events

No custom events are declared.

A native listener could be passed through the Vue component/root, but making a generic `<div>` card clickable creates keyboard/semantics problems unless you deliberately implement the complete interactive pattern.

If the entire surface navigates somewhere, prefer a proper link composition. If it performs an action, prefer a button. Avoid turning `RxCard` itself into a fake control merely because it has a convenient visual box.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | All card content. |

There are no dedicated `header`, `body`, or `footer` slots in the current component. Create structure inside the default slot:

```vue
<RxCard>
  <header>
    <h2>Team plan</h2>
    <RxBadge variant="success">Active</RxBadge>
  </header>

  <p>Up to 20 members.</p>

  <footer>
    <RxButton>Manage plan</RxButton>
  </footer>
</RxCard>
```

## Styling

Default markup uses `rx-card`; a non-default variant contributes its modifier class.

Add application styling normally:

```vue
<RxCard class="dashboard-panel">...</RxCard>
```

Or use the structural component without Resux classes:

```vue
<RxCard unstyled class="surface-panel">...</RxCard>
```

`unstyled` does not change the root element or slot structure.

## Semantic structure

The component intentionally renders a generic `<div>` because “card” is a visual pattern, not one universal HTML semantic.

Choose semantics **inside** or around the card according to content.

### Article-like card

If the content can stand independently, native `<article>` may be a better root than `RxCard`:

```html
<article class="article-card">
  <h2>Architecture Deep Dive</h2>
  <p>Understand compiler, server, and browser ownership.</p>
</article>
```

### Settings group

A heading and section relationship may be more appropriate:

```vue
<RxCard>
  <section aria-labelledby="security-heading">
    <h2 id="security-heading">Security</h2>
    ...
  </section>
</RxCard>
```

### Form controls

If the card groups related form controls, consider whether `<fieldset>`/`<legend>` gives stronger semantics than a generic card container.

## Accessibility

Do not add roles mechanically just because the component is visually prominent.

- `role="group"` is not required for every card.
- `role="region"` should generally have a useful accessible name and represent a meaningful region.
- `article` semantics should be used when the content is independently distributable/self-contained.
- clickable cards need real keyboard/focus semantics, ideally through native links/buttons rather than a click listener on the `<div>`.
- headings inside repeated cards should preserve a logical document outline.

The visual border/background does not supply semantics by itself.

## SSR / resumability / hydration

`RxCard` has no internal reactive state, custom events, or mount behavior. Its markup can be server-rendered inside a Vue island and adds very little component-specific client work.

However, the package boundary still matters: `RxCard` is a Vue `defineComponent()` export from `resuxjs/ui`. If the rest of the page is normal Resux, using a native semantic container can avoid creating a Vue runtime boundary solely for a surface style.

For example, this normal Resux markup may be preferable:

```html
<article class="card">
  <h2>Architecture Deep Dive</h2>
  <p>...</p>
</article>
```

Read [Component Anatomy](./component-anatomy.md) and [Vue Islands](/guide/vue-islands).

## Recipe: dashboard metric

```vue
<RxCard>
  <p class="metric-label">Successful builds</p>
  <strong class="metric-value">128</strong>
  <RxBadge variant="success">+12%</RxBadge>
</RxCard>
```

The card supplies the visual surface. Application markup owns the meaning of the label/value/trend.

## Recipe: action card without fake click semantics

Instead of:

```vue
<!-- Avoid making the generic div itself the only control -->
<RxCard @click="openProject">
  <h3>Resux docs</h3>
</RxCard>
```

prefer an explicit action:

```vue
<RxCard>
  <h3>Resux docs</h3>
  <p>Framework documentation.</p>
  <RxButton @click="openProject">Open project</RxButton>
</RxCard>
```

Or use a real `<a>` as the appropriate navigational element.

## Recipe: unstyled/headless surface

```vue
<RxCard
  unstyled
  class="rounded-xl border border-slate-700 bg-slate-900 p-6"
>
  <h2>Custom card</h2>
  <p>Application-owned styling.</p>
</RxCard>
```

This is useful inside a Vue UI subtree when you want the component structure/API but not the built-in theme.

## Common mistakes

### Assuming Card is interactive

It is a `<div>` and declares no custom action API.

### Assuming arbitrary variants are styled

Only documented built-in variants are verified by the current CSS.

### Using a generic card where native semantics are stronger

Prefer `article`, `section`, `fieldset`, link, or button semantics when they accurately describe the content/action.

### Creating a Vue island for static presentation only

Normal Resux/native markup is usually the smaller boundary.

## Related

- [Badge](./badge.md)
- [Avatar](./avatar.md)
- [Divider](./divider.md)
- [Button](./button.md)
- [Component Anatomy](./component-anatomy.md)
- [Vue Islands](/guide/vue-islands)
