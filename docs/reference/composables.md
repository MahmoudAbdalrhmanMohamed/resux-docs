# Composables and Globals Reference

Generated applications include `resuxjs/globals` types, so the APIs on this page can normally be used without imports inside Resux application files. Libraries and explicit modules can import from `resuxjs` or a focused subpath.

## Reactivity

Resux provides its own reactivity layer for normal resumable components.

```ts
import {
  ref,
  reactive,
  computed,
  watch,
  watchEffect,
  readonly,
  toRef,
  toRefs,
  unref,
  isRef,
  isReactive,
  isReadonly,
  nextTick
} from 'resuxjs/reactivity'
```

### `ref(value)`

```ts
const count = ref(0)
count.value++
```

### `reactive(object)`

```ts
const state = reactive({ count: 0, user: { name: 'Mahmoud' } })
state.count++
```

Watching a reactive object is deep by default. Array index additions also invalidate length-dependent effects.

### `computed(getter | { get, set })`

```ts
const doubled = computed(() => count.value * 2)
```

Writable form:

```ts
const fullName = computed({
  get: () => `${first.value} ${last.value}`,
  set: (value) => {
    const [nextFirst, nextLast = ''] = value.split(' ')
    first.value = nextFirst
    last.value = nextLast
  }
})
```

### `watch(source, callback, options?)`

```ts
const stop = watch(
  () => state.user.name,
  (next, previous, onCleanup) => {
    const controller = new AbortController()
    onCleanup(() => controller.abort())
    console.log({ next, previous })
  },
  { immediate: true }
)

stop()
```

Watch cleanup runs before the watcher reruns and when it is stopped.

### `watchEffect(effect, options?)`

```ts
const stop = watchEffect((onCleanup) => {
  const id = setInterval(() => console.log(count.value), 1000)
  onCleanup(() => clearInterval(id))
})
```

### Utility helpers

```ts
const locked = readonly(state)
const countRef = toRef(state, 'count')
const allRefs = toRefs(state)
const value = unref(countRef)

isRef(countRef)
isReactive(state)
isReadonly(locked)
await nextTick()
```

These APIs are similar to familiar Vue APIs but are implemented by Resux. Do not assume undocumented Vue scheduler or devtools internals are identical.

## Resumable state

### `useState<T>(key, factory?)`

Create or retrieve a named ref owned by the current rendered component scope:

```ts
const draftStep = useState<number>('draft-step', () => 0)
draftStep.value++
```

Calling `useState` again with the same key inside that component scope returns the same ref. A different component scope using the same key receives a different ref.

Use `ref` or `reactive` when named serialization is unnecessary. The key must be stable and the value must be JSON-serializable.

### `useGlobalState<T>(key, factory?)`

Create or retrieve an app-wide serialized ref shared by all Resux component scopes:

```ts
const session = useGlobalState('session', () => ({
  user: null as null | { id: string; name: string },
  authenticated: false
}))
```

Components using the same key receive the same ref. Choose one canonical initiator for each key and give only that call the factory. Calls without a factory receive the same ref and the initial value already established for the key; they do not create another value. The first call wins: if it omits the factory, the key is initialized to `undefined`, and any later factory for that key is ignored.

During SSR, the registry belongs only to the current request. The values are serialized once under `payload.globalState`, restored as shared browser refs, and preserved during Resux client navigation. A mutation refreshes rendered scopes so bindings in separate components remain synchronized.

Global-state values must be JSON-serializable. Keep credentials, database clients, DOM nodes, sockets, functions, and other runtime-only objects outside global state.

## Async data

### `useAsyncData<T>(key, handler?)`

```ts
const resource = useAsyncData('dashboard-stats', async ({ signal }) => {
  return $fetch<{ users: number }>('/api/stats', { signal })
})

const { data, value, pending, error } = await resource
```

Return shape:

```ts
type AsyncDataResource<T> = {
  data: Ref<T | undefined>
  value: Ref<T | undefined>
  pending: Ref<boolean>
  error: Ref<{ name: string; message: string } | null>
  then(...): PromiseLike<unknown>
}
```

The resource is thenable. Awaiting it waits for the current server/client resolution and returns the refs, not the raw data value.

## Fetching

### `apiURL(path)`

Resolve an internal API path safely during SSR:

```ts
const url = apiURL('/api/profile')
```

Resux can use route origin information or configured public origin keys such as `appOrigin`, `appURL`, `siteURL`, or `origin`.

### `useFetch<T>(url, init?)`

Fetch JSON through an async-data resource:

```ts
const request = useFetch<{ ok: boolean }>('/api/status')
const { data, pending, error } = await request

if (data.value?.ok) {
  // ready
}
```

`useFetch` returns the same resource style as `useAsyncData`; it does not return a plain ref or plain response body.

### `$fetch<T>(url, init?)`

Fetch and return the parsed value:

```ts
const profile = await $fetch<{ id: string; name: string }>('/api/profile')
```

Use `useFetch` when pending/error state and resumable payload behavior are useful. Use `$fetch` for direct request/response control.

## Routing

### `useRoute()`

```ts
const route = useRoute()

route.path
route.params
route.query
route.origin
route.userAgent
```

### `useRouter()`

```ts
const router = useRouter()

await router.push('/account')
await router.replace('/login')
router.back()
router.forward()
router.go(-2)
```

Internal navigation can use route payloads rather than downloading and hydrating a full application bundle.

### `navigateTo(to, options?)`

Use in middleware or server-aware navigation flows:

```ts
return navigateTo('/login', { statusCode: 302 })
```

### `abortNavigation(message?, options?)`

```ts
return abortNavigation('Not allowed', { statusCode: 403 })
```

## Page metadata and document head

### `definePageMeta(meta)`

```ts
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth'],
  title: 'Dashboard',
  meta: [{ name: 'robots', content: 'noindex' }]
})
```

### `useHead(input)`

```ts
useHead({
  title: 'Account',
  meta: [{ name: 'description', content: 'Manage your account' }],
  link: [{ rel: 'canonical', href: 'https://example.com/account' }],
  htmlAttrs: { lang: 'en' }
})
```

### `useSeoMeta(input)`

```ts
useSeoMeta({
  title: 'Docs',
  description: 'Resux documentation',
  ogTitle: 'Resux Docs',
  ogImage: '/social-card.png',
  twitterCard: 'summary_large_image'
})
```

SEO fields include common description, robots, author, theme, Open Graph, Facebook, and Twitter metadata.

## Runtime configuration

### `useRuntimeConfig()`

```ts
const config = useRuntimeConfig()
console.log(config.public.apiBase)
```

Only public runtime config is available in browser-resumed code. Keep private keys and server URLs outside `public`.

## Application instance and injection

### `useResuxApp()`

```ts
const app = useResuxApp()
app.provide('analytics', analyticsClient)

const route = app.route
const payload = app.payload
const config = app.$config
const injections = app.provides
```

Plugins receive the same application-style object.

## Error handling

### `createError(input)`

```ts
const error = createError({
  statusCode: 404,
  message: 'Product not found',
  fatal: false,
  data: { productId }
})
```

### `showError(input)`

Set/throw the current application error and stop the active flow:

```ts
showError({
  statusCode: 403,
  message: 'Access denied'
})
```

### `useError()` and `clearError()`

```ts
const currentError = useError()

if (currentError.value) {
  clearError()
}
```

Use the app error component and [App Shell and Errors](/guide/app-shell-errors) for user-facing behavior.

## Lifecycle

### `onMounted(callback)`

Runs browser-only mounted work when the scope resumes:

```ts
onMounted(() => {
  const controller = new AbortController()
  window.addEventListener('resize', updateLayout, {
    signal: controller.signal
  })

  return () => controller.abort()
})
```

Do not access `window` or `document` outside a browser-safe context.

## SFC setup macros

The Resux compiler provides setup-context equivalents for familiar macros:

```ts
const props = defineProps<{ title: string }>()
const emit = defineEmits<{ save: [id: string] }>()
const slots = defineSlots()
const model = defineModel<string>()

defineExpose({ focus })
defineOptions({ name: 'AccountForm' })
```

`emit(...)` is also available in setup context. Only the syntax documented by the compiler subset is supported.

## Server handlers

### `defineEventHandler(handler)` and `eventHandler(handler)`

```ts
export default defineEventHandler(async (event) => {
  const body = await readBody<{ name: string }>(event)
  const query = getQuery(event)
  setHeader(event, 'cache-control', 'no-store')

  return { body, query }
})
```

### `defineServerMiddleware(middleware)`

```ts
export default defineServerMiddleware((event) => {
  setHeader(event, 'x-app', 'resux')
})
```

### Server helper signatures

```ts
const body = await readBody<T>(event)
const query = getQuery(event)
setHeader(event, name, value)
```

Handlers can return JSON-compatible values, strings, `Response` objects, redirects, abort results, or `false` for a forbidden result where supported.

## Framework factories

### `defineResuxConfig(config)`

```ts
export default defineResuxConfig({
  runtimeConfig: {
    public: { appOrigin: 'https://example.com' }
  }
})
```

### `defineResuxPlugin(plugin)`

```ts
export default defineResuxPlugin(async (app) => {
  app.provide('buildLabel', 'production')
})
```

### `defineResuxRouteMiddleware(middleware)`

```ts
export default defineResuxRouteMiddleware((to) => {
  if (to.path.startsWith('/admin')) {
    return navigateTo('/login')
  }
})
```

### `defineResuxModule(module)`

```ts
export default defineResuxModule({
  defaults: { enabled: true },
  setup(options, resux) {
    if (options.enabled) {
      resux.addCss('/module.css')
    }
  }
})
```

See [Modules and Route Rules](/guide/modules-route-rules) for the complete module context.

## Internationalization

When i18n is enabled:

```ts
const {
  locale,
  dir,
  locales,
  t,
  tm,
  setLocale,
  localePath,
  switchLocalePath
} = useI18n()
```

Focused helpers:

```ts
const localePath = useLocalePath()
const switchLocalePath = useSwitchLocalePath()

localePath('/cart', 'ar')
switchLocalePath('ar')
```

Templates can use:

```vue
<p>{{ $t('welcome.greeting', { name: user.name }) }}</p>
```

`$tm(key)` returns raw message catalog data. Nested message lookup uses own properties and blocks unsafe prototype keys.

## Device detection

```ts
const device = useDevice()

if (device.isMobile) {
  // server-safe branch based on request user agent
}
```

Available properties include:

- `isMobile`
- `isTablet`
- `isDesktop`
- `isIos`
- `isAndroid`

The same value is available as `$device` in supported contexts.

## Image URL generation

```ts
const image = useResuxImage()

const src = image('/hero.jpg', {
  width: 1200,
  height: 675,
  quality: 82,
  format: 'webp',
  fit: 'cover',
  cache: '7d'
})
```

See [Media and Optimization](/guide/media).

## Lazy packages

### `useLazyPackage(name, options?)`

```ts
const packageModule = await useLazyPackage('swiper', {
  mode: 'progressive',
  css: ['swiper/css']
})
```

### `useClientPackage(name, options?)`

```ts
const chart = await useClientPackage('chart.js')
```

### Reusable loaders

```ts
const loadEditor = defineLazyPackage('editor-package', {
  mode: 'progressive'
})

const loadBrowserEditor = defineClientOnlyPackage('editor-package')
```

### `usePackageReady(name)`

```ts
const ready = usePackageReady('editor-package')
```

## Client enhancements and package adapters

### `defineClientEnhancement(name, setup)`

```ts
export const tooltip = defineClientEnhancement(
  'tooltip',
  async (target, context) => {
    const instance = await mountTooltip(target, context.options)
    return () => instance.destroy()
  }
)
```

### `useClientEnhancement(name, options?)`

```ts
const enhancement = await useClientEnhancement('tooltip', {
  target: '#help',
  trigger: 'interaction',
  options: { placement: 'bottom' }
})

await enhancement.activate()
await enhancement.dispose()
```

Triggers:

```ts
'visible' | 'interaction' | 'idle' | 'immediate' | 'manual' | 'page-load'
```

### `definePackageAdapter(definition)`

```ts
export const carousel = definePackageAdapter({
  name: 'carousel',
  packageName: 'swiper',
  mode: 'progressive',
  css: ['swiper/css'],
  defaults: { slidesPerView: 1 },
  async enhance(target, options) {
    const { default: Swiper } = await import('swiper')
    const instance = new Swiper(target, options)
    return () => instance.destroy(true, true)
  }
})
```

Read [Third-party Package Integration](/guide/package-integration) for execution modes, bundle controls, and cleanup requirements.

## Serialization and context rules

- State and async data crossing SSR/browser boundaries must be JSON-serializable.
- Private runtime config and server objects must remain server-only.
- Browser-only APIs belong in mounted work, client packages, client enhancements, or islands.
- Node/compiler APIs must not be imported into client handlers.
- Cleanup timers, listeners, observers, requests, and package instances whenever an API provides a cleanup hook.
