# Core Concepts

Resux combines compile-time analysis, SSR, serialized state, delegated events, route payload navigation, progressive enhancement, and explicit extension points.

## Concept map

| Concept | Meaning |
| --- | --- |
| Resux component | A compiled `.vue` component using the documented subset, without Vue hydration. |
| Scope | One rendered component instance and its resumable state, async data, props, and module id. |
| Payload | Route, scopes, client modules, public config, plugins, middleware, page metadata, and island entries serialized for the browser. |
| Binding | A compiler-marked text, attribute, class, style, visibility, or HTML location that can be patched after resume. |
| Handler module | Client code generated for a component's event handlers. |
| Route payload | Fresh rendered output fetched for same-origin client navigation. |
| Client enhancement | Named progressive behavior attached by trigger and disposed when no longer needed. |
| Package mode | How a third-party package participates in SSR and the browser: `ssr`, `clientOnly`, `serverOnly`, or `progressive`. |
| Module | Build-time extension contributing files, config, hooks, templates, types, Vite/Nitro changes, or routes. |
| Hook | Typed lifecycle event emitted by core, compiler, Vite, Nitro, loading, and error flows. |
| Vue island | Opt-in component mounted by the full Vue runtime. |

## Compile-time responsibilities

The compiler:

- discovers project conventions,
- parses `.vue` SFCs,
- validates template and style support,
- transforms setup code,
- records bindings and handlers,
- verifies resumable captures,
- creates routes and localized route variants,
- analyzes third-party package usage,
- emits server modules and client entry points,
- and writes generated manifests and types.

## Server responsibilities

The server:

- applies request middleware and route rules,
- handles APIs and custom server routes,
- runs route middleware,
- renders the app shell, layout, and page,
- merges head entries,
- serializes state and public configuration,
- serves runtime and handler assets,
- transforms media when configured,
- and exposes `/__resux/health`.

## Browser responsibilities

The browser runtime:

- reads the serialized payload,
- delegates supported events,
- imports handlers on demand,
- resumes scopes,
- applies DOM patches,
- runs client plugins and middleware,
- handles route payload navigation,
- activates registered client enhancements,
- and disposes observers and cleanup functions.

## Choosing the correct tool

| Need | Preferred feature |
| --- | --- |
| Shared serializable UI state | `useState` |
| SSR data with pending/error refs | `useAsyncData` or `useFetch` |
| Private database or credential work | server API, middleware, plugin, or utility |
| App-wide provided value | plugin and `useResuxApp()` |
| Build-time extension | module or `resuxjs/kit` |
| Browser-only DOM behavior | client enhancement |
| Full Vue component behavior | Vue island |
| Third-party library loaded later | progressive package adapter |
| Response headers, cache, redirects, CORS | route rules |

## Serialization is architectural

Resux does not reconstruct a complete client component tree. It resumes from serialized values. Functions, class instances, sockets, DOM nodes, and other runtime-only objects should not be stored in resumable state.

Read [Resumability and Handlers](/guide/resumability-handlers) and [Execution Contexts](/guide/execution-contexts) next.
