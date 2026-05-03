# Runtime Config

Runtime config stores values that should be available to the server runtime and optionally exposed to the browser.

## Define config

```ts
export default defineResuxConfig({
  runtimeConfig: {
    apiSecret: process.env.API_SECRET,
    public: {
      appOrigin: process.env.APP_ORIGIN,
      apiBase: '/api'
    }
  }
})
```

## Read config

```vue
<script setup lang="ts">
const config = useRuntimeConfig()
</script>

<template>
  <p>API base: {{ config.public.apiBase }}</p>
</template>
```

## Public config

Only `runtimeConfig.public` is serialized to the browser payload. Keep secrets outside `public`.

```ts
// Safe in browser
config.public.appOrigin

// Server-only by convention
config.apiSecret
```

## API URL resolution

For internal `/api/...` URLs during SSR, `$fetch` and `apiURL` use this origin priority:

1. Current request origin.
2. Public runtime origins such as `appOrigin`, `appURL`, `siteURL`, or `origin`.
3. Fallback `http://localhost:3000`.

Set `runtimeConfig.public.appOrigin` for predictable production SSR fetches behind proxies.
