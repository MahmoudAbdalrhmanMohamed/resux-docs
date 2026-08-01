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

Advanced integrations may use `renderAppAsync`, `AsyncResuxRenderer`, template rendering helpers, and server setup context creation.

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

The subpath exposes definitions for routes, handlers, middleware results, components, templates, bindings, app injections, package modes/adapters, media config, head/SEO input, errors, async data, and rendering.

## Stability

Runtime internals are lower-level than application composables. Generated client source shape and internal URLs may evolve; prefer documented high-level APIs for application code.
