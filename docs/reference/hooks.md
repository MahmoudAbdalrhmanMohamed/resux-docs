# Lifecycle Hooks Reference

The hook registry is exported from `resuxjs/core`; module setup can register the same hooks through `ResuxModuleContext.hook()`.

## Register a hook

```ts
export default defineResuxModule({
  setup(_options, resux) {
    const remove = resux.hook('build:done', ({ appRoot, outDir, mode }) => {
      console.log({ appRoot, outDir, mode })
    })

    // remove() unregisters this exact handler.
  }
})
```

## Core signatures

```ts
class ResuxHooks {
  hook<K extends ResuxHookName>(
    name: K,
    handler: ResuxHookHandler<ResuxHookPayloads[K]>
  ): () => void

  addHooks(handlers: Partial<{
    [K in ResuxHookName]:
      | ResuxHookHandler<ResuxHookPayloads[K]>
      | ResuxHookHandler<ResuxHookPayloads[K]>[]
  }>): void

  callHook<K extends ResuxHookName>(
    name: K,
    payload: ResuxHookPayloads[K]
  ): Promise<void>
}

function createResuxHooks(): ResuxHooks
```

## Hook payloads

| Hook | Payload |
| --- | --- |
| `config:resolved` | `{ rootDir: string; buildDir: string; config: Record<string, unknown> }` |
| `app:resolve` | `{ appRoot: string; outDir: string }` |
| `app:templates` | `{ outDir: string; templatesDir: string }` |
| `app:templatesGenerated` | `{ outDir: string; files: string[] }` |
| `pages:extend` | `{ pages: Array<Record<string, unknown>> }` |
| `pages:resolved` | `{ pages: Array<Record<string, unknown>> }` |
| `imports:dirs` | `{ dirs: string[] }` |
| `imports:extend` | `{ imports: Array<Record<string, unknown>> }` |
| `components:dirs` | `{ dirs: string[] }` |
| `components:extend` | `{ components: Array<Record<string, unknown>> }` |
| `plugins:dirs` | `{ dirs: string[] }` |
| `plugins:extend` | `{ plugins: Array<Record<string, unknown>> }` |
| `middleware:dirs` | `{ dirs: string[] }` |
| `middleware:extend` | `{ middleware: Array<Record<string, unknown>> }` |
| `vite:extendConfig` | `{ config: Record<string, unknown>; dev: boolean }` |
| `vite:serverCreated` | `{ server: unknown }` |
| `vite:compiled` | `{ outDir: string; dev: boolean }` |
| `build:before` | `{ appRoot: string; outDir: string; mode: 'dev' | 'build' }` |
| `build:manifest` | `{ manifest: Record<string, unknown>; outDir: string }` |
| `build:done` | `{ appRoot: string; outDir: string; mode: 'dev' | 'build' }` |
| `build:error` | `{ appRoot: string; outDir: string; mode: 'dev' | 'build'; error: unknown }` |
| `nitro:config` | `{ config: Record<string, unknown> }` |
| `nitro:init` | `{ appRoot: string }` |
| `nitro:build:before` | `{ appRoot: string; preset?: string }` |
| `nitro:build:public-assets` | `{ appRoot: string; publicDir: string }` |
| `prepare:types` | `{ outDir: string; files: string[] }` |
| `dev:reload` | `{ appRoot: string; changedPath: string }` |
| `dev:error` | `{ appRoot: string; error: unknown }` |
| `page:loading:start` | `{ path?: string }` |
| `page:loading:end` | `{ path?: string }` |
| `page:finish` | `{ path?: string }` |
| `app:error` | `{ error: unknown }` |
| `app:error:cleared` | `{ path?: string }` |

## Dispatch behavior

Hooks run in registration order.

`callHook()` dispatches a **stable snapshot** of the handler array. If a handler registers or removes another handler while a hook is running, that mutation affects the next dispatch rather than changing the current loop.

Handlers are awaited sequentially. When one throws/rejects, dispatch stops and the error is wrapped as:

```txt
Resux hook "<name>" failed: <message>
```

The original error object is therefore not re-thrown unchanged by `callHook()`.

## Unregistering

`hook()` returns a function that removes the exact registered handler:

```ts
const remove = hooks.hook('page:finish', payload => {
  console.log(payload.path)
})

remove()
```

Removing the last handler for a hook removes that hook's internal entry.

## Bulk registration

```ts
hooks.addHooks({
  'build:before': payload => console.log('start', payload.appRoot),
  'build:done': [
    payload => console.log('done', payload.outDir),
    payload => publishMetrics(payload)
  ]
})
```

A hook value can be one handler or an array of handlers.

## Choosing a hook

Use the latest hook that still gives you the information needed:

- configuration/modules: `config:resolved` and the extension hooks;
- generated files: template/type/build-manifest hooks;
- Vite/Nitro integration: their focused hooks rather than generic build hooks;
- dev tooling: `dev:reload` / `dev:error`;
- application loading/error observation: page/app hooks.

Do not use a hook merely because its name resembles an API from Nuxt. The payload table above is the current Resux contract.

## Environment and runtime cost

Most hooks are build/server lifecycle events. Page loading/error hooks can be surfaced by runtime behavior, but registering low-level Core hooks should still be an intentional integration choice. Hooks do not make an ordinary Resux component Vue-hydrated.

## Related

- [Core API](./core.md)
- [Resux Kit](./kit.md)
- [Modules and Route Rules](/guide/modules-route-rules)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
