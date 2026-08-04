# State and Reactivity

Resux includes a native reactivity layer used by resumable components and exposed through `resuxjs` and `resuxjs/reactivity`.

## Choose the smallest state scope

Use local reactivity by default. Reach for named resumable state only when the value must be serialized and restored across the server/browser boundary.

| Need | Preferred API |
| --- | --- |
| One local scalar value | `ref` |
| A local object with related fields | `reactive` |
| A derived value | `computed` |
| A named value that must be serialized and restored | `useState` |
| Server data with pending and error state | `useAsyncData` or `useFetch` |

::: tip Important
`useState` in Resux is stored **per rendered component scope**. It is not one app-global object shared by every component. Using the same key in two different component instances does not make one component overwrite the other. Reusing a key inside the same component scope returns the same ref.
:::

## Local refs

Use `ref` for ordinary component-local values:

```ts
const count = ref(0)
const doubled = computed(() => count.value * 2)
```

A plain `ref` participates in reactive rendering and keeps state ownership close to the component that uses it. Prefer this for counters, toggles, selected tabs, open/closed state, and similar UI details.

## Reactive objects

Use `reactive` when several local fields belong together:

```ts
const form = reactive({
  name: '',
  tags: [] as string[]
})
```

Array index changes and length-dependent effects are tracked. Mutating an array can trigger both the changed index and relevant length dependencies.

Avoid wrapping unrelated values in one large reactive object. Smaller state is easier to understand, test, and reset.

## Named resumable state

Use `useState` only when the value must be included in the serialized scope payload and restored by the browser:

```ts
const cart = useState('cart', () => ({
  items: [] as string[]
}))
```

The key identifies the value **inside the current component scope**. Use stable, descriptive keys and keep the value JSON-compatible.

Do not use `useState` merely because a value is reactive. For normal local UI state, `ref` or `reactive` is clearer and avoids unnecessary serialization.

## Computed values

```ts
const fullName = computed(() => `${form.name} (${form.tags.length})`)
```

Writable form:

```ts
const normalized = computed({
  get: () => form.name.trim(),
  set: value => {
    form.name = value
  }
})
```

## `watch`

```ts
const stop = watch(
  () => form.name,
  (next, previous, onCleanup) => {
    const controller = new AbortController()
    validateName(next, controller.signal)
    onCleanup(() => controller.abort())
  },
  { immediate: true }
)
```

Watching a reactive object is deep by default. Options include `immediate`, `deep`, `flush`, and `once` where supported by the current API.

## `watchEffect`

```ts
const stop = watchEffect((onCleanup) => {
  const id = setInterval(() => console.log(form.name), 1000)
  onCleanup(() => clearInterval(id))
})
```

Dependencies from stale conditional branches are removed before the next run.

## Readonly and conversion helpers

```ts
const readonlyForm = readonly(form)
const name = toRef(form, 'name')
const fields = toRefs(form)

isRef(name)
isReactive(form)
isReadonly(readonlyForm)
unref(name)
toRaw(form)
```

## Scheduler

```ts
form.name = 'Mahmoud'
await nextTick()
```

`nextTick` waits for queued reactive work to flush.

## Low-level reactivity

The focused `resuxjs/reactivity` entry also exports lower-level APIs such as `effect`, `stop`, and `isComputed`. Application components normally need the higher-level APIs documented above.

## Serialization rules

Values included in the Resux payload must be JSON-compatible. Keep functions, class instances, DOM nodes, sockets, streams, `Map`, `Set`, and runtime-only clients outside `useState` and resolved async-data values.

For private or complex server state, store an identifier and retrieve the actual resource through a server endpoint.
