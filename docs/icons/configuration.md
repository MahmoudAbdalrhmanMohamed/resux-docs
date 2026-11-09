# Icon Configuration

Resux provides full configuration control over icon sizes, rendering modes, aliases, offline collections, and custom local icon directories.

## Module options (`ResuxIconsModuleOptions`)

```ts
// resux.config.ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/icons', {
      component: 'Icon',
      defaultSize: '1.25rem',
      mode: 'svg', // 'svg' or 'css'
      collections: ['lucide', 'ph', 'mdi'],
      aliases: {
        github: 'lucide:github',
        twitter: 'lucide:twitter',
        mail: 'lucide:mail',
      },
      customCollectionsDir: './assets/icons',
      ssr: true,
      apiProvider: 'https://api.iconify.design',
      lazy: false,
    }]
  ]
})
```

## Options reference

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `component` | `string` | `'Icon'` | Name of the component globally registered/available in templates. |
| `defaultSize` | `string` | `'1em'` | Default width and height applied when no explicit `size` prop is provided. |
| `mode` | `'svg' \| 'css'` | `'svg'` | Default rendering mode. `'svg'` produces full vector paths; `'css'` renders a `<span>` with CSS `mask` / `background`. |
| `collections` | `string[]` | `[]` | List of enabled icon collections (e.g. `['lucide', 'mdi']`). |
| `aliases` | `Record<string, string>` | `{}` | Custom shorthand aliases mapping friendly names to collection names (e.g. `{ logo: 'custom:brand-logo' }`). |
| `customCollectionsDir` | `string` | `'./assets/icons'` | Path to the directory containing local `.svg` files for `custom:*` icons. |
| `ssr` | `boolean` | `true` | When `true`, statically resolvable icons render directly during SSR. When `false`, icons render on the client only. |
| `apiProvider` | `string` | `'https://api.iconify.design'` | Base URL for remote Iconify-compatible API fallback requests. |
| `lazy` | `boolean` | `false` | Default loading strategy across icons. |

## Aliases configuration

Aliases let you define concise names for commonly used icons:

```ts
aliases: {
  home: 'lucide:home',
  check: 'ph:check-circle',
  brand: 'custom:company-logo',
}
```

In templates, you can then write:

```vue
<Icon name="home" />
<Icon name="brand" />
```

Resux resolves aliases recursively, preventing circular loops while ensuring that built-in aliases (like `check`, `mail`, `search`) and custom user aliases are resolved cleanly.

## Offline collections configuration

When an icon collection package such as `@iconify-json/lucide` is installed in your project:

```sh
npm install -D @iconify-json/lucide
```

Resux detects the installed package and resolves icon SVG data at build-time. This eliminates runtime API requests and enables compile-time inlining into your production bundles.

## Custom local icons directory

By default, Resux looks in `./assets/icons` for custom SVGs:

```ts
customCollectionsDir: './assets/icons'
```

Icons placed in this directory (including subdirectories) become immediately accessible via the `custom:` prefix:

- `./assets/icons/logo.svg` -> `<Icon name="custom:logo" />`
- `./assets/icons/social/github.svg` -> `<Icon name="custom:social/github" />`

## Related

- [Icons overview](./index.md)
- [Usage and Registry](./usage.md)
- [Runtime Loading and SSR](./runtime.md)
