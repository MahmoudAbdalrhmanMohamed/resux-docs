# Deployment

Resux supports Node, Docker, and Nitro deployment flows.

## Production build

```sh
npm run build
```

A full production build creates:

```txt
.resux/     lower-level Resux server/client build output
.output/    Nitro production server output
```

Run it:

```sh
node .output/server/index.mjs
```

The generated starter maps this to:

```sh
npm run start
```

## Node server

```sh
npm install
npm run build
PORT=3000 npm run start
```

## Docker files

Generate Docker deployment files:

```sh
resux deploy . --preset docker
```

Overwrite existing files:

```sh
resux deploy . --preset docker --force
```

Build and run:

```sh
docker build -t resux-app .
docker run --rm -p 3000:3000 resux-app
```

## Nitro preset

Generate Nitro helper files:

```sh
resux deploy . --preset nitro
```

The Nitro preset writes:

```txt
nitro.config.ts
.resux-nitro/handler.ts
```

The generated handler wraps `createResuxNodeHandler()` from `resuxjs/node`.

## Security headers

Production serving enables default hardening headers, including examples such as:

- `x-content-type-options`
- `referrer-policy`
- `x-frame-options`
- `cross-origin-opener-policy`
- restrictive `permissions-policy`

Disable them only when your host or reverse proxy owns those headers:

```sh
resux start . --no-security-headers
```

## Health checks

Use:

```txt
/__resux/health
```

## Inspect in CI

```sh
resux inspect . --json > resux-manifest-summary.json
```

The inspect output helps capture routes, server handlers, route rules, features, and diagnostics during deployment.
