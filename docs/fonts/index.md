# Fonts

`resuxjs/fonts` is Resux's built-in **Google Fonts stylesheet loader**. It builds Google Fonts CSS URLs, adds optional preconnect hints, groups families by loading strategy, and exposes resolved non-secret metadata through public runtime config.

::: warning Current scope
The current first-party module supports **Google Fonts only**. It does not download/self-host font files, scan local fonts, generate `@font-face`, calculate fallback metrics, provide multiple font providers, or cache provider assets locally. Those are capabilities of other font systems—not current `resuxjs/fonts` behavior.
:::

## Enable the module

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/fonts', {
      google: [
        {
          name: 'Inter',
          weights: ['100..900'],
          display: 'swap'
        }
      ]
    }]
  ]
})
```

Then use the family through normal CSS:

```css
:root {
  font-family: 'Inter', system-ui, sans-serif;
}
```

Resux does not scan CSS to discover families. The family must be configured in the module.

## Loading strategies

The module supports:

| Strategy | Result |
| --- | --- |
| `eager` | Adds the Google Fonts stylesheet immediately. Default. |
| `preload` | Adds `rel="preload" as="style"` **and** the normal stylesheet. |
| `lazy` | Adds a stylesheet preload and an inline script that attaches the stylesheet after `window.load` (or immediately if already loaded). |

See [Configuration](./configuration.md) for precedence and exact options, and [Performance and CSP](./performance.md) before choosing deferred loading.

## Preconnect

When Google families exist, `preconnect` defaults to true and adds:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

Disable it when your application already manages those hints.

## Type-safe family helper

```ts
import { googleFont } from 'resuxjs/fonts'

const inter = googleFont({
  name: 'Inter',
  weights: ['100..900'],
  display: 'swap',
  strategy: 'preload'
})
```

`googleFont()` is an identity helper: it returns the family object you pass. Its value is TypeScript guidance/reuse, not hidden runtime processing.

## SSR / build / client boundary

The module participates in Resux setup and adds head entries:

- eager/preload stylesheet links are discoverable in server-generated head output;
- preconnect links are server-added when enabled;
- lazy/deferred loading adds an inline browser script, so that strategy depends on client JavaScript and must be compatible with your Content Security Policy;
- public runtime metadata describes configured family names and resolved strategies, but font CSS itself comes from Google Fonts.

## Privacy and reliability

Because the current module references Google-hosted CSS/fonts, browsers make requests to Google domains. If your requirements demand self-hosting, offline operation, stricter privacy, or no third-party font network dependency, do not claim that the Resux fonts module solves those requirements today. Self-host fonts using normal application CSS/assets or another integration.

## Related

- [Configuration](./configuration.md)
- [Performance and CSP](./performance.md)
- [CSS and Tailwind](/guide/css-tailwind)
- [Security and Caching](/guide/security-caching)
