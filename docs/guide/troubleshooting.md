# Troubleshooting

## Failed to parse URL from /api/...

Use `$fetch('/api/...')` or `apiURL('/api/...')` when code can run during SSR.

```ts
await $fetch('/api/test')
await fetch(apiURL('/api/test'))
```

## Skeleton never disappears

Render `error` and guard success UI with `!pending && !error && data`.

```vue
<p v-if="pending">Loading</p>
<p v-if="error">{{ error.message }}</p>
<pre v-if="!pending && !error && data">{{ data }}</pre>
```

## Handler capture compile error

Move non-serializable values out of resumable handlers or put resumable state in `useState`.

```ts
const count = useState('count', () => 0)

function increment() {
  count.value++
}
```

## Dev edits do not appear

Keep the dev server running:

```sh
resux dev .
```

The dev server uses Vite middleware and a dev update channel at:

```txt
/__resux/dev-events
```

If the browser is not connected to that endpoint, reload manually.

## Port already in use

Pass another port:

```sh
resux dev --port 4000
resux preview --host 0.0.0.0 --port 4000
```

## No pages found

Add `.vue` files under `pages/` or `app/pages/`, then inspect:

```sh
resux inspect .
```

## Route rule does not apply

Check the build manifest:

```sh
resux inspect . --json
```

Look for `routeRules` and confirm the path pattern matches the request path.

## Vue-only feature is unsupported

Normal Resux components support a compiler-friendly subset. Move complex Vue runtime behavior into a Vue island.
