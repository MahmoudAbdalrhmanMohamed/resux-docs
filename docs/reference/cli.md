# CLI Reference

The `resuxjs` package installs these binaries:

- `resuxjs`
- `resux`
- `create-resux`
- `create-resuxjs`

Use `resux` in project scripts and either create binary for scaffolding.

## Command overview

```sh
resux init [project-dir] [options]
resux dev [app-root] [options]
resux prepare [app-root] [options]
resux build [app-root] [options]
resux compile [app-root] [options]
resux preview [app-root] [options]
resux start [app-root] [options]
resux inspect [app-root] [target] [options]
resux check [app-root] [options]
resux deploy [app-root] [options]
resux halal <command> [app-root] [options]
```

When `app-root` is omitted, Resux uses the current directory.

## `init`

Create a new application:

```sh
npx create-resuxjs@latest my-app
npx resuxjs@latest init my-app
```

Common options:

| Option | Purpose |
| --- | --- |
| `--template <name>` | Select `minimal`, `default`, `full`, `i18n`, `pwa`, `media`, `package-compatibility`, or `dashboard` |
| `--features <list>` | Enable comma-separated optional starter features such as `i18n,pwa` |
| `--hreflang` | Enable i18n alternate-language links when creating an i18n starter |
| `--install` / `--no-install` | Enable or skip dependency installation |
| `--package-manager <pm>` / `--pm <pm>` | Select npm, pnpm, yarn, or bun for generated instructions |
| `--force` | Replace an existing target directory after safety checks |
| `-y`, `--yes` | Accept defaults |

`--force` is intentionally blocked for dangerous targets such as the current working directory, its ancestors, the filesystem root, and the user home directory.

## `dev`

Prepare generated files, compile the application, start Vite middleware, serve SSR pages and APIs, and rebuild after source changes.

```sh
resux dev
resux dev . --host 0.0.0.0 --port 4000
resux dev . --open
```

Development uses `.resux/vite-client` and a development event channel at `/__resux/dev-events`.

## `prepare`

Generate framework types and integration directories without starting a server:

```sh
resux prepare
```

This is suitable for post-install hooks, editors, CI preparation, and type checking.

## `build`

Create the lower-level Resux output and production Nitro output:

```sh
resux build
```

Important generated directories:

```txt
.resux/
.resux-nitro/
.nitro/
.output/
```

The production server entry is normally:

```sh
node .output/server/index.mjs
```

## `compile`

Run the lower-level compiler/build pipeline without treating the result as a complete provider deployment:

```sh
resux compile
```

Use `build` for normal applications. `compile` is mainly useful for framework development and advanced integrations.

## `preview`

Serve a built application for local verification:

```sh
resux preview
resux preview . --host 0.0.0.0 --port 4000
```

Preview validates the on-disk Halal report integrity before serving.

## `start`

Start the production Node server:

```sh
resux start
PORT=3000 resux start . --host 0.0.0.0
```

Production startup requires an authenticated Halal report when Halal Core production enforcement is active.

Security headers are enabled by default. Disable them only when a trusted reverse proxy owns the policy:

```sh
resux start . --no-security-headers
```

## `inspect`

Inspect generated routes, packages, bundles, SEO data, server handlers, middleware, route rules, features, and diagnostics:

```sh
resux inspect
resux inspect --json
resux inspect routes
resux inspect packages
resux inspect bundles --json
resux inspect seo --json
```

JSON output is useful for CI artifacts and automated checks.

## `check`

Validate project structure and generated integration files:

```sh
resux check
resux check --json
resux check --fix
```

`--fix` can regenerate supported framework-owned files. Review the resulting diff before committing it.

## `deploy`

Generate or refresh deployment support files:

```sh
resux deploy . --preset node
resux deploy . --preset docker
resux deploy . --preset nitro
resux deploy . --preset docker --force
```

| Preset | Generated result |
| --- | --- |
| `node` | Node deployment instructions and project integration |
| `docker` | Dockerfile, `.dockerignore`, and deployment instructions |
| `nitro` | `nitro.config.ts`, `.resux-nitro/handler.ts`, and deployment instructions |

Deployment guard validation runs before deployment output is accepted.

## Halal Core commands

```sh
resux halal check
resux halal report
resux halal explain
resux halal submit-review
resux halal verify-review
```

- `check` evaluates the project and prints the status.
- `report` generates machine-readable and human-readable reports.
- `explain` explains the detected categories and reasons.
- `submit-review` creates `halal-review-request.json`; it does **not** currently upload or email it automatically.
- `verify-review` verifies a local signed `halal-review-approval.json`.

See [Halal Core](/guide/halal-core) for the status model, report signing, secrets, and review process.

## Shared server and diagnostic options

| Option | Purpose |
| --- | --- |
| `-p`, `--port <port>` | Set the listening port |
| `--host <host>` | Set the listening host |
| `--open` | Open the development URL where supported |
| `--https` | Enable HTTPS where supported by the command |
| `--debug` | Enable additional diagnostic output |
| `--trace-resume` | Trace client resume behavior |
| `--trace-routes` | Trace route matching and navigation |
| `--trace-build` | Trace compiler/build behavior |
| `--json` | Produce machine-readable output for supported commands |
| `--security-headers` | Explicitly enable production security headers |
| `--no-security-headers` | Disable framework security headers |
| `--force` | Overwrite supported generated files |
| `--fix` | Repair supported generated files during checks |
| `-v`, `--version` | Print the installed Resux version |
| `-h`, `--help` | Show command help |

## Recommended project scripts

```json
{
  "scripts": {
    "prepare": "resux prepare",
    "dev": "resux dev",
    "build": "resux build",
    "preview": "resux preview",
    "start": "resux start",
    "inspect": "resux inspect",
    "check": "resux check"
  }
}
```
