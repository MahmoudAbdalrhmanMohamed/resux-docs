# UI and Motion (`resuxjs/ui`)

The optional UI package exports a Resux build-time module, design-token helpers, Web Animations API utilities, Vue directives, and Vue runtime components.

::: warning Vue runtime package
The UI components are implemented with Vue `defineComponent`, `ref`, and `onMounted`. Use them in Vue islands or an explicit Vue/client runtime integration. They are not zero-hydration Resux template primitives.
:::

## Module configuration

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/ui', {
      css: ['/assets/css/ui-overrides.css'],
      defaultStyles: true,
      tokens: {
        accent: '#03c8bf',
        radius: '12px'
      },
      animations: {
        enabled: true,
        defaultPreset: 'fade-up'
      }
    }]
  ]
})
```

The module can add CSS and public token/animation configuration. Component imports remain explicit in Vue code.

## Tokens

```ts
import { defineUiTokens } from 'resuxjs/ui'

export const tokens = defineUiTokens({
  accent: '#03c8bf',
  surface: '#0f172a'
})
```

## Animation helper

```ts
import { useAnimate } from 'resuxjs/ui'

const animation = useAnimate(element, {
  type: 'fade-up',
  duration: 400,
  delay: 100,
  easing: 'ease-out',
  fill: 'forwards'
})
```

Built-in presets:

- `fade-up`
- `fade-down`
- `scale-in`
- `slide-in-left`
- `slide-in-right`
- `pulse-glow`
- `bounce-in`

`useAnimate` returns `null` when there is no browser element, Web Animations support is missing, or reduced motion is requested.

## Directive

`vAnime` and `vAnimate` are aliases. They trigger when an element enters the viewport when `IntersectionObserver` is available.

```vue
<div v-anime="{ type: 'fade-up', duration: 500 }">Content</div>
```

## Components

Both `Rx*` and matching `Resux*` aliases are exported:

### Forms

- `RxButton` / `ResuxButton`
- `RxInput` / `ResuxInput`
- `RxTextarea` / `ResuxTextarea`
- `RxSelect` / `ResuxSelect`
- `RxDatePicker` / `ResuxDatePicker`
- `RxSwitch` / `ResuxSwitch`

### Content and feedback

- `RxCard`, `RxBadge`, `RxAvatar`, `RxAlert`
- `RxSkeleton`, `RxDivider`, `RxKbd`

### Overlays and navigation

- `RxModal`, `RxDropdown`, `RxPopover`, `RxTooltip`
- `RxAccordion`, `RxTabs`

### Motion and icons

- `RxMotion`, `RxReveal`, `RxAutoAnimate`, `RxIcon`

## Example island

```vue
<script setup lang="ts">
import { RxButton, RxModal } from 'resuxjs/ui'
import { ref } from 'vue'

const open = ref(false)
</script>

<template>
  <RxButton @click="open = true">Open</RxButton>
  <RxModal v-if="open" @close="open = false">
    Modal content
  </RxModal>
</template>
```

## Accessibility

The primitives provide structure and defaults, but application code must still test keyboard navigation, labels, focus management, contrast, reduced motion, and screen-reader behavior for the exact composition used.
