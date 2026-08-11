# Icon Usage and Registry

## Component imports

```ts
import { Icon, ResuxIcon } from 'resuxjs/icons'
```

`ResuxIcon === Icon`.

## Props

The Vue component declares these props:

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | — | Yes | Registry key or remote Iconify-style name. |
| `size` | `string | number` | `'1.25rem'` | No | SVG width/height. Numeric values become px-style dimensions. |
| `mode` | `string` | `'svg'` | No | Current component metadata prop. The renderer currently emits SVG. |
| `lazy` | `boolean` | `false` | No | Defer unknown/remote fetch until near viewport when IntersectionObserver is available. |
| `loading` | `string` | `'eager'` | No | `loading="lazy"` also activates lazy fetch behavior. |
| `apiProvider` | `string` | `''` | No | Per-component provider override; empty resolves through runtime config/default. |
| `class` | `string` | `''` | No | Additional SVG class string. |

Undeclared Vue attributes are forwarded to the rendered SVG after the component's defaults.

## Size

```vue
<Icon name="check" size="16" />
<Icon name="check" :size="24" />
<Icon name="check" size="1.5rem" />
```

Use CSS-sized strings when you want the icon to scale with typography.

## Color

There is no declared `color` prop in the component. The SVG uses `fill="currentColor"`, so the normal CSS `color` property is the primary styling mechanism:

```vue
<Icon name="check" class="text-success" />
```

You can also forward native SVG/style attributes when needed.

## Registry shape

```ts
export interface IconPathData {
  d: string
  opacity?: string
}

export interface IconData {
  path?: string
  paths?: IconPathData[]
  opacity?: string
  viewBox?: string
}
```

An icon may use one path:

```ts
iconRegistry['app:check'] = {
  viewBox: '0 0 24 24',
  path: 'M…'
}
```

Or multiple paths:

```ts
iconRegistry['app:brand'] = {
  viewBox: '0 0 32 32',
  paths: [
    { d: 'M…', opacity: '0.6' },
    { d: 'M…' }
  ]
}
```

If `viewBox` is absent, the component uses its default SVG view box.

## Extending the registry

`iconRegistry` is an exported mutable object. Register application icons from a deterministic initialization module before the relevant Vue components render:

```ts
import { iconRegistry } from 'resuxjs/icons'

iconRegistry['app:logo'] = {
  viewBox: '0 0 24 24',
  path: 'M…'
}
```

Avoid mutating the registry unpredictably during rendering; treat it as an application-level registry.

## `defineIconCollections()`

```ts
import { defineIconCollections } from 'resuxjs/icons'

const iconOptions = defineIconCollections(['mdi', 'ph'])
```

The helper returns:

```ts
{ collections: ['mdi', 'ph'] }
```

It is a configuration convenience; it does not itself download or register every icon in those collections.

## Decorative icons

Default SVG output is `aria-hidden="true"`:

```vue
<button>
  <Icon name="check" />
  Save
</button>
```

This keeps the icon decorative while the button text supplies the accessible name.

## Semantic icon-only controls

Do not rely on the SVG name string as an accessible label:

```vue
<button type="button" aria-label="Close">
  <Icon name="close" />
</button>
```

The surrounding interactive element should normally own the accessible name.

## SVG attributes

Because attributes are forwarded, you can deliberately override presentation/accessibility attributes for non-interactive semantic SVG usage. Test the resulting accessibility tree rather than assuming all SVG attribute combinations behave consistently.

## SSR / runtime boundary

A registry hit can render complete SVG path markup in the Vue render output without a network request. The icon is still a Vue component, so it belongs in the Vue rendering/island system rather than Resux's zero-hydration template component model.

Remote registry misses require client behavior; see [Runtime Loading](./runtime.md).

## Related

- [Icons overview](./index.md)
- [Runtime Loading](./runtime.md)
- [Configuration](./configuration.md)
