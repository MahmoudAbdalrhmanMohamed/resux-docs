# Accordion (RxAccordion)

Collapsible disclosure panel with internal toggle state initialized from the `open` prop and `+` / `-` indicator.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxAccordion` looks and behaves in real time:

<RxComponentPreview component="RxAccordion" title="Accordion (RxAccordion) — Live Visual Preview" />

## Import

```ts
import { RxAccordion } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxAccordion } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxAccordion } from 'resuxjs/ui'
</script>

<template>
  <div class="space-y-2 max-w-lg">
    <RxAccordion title="How does Resux resumability differ from hydration?" :open="true">
      Resux serializes state into <code>window.__RESUX__</code> and attaches lightweight event listeners only to interactive boundaries, avoiding full-page VNode reconstruction on initial load.
    </RxAccordion>
    <RxAccordion title="How are static icons optimized at build time?">
      <code>transformStaticIcons</code> replaces static <code>&lt;Icon name="lucide:check" /&gt;</code> tags with inline SVG or CSS mask spans during compilation when no dynamic bindings or directives are present.
    </RxAccordion>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxAccordion` produces the following HTML structure (`rx-accordion > button.rx-accordion-header + [div.rx-accordion-body]`):

```html
<div class="rx-accordion">
  <button class="rx-accordion-header">
    <span>How does Resux resumability differ from hydration?</span>
    <span>-</span>
  </button>
  <div class="rx-accordion-body">
    Resux serializes state into window.__RESUX__...
  </div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `title` | `string` | `'Accordion Title'` | No | Header button label. |
| `open` | `boolean` | `false` | No | Initial open state when mounted. |
| `unstyled` | `boolean` | `false` | No | Removes `rx-accordion*` classes. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Collapsible panel content rendered inside `.rx-accordion-body` when open. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxAccordion unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxAccordion
</RxAccordion>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
