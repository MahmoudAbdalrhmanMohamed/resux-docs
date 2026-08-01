# Rendering Lifecycle

This page follows a Resux application from command execution to browser interaction and disposal.

## 1. Preparation

`resux prepare`, `resux check --fix`, `resux dev`, and `resux build` can scaffold required safe files and generated directories.

Preparation produces or validates items such as:

- `env.d.ts`
- `tsconfig.json`
- `nitro.config.ts`
- `.resux-nitro/handler.ts`
- generated component/import/type declarations
- ignored generated paths

## 2. Configuration and modules

Resux loads `resux.config.ts`, resolves defaults, and creates the module container. Modules contribute config and files, then lifecycle hooks run, including `config:resolved` and `app:resolve`.

## 3. Discovery

The compiler discovers:

- components and component directories,
- pages and layouts,
- `app.vue` and `error.vue`,
- plugins and client enhancements,
- route and request middleware,
- server handlers and server plugins,
- Vue islands,
- auto-import directories,
- and package usage.

## 4. SFC compilation

Each Resux `.vue` file is parsed with Vue's compiler packages but converted into Resux's own component definition.

Compilation produces:

- server source,
- browser handler source,
- template nodes,
- expression and binding ids,
- styles and scope ids,
- handler names,
- and page metadata.

Unsupported style languages, style modules, style `src`, unsupported directives, and unsafe handler captures fail with a `ResuxCompileError` and source location when available.

## 5. Manifest and generated output

The build records routes, components, layouts, plugins, enhancements, middleware, server handlers, islands, route rules, runtime config, package diagnostics, and generated type information.

Development emits Vite client entries. Production bundles client assets and a server manifest, then builds Nitro output.

## 6. Request handling

For an HTTP request, Resux applies this broad order:

1. health and internal framework endpoints,
2. request middleware,
3. route-rule matching,
4. server API/custom route matching,
5. static and generated media handling,
6. page route matching,
7. route middleware,
8. SSR rendering,
9. response headers and document output.

Redirects and aborts can stop the flow earlier.

## 7. SSR rendering

Rendering creates an app context, runs eligible plugins, executes page/layout/component setup, resolves async data, builds component scopes, renders template nodes, merges app/page/module head entries, and serializes the payload.

The result contains:

```ts
type RenderResult = {
  html: string
  payload: ResuxPayload
  head: HeadEntry
  statusCode?: number
}
```

## 8. Browser boot

The runtime reads the payload, installs delegated listeners, initializes route navigation, registers client plugins and middleware, and scans registered client enhancements.

It does not eagerly execute every handler module.

## 9. Interaction resume

When an event reaches a Resux-marked element:

1. modifiers and filters are checked,
2. the component handler module is imported if needed,
3. the serialized scope is reconstructed,
4. the handler runs,
5. reactive dependencies trigger updates,
6. marked DOM bindings are patched.

## 10. Client navigation

Internal links are intercepted when eligible. The runtime asks `/__resux/route` for the destination, handles redirect/abort results, updates the page content and head, applies the new payload, and runs page loading/finish hooks.

## 11. Cleanup

When enhancements or page content are replaced, Resux disconnects shared observers, removes pending registrations, and calls cleanup functions returned by enhancements or mounted work.

This lifecycle is why cleanup-returning setup functions are important for global listeners, observers, timers, and library instances.
