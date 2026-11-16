# Modal (RxModal)

Dialog overlay with backdrop click dismissal (`@click.self`), optional `<h3>` title header, and `update:open` / `close` events.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxModal` looks and behaves in real time:

<RxComponentPreview component="RxModal" title="Modal (RxModal) — Live Visual Preview" />

## Import

```ts
import { RxModal } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxModal } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxModal, RxButton, RxInput } from 'resuxjs/ui'

const isModalOpen = ref(false)
const confirmTag = ref('v0.4.0-beta.7')
</script>

<template>
  <div>
    <RxButton variant="primary" @click="isModalOpen = true">
      Open Release Confirmation Modal
    </RxButton>

    <RxModal
      :open="isModalOpen"
      title="Publish resuxjs Release"
      @update:open="isModalOpen = $event"
    >
      <div class="space-y-4">
        <p class="text-sm opacity-80">
          Confirm the npm dist-tag and Halal Core report signature before publishing to the registry.
        </p>
        <RxInput v-model="confirmTag" placeholder="v0.4.0-beta.7" />
        <div class="flex justify-end gap-2">
          <RxButton variant="ghost" size="sm" @click="isModalOpen = false">Cancel</RxButton>
          <RxButton variant="primary" size="sm" @click="isModalOpen = false">Confirm &amp; Publish</RxButton>
        </div>
      </div>
    </RxModal>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxModal` produces the following HTML structure (`rx-modal-backdrop > div.rx-modal-content > [h3] + slot`):

```html
<div class="rx-modal-backdrop">
  <div class="rx-modal-content">
    <h3 style="margin-top: 0px;">Publish resuxjs Release</h3>
    <p>Confirm the npm dist-tag and Halal Core report signature...</p>
  </div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `open` | `boolean` | `false` | No | Controls whether the modal dialog is mounted in the DOM. |
| `title` | `string` | `''` | No | Optional dialog title rendered inside `<h3 style="margin-top: 0">`. |
| `unstyled` | `boolean` | `false` | No | Omits `rx-modal-backdrop` and `rx-modal-content` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:open` | `boolean` | Emitted with `false` when clicking the backdrop. |
| `close` | `void` | Emitted alongside `update:open` when closing. |

## Slots

| Slot | Description |
| --- | --- |
| `default` | Dialog body content and action buttons. |

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxModal unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxModal
</RxModal>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
