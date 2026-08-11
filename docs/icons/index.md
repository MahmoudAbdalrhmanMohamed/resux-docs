# Icons

`resuxjs/icons` provides a Vue SVG icon component, an exported local SVG-path registry, optional Iconify-compatible remote fetching, request caching/deduplication, and visibility-based lazy fetching.

::: warning Vue runtime boundary
`Icon` / `ResuxIcon` are Vue components. Use them inside a [Vue island](/guide/vue-islands) or another explicit Vue runtime context. This package does not turn a normal Resux template subtree into a resumable icon component automatically.
:::

## Basic usage

```vue
<script setup lang="ts">
import { Icon } from 'resuxjs/icons'
</script>

<template>
  <Icon name="check" size="1.25rem" />
</template>
```

`ResuxIcon` from `resuxjs/icons` is an alias of `Icon`.

::: info Different from `resuxjs/ui`
`resuxjs/ui` also exports an `RxIcon` / `ResuxIcon` placeholder primitive that renders text such as `[check]`. For actual SVG registry/provider behavior, import from `resuxjs/icons`.
:::

## Local registry first

If `name` matches an entry in the exported `iconRegistry`, the component renders that SVG data directly. Built-in/local registry icons do not need a remote fetch.

```ts
import { iconRegistry } from 'resuxjs/icons'

iconRegistry['company:mark'] = {
  viewBox: '0 0 32 32',
  paths: [
    { d: 'M…' },
    { d: 'M…', opacity: '0.7' }
  ]
}
```

See [Usage and Registry](./usage.md).

## Remote icons

When a name is not found locally, the component can fetch icon data from its resolved Iconify-compatible API provider. Remote behavior is client-side: built-in registry data can render immediately, while an unknown/remote icon initially has fallback SVG data until the client fetch succeeds.

```vue
<Icon name="ph:check-circle" />
```

See [Runtime Loading](./runtime.md) for caching, lazy fetching, SSR behavior, and failure handling.

## Module configuration

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/icons', {
      component: 'Icon',
      mode: 'svg',
      apiProvider: 'https://api.iconify.design',
      collections: ['ph', 'mdi'],
      lazy: false
    }]
  ]
})
```

The current defaults are:

- `collections: []`
- `component: 'Icon'`
- `mode: 'svg'`
- default Iconify-compatible provider
- `lazy: false`

See [Configuration](./configuration.md) before assuming every module option changes component rendering; some options are exposed as runtime/module metadata while the current component has its own prop defaults.

## Accessibility default

The rendered SVG sets `aria-hidden="true"` by default, which is appropriate for decorative icons paired with visible text.

```vue
<button type="button">
  <Icon name="check" />
  Confirm
</button>
```

For a standalone semantic icon, supply a real accessible name through surrounding markup or explicit SVG attributes and test it. Attributes are forwarded to the SVG, so an explicit `aria-hidden`/role/label can override the default when intentionally supplied.

## Styling

The component renders an inline SVG with:

- `fill="currentColor"`
- inline size styles
- baseline classes including inline/shrink/vertical alignment helpers plus your `class`

Set color through normal CSS/currentColor:

```vue
<Icon name="check" class="success-icon" />
```

```css
.success-icon { color: #16a34a; }
```

## Related

- [Usage and Registry](./usage.md)
- [Configuration](./configuration.md)
- [Runtime Loading](./runtime.md)
- [Button](/components/button)
- [Vue Islands](/guide/vue-islands)
