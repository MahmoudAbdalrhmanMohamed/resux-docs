# Teleport

Resux includes a built-in, resumable `<Teleport>` component that moves a component's server-rendered HTML and client DOM nodes to a target DOM node outside the component hierarchy (such as `document.body` or `#modals`).

Unlike standard Vue SSR which requires full hydration to attach teleports, Resux's Teleport is **resumable**: it renders server HTML with boundary markers and resumes client DOM placement, target switching, and reactive updates with zero hydration overhead.

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'resux'

const showModal = ref(false)
</script>

<template>
  <button type="button" @click="showModal = true">
    Open Modal
  </button>

  <Teleport to="body">
    <div v-if="showModal" class="modal-overlay">
      <div class="modal-card">
        <h3>Teleported Modal</h3>
        <p>This content is rendered inside document.body.</p>
        <button type="button" @click="showModal = false">Close</button>
      </div>
    </div>
  </Teleport>
</template>
```

## Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `to` | `string` | *(required)* | Target element query selector (e.g. `'body'`, `'#modal-root'`, `'[data-portal]'`). |
| `disabled` | `boolean` | `false` | When `true`, content remains at its original location in the template instead of being moved to `to`. |

## Dynamic disabling

You can toggle the `disabled` prop reactively to keep elements in place on mobile viewports while teleporting them on desktop:

```vue
<script setup lang="ts">
import { ref } from 'resux'

const isMobile = ref(false)
</script>

<template>
  <Teleport to="#sidebar-slot" :disabled="isMobile">
    <aside class="sidebar-widget">
      Navigation Content
    </aside>
  </Teleport>
</template>
```

When `disabled` changes:
- `false -> true`: Resux reconciles the nodes back to their original position in the DOM.
- `true -> false`: Resux moves the nodes to the specified `to` target selector.

## Server-Side Rendering (SSR) & Resumability

During server-side rendering, Resux renders `<Teleport>` boundaries with specialized markers:

```html
<!--rx-teleport-start:scope:id to="body"-->
<div class="modal-overlay">...</div>
<!--rx-teleport-end:scope:id-->
```

On the client:
1. If the target element exists in the initial DOM, Resux's resume runtime immediately moves the nodes into the target element.
2. If the target element has not yet rendered (e.g. declared lower in the document), Resux automatically defers attachment until the target element appears in the DOM (`deferMissingTarget: true`).
3. Resux manages SVG and MathML namespaces across boundaries so elements moved into `<svg>` or `<math>` containers preserve their correct XML namespaces.
4. If an implicit HTML table wrapper triggers foster parenting, Resux's teleport engine recovers and reconciles the orphaned nodes without hydration mismatch errors.
