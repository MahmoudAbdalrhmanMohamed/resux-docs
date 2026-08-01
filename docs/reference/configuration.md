# Configuration Reference

Create `resux.config.ts` in the application root:

```ts
export default defineResuxConfig({
  app: {
    head: {
      title: 'My Resux App',
      meta: [
        { name: 'description', content: 'A resumable application' }
      ],
      link: [
        { rel: 'icon', href: '/favicon.svg' }
      ],
      htmlAttrs: { lang: 'en' },
      bodyAttrs: { class: 'app-body' }
    }
  },
  css: ['/assets/css/main.css'],
  runtimeConfig: {
    databaseURL: process.env.DATABASE_URL,
    public: {
      appOrigin: 'https://example.com',
      apiBase: '/api'
    }
  },
  modules: ['resux:security'],
  routeRules: {
    '/old': { redirect: { to: '/', statusCode: 301 } }
  },
  deploy: {
    target: 'auto'
  }
})
```

The configuration object is intentionally extensible because modules can introduce their own top-level keys.

## Core build fields

| Field | Purpose |
| --- | --- |
| `builder` | Select or identify the client/build pipeline for advanced integrations |
| `serverBuilder` | Select or identify the server build pipeline |
| `buildDir` | Change the default generated Resux build directory |
| `compatibilityDate` | Pin provider/runtime compatibility behavior where supported |
| `deploy` | Configure deployment target and Nitro preset |

Most applications should keep the default builders and build directory.

## `app.head`

Global document defaults:

```ts
app: {
  head: {
    title: 'Resux App',
    meta: [
      { name: 'description', content: 'A resumable app' },
      { property: 'og:type', content: 'website' }
    ],
    link: [
      { rel: 'canonical', href: 'https://example.com' }
    ],
    script: [],
    style: [],
    noscript: [],
    htmlAttrs: { lang: 'en', dir: 'ltr' },
    bodyAttrs: { class: 'site' }
  }
}
```

Head entries from the app, modules, layouts, and pages are composed. Attribute objects are merged, while list fields such as `meta`, `link`, `script`, `style`, and `noscript` are accumulated.

Use `useHead()` and `useSeoMeta()` for request/page-specific values.

## `css`

Register global CSS files:

```ts
css: [
  '/assets/css/reset.css',
  '/assets/css/main.css'
]
```

Modules can add CSS with `addCss()`. Third-party package CSS can also be declared under `packages.css`.

## `runtimeConfig`

```ts
runtimeConfig: {
  secretToken: process.env.SECRET_TOKEN,
  databaseURL: process.env.DATABASE_URL,
  public: {
    appOrigin: process.env.APP_ORIGIN,
    apiBase: '/api'
  }
}
```

Rules:

- Only `runtimeConfig.public` is serialized to the browser.
- Private values are server-only and must not be read from client handlers.
- Values sent to the browser must be JSON-serializable.
- Runtime config merging blocks prototype-pollution keys such as `__proto__`, `prototype`, and `constructor`.

For SSR internal URL resolution, Resux recognizes public origin keys including:

- `appOrigin`
- `appURL`
- `siteURL`
- `origin`

## `modules`

```ts
modules: [
  'resux:security',
  ['resux:performance', { assetMaxAge: 31536000 }],
  ['resuxjs/i18n', { defaultLocale: 'en' }],
  ['./modules/example.ts', { enabled: true }]
]
```

A module entry can be:

- a built-in alias
- a package name
- a local module path
- a tuple of module and options

Read [Modules and Route Rules](/guide/modules-route-rules) for all module-context methods.

## `routeRules`

```ts
routeRules: {
  '/old': {
    redirect: { to: '/new', statusCode: 301 }
  },
  '/admin/**': {
    headers: { 'x-robots-tag': 'noindex' },
    cache: false
  },
  '/assets/**': {
    cache: { maxAge: 31536000, swr: 86400 }
  },
  '/public-api/**': {
    cors: {
      origin: 'https://app.example.com',
      methods: ['GET', 'POST'],
      headers: ['content-type', 'authorization'],
      credentials: true
    }
  }
}
```

Supported rule behavior includes:

- response headers
- redirect string or `{ to, statusCode }`
- response status code
- `cache: false`, raw cache-control string, or `{ maxAge, swr }`
- CORS boolean or detailed configuration

Exact paths win over broader wildcard patterns. `/**` matches a path prefix and descendants.

## `deploy`

```ts
export default defineResuxConfig({
  deploy: {
    target: 'auto',
    nitroPreset: 'node-server'
  }
})
```

Supported Resux target names:

```ts
'auto' | 'node' | 'vercel' | 'netlify' | 'cloudflare' | 'static'
```

When `target` is `auto`, Resux can infer deployment behavior from explicit environment variables, provider variables, files such as `vercel.json` or `netlify.toml`, and package scripts. Pin the target when deterministic CI output is more important than automatic detection.

See [Deployment](/guide/deployment).

## `packages`

```ts
packages: {
  lazy: true,
  clientOnly: ['chart.js'],
  serverOnly: ['pg'],
  mode: {
    swiper: 'progressive'
  },
  external: ['pg'],
  noExternal: ['some-esm-package'],
  transpile: ['legacy-package'],
  optimizeDeps: ['dayjs'],
  css: {
    swiper: ['swiper/css']
  },
  aliases: {
    '@shared': './lib/shared.ts'
  },
  guards: true,
  diagnostics: true
}
```

Read [Third-party Package Integration](/guide/package-integration) before marking packages client-only or server-only.

## Images

```ts
image: {
  provider: 'resux',
  quality: 82,
  format: 'webp',
  cache: '7d',
  densities: [1, 2],
  providers: {
    cdn: {
      baseURL: 'https://cdn.example.com',
      modifiers: {
        quality: 80
      }
    }
  }
}
```

Use `useResuxImage()` or built-in media components to consume the settings. See [Media and Optimization](/guide/media).

## Videos

`video` is available for framework and module video configuration. Runtime video transformation supports MP4/WebM and requires `ffmpeg` when a transform is requested. Keep provider-specific settings documented with the module or application integration that consumes them.

## i18n

```ts
i18n: {
  defaultLocale: 'en',
  fallbackLocale: 'en',
  strategy: 'prefix_except_default',
  locales: [
    { code: 'en', name: 'English', dir: 'ltr' },
    { code: 'ar', name: 'العربية', dir: 'rtl' }
  ],
  messages: {
    en: () => import('./locales/en.json'),
    ar: () => import('./locales/ar.json')
  },
  seo: {
    hreflang: true
  }
}
```

Enable the corresponding module and read [i18n & Localization](/guide/i18n).

## A production-oriented example

```ts
export default defineResuxConfig({
  app: {
    head: {
      title: 'Store',
      meta: [{ name: 'description', content: 'Resumable storefront' }]
    }
  },
  runtimeConfig: {
    paymentSecret: process.env.PAYMENT_SECRET,
    public: {
      appOrigin: process.env.APP_ORIGIN,
      apiBase: '/api'
    }
  },
  modules: [
    'resux:security',
    ['resux:performance', { assetMaxAge: 31536000 }],
    ['resuxjs/icons', { lazy: true }],
    ['resuxjs/fonts', { strategy: 'preload' }]
  ],
  routeRules: {
    '/api/**': { cache: false },
    '/__resux/**': { headers: { 'x-content-type-options': 'nosniff' } }
  },
  packages: {
    clientOnly: ['chart.js'],
    diagnostics: true
  },
  deploy: {
    target: 'auto'
  }
})
```

## Configuration safety

- Never put secrets under `runtimeConfig.public`.
- Do not use user-controlled object keys to construct config fragments.
- Keep server-only packages out of client handlers.
- Review module code because modules execute during build.
- Prefer exact route rules for sensitive endpoints.
- Validate the final result with `resux inspect --json` and `resux check`.
