# Resumability and Handlers

Resux resumability is centered on explicit serializable state and event handlers that can be safely resumed later in the browser.

## Resumable scope

Each rendered component instance gets a scope. A scope can contain:

- Props that can be serialized.
- `useState()` refs.
- `useAsyncData()` resources.
- Handler references.
- Template binding ids used for client patches.

The scope is serialized during SSR and restored only when the browser needs it.

## Safe state

Use `useState()` for local interactive values:

```vue
<script setup lang="ts">
const count = useState('count', () => 0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">Count: {{ count }}</button>
</template>
```

State values must be JSON-serializable. Strings, numbers, booleans, arrays, plain objects, and `null` are safe. Sockets, class instances, DOM nodes, functions, `Map`, and `Set` are not safe state values.

## Handler captures

Handlers may capture resumable values such as refs from `useState()` and `useAsyncData()`.

Good:

```ts
const message = useState('message', () => 'hello')

function shout() {
  message.value = message.value.toUpperCase()
}
```

Risky:

```ts
const socket = new WebSocket('wss://example.com')

function send() {
  socket.send('hello')
}
```

The risky example depends on a browser-only, non-serializable object. Move that work into `onMounted()`, a Vue island, or a server API depending on the feature.

## Inline events

Inline event expressions are supported when they only use resumable values:

```vue
<button @click="count.value++">Add</button>
```

Named handlers are easier to test and explain, especially when the handler performs more than one mutation.

## Event modifiers

Resux supports common event modifiers such as `.prevent`, `.stop`, `.self`, `.once`, key filters, mouse filters, and system modifiers.

```vue
<form @submit.prevent="save">
  <button>Save</button>
</form>
```

`.capture` and `.passive` are accepted by the compiler, but the browser runtime still uses delegated resumable listeners.

## Client patches

After a resumed handler runs, Resux computes patches for marked template bindings:

- Text interpolation.
- Dynamic attributes.
- `v-html`.
- Conditional blocks.
- List blocks.

Keep templates simple and compiler-friendly. If a widget needs complex browser-managed state, use a Vue island.

## Mounted work

`onMounted()` runs when a component scope is first resumed in the browser. It does not run during the initial server render.

```ts
onMounted(() => {
  console.log('scope resumed in the browser')
})
```

Use it for browser-only APIs that belong to a resumable Resux component. Use a Vue island when the feature needs full Vue lifecycle behavior.

## Choosing the right place

| Need | Use |
| --- | --- |
| Counter, menu state, filters | `useState()` |
| SSR data or skeleton data | `useAsyncData()` |
| Internal API calls in SSR-capable code | `$fetch()` or `apiURL()` |
| Browser-only initialization after resume | `onMounted()` |
| Full Vue runtime behavior | Vue island |
| Secrets or private server work | Server API or server route |
