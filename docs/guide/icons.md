# Icons (`resuxjs/icons`)

The icons package provides a build-time module and a Vue runtime icon component backed by a local registry and optional Iconify-compatible HTTP provider.

::: warning Runtime boundary
`Icon` and `ResuxIcon` are Vue components. Use them inside a Vue island or another Vue/client runtime context. Registering the module can expose configuration and a named component, but it does not turn normal Resux components into hydrated Vue components.
:::

## Module configuration

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/icons', {
      component: 'Icon',
      mode: 'svg',
      apiProvider: 'https://api.iconify.design',
      collections: ['material-symbols', 'mdi', 'ph'],
      lazy: true
    }]
  ]
})
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `collections` | `string[]` | built-in/default list | Collections intended for the app. |
| `component` | `string` | `Icon` | Registered component name. |
| `mode` | `'css' \| 'svg'` | `'svg'` | Rendering mode metadata. Current component renders SVG. |
| `apiProvider` | `string` | Iconify API | Base URL used for dynamic icon fetching. |
| `lazy` | `boolean` | `true` | Defer fetching until the icon becomes visible where supported. |

The normalized provider is stored in public runtime config so client instances use the same endpoint.

## Use in a Vue island

```vue
<script setup lang="ts">
import { ResuxIcon } from 'resuxjs/icons'
</script>

<template>
  <ResuxIcon
    name="ph:check-circle"
    size="1.5rem"
    color="currentColor"
    lazy
  />
</template>
```

## Local registry

Frequently used icons are available from `iconRegistry`. Registry records can contain one path or multiple paths with optional opacity and a custom `viewBox`.

```ts
import { iconRegistry } from 'resuxjs/icons'

iconRegistry['company:logo'] = {
  viewBox: '0 0 32 32',
  paths: [
    { d: '...', opacity: '0.7' },
    { d: '...' }
  ]
}
```

Use a stable application initialization point when extending the registry.

## Dynamic fetching

```ts
import { fetchIconifyIcon } from 'resuxjs/icons'

const data = await fetchIconifyIcon(
  'ph:check-circle',
  'https://api.iconify.design'
)
```

Dynamic behavior includes:

- provider URL normalization,
- cache keys that include provider and icon name,
- concurrent request deduplication,
- multi-path SVG parsing,
- safe fallback when a request fails,
- and stale-request protection when the component's name/provider changes before a request finishes.

## Lazy loading

When lazy mode is enabled and `IntersectionObserver` exists, the component waits until it approaches the viewport. Without observer support it loads immediately.

## Custom providers

Use HTTPS for public providers. Only configure a provider you trust because the client requests SVG data from it. Apply CSP and network allow-lists appropriate to your application.

```ts
['resuxjs/icons', {
  apiProvider: 'https://icons.example.com'
}]
```

## Helper

```ts
import { defineIconCollections } from 'resuxjs/icons'

const options = defineIconCollections(['mdi', 'ph'])
```

## Troubleshooting

- Confirm the icon name uses `collection:name` format.
- Confirm the provider returns Iconify-compatible JSON/SVG data.
- Check CSP `connect-src`.
- Check the element actually intersects the viewport when `lazy` is active.
- Use a local registry entry for critical icons that must not depend on a remote service.
