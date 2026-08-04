# Resumability and Handlers

Resumability lets the browser continue from server-rendered output without hydrating the full component tree.

## What is serialized

A scope may contain:

- component/module id,
- serializable props,
- `useState` values,
- resolved async data,
- pending and error state,
- and references to generated browser modules.

Only values representable by the Resux JSON payload should cross the server/browser boundary.

::: tip Scope, not global state
`useState` values belong to one rendered component scope. The same key used by another component instance does not overwrite this scope. For ordinary component-local UI state that does not require named serialization, prefer `ref` or `reactive`.
:::

## Safe serialized state

The examples in this section intentionally use `useState` because they demonstrate values that must be included in the serialized scope payload:

```ts
const count = useState('counter', () => 0)
const filters = useState('filters', () => ({ query: '', active: true }))
```

Good values include strings, numbers, booleans, `null`, arrays, and plain objects made from those values.

Avoid functions, class instances, DOM nodes, streams, sockets, `Map`, `Set`, and private server clients.

## Safe handler captures

```ts
const count = useState('counter', () => 0)
const step = 2

function increment() {
  count.value += step
}
```

The compiler analyzes handlers and rejects captures it cannot safely reproduce. Imports intended for browser execution must be compatible with the configured package mode.

Move private or server-only work behind an API:

```ts
async function save() {
  await $fetch('/api/save', {
    method: 'POST',
    body: { value: count.value }
  })
}
```

## Delegated events

Resux installs shared event listeners and finds handler metadata in the event path. Named and supported inline handlers compile to browser modules.

```vue
<button @click="increment">Add</button>
<form @submit.prevent="save">...</form>
<input @keydown.enter="search" />
```

Supported modifier groups include control, system, mouse, and key filters. `.capture` and `.passive` are accepted syntax but still participate in the delegated runtime model.

## Reactive patches

The compiler records dynamic text, attributes, class, style, visibility, and HTML bindings. After a handler mutates a dependency, the resumed effect evaluates the relevant expressions and updates the matching DOM nodes.

```vue
<p :class="{ active: count > 0 }">{{ count }}</p>
```

## Watch cleanup

```ts
watchEffect((onCleanup) => {
  const timer = setInterval(refresh, 5000)
  onCleanup(() => clearInterval(timer))
})
```

Watch dependencies are cleaned before re-running, which prevents stale branches from continuing to trigger effects.

## Mounted cleanup

```ts
onMounted(() => {
  const controller = new AbortController()
  window.addEventListener('resize', handleResize, { signal: controller.signal })
  return () => controller.abort()
})
```

Mounted work runs when the scope first resumes in the browser, not during SSR.

## Client enhancements

Enhancement setup receives a target and context and may return a cleanup function:

```ts
export default defineClientEnhancement('tooltip', (target, context) => {
  const instance = createTooltip(target, context.options)
  return () => instance.destroy()
})
```

Use `useClientEnhancement` for manual control and `disposeClientEnhancements` for explicit global disposal in advanced integration code.

## Debugging

```sh
resux dev --trace-resume
resux inspect enhancements --json
resux inspect bundles --json
```

If a handler fails compilation, reduce captures, move work to a server endpoint, configure the package mode, or use a client enhancement/Vue island.
