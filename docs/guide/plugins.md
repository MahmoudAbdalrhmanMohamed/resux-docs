# Plugins

Plugins extend the application context. They can run on the server, browser, or both depending on mode.

## Basic plugin

```ts
// plugins/01.app.ts
export default defineResuxPlugin((app) => {
  app.provide('appName', 'Resux App')
})
```

Read provided values through the app context:

```ts
const app = useResuxApp()
const appName = app.provides.appName
```

For stronger typing, augment `ResuxAppInjections` in an application declaration file.

## Execution modes

Filename suffixes:

```txt
plugins/analytics.client.ts
plugins/database.server.ts
plugins/shared.ts
```

Module-registered plugins can set `mode: 'client' | 'server' | 'all'` explicitly.

- `server`: emitted only for SSR/server setup.
- `client`: emitted only for browser runtime.
- `all`: participates in both where supported.

## Ordering

Plugins are sorted deterministically by normalized file path. Numeric prefixes are a useful way to make order obvious:

```txt
plugins/01.config.ts
plugins/02.analytics.client.ts
```

## Client enhancements

Files under `enhancements/`, `client-enhancements/`, and their `app/` equivalents are discovered as client-mode plugins and registered in the enhancement manifest.

```ts
export default defineClientEnhancement('chart', async (target, context) => {
  const chart = await createChart(target, context.options)
  return () => chart.destroy()
})
```

Use:

```ts
const enhancement = await useClientEnhancement('chart', {
  target: '#sales-chart',
  trigger: 'visible',
  options: { type: 'bar' }
})
```

## Server plugins

`server/plugins/` is reserved for server-only setup and package analysis. Use it for infrastructure initialization that should not become a browser plugin.

## Module-added plugins

```ts
resux.addPlugin({
  src: './runtime/plugin.ts',
  mode: 'client'
})
```

## Rules

- Never put server secrets in a client or all-mode plugin.
- Keep plugin setup deterministic.
- Return/attach cleanup for browser resources through enhancement APIs.
- Prefer server middleware for request-specific behavior.
- Prefer modules for build-time configuration and generated files.
