# Counter Example

A counter demonstrates SSR state, resumable events, computed values, and reactive DOM patches.

```vue
<script setup lang="ts">
const count = useState('example-counter', () => 0)
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

The server renders the initial values. The browser imports the generated handler module after the first relevant click, reconstructs the state, and patches the three dynamic bindings.

Use a stable state key and keep its value serializable.
