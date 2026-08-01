# Security and Caching

Resux provides secure defaults and extension points, but application authorization, validation, dependency review, and infrastructure security remain the developer's responsibility.

## Production headers

The production Node server enables hardening headers including examples such as:

- `x-content-type-options`
- `referrer-policy`
- `x-frame-options`
- `cross-origin-opener-policy`
- restrictive `permissions-policy`

Disable them only when a trusted host or reverse proxy owns the complete policy:

```sh
resux start --no-security-headers
```

## Route rules

```ts
routeRules: {
  '/account/**': {
    cache: false,
    headers: { 'x-robots-tag': 'noindex' }
  },
  '/public-api/**': {
    cors: {
      origin: 'https://example.com',
      methods: ['GET'],
      headers: ['content-type']
    }
  },
  '/__resux/assets/**': {
    cache: { maxAge: 31536000 }
  }
}
```

`cache: false` produces `no-store`. String values are passed as cache-control. Object values support `maxAge` and `swr`.

## Default cache model

- route payloads and dynamic SSR data should not be cached accidentally,
- build-stable runtime/handler assets may use immutable caching,
- transformed media can use long-lived or configured persistent caching,
- user-specific APIs should normally use `no-store` unless carefully varied.

## Runtime config

Only `runtimeConfig.public` reaches the browser. Private keys belong in server-only config and files.

Deep config merging blocks prototype-pollution keys.

## Public files and traversal

Public, asset, generated media, and framework asset handlers resolve paths against explicit roots and reject paths outside those roots.

## Remote media

The media pipeline accepts HTTP(S) sources. Treat remote-source support as a network boundary:

- restrict sources at your application or proxy layer,
- avoid exposing unrestricted private-network fetching,
- limit payload sizes and timeouts at infrastructure level,
- and monitor transformation CPU usage.

## HTML and user content

Do not treat `v-html` as an authorization or sanitization system. Sanitize user-controlled HTML with a dedicated, well-maintained policy appropriate to your application.

## Halal Core

Halal Core scans policy categories and protects production reports with authenticated integrity when a signing secret is configured. It is an additional policy layer, not a replacement for application security review.

## Dependencies

Use package diagnostics and ordinary supply-chain tools:

```sh
resux inspect packages --json
npm audit
npm outdated
```

Pin and review sensitive server dependencies, and configure package modes so server-only code cannot leak into browser bundles.
