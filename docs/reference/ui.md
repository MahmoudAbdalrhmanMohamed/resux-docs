# UI API Reference (`resuxjs/ui`)

`resuxjs/ui` is an optional Vue-runtime UI and motion package. The components are Vue `defineComponent` components, so use them inside a [Vue island](../guide/vue-islands.md) or another explicit Vue runtime boundary. They are not zero-hydration Resux template primitives.

Every `Rx*` component has a matching `Resux*` alias. For example, `RxDatePicker` and `ResuxDatePicker` are the same component.

## Imports

```ts
import {
  RxButton,
  RxDatePicker,
  RxModal,
  defineUiTokens,
  useAnimate,
  vAnime
} from 'resuxjs/ui'
```

## Module setup

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/ui', {
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

Set `unstyled` on a component when you want its behavior/markup without Resux's default component class.

## Package-level APIs

### `defineUiTokens(tokens)`

Identity helper for defining UI tokens with type inference.

```ts
const tokens = defineUiTokens({
  accent: '#03c8bf',
  surface: '#0f172a'
})
```

### `isReducedMotion()`

Returns whether the current browser requests reduced motion. Browser-only motion code should respect this result.

### `useAnimate(element, options)`

Runs a Web Animations API preset and returns the `Animation` instance or `null` when animation cannot/should not run.

Common options:

- `type`: animation preset
- `duration`: milliseconds
- `delay`: milliseconds
- `easing`
- `fill`

Built-in presets include `fade-up`, `fade-down`, `scale-in`, `slide-in-left`, `slide-in-right`, `pulse-glow`, and `bounce-in`.

### `vAnime` / `vAnimate`

Vue directive aliases that animate an element when it enters the viewport when `IntersectionObserver` is available. Directive cleanup disconnects the observer and cancels the active animation when the element is unmounted.

## Form components

### `RxButton` / `ResuxButton`

Button primitive.

Key props:

| Prop | Type | Default |
| --- | --- | --- |
| `variant` | `string` | `'primary'` |
| `size` | `string` | `'md'` |
| `type` | `string` | `'button'` |
| `disabled` | `boolean` | `false` |
| `unstyled` | `boolean` | `false` |

Normal button attributes and listeners are forwarded.

```vue
<RxButton variant="primary" :disabled="saving" @click="save">
  Save
</RxButton>
```

### `RxInput` / `ResuxInput`

Text/input primitive with `v-model` support.

| Prop | Type | Default |
| --- | --- | --- |
| `modelValue` | `string \| number` | `''` |
| `type` | `string` | `'text'` |
| `placeholder` | `string` | `''` |
| `disabled` | `boolean` | `false` |
| `unstyled` | `boolean` | `false` |

Emits `update:modelValue` from the underlying input event.

```vue
<RxInput v-model="email" type="email" placeholder="you@example.com" />
```

### `RxTextarea` / `ResuxTextarea`

| Prop | Type | Default |
| --- | --- | --- |
| `modelValue` | `string` | `''` |
| `rows` | `number` | `3` |
| `placeholder` | `string` | `''` |
| `disabled` | `boolean` | `false` |
| `unstyled` | `boolean` | `false` |

Emits `update:modelValue`.

### `RxSelect` / `ResuxSelect`

Custom select primitive.

| Prop | Type | Default |
| --- | --- | --- |
| `modelValue` | `string \| number` | `''` |
| `options` | `(string \| { label: string; value: string \| number })[]` | `[]` |
| `placeholder` | `string` | `'Select an option'` |
| `disabled` | `boolean` | `false` |
| `unstyled` | `boolean` | `false` |

Emits `update:modelValue` when an option is selected.

```vue
<RxSelect
  v-model="role"
  :options="[
    { label: 'Admin', value: 'admin' },
    { label: 'Editor', value: 'editor' }
  ]"
/>
```

### `RxDatePicker` / `ResuxDatePicker`

Date input primitive. This is the built-in choice when you only need a standard calendar/date field and do not need a third-party calendar library.

| Prop | Type | Default |
| --- | --- | --- |
| `modelValue` | `string \| Date` | `''` |
| `placeholder` | `string` | `'Select date'` |
| `unstyled` | `boolean` | `false` |

Emits `update:modelValue` with the input's ISO-style `YYYY-MM-DD` string.

`Date` values are formatted for the native `<input type="date">`. Invalid `Date` objects are treated as an empty input instead of throwing, and current prop changes are reflected on subsequent renders.

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxDatePicker } from 'resuxjs/ui'

const birthday = ref('')
</script>

<template>
  <label>
    Birthday
    <RxDatePicker v-model="birthday" />
  </label>
  <p v-if="birthday">Selected: {{ birthday }}</p>
</template>
```

For date ranges, time selection, locale-specific calendars, or advanced disabled-date rules, use a progressive third-party integration; see the [Integration Cookbook](../guide/integration-cookbook.md#date-pickers).

### `RxSwitch` / `ResuxSwitch`

| Prop | Type | Default |
| --- | --- | --- |
| `modelValue` | `boolean` | `false` |
| `disabled` | `boolean` | `false` |
| `unstyled` | `boolean` | `false` |

Emits `update:modelValue` with the toggled boolean value.

## Content and feedback

### `RxCard` / `ResuxCard`

Container primitive. Key props: `variant` (`'default'`) and `unstyled` (`false`). Default slot contains card content.

### `RxBadge` / `ResuxBadge`

Inline badge. Key props: `variant` (`'default'`) and `unstyled` (`false`).

### `RxAvatar` / `ResuxAvatar`

Avatar/image primitive.

| Prop | Type | Default |
| --- | --- | --- |
| `src` | `string` | `''` |
| `alt` | `string` | `'Avatar'` |
| `size` | `string` | `'md'` |
| `status` | `string` | `''` |

Always provide a meaningful `alt` value when the image conveys identity or content.

### `RxAlert` / `ResuxAlert`

Feedback block.

| Prop | Type | Default |
| --- | --- | --- |
| `variant` | `string` | `'info'` |
| `title` | `string` | `''` |
| `dismissible` | `boolean` | `false` |
| `unstyled` | `boolean` | `false` |

Use alert text that remains understandable without animation or color alone.

### `RxSkeleton` / `ResuxSkeleton`

Loading placeholder.

| Prop | Type | Default |
| --- | --- | --- |
| `width` | `string` | `'100%'` |
| `height` | `string` | `'1rem'` |
| `rounded` | `string` | `'0.375rem'` |
| `unstyled` | `boolean` | `false` |

Skeletons are visual hints; expose real loading state through accessible text/ARIA where the user needs it.

### `RxDivider` / `ResuxDivider`

| Prop | Type | Default |
| --- | --- | --- |
| `label` | `string` | `''` |
| `orientation` | `string` | `'horizontal'` |
| `unstyled` | `boolean` | `false` |

### `RxKbd` / `ResuxKbd`

Keyboard-key visual primitive. It accepts the default slot and `unstyled`.

```vue
<RxKbd>Ctrl</RxKbd> + <RxKbd>K</RxKbd>
```

## Overlays and navigation

### `RxModal` / `ResuxModal`

| Prop | Type | Default |
| --- | --- | --- |
| `open` | `boolean` | `false` |
| `title` | `string` | `''` |
| `unstyled` | `boolean` | `false` |

Emits `update:open` and `close` when it closes.

```vue
<RxModal v-model:open="open" title="Delete item" @close="onClosed">
  Confirm the destructive action here.
</RxModal>
```

Application code must test focus trapping/restoration, escape behavior, background interaction, and screen-reader labeling for its exact modal composition.

### `RxPopover` / `ResuxPopover`

Props: `open` (`boolean`, default `false`) and `unstyled`. Emits `update:open`. Use the `trigger` slot for the activator and the default slot for popover content.

### `RxDropdown` / `ResuxDropdown`

| Prop | Type | Default |
| --- | --- | --- |
| `items` | `{ label: string; action?: () => void }[]` | `[]` |
| `open` | `boolean` | `false` |
| `unstyled` | `boolean` | `false` |

Emits `update:open`. An item's optional `action` is called when selected.

### `RxTooltip` / `ResuxTooltip`

Props: `text` (`''`), `placement` (`'top'`), and `unstyled`. Tooltips must not be the only place essential information appears.

### `RxAccordion` / `ResuxAccordion`

Props: `title` (`'Accordion Title'`), `open` (`false`), and `unstyled`. The component keeps its own open state initialized from `open`; use it for simple disclosure content rather than as a controlled state primitive.

### `RxTabs` / `ResuxTabs`

| Prop | Type | Default |
| --- | --- | --- |
| `items` | `{ label: string; key: string }[]` | `[]` |
| `modelValue` | `string` | `''` |
| `unstyled` | `boolean` | `false` |

Emits `update:modelValue` when a tab button is selected.

## Motion components

### `RxMotion` / `ResuxMotion`

Animation wrapper. Key props include `tag` (`'div'`), `preset` (`'fade-up'`), `duration` (`400`), and `delay` (`0`). Use this when a Vue island owns the animated subtree.

### `RxReveal` / `ResuxReveal`

Visibility-triggered reveal wrapper. Key props: `preset` (`'fade-up'`), `duration` (`400`), and `unstyled`.

### `RxAutoAnimate` / `ResuxAutoAnimate`

Wrapper for animating child-list/layout changes. Key props: `duration` (`300`) and `unstyled`.

## Icon component

### `RxIcon` / `ResuxIcon`

| Prop | Type | Default |
| --- | --- | --- |
| `name` | `string` | `'check'` |
| `size` | `string \| number` | `'1.25rem'` |
| `color` | `string` | `'currentColor'` |
| `unstyled` | `boolean` | `false` |

For the larger icon registry/provider system, see [Icons](../guide/icons.md) and the `resuxjs/icons` package.

## Alias list

The package exports these equivalent names:

- `RxMotion` / `ResuxMotion`
- `RxReveal` / `ResuxReveal`
- `RxAutoAnimate` / `ResuxAutoAnimate`
- `RxButton` / `ResuxButton`
- `RxCard` / `ResuxCard`
- `RxBadge` / `ResuxBadge`
- `RxInput` / `ResuxInput`
- `RxSelect` / `ResuxSelect`
- `RxDatePicker` / `ResuxDatePicker`
- `RxPopover` / `ResuxPopover`
- `RxIcon` / `ResuxIcon`
- `RxAvatar` / `ResuxAvatar`
- `RxAlert` / `ResuxAlert`
- `RxAccordion` / `ResuxAccordion`
- `RxTooltip` / `ResuxTooltip`
- `RxDropdown` / `ResuxDropdown`
- `RxTabs` / `ResuxTabs`
- `RxTextarea` / `ResuxTextarea`
- `RxSwitch` / `ResuxSwitch`
- `RxSkeleton` / `ResuxSkeleton`
- `RxDivider` / `ResuxDivider`
- `RxKbd` / `ResuxKbd`
- `RxModal` / `ResuxModal`

## Testing UI integrations

For a component library page, test at least:

- server fallback around the Vue island
- initial prop rendering
- `v-model` events
- disabled states
- keyboard navigation
- focus behavior for overlays
- invalid/empty values
- prop changes after mount
- reduced-motion behavior
- cleanup after unmount/navigation

The `resux-lab` compatibility bench contains the executable UI showcase used to keep this reference aligned with the framework implementation.
