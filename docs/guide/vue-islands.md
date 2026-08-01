# Vue Islands

Vue islands are an explicit escape hatch for widgets that need the full Vue runtime.

## When to use an island

Use a Vue island for:

- a Vue-specific component library,
- complex Vue lifecycle behavior,
- client-side rendering patterns outside the Resux compiler subset,
- or an existing Vue widget that is not practical to rewrite as a progressive enhancement.

Do not use islands by default for simple counters, forms, links, or server-rendered content.

## Create an island

```vue
<!-- islands/vue/CounterIsland.vue -->
<script setup lang="ts">
import { ref } from 'vue'
const count = ref(0)
</script>

<template>
  <button @click="count++">Vue count: {{ count }}</button>
</template>
```

Resux discovers islands and creates separate Vite client entries.

## Render an island

Use the island name through the supported island component convention in your Resux template. The surrounding page remains a Resux-rendered component; only the island subtree is mounted by Vue.

## Props

Pass JSON-compatible props so they can be represented safely in SSR output and client initialization.

## Boundaries

- Island state is Vue state, not automatically Resux resumable state.
- Island lifecycle is Vue lifecycle.
- Resux route navigation may replace the island container and mount a new instance.
- Global listeners and external library instances still require cleanup.
- Avoid sharing private server objects through props.

## Alternatives

Before using an island, consider:

- a Resux event handler,
- a client enhancement,
- a progressive package adapter,
- native HTML/CSS behavior,
- or a server-rendered interaction.

Client enhancements usually ship less framework runtime than a Vue island.
