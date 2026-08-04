# Getting Started

This guide creates a Resux app, explains the generated project, and prepares it for development and production.

## Requirements

- Node.js `>=20.19.0`
- npm, pnpm, yarn, or Bun
- a modern browser for the resumable client runtime

```sh
node --version
```

## Create an application

Use either the full CLI or the create wrapper:

```sh
npx resuxjs@latest init my-app
# or
npx create-resuxjs@latest my-app
```

Then:

```sh
cd my-app
npm install
npm run dev
```

## Starter templates

```sh
npx create-resuxjs@latest my-app --template default
```

Available templates:

| Template | Intended use |
| --- | --- |
| `minimal` | Smallest app shell and page |
| `default` | General starter with common conventions |
| `full` | Broad feature demonstration |
| `i18n` | Localized routes and messages |
| `pwa` | Progressive web app starter files |
| `media` | Images, pictures, and video examples |
| `package-compatibility` | Third-party package modes and diagnostics |
| `dashboard` | Dashboard-oriented structure and UI |

## Optional features

Features can be selected independently or combined:

```sh
npx create-resuxjs@latest my-app \
  --features seo,i18n,media,tailwind,server-api,tests
```

Supported feature names:

- `seo`
- `i18n`
- `media`
- `pwa`
- `tailwind`
- `package-compatibility`
- `server-api`
- `tests`

For i18n starters:

```sh
npx create-resuxjs@latest my-app --features i18n --hreflang
```

## Other create options

```sh
npx create-resuxjs@latest my-app --no-install
npx create-resuxjs@latest my-app --package-manager pnpm
npx create-resuxjs@latest my-app --yes
```

`--force` empties a non-empty target, but Resux refuses to apply it to protected locations such as the filesystem root, home directory, current working directory, or an ancestor of the working directory.

## Generated scripts

A generated app contains scripts similar to:

```json
{
  "scripts": {
    "prepare": "resux prepare",
    "dev": "resux dev",
    "build": "resux build",
    "preview": "resux preview",
    "start": "resux start",
    "inspect": "resux inspect",
    "typecheck": "vue-tsc --noEmit"
  }
}
```

Run preparation and validation after changing framework versions or generated conventions:

```sh
npm run prepare
npx resux check
npx resux check --fix
```

## Your first page

Create `pages/index.vue`:

```vue
<script setup lang="ts">
useSeoMeta({
  title: 'Home',
  description: 'My first Resux application'
})

const count = ref(0)

function increment() {
  count.value++
}
</script>

<template>
  <main>
    <h1>Hello Resux</h1>
    <button @click="increment">Clicked {{ count }} times</button>
  </main>
</template>
```

Templates auto-unwrap Resux refs. Script code uses `.value`.

`ref` is the right default here because the counter belongs only to this page component. Use `reactive` for grouped local fields. Use `useState` only when a named value must be serialized into the component scope payload and restored exactly during browser resume.

## Add an API route

Create `server/api/status.ts`:

```ts
export default defineEventHandler(() => ({
  ok: true,
  framework: 'resux'
}))
```

Request it from a page:

```ts
const status = await useFetch<{ ok: boolean }>('/api/status')
```

`useFetch` returns an async-data resource with `data`, `value`, `pending`, and `error` refs.

## Inspect the project

```sh
npx resux inspect
npx resux inspect routes
npx resux inspect packages --json
npx resux inspect seo --json
```

Inspect targets include routes, plugins, enhancements, middleware, imports, components, build, images, server, packages, templates, bundles, and SEO.

## Production build

For production report authentication, configure a secret of at least 32 characters:

```sh
export RESUX_HALAL_REPORT_SIGNING_SECRET='replace-with-a-private-random-secret'
```

Then:

```sh
npm run build
npm run start
```

Build output normally includes:

```txt
.resux/   Resux compiler/runtime output
.output/  Nitro production output
```

## Recommended reading

- [Framework Tour](/guide/framework-tour)
- [Project Structure](/guide/project-structure)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [Template Syntax](/guide/template-syntax)
- [Deployment](/guide/deployment)
