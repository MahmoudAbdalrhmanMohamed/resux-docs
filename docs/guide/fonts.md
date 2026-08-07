# Fonts (`resuxjs/fonts`)

The fonts module builds Google Fonts stylesheet URLs, adds optional preconnect hints, and lets you control loading globally or per font family.

The current default strategy is `eager`. Use `preload` only for fonts that are important to the first render, and use `lazy` for families that can wait until after the page finishes loading.

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
          weights: ['100..900'],
          display: 'swap',
          strategy: 'preload'
        },
        {
          name: 'Alexandria',
          weights: [300, 400, 500, 600, 700],
          display: 'swap',
          strategy: 'lazy'
        }
      ]
    }]
  ]
})
```

In this example:

- `Inter` is preloaded and also added as a normal stylesheet, so it can be used immediately.
- `Alexandria` is preloaded as a stylesheet resource, but the actual stylesheet is attached after `window.load`.
- `strategy: 'lazy'` already enables page-load deferral. You do not need to also set `deferUntilPageLoad: true` for the same family.

## Module options

| Option | Type | Default |
| --- | --- | --- |
| `google` | `ResuxFontFamilyInput[]` | `[]` |
| `preconnect` | `boolean` | `true` |
| `strategy` | `'eager' \| 'preload' \| 'lazy'` | `'eager'` |
| `deferUntilPageLoad` | `boolean` | `false` |

Module-level `strategy` and `deferUntilPageLoad` act as defaults for families that do not define their own loading behavior.

## Family options

| Property | Type | Behavior |
| --- | --- | --- |
| `name` | `string` | Required family name. Control characters are removed and URL encoding is applied. |
| `weights` | `(number \| string)[]` | Values from 1–1000 or ranges such as `'100..900'`. Invalid entries are ignored. |
| `display` | `'auto' \| 'block' \| 'swap' \| 'fallback' \| 'optional'` | Google `font-display` value. Invalid values fall back to `swap`. |
| `strategy` | `'eager' \| 'preload' \| 'lazy'` | Overrides the module strategy for this family. |
| `deferUntilPageLoad` | `boolean` | `true` forces deferred loading. `false` prevents inherited module-level deferral unless this family explicitly uses `strategy: 'lazy'`. |

## Loading strategies

### `eager`

Adds the Google Fonts stylesheet immediately:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/...">
```

This is the default strategy.

### `preload`

Adds both a stylesheet preload and the normal stylesheet link:

```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/...">
<link rel="stylesheet" href="https://fonts.googleapis.com/...">
```

Use this for genuinely critical fonts. Preloading does not replace the stylesheet link.

### `lazy`

Adds a stylesheet preload, then injects the real stylesheet after `window.load`. If the document is already fully loaded, the stylesheet is attached immediately.

This is the same deferred path used when `deferUntilPageLoad: true` applies to a family.

## Strategy precedence

Per-family settings take precedence over module defaults.

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      strategy: 'lazy',
      google: [
        {
          name: 'Inter',
          weights: [400, 500, 600, 700],
          strategy: 'eager'
        },
        {
          name: 'Alexandria',
          weights: [300, 400, 500, 600, 700]
        }
      ]
    }]
  ]
})
```

Here `Inter` loads eagerly because its family strategy overrides the module default, while `Alexandria` inherits `lazy`.

You can also use `deferUntilPageLoad` when you specifically want a boolean override:

```ts
['resuxjs/fonts', {
  deferUntilPageLoad: true,
  google: [
    { name: 'Inter', weights: [400, 700], deferUntilPageLoad: false },
    { name: 'Alexandria', weights: [400, 700] }
  ]
}]
```

`Inter` stays eager while `Alexandria` inherits page-load deferral.

## Grouping

Families are partitioned into eager and lazy groups. Each group receives one Google Fonts CSS URL containing its normalized families.

Weights are normalized, de-duplicated, and sorted before Resux builds the Google Fonts URL. Variable ranges such as `'100..900'` are supported.

## Preconnect

Preconnect is enabled by default when Google fonts are configured:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

Disable it when you manage these hints yourself:

```ts
['resuxjs/fonts', {
  preconnect: false,
  google: [
    { name: 'Inter', weights: [400, 700] }
  ]
}]
```

## Public runtime metadata

The module exposes non-secret configuration under `runtimeConfig.public.fonts`, including:

- provider (`google`)
- configured family names
- each family's resolved strategy
- whether each family is deferred
- the module-level strategy and defer setting

## Helper

Use `googleFont()` when you want a typed reusable family definition:

```ts
import { googleFont } from 'resuxjs/fonts'

const inter = googleFont({
  name: 'Inter',
  weights: ['100..900'],
  display: 'swap',
  strategy: 'preload'
})
```

## CSP

Google-hosted fonts usually require policy entries similar to:

```txt
style-src https://fonts.googleapis.com
font-src https://fonts.gstatic.com
```

The lazy/deferred mode uses an inline script to attach the stylesheet after page load. A strict CSP may therefore require a nonce/hash or a different loading strategy. Do not weaken CSP globally just to support the font loader.

## Performance guidance

- Keep the module default as `eager` unless most of your typography is non-critical.
- Use `preload` only for families needed during the first render.
- Use `lazy` for secondary or route-specific typography.
- Avoid downloading weights you do not use.
- Prefer `swap` or `optional` based on your typography requirements.
- Consider self-hosting when privacy, CSP, reliability, or regional performance requires it.
