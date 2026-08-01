# Head and SEO

Resux composes global configuration, module contributions, page metadata, component head calls, and i18n alternate links into the rendered document head.

## Global head

```ts
export default defineResuxConfig({
  app: {
    head: {
      title: 'My App',
      meta: [
        { name: 'description', content: 'A Resux application' },
        { name: 'theme-color', content: '#111827' }
      ],
      link: [{ rel: 'icon', href: '/favicon.svg' }],
      htmlAttrs: { lang: 'en' },
      bodyAttrs: { class: 'app-body' }
    }
  }
})
```

Global/module head composition supports arrays such as `meta`, `link`, `script`, `style`, and `noscript`, plus merged HTML/body attributes.

## `useHead`

```ts
useHead({
  title: 'Pricing',
  meta: [{ name: 'description', content: 'Pricing options' }],
  link: [{ rel: 'canonical', href: 'https://example.com/pricing' }],
  htmlAttrs: { lang: 'en' }
})
```

Use structured entries rather than interpolating untrusted HTML into head fields.

## `useSeoMeta`

```ts
useSeoMeta({
  title: 'Product',
  description: 'Product details',
  robots: 'index,follow',
  ogTitle: 'Product',
  ogDescription: 'Product details',
  ogImage: 'https://example.com/og.png',
  twitterCard: 'summary_large_image',
  twitterImage: 'https://example.com/og.png'
})
```

The helper maps common keys to name/property meta entries.

## Page metadata

```ts
definePageMeta({
  title: 'Dashboard',
  meta: [{ name: 'robots', content: 'noindex' }]
})
```

For dynamic SEO, use `useHead` or `useSeoMeta` in setup.

## Image preload priority

The renderer can prioritize relevant head image preloads so critical images are discovered early. Use responsive media attributes and avoid preloading every image.

## i18n SEO

When enabled, i18n can add canonical and alternate `hreflang` links. Configure:

```ts
i18n: {
  seo: { hreflang: true }
}
```

## Inspect SEO

```sh
resux inspect seo
resux inspect seo --json
```

The SEO target checks route metadata and reports diagnostics such as missing canonical information in applicable test routes.

## Safety notes

- Escape or validate user-derived titles and URLs.
- Do not inject arbitrary scripts from user input.
- Keep canonical and Open Graph URLs absolute in production.
- Keep private runtime config out of head output.
