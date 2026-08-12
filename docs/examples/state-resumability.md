# State and Resumable Handlers

**Lab-backed example:** [`pages/state.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/pages/state.vue) · [Open the live page](https://resux-lab.vercel.app/state)

The lab keeps a counter, a configurable step and a status message in `useState()` values. Four buttons mutate that state through normal template handlers. This makes the page useful for checking both state serialization and interaction-time handler loading.

## Minimal pattern

```vue
<script setup lang="ts">
const count = useState('lab-count', () => 0)
const step = useState('lab-step', () => 1)

function increment() {
  count.value = count.value + step.value
}

function reset() {
  count.value = 0
  step.value = 1
}
</script>

<template>
  <p>Counter: {{ count }}</p>
  <p>Step: {{ step }}</p>
  <button @click="increment">Increment</button>
  <button @click="reset">Reset</button>
</template>
```

## Multiple values can participate in one handler

A resumable handler is not limited to one state key. The lab increments `count` using the current `step`, then updates a message that explains what happened. Keep the state required by an interaction serializable so Resux can reconstruct the handler scope correctly.

```ts
const message = useState(
  'lab-message',
  () => 'First click loads this page handler chunk.'
)

function increment() {
  count.value = count.value + step.value
  message.value = 'Incremented with resumable @click.'
}
```

## What to inspect in DevTools

1. Load the page without clicking a control.
2. Open **Network** and filter JavaScript requests.
3. Click **Increment** for the first time.
4. Inspect the generated handler/module request associated with that interaction.
5. Click again and verify the visible bindings update without replacing the whole page.

The lab itself includes this manual QA instruction because the important behavior is not only the final counter value—it is *when* browser code is loaded and *how much* DOM work follows the interaction.

## Resux state vs Vue reactivity

For Vue-owned `ref()`, `reactive()`, `computed()` and watchers, see the [Reactivity API](/reference/reactivity) and [Vue Islands](/guide/vue-islands). The Resux Lab also has a dedicated `pages/features/reactivity.vue` regression page for Vue reactivity. Do not treat a Vue runtime example as proof that the same work is handled by Resux resumability.

## Related

- [State and Reactivity guide](/guide/state)
- [Resumability and Handlers](/guide/resumability-handlers)
- [Resumability Deep Dive](/guide/resumability-deep-dive)
- [Execution Contexts](/guide/execution-contexts)
