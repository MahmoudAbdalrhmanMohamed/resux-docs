# Security and Caching

Resux has two layers for response behavior: production server defaults and route rules. Use them together with server middleware when you need request-specific logic.

## Production security headers

Production serving enables default hardening headers. They are intended to make generated apps safer by default.

Common defaults include:

- `x-content-type-options`
- `referrer-policy`
- `x-frame-options`
- `cross-origin-opener-policy`
- `permissions-policy`

Disable them only when a host or reverse proxy owns those headers:

```sh
resux start . --no-security-headers
```

## Route rules

Route rules are path-based response rules in `resux.config.ts`.

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

Use route rules for behavior that can be decided from the path. Use server middleware when the decision depends on cookies, auth, headers, or request body data.

## Cache behavior

Resux route payloads and SSR pages usually need fresh data, so they are good candidates for `no-store` behavior. Build-stable runtime and handler assets can use long immutable caching.

The `resux:performance` module can add cache rules for built runtime assets and route payloads:

```ts
export default defineResuxConfig({
  modules: ['resux:performance']
})
```

When adding cache rules manually, avoid caching user-specific HTML or route payload responses unless you control the personalization boundary.

## CORS

Route rules support CORS headers for path groups. Keep CORS narrow:

```ts
export default defineResuxConfig({
  routeRules: {
    '/api/public/**': {
      cors: {
        origin: 'https://example.com',
        methods: ['GET']
      }
    }
  }
})
```

Use server middleware when CORS behavior needs request-specific origin checks.

## Security module

`resux:security` adds default production hardening behavior and can extend route rules with headers or CSP-like policy entries.

```ts
export default defineResuxConfig({
  modules: ['resux:security']
})
```

Use the module for app-wide security defaults. Use route rules for path-specific policy.

## Server middleware for request-specific policy

Server middleware is the right place for policies that depend on request state.

```ts
export default defineServerMiddleware((event) => {
  if (event.path.startsWith('/private')) {
    setHeader(event, 'cache-control', 'no-store')
  }
})
```

Middleware runs before handlers, public files, and page rendering.

## Deployment checks

After building, check:

```sh
resux inspect . --json
curl http://localhost:3000/__resux/health
```

Use inspect output to confirm route rules and diagnostics. Use the health endpoint to confirm the deployed server is responding.

## Related pages

- [Modules and Route Rules](/guide/modules-route-rules)
- [Middleware](/guide/middleware)
- [Deployment](/guide/deployment)
- [Configuration Reference](/reference/configuration)
