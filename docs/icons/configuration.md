# Icon Configuration

## Module options

```ts
export interface ResuxIconsModuleOptions {
  collections?: string[]
  component?: string
  mode?: 'css' | 'svg'
  apiProvider?: string
  lazy?: boolean
}
```

| Option | Default | Description |
| --- | --- | --- |
| `collections` | `[]` | Collection names exposed by module/runtime configuration. This does not automatically bundle/download every icon. |
| `component` | `'Icon'` | Component registration/configuration name. |
| `mode` | `'svg'` | Rendering mode metadata. The current `Icon` component renderer emits SVG. |
| `apiProvider` | built-in Iconify-compatible provider | Default remote provider base URL after normalization. |
| `lazy` | `false` | Runtime/module configuration flag. See the component note below. |

## Correct defaults

Use the source defaults, not assumptions from other icon libraries:

```ts
['resuxjs/icons', {
  collections: [],
  component: 'Icon',
  mode: 'svg',
  lazy: false
}]
```

## Component vs module `lazy`

The current `Icon` component decides lazy fetching from its **component props**:

- `lazy` prop (default false), or
- `loading="lazy"`.

Although the module stores a `lazy` value in public icon runtime configuration, the component's `isLazy` decision in the current implementation does not read that runtime `lazy` field. Therefore, do not promise that setting only module `lazy: true` automatically makes every imported `Icon` instance lazy.

Use an explicit component prop when you need the behavior today:

```vue
<Icon name="ph:camera" lazy />
```

## `mode`

Both module options and the component expose a mode surface, but the current Vue icon renderer produces an `<svg>` in the implementation path documented here. Do not document CSS-mask/span rendering as an implemented component mode until source behavior exists and tests cover it.

## Collections

`collections` is useful metadata/configuration, but the current icon package is not a full build-time Iconify collection bundler. Known registry entries live in `iconRegistry`; unknown names may be fetched remotely at runtime.

Do not claim tree-shaking of arbitrary remote collection JSON or local `@iconify-json/*` bundle scanning: those capabilities are not implemented by this module today.

## Provider

```ts
['resuxjs/icons', {
  apiProvider: 'https://icons.example.com'
}]
```

The normalized provider is exposed in public runtime config and used as the default provider for remote component requests unless `apiProvider` is supplied directly on the component.

Provider configuration is public and must never contain credentials.

## Public runtime config

Module setup exposes icon configuration under public runtime configuration, including component name, collections, mode, provider, and lazy metadata.

## Security

A remote provider means browser/client code fetches icon data over the network. Apply appropriate:

- CSP `connect-src` rules;
- HTTPS/provider trust requirements;
- availability/reliability expectations;
- privacy review;
- application fallback behavior.

For critical icons that must render without remote availability, register them in `iconRegistry`.

## Related

- [Icons overview](./index.md)
- [Usage and Registry](./usage.md)
- [Runtime Loading](./runtime.md)
