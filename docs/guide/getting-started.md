# Getting Started

This guide gets a Resux app running, shows you the important generated files, and walks through the basic development workflow.

## Requirements

You need:

- Node.js `>=20.19.0`
- npm, pnpm, yarn, or Bun
- a modern browser

Check your Node.js version:

```sh
node --version
```

Resux currently has two npm channels:

- `latest` → stable 0.3.x releases
- `next` → public-beta 0.4.x prereleases

The current public beta is **0.4.0-beta.2**.

## Create an application

For the stable channel:

```sh
npx create-resuxjs@latest my-app
```

For the public beta:

```sh
npx create-resuxjs@next my-app
```

If you want a repeatable beta setup, pin the exact release:

```sh
npx create-resuxjs@0.4.0-beta.2 my-app
```

Then start the project:

```sh
cd my-app
npm install
npm run dev
```

You can also create a project through the main package CLI:

```sh
npx resuxjs@next init my-app
```

Before using the beta for an important workload, read [Project Status](/reference/status) and [Current Limits](/reference/limits).

## Choose a starter template

The default template is a good place to begin:

```sh
npx create-resuxjs@next my-app --template default
```

Available templates:

| Template | Good for |
| --- | --- |
| `minimal` | The smallest Resux application |
| `default` | General application development |
| `full` | Exploring a broader set of framework features |
| `i18n` | Localized routes and messages |
| `pwa` | Progressive web app setup |
| `media` | Image, picture, and video examples |
| `package-compatibility` | Testing third-party packages |
| `dashboard` | Dashboard-style applications |

## Add optional features

You can generate several optional features together:

```sh
npx create-resuxjs@next my-app \
  --features seo,i18n,media,tailwind,server-api,tests
```

Supported feature names include:

- `seo`
- `i18n`
- `media`
- `pwa`
- `tailwind`
- `package-compatibility`
- `server-api`
- `tests`

For an i18n starter with hreflang output:

```sh
npx create-resuxjs@next my-app --features i18n --hreflang
```

Other useful create options:

```sh
npx create-resuxjs@next my-app --no-install
npx create-resuxjs@next my-app --package-manager pnpm
npx create-resuxjs@next my-app --yes
```

`--force` can clear a non-empty target directory, but Resux blocks dangerous locations such as the filesystem root, your home directory, the current working directory, and ancestors of the current working directory.

## Generated scripts

A generated app includes scripts similar to:

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

After upgrading Resux or changing generated conventions, it is useful to run:

```sh
npm run prepare
npx resux check
```

Use `npx resux check --fix` when you want Resux to apply supported automatic fixes.

## Create your first page

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

Templates automatically unwrap Resux refs, while script code uses `.value`.

For local component state, `ref` is usually the simplest choice. Use `reactive` for grouped fields, `useState` for named JSON-compatible state that belongs to a component scope, and `useGlobalState` when separate components intentionally share request-isolated application state.

`@click` is the shorter form of `rx-on:click`. Likewise, `:disabled` maps to `rx-bind:disabled`. See [How Resux Uses Vue](/guide/how-resux-uses-vue) for the syntax and runtime model.

## Add an API route

Create `server/api/status.ts`:

```ts
export default defineEventHandler(() => ({
  ok: true,
  framework: 'resux'
}))
```

Then request it from a page:

```ts
const status = await useFetch<{ ok: boolean }>('/api/status')
```

`useFetch` returns an async-data resource with `data`, `value`, `pending`, and `error` refs.

## Inspect the project

The inspect command is useful when you want to see what Resux discovered or generated:

```sh
npx resux inspect
npx resux inspect routes
npx resux inspect packages --json
npx resux inspect seo --json
```

Inspect targets include routes, plugins, enhancements, middleware, imports, components, build, images, server, packages, templates, bundles, and SEO.

## Build for production

If you use production report authentication, configure a private signing secret of at least 32 characters:

```sh
export RESUX_HALAL_REPORT_SIGNING_SECRET='replace-with-a-private-random-secret'
```

Then build and start the app:

```sh
npm run build
npm run start
```

Typical build output includes:

```txt
.resux/   Resux compiler/runtime output
.output/  Nitro production output
```

## Where to go next

- [Framework Tour](/guide/framework-tour)
- [Project Structure](/guide/project-structure)
- [Template Syntax](/guide/template-syntax)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [Resumability Deep Dive](/guide/resumability-deep-dive)
- [Deployment](/guide/deployment)
