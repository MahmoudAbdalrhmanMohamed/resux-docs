# TypeScript and Generated Types

Generated applications use TypeScript declarations so Resux globals and discovered project features are available without manual imports.

## Application setup

A typical `tsconfig.json` includes:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "types": ["node", "resuxjs/globals"]
  },
  "include": [
    "**/*.ts",
    "**/*.tsx",
    "**/*.vue",
    "types/**/*.d.ts",
    "env.d.ts"
  ]
}
```

## Generate declarations

```sh
resux prepare
```

Preparation/build can generate declarations for:

- components,
- auto-imports,
- module type templates,
- build metadata,
- and framework globals.

Generated declarations live under `.resux/types` and should not be edited manually.

## App injections

Add type-safe plugin provides:

```ts
// types/app.d.ts
import 'resuxjs'

declare module 'resuxjs' {
  interface ResuxAppInjections {
    apiClient: {
      get<T>(url: string): Promise<T>
    }
  }
}
```

## Module type templates

```ts
addTypeTemplate({
  filename: 'my-module.d.ts',
  getContents: () => `declare const moduleFeatureEnabled: boolean`
})
```

## Compiler types

Tool authors can import build and compiler types from `resuxjs/compiler`. Application code should normally use `resuxjs` or focused runtime/reactivity subpaths.

## Validation

```sh
npm run typecheck
resux check
resux build
```

Type checking does not replace a framework build: the compiler also validates template support and resumability rules.
