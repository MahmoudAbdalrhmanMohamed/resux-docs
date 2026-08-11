# Component Anatomy

This page teaches you **how to read and evaluate a `resuxjs/ui` component**. The individual component pages tell you the exact props, events, slots, limitations, and examples. This guide explains the recurring implementation model behind them so that a component name never hides its runtime cost or behavior.

## First: there are two different meanings of “component” in Resux

This is the most important distinction in the UI documentation.

### Normal Resux component/template

Normal `.vue`-style Resux pages/components are compiled by Resux. They follow the server-rendered/resumable application model described in [How Resux Uses Vue](/guide/how-resux-uses-vue) and [Resumability Deep Dive](/guide/resumability-deep-dive).

### `resuxjs/ui` component

The `resuxjs/ui` package is implemented with Vue `defineComponent()`. Its components are Vue runtime components.

That means:

- their props are Vue props,
- custom events are Vue emits,
- `setup()`/refs/mount hooks are Vue-owned where used,
- `v-model` follows Vue's `modelValue` + `update:modelValue` convention,
- motion components that run on mount require browser-side Vue lifecycle,
- interactive state inside components such as Select/Popover/Tabs is Vue state.

Use these components inside a [Vue island](/guide/vue-islands) or another explicit Vue runtime boundary.

## Why this distinction matters

Consider two visually identical badges:

```vue
<!-- Normal Resux markup -->
<span class="status-badge">Draft</span>
```

and:

```vue
<!-- Inside a Vue runtime boundary -->
<RxBadge>Draft</RxBadge>
```

Both can produce a `<span>` that looks the same. The first needs no Vue component merely to exist. The second is useful when you are already inside a Vue-owned UI subtree or want the UI package's consistent primitive API/styles.

A static component is not “bad,” but **do not create a Vue island only because a visual primitive exists in the UI package**.

## The repeated implementation pattern

Many UI primitives follow a small pattern:

```ts
export const RxExample = defineComponent({
  name: 'RxExample',
  props: {
    variant: { type: String, default: 'default' },
    unstyled: { type: Boolean, default: false }
  },
  setup(props, { slots, attrs }) {
    return () => h(
      'div',
      {
        ...attrs,
        class: props.unstyled
          ? attrs.class
          : ['rx-example', `rx-example-${props.variant}`, attrs.class]
      },
      slots.default?.()
    )
  }
})
```

The exact code differs per component, but this pattern explains several recurring docs sections.

## Props

Props configure behavior owned by the component.

For example, `RxButton` currently declares:

- `variant`,
- `size`,
- `type`,
- `disabled`,
- `unstyled`.

The docs list the actual defaults and current built-in style variants rather than pretending that every arbitrary string has built-in design treatment.

### String props are often open-ended

Several props are implemented as Vue `String` props rather than closed TypeScript unions. For example, a `variant` may technically accept any string even when built-in CSS defines only a small verified set.

The docs therefore distinguish:

- **accepted prop shape** — what the component lets Vue receive,
- **built-in behavior/style** — what the framework currently implements.

Do not assume `variant="purple"` is a supported built-in design simply because it does not produce a type error.

## Native attributes

Most primitives spread undeclared `attrs` onto their root/native element.

Example:

```vue
<RxButton
  id="save"
  data-testid="save-button"
  aria-describedby="save-help"
  @focus="onFocus"
>
  Save
</RxButton>
```

When the component renders a native `<button>`, these attributes/listeners can reach that root according to Vue's attribute fallthrough behavior and the component implementation.

This is why each docs page tells you the actual root element. Native semantics depend on it.

## Root element matters

The name “Card,” “Alert,” or “Divider” does not automatically create a WAI-ARIA semantic contract.

Examples from the current package:

- `RxButton` renders `<button>`.
- `RxInput` renders `<input>`.
- `RxTextarea` renders `<textarea>`.
- `RxDatePicker` renders `<input type="date">`.
- `RxKbd` renders `<kbd>`.
- `RxCard` renders `<div>`.
- `RxBadge` renders `<span>`.
- `RxDivider` renders a `<div>` composition rather than automatically giving itself `role="separator"`.

Native element choice answers questions about keyboard behavior, form behavior, semantics, and attributes more reliably than the component name.

## Slots

Slots are content insertion points owned by Vue.

Simple primitives typically expose a `default` slot:

```vue
<RxCard>
  <h2>Project</h2>
  <p>Ready to deploy.</p>
</RxCard>
```

Other components can expose named slots for structured regions. The individual page lists exactly which slots exist and whether they receive slot props.

Do not invent slot names based on other UI libraries. Resux docs document only slots implemented by the current source.

## `v-model`

Input-like components that support Vue two-way binding generally use the standard contract:

```text
prop: modelValue
emit: update:modelValue
```

Example:

```vue
<script setup>
import { ref } from 'vue'
import { RxInput } from 'resuxjs/ui'

const name = ref('')
</script>

<template>
  <RxInput v-model="name" />
</template>
```

Conceptually Vue expands this to:

```vue
<RxInput
  :model-value="name"
  @update:model-value="name = $event"
/>
```

### Value conversion is component-specific

Do not assume every component preserves input types identically.

For example, native text input events naturally produce strings. A prop may accept `string | number`, but the emitted native input value can still be a string unless the component explicitly converts it.

The page for each form component calls out its actual behavior.

## Custom events

A component can declare custom emits, for example `update:modelValue` or a dismiss/change event.

If a component declares **no custom emits**, normal native listeners may still work through root attribute forwarding when appropriate:

```vue
<RxButton @click="save">Save</RxButton>
```

The difference matters when you are trying to understand whether an event is:

- a native DOM event forwarded through the component,
- or a custom component event intentionally emitted by its implementation.

## Internal state: controlled vs initialized

A prop named `open` does not automatically mean “fully controlled component.”

A component may copy an initial prop value into an internal Vue ref and then manage state locally. If it does not watch later prop changes or emit a corresponding update event, it is not a standard controlled `v-model` contract.

This is why the docs explicitly call out behavior such as:

- whether `open` is only an initial value,
- whether an `update:open` event exists,
- whether the component watches external changes,
- whether content stays mounted while hidden.

When state synchronization matters, verify the exact component page/source rather than assuming patterns from another design system.

## `unstyled`

Many UI components expose:

```ts
unstyled: boolean
```

For most primitives, `unstyled` means the component stops adding its normal `rx-*` classes while preserving your passed attributes/classes.

Example:

```vue
<RxButton unstyled class="my-button">
  Save
</RxButton>
```

### `unstyled` can also affect behavior in motion primitives

For `RxMotion`, `RxReveal`, and `RxAutoAnimate`, `unstyled` is currently also used as a gate that skips their mount animation.

So on those components it behaves more like **disable the built-in enhancement**, not only “remove CSS classes.”

This is exactly the kind of implementation-specific detail that the docs should make explicit.

## Styling model

When the UI module's built-in styles are enabled, primitives use stable class names such as:

```text
rx-btn
rx-btn-primary
rx-btn-md
rx-card
rx-badge-success
rx-input
```

Your own `class` is merged/preserved according to the component implementation.

### Tokens

The UI module accepts `tokens` and exports `defineUiTokens()`, but the current primitive stylesheet should not be assumed to convert arbitrary token keys into automatic CSS variables.

Treat tokens as typed/configured UI data unless a specific built-in style documents that it consumes a token.

Read [UI Package API](/reference/ui) for the module options.

## Motion model

The UI motion APIs use the browser Web Animations API where available.

Current built-in presets include:

- `fade-up`,
- `fade-down`,
- `scale-in`,
- `slide-in-left`,
- `slide-in-right`,
- `pulse-glow`,
- `bounce-in`.

`useAnimate()` builds keyframes and calls `element.animate()`.

### Reduced motion

`isReducedMotion()` checks:

```css
(prefers-reduced-motion: reduce)
```

and motion helpers/components that call it can skip animations when the user requests reduced motion.

### `RxMotion`

Runs the requested preset on mount.

### `RxReveal`

Also runs on mount. The current component does **not** mean “animate when entering viewport.”

### `vAnime` / `vAnimate`

These directives are the viewport-triggered path: they use `IntersectionObserver` when available, start the animation when intersecting, then unobserve/clean up.

### `RxAutoAnimate`

Despite the name, the current component runs a one-time `scale-in` animation on mount. It does not observe child insertion/removal/reordering/layout changes.

Read the motion component pages before choosing an API.

## Accessibility: name is not a guarantee

A production UI library component name can create expectations—“Modal must trap focus,” “Dropdown must implement arrow-key navigation,” and so on. The Resux UI primitives are deliberately small, so the source is the authority.

### Strong native foundations

Some components inherit useful platform behavior because they use native elements:

- Button → native button activation/disabled semantics.
- Input/Textarea → native form controls.
- DatePicker → native date input.
- Kbd → semantic keyboard notation.

### Custom widgets need inspection

Custom widgets such as Modal, Dropdown, Tooltip, Popover, Tabs, Select, and Accordion may not implement the complete keyboard/focus/ARIA patterns expected from mature headless UI libraries.

Each component page documents what is currently present and what your application must add/test.

### Do not rely on color alone

Visual variants such as `success`, `warning`, or `danger` must still communicate meaning through text or another accessible signal.

## SSR behavior

Vue UI components can participate in server rendering where the surrounding integration renders them, but their **interactive lifecycle still belongs to Vue**.

This distinction is useful:

```text
SSR-compatible ≠ resumable Resux primitive
```

A server-rendered Vue button can appear in HTML, but its Vue event/state semantics still require the Vue runtime boundary that owns it.

## Runtime cost

Think in terms of the **boundary**, not just the individual component.

If an existing Vue island already contains a form, adding `RxButton` and `RxInput` to that island does not create a second Vue runtime. But introducing a Vue island solely to render a static `RxBadge` creates a much larger runtime decision than the badge's own implementation suggests.

Ask:

1. Is this region already Vue-owned?
2. Does it need Vue state/events/lifecycle?
3. Could normal Resux/native HTML provide the same behavior?
4. Would a small Resux handler/client enhancement be a better fit?

## Component page standard

Every component page should answer these questions:

1. **What does it render?** Exact root/native element.
2. **When should I use it?** Real use cases and when native markup is better.
3. **How do I import it?** `Rx*` and alias if applicable.
4. **What are all props?** Type, default, behavior, verified variants.
5. **What events does it emit?** Custom vs native/fallthrough listeners.
6. **What slots exist?** Including slot props.
7. **Does it keep internal state?** Controlled/initial-value behavior.
8. **How is it styled?** Classes, `unstyled`, variants.
9. **What accessibility semantics exist?** And what is missing.
10. **What happens during SSR/browser mount?** Runtime ownership/cost.
11. **What are common recipes?** Realistic composition examples.
12. **What are current limitations?** No inferred capabilities.

This page exists so the catalog can use a consistent vocabulary rather than repeating the same architecture explanation without context.

## Choosing between native Resux markup and UI package components

| Need | Prefer |
| --- | --- |
| Static semantic content | Native/normal Resux markup |
| Small resumable application interaction supported by compiler | Normal Resux handler/state |
| Existing Vue-owned form/widget subtree | `resuxjs/ui` inside the island |
| Vue ecosystem component | Vue island |
| Imperative DOM package around existing HTML | Client enhancement/progressive package |
| SVG icon registry/provider/loading | `resuxjs/icons`, not `RxIcon` placeholder primitive |
| Resux-renderer image/video behavior | `ResuxImg` / `ResuxPicture` / `ResuxVideo` |

## Example: designing a settings panel

Suppose you need a settings panel with a name input, theme switch, save button, and a static account-status badge.

### If the whole panel is already a Vue island

Using:

```vue
<RxInput v-model="name" />
<RxSwitch v-model="darkMode" />
<RxButton @click="save">Save</RxButton>
<RxBadge variant="success">Active</RxBadge>
```

is coherent because one Vue boundary owns all of it.

### If the page is otherwise normal Resux

Ask whether the settings interactions can be implemented with normal Resux template/state/handlers. If yes, native inputs/buttons plus Resux resumability may preserve a smaller browser boundary.

Do not create a Vue island solely because the UI package offers matching visual primitives.

## Example: static article card

This:

```vue
<RxCard>
  <h2>Architecture Deep Dive</h2>
  <p>Learn how compiler, server, and browser runtime connect.</p>
</RxCard>
```

is fine inside an existing Vue UI subtree.

On a static Resux documentation/listing page, this is usually enough:

```html
<article class="card">
  <h2>Architecture Deep Dive</h2>
  <p>Learn how compiler, server, and browser runtime connect.</p>
</article>
```

The native `article` can even have stronger semantics than a generic `RxCard` `<div>`.

## Example: viewport animation

If you need mount animation:

```vue
<RxMotion preset="fade-up">
  <section>...</section>
</RxMotion>
```

If you specifically need a Vue directive that waits for viewport intersection, use the documented `vAnime` / `vAnimate` path rather than assuming `RxReveal` has that behavior.

If you need a non-Vue progressive animation, consider whether a normal Resux/client-enhancement approach is more appropriate for the page.

## Related

- [UI Components](/components/)
- [UI Package API](/reference/ui)
- [UI and Motion Guide](/guide/ui-animations)
- [Vue Islands](/guide/vue-islands)
- [Execution Contexts](/guide/execution-contexts)
- [Architecture Deep Dive](/guide/architecture-deep-dive)
