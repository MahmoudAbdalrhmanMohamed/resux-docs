# Lifecycle Hooks Reference

The core hook system is available from `resuxjs/core` and through module context.

## Register a hook

```ts
export default defineResuxModule({
  setup(_options, resux) {
    const remove = resux.hook('build:done', ({ appRoot, outDir, mode }) => {
      console.log({ appRoot, outDir, mode })
    })

    // call remove() when a dynamically registered hook is no longer needed
  }
})
```

## Hook groups

### Configuration and application

- `config:resolved`
- `app:resolve`
- `app:templates`
- `app:templatesGenerated`

### Pages, imports, components, plugins, middleware

- `pages:extend`
- `pages:resolved`
- `imports:dirs`
- `imports:extend`
- `components:dirs`
- `components:extend`
- `plugins:dirs`
- `plugins:extend`
- `middleware:dirs`
- `middleware:extend`

### Vite

- `vite:extendConfig`
- `vite:serverCreated`
- `vite:compiled`

### Build

- `build:before`
- `build:manifest`
- `build:done`
- `build:error`

### Nitro

- `nitro:config`
- `nitro:init`
- `nitro:build:before`
- `nitro:build:public-assets`

### Preparation and development

- `prepare:types`
- `dev:reload`
- `dev:error`

### Page loading and errors

- `page:loading:start`
- `page:loading:end`
- `page:finish`
- `app:error`
- `app:error:cleared`

## Error behavior

Hooks run in registration order. A hook failure is wrapped with the hook name and stops the current hook call, so hook implementations should include useful context and avoid silently swallowing critical failures.

## Public core API

`resuxjs/core` exports `ResuxHooks`, `createResuxHooks`, hook payload types, the module container, config helpers, and core application creation APIs. It is intended primarily for modules, builders, and framework integrations.
