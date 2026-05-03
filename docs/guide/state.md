# State

Resux state is explicit and resumable. Use `useState` for values that should be available after the HTML response reaches the browser.

## Basic state

```vue
<script setup lang="ts">
const count = useState('count', () => 0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">{{ count }}</button>
</template>
```

## Keys matter

`useState` takes a key. Use stable keys that describe the state.

```ts
const sidebarOpen = useState('layout:sidebar-open', () => false)
const draftTitle = useState('post:draft-title', () => '')
```

## JSON serializable only

State values must be JSON-serializable.

Good:

```ts
useState('settings', () => ({ theme: 'dark', compact: true }))
```

Avoid:

```ts
useState('socket', () => new WebSocket('wss://example.com'))
useState('map', () => new Map())
```

## Template auto-unwrapping

Templates read refs without `.value`:

```vue
<template>
  <p>{{ count }}</p>
</template>
```

Script uses `.value`:

```ts
count.value++
```

## State and handlers

Handlers can safely capture state refs created by `useState`:

```ts
const message = useState('message', () => 'hello')

function shout() {
  message.value = message.value.toUpperCase()
}
```

The compiler validates resumability captures so unsupported patterns fail early.

## State vs async data

Use `useState` for local interactive state. Use `useAsyncData` for data loaded from a server or expensive async source.

| Need | Use |
| --- | --- |
| Button counter | `useState` |
| UI open/closed flag | `useState` |
| API response | `useAsyncData` |
| SSR-fetched page data | `await useAsyncData` |
| Client skeleton that resolves after resume | non-awaited `useAsyncData` |
