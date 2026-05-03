# Configuration Reference

Create `resux.config.ts` at the app root.

```ts
export default defineResuxConfig({
  app: {
    head: {
      title: 'My App'
    }
  },
  css: ['/styles/global.css'],
  runtimeConfig: {
    public: {
      appOrigin: 'https://example.com'
    }
  },
  modules: ['resux:security', 'resux:performance'],
  routeRules: {
    '/old': { redirect: { to: '/', statusCode: 301 } }
  }
})
```

## `app.head`

Global document head defaults.

```ts
app: {
  head: {
    title: 'Resux App',
    meta: [{ name: 'description', content: 'A resumable app' }],
    link: [{ rel: 'icon', href: '/favicon.svg' }]
  }
}
```

## `css`

Global CSS files to include.

```ts
css: ['/styles/global.css']
```

Modules can add more CSS with `addCss`.

## `runtimeConfig`

```ts
runtimeConfig: {
  secretToken: process.env.SECRET_TOKEN,
  public: {
    appOrigin: process.env.APP_ORIGIN,
    apiBase: '/api'
  }
}
```

Only `public` config is serialized to the browser.

## `modules`

```ts
modules: [
  'resux:security',
  ['resux:performance', { assetMaxAge: 31536000 }],
  ['./modules/example.ts', { enabled: true }]
]
```

## `routeRules`

```ts
routeRules: {
  '/old': { redirect: '/new' },
  '/admin/**': { headers: { 'x-robots-tag': 'noindex' } },
  '/api/**': { cache: false },
  '/assets/**': { cache: { maxAge: 31536000 } },
  '/public-api/**': {
    cors: {
      origin: '*',
      methods: ['GET', 'POST'],
      headers: ['content-type']
    }
  }
}
```

Route rules support redirects, response headers, status codes, cache headers, and CORS headers.

## Public origin keys

For SSR internal API URL resolution, Resux looks for these public runtime config keys:

- `appOrigin`
- `appURL`
- `siteURL`
- `origin`

Example:

```ts
runtimeConfig: {
  public: {
    appOrigin: 'https://my-app.example.com'
  }
}
```
