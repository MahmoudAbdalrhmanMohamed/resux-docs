# Compiler Internals

Resux compiles `.vue` files into server modules, client handler modules, and build manifests.

## Build pipeline

`buildProject(appRoot, outDir, options)` does the following:

1. Cleans generated output.
2. Reads runtime config and creates route rules.
3. Discovers components, pages, layouts, app shell, error page, plugins, middleware, server middleware, server handlers, and Vue islands.
4. Compiles each `.vue` file.
5. Writes server component modules.
6. Writes client handler modules.
7. Builds client assets with Vite for production or writes Vite dev entries.
8. Writes `manifest.mjs` and `manifest.json`.
9. Optionally builds a server bundle.

## Build options

```ts
type BuildOptions = {
  vite?: 'build' | 'dev'
  server?: 'bundle' | 'modules'
}
```

Default server mode is `modules` during dev and `bundle` during production builds.

## Compile errors

Resux throws compile errors for unsupported or unsafe patterns. Examples:

- Missing `<template>` block.
- Dynamic binding without argument or expression.
- Event without argument or expression.
- `v-if`, `v-for`, `v-show`, `v-text`, `v-html`, or `v-model` without expression.
- `v-model` expression that cannot be assigned to.
- Unsupported directives.
- Unsupported event modifiers.
- Handler captures that are not resumability-safe.

## Template compilation

The compiler maps supported template syntax into a small template tree:

- Text nodes.
- Interpolation nodes.
- Element nodes.
- Static and dynamic attributes.
- Event records.
- `v-if` blocks.
- `v-for` blocks.
- `v-html` bindings.

## Auto-unwrapping refs

Template expressions are analyzed so known ref bindings can be auto-unwrapped. This allows:

```vue
<template>{{ count }}</template>
```

while keeping script mutation explicit:

```ts
count.value++
```

## Route manifest

Route files are converted into route records with path, params, file, component id, and static page meta.

```txt
pages/index.vue -> /
pages/post/[id].vue -> /post/:id
pages/docs/[...slug].vue -> /docs/:slug*
```

## Vite integration

Resux uses Vite for:

- Dev middleware.
- Production client bundling.
- Handler chunks.
- Vue island bundling.
- Server bundling in production mode.

The dev server writes generated client modules into `.resux/vite-client` and serves them through Vite middleware.
