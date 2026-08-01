# Dev Server, Diagnostics, and Build Output

## Development

```sh
resux dev
resux dev --host 0.0.0.0 --port 4000 --open
```

Development uses Vite middleware for generated client modules and an internal event stream for rebuild/reload notifications.

Useful diagnostics:

```sh
resux dev --debug
resux dev --trace-build
resux dev --trace-routes
resux dev --trace-resume
```

`--https` currently changes the emitted/opened URL but local transport remains HTTP; it is not a local TLS server switch.

## Preparation and checks

```sh
resux prepare
resux check
resux check --json
resux check --fix
```

Checks validate required files, generated directories, scripts, TypeScript setup, Nitro bridge files, and general build readiness.

## Compile and build

```sh
resux compile
resux build
```

- `compile` creates lower-level `.resux` output.
- `build` creates `.resux` output and deployable Nitro output.

## Preview and start

```sh
resux preview
resux start --host 0.0.0.0 --port 3000
```

Preview rebuilds when required assets are missing or stale. `start` is the production-oriented alias in the current CLI.

## Inspect targets

```sh
resux inspect routes
resux inspect plugins
resux inspect enhancements
resux inspect middleware
resux inspect imports
resux inspect components
resux inspect build
resux inspect images
resux inspect server
resux inspect packages
resux inspect templates
resux inspect bundles
resux inspect seo
```

Add `--json` for CI-friendly output.

## `.resux` map

```txt
.resux/
  client/
    runtime-client.mjs
    plugins/
    middleware/
    handlers/
    chunks/
    assets/
  server/
    manifest.mjs
    handlers/
    resux-plugins/
    resux-middleware/
    request-middleware/
  server-bundle/
  vite-client/
  templates/
  types/
  dev/
```

Exact files vary by enabled features.

## Internal endpoints

Examples include:

```txt
/__resux/health
/__resux/route
/__resux/runtime-client.mjs
/__resux/plugins/*
/__resux/middleware/*
/__resux/handlers/*
/__resux/vue-islands/*
/_resux/generated/images/*
/_resux/generated/videos/*
```

Treat internal URL shapes as framework implementation details unless documented for a specific integration.

## Tailwind automation

When `assets/css/tailwind.css` exists and a compatible Tailwind CLI is installed, development can start a Tailwind watcher and production builds generate minified CSS before bundling.

See [CSS and Tailwind](/guide/css-tailwind).
