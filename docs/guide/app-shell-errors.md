# App Shell, Errors, and Public Files

## `app.vue`

`app.vue` is the optional outer application component. A common shell renders navigation, layout selection, the active page, and global UI.

```vue
<template>
  <div class="app-shell">
    <header>My App</header>
    <ResuxLayout>
      <ResuxPage />
    </ResuxLayout>
  </div>
</template>
```

Resux also checks `app/app.vue` when a root file is absent.

## Layout and page placeholders

- `<ResuxPage />` renders the matched page.
- `<ResuxLayout />` renders the layout selected by page metadata.
- `<slot />` renders page content inside a layout.

Avoid rendering the page twice by placing both `<ResuxPage />` and a layout that already contains the page placeholder incorrectly.

## `error.vue`

`error.vue` can render not-found and server errors. It may read the current error through `useError()`.

```vue
<script setup lang="ts">
const error = useError()

function recover() {
  clearError()
}
</script>

<template>
  <main>
    <h1>{{ error?.statusCode ?? 500 }}</h1>
    <p>{{ error?.message ?? 'Unexpected error' }}</p>
    <button @click="recover">Try again</button>
  </main>
</template>
```

Related APIs:

- `createError(input)` creates a structured error.
- `showError(input)` stores and throws a fatal render error.
- `useError()` returns the current error ref.
- `clearError()` clears it and emits the error-cleared hook.

## Server error responses

Server handlers may return a `Response`, a string, JSON-compatible data, `false`, a redirect result, or an abort result. Unhandled errors produce development diagnostics and a safer production response.

## Public files

Files under `public/` are served from `/`:

```txt
public/favicon.svg  -> /favicon.svg
public/robots.txt   -> /robots.txt
```

The server applies path-boundary checks to prevent traversal.

## Source assets

Resux also serves `/assets/*` from the app's `assets/` directory because compiled imports and configured CSS may resolve there.

For optimized images and video, prefer [Media and Optimization](/guide/media).

## Loading hooks and UI

The core hook system includes:

- `page:loading:start`
- `page:loading:end`
- `page:finish`
- `app:error`
- `app:error:cleared`

Modules or advanced integrations can use these hooks to implement loading indicators and centralized error reporting.
