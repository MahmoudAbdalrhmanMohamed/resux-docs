# Plugins

Plugins run during app rendering and can provide values to the Resux app instance.

## Create a plugin

```ts
// plugins/app.ts
export default defineResuxPlugin((resuxApp) => {
  resuxApp.provide('version', '0.2.23')
})
```

## Read the app instance

```vue
<script setup lang="ts">
const app = useResuxApp()
const version = app.provides.version
</script>

<template>
  <small>Version: {{ version }}</small>
</template>
```

## Plugin context

A plugin receives a `ResuxAppLike` object:

```ts
type ResuxAppLike = {
  route: RouteContext
  payload: ResuxPayload
  $config: RuntimeConfig
  provides: Record<string, unknown>
  provide(key: string, value: unknown): void
}
```

## Plugin modes

The compiler recognizes plugins from `plugins/`. The build manifest records a plugin mode of `all`, `server`, or `client`. Keep plugin side effects explicit and test them with `resux inspect --json`.

## Good plugin use cases

- Provide simple app-wide values.
- Initialize serializable services.
- Read public runtime config.
- Add tiny helpers that pages can access through `useResuxApp()`.

Avoid hiding large client-only runtime behavior in plugins. Use Vue islands for complex browser widgets.
