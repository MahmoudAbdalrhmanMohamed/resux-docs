# View Transitions

Resux integrates the native browser **View Transitions API** into its client router and resumable runtime. This enables smooth, animated transitions between page routes without client SPA hydration overhead or third-party animation libraries.

## Overview

When navigating between routes, Resux captures a snapshot of the current DOM, executes the DOM swap callback inside `document.startViewTransition()`, and lets the browser animate the transition between the old and new view.

Because Resux operates with a **Resume-First** architecture, View Transitions protect the 14 KiB raw / 5 KiB gzip bootstrap budget while delivering fluid native animations.

## Enabling View Transitions

### Global configuration

Enable View Transitions across your entire application in `resux.config.ts`:

```ts
// resux.config.ts
import { defineResuxConfig } from 'resux'

export default defineResuxConfig({
  router: {
    // Enable View Transitions API for all route navigations
    viewTransition: true
  }
})
```

### Per-link control with `<ResuxLink>`

You can explicitly opt in or opt out of View Transitions on individual links using the `:view-transition` prop:

```vue
<template>
  <!-- Force View Transition for this link -->
  <ResuxLink to="/dashboard" :view-transition="true">
    Dashboard
  </ResuxLink>

  <!-- Disable View Transition for this link -->
  <ResuxLink to="/quick-view" :view-transition="false">
    Instant View
  </ResuxLink>
</template>
```

When an explicit boolean is passed to `<ResuxLink>`, it overrides both page metadata and global router configuration.

### Per-page control with `definePageMeta`

Configure View Transitions for specific pages using `definePageMeta()`:

```vue
<!-- pages/gallery.vue -->
<script setup lang="ts">
definePageMeta({
  viewTransition: true
})
</script>

<template>
  <main class="gallery">
    <h1>Photo Gallery</h1>
  </main>
</template>
```

### Programmatic navigation with `navigateTo`

Pass `viewTransition: true` to programmatic navigation calls:

```ts
import { navigateTo } from 'resux'

// Trigger navigation with View Transition
await navigateTo('/products/42', {
  viewTransition: true
})
```

## `useViewTransition` composable

For custom UI transitions or testing browser capability, Resux exports the `useViewTransition()` composable:

```vue
<script setup lang="ts">
import { ref } from 'resux'
import { useViewTransition } from 'resux'

const vt = useViewTransition()
const isListView = ref(true)

async function toggleLayout() {
  await vt.start(() => {
    isListView.value = !isListView.value
  })
}
</script>

<template>
  <button type="button" @click="toggleLayout">
    Toggle View (Supported: {{ vt.isSupported }})
  </button>
</template>
```

`useViewTransition()` returns:
- `isSupported`: `boolean` indicating whether `document.startViewTransition` is available.
- `start(callback)`: Runs `callback()` wrapped in `executeViewTransition()`, safely handling browser fallback if unsupported.

## Speculative Route Preloading Integration

Resux pairs View Transitions with the browser's **Speculation Rules API** (`<script type="speculationrules">`) for **instant, zero-latency animated transitions**:

```ts
// resux.config.ts
export default defineResuxConfig({
  router: {
    viewTransition: true
  },
  app: {
    head: {
      script: [
        {
          type: 'speculationrules',
          innerHTML: JSON.stringify({
            prerender: [
              {
                where: {
                  and: [
                    { href_matches: '/*' },
                    { not: { href_matches: '/api/*' } }
                  ]
                },
                eagerness: 'moderate' // Prerender on link hover or focus
              }
            ]
          })
        }
      ]
    }
  }
})
```

When configured:
1. Hovering over a `<ResuxLink>` silently prerenders the target route in the background.
2. Clicking the link activates the prerendered document immediately.
3. The browser runs the View Transition animation with **zero network latency**.

## CSS Customization

You can customize view transition animations using standard CSS pseudo-elements:

```css
/* Custom cross-fade with zoom */
::view-transition-old(root) {
  animation: 200ms ease-out both fade-out;
}

::view-transition-new(root) {
  animation: 200ms ease-in both fade-in;
}

@keyframes fade-out {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0; transform: scale(0.98); }
}

@keyframes fade-in {
  from { opacity: 0; transform: scale(1.02); }
  to { opacity: 1; transform: scale(1); }
}
```

To give specific persistent elements (like headers, cards, or hero images) shared element transitions:

```css
.hero-card {
  view-transition-name: hero-card;
}
```

## Accessibility: Reduced Motion

Resux's View Transition engine **automatically detects and respects** the `(prefers-reduced-motion: reduce)` media query:

- If reduced motion is preferred, transitions are automatically bypassed and DOM swaps execute immediately.
- This ensures users with motion sensitivities are protected without requiring extra code in your application.
