# Kbd

`RxKbd` renders the semantic HTML `<kbd>` element with Resux UI styling. It is a **presentation/semantics primitive**, not an interactive keyboard shortcut system.

Use it when documentation, help text, onboarding, or a command palette needs to visually represent **input the user should type or press**.

## When to use it

Good examples:

- keyboard shortcuts such as `Ctrl` + `K`,
- a single key such as `Esc`,
- key sequences such as `G` then `H`,
- terminal/help instructions where a user must press a key.

Do **not** use `RxKbd` as a substitute for a button. `<kbd>` communicates keyboard/user-input notation; it does not make its content focusable or clickable.

If the content is simply an arbitrary code token, use normal code/text semantics instead of `<kbd>`.

## Import

```ts
import { RxKbd } from 'resuxjs/ui'
// Equivalent alias: ResuxKbd
```

`RxKbd` and `ResuxKbd` point to the same Vue component object. Choose one naming convention and keep it consistent within your Vue UI subtree.

## Basic usage

```vue
<p>
  Press <RxKbd>Ctrl</RxKbd> + <RxKbd>K</RxKbd> to search.
</p>
```

The component renders conceptually as:

```html
<p>
  Press <kbd class="rx-kbd">Ctrl</kbd> + <kbd class="rx-kbd">K</kbd> to search.
</p>
```

The exact class output follows the current component implementation and `unstyled` setting.

## Key sequences

Keep each independently pressed key in its own `<kbd>` when that makes the sequence easier to understand:

```vue
<p>
  Open search with
  <RxKbd>Ctrl</RxKbd>
  +
  <RxKbd>Shift</RxKbd>
  +
  <RxKbd>F</RxKbd>.
</p>
```

For a sequence rather than a simultaneous chord, use surrounding language:

```vue
<p>
  Press <RxKbd>G</RxKbd>, then <RxKbd>H</RxKbd>.
</p>
```

The component does not parse shortcut syntax or add separators for you; the surrounding document owns that presentation.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `unstyled` | `boolean` | `false` | No | Omits the built-in `rx-kbd` class so application styling can own the element. |

There is intentionally no `key`, `shortcut`, `pressed`, or keyboard-listener prop. `RxKbd` only renders notation.

## Native attributes

Because the component is a small Vue primitive whose root is `<kbd>`, root attributes/classes can be supplied through normal component attribute fallthrough.

```vue
<RxKbd
  class="docs-shortcut"
  data-command="search"
  title="Open search"
>
  Ctrl K
</RxKbd>
```

Use native attributes only when they are meaningful for the rendered `<kbd>`. Adding `tabindex="0"` just to make the key cap focusable usually creates unnecessary keyboard stops.

## Events

`RxKbd` declares no custom events.

A DOM listener passed through the root may technically be possible through Vue attribute fallthrough, but attaching click behavior to a `<kbd>` is usually the wrong semantic design. If users must activate an action, use [Button](./button.md) or another proper interactive element and place the shortcut hint inside/next to it.

## Slots

| Slot | Props | Description |
| --- | --- | --- |
| `default` | None | The displayed key name or key-sequence notation. |

The slot can contain more than plain text, but simple text normally produces the clearest keyboard notation.

## Styling

With default UI styles enabled, the built-in `rx-kbd` class provides a compact key-cap presentation, including typography/border/background treatment defined by the current UI stylesheet.

Use your own class alongside it:

```vue
<RxKbd class="shortcut-key">Esc</RxKbd>
```

Or opt out of Resux styling completely:

```vue
<RxKbd unstyled class="my-keycap">Esc</RxKbd>
```

`unstyled` does not change the semantic `<kbd>` root; it only removes the Resux-generated styling class for this component.

## Accessibility

`<kbd>` is the appropriate semantic element for **user input notation**. It does not itself announce “this shortcut is currently available” or register a keyboard command.

For accessible shortcut documentation:

- include the action in normal text, not only the key cap,
- do not communicate meaning only through key-cap color,
- avoid making static key notation focusable,
- if a real control has a keyboard shortcut, ensure the control itself has a useful accessible name,
- consider whether platform-specific modifier names differ (`Ctrl` vs `Command`).

Example:

```vue
<button aria-keyshortcuts="Control+K" @click="openSearch">
  Search
  <span aria-hidden="true">
    <RxKbd>Ctrl</RxKbd> + <RxKbd>K</RxKbd>
  </span>
</button>
```

`aria-keyshortcuts` belongs on the actual actionable control, not on the decorative `<kbd>` notation. Whether you hide duplicate visual notation from assistive technology depends on the surrounding accessible name/content.

## SSR / resumability / hydration

`RxKbd` itself has **no client state, mount hook, or custom interaction**. Its output can be server-rendered as a simple `<kbd>`.

However, `RxKbd` is still defined in `resuxjs/ui`, which is the Vue UI package. If you introduce a Vue island solely to render this static primitive, the island is a much larger runtime decision than the component itself.

In a normal Resux template that does not otherwise need Vue, native markup is equivalent and cheaper:

```html
<kbd class="shortcut-key">Ctrl</kbd>
```

Use the UI component when you are already inside a Vue-owned UI region or want its package-level styling/API consistency.

Read [Component Anatomy](./component-anatomy.md) for the runtime distinction.

## Recipe: shortcut list

```vue
<template>
  <dl class="shortcuts">
    <div>
      <dt>Search</dt>
      <dd><RxKbd>Ctrl</RxKbd> + <RxKbd>K</RxKbd></dd>
    </div>
    <div>
      <dt>Close dialog</dt>
      <dd><RxKbd>Esc</RxKbd></dd>
    </div>
    <div>
      <dt>Save</dt>
      <dd><RxKbd>Ctrl</RxKbd> + <RxKbd>S</RxKbd></dd>
    </div>
  </dl>
</template>
```

The surrounding `<dl>` gives the shortcuts structure; `RxKbd` only represents the key input.

## Common mistakes

### Treating it as a button

```vue
<!-- Avoid -->
<RxKbd @click="save">S</RxKbd>
```

Use a real button/control for an action.

### Hiding the action name

```vue
<!-- Ambiguous without context -->
<RxKbd>Ctrl K</RxKbd>
```

Prefer:

```vue
<p>Open search: <RxKbd>Ctrl</RxKbd> + <RxKbd>K</RxKbd></p>
```

### Creating a Vue island for static notation only

If the surrounding page is normal Resux and no Vue behavior is required, use native `<kbd>`.

## Related

- [Button](./button.md)
- [Component Anatomy](./component-anatomy.md)
- [UI Package API](/reference/ui)
- [Vue Islands](/guide/vue-islands)
