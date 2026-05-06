# What is Resux?

Resux is an experimental resumable web framework with a custom runtime. It uses familiar `.vue` files and `pages/` routing, but normal Resux components do not hydrate through the Vue runtime. Instead, the compiler reads a focused Vue-like SFC subset, renders HTML on the server, serializes state, and lets the browser resume only the scopes that are needed.

::: tip Current scope (0.2.x)
Current `0.2.x` releases provide a stable working core for the compiler subset, SSR renderer, resumable runtime, routing, and CLI workflow. The framework is still experimental overall, and Vue islands plus unsupported Vue syntax outside the documented subset remain experimental.
:::

## The core idea

Most frameworks send HTML and then hydrate the app, which means the browser re-runs a large part of the component tree. Resux tries a different flow:

1. Compile `.vue` files into server modules and small client handler modules.
2. Render the requested route to HTML on the server.
3. Serialize route data, state refs, async data, and module references into the page payload.
4. In the browser, install a tiny delegated event runtime.
5. Load a handler chunk only when the user interacts with an element that needs it.
6. Resume the component scope from serialized data and patch only marked DOM bindings.

## What Resux is good for today

Resux is a good fit for production apps that align with the documented subset and resumability model:

- HTML-first pages.
- Simple `.vue`-style authoring.
- File-based routing.
- Server APIs in the same project.
- Explicit, serializable state.
- Lazy event handler loading.
- A way to add full Vue widgets through islands only where needed.

## What Resux is not yet

Resux is not a full Vue replacement. It intentionally supports a small compiler-friendly subset. Unsupported patterns should fail at compile time instead of silently falling back to hydration.

Use [Current Limits](/reference/limits) before starting a large app.

## Resux vs hydration frameworks

| Area | Hydration framework | Resux |
| --- | --- | --- |
| First response | Server HTML | Server HTML |
| Browser boot | Hydrate component tree | Install small resume runtime |
| Event code | Usually bundled with page/app | Loaded on first interaction |
| Component model | Full framework runtime | Compiler-supported SFC subset |
| Escape hatch | Normal client component | Vue island |
| State model | Runtime reactive graph | Serialized resumable refs |

## Package name

Install and run Resux through the `resuxjs` package:

```sh
npm i resuxjs
npx resuxjs@latest init my-app
```

`npm view resuxjs version` returns `0.2.23` (latest tag checked on 2026-05-07).

The package exposes CLI binaries named `resuxjs`, `resux`, and `create-resux`.
