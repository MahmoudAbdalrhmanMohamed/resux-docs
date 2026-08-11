# Runtime Reference

The runtime package contains server rendering definitions, application composables, route/payload types, and the generated browser runtime source.

## Server rendering

```ts
import { renderApp, renderDocument } from 'resuxjs/runtime'

const result = await renderApp({
  page,
  route,
  components,
  layouts,
  runtimeConfig,
  appHead,
  plugins
})

const html = renderDocument(result)
```

Advanced integrations may use `renderAppAsync`, `AsyncResuxRenderer`, `renderTemplateNodesAsync`, expression/patch helpers, and server setup context creation.

## Component model

The runtime represents compiled components with:

- a server setup function,
- template nodes,
- handlers,
- styles,
- optional page metadata,
- and stable module identifiers.

## Payload

```ts
type ResuxPayload = {
  route: RouteContext
  scopes: Record<string, SerializedScope>
  modules: Record<string, string>
  vueIslands?: Record<string, string>
  config?: RuntimeConfig
  plugins?: ClientPluginManifestRecord[]
  middleware?: ClientRouteMiddlewareManifestRecord[]
  pageMeta?: PageMeta
}
```

## Device parsing

`parseUserAgent()` is a public low-level utility used by the runtime's device helpers.

```ts
import { parseUserAgent } from 'resuxjs/runtime'

const device = parseUserAgent(request.headers.get('user-agent') ?? '')
```

```ts
interface DeviceInfo {
  isMobile: boolean
  isTablet: boolean
  isDesktop: boolean
  isIos: boolean
  isAndroid: boolean
  [key: string]: boolean
}

function parseUserAgent(ua?: string): DeviceInfo
```

The current implementation derives those booleans from user-agent string patterns. Treat the result as lightweight feature/context classification rather than authoritative device detection.

## Browser runtime

`getClientRuntimeSource()` generates the delegated resume runtime used by compiler output. It supports event dispatch, patches, navigation, plugins, client middleware, packages, enhancements, and cleanup.

## Client enhancements

Advanced APIs include:

- `defineClientEnhancement`
- `getClientEnhancement`
- `hasClientEnhancement`
- `scanClientEnhancements`
- `useClientEnhancement`
- `disposeClientEnhancements`

## Runtime types

The subpath exposes definitions for routes, handlers, middleware results, components, templates, bindings, app injections, package modes/adapters, media config, head/SEO input, errors, async data, device information, and rendering.

## Stability

Runtime internals are lower-level than application composables. Generated client source shape and internal URLs may evolve; prefer documented high-level APIs for application code.
