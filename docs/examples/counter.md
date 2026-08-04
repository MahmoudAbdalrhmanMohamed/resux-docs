# Counter Example

A counter demonstrates component-local reactivity, resumable events, computed values, and reactive DOM patches.

```vue
<script setup lang="ts">
const count = ref(0)
const doubled = computed(() => count.value * 2)

function increment() {
  count.value++
}

function reset() {
  count.value = 0
}
</script>

<template>
  <section>
    <h1>Counter</h1>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubled }}</p>
    <button @click="increment">Increment</button>
    <button @click="reset" :disabled="count === 0">Reset</button>
  </section>
</template>
```

The server renders the initial values. The browser imports the generated handler module after the first relevant click, resumes the component scope, and patches the three dynamic bindings.

Use `ref` for ordinary local state like this counter. Use `reactive` when several local fields belong together. Choose `useState` only when a named JSON-compatible value must be serialized and restored as part of the component scope payload.
