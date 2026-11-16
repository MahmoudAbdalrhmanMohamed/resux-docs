# Tooltip (RxTooltip)

Hover-activated floating hint bubble supporting `top`, `bottom`, `left`, and `right` placements.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxTooltip` looks and behaves in real time:

<RxComponentPreview component="RxTooltip" title="Tooltip (RxTooltip) — Live Visual Preview" />

## Import

```ts
import { RxTooltip } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxTooltip } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxTooltip, RxButton } from 'resuxjs/ui'
</script>

<template>
  <div class="flex flex-wrap items-center gap-4 py-4">
    <RxTooltip text="Compiles static <Icon> tags into 0 KB inline SVGs" placement="top">
      <RxButton variant="outline" size="sm">Hover Top</RxButton>
    </RxTooltip>
    <RxTooltip text="Preloads route head stylesheets before DOM swap" placement="bottom">
      <RxButton variant="outline" size="sm">Hover Bottom</RxButton>
    </RxTooltip>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxTooltip` produces the following HTML structure (`rx-tooltip-wrapper > slot + [div.rx-tooltip.rx-tooltip-${placement}]`):

```html
<div class="rx-tooltip-wrapper">
  <button class="rx-btn rx-btn-outline rx-btn-sm">Hover Top</button>
  <div class="rx-tooltip rx-tooltip-top">
    Compiles static &lt;Icon&gt; tags into 0 KB inline SVGs
  </div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `text` | `string` | `''` | No | Tooltip message text. Tooltip only renders when `text` is non-empty. |
| `placement` | `'top' \| 'bottom' \| 'left' \| 'right'` | `'top'` | No | Position relative to the wrapped trigger element. |
| `unstyled` | `boolean` | `false` | No | Removes `rx-tooltip*` classes. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Target element that triggers the tooltip on `mouseenter` / `mouseleave`. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxTooltip unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxTooltip
</RxTooltip>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
