# Troubleshooting

## Run the standard diagnostic sequence

```sh
node --version
npm install
resux prepare
resux check --json
resux inspect build --json
resux build --debug --trace-build
```

Node must satisfy the framework engine requirement.

## Unsupported template or SFC syntax

Symptoms:

- `ResuxCompileError`
- unknown directive errors
- unsupported style language/module/src errors
- unsafe handler capture errors

Actions:

1. Compare the component with [Template Syntax](/guide/template-syntax).
2. Move browser-library behavior into a client enhancement or Vue island.
3. Keep normal component styles as plain CSS.
4. Reduce handler captures to serializable or browser-safe values.

## A handler works on SSR but not after clicking

Run:

```sh
resux dev --trace-resume
resux inspect bundles --json
```

Check that the handler is discoverable, its imports are browser-compatible, and the state it uses was serialized.

## A package appears in the wrong bundle

```sh
resux inspect packages --json
```

Configure `packages.mode`, `clientOnly`, `serverOnly`, `external`, `noExternal`, aliases, or a progressive adapter.

## Internal API fetch fails during SSR

Set a public app origin or use `$fetch`:

```ts
runtimeConfig: {
  public: { appOrigin: 'https://example.com' }
}
```

## `useFetch` access is incorrect

`useFetch` returns an async-data resource:

```ts
const result = await useFetch('/api/status')
console.log(result.data.value)
console.log(result.pending.value)
console.log(result.error.value)
```

## Image transforms return 501

Verify that `sharp` is installed and loadable in the server runtime. Check the requested format and source response.

## Video transforms return 501

Install `ffmpeg` or set:

```sh
export RESUX_FFMPEG_PATH=/absolute/path/to/ffmpeg
```

## Production start or deploy rejects the Halal report

Set `RESUX_HALAL_REPORT_SIGNING_SECRET` before the production build and use the same secret during production verification. Rebuild after changing the key.

## Review-required project cannot build

Generate the request:

```sh
resux halal submit-review
```

The current framework does not send it automatically. Obtain a valid signed approval file, place it at the project root, then run:

```sh
resux halal verify-review
```

## Generated files are missing

```sh
resux check --fix
resux prepare
```

Do not hand-edit `.resux` output.

## Dev changes are not visible

Check terminal build errors, then use `--trace-build`. Restart only after resolving syntax or watcher exclusions. Generated and dependency directories are intentionally ignored by the source watcher.

## Route does not match

```sh
resux inspect routes
resux dev --trace-routes
```

Verify file naming, dynamic segment placement, middleware result, localized route strategy, and route-rule redirects.
