# Compiler API (`resuxjs/compiler`)

The compiler entry point turns Resux's supported SFC/file conventions into server modules, browser handler modules, route/manifests, generated types/templates, package diagnostics, and deployment-ready build output.

::: warning Node/build-time API
`resuxjs/compiler` imports Node filesystem/path/module APIs, TypeScript, Vite, and Vue compiler packages. It is build/tooling code, not a browser runtime entry point.
:::

## Main exports

```ts
import {
  buildProject,
  compileVueFile,
  compileVueSource,
  createRouteManifest,
  ResuxCompileError
} from 'resuxjs/compiler'
```

Public types include the compile/build/result records documented below.

## `ResuxCompileError`

```ts
interface CompileErrorLocation {
  file: string
  line: number
  column: number
}

class ResuxCompileError extends Error {
  readonly location?: CompileErrorLocation

  constructor(message: string, location?: CompileErrorLocation)
}
```

When a location exists, the constructor formats the error message with `(file:line:column)` and also preserves the structured `location` field.

## `compileVueFile()`

```ts
function compileVueFile(
  file: string,
  options: {
    id: string
    name?: string
  }
): Promise<CompiledComponent>
```

Reads the file as UTF-8 and delegates to `compileVueSource()`. If `name` is omitted, the compiler derives a PascalCase name from the `.vue` filename.

```ts
const component = await compileVueFile(
  '/app/components/Counter.vue',
  { id: 'counter' }
)
```

## `compileVueSource()`

```ts
function compileVueSource(
  source: string,
  options: {
    file: string
    id: string
    name: string
  }
): CompiledComponent
```

Compiles an in-memory SFC source string.

Current verified high-level flow:

1. parse the SFC;
2. require a `<template>` block;
3. analyze `<script setup>` bindings/handlers/page metadata;
4. compile supported template directives/expressions;
5. compile plain-CSS `<style>` blocks and scoped style IDs;
6. validate resumable browser-handler captures;
7. generate separate server and client module sources;
8. return template/handler/style/expression metadata.

### Style limits

Resumable component style blocks currently reject:

- non-CSS `lang` values;
- `<style module>`;
- `<style src>`.

Scoped CSS is supported and contributes a generated scope attribute ID.

## `CompiledComponent`

```ts
interface CompiledComponent {
  id: string
  name: string
  file: string
  serverSource: string
  clientSource: string
  template: TemplateNode[]
  handlers: string[]
  styles: ComponentStyle[]
  styleScopeId?: string
  meta?: PageMeta
  expressions?: Array<{
    id: string
    original: string
    transformed: string
    locals: string[]
  }>
}
```

`handlers` is de-duplicated from the compiled template event list.

## `createRouteManifest()`

```ts
function createRouteManifest(
  root: string,
  files: string[],
  idByFile?: Map<string, string>,
  compiledByFile?: Map<string, CompiledComponent>
): RouteManifestRecord[]
```

The function converts `pages/` or `app/pages/` Vue files into sorted route records.

Verified conventions include:

- trailing `index.vue` collapses to its directory route;
- `[id].vue` becomes `:id`;
- `[...slug].vue` becomes `:slug*`;
- route param names are recorded in `params`;
- supplied component IDs and compiled page metadata are attached when provided;
- records are sorted by route specificity/score and path.

```ts
interface RouteManifestRecord {
  id: string
  path: string
  file: string
  params: string[]
  componentId: string
  meta?: PageMeta
}
```

## `buildProject()`

```ts
function buildProject(
  appRoot: string,
  outDir?: string,
  options?: BuildOptions
): Promise<BuildResult>
```

Default `outDir` is `<appRoot>/.resux`.

### Build options

```ts
interface BuildOptions {
  vite?: 'build' | 'dev'
  server?: 'bundle' | 'modules'
  hooks?: ResuxHooks
  changedPath?: string
  traceBuild?: boolean
}
```

| Option | Default/behavior |
| --- | --- |
| `vite` | `'build'`; `'dev'` selects dev-oriented output behavior. |
| `server` | `'bundle'`, except dev mode defaults to `'modules'`. |
| `hooks` | If omitted, a fresh core hook registry is created for the build. |
| `changedPath` | Enables the compiler's incremental-development path only when `vite === 'dev'` and the string is non-empty. |
| `traceBuild` | Detailed build tracing when true. |

A normal non-incremental build cleans generated output before writing new artifacts.

### `BuildResult`

```ts
interface BuildResult {
  appRoot: string
  outDir: string
  routes: RouteManifestRecord[]
  components: CompiledComponent[]
  layouts: CompiledComponent[]
  plugins: CompiledPlugin[]
  clientEnhancements: ClientEnhancementManifestEntry[]
  middleware: CompiledMiddleware[]
  serverMiddleware: CompiledServerMiddleware[]
  serverHandlers: ServerHandlerRecord[]
  vueIslands: VueIslandRecord[]
  routeRules: Record<string, RouteRuleConfig>
  app?: CompiledComponent
  error?: CompiledComponent
}
```

## Other public build records

### `CompiledPlugin`

```ts
interface CompiledPlugin {
  id: string
  file: string
  mode: 'all' | 'server' | 'client'
  serverSource: string
  clientSource: string
}
```

### `ClientEnhancementManifestEntry`

```ts
interface ClientEnhancementManifestEntry {
  name: string
  id: string
  file: string
  src: string
}
```

### `CompiledMiddleware`

```ts
interface CompiledMiddleware {
  id: string
  name: string
  file: string
  mode: 'all' | 'server' | 'client'
  global: boolean
  serverSource: string
  clientSource: string
}
```

### `CompiledServerMiddleware`

```ts
interface CompiledServerMiddleware {
  id: string
  file: string
  source: string
}
```

### `ServerHandlerRecord`

```ts
interface ServerHandlerRecord {
  id: string
  path: string
  file: string
  params: string[]
  source: string
}
```

### `VueIslandRecord`

```ts
interface VueIslandRecord {
  name: string
  file: string
}
```

### `RouteRuleConfig`

```ts
interface RouteRuleConfig {
  headers?: Record<string, string>
  redirect?: string | { to: string; statusCode?: number }
  statusCode?: number
  cache?: false | string | { maxAge?: number; swr?: number }
  cors?: boolean | {
    origin?: string
    methods?: string[]
    headers?: string[]
    credentials?: boolean
  }
}
```

## Compiler/runtime boundary

The compiler is where Resux decides what can remain server/resumable versus what must be emitted as browser/client code. Unsupported captures/directives/package usages are compile-time concerns because silently falling back to broad hydration would violate Resux's runtime model.

Use application-facing guides for authored SFC behavior:

- [Template Syntax](/guide/template-syntax)
- [Resumability and Handlers](/guide/resumability-handlers)
- [Package Integration](/guide/package-integration)
- [Vue Islands](/guide/vue-islands)

## Related

- [Core API](./core.md)
- [Resux Kit](./kit.md)
- [File Conventions](./file-conventions.md)
- [Dev Server and Build Output](/guide/dev-build-output)
