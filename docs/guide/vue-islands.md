# Vue Islands

Normal Resux components do not hydrate with Vue. Vue islands are the escape hatch for complex client widgets that need the full Vue runtime.

## Create an island

Put Vue island files under `islands/vue`.

```txt
islands/vue/CounterIsland.vue
```

```vue
<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{ start: number }>()
const count = ref(props.start)
</script>

<template>
  <button @click="count++">
    Vue island count: {{ count }}
  </button>
</template>
```

## Use an island

```vue
<template>
  <VueIsland name="CounterIsland" :props="{ start: 1 }" />
</template>
```

## When to use islands

Use a Vue island for:

- Rich client-only widgets.
- Complex third-party Vue components.
- Behavior that depends heavily on Vue runtime reactivity.
- Browser APIs that are not appropriate for Resux resumable handlers.

Keep normal content, routing, simple state, async data, and buttons as Resux components.

## Bundle model

The compiler discovers islands, creates Vite client entries, and emits island assets under Resux client output. They are opt-in and separate from normal Resux handler chunks.
