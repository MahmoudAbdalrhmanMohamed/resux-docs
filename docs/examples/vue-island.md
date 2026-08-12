# Vue Island

**Lab-backed example:** [`pages/vue-island.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/pages/vue-island.vue) and [`islands/vue/IslandCounter.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/islands/vue/IslandCounter.vue) · [Open the live page](https://resux-lab.vercel.app/vue-island)

Vue islands are an explicit escape hatch: keep the outer page owned by Resux and give Vue runtime ownership only to the nested widget that actually needs Vue behavior.

## Render the island from a Resux page

```vue
<script setup lang="ts">
definePageMeta({ title: 'Vue Island' })
</script>

<template>
  <section>
    <h1>Vue runtime island</h1>
    <VueIsland name="IslandCounter" :props="{ start: 7 }" />
  </section>
</template>
```

The `start` value crosses the boundary as serializable props.

## Implement the Vue-owned widget

Create `islands/vue/IslandCounter.vue`:

```vue
<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{ start: number }>()
const count = ref(props.start)
</script>

<template>
  <div>
    <p>{{ count }}</p>
    <button @click="count++">Vue increment</button>
  </div>
</template>
```

Only this nested widget needs Vue's `ref()` and event runtime. The surrounding route does not have to become a Vue-owned application subtree just because one control benefits from Vue.

## When this pattern is appropriate

Use a Vue island when a third-party Vue component or Vue-specific local widget genuinely requires Vue ownership. Prefer native Resux templates and resumable handlers when the feature can stay within the Resux execution model.

This boundary is especially important for `resuxjs/ui`: those components are Vue `defineComponent()` components, so place them in an explicit Vue runtime boundary rather than assuming they are Resux template primitives.

## Related

- [Vue Islands guide](/guide/vue-islands)
- [How Resux Uses Vue](/guide/how-resux-uses-vue)
- [Execution Contexts](/guide/execution-contexts)
- [UI Components](/components/)
