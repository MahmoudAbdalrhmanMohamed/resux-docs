# Integration Cookbook

This cookbook turns the generic [third-party package model](./package-integration.md) into repeatable recipes. Resux is a web/TypeScript framework, so these recipes cover browser and Node packages rather than Flutter packages.

The same rule applies to every integration: **render useful HTML first, then load browser-only behavior only where it is needed**.

## Choose the integration shape first

| Integration shape | Use it for | Resux tools |
| --- | --- | --- |
| SSR-safe library | parsing, validation, date/utility functions | `packages.mode[name] = 'ssr'`, normal imports |
| Progressive DOM enhancement | carousels, charts, players, editors | `progressive`, `defineClientEnhancement`, `useClientEnhancement` |
| Browser-only SDK | maps, camera, payment elements | `clientOnly`, `useClientPackage`, `.client` plugin |
| Vue component tree | complex Vue wrappers and stateful widgets | `<VueIsland>` + explicit component imports |
| Server-only SDK | private auth/admin clients, database/service secrets | `serverOnly`, server handlers/APIs |

Recommended project structure:

```text
app/
  components/
    integrations/
  composables/
  enhancements/
  plugins/
  server/
    api/
    services/
  types/
resux.config.ts
```

Keep vendor initialization in `integrations/`, `enhancements/`, or `server/services/`. Pages should consume a small application-facing API instead of containing vendor setup code.

## Swiper

### Install

```sh
npm install swiper
```

### Configure Resux

```ts
export default defineResuxConfig({
  packages: {
    mode: { swiper: 'progressive' },
    css: {
      swiper: ['swiper/css', 'swiper/css/navigation', 'swiper/css/pagination']
    }
  }
})
```

### Progressive enhancement

Server-render the slides as ordinary HTML so links and content remain useful without JavaScript.

```ts
// enhancements/swiper.client.ts
export const swiperEnhancement = defineClientEnhancement('swiper', async (target, context) => {
  const [{ default: Swiper }, { Navigation, Pagination }] = await Promise.all([
    import('swiper'),
    import('swiper/modules')
  ])

  const instance = new Swiper(target, {
    modules: [Navigation, Pagination],
    slidesPerView: 1,
    navigation: true,
    pagination: { clickable: true },
    ...(context.options || {})
  })

  return () => instance.destroy(true, true)
})
```

### Best practices

- Keep slide text/images in SSR HTML.
- Load Swiper only when the carousel is visible or interacted with.
- Destroy the instance during cleanup.
- Give navigation controls accessible labels.
- Avoid importing every Swiper module.

Common mistakes are importing Swiper during SSR, loading its entire CSS bundle globally for one carousel, and recreating instances on every navigation without cleanup.

**Lab verification:** `/package-tests/swiper` covers the SSR-first progressive pattern.

## Google Maps

Google Maps JavaScript is browser-only. Do not execute it during SSR.

### Install

Use Google's loader package when you want npm-managed loading:

```sh
npm install @googlemaps/js-api-loader
```

### Runtime config

A browser Maps key is public by design, but it must be restricted by HTTP referrer and enabled APIs in Google Cloud.

```ts
export default defineResuxConfig({
  packages: {
    mode: { '@googlemaps/js-api-loader': 'clientOnly' }
  },
  runtimeConfig: {
    public: {
      googleMapsKey: process.env.GOOGLE_MAPS_BROWSER_KEY
    }
  }
})
```

### Client integration

```ts
const loaderPackage = await useClientPackage<typeof import('@googlemaps/js-api-loader')>(
  '@googlemaps/js-api-loader'
)

const loader = new loaderPackage.Loader({
  apiKey: useRuntimeConfig().public.googleMapsKey,
  version: 'weekly'
})

const { Map } = await loader.importLibrary('maps')
const map = new Map(target, {
  center: { lat: 30.0444, lng: 31.2357 },
  zoom: 11
})
```

### Best practices

- Render an address, directions link, or static placeholder during SSR.
- Load interactive maps on visibility or interaction rather than page load.
- Restrict browser keys by origin and API.
- Never put a server/private Google credential in `runtimeConfig.public`.
- Dispose listeners when the target is removed.

Recommended structure: `components/integrations/MapPlaceholder.vue`, `enhancements/google-map.client.ts`, and server geocoding under `server/services/` when private credentials are required.

## Video players

Use the native `<video>` element as the SSR fallback. Add a player library progressively only when richer controls are needed.

### Plyr example

```sh
npm install plyr
```

```ts
export default defineResuxConfig({
  packages: {
    mode: { plyr: 'progressive' },
    css: { plyr: ['plyr/dist/plyr.css'] }
  }
})
```

```ts
export const playerEnhancement = defineClientEnhancement('player', async (target) => {
  const { default: Plyr } = await import('plyr')
  const player = new Plyr(target)
  return () => player.destroy()
})
```

Performance rules:

- Do not autoplay large video unless the product requires it.
- Use `preload="metadata"` or `preload="none"` for non-hero media.
- Provide poster images and captions.
- Lazy-load the player library; the native video should work first.

**Lab verification:** `/package-tests/video-player` and `/media-test/video`.

## PDF viewers

`pdfjs-dist` uses browser APIs and a worker. Treat the visual viewer as client-only; keep a normal PDF link in SSR HTML.

```sh
npm install pdfjs-dist
```

```ts
export default defineResuxConfig({
  packages: {
    mode: { 'pdfjs-dist': 'clientOnly' }
  }
})
```

Configure the worker in the client-only PDF adapter before the first document is loaded:

```ts
import workerUrl from 'pdfjs-dist/build/pdf.worker.mjs?url'

const pdfjs = await useClientPackage<typeof import('pdfjs-dist')>('pdfjs-dist')
pdfjs.GlobalWorkerOptions.workerSrc = workerUrl

const documentTask = pdfjs.getDocument('/files/guide.pdf')
const pdf = await documentTask.promise
const page = await pdf.getPage(1)
// render the page to a canvas owned by the client integration
```

Keep worker configuration in one adapter module so upgrades do not spread through pages. Verify the worker URL resolves in the production build. Avoid rendering dozens of pages immediately; render visible pages and release canvases when they leave the working set.

Common mistakes: trying to render canvas on the server, forgetting the worker asset, and removing the ordinary download/open link.

## Charts

Charts are usually best as progressive enhancements. The server should render a heading, summary, table, or key metrics first.

### Chart.js

```sh
npm install chart.js
```

```ts
export default defineResuxConfig({
  packages: { mode: { 'chart.js': 'progressive' } }
})
```

```ts
export const chartEnhancement = defineClientEnhancement('chart', async (target, context) => {
  const { Chart, registerables } = await import('chart.js')
  Chart.register(...registerables)
  const chart = new Chart(target as HTMLCanvasElement, context.options as any)
  return () => chart.destroy()
})
```

For large dashboards, import only the Chart.js controllers/scales you use or consider ECharts with on-demand imports. Avoid placing raw chart-only information behind canvas; keep an accessible SSR summary/table.

**Lab verification:** `/package-tests/chart` and `/package-tests/echarts`.

## Date pickers

For a simple date input, prefer the built-in [`RxDatePicker`](../reference/ui.md#rxdatepicker--resuxdatepicker) inside a Vue island. It avoids another dependency.

For advanced calendars/ranges, use a client-only package such as Flatpickr:

```sh
npm install flatpickr
```

```ts
export default defineResuxConfig({
  packages: {
    mode: { flatpickr: 'progressive' },
    css: { flatpickr: ['flatpickr/dist/flatpickr.css'] }
  }
})
```

```ts
export const datePickerEnhancement = defineClientEnhancement('date-picker', async (target, context) => {
  const { default: flatpickr } = await import('flatpickr')
  const instance = flatpickr(target as HTMLInputElement, context.options || {})
  return () => instance.destroy()
})
```

Keep a real `<input type="date">` or text input as the baseline. Validate and normalize dates on the server as well as the client.

## Camera and microphone

No package is required for basic capture. `navigator.mediaDevices.getUserMedia()` is browser-only and requires a secure context (`https` or localhost) plus explicit user permission.

```ts
async function openCamera(video: HTMLVideoElement) {
  if (!navigator.mediaDevices?.getUserMedia) {
    throw new Error('Camera capture is not supported in this browser.')
  }

  const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false })
  video.srcObject = stream
  return () => stream.getTracks().forEach(track => track.stop())
}
```

Best practices:

- Start capture only after a user action.
- Explain why permission is needed before prompting.
- Stop every media track on navigation/unmount.
- Never assume permission state is permanent.
- Provide upload/file fallback when camera access is unavailable.

## File picker and uploads

The most portable file picker is native HTML:

```html
<input type="file" accept="image/*,.pdf" multiple>
```

For drag/drop or custom UI, progressively enhance the native input. The File System Access API can be offered as an optional capability, not the only flow.

Upload files to a server endpoint with `FormData`; validate size, MIME/content, authorization, and storage rules on the server. Client `accept` is only a hint and is not a security boundary.

Recommended structure:

```text
components/integrations/FilePicker.vue
server/api/uploads.post.ts
server/services/storage.ts
```

## Permission handling

Use capability detection first, then the Permissions API where it is actually supported.

```ts
async function readPermission(name: PermissionName) {
  if (typeof navigator === 'undefined' || !('permissions' in navigator)) {
    return 'unsupported'
  }

  try {
    return (await navigator.permissions.query({ name })).state
  } catch {
    return 'unknown'
  }
}
```

The `typeof navigator` check makes the helper safe if it is reached during SSR; permission queries should still normally run only after client initialization or a user-driven browser flow.

Do not use a permission query as a substitute for calling the real browser API. Browsers expose different permission names and behaviors. Handle `denied`, unavailable APIs, and re-prompt behavior explicitly.

## Authentication SDKs

Split authentication into two responsibilities:

1. a browser SDK may initiate login or retrieve a public identity token;
2. the server verifies tokens, creates application sessions, and guards private data.

Do not make browser local storage the source of truth for authorization.

```ts
export default defineResuxConfig({
  packages: {
    mode: {
      'vendor-browser-auth': 'clientOnly',
      'vendor-admin-sdk': 'serverOnly'
    }
  },
  runtimeConfig: {
    authClientId: process.env.AUTH_CLIENT_ID,
    authClientSecret: process.env.AUTH_CLIENT_SECRET,
    public: {
      authClientId: process.env.PUBLIC_AUTH_CLIENT_ID
    }
  }
})
```

Only values intended to be public belong under `runtimeConfig.public`.

## Firebase

Use Firebase's modular client SDK for browser features and keep Firebase Admin server-only.

```sh
npm install firebase firebase-admin
```

```ts
export default defineResuxConfig({
  packages: {
    mode: {
      firebase: 'clientOnly',
      'firebase-admin': 'serverOnly'
    }
  }
})
```

Client initialization can live in `plugins/firebase.client.ts` or a small lazy loader. Admin initialization belongs in `server/services/firebase-admin.ts` and reads private runtime configuration.

Best practices:

- Reuse one app instance rather than initializing per component.
- Import modular Firebase functions instead of compatibility bundles.
- Enforce Firestore/Storage Security Rules; hiding UI is not authorization.
- Verify auth tokens on the server before privileged operations.

## Supabase

```sh
npm install @supabase/supabase-js
```

The browser may use the project URL and anonymous/publishable key. Service-role keys are server-only.

```ts
export default defineResuxConfig({
  packages: {
    mode: { '@supabase/supabase-js': 'ssr' }
  },
  runtimeConfig: {
    supabaseServiceRole: process.env.SUPABASE_SERVICE_ROLE_KEY,
    public: {
      supabaseUrl: process.env.PUBLIC_SUPABASE_URL,
      supabaseAnonKey: process.env.PUBLIC_SUPABASE_ANON_KEY
    }
  }
})
```

Create separate browser and server adapters so the service-role key can never enter browser code. Rely on Row Level Security for client-accessible data and verify session/cookies in server APIs.

## Stripe

Use Stripe.js in the browser and the `stripe` Node SDK on the server.

```sh
npm install @stripe/stripe-js stripe
```

```ts
export default defineResuxConfig({
  packages: {
    mode: {
      '@stripe/stripe-js': 'clientOnly',
      stripe: 'serverOnly'
    }
  },
  runtimeConfig: {
    stripeSecretKey: process.env.STRIPE_SECRET_KEY,
    stripeWebhookSecret: process.env.STRIPE_WEBHOOK_SECRET,
    public: {
      stripePublishableKey: process.env.PUBLIC_STRIPE_PUBLISHABLE_KEY
    }
  }
})
```

```ts
const { loadStripe } = await useClientPackage<typeof import('@stripe/stripe-js')>(
  '@stripe/stripe-js'
)
const stripe = await loadStripe(useRuntimeConfig().public.stripePublishableKey)
```

Create PaymentIntents/Checkout Sessions on the server, not in the browser. Verify webhook signatures against the **raw** request body. Never expose `sk_...` or service secrets through `public` config.

## Editors, syntax highlighting, and markdown

The same execution model covers other common packages:

- markdown parser (`marked`, `markdown-it`): often `ssr`
- syntax highlighter (`highlight.js`, Shiki): SSR or progressive depending on bundle size
- DOM editor (Monaco, CodeMirror, TipTap): client-only or Vue island
- animation (`gsap`, `animejs`): progressive enhancement
- utility packages (`date-fns`, `lodash-es`): SSR-safe, import only needed functions

**Lab verification:** the `/package-tests` routes exercise markdown, highlighting, utilities, GSAP, Anime.js, Swiper, Chart.js, ECharts, Plyr, CSS-package loading, missing-package diagnostics, and multiple enhancement triggers.

## Common mistakes across integrations

1. Importing a browser SDK at module top level when SSR executes the file.
2. Putting private credentials in `runtimeConfig.public`.
3. Replacing meaningful server HTML with an empty client-only box.
4. Loading a heavy library on every route.
5. Forgetting CSS/worker assets.
6. Forgetting cleanup for listeners, observers, streams, maps, charts, and players.
7. Treating client validation as authorization or security validation.
8. Initializing one SDK instance per component instead of using a shared adapter.
9. Swallowing package-load errors instead of giving a fallback and useful diagnostics.

## Performance checklist

For every new integration, answer these before shipping:

- Can the page render useful HTML without the package?
- Can activation wait for `visible`, `interaction`, or `idle`?
- Is the package restricted to the routes that need it?
- Are only required modules/locales/styles imported?
- Does cleanup free listeners, observers, canvases, workers, media tracks, and SDK instances?
- Is there an accessible non-canvas/non-map fallback where the content matters?
- Are secrets guaranteed to stay server-only?

Use `resux inspect packages --json` and `resux inspect bundles --json` when a dependency appears in the wrong execution context or bundle.

## Verification policy

The `resux-lab` repository is the executable compatibility bench. Local, credential-free integrations are expected to compile and run there. Provider integrations that require private accounts/keys (Google Maps, Firebase Admin, Supabase service role, Stripe server/webhooks) are source/configuration patterns and must be exercised with dedicated test credentials before production use; documentation must not pretend those external services were contacted when credentials were not supplied.
