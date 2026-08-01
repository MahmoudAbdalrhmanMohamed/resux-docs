# Deployment

Resux builds a server-rendered application with a resumable client runtime. A normal production build creates both framework-level output and a Nitro-compatible production server.

## Build output

```sh
npm run build
```

Important directories:

```txt
.resux/          compiler output, manifests, client assets, server bundle, reports
.resux-nitro/    generated Resux-to-Nitro adapter files
.nitro/          Nitro intermediate files
.output/         production server/public output
```

Do not edit generated directories manually.

## Run the production server

```sh
node .output/server/index.mjs
```

Generated applications normally provide:

```sh
npm run start
```

The health endpoint is:

```txt
/__resux/health
```

Use it for container, load balancer, and uptime probes.

## Deployment targets

Resux deployment target names are:

```ts
'auto' | 'node' | 'vercel' | 'netlify' | 'cloudflare' | 'static'
```

Configure them in `resux.config.ts`:

```ts
export default defineResuxConfig({
  deploy: {
    target: 'vercel',
    nitroPreset: 'vercel'
  }
})
```

`target: 'auto'` resolves the deployment from the strongest available signal, including:

1. explicit `deploy.target` and `deploy.nitroPreset`
2. `NITRO_PRESET` or `RESUX_NITRO_PRESET`
3. provider environment variables
4. project files such as `vercel.json`, `netlify.toml`, or `wrangler.*`
5. package-script heuristics

Pin the target in CI when the same repository is built for multiple providers.

Cloudflare worker presets are opt-in because Node-oriented adapters are not automatically valid inside a Worker runtime.

## Generate deployment files

```sh
resux deploy . --preset node
resux deploy . --preset docker
resux deploy . --preset nitro
```

Overwrite framework-owned deployment files:

```sh
resux deploy . --preset docker --force
```

Review the resulting diff before committing.

## Node deployment

```sh
npm ci
npm run build
HOST=0.0.0.0 PORT=3000 npm run start
```

Recommended runtime requirements:

- use the Node version required by the installed `resuxjs` package
- deploy `.output` and any runtime files referenced by the server
- provide private runtime environment variables at the host
- keep writable cache directories available when runtime-generated media caching is enabled
- terminate TLS at a trusted proxy or configure the server appropriately

## Docker deployment

Generate Docker files:

```sh
resux deploy . --preset docker
```

Build and run:

```sh
docker build -t resux-app .
docker run --rm -p 3000:3000 --env-file .env.production resux-app
```

Do not copy development `.env` files or source-control credentials into the image. Use BuildKit/runtime secrets where appropriate.

## Nitro integration

```sh
resux deploy . --preset nitro
```

This writes integration files such as:

```txt
nitro.config.ts
.resux-nitro/handler.ts
```

The adapter wraps the Resux Node handler and maps production output into Nitro conventions. Route pages, API endpoints, and route payloads should remain uncached unless the application explicitly proves they are build-stable. Resux runtime and handler assets can use immutable caching because their names are build-specific.

Nitro prerender crawling is conservative by default to protect routes that depend on request state or resumable payload generation.

## Security headers

The production server enables default hardening headers, including policies such as:

- `x-content-type-options`
- `referrer-policy`
- `x-frame-options`
- `cross-origin-opener-policy`
- restrictive `permissions-policy`

Disable framework headers only when the hosting platform or reverse proxy owns the complete policy:

```sh
resux start . --no-security-headers
```

When disabling them, verify the final public response headers—not only the application configuration.

## Halal report requirement

Production server startup and deployment verification require an authenticated Halal report. Build with a private signing secret of at least 32 characters:

```sh
export RESUX_HALAL_REPORT_SIGNING_SECRET="a-long-private-random-secret"
npm run build
```

A plain `sha256:` checksum is sufficient for local integrity checks but is not accepted as production authentication.

When a signed human approval is needed, also provide a separate review secret:

```sh
export RESUX_HALAL_REVIEW_SIGNING_SECRET="a-different-long-private-secret"
```

Never expose either secret to client runtime config or commit it to the repository. Read [Halal Core](/guide/halal-core).

## CI example

```yaml
name: Build Resux application

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: .nvmrc
          cache: npm
      - run: npm ci
      - run: npm run check
      - run: npm run build
        env:
          RESUX_HALAL_REPORT_SIGNING_SECRET: ${{ secrets.RESUX_HALAL_REPORT_SIGNING_SECRET }}
          RESUX_HALAL_REVIEW_SIGNING_SECRET: ${{ secrets.RESUX_HALAL_REVIEW_SIGNING_SECRET }}
      - run: npm run inspect -- --json > resux-inspect.json
```

Do not provide production secrets to untrusted fork pull requests.

## Inspect deployment output

```sh
resux inspect --json
resux inspect routes --json
resux inspect packages --json
resux inspect bundles --json
resux inspect seo --json
```

Capture inspect output as a CI artifact when you need to audit routes, server handlers, route rules, packages, feature flags, diagnostics, or SEO output.

## Caching guidance

- SSR pages, route payloads, authenticated responses, and APIs should default to `no-store` unless designed otherwise.
- Fingerprinted Resux runtime and handler assets can use long immutable caching.
- Route rules can configure cache-control for known-safe paths.
- Generated image transformations may use persistent or immutable caching.
- Never cache private responses at a shared CDN without a correct cache key and authorization design.

## Media dependencies

Image transformation uses `sharp`. Video transformation uses `ffmpeg` when requested.

```sh
export RESUX_FFMPEG_PATH=/usr/bin/ffmpeg
```

Confirm native dependencies exist in the final runtime image, not only in the build stage. See [Media and Optimization](/guide/media).

## Pre-deployment checklist

- `npm ci` succeeds from the committed lockfile.
- `resux check` passes.
- `resux build` succeeds with production secrets.
- The correct deploy target/preset is selected.
- `node .output/server/index.mjs` starts successfully.
- `/__resux/health` responds successfully.
- SSR pages, APIs, route payloads, runtime assets, and media routes have the expected cache headers.
- Security headers are present at the public edge.
- Server-only runtime config is not present in browser payloads.
- Halal report verification succeeds.
- Native media dependencies are installed when used.
