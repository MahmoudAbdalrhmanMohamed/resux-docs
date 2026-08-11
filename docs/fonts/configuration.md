# Font Configuration

The public font module surface is small enough to document completely.

## Module options

```ts
export interface ResuxFontsModuleOptions {
  google?: ResuxFontFamilyInput[]
  preconnect?: boolean
  strategy?: 'eager' | 'preload' | 'lazy'
  deferUntilPageLoad?: boolean
}
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `google` | `ResuxFontFamilyInput[]` | `[]` | Google font families to include. |
| `preconnect` | `boolean` | `true` | Add preconnect hints when Google families exist. |
| `strategy` | `'eager' | 'preload' | 'lazy'` | `'eager'` | Module default loading strategy. |
| `deferUntilPageLoad` | `boolean` | `false` | Module-level deferred-loading default for families that do not override it. |

## Family options

```ts
export interface ResuxFontFamilyInput {
  name: string
  weights?: Array<number | string>
  display?: 'auto' | 'block' | 'swap' | 'fallback' | 'optional'
  strategy?: 'eager' | 'preload' | 'lazy'
  deferUntilPageLoad?: boolean
}
```

| Property | Default | Behavior |
| --- | --- | --- |
| `name` | required | Family name used to build the Google Fonts URL. Control characters are removed and the value is encoded. |
| `weights` | omitted | Positive font weights from 1–1000, or variable ranges like `'100..900'`. Invalid entries are ignored. |
| `display` | effectively `swap` when not valid/supplied for generated URL grouping | Accepted: auto/block/swap/fallback/optional. |
| `strategy` | inherits module | Per-family loading override. |
| `deferUntilPageLoad` | inherits module | Boolean override for deferred behavior; explicit family `false` can prevent inherited deferral. |

## Weight normalization

Examples:

```ts
{ name: 'Inter', weights: [400, 500, 700] }
{ name: 'Inter', weights: ['100..900'] }
```

The module normalizes, de-duplicates, and sorts accepted weights before producing the URL.

Invalid values such as negative weights, values above 1000, malformed ranges, or reversed ranges are ignored rather than documented as supported.

## Display

```ts
{
  name: 'Inter',
  weights: [400, 700],
  display: 'optional'
}
```

The implementation recognizes:

```ts
'auto' | 'block' | 'swap' | 'fallback' | 'optional'
```

Do not document arbitrary strings as supported `font-display` values.

## Strategy precedence

Per-family configuration takes precedence over module defaults.

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      strategy: 'lazy',
      google: [
        { name: 'Inter', weights: [400, 600], strategy: 'eager' },
        { name: 'Alexandria', weights: [400, 700] }
      ]
    }]
  ]
})
```

Here:

- Inter is eager because its family strategy overrides the module strategy.
- Alexandria inherits lazy.

### Boolean deferral override

```ts
['resuxjs/fonts', {
  deferUntilPageLoad: true,
  google: [
    { name: 'Inter', weights: [400], deferUntilPageLoad: false },
    { name: 'Alexandria', weights: [400] }
  ]
}]
```

Inter stays eager/default-strategy unless otherwise specified; Alexandria inherits deferred loading.

`strategy: 'lazy'` is itself a deferred path. You do not need to also set `deferUntilPageLoad: true` on the same family.

## URL grouping

Families are partitioned into eager/non-deferred and lazy/deferred groups. Each group receives a Google Fonts CSS URL containing that group's normalized family queries.

This means two families with different loading strategies can result in separate Google Fonts stylesheet URLs/head behavior.

## `googleFont()`

```ts
function googleFont(input: ResuxFontFamilyInput): ResuxFontFamilyInput
```

Example:

```ts
import { googleFont } from 'resuxjs/fonts'

export const headingFont = googleFont({
  name: 'Alexandria',
  weights: [500, 600, 700],
  display: 'swap',
  strategy: 'eager'
})
```

## Public runtime metadata

Module setup extends public runtime config with font metadata including:

- `provider: 'google'`
- configured `families`
- `familyConfigs` with each family's resolved strategy and deferred flag
- module-level `strategy`
- module-level `deferUntilPageLoad`

This metadata is public by design. Do not put secrets in font module options.

## Unsupported configuration

The current `ResuxFontFamilyInput` has no first-party fields for:

- local font file paths
- custom provider IDs
- styles/italics list
- subsets
- unicode ranges
- font stretch
- `@font-face` source definitions
- fallback metric generation
- CSS variable generation
- download/caching directories

Use normal CSS/assets or an integration when you need those capabilities.

## Related

- [Fonts overview](./index.md)
- [Performance and CSP](./performance.md)
