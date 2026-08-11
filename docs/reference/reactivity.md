# Reactivity API (`resuxjs/reactivity`)

`resuxjs/reactivity` exposes Resux's framework-native reactive primitives without the rest of the application runtime. This is the focused package for refs, reactive/readonly proxies, computed values, watchers, effects, and scheduler synchronization.

The APIs are isomorphic JavaScript and do not require a DOM. Resux application components can usually use the same names through the root `resuxjs` auto-import/runtime surface; import this subpath when a library or integration specifically needs only reactivity.

## Imports

```ts
import {
  effect,
  stop,
  ref,
  isRef,
  unref,
  toRef,
  toRefs,
  reactive,
  isReactive,
  toRaw,
  readonly,
  isReadonly,
  computed,
  isComputed,
  watch,
  watchEffect,
  nextTick
} from 'resuxjs/reactivity'
```

## `ref()`

```ts
function ref<T>(value: T): Ref<T>
```

Creates a ref with a `.value` property. Object/array values are converted through `reactive()`.

```ts
const count = ref(0)
count.value++
```

Passing an existing ref returns that ref rather than wrapping it again.

### `isRef()`

```ts
function isRef(value: unknown): value is Ref
```

### `unref()`

```ts
function unref<T>(value: T | Ref<T>): T
```

Returns `value.value` for a ref and the input unchanged otherwise.

### `toRef()`

```ts
function toRef<T extends object, K extends keyof T>(
  object: T,
  key: K,
  defaultValue?: T[K]
): Ref<T[K]>
```

Creates a ref that reads/writes one property on the source object. If that property is already a ref, the existing ref is returned.

The optional default is returned when the source property is `undefined`; assigning through the ref still writes the source property.

### `toRefs()`

```ts
function toRefs<T extends object>(
  object: T
): { [K in keyof T]: Ref<T[K]> }
```

Creates property refs for enumerable string keys. Array input preserves array shape.

## `reactive()`

```ts
function reactive<T extends object>(target: T): T
```

Creates a proxy for plain objects and arrays. Nested objects/arrays are wrapped when read.

```ts
const state = reactive({
  profile: { name: 'Ada' },
  tags: ['compiler']
})

state.profile.name = 'Grace'
state.tags.push('runtime')
```

Current proxy tracking includes property reads, `in` checks, key iteration, set/add/delete operations, and array length/index relationships.

::: info Supported target kinds
The base proxy implementation currently handles plain objects and arrays. Other object kinds such as `Map`, `Set`, `Date`, DOM nodes, and class instances are returned without Resux proxy instrumentation rather than receiving collection-specific handlers.
:::

### `isReactive()`

```ts
function isReactive(value: unknown): boolean
```

Returns true for Resux reactive proxies. A readonly proxy around a reactive proxy is also recognized as reactive through its wrapped target.

### `toRaw()`

```ts
function toRaw<T>(value: T): T
```

Unwraps Resux reactive/readonly proxy layers until the original target is reached.

Do not mutate the raw object as a routine way to bypass reactivity; use it for identity/interoperability cases where the raw target is actually required.

## `readonly()`

```ts
function readonly<T>(target: T): Readonly<T>
```

Creates a readonly proxy for supported objects/arrays.

```ts
const source = reactive({ count: 1 })
const view = readonly(source)
```

Reads work and nested objects are wrapped readonly. The current set/delete traps decline to mutate but do not throw a Resux-specific warning/error. Do not use write attempts as a validation mechanism.

### `isReadonly()`

```ts
function isReadonly(value: unknown): boolean
```

## `computed()`

```ts
function computed<T>(getter: () => T): ComputedRef<T>

function computed<T>(options: {
  get: () => T
  set?: (value: T) => void
}): ComputedRef<T>
```

Computed values are lazy and cached until a tracked dependency invalidates them.

```ts
const first = ref('Ada')
const last = ref('Lovelace')
const full = computed(() => `${first.value} ${last.value}`)
```

Writable form:

```ts
const normalized = computed({
  get: () => first.value.trim(),
  set: value => {
    first.value = value.trim()
  }
})
```

A getter-only computed has no setter; assigning to `.value` does not create one.

### `isComputed()`

```ts
function isComputed(value: unknown): boolean
```

The current check identifies objects carrying Resux ref + readonly computed flags.

## `effect()`

```ts
function effect<T = unknown>(
  fn: () => T,
  options?: ReactiveEffectOptions
): ReactiveEffectRunner<T>
```

By default the function runs immediately and tracks reactive reads.

```ts
const count = ref(0)
const runner = effect(() => {
  console.log(count.value)
})
```

Options:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `scheduler` | `() => void` | — | Called instead of re-running immediately after dependency triggers. |
| `onStop` | `() => void` | — | Called once when an active effect is stopped. |
| `lazy` | `boolean` | `false` | Skip the initial automatic run. |

The returned runner is callable and exposes `runner.effect.active` plus `runner.effect.stop()`.

### `stop()`

```ts
function stop(runner: ReactiveEffectRunner): void
```

Stops dependency tracking for the runner and invokes its `onStop` callback once. Calling the stopped runner directly still executes its function, but it no longer tracks dependencies as an active effect.

## `watch()`

```ts
function watch<T = unknown>(
  source: WatchSource<T> | WatchSource<T>[],
  callback: WatchCallback<T>,
  options?: WatchOptions
): WatchStopHandle
```

Sources can be refs, getter functions, reactive objects, or arrays of sources.

```ts
const stopWatch = watch(
  () => state.profile.name,
  (value, oldValue, onCleanup) => {
    const controller = new AbortController()
    validate(value, controller.signal)
    onCleanup(() => controller.abort())
  },
  { immediate: true }
)
```

Current options:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `immediate` | `boolean` | `false` | Run the callback immediately. The first `oldValue` is `undefined`. |
| `deep` | `boolean` | `false` | Traverse nested enumerable string/symbol properties. Reactive-object sources are deep-traversed automatically. |
| `flush` | `'sync' | 'post'` | `'post'` | Run synchronously or queue after the current reactive work. |

Calling the returned stop handle runs the latest registered cleanup and stops the watcher.

## `watchEffect()`

```ts
function watchEffect(
  effectFn: (onCleanup: (cleanup: () => void) => void) => void,
  options?: WatchOptions
): WatchStopHandle
```

Dependencies are whatever reactive values are read during the current run. Cleanup runs before the next run and when stopped.

```ts
const stopEffect = watchEffect(onCleanup => {
  const id = setInterval(() => console.log(state.profile.name), 1000)
  onCleanup(() => clearInterval(id))
})
```

`flush` is relevant to re-runs; `immediate` has no separate meaning for `watchEffect` because the effect establishes its dependencies by running initially.

## `nextTick()`

```ts
function nextTick<T = void>(
  fn?: () => T | PromiseLike<T>
): Promise<T | void>
```

Waits for the current Resux scheduler flush when one exists, otherwise resolves from the shared resolved promise.

```ts
state.profile.name = 'Grace'
await nextTick()
```

The scheduler drains normal and post-flush queues, keeps processing jobs queued during the same flush, limits one recursively queued job to 100 executions, and continues through queued jobs after an error before rejecting with the first captured error.

## Public types

```ts
interface Ref<T = unknown> {
  value: T
  readonly __v_isRef: true
}

interface ComputedRef<T = unknown> extends Ref<T> {
  readonly __v_isReadonly: true
}

type MaybeRef<T> = T | Ref<T>
type MaybeRefOrGetter<T> = MaybeRef<T> | (() => T)
type WatchSource<T = unknown> = Ref<T> | (() => T) | object

type WatchCleanup = () => void
type WatchStopHandle = () => void
```

Also exported: `WatchOptions`, `WatchCallback`, `ReactiveEffectOptions`, and `ReactiveEffectRunner`.

## Resumability and serialization

Reactivity and serialization are separate concerns. `ref()` / `reactive()` make values reactive; they do not automatically make arbitrary values safe for Resux payload serialization.

Use JSON-compatible data when values cross the server/browser boundary through `useState`, `useGlobalState`, async data, or another serialized payload. Keep functions, DOM objects, sockets, database clients, `Map`/`Set`, and other runtime-only objects out of resumable payload state.

## Related

- [State and Reactivity](/guide/state)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [Composables and Globals](./composables.md)
