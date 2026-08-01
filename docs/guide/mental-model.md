# Mental Model

Think of Resux as a compiler and server framework that leaves a structured continuation inside the HTML response.

## Not hydration

Hydration commonly downloads component code and re-executes a client component tree to attach behavior. Resux instead serializes the minimum information needed to continue a rendered scope later.

The browser receives:

- finished HTML,
- scope identifiers,
- serializable state and async data,
- binding metadata already present in the DOM,
- module URLs,
- route and page metadata,
- public config,
- and client plugin/middleware manifests.

## A component becomes two concerns

For a resumable component, the compiler emits:

1. **Server behavior** that runs setup and renders HTML.
2. **Client handler behavior** that resumes state and runs interaction code.

This split explains several framework rules:

- event handlers cannot capture arbitrary server objects,
- state crossing the boundary must be serializable,
- direct browser APIs belong in mounted or client-only contexts,
- and unsupported template behavior is rejected instead of hydrated.

## Navigation is another server render

Same-origin navigation does not reconstruct a full client router component tree. The runtime requests a route payload, lets route middleware run, receives rendered output and metadata, updates the page region and head, then activates the new payload.

The server remains the source of truth for route matching and SSR output.

## Reactivity updates marked DOM

Resux reactivity tracks dependencies inside resumed scopes. When state changes, the runtime evaluates compiler-recorded expressions and patches only affected bindings.

This is why the supported expression and directive subset matters: the compiler must understand what can change.

## Progressive behavior is separate from component hydration

Some behavior is better represented as a DOM enhancement than a component runtime. Resux supports named enhancements with triggers:

- `visible`
- `interaction`
- `idle`
- `immediate`
- `manual`
- `page-load`

Enhancements can return cleanup functions and are disposed when needed.

## Vue islands are explicit

A Vue island creates a separate Vue runtime boundary for a widget that genuinely needs Vue component semantics or a Vue-specific library. It does not convert surrounding Resux components into hydrated Vue components.

## Rules that follow from the model

1. Prefer server work for data access and secrets.
2. Store only serializable values in resumable state.
3. Keep handlers small and capture reconstructable values.
4. Use route rules for HTTP policy.
5. Use modules for build-time extension.
6. Use progressive enhancements for DOM libraries.
7. Use Vue islands only where full Vue is necessary.
8. Treat generated output as disposable build artifacts.
