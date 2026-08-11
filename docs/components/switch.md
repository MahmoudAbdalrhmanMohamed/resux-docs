# Switch

`RxSwitch` is a boolean control rendered as a native `<button type="button">` with `role="switch"` and `aria-checked`.

## Import

```ts
import { RxSwitch } from 'resuxjs/ui'
// Equivalent alias: ResuxSwitch
```

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxSwitch } from 'resuxjs/ui'

const enabled = ref(false)
</script>

<template>
  <RxSwitch v-model="enabled" aria-label="Enable notifications" />
</template>
```

## Labeled switch

Prefer a visible label when practical:

```vue
<div class="setting-row">
  <span id="email-label">Email notifications</span>
  <RxSwitch v-model="emailEnabled" aria-labelledby="email-label" />
</div>
```

## Disabled

```vue
<RxSwitch v-model="enabled" disabled aria-label="Feature unavailable" />
```

The component does not emit a new value while disabled, and the native button is disabled.

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `boolean` | `false` | No | Current switch state. |
| `disabled` | `boolean` | `false` | No | Native disabled state and interaction guard. |
| `unstyled` | `boolean` | `false` | No | Omits Resux switch classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `boolean` | Emits the negated current value when activated. |

## Slots

No slots. The rendered button contains the switch thumb span.

## Markup

The root includes:

```html
<button type="button" role="switch" aria-checked="false">
  <span></span>
</button>
```

Styled state adds `checked` to the root and uses `rx-switch` / `rx-switch-thumb` classes.

## Accessibility

The native button supplies focus and Enter/Space activation. `role="switch"` and `aria-checked` communicate the boolean state. The component does not generate a label, so provide `aria-label`, `aria-labelledby`, or a surrounding labeling pattern.

Do not communicate state only through thumb position/color; keep the accessible name clear and, when useful, expose state text nearby.

## SSR / resumability / hydration

The initial checked state can be SSR-rendered, but toggling and `v-model` updates require the Vue island/runtime. For server-submitted forms, remember that this component is a button and does not automatically create a named form value like a native checkbox.

## Complete example

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxSwitch } from 'resuxjs/ui'

const reducedData = ref(false)
</script>

<template>
  <section aria-labelledby="data-title">
    <h2 id="data-title">Data usage</h2>
    <div>
      <div id="reduced-data-label">Reduce media data</div>
      <p id="reduced-data-help">Prefer lighter media when possible.</p>
      <RxSwitch
        v-model="reducedData"
        aria-labelledby="reduced-data-label"
        aria-describedby="reduced-data-help"
      />
    </div>
  </section>
</template>
```

## Related

- [Input](./input.md)
- [Accessibility limits](/reference/limits)
- [Vue Islands](/guide/vue-islands)
