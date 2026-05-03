# Example: Counter

A minimal interactive Resux component.

```vue
<script setup lang="ts">
const count = useState('count', () => 0)

function increment() {
  count.value++
}

function decrement() {
  count.value--
}

function reset() {
  count.value = 0
}
</script>

<template>
  <section class="counter">
    <h1>Counter</h1>
    <p>Current value: {{ count }}</p>

    <button @click="decrement">-</button>
    <button @click="increment">+</button>
    <button @click="reset">Reset</button>
  </section>
</template>
```

What happens:

1. The server renders the counter HTML.
2. `count` is serialized in the payload.
3. The browser installs the resume runtime.
4. The first button click loads the handler module.
5. The scope resumes and only marked bindings update.
