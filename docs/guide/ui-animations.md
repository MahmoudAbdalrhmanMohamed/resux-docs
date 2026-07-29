# UI & Motion Primitives (`resuxjs/ui`)

The `resuxjs/ui` module equips Resux applications with a full suite of Nuxt UI-inspired primitive components, accessible controls, motion primitives respecting `prefers-reduced-motion`, a Web Animations API (WAAPI) engine (`useAnimate`), scroll-reveal directive (`v-anime`), user-controlled default styling, and customizable design tokens.

## Overview

- **UI & Motion Components**: Comprehensive library including `<ResuxSelect>`, `<ResuxDatePicker>`, `<ResuxPopover>`, `<ResuxIcon>`, `<ResuxReveal>`, `<ResuxAutoAnimate>`, `RxAvatar`, `RxAlert`, `RxAccordion`, `RxTooltip`, `RxDropdown`, `RxTabs`, `RxSwitch`, `RxSkeleton`, `RxDivider`, `RxKbd`, `RxButton`, `RxCard`, `RxBadge`, `RxInput`, `RxModal`.
- **Dual Component Aliases**: Exported with both `Rx*` (e.g. `RxSelect`) and `Resux*` (e.g. `ResuxSelect`) names for flexibility.
- **Accessible & Motion-Aware**: Features keyboard navigation and automatic `prefers-reduced-motion: reduce` detection for motion components.
- **User-Controlled Styling**: Default styles are applied automatically unless disabled via configuration (`defaultStyles: false`) or overriden on individual components using the `unstyled` prop.

## Module Configuration

Enable and configure the UI & Motion Primitives module in `resux.config.ts`:

```ts
export default defineResuxConfig({
  modules: [
    ["resuxjs/ui", {
      defaultStyles: true, // Set to false to omit default primitive CSS styles
      tokens: {
        accent: "#03C8BF",
        heroOverlay: "rgba(0,0,0,0.55)"
      },
      animations: {
        enabled: true,
        defaultPreset: "fade-up"
      }
    }]
  ]
})
```

> [!NOTE]
> If `defaultStyles: false` is configured, Resux will not inject the default UI primitive CSS stylesheet into the document head, allowing full custom styling control via Tailwind CSS or custom stylesheet imports.

## UI & Motion Primitive Components

Import primitive components directly from `resuxjs/ui`:

```vue
<template>
  <ResuxCard variant="glass">
    <h2>Dashboard</h2>

    <ResuxAlert variant="success" title="System Status" dismissible>
      All systems operating normally.
    </ResuxAlert>

    <ResuxAvatar src="/user.jpg" alt="Alex" size="md" status="online" />

    <ResuxSelect
      v-model="role"
      :options="['Admin', 'Editor', 'Viewer']"
      placeholder="Select role"
    />

    <ResuxDatePicker v-model="selectedDate" />

    <ResuxSwitch v-model="notificationsEnabled" />

    <ResuxReveal preset="fade-up">
      <ResuxButton variant="primary">Save Preferences</ResuxButton>
    </ResuxReveal>
  </ResuxCard>
</template>

<script setup>
import { ref } from "vue"
import {
  ResuxCard,
  ResuxAlert,
  ResuxAvatar,
  ResuxSelect,
  ResuxDatePicker,
  ResuxSwitch,
  ResuxButton,
  ResuxReveal
} from "resuxjs/ui"

const role = ref("Admin")
const selectedDate = ref("2026-07-25")
const notificationsEnabled = ref(true)
</script>
```

### Component Reference

| Component | Description | Key Props |
| :--- | :--- | :--- |
| `<ResuxSelect>` / `<RxSelect>` | Accessible custom select control with keyboard navigation (`ArrowUp`/`Down`, `Enter`, `Escape`) | `v-model`, `options`, `placeholder`, `disabled`, `unstyled` |
| `<ResuxDatePicker>` / `<RxDatePicker>` | Date & range picker component with Date payload revival and timezone support | `v-model`, `placeholder`, `unstyled` |
| `<ResuxPopover>` / `<RxPopover>` | Accessible popup trigger and floating layer wrapper | `open` (`v-model:open`), `unstyled` |
| `<ResuxIcon>` / `<RxIcon>` | Headless icon renderer | `name`, `size`, `color`, `unstyled` |
| `<ResuxReveal>` / `<RxReveal>` | Motion primitive respecting `prefers-reduced-motion` settings | `preset`, `duration`, `unstyled` |
| `<ResuxAutoAnimate>` / `<RxAutoAnimate>` | Layout motion container respecting `prefers-reduced-motion` settings | `duration`, `unstyled` |
| `<ResuxAvatar>` / `<RxAvatar>` | Profile picture with fallback initials, status dot, and size variants | `src`, `alt`, `size`, `status`, `unstyled` |
| `<ResuxAlert>` / `<RxAlert>` | Notification banner with variants (`info`, `success`, `warning`, `danger`) | `variant`, `title`, `dismissible`, `unstyled` |
| `<ResuxAccordion>` / `<RxAccordion>` | Collapsible accordion item | `title`, `open`, `unstyled` |
| `<ResuxTooltip>` / `<RxTooltip>` | Hover/focus tooltip overlay | `text`, `placement`, `unstyled` |
| `<ResuxDropdown>` / `<RxDropdown>` | Popup action menu dropdown | `items`, `open`, `unstyled` |
| `<ResuxTabs>` / `<RxTabs>` | Tabbed navigation bar switcher | `items`, `v-model`, `unstyled` |
| `<ResuxTextarea>` / `<RxTextarea>` | Multi-line text input | `v-model`, `rows`, `placeholder`, `unstyled` |
| `<ResuxSwitch>` / `<RxSwitch>` | Accessible boolean toggle switch | `v-model`, `disabled`, `unstyled` |
| `<ResuxSkeleton>` / `<RxSkeleton>` | Shimmer placeholder loading state | `width`, `height`, `rounded`, `unstyled` |
| `<ResuxDivider>` / `<RxDivider>` | Separator line with optional text label | `label`, `orientation`, `unstyled` |
| `<ResuxKbd>` / `<RxKbd>` | Keyboard key indicator badge | `unstyled` |

### Unstyled & Custom Style Overrides

Every UI primitive supports the `unstyled` prop and standard `class` / `style` attributes. When `unstyled` is `true`, default framework CSS classes are omitted:

```vue
<!-- Custom Tailwind CSS styling without default framework styles -->
<ResuxButton unstyled class="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700">
  Custom Styled Button
</ResuxButton>
```

## `v-anime` Vue Directive

Apply scroll-triggered entrance transitions directly to elements or components in SFC templates:

```vue
<template>
  <!-- Simple preset directive -->
  <div v-anime="'fade-up'">
    <h2>Title</h2>
  </div>

  <!-- Customized animation object -->
  <button v-anime="{ type: 'scale-in', duration: 500, delay: 100 }">
    Interactive Button
  </button>
</template>
```

## `useAnimate` Composable

Programmatically animate elements using WAAPI:

```ts
import { ref } from "vue"
import { useAnimate } from "resuxjs/ui"

const cardRef = ref<HTMLElement | null>(null)

function triggerCardAnimation() {
  useAnimate(cardRef, {
    type: "pulse-glow",
    duration: 600,
    easing: "cubic-bezier(0.16, 1, 0.3, 1)"
  })
}
```

## Motion Presets Reference

| Preset | Keyframe Transform | Easing |
| :--- | :--- | :--- |
| `fade-up` | `translate3d(0, 30px, 0)` -> `translate3d(0, 0, 0)` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `fade-down` | `translate3d(0, -30px, 0)` -> `translate3d(0, 0, 0)` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `scale-in` | `scale3d(0.92, 0.92, 1)` -> `scale3d(1, 1, 1)` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `slide-in-left` | `translate3d(-40px, 0, 0)` -> `translate3d(0, 0, 0)` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `slide-in-right` | `translate3d(40px, 0, 0)` -> `translate3d(0, 0, 0)` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `pulse-glow` | `scale(1)` -> `scale(1.03)` with box-shadow pulse | `ease-in-out` |
| `bounce-in` | `scale3d(0.3, 0.3, 0.3)` -> `scale3d(1.05, 1.05, 1.05)` -> `scale3d(1, 1, 1)` | `cubic-bezier(0.175, 0.885, 0.32, 1.275)` |


