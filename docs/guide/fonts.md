# Fonts (`resuxjs/fonts`)

The fonts module generates Google Fonts links, optional preconnects, and eager, preload, or page-load-deferred stylesheet behavior.

## Configuration

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      preconnect: true,
      strategy: 'eager',
      google: [
        {
          name: 'Inter',
          weights: [400, 500, 600, 700],
          display: 'swap',
          strategy: 'preload'
        },
        {
          name: 'Alexandria',
          weights: [300, 400, 500, 600, 700],
          display: 'swap',
          strategy: 'lazy',
          deferUntilPageLoad: true
        }
      ]
    }]
  ]
})
```

## Module options

| Option | Type | Default |
| --- | --- | --- |
| `google` | `ResuxFontFamilyInput[]` | `[]` |
| `preconnect` | `boolean` | `true` |
| `strategy` | `'eager' \| 'preload' \| 'lazy'` | `'eager'` |
| `deferUntilPageLoad` | `boolean` | `false` |

## Family options

| Property | Type | Behavior |
| --- | --- | --- |
| `name` | `string` | Required family name. Control characters are removed and URL encoding is applied. |
| `weights` | `(number \| string)[]` | Values from 1–1000 or ranges such as `'100..900'`. Invalid entries are ignored. |
| `display` | Google font-display value | Invalid values fall back to `swap`. |
| `strategy` | eager/preload/lazy | Overrides the module default for the family. |
| `deferUntilPageLoad` | `boolean` | Explicitly controls deferred loading. |

## Strategies

### Eager

Adds a stylesheet link immediately.

### Preload

Adds a stylesheet preload and the stylesheet link. Preload does not replace the stylesheet.

### Lazy/page-load deferred

Adds a style preload and a small inline script that appends the stylesheet after `window.load`, or immediately if the document is already complete.

## Grouping

Families are partitioned into eager and lazy groups. Each group receives one Google Fonts CSS URL containing its normalized families.

## Public runtime metadata

The module exposes non-secret family configuration under `runtimeConfig.public.fonts`, including provider, names, strategy, and whether each family is deferred.

## Helper

```ts
import { googleFont } from 'resuxjs/fonts'

const inter = googleFont({
  name: 'Inter',
  weights: ['100..900'],
  display: 'swap'
})
```

## CSP

Google-hosted fonts usually require policy entries similar to:

```txt
style-src https://fonts.googleapis.com
font-src https://fonts.gstatic.com
```

The deferred mode uses an inline script, so a strict CSP may require a nonce/hash or a different loading strategy. Do not weaken CSP globally just to support one font loader.

## Performance guidance

- Use eager/preload only for genuinely critical families.
- Avoid downloading weights that are not used.
- Prefer `swap` or `optional` based on your typography requirements.
- Consider self-hosting when privacy, CSP, reliability, or regional performance requires it.
