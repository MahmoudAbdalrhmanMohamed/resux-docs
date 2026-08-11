# UI Components

`resuxjs/ui` is Resux's optional Vue UI and motion package. This section is the component catalog; every public component has its own page with its actual props, emitted events, slots, styling hooks, accessibility behavior, runtime cost, examples, and current limitations.

::: warning Vue runtime boundary
The components exported by `resuxjs/ui` are Vue `defineComponent` components. They belong inside a [Vue island](/guide/vue-islands) or another explicit Vue runtime boundary. They are **not** zero-hydration Resux template primitives. Use normal Resux templates when you do not need Vue-owned state or event handling.
:::

## Before choosing a component

Read [Component Anatomy](./component-anatomy.md) once before working through the catalog. It explains the repeated model behind these pages:

- why `resuxjs/ui` is a Vue boundary even when a primitive itself is static,
- how props, native attrs, custom events, slots, and `v-model` are implemented,
- how to distinguish an accepted string prop from a variant that actually has built-in CSS,
- what `unstyled` does,
- how mount animations and reduced motion work,
- why root/native elements matter for accessibility,
- how to decide between an `Rx*` component and normal Resux/native HTML.

A component name is **not** a promise of design-system-level behavior. The individual page documents the current source. For example, a component named Modal or Dropdown must not be assumed to include focus trapping or complete keyboard navigation unless the implementation actually provides it.

## How to read each page

The detailed component pages answer the same practical questions wherever they apply:

1. **What does it render?** Root/native element and structure.
2. **When should I use it?** Including when native Resux HTML is better.
3. **How do I import it?** `Rx*` plus matching alias.
4. **What are every prop/default and verified variant?**
5. **Which events are custom vs native/fallthrough listeners?**
6. **Which slots exist?**
7. **Does it keep internal state or support `v-model`?**
8. **How do built-in classes and `unstyled` work?**
9. **Which accessibility behaviors exist and which are application-owned?**
10. **What happens during SSR/browser mount?**
11. **What does it cost if it creates/requires a Vue boundary?**
12. **What are the current limitations and common mistakes?**

That standard is intentionally more demanding than a one-line component catalog.

## Install and enable

`resuxjs/ui` ships with the `resuxjs` package; there is no separate UI dependency.

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/ui', {
      defaultStyles: true,
      animations: {
        enabled: true,
        defaultPreset: 'fade-up'
      }
    }]
  ]
})
```

Import components from the package entry point:

```ts
import { RxButton, RxInput, RxModal } from 'resuxjs/ui'
```

Every `Rx*` component has a matching `Resux*` alias that points to the same component object. For example, `RxButton === ResuxButton`.

## Forms and input

| Component | Use it for | Runtime note |
| --- | --- | --- |
| [Button](./button.md) | Native button actions | Vue event handling when listeners are attached |
| [Input](./input.md) | Single-line input with `v-model` | Emits `update:modelValue` from the native input event |
| [Textarea](./textarea.md) | Multi-line text input | Emits `update:modelValue` |
| [Select](./select.md) | Small custom option picker | Custom keyboard handling; see accessibility limitations |
| [DatePicker](./date-picker.md) | Native date selection | Renders `<input type="date">` |
| [Switch](./switch.md) | Boolean on/off state | Button semantics plus `role="switch"` |

## Content and feedback

| Component | Use it for | Notes |
| --- | --- | --- |
| [Card](./card.md) | Grouped visual content | Non-interactive `<div>` container; choose stronger native semantics when appropriate |
| [Badge](./badge.md) | Status/category labels | Non-interactive inline content; do not rely on color alone |
| [Avatar](./avatar.md) | Identity image/fallback initials | Uses a native `<img>` when `src` is provided |
| [Alert](./alert.md) | Important feedback | Renders `role="alert"`; optional dismiss event |
| [Skeleton](./skeleton.md) | Visual loading placeholder | Default shimmer does not currently suppress itself for reduced motion |
| [Divider](./divider.md) | Visual separation | No automatic separator ARIA role; built-in vertical style is not implied |
| [Kbd](./kbd.md) | Keyboard key notation | Renders semantic `<kbd>`; it is not an interactive shortcut system |

## Disclosure, navigation, and overlays

| Component | Use it for | Important limitation |
| --- | --- | --- |
| [Accordion](./accordion.md) | Simple local disclosure | `open` initializes internal state; it is not a controlled `v-model` API |
| [Tabs](./tabs.md) | Selecting a tab key | Renders tab buttons only; panel rendering is application-owned |
| [Popover](./popover.md) | Click-toggled floating content | No built-in focus management or outside-click behavior |
| [Dropdown](./dropdown.md) | Small action menu | No arrow-key menu navigation/focus management |
| [Tooltip](./tooltip.md) | Pointer-hover supplemental text | Hover-only in the current implementation; do not rely on it for required information |
| [Modal](./modal.md) | Simple overlay content | No built-in focus trap, Escape handling, or dialog ARIA contract |

## Motion

| Component/API | Behavior |
| --- | --- |
| [Motion](./motion.md) | Runs a configured Web Animations preset on mount |
| [Reveal](./reveal.md) | Runs a preset on mount; despite the name it is not viewport-observed |
| [AutoAnimate](./auto-animate.md) | Runs a one-time `scale-in` animation on mount; it does not observe child-list/layout changes |
| [`useAnimate()`](/reference/ui#useanimate-element-options) | Imperative Web Animations helper |
| [`vAnime` / `vAnimate`](/reference/ui#vanime-vanimate) | IntersectionObserver-based Vue directive |

## UI icon primitive

[RxIcon](./icon.md) is a small UI primitive that renders a text placeholder such as `[check]`. It is **not** the full SVG icon system.

For the SVG registry, remote Iconify-compatible loading, caching, and lazy loading, use [`Icon` / `ResuxIcon` from `resuxjs/icons`](/icons/).

## Styling model

When `defaultStyles` is enabled, the UI module injects its built-in primitive CSS into document head output. Components append stable `rx-*` classes unless `unstyled` is true.

```vue
<RxButton class="my-save-button">Save</RxButton>
<RxButton unstyled class="my-button">Headless styling</RxButton>
```

`unstyled` removes Resux-generated component classes; attributes and your own `class` still pass through. For motion primitives, read their pages carefully because `unstyled` also gates their mount animation behavior.

`tokens` are stored under public runtime UI configuration, but the current primitive CSS does not automatically translate arbitrary token keys into CSS variables. Treat `defineUiTokens()` as a typed configuration helper, not as proof that every token changes built-in CSS.

## SSR, resumability, and hydration

The key distinction is ownership:

- **Resux template primitives** such as `ResuxImg`, `ResuxPicture`, and `ResuxVideo` are handled by the Resux renderer and can preserve Resux's resumable/progressive model.
- **`resuxjs/ui` components** are Vue components. Their server-renderable markup may appear during SSR, but their Vue state, emitted events, mount hooks, and motion behavior need the Vue runtime boundary that owns them.
- Non-interactive UI components such as Card, Badge, Divider, Kbd, Skeleton, and Avatar have little client behavior themselves, but using them through a Vue island still incurs that island's Vue runtime cost.
- Interactive components such as Select, Switch, Popover, Dropdown, Tabs, Accordion, Tooltip, Modal, Input, and Textarea rely on Vue event/state behavior for interaction.

Read [Vue Islands](/guide/vue-islands), [Execution Contexts](/guide/execution-contexts), [Rendering Lifecycle](/guide/rendering-lifecycle), and [Architecture Deep Dive](/guide/architecture-deep-dive) before using a large Vue-owned UI subtree.

## Accessibility baseline

The source code is the source of truth, not component names. Some primitives use useful native semantics (`button`, `input`, `textarea`, `kbd`, `role="switch"`, `role="alert"`), while several custom overlays/navigation widgets are intentionally small and do **not** implement the complete WAI-ARIA interaction patterns expected from a production design-system widget.

Each component page calls out the exact current behavior and what the application must add or test. Do not infer keyboard navigation, focus trapping, accessible names, or ARIA state that the implementation does not provide.

## Package-level APIs

The UI package also exports:

- `ResuxUiModuleOptions`
- `defineUiTokens()`
- `AnimationPreset`
- `AnimateOptions`
- `isReducedMotion()`
- `useAnimate()`
- `vAnime`
- `vAnimate`
- the default UI module

See the [UI package reference](/reference/ui) for these APIs.

## Related

- [Component Anatomy](./component-anatomy.md)
- [UI and Motion guide](/guide/ui-animations)
- [Vue Islands](/guide/vue-islands)
- [Icons](/icons/)
- [Images and Media](/media/)
- [CSS and Tailwind](/guide/css-tailwind)
- [Accessibility and current limits](/reference/limits)
