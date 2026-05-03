# Modules and Route Rules

Modules extend Resux during build without adding hydration. Route rules customize response behavior by path.

## Built-in modules

Resux includes two built-in module specifiers:

```ts
export default defineResuxConfig({
  modules: [
    'resux:security',
    ['resux:performance', { assetMaxAge: 31536000 }]
  ]
})
```

- `resux:security` adds default production hardening headers and can add custom headers or CSP through route rules.
- `resux:performance` adds immutable cache rules for built runtime and handler assets, plus `no-store` behavior for route payloads.

## Route rules

```ts
export default defineResuxConfig({
  routeRules: {
    '/old': { redirect: { to: '/', statusCode: 301 } },
    '/admin/**': { headers: { 'x-robots-tag': 'noindex' } },
    '/api/**': { cache: false },
    '/assets/**': { cache: { maxAge: 31536000 } }
  }
})
```

## Supported rule fields

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

## Custom module file

```ts
// modules/security.ts
export default defineResuxModule({
  defaults: { header: 'enabled' },
  setup(options, resux) {
    resux.addCss('/module.css')
    resux.addHead({ meta: [{ name: 'module', content: options.header }] })
    resux.addRouteRule('/secure/**', {
      headers: { 'x-module': options.header },
      cache: { maxAge: 60, swr: 30 }
    })
    resux.extendRuntimeConfig({
      public: { securityModule: options.header }
    })
  }
})
```

Use it from config:

```ts
export default defineResuxConfig({
  modules: [
    ['./modules/security.ts', { header: 'enabled' }]
  ]
})
```

## Module context

```ts
type ResuxModuleContext = {
  rootDir: string
  buildDir: string
  options: Record<string, unknown>
  addCss(href: string): void
  addHead(head: Record<string, unknown>): void
  addRouteRule(path: string, rule: Record<string, unknown>): void
  extendRuntimeConfig(config: Record<string, unknown>): void
}
```

## Module forms

Modules can be:

- Built-in `resux:*` specifiers.
- NPM package specifiers.
- Local files.
- Inline functions.
- Objects returned by `defineResuxModule`.

## Best practices

- Keep module output deterministic.
- Use route rules instead of ad-hoc response mutation when possible.
- Put public browser config under `runtimeConfig.public`.
- Prefer `addCss` for global CSS files instead of importing CSS from every page.
