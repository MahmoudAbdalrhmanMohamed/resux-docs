# UI Components

`resuxjs/ui` is Resux's optional Vue UI and motion package. This section is the component catalog; every public component has its own page with its actual props, emitted events, slots, styling hooks, accessibility behavior, and runtime cost.

::: warning Vue runtime boundary
The components exported by `resuxjs/ui` are Vue `defineComponent` components. They belong inside a [Vue island](/guide/vue-islands) or another explicit Vue runtime boundary. They are **not** zero-hydration Resux template primitives. Use normal Resux templates when you do not need Vue-owned state or event handling.
:::

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
| [Card](./card.md) | Grouped content | Non-interactive container |
| [Badge](./badge.md) | Status/category labels | Non-interactive inline content |
| [Avatar](./avatar.md) | Identity image/fallback initials | Uses a native `<img>` when `src` is provided |
| [Alert](./alert.md) | Important feedback | Renders `role="alert"`; optional dismiss event |
| [Skeleton](./skeleton.md) | Visual loading placeholder | Default shimmer does not currently suppress itself for reduced motion |
| [Divider](./divider.md) | Visual separation | Visual primitive; no automatic separator ARIA role |
| [Kbd](./kbd.md) | Keyboard key notation | Renders semantic `<kbd>` |

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

`unstyled` removes Resux-generated component classes; attributes and your own `class` still pass through. `tokens` are stored under public runtime UI configuration, but the current primitive CSS does not automatically translate arbitrary token keys into CSS variables. Treat `defineUiTokens()` as a typed configuration helper, not as proof that every token changes built-in CSS.

## SSR, resumability, and hydration

The key distinction is ownership:

- **Resux template primitives** such as `ResuxImg`, `ResuxPicture`, and `ResuxVideo` are handled by the Resux renderer and can preserve Resux's resumable/progressive model.
- **`resuxjs/ui` components** are Vue components. Their server-renderable markup may appear during SSR, but their Vue state, emitted events, mount hooks, and motion behavior need the Vue runtime boundary that owns them.
- Non-interactive UI components such as Card, Badge, Divider, Kbd, Skeleton, and Avatar have little client behavior themselves, but using them through a Vue island still incurs that island's Vue runtime cost.
- Interactive components such as Select, Switch, Popover, Dropdown, Tabs, Accordion, Tooltip, Modal, Input, and Textarea rely on Vue event/state behavior for interaction.

Read [Vue Islands](/guide/vue-islands), [Execution Contexts](/guide/execution-contexts), and [Rendering Lifecycle](/guide/rendering-lifecycle) before using a large Vue-owned UI subtree.

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

- [UI and Motion guide](/guide/ui-animations)
- [Vue Islands](/guide/vue-islands)
- [Icons](/icons/)
- [Images and Media](/media/)
- [CSS and Tailwind](/guide/css-tailwind)
- [Accessibility and current limits](/reference/limits)
