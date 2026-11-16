# Kbd (RxKbd)

Semantic `<kbd>` keyboard shortcut keycap primitive for command palettes, hotkeys, and CLI documentation.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxKbd` looks and behaves in real time:

<RxComponentPreview component="RxKbd" title="Kbd (RxKbd) — Live Visual Preview" />

## Import

```ts
import { RxKbd } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxKbd } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxKbd } from 'resuxjs/ui'
</script>

<template>
  <div class="flex flex-wrap items-center gap-4 text-sm">
    <span class="flex items-center gap-1">
      Search Docs: <RxKbd>Ctrl</RxKbd> + <RxKbd>K</RxKbd>
    </span>
    <span class="flex items-center gap-1">
      Quick Build: <RxKbd>⌘</RxKbd> + <RxKbd>Shift</RxKbd> + <RxKbd>B</RxKbd>
    </span>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxKbd` produces the following HTML structure (`rx-kbd`):

```html
<kbd class="rx-kbd">Ctrl</kbd> + <kbd class="rx-kbd">K</kbd>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `unstyled` | `boolean` | `false` | No | Renders `<kbd>` without the `rx-kbd` keycap class. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

| Slot | Description |
| --- | --- |
| `default` | Key symbol or shortcut text (e.g., `Ctrl`, `K`, `⌘`, `Enter`). |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxKbd unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxKbd
</RxKbd>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
