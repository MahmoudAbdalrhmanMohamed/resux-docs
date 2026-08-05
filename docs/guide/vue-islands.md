# Vue Islands

Vue islands are an explicit boundary for widgets that need the full Vue runtime. Normal Resux components use the Resux compiler, reactivity layer, server renderer, and resumable browser runtime.

Read [How Resux Uses Vue](/guide/how-resux-uses-vue) before choosing this boundary.

## When to use an island

Use a Vue island for:

- a Vue-specific component library,
- complex Vue lifecycle behavior,
- client-side rendering patterns outside the Resux compiler subset,
- or an existing Vue widget that is not practical to rewrite as a progressive enhancement.

Do not use islands by default for simple counters, forms, links, or server-rendered content.

## Create an island

A file under `islands/vue` is a real Vue component. Import reactivity from `vue` and use native Vue template semantics inside the island:

```vue
<!-- islands/vue/CounterIsland.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{ initial?: number }>()
const count = ref(props.initial ?? 0)
</script>

<template>
  <button @click="count++">Vue count: {{ count }}</button>
</template>
```

Resux discovers islands and creates separate Vite/Vue client entries.

## Render an island from Resux

The surrounding page is a normal Resux component, so use Resux directive syntax there:

```vue
<template>
  <section>
    <h2>Interactive counter</h2>
    <VueIsland
      name="CounterIsland"
      rx-bind:props="{ initial: 3 }"
    />
  </section>
</template>
```

Only the island container is mounted by Vue. The surrounding page remains server-rendered and resumable.

## Props

The `props` binding must evaluate to an object whose values are JSON-compatible. Resux serializes the object into the SSR island container and passes it to Vue during mounting.

```vue
<VueIsland
  name="CounterIsland"
  rx-bind:props="{
    initial: 3,
    labels: ['Increase', 'Reset'],
    preferences: { compact: true }
  }"
/>
```

Do not pass functions, live refs, class instances, DOM nodes, open connections, or private server objects through island props.

## Boundaries

- Island state is Vue state, not Resux resumable state.
- Island lifecycle is Vue lifecycle.
- Resux route navigation may replace the island container and mount a new instance.
- Global listeners and external library instances still require cleanup.
- Data crossing the boundary must be serializable and safe for the browser.

## Alternatives

Before using an island, consider:

- a Resux event handler,
- a client enhancement,
- a progressive package adapter,
- native HTML/CSS behavior,
- or a server-rendered interaction.

Client enhancements usually ship less framework runtime than a Vue island.
