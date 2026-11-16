# Avatar (RxAvatar)

User or team identity avatar that renders an image when `src` is provided or automatically falls back to uppercase initials from `alt`, with optional presence status dot.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxAvatar` looks and behaves in real time:

<RxComponentPreview component="RxAvatar" title="Avatar (RxAvatar) — Live Visual Preview" />

## Import

```ts
import { RxAvatar } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxAvatar } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { RxAvatar } from 'resuxjs/ui'
</script>

<template>
  <div class="flex items-center gap-4">
    <RxAvatar alt="Mahmoud Abdelrahman" size="lg" status="online" />
    <RxAvatar alt="Resux Core" size="md" status="busy" />
    <RxAvatar alt="Nitro Engine" size="sm" status="away" />
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxAvatar` produces the following HTML structure (`rx-avatar rx-avatar-${size} > (img.rx-avatar-img | span.rx-avatar-fallback) + [span.rx-avatar-status.rx-status-${status}]`):

```html
<div class="rx-avatar rx-avatar-lg">
  <span class="rx-avatar-fallback">MA</span>
  <span class="rx-avatar-status rx-status-online"></span>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `src` | `string` | `''` | No | Image URL. When empty, renders the first 2 characters of `alt` uppercased. |
| `alt` | `string` | `'Avatar'` | No | Accessible alt text and source for the 2-letter fallback initials. |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | No | Controls avatar dimensions (`rx-avatar-sm`, `rx-avatar-md`, `rx-avatar-lg`). |
| `status` | `'' \| 'online' \| 'busy' \| 'away' \| 'offline'` | `''` | No | Optional presence indicator dot (`rx-status-${status}`). |
| `unstyled` | `boolean` | `false` | No | Strips default `rx-avatar*` classes. |

## Events

This component does not emit custom events (native DOM events forward normally).

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxAvatar unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxAvatar
</RxAvatar>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
