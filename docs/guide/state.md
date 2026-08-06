# State and Reactivity

Resux includes a native reactivity layer used by resumable components and exposed through `resuxjs` and `resuxjs/reactivity`.

## Choose the smallest state scope

Use local reactivity by default. Reach for serialized state only when the value must cross the server/browser boundary, and use app-wide state only when multiple components intentionally own the same value.

| Need | Preferred API |
| --- | --- |
| One local scalar value | `ref` |
| A local object with related fields | `reactive` |
| A derived value | `computed` |
| Named serialized state owned by one component scope | `useState` |
| Named serialized state shared across component scopes | `useGlobalState` |
| Server data with pending and error state | `useAsyncData` or `useFetch` |

::: tip Scope matters
`useState` is stored **per rendered component scope**. Reusing a key inside that scope returns the same ref, but the same key in another component instance creates a different scoped ref.

`useGlobalState` is stored once for the current Resux application. Components using the same global key receive the same ref.
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

## Component-scoped resumable state

Use `useState` when a named value belongs to one component scope and must be serialized and restored by the browser:

```ts
const draft = useState('draft', () => ({
  title: '',
  body: ''
}))
```

The key identifies the value **inside the current component scope**. Another component can use the same key without overwriting this component's value.

Do not use `useState` merely because a value is reactive. For normal local UI state that does not require named serialization, `ref` or `reactive` is clearer.

## App-wide global state

Use `useGlobalState` when layouts, pages, or separate components intentionally need one shared serialized value:

```ts
const session = useGlobalState('session', () => ({
  user: null as null | { id: string; name: string },
  authenticated: false
}))
```

A second component using the same key receives the same ref:

```ts
const session = useGlobalState('session')

function signOut() {
  session.value = {
    user: null,
    authenticated: false
  }
}
```

Choose one canonical initiator for each key and give only that call the factory. Consumers that omit the factory receive the same ref and the initial value already established for the key; they do not create a separate value. The first call wins: if it omits the factory, the key is initialized to `undefined`, and a factory supplied by a later call is ignored.

During SSR, global state is isolated to the current request. It is serialized once under `payload.globalState`, restored as shared browser refs, and preserved during Resux client navigation. Changing a global value refreshes bindings in every rendered scope that reads it.

Use stable, descriptive keys, and make sure the canonical initiator runs before factory-free consumers.

Suitable uses include authenticated-user summaries, application preferences, cart summaries, feature flags loaded for the current application, and state shared by a persistent layout and its pages.

Do not use global state for unrelated local controls or as a replacement for server APIs. Private credentials, database clients, and request-only server objects must never be placed in it.

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

Watching a reactive object is deep by default. Deep traversal includes enumerable string and symbol keys. Current options are `immediate`, `deep`, and `flush` (`'sync'` or `'post'`).

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

`toRefs()` preserves array shape when its input is an array, so positional refs continue to work with array checks and array-oriented code:

```ts
const values = reactive([1, 2])
const valueRefs = toRefs(values)

Array.isArray(valueRefs) // true
valueRefs[0].value = 3
```

## Scheduler

```ts
form.name = 'Mahmoud'
await nextTick()
```

`nextTick` waits for queued reactive work to flush. If one queued callback throws, the scheduler continues running the other queued callbacks and then rejects with the first error.

## Low-level reactivity

The focused `resuxjs/reactivity` entry also exports lower-level APIs such as `effect`, `stop`, and `isComputed`. Application components normally need the higher-level APIs documented above.

## Serialization rules

Values included in the Resux payload must be JSON-compatible. Keep functions, class instances, DOM nodes, sockets, streams, `Map`, `Set`, and runtime-only clients outside `useState`, `useGlobalState`, and resolved async-data values.

For private or complex server state, store an identifier and retrieve the actual resource through a server endpoint.
