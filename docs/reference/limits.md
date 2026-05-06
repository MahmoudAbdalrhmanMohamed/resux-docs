# Current Limits

Resux has a stable v1 core plus experimental edges. These limits are part of the current design and should be expected.

## Framework maturity

Stable core:

- Compiler + route manifest for the documented SFC subset.
- SSR renderer and payload serialization.
- Resume runtime and delegated event model.
- Core CLI commands (`init`, `dev`, `build`, `preview`, `start`, `inspect`, `deploy`).
- Resux-native reactivity/composable APIs documented in this site.

Still experimental:

- Vue runtime islands as an escape hatch.
- Unsupported Vue SFC syntax outside the documented subset.
- Nitro adapter scope and deployment behavior beyond documented presets.

## Vue runtime limit

Normal Resux components do not hydrate through Vue. The Vue runtime is available only through Vue islands.

## Compiler subset

Resux supports a focused Vue-like subset. Unsupported Vue features should fail at compile time instead of silently hydrating.

Current supported syntax is listed in [Template Syntax](/guide/template-syntax).

## No fallback hydration

There is no fallback mode where unsupported components automatically hydrate as Vue. Move unsupported interactive widgets to Vue islands.

## Event listener model

The runtime uses delegated resumable listeners. `.capture` and `.passive` can be accepted in templates, but the listener model is still delegated.

## Nitro scope

Nitro support is an adapter/deployment preset, not the primary dev server.

## State serialization

Resumable state and async data must be JSON-serializable. Avoid functions, classes, Maps, Sets, sockets, DOM nodes, and other runtime-only objects in serialized state.

## Browser-only APIs

Use `onMounted` or Vue islands for browser-only APIs. Server rendering does not have `window`, `document`, or other browser globals.

## Roadmap ideas

These are natural future areas, not promises:

- Broader template support.
- More compile-time diagnostics.
- Better typed file conventions.
- Richer dev overlay.
- More deployment presets.
- Better docs examples as the framework evolves.
