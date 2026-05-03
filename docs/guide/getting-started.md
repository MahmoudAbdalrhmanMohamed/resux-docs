# Getting Started

This page takes you from zero to a running Resux app.

## Requirements

Resux requires Node `>=20.19.0` for the framework package. The docs site itself only needs Node 18+, but generated Resux apps should use the framework requirement.

Check your version:

```sh
node --version
```

## Create a new app

```sh
npx resuxjs@latest init my-app
cd my-app
npm install
npm run dev
```

Open the local URL printed by the command.

## Create options

Create in a named directory:

```sh
npx resuxjs@latest init my-app
```

Skip install:

```sh
npx resuxjs@latest init my-app --no-install
```

Choose a package manager for the generated next steps:

```sh
npx resuxjs@latest init my-app --package-manager pnpm
npx resuxjs@latest init my-app --pm bun
```

Overwrite a non-empty target directory:

```sh
npx resuxjs@latest init my-app --force
```

Accept defaults without prompts:

```sh
npx resuxjs@latest init my-app --yes
```

## Generated package scripts

A generated app uses a single dependency on `resuxjs` and scripts like these:

```json
{
  "scripts": {
    "dev": "resux dev .",
    "build": "resux build .",
    "preview": "resux preview .",
    "start": "node .output/server/index.mjs",
    "inspect": "resux inspect ."
  }
}
```

## Your first page

Create `pages/index.vue`:

```vue
<script setup lang="ts">
useSeoMeta({
  title: 'Home',
  description: 'My first Resux app'
})

const count = useState('count', () => 0)

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

The template can read `count` directly because templates auto-unwrap Resux refs. In script, mutate refs through `.value`.

## Build for production

```sh
npm run build
npm run start
```

`resux build` writes lower-level Resux output to `.resux` and a Nitro production server to `.output`.

## Inspect a build

```sh
npm run inspect
npm run inspect -- --json
```

Use inspect output to debug discovered routes, components, layouts, plugins, middleware, server handlers, route rules, features, and diagnostics.
