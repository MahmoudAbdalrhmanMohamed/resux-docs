# State and Reactivity

Resux includes a native reactivity layer used by resumable components and exposed through `resuxjs` and `resuxjs/reactivity`.

## Local refs

```ts
const count = ref(0)
const doubled = computed(() => count.value * 2)
```

A plain `ref` participates in reactive rendering. Use `useState` when the value must be serialized and restored as named application state.

## Resumable state

```ts
const cart = useState('cart', () => ({ items: [] as string[] }))
```

Keys should be stable and unique for the intended scope/application behavior.

## Reactive objects

```ts
const form = reactive({
  name: '',
  tags: [] as string[]
})
```

Array index changes and length-dependent effects are tracked. Mutating an array can trigger both the changed index and relevant length dependencies.

## Computed values

```ts
const fullName = computed(() => `${form.name} (${form.tags.length})`)
```

Writable form:

```ts
const normalized = computed({
  get: () => form.name.trim(),
  set: value => { form.name = value }
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

State included in the Resux payload must be JSON-compatible. Keep runtime-only objects outside `useState` and resolved async-data values.

For private or complex server state, store an identifier and retrieve the actual resource through a server endpoint.
