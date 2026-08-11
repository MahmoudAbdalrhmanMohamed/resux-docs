# Divider

`RxDivider` is a small **visual separator** with an optional text label. It is intentionally simple: it renders presentational markup and does not automatically decide whether the separation is semantic for assistive technology.

## When to use it

Use a divider when adjacent visual groups need clearer separation, for example:

- two groups of settings,
- “or” between sign-in methods,
- sections inside a card/panel,
- groups of menu/content items.

Do not add a divider only because a design mock contains a line. Often spacing, headings, or native sectioning elements communicate structure more clearly.

## Import

```ts
import { RxDivider } from 'resuxjs/ui'
// Equivalent alias: ResuxDivider
```

## Basic usage

```vue
<RxDivider />
<RxDivider label="or" />
```

A label is useful when the separation itself has meaning:

```vue
<RxButton>Continue with email</RxButton>
<RxDivider label="or" />
<RxButton variant="secondary">Continue with passkey</RxButton>
```

## Orientation

```vue
<RxDivider orientation="horizontal" />
```

`orientation` is a string prop that contributes a modifier class. The current built-in stylesheet verifies **horizontal** divider styling. Passing another orientation does not mean complete built-in layout/accessibility support exists.

For a custom vertical divider, provide your own styling and semantics deliberately:

```vue
<RxDivider
  orientation="vertical"
  class="toolbar-divider"
  role="separator"
  aria-orientation="vertical"
/>
```

```css
.toolbar-divider {
  /* application-owned vertical layout */
}
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `label` | `string` | `''` | No | Optional text displayed in the divider composition. |
| `orientation` | `string` | `'horizontal'` | No | Adds `rx-divider-${orientation}`. Built-in styling currently verifies the horizontal case. |
| `unstyled` | `boolean` | `false` | No | Omits Resux divider classes. |

There is no built-in `decorative`, `role`, or `ariaOrientation` prop. Native attributes can be passed when you need semantics.

## Events

No custom events are declared. A divider is not an interactive control.

## Slots

There are no component slots in the current primitive. Label text comes from the `label` prop.

If you need complex custom content in the center of a separator, compose application markup rather than assuming arbitrary slot support.

## Render/styling model

Styled markup uses classes including:

- `rx-divider`,
- `rx-divider-${orientation}`,
- `rx-divider-label` when the label composition is present.

You can add your own class:

```vue
<RxDivider label="More options" class="settings-divider" />
```

Or remove built-in classes:

```vue
<RxDivider
  unstyled
  label="or"
  class="my-divider"
/>
```

`unstyled` leaves the component's structure/label behavior intact; your CSS must supply the complete visual treatment.

## Accessibility

The current component uses generic `<div>`-based markup and does **not** automatically add `role="separator"` or `aria-orientation`.

That is intentional to avoid pretending every decorative line is a semantic separator.

### Decorative divider

If the divider only provides visual spacing/grouping and surrounding HTML already communicates the structure, no separator role may be needed.

```vue
<section aria-labelledby="profile-heading">
  <h2 id="profile-heading">Profile</h2>
  ...
  <RxDivider />
  ...
</section>
```

### Semantic separator

If the separator itself is meaningful, provide the appropriate semantics:

```vue
<RxDivider
  role="separator"
  aria-orientation="horizontal"
/>
```

### Labeled separator

A visual `label="or"` does not automatically establish an accessible separator name/relationship. Test the resulting composition in the context where it is used. Often the surrounding controls/text provide sufficient meaning; in other cases you may prefer explicit application markup.

### Avoid fake interaction

Do not attach click/keyboard behavior to the divider line. Use buttons, disclosure controls, tabs, or other proper widgets for actions.

## SSR / resumability / hydration

`RxDivider` has no interactive state or client lifecycle requirement of its own. Its output can be server-rendered inside an existing Vue boundary.

However, it is still a component from the Vue-based `resuxjs/ui` package. A normal Resux page that only needs a visual separator can use native markup instead of introducing Vue:

```html
<hr>
```

or application-owned decorative markup:

```html
<div class="divider" aria-hidden="true"></div>
```

Choose native `<hr>` when its semantic “thematic break” meaning is appropriate. Choose generic decoration when it is purely visual. Use `RxDivider` when you are already inside a Vue UI subtree and want the package's styling/composition.

Read [Component Anatomy](./component-anatomy.md) for the runtime boundary.

## Recipe: form alternatives

```vue
<form>
  <RxButton type="submit">Continue</RxButton>

  <RxDivider label="or" />

  <RxButton type="button" variant="secondary">
    Use a passkey
  </RxButton>
</form>
```

The buttons own the actions; the divider only explains their visual relationship.

## Recipe: card sections

```vue
<RxCard>
  <section>
    <h3>Account</h3>
    <p>Manage profile information.</p>
  </section>

  <RxDivider />

  <section>
    <h3>Security</h3>
    <p>Manage sessions and authentication.</p>
  </section>
</RxCard>
```

If those sections already have strong heading/spacing structure, evaluate whether the divider adds useful clarity or only decoration.

## Common mistakes

### Assuming `orientation="vertical"` is fully styled

The prop can create a modifier class, but the current built-in CSS only verifies horizontal styling. Add your own vertical layout.

### Assuming semantic separator behavior

Add `role="separator"`/`aria-orientation` only when the line is semantically meaningful.

### Using Divider instead of native `<hr>` everywhere

Native `<hr>` already represents a thematic break. Use the simplest element that communicates the correct meaning.

### Creating a Vue island for a separator

If no Vue behavior is otherwise needed, normal Resux/native HTML is the cheaper boundary.

## Related

- [Card](./card.md)
- [Kbd](./kbd.md)
- [Component Anatomy](./component-anatomy.md)
- [CSS and Tailwind](/guide/css-tailwind)
