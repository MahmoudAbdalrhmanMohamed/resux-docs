# Head and SEO

Resux can render head tags from global config, page meta, and runtime composables.

## App head in config

```ts
export default defineResuxConfig({
  app: {
    head: {
      title: 'My App',
      meta: [
        { name: 'description', content: 'A Resux app' }
      ],
      link: [
        { rel: 'icon', href: '/favicon.svg' }
      ]
    }
  }
})
```

## Page meta

```vue
<script setup lang="ts">
definePageMeta({
  title: 'Docs',
  meta: [
    { name: 'robots', content: 'index,follow' }
  ]
})
</script>
```

## useHead

```ts
useHead({
  title: 'Profile',
  meta: [
    { name: 'description', content: 'User profile' }
  ],
  link: [
    { rel: 'canonical', href: 'https://example.com/profile' }
  ]
})
```

## useSeoMeta

`useSeoMeta` maps common SEO keys to meta tags.

```ts
useSeoMeta({
  title: 'Resux Blog',
  description: 'Articles about resumability',
  ogTitle: 'Resux Blog',
  ogDescription: 'Articles about resumability',
  ogImage: '/og.png',
  twitterCard: 'summary_large_image'
})
```

Common fields include:

- `title`
- `description`
- `keywords`
- `robots`
- `author`
- `themeColor`
- `colorScheme`
- `applicationName`
- `referrer`
- `generator`
- `ogTitle`, `ogDescription`, `ogImage`, `ogUrl`, `ogType`, `ogSiteName`, `ogLocale`
- `twitterCard`, `twitterTitle`, `twitterDescription`, `twitterImage`, `twitterSite`, `twitterCreator`

## Merge order

Think of head entries as layers:

1. App default head from config.
2. Page meta from `definePageMeta`.
3. Runtime entries from `useHead` and `useSeoMeta`.
4. Document defaults such as charset and viewport.

Use page-level APIs for route-specific metadata and config for site-wide defaults.
