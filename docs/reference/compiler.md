# Compiler Reference

The compiler turns the Resux SFC subset and file conventions into server modules, browser modules, route records, manifests, diagnostics, and generated types.

## Main entry points

```ts
import {
  buildProject,
  compileVueFile,
  compileVueSource,
  createRouteManifest,
  ResuxCompileError
} from 'resuxjs/compiler'
```

## `buildProject`

```ts
const result = await buildProject(appRoot, outDir, {
  vite: 'build',
  server: 'bundle',
  traceBuild: false
})
```

Build options:

- `vite`: `build` or `dev`
- `server`: `bundle` or `modules`
- `hooks`: custom `ResuxHooks`
- `changedPath`: incremental development hint
- `traceBuild`: detailed diagnostics

The result includes routes, components, layouts, plugins, client enhancements, middleware, server middleware, server handlers, islands, route rules, and optional app/error components.

## Component output

A compiled component records:

- id, name, and file
- server and client source
- template nodes
- handlers
- styles and scope id
- page metadata
- expression transformation diagnostics

## Compile validation

The compiler rejects unsupported or unsafe input, including examples such as:

- missing template blocks,
- unsupported style languages,
- style modules and style `src`,
- unsupported directives,
- invalid conditional/list syntax,
- unsafe browser handler captures,
- and incompatible package usage.

`ResuxCompileError` can include file, line, and column information.

## Discovery

The build includes application conventions, module contributions, auto-import directories, client enhancements, server plugins/utilities, and package diagnostics.

## Generated outputs

Generated output includes server modules, Vite client entries, bundled client assets, manifests, diagnostics JSON, templates, and `.d.ts` files.

## Tooling guidance

Compiler APIs are intended for builders, tests, adapters, and framework tooling. Ordinary applications should use CLI commands rather than calling `buildProject` directly.
