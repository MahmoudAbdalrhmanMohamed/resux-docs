# Composables and Globals Reference

Generated apps include types for `resuxjs/globals`, so Resux APIs can be used without imports in app files.

## State

### `useState<T>(key, factory?)`

Create or read a resumable ref.

```ts
const count = useState<number>('count', () => 0)
count.value++
```

- `key`: stable state key.
- `factory`: optional initial value factory.
- Value must be JSON-serializable.

## Reactivity (Resux-native)

Resux ships its own lightweight reactivity system for resumable components. It does not require Vue hydration runtime for normal Resux components.

Use globals in app files, or import from `resuxjs` / `resuxjs/reactivity`.

### `ref<T>(value)`

```ts
const count = ref(0)
count.value++
```

### `reactive<T extends object>(value)`

```ts
const state = reactive({ count: 0 })
state.count++
```

### `computed<T>(getter | { get, set? })`

```ts
const doubled = computed(() => count.value * 2)
```

### `watch(source, callback, options?)`

```ts
watch(count, (next, prev) => {
  console.log(next, prev)
})
```

### `watchEffect(effect, options?)`

```ts
watchEffect((onCleanup) => {
  const id = setInterval(() => console.log(count.value), 1000)
  onCleanup(() => clearInterval(id))
})
```

### `readonly(value)`

```ts
const locked = readonly(state)
```

### `toRef(object, key, defaultValue?)` and `toRefs(object)`

```ts
const state = reactive({ a: 1, b: 2 })
const a = toRef(state, 'a')
const { b } = toRefs(state)
```

### `unref(value)`, `isRef(value)`, `isReactive(value)`, `isReadonly(value)`

```ts
if (isRef(count)) {
  console.log(unref(count))
}
```

### `nextTick(fn?)`

```ts
await nextTick()
```

## Async data

### `useAsyncData<T>(key, handler?)`

Create a resumable async resource.

```ts
const { data, pending, error } = await useAsyncData('stats', ({ signal }) => {
  return $fetch('/api/stats', { signal })
})
```

Return type:

```ts
type AsyncDataResource<T> = {
  data: Ref<T | undefined>
  value: Ref<T | undefined>
  pending: Ref<boolean>
  error: Ref<{ name: string; message: string } | null>
}
```

The resource is thenable, so `await useAsyncData(...)` waits for server-side resolution.

## Routing

### `useRoute()`

```ts
const route = useRoute()
route.path
route.params
route.query
route.origin
```

### `useRouter()`

```ts
const router = useRouter()
await router.push('/about')
router.replace('/login')
router.back()
router.forward()
router.go(-1)
```

## Head

### `useHead(input)`

```ts
useHead({
  title: 'Page title',
  meta: [{ name: 'description', content: 'Description' }],
  link: [{ rel: 'canonical', href: 'https://example.com' }]
})
```

### `useSeoMeta(input)`

```ts
useSeoMeta({
  title: 'Docs',
  description: 'Resux docs',
  ogTitle: 'Docs',
  twitterCard: 'summary_large_image'
})
```

## Config and app

### `useRuntimeConfig()`

```ts
const config = useRuntimeConfig()
config.public.appOrigin
```

### `useResuxApp()`

```ts
const app = useResuxApp()
app.provides
app.provide('key', 'value')
```

## Fetch helpers

### `apiURL(path)`

Resolve internal API URLs for SSR-safe native fetch calls.

```ts
const response = await fetch(apiURL('/api/stats'))
```

### `useFetch<T>(url, init?)`

Fetch JSON and return a ref.

```ts
const data = await useFetch<{ ok: boolean }>('/api/status')
```

### `$fetch<T>(url, init?)`

Fetch JSON and return the parsed value.

```ts
const stats = await $fetch<{ users: number }>('/api/stats')
```

## Lifecycle

### `onMounted(callback)`

Runs when the scope is first resumed in the browser.

```ts
onMounted(() => {
  console.log('browser resumed')
})
```

## Page meta

### `definePageMeta(meta)`

```ts
definePageMeta({
  layout: 'dashboard',
  middleware: ['auth'],
  title: 'Dashboard',
  meta: [{ name: 'robots', content: 'noindex' }]
})
```

## Config and extension factories

### `defineResuxConfig(config)`

```ts
export default defineResuxConfig({
  app: { head: { title: 'App' } },
  runtimeConfig: { public: { appOrigin: 'https://example.com' } }
})
```

### `defineResuxPlugin(plugin)`

```ts
export default defineResuxPlugin((app) => {
  app.provide('name', 'Resux')
})
```

### `defineResuxRouteMiddleware(middleware)`

```ts
export default defineResuxRouteMiddleware((to) => {
  if (to.path === '/admin') return navigateTo('/login')
})
```

### `defineResuxModule(module)`

```ts
export default defineResuxModule({
  setup(options, resux) {
    resux.addCss('/module.css')
  }
})
```

## Server helpers

### `defineEventHandler(handler)` and `eventHandler(handler)`

```ts
export default defineEventHandler(() => ({ ok: true }))
```

### `defineServerMiddleware(middleware)`

```ts
export default defineServerMiddleware((event) => {
  setHeader(event, 'x-app', 'resux')
})
```

### `readBody<T>(event)`

```ts
const body = await readBody<{ name: string }>(event)
```

### `getQuery(event)`

```ts
const query = getQuery(event)
```

### `setHeader(event, name, value)`

```ts
setHeader(event, 'cache-control', 'no-store')
```

## Navigation helpers

### `navigateTo(to, options?)`

```ts
return navigateTo('/login', { statusCode: 302 })
```

### `abortNavigation(message?, options?)`

```ts
return abortNavigation('Not allowed', { statusCode: 403 })
```

## Internationalization (i18n)

### `useI18n()`

Provides access to translation methods and active locale state when `resux:i18n` is enabled.

```ts
const { locale, dir, locales, t, setLocale, localePath, switchLocalePath } = useI18n()
```

### `useLocalePath()` and `useSwitchLocalePath()`

Helper functions for generating localized route URLs based on current or target locale code.

```ts
const localePath = useLocalePath()
const switchLocalePath = useSwitchLocalePath()

const arCart = localePath('/cart', 'ar')
const arPage = switchLocalePath('ar')
```

### `$t(key, params?)` and `$tm(key)`

Global template functions for string translation and raw message catalog access.

```html
<p>{{ $t('welcome.greeting', { name: user.name }) }}</p>
```

## Device Detection

### `useDevice()` and `$device`

SSR-safe device detection helper that inspects the request User-Agent.

```ts
const device = useDevice()
if (device.isMobile) {
  // Mobile rendering layout logic
}
```

Properties returned:
- `isMobile`: `boolean`
- `isTablet`: `boolean`
- `isDesktop`: `boolean`
- `isIos`: `boolean`
- `isAndroid`: `boolean`

## Media & Image Builders

### `useResuxImage()`

Returns a URL builder function for Resux image provider optimization.

```ts
const img = useResuxImage()
const src = img('/banner.png', { width: 800, quality: 80, format: 'webp' })
```

## Progressive Packages & Client Enhancements

### `useLazyPackage<T>(name, options?)` and `useClientPackage<T>(name, options?)`

Dynamically loads third-party packages or client scripts progressively on user interaction or mount.

```ts
const swiper = await useLazyPackage('swiper')
```

### `definePackageAdapter(definition)` & `defineClientEnhancement(name, setup)`

Define custom progressive adapters and client DOM enhancements for client-only interactivity.

```ts
export const vCalendar = definePackageAdapter({
  name: 'v-calendar',
  packageName: 'v-calendar',
  enhance(el, options) {
    // Progressive DOM enhancement setup
  }
})
```

### `useClientEnhancement(name, options?)`

Activates a registered client-side enhancement on demand.

```ts
const { ready, activate, dispose } = await useClientEnhancement('v-calendar')
```

