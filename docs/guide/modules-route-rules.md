# Modules and Route Rules

Resux modules run during framework preparation/build and extend the application without hydrating it. Route rules customize response behavior by path.

Modules are trusted build-time code. Review a module before installing it because it can read project files, write generated files, register server code, and change Vite or Nitro configuration.

## Register modules

```ts
export default defineResuxConfig({
  modules: [
    'resux:security',
    ['resux:performance', { assetMaxAge: 31536000 }],
    ['resuxjs/i18n', { defaultLocale: 'en' }],
    ['./modules/analytics.ts', { enabled: true }]
  ]
})
```

A module entry can be a built-in alias, npm package, local path, inline module, or `[module, options]` tuple.

## Built-in modules

### `resux:security`

Adds production hardening behavior and can contribute headers or policy through route rules.

### `resux:performance`

Adds cache behavior for build-stable runtime/handler assets and conservative no-store behavior for route payloads.

Other optional features such as i18n, icons, fonts, and UI are available through their package/module entry points.

## Define a module

```ts
// modules/site-tools.ts
export default defineResuxModule({
  meta: {
    name: 'site-tools',
    configKey: 'siteTools'
  },
  defaults: {
    enabled: true,
    header: 'active'
  },
  async setup(options, resux) {
    if (!options.enabled) return

    resux.addCss('/site-tools.css')
    resux.addHead({
      meta: [{ name: 'site-tools', content: options.header }]
    })
    resux.addRouteRule('/internal/**', {
      headers: { 'x-site-tools': options.header },
      cache: false
    })
    resux.extendRuntimeConfig({
      public: {
        siteToolsEnabled: true
      }
    })
  }
})
```

## Complete module context

A module receives `rootDir`, `buildDir`, its resolved `options`, and extension methods.

### Application output

```ts
resux.addCss('/module.css')
resux.addHead({ meta: [{ name: 'module', content: 'enabled' }] })
resux.addRouteRule('/docs/**', { cache: { maxAge: 300 } })
resux.extendRuntimeConfig({ public: { moduleEnabled: true } })
```

### Hooks

```ts
const remove = resux.hook('build:before', async (payload) => {
  // inspect or extend supported build payload
})

// remove() unregisters the hook
```

Hook names and payloads are framework extension contracts; verify them against the installed Resux version before publishing a reusable module.

### Components

```ts
resux.addComponent({
  file: './runtime/ModuleBanner.vue',
  name: 'ModuleBanner',
  global: true,
  mode: 'all',
  lazy: false
})

resux.addComponentsDir({
  path: './runtime/components',
  global: true,
  mode: 'all',
  pathPrefix: false
})
```

Supported mode values are `all`, `server`, and `client`.

### Imports

```ts
resux.addImports({
  from: './runtime/composables',
  name: 'useModuleFeature'
})

resux.addImports([
  { from: './runtime/utils', name: 'formatValue' },
  { from: './runtime/utils', name: 'parseValue', as: 'parseModuleValue' }
])

resux.addImportsDir('./runtime/composables')
```

### Plugins and middleware

```ts
resux.addPlugin({
  src: './runtime/plugin.ts',
  mode: 'all'
})

resux.addRouteMiddleware({
  name: 'module-auth',
  src: './runtime/auth-middleware.ts',
  global: false,
  mode: 'all'
})
```

Client/server mode restrictions should match the APIs used by the file.

### Server extensions

```ts
resux.addServerHandler({
  route: '/api/module/status',
  handler: './runtime/status-handler.ts',
  method: 'GET'
})

resux.addServerPlugin('./runtime/server-plugin.ts')
```

A server handler can also be marked as middleware when the integration requires it.

### Generated templates and types

```ts
resux.addTemplate({
  filename: 'module/runtime-config.mjs',
  getContents: () => 'export default { enabled: true }',
  write: true
})

resux.addTypeTemplate({
  filename: 'types/module.d.ts',
  getContents: () => 'declare const moduleEnabled: boolean',
  write: true
})
```

Keep generated output deterministic so clean builds and CI produce the same files.

### Extend pages, Vite, and Nitro

```ts
resux.extendPages((pages) => {
  // add or adjust supported page records
})

resux.extendViteConfig((vite) => {
  vite.define = {
    ...(vite.define as Record<string, unknown>),
    __MODULE_BUILD__: JSON.stringify(true)
  }
})

resux.extendNitroConfig((nitro) => {
  // provider/server configuration
})

resux.addVitePlugin(myVitePlugin)
resux.addPrerenderRoutes(['/about', '/legal'])
```

Do not place secrets in Vite `define` values or public runtime config because they can be emitted into browser output.

## Route rules

```ts
export default defineResuxConfig({
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
})
```

## Rule fields

```ts
type RouteRule = {
  headers?: Record<string, string>
  redirect?: string | { to: string; statusCode?: number }
  statusCode?: number
  cache?: false | string | { maxAge?: number; swr?: number }
  cors?: boolean | {
    origin?: string
    methods?: string[]
    headers?: string[]
    credentials?: boolean
  }
}
```

### Matching behavior

- exact paths match directly
- a pattern ending in `/**` matches the prefix and descendants
- `*` matches within a path segment
- `**` can span multiple segments
- more specific patterns take priority over broader wildcard patterns

### Cache examples

```ts
routeRules: {
  '/api/**': { cache: false },
  '/feed.xml': { cache: 'public, max-age=300' },
  '/images/**': { cache: { maxAge: 86400, swr: 3600 } }
}
```

`cache: false` becomes `no-store`. Do not use public caching for personalized or authenticated responses.

### Redirect examples

```ts
routeRules: {
  '/temporary': { redirect: '/new-location' },
  '/permanent': {
    redirect: { to: '/new-location', statusCode: 301 }
  }
}
```

A redirect string uses the framework default redirect status. Set the status explicitly when permanence matters.

### CORS examples

```ts
routeRules: {
  '/open/**': { cors: true },
  '/partner/**': {
    cors: {
      origin: 'https://partner.example.com',
      methods: ['GET'],
      headers: ['authorization'],
      credentials: true
    }
  }
}
```

Do not combine `credentials: true` with an unrestricted origin in production.

## Module author checklist

- Keep module setup deterministic and idempotent.
- Use public APIs from `resuxjs/kit` instead of importing private source paths.
- Mark client/server modes accurately.
- Return or register cleanup for long-lived development hooks where supported.
- Keep secrets server-only.
- Avoid duplicate head/CSS entries.
- Validate module options and provide safe defaults.
- Test `resux prepare`, `resux dev`, `resux build`, and the provider output.
- Document generated files and overwrite behavior.
- Publish compatibility ranges and release notes for reusable modules.
