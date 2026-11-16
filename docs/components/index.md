# UI Components (`resuxjs/ui` & Framework Primitives)

Resux ships a complete, dependency-free suite of **25 UI components** in `resuxjs/ui` (`Rx*` and `Resux*` aliases), plus the modular `<Icon>` component in `resuxjs/icons` and the built-in `<Teleport>` and `<Transition>` framework primitives.

Every component page in this section includes a **Live Interactive UI Preview ("See How It Looks")**, runnable Vue SFC examples, rendered DOM (`rx-*`) inspection, and full TypeScript prop tables.

<RxComponentPreview component="RxButton" title="Interactive UI Suite Preview — Try Variants & Sizes" />

## Quick Import

```ts
import {
  RxButton,
  RxInput,
  RxTextarea,
  RxSelect,
  RxDatePicker,
  RxSwitch,
  RxVerificationCode,
  RxCard,
  RxBadge,
  RxAvatar,
  RxAlert,
  RxSkeleton,
  RxDivider,
  RxKbd,
  RxAccordion,
  RxTabs,
  RxPopover,
  RxDropdown,
  RxTooltip,
  RxModal,
  RxMotion,
  RxReveal,
  RxAutoAnimate,
  RxIcon
} from 'resuxjs/ui'
```

## Component Catalog by Category

### Actions & Form Controls

- **[`RxButton` (`/components/button`)](/components/button)** — Accessible action button primitive with semantic variants, three sizes, disabled state handling, and optional unstyled mode.
- **[`RxInput` (`/components/input`)](/components/input)** — Two-way bound single-line input control (`v-model`) supporting text, email, password, number, search, and url types with `inheritAttrs: false`.
- **[`RxTextarea` (`/components/textarea`)](/components/textarea)** — Multi-line text input primitive with configurable row height, `v-model` binding, and shared `rx-input rx-textarea` styling.
- **[`RxSelect` (`/components/select`)](/components/select)** — Accessible native `<select>` wrapper supporting string arrays or `{ label, value, disabled }` option objects with a custom chevron indicator.
- **[`RxDatePicker` (`/components/date-picker`)](/components/date-picker)** — Native HTML5 date input control (`type="date"`) with `v-model` support and consistent `rx-input rx-datepicker` styling.
- **[`RxSwitch` (`/components/switch`)](/components/switch)** — Accessible WAI-ARIA toggle switch (`role="switch"`) with `aria-checked`, `data-state="checked|unchecked"`, and animated thumb element.
- **[`RxVerificationCode` (`/components/verification-code`)](/components/verification-code)** — Interactive multi-cell OTP / 2FA verification code input (`1..12` cells) with numeric/alphanumeric filtering, paste handling, masking, and choreographed `verifying` / `success` / `error` status transitions.

### Surfaces & Layout Structure

- **[`RxCard` (`/components/card`)](/components/card)** — Surface container primitive for grouping metrics, forms, and settings panels with optional visual variants (`default`, `elevated`, `outlined`, `subtle`).
- **[`RxDivider` (`/components/divider`)](/components/divider)** — Horizontal or vertical visual separator line with optional centered text label.
- **[`RxAccordion` (`/components/accordion`)](/components/accordion)** — Collapsible disclosure panel with internal toggle state initialized from the `open` prop and `+` / `-` indicator.
- **[`RxTabs` (`/components/tabs`)](/components/tabs)** — Controlled horizontal tab bar (`v-model`) that renders `.rx-tab-btn` triggers from an `items` array of `{ label, key }` objects.
- **[`RxKbd` (`/components/kbd`)](/components/kbd)** — Semantic `<kbd>` keyboard shortcut keycap primitive for command palettes, hotkeys, and CLI documentation.

### Identity & Data Display

- **[`RxAvatar` (`/components/avatar`)](/components/avatar)** — User or team identity avatar that renders an image when `src` is provided or automatically falls back to uppercase initials from `alt`, with optional presence status dot.
- **[`RxBadge` (`/components/badge`)](/components/badge)** — Compact inline status pill for version tags, build states, and metric indicators.
- **[`RxSkeleton` (`/components/skeleton`)](/components/skeleton)** — Animated shimmer placeholder block with configurable `width`, `height`, and `rounded` radius for async loading states.
- **[`RxIcon` (`/components/icon`)](/components/icon)** — Covers both the lightweight `RxIcon` text placeholder primitive (`[name]`) in `resuxjs/ui` and the full `<Icon>` SVG/CSS-mask component in `resuxjs/icons` with compile-time static inlining.

### Overlays & Dialogs

- **[`RxModal` (`/components/modal`)](/components/modal)** — Dialog overlay with backdrop click dismissal (`@click.self`), optional `<h3>` title header, and `update:open` / `close` events.
- **[`RxPopover` (`/components/popover`)](/components/popover)** — Floating contextual overlay with a customizable `#trigger` slot, internal open state synced with `:open`, and `update:open` emission.
- **[`RxDropdown` (`/components/dropdown`)](/components/dropdown)** — Action menu overlay driven by an `items` array of `{ label, action }` objects that automatically closes and invokes `item.action()` on selection.
- **[`RxTooltip` (`/components/tooltip`)](/components/tooltip)** — Hover-activated floating hint bubble supporting `top`, `bottom`, `left`, and `right` placements.

### Feedback & Motion Enhancements

- **[`RxAlert` (`/components/alert`)](/components/alert)** — Accessible status callout banner (`role="alert"`) with semantic variants (`info`, `success`, `warning`, `error`), optional title, and dismiss button.
- **[`RxMotion` (`/components/motion`)](/components/motion)** — Web Animations API wrapper component that animates its root tag on mount using `useAnimate` presets (`fade-in`, `fade-up`, `fade-down`, `slide-left`, `slide-right`, `zoom-in`, `zoom-out`) while respecting `prefers-reduced-motion`.
- **[`RxReveal` (`/components/reveal`)](/components/reveal)** — Scroll-triggered viewport entrance wrapper powered by `IntersectionObserver` (`threshold: 0.1`) that hides content (`opacity: 0`) until scrolled into view and then plays the configured preset.
- **[`RxAutoAnimate` (`/components/auto-animate`)](/components/auto-animate)** — Zero-config mount & list container animation wrapper (`scale-in` on mount) for dynamic queues, tag lists, and notification stacks.

### Built-in Framework Primitives

- **[`Teleport` (`/components/teleport`)](/components/teleport)** — Nuxt/Vue-compatible `<Teleport to="#selector">` primitive that injects server-rendered HTML into target containers (`body`, `#modals`, `#notifications`) and resumes event handlers across DOM boundaries.
- **[`Transition` (`/components/transition`)](/components/transition)** — Built-in `<Transition>` primitive applying CSS enter/leave classes (`{name}-enter-from`, `{name}-enter-active`, `{name}-leave-to`) when child elements are inserted/removed via `v-if` or have their display state toggled via `v-show`.
