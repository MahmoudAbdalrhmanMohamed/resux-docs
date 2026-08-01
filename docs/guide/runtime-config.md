# Runtime Config

Runtime config separates server-only values from browser-visible public values.

## Configuration

```ts
export default defineResuxConfig({
  runtimeConfig: {
    databaseURL: process.env.DATABASE_URL,
    signingKey: process.env.SIGNING_KEY,
    public: {
      appOrigin: process.env.APP_ORIGIN,
      apiBase: '/api',
      environment: process.env.NODE_ENV ?? 'development'
    }
  }
})
```

## Read config

```ts
const config = useRuntimeConfig()
config.public.apiBase
```

Server handlers and server-mode plugins can read private values. Only `public` is serialized to the browser payload.

## Internal API origin

SSR URL resolution checks public keys such as:

- `appOrigin`
- `appURL`
- `siteURL`
- `origin`

Set an accurate production origin when internal native `fetch` calls depend on it.

## Module extension

```ts
resux.extendRuntimeConfig({
  public: {
    featureEnabled: true
  }
})
```

Nested config is merged. Resux blocks dangerous prototype keys such as `__proto__`, `prototype`, and `constructor` during deep merging.

## Environment strategy

Use environment variables for deployment-specific secrets and values. Keep a non-secret `.env.example` with names only.

```txt
DATABASE_URL=
SIGNING_KEY=
APP_ORIGIN=
RESUX_HALAL_REPORT_SIGNING_SECRET=
```

`SIGNING_KEY` populates the application-specific `runtimeConfig.signingKey` shown above. `RESUX_HALAL_REPORT_SIGNING_SECRET` is a separate framework build/runtime secret used to authenticate the Halal report; do not reuse one secret for both purposes.

Never commit actual keys.

## Serialization limits

Public config must be JSON-compatible. Functions, classes, symbols, open connections, and server clients cannot be serialized safely.
