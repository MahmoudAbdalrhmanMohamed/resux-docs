# CLI Reference

Resux installs CLI binaries named `resuxjs`, `resux`, and `create-resux`.

## Commands

```sh
resux init [project-dir] [options]
resux dev [app-root] [options]
resux build [app-root] [options]
resux compile [app-root] [options]
resux preview [app-root] [options]
resux start [app-root] [options]
resux inspect [app-root] [options]
resux deploy [app-root] [options]
```

If `app-root` is omitted, Resux uses the current directory.

## `resux init`

Scaffold a new app.

```sh
npx resuxjs@latest init my-app
```

Options:

| Option | Description |
| --- | --- |
| `--install` | Install dependencies after scaffolding. |
| `--no-install` | Skip dependency installation. |
| `--package-manager <pm>` | Use `npm`, `pnpm`, `yarn`, or `bun` for next steps. |
| `--pm <pm>` | Alias for `--package-manager`. |
| `--force` | Empty the target directory before scaffolding. |
| `-y`, `--yes` | Use default answers. |
| `-h`, `--help` | Show init help. |

## `resux dev`

Start the dev server with Vite middleware and live rebuild reloads.

```sh
resux dev .
resux dev --port 4000
resux dev --host 0.0.0.0 --port 4000
```

## `resux build`

Build server/client output into `.resux`, then build Nitro `.output`.

```sh
resux build .
```

## `resux compile`

Build only the lower-level `.resux` output.

```sh
resux compile .
```

## `resux preview`

Serve the built app, rebuilding when needed.

```sh
resux preview .
```

## `resux start`

Alias for preview intended for production Node servers.

```sh
resux start . --host 0.0.0.0 --port 3000
```

## `resux inspect`

Print a build manifest summary.

```sh
resux inspect .
resux inspect . --json
```

Inspect includes counts and details for routes, components, layouts, plugins, middleware, server middleware, server handlers, route rules, features, and diagnostics.

## `resux deploy`

Generate deployment files.

```sh
resux deploy . --preset node
resux deploy . --preset docker
resux deploy . --preset nitro
resux deploy . --preset docker --force
```

Options:

| Option | Description |
| --- | --- |
| `--preset node` | Generate Node deployment guide. |
| `--preset docker` | Generate Dockerfile, `.dockerignore`, deployment guide. |
| `--preset nitro` | Generate Nitro config, adapter, deployment guide. |
| `--force` | Overwrite existing deployment files. |

## Shared options

| Option | Description |
| --- | --- |
| `--security-headers` | Enable default production security headers. |
| `--no-security-headers` | Disable default production security headers. |
| `--json` | Print JSON output for inspect. |
| `-p`, `--port <port>` | Set server port. Default is `3000` or `PORT`. |
| `--host <host>` | Set server host. |
| `-v`, `--version` | Print Resux version. |
| `-h`, `--help` | Show help. |
