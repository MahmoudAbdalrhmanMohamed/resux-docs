# Dev Server and Build Output

Resux uses the same source conventions in development and production, but the output directories and serving model differ by command.

## Development

`resux dev .` starts the app in development mode.

```sh
resux dev .
resux dev . --port 4000
```

In dev mode, Resux:

- Discovers app files and creates the manifest.
- Emits generated client modules under `.resux/vite-client`.
- Serves the resume runtime and handler modules through Vite middleware.
- Rebuilds when source files change.
- Uses a dev update channel at `/__resux/dev-events`.
- Reloads the browser after a successful rebuild.

Dev reloads do not add Vue hydration. They only make the development loop faster.

## Build

`resux build .` creates production output.

```sh
resux build .
```

It writes:

```txt
.resux/     lower-level Resux server/client build output
.output/    Nitro production server output
```

`.resux/` contains Resux internals such as compiled modules, manifests, runtime assets, and handler chunks. `.output/` is the production server output used by the generated start command.

## Compile only

`resux compile .` builds the lower-level Resux output without producing the full production server.

```sh
resux compile .
```

Use this when you need to inspect compiler output or debug generated manifests.

## Preview and start

Preview serves a built app locally:

```sh
resux preview .
```

Production start uses the generated Nitro server:

```sh
node .output/server/index.mjs
```

Generated apps usually expose this as:

```json
{
  "scripts": {
    "preview": "resux preview .",
    "start": "node .output/server/index.mjs"
  }
}
```

## Inspect

`resux inspect` prints discovered routes and build diagnostics.

```sh
resux inspect .
resux inspect . --json
```

Use inspect output to confirm:

- Pages and route params.
- Components and layouts.
- Middleware and plugins.
- Server handlers.
- Route rules.
- Feature flags and diagnostics.

## Deployment file generation

`resux deploy` writes deployment support files without changing application source code.

```sh
resux deploy . --preset node
resux deploy . --preset docker
resux deploy . --preset nitro
```

Use `--force` when you intentionally want to refresh existing deployment files.

## Health check

Dev and production servers expose:

```txt
/__resux/health
```

Use it for uptime checks, container health checks, and deployment smoke tests.

## Git hygiene

Do not edit generated output by hand. Change source files and rebuild.

Common generated directories:

```txt
.resux/
.output/
.resux-nitro/
docs/.vitepress/.temp
docs/.vitepress/dist
```

Commit deployment helper files only when they are intended source files for the app or docs site.

## Related pages

- [CLI Reference](/reference/cli)
- [Compiler Internals](/reference/compiler)
- [Deployment](/guide/deployment)
- [Troubleshooting](/guide/troubleshooting)
