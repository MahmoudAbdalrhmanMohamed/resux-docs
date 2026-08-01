# Execution Contexts

Resux code can run during configuration, compilation, server requests, SSR, browser resume, progressive enhancement, or Vue island mounting. The same source file should not assume all contexts are available.

## Context matrix

| Context | Examples | Has request? | Has browser DOM? | May contain secrets? |
| --- | --- | ---: | ---: | ---: |
| Configuration | `resux.config.ts` | No | No | Build environment only |
| Module setup | `modules/*`, npm module | No | No | Avoid exposing through public config |
| Core hooks | build/Vite/Nitro hooks | Depends on hook | Usually no | Yes when server/build only |
| Server plugin | `server/plugins/*` | No direct request | No | Yes |
| Request middleware | `server/middleware/*` | Yes | No | Yes |
| Server handler | `server/api/*`, `server/routes/*` | Yes | No | Yes |
| Route middleware | `middleware/*` | Route context | Client mode may run in browser | Do not expose secrets |
| Plugin | `plugins/*` | SSR plugin sees app context | Client mode may run in browser | Depends on mode |
| Component setup | page/layout/component | During SSR | No during SSR | No private secrets in serialized output |
| Resumable event | `@click`, `@submit` | No server request | Yes | Never |
| `onMounted` | resumed scope | No | Yes | Never |
| Client enhancement | `enhancements/*` | No | Yes | Never |
| Vue island | `islands/vue/*` | No | Yes | Never |

## Build-time modules

Modules can add components, imports, plugins, middleware, server handlers, templates, types, route rules, prerender routes, Vite plugins, and Nitro configuration.

```ts
import { defineResuxModule, addTemplate, addTypeTemplate } from 'resuxjs/kit'

export default defineResuxModule({
  meta: { name: 'example', configKey: 'example' },
  defaults: { enabled: true },
  setup(options) {
    if (!options.enabled) return

    addTemplate({
      filename: 'example.mjs',
      getContents: () => 'export const enabled = true'
    })

    addTypeTemplate({
      filename: 'example.d.ts',
      getContents: () => 'declare const exampleEnabled: boolean'
    })
  }
})
```

Kit helpers throw when called outside active module setup.

## Server-only work

Use server handlers, middleware, server plugins, and `server/utils` for:

- database connections,
- private tokens,
- filesystem access,
- signed cookies,
- privileged network requests,
- and private runtime configuration.

```ts
export default defineEventHandler(async (event) => {
  const body = await readBody<unknown>(event)
  const saved = Boolean(
    body &&
    typeof body === 'object' &&
    !Array.isArray(body) &&
    'name' in body &&
    typeof body.name === 'string' &&
    body.name.trim()
  )

  return { saved }
})
```

## SSR component setup

Component setup creates HTML and resumable state. It must tolerate server execution.

```ts
const route = useRoute()
const config = useRuntimeConfig()
const result = await useAsyncData('record', () => $fetch(`/api/records/${route.params.id}`))
```

Do not read `window`, `document`, storage, or browser constructors directly during setup.

## Browser resume and cleanup

`onMounted` queues work for the first browser resume, but its return value is not a disposal hook. Put long-lived browser resources in a client enhancement whose setup returns cleanup.

```ts
// enhancements/window-resize.ts
export const windowResizeEnhancement = defineClientEnhancement(
  'window-resize',
  () => {
    const onResize = () => console.log(window.innerWidth)
    window.addEventListener('resize', onResize)

    return () => window.removeEventListener('resize', onResize)
  }
)
```

```ts
onMounted(async () => {
  const enhancement = await useClientEnhancement('window-resize', {
    trigger: 'immediate'
  })

  await enhancement.activate()
})
```

Resux calls enhancement cleanup during navigation or explicit disposal.

## Environment boundaries

- Private `runtimeConfig` stays on the server.
- `runtimeConfig.public` is serialized.
- Plugin and middleware suffixes control server/client participation.
- `serverOnly` packages must never be imported by browser sources.
- `clientOnly` packages should not be executed during SSR.
- `progressive` packages should activate through an adapter or enhancement trigger.

Use [Third-party Packages](/guide/package-integration) and [Plugins](/guide/plugins) for concrete patterns.
