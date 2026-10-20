# Font Configuration

Resux provides a unified, strongly-typed font configuration interface supporting automated fontless scanning, Fontaine zero-CLS fallback metrics, local self-hosted files, and multi-provider options.

## Module options (`ResuxFontsModuleOptions`)

```ts
export interface ResuxFontsModuleOptions {
  /** Enable automatic CSS and template font scanning with fontless. Defaults to true. */
  autoScan?: boolean

  /** Global font defaults across all resolved families */
  defaults?: {
    preload?: boolean
    subsets?: string[]
    weights?: ResuxFontWeight[]
    styles?: Array<'normal' | 'italic' | 'oblique'>
    fallbacks?: string[]
  }

  /** Provider configurations (google, bunny, fontshare, fontsource, local) */
  providers?: {
    google?: boolean | Record<string, unknown>
    bunny?: boolean | Record<string, unknown>
    fontshare?: boolean | Record<string, unknown>
    fontsource?: boolean | Record<string, unknown>
    local?: boolean | Record<string, unknown>
  }

  /** Devtools panel toggle during development (defaults to true) */
  devtools?: boolean

  /** Provider-aware font families list */
  families?: ResuxFontFamilyInput[]

  /** Backward-compatible Google font families list */
  google?: ResuxFontFamilyInput[]

  /** Add preconnect hints when Google families exist. Defaults to true. */
  preconnect?: boolean

  /** Default loading strategy across families ('eager' | 'preload' | 'lazy') */
  strategy?: 'eager' | 'preload' | 'lazy'

  /** Default deferral until window.load */
  deferUntilPageLoad?: boolean
}
```

## Family options (`ResuxFontFamilyInput`)

```ts
export interface ResuxFontFamilyInput {
  name: string
  provider?: 'google' | 'local' | 'remote'
  weights?: ResuxFontWeight[]
  weight?: ResuxFontWeight
  style?: 'normal' | 'italic' | 'oblique'
  display?: 'auto' | 'block' | 'swap' | 'fallback' | 'optional'
  strategy?: 'eager' | 'preload' | 'lazy'
  deferUntilPageLoad?: boolean
  src?: string | ResuxFontSourceInput | Array<string | ResuxFontSourceInput>
  faces?: ResuxFontFaceInput[]
  unicodeRange?: string
  preload?: boolean
  variable?: string
  axes?: Record<string, number | [number, number]>
  fallbacks?: string[]
}
```

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `string` | *(required)* | Name of the font family. |
| `provider` | `'google' \| 'local' \| 'remote'` | `'google'` | Provider determining font resolution. |
| `weights` | `Array<number \| string \| ResuxFontWeightName>` | `[]` | List of weights to include. Accepts numeric values (`400`), ranges (`'100..900'`), or semantic names (`'bold'`). |
| `display` | `ResuxFontDisplay` | `'swap'` | CSS `font-display` value. |
| `fallbacks` | `string[]` | `[]` | List of fallback fonts. Resux invokes `fontaine` to calculate and emit zero-CLS fallback metrics (`size-adjust`, `ascent-override`, `descent-override`). |
| `variable` | `string` | `undefined` | CSS custom property to define (e.g. `'--font-inter'`). |
| `axes` | `Record<string, number \| [number, number]>` | `undefined` | Variable font axes settings (e.g. `{ wght: 700, wdth: 100 }`). |
| `src` | `string \| ResuxFontSourceInput \| ...` | `undefined` | File path or URL for local or remote font files. |
| `faces` | `ResuxFontFaceInput[]` | `undefined` | Specific `@font-face` definitions for multi-weight/style local fonts. |
| `strategy` | `'eager' \| 'preload' \| 'lazy'` | inherits module | Loading strategy override for this family. |

## Semantic Named Weights

Resux accepts standard CSS numeric weights or any of the following semantic aliases:

- `100`: `'thin'`, `'hairline'`
- `200`: `'extralight'`, `'extra-light'`, `'ultralight'`
- `300`: `'light'`
- `400`: `'normal'`, `'regular'`
- `500`: `'medium'`
- `600`: `'semibold'`, `'semi-bold'`, `'demibold'`
- `700`: `'bold'`
- `800`: `'extrabold'`, `'extra-bold'`, `'ultrabold'`
- `900`: `'black'`, `'heavy'`

## Example Configurations

### 1. Modern Google Font with Fontaine Zero-CLS

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      families: [
        {
          name: 'Inter',
          weights: ['regular', 'bold'],
          display: 'swap',
          fallbacks: ['Arial'],
          variable: '--font-inter',
        }
      ]
    }]
  ]
})
```

### 2. Local Self-Hosted Font

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      families: [
        {
          name: 'CalSans',
          provider: 'local',
          src: '/fonts/CalSans-SemiBold.woff2',
          weight: 'semibold',
          style: 'normal',
          variable: '--font-cal-sans',
        }
      ]
    }]
  ]
})
```

### 3. Variable Font with Axes

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      families: [
        {
          name: 'Roboto Flex',
          weights: ['100..900'],
          axes: {
            wdth: 100,
            opsz: 14
          }
        }
      ]
    }]
  ]
})
```

## Related

- [Fonts overview](./index.md)
- [Performance and Zero-CLS](./performance.md)
