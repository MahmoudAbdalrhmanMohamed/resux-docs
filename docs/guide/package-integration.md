# Third-party Package Integration

Third-party packages do not all belong in the same execution context. Resux lets you declare whether a package runs during SSR, only in the browser, only on the server, or as a progressive enhancement.

## Package modes

```ts
type ResuxPackageMode =
  | 'ssr'
  | 'clientOnly'
  | 'serverOnly'
  | 'progressive'
```

| Mode | Use it when |
| --- | --- |
| `ssr` | The package is safe to import and execute during server rendering |
| `clientOnly` | The package requires `window`, `document`, canvas, browser storage, or another browser API |
| `serverOnly` | The package contains secrets, filesystem access, database clients, or Node-only behavior |
| `progressive` | HTML should render first and the package should enhance a specific element later |

## Configuration

```ts
export default defineResuxConfig({
  packages: {
    lazy: true,
    clientOnly: ['chart.js'],
    serverOnly: ['pg'],
    mode: {
      swiper: 'progressive',
      zod: 'ssr'
    },
    external: ['pg'],
    noExternal: ['some-esm-package'],
    transpile: ['legacy-esm-package'],
    optimizeDeps: ['dayjs'],
    css: {
      swiper: ['swiper/css']
    },
    aliases: {
      '@shared-lib': './lib/shared.ts'
    },
    guards: true,
    diagnostics: true
  }
})
```

## Configuration fields

| Field | Description |
| --- | --- |
| `lazy` | Enable lazy package loading globally or for selected package names |
| `clientOnly` | Packages that must never execute during SSR |
| `serverOnly` | Packages that must never enter client output |
| `mode` | Per-package execution mode |
| `external` | Keep packages external in server bundling |
| `noExternal` | Force packages into server bundling |
| `transpile` | Transpile packages that publish incompatible syntax |
| `optimizeDeps` | Include packages in Vite dependency optimization |
| `css` | Global or per-package CSS imports |
| `aliases` | Package/import aliases |
| `guards` | Enable execution-context guards |
| `diagnostics` | Include package diagnostics in inspect output |

## Lazy loading

```ts
const library = await useLazyPackage<typeof import('some-library')>(
  'some-library',
  {
    mode: 'progressive',
    css: ['some-library/styles.css']
  }
)
```

Useful options include:

- `clientOnly`
- `mode`
- `css`
- `exportName`
- `preferDefault`

Use `useClientPackage()` as the browser-only convenience form:

```ts
const chart = await useClientPackage<typeof import('chart.js')>('chart.js')
```

## Reusable lazy loaders

```ts
const loadEditor = defineClientOnlyPackage<typeof import('some-editor')>(
  'some-editor',
  { css: ['some-editor/editor.css'] }
)

onMounted(async () => {
  const editor = await loadEditor()
  // initialize the editor
})
```

Use `usePackageReady(name)` when a template or enhancement needs to know whether a package was loaded.

## Client enhancements

A client enhancement attaches behavior to existing server-rendered DOM without hydrating the whole component tree.

```ts
export const tooltipEnhancement = defineClientEnhancement(
  'tooltip',
  async (target, context) => {
    const { createTooltip } = await import('./tooltip-client')
    const tooltip = createTooltip(target, context.options)

    return () => {
      tooltip.destroy()
    }
  }
)
```

Activate it:

```ts
const enhancement = await useClientEnhancement('tooltip', {
  target: '#help-button',
  trigger: 'interaction',
  options: { placement: 'bottom' }
})

await enhancement.activate()
await enhancement.dispose()
```

Supported triggers are:

```ts
'visible' | 'interaction' | 'idle' | 'immediate' | 'manual' | 'page-load'
```

Enhancement setup can return a cleanup function. Resux uses cleanup to prevent stale observers, duplicate listeners, and abandoned package instances across navigation or disposal.

## Package adapters

Adapters package a third-party integration into a reusable definition:

```ts
export const carouselAdapter = definePackageAdapter({
  name: 'carousel',
  packageName: 'swiper',
  mode: 'progressive',
  imports: ['Navigation'],
  css: ['swiper/css', 'swiper/css/navigation'],
  defaults: {
    slidesPerView: 1
  },
  validateOptions(options) {
    const slidesPerView = Number(options.slidesPerView)
    if (!Number.isFinite(slidesPerView) || slidesPerView < 1) {
      throw new Error('slidesPerView must be at least 1')
    }
  },
  async enhance(target, options) {
    const { default: Swiper } = await import('swiper')
    const instance = new Swiper(target, options)
    return () => instance.destroy(true, true)
  }
})
```

## Choosing between an enhancement and a Vue island

Use a client enhancement when:

- SSR HTML already represents the content
- the library can attach to one DOM element
- state does not need a complex Vue component tree
- a cleanup function can fully dispose the library

Use a Vue island when:

- the widget is naturally a Vue component
- it relies on Vue provide/inject, component slots, or a complex reactive subtree
- the library provides a Vue wrapper that is safer than raw DOM integration

## Common failure patterns

### Package touches `window` during SSR

Move it to `clientOnly`, use a `.client` plugin, call it from `onMounted`, or create a progressive enhancement.

### CSS is missing

Declare package CSS in `packages.css`, the lazy-package options, a module `addCss()` call, or a client entry imported by the enhancement.

### Duplicate listeners after navigation

Return a cleanup function from the enhancement or adapter and ensure the third-party instance is destroyed.

### Package appears in the wrong bundle

Inspect package diagnostics:

```sh
resux inspect packages --json
resux inspect bundles --json
```

Then correct `mode`, `external`, `noExternal`, `transpile`, or `optimizeDeps`.

## Security rules

- Never expose server-only secrets through a browser package.
- Do not mark database, filesystem, authentication-admin, or private SDK packages as client-only.
- Validate user-controlled enhancement options before passing them to a library.
- Treat dynamically imported code as part of your application security surface.
- Review package licenses, maintenance status, and supply-chain risk before adoption.
