# Architecture Deep Dive

This page explains **how the pieces of Resux fit together**. It is intentionally more detailed than the framework tour. Read it when you want to understand not only *which API to call*, but *why that API exists, where it runs, what code it produces, and what happens after the browser receives the page*.

Resux is easiest to understand as several cooperating systems rather than one large runtime:

1. a **project/application model** that discovers pages, layouts, components, plugins, middleware, server handlers, and modules,
2. a **compiler** that turns the supported `.vue`-style source subset into server-renderable code plus resumability metadata,
3. a **server runtime** that resolves routes, runs application logic, renders HTML, composes head/style output, and serializes a route payload,
4. a **browser resumability runtime** that starts from existing server HTML and activates only the behavior required by navigation, an event, or a client enhancement,
5. a **custom reactivity system** used by normal Resux code,
6. an optional **Vue runtime boundary** for Vue islands and `resuxjs/ui`,
7. first-party **icons, fonts, image/video behavior, i18n, modules, package adapters, and deployment adapters** around that core.

The distinction between these systems matters. A feature can be available in a Resux project without meaning that every page ships a Vue application or hydrates a component tree.

## The most important boundary

A normal Resux page may be authored in a `.vue` file, but the filename does not tell you which runtime owns it.

### Normal Resux component

A normal Resux page/component is compiled by the Resux compiler. Its goal is:

- server HTML first,
- serializable state,
- generated binding metadata,
- generated handler modules for browser interactions,
- delegated browser events,
- and activation of only the scope that needs to run.

It is **not a normal Vue component tree waiting for Vue hydration**.

### Vue island

A Vue island is an explicit escape hatch for a region that genuinely needs Vue runtime semantics or a Vue ecosystem package. Inside that boundary, Vue owns the component lifecycle and state.

### `resuxjs/ui`

The UI package is implemented with Vue `defineComponent()`. Therefore `RxButton`, `RxModal`, `RxTabs`, and the other UI package components belong to a Vue runtime boundary. Some are visually static, but they are still Vue component definitions.

This produces a useful rule:

> Choose the **smallest runtime that correctly owns the feature**. Do not create a Vue island merely to render markup that normal Resux HTML can already express.

See [How Resux Uses Vue](/guide/how-resux-uses-vue), [Vue Islands](/guide/vue-islands), and [Component Anatomy](/components/component-anatomy).

## Source layout as an architecture map

The source repository itself reveals the major subsystems:

| Source area | Responsibility | Public surface |
| --- | --- | --- |
| `src/compiler/` | SFC/template compilation, resumable handler generation, validation, directives | `resuxjs/compiler` |
| `src/runtime/` | SSR/runtime APIs, app model, route payloads, server/client behavior, media behavior, packages | `resuxjs`, `resuxjs/runtime`, `resuxjs/globals` |
| `src/reactivity/` | `ref`, `reactive`, `computed`, watchers, scheduling | `resuxjs/reactivity` and runtime re-exports |
| `src/ui/` | Optional Vue UI primitives and motion APIs | `resuxjs/ui` |
| `src/icons/` | Icon registry, loaders, providers/cache/runtime behavior | `resuxjs/icons` |
| `src/fonts/` | Font configuration and generated font/head behavior | `resuxjs/fonts` |
| `src/i18n/` | Locale configuration, route resolution, translation helpers | `resuxjs/i18n` |
| `src/core/` | Core Resux instance/config/module container infrastructure | `resuxjs/core` |
| `src/kit/` | Helpers for authoring Resux modules/extensions | `resuxjs/kit` |
| `src/deploy/` | Deployment target generation/adapters | used by CLI/build flow |
| `src/halal-core/` | Optional policy scanning, reporting, review and integrity workflow | `resuxjs/halal` |
| `src/create.ts` | Project/template creation | `resuxjs/create` |
| `src/nitro-server/` / `src/node.ts` | Server integration/Node handler surfaces | `resuxjs/node` |

For a public-export-to-source-to-tests map, read [Source Map](/reference/source-map).

## Phase 1: project discovery

Before a request can be rendered, Resux needs to know what the application contains. The framework works from conventions such as:

- `app.vue`,
- `error.vue`,
- `pages/`,
- `layouts/`,
- `components/`,
- `plugins/`,
- route middleware,
- `server/api/` and other server handlers,
- Vue islands,
- runtime/config files,
- and contributions from modules.

Modules can extend this picture rather than merely run arbitrary startup code. The module context can contribute CSS, head entries, route rules, components, component directories, auto-imports, plugins, route middleware, server handlers, server plugins, generated templates/types, Vite configuration, Nitro configuration, Vite plugins, pages, and prerender routes.

That is why a Resux module is best understood as a **build/application extension contract**, not just a function that happens to execute during startup.

Read [Modules and Route Rules](/guide/modules-route-rules) and [Resux Kit API](/reference/kit).

## Phase 2: compilation

The compiler converts the supported Resux SFC/template model into artifacts that the server and browser can use independently.

Conceptually, compilation has several jobs.

### Parse authored structure

The compiler needs to understand:

- template elements,
- static and dynamic attributes,
- text/interpolations,
- events and event modifiers,
- supported control-flow directives,
- script/setup logic,
- styles and scoped styles,
- and references that must survive from server rendering to a later interaction.

### Create server-renderable behavior

The server needs enough information to execute setup logic and render a component without starting a browser runtime. That means the generated representation is useful for SSR independently of event activation.

### Create DOM binding metadata

Reactive output must later know **which existing DOM location corresponds to which expression**. Resux therefore generates binding/block metadata rather than requiring the browser to render the whole page a second time just to discover that relationship.

### Split browser handlers

An interaction should be able to load its generated handler code without loading every component that contributed HTML to the page. Handler/module identifiers therefore become part of the server/browser contract.

### Validate resumability boundaries

A value that must be reconstructed later cannot rely on arbitrary unserializable browser/server state. Unsupported or unsafe patterns should be diagnosed during compilation instead of silently becoming hidden full hydration.

This is a key design goal: **the framework should make runtime ownership explicit**.

Read [Compiler API](/reference/compiler), [Template Syntax](/guide/template-syntax), and [Resumability Deep Dive](/guide/resumability-deep-dive).

## Phase 3: server request execution

When a request arrives, the server side has a different responsibility from the compiler. Compilation already produced the application artifacts; now the runtime must execute the request.

A simplified request looks like this:

```text
HTTP request
    ↓
route matching
    ↓
route/global middleware
    ↓
active app + layout + page setup
    ↓
state / async data / fetch / runtime config
    ↓
head + styles + media registrations
    ↓
SSR HTML
    ↓
serialized Resux payload
    ↓
HTTP response
```

The payload is important because HTML alone cannot describe every piece of resumable state. It can contain the information needed for the route, state, async resources, middleware/plugin manifests, module identifiers, runtime configuration, and other data that the browser needs to continue from the server result.

The exact payload should be treated as a framework contract, not an application database. Do not deliberately put secrets into serializable/public state.

Read [Request Lifecycle](/guide/request-lifecycle), [Runtime Config](/guide/runtime-config), and [Security and Caching](/guide/security-caching).

## Phase 4: HTML reaches the browser

At this point the browser already has the rendered page.

This is the architectural difference to keep in mind:

```text
Traditional tree hydration
server HTML → load component runtime → recreate/walk component tree → attach behavior

Resux normal path
server HTML → install small runtime/delegation → resume a scope when it is actually needed
```

That comparison is conceptual, not a promise that browser JavaScript is always zero. Resux still needs browser runtime code for features such as delegated interaction, client navigation, client enhancements, deferred media behavior, and any explicit Vue island. The goal is to avoid treating *all server-rendered HTML* as a component tree that must immediately become live.

## Phase 5: delegated interaction

Suppose the page contains a button whose click changes resumable state.

The server has already rendered the button. The browser does not need to recreate the button merely to make it visible. Instead, the generated HTML/runtime metadata identifies the interaction.

When the event occurs, the browser can conceptually:

1. receive it through the delegated event layer,
2. identify the generated handler/module,
3. import code that has not already been loaded,
4. reconstruct the required serialized scope/state,
5. execute the handler,
6. let reactive dependencies run,
7. update the marked DOM bindings/blocks affected by the change.

This explains why serializability and safe captures matter: **the handler may run later than the server render that created its scope**.

Read [Resumability and Handlers](/guide/resumability-handlers) and [Resumability Deep Dive](/guide/resumability-deep-dive).

## Phase 6: same-origin navigation

Navigation is another place where “HTML first” does not mean “reload everything forever.” Resux can request a route payload for same-origin navigation and update the active route/app shell rather than requiring a full document reload for every transition.

The browser route lifecycle can include:

- client/global route middleware,
- fetching the next route payload,
- replacing route HTML/content,
- updating head/styles/state metadata,
- installing the next route's resumability/client-enhancement metadata,
- disposing resources associated with the previous route.

This is distinct from hydrating every route component. Navigation can be client-side while component interaction remains scope-oriented.

Read [Routing](/guide/routing) and [Rendering Lifecycle](/guide/rendering-lifecycle).

## State ownership

A useful debugging question is: **who owns this state?**

### Server-only state

Examples include request-only secrets, private service clients, server middleware state, or data that should never be serialized to the browser. Keep this on the server.

### Resumable application state

`useState()` and the custom reactivity primitives can participate in Resux's normal runtime model when their values are safe to serialize/reconstruct.

### Async resources

`useAsyncData()` / `useFetch()` have both server-render and browser-navigation concerns. The resource exposes reactive data/pending/error state while the runtime coordinates initial and later requests.

### Vue-island state

Inside a Vue island, Vue owns the state/lifecycle for that subtree. Do not assume a Vue ref is automatically the same thing as Resux resumable state outside the island.

### DOM/plugin state

Third-party browser libraries often own non-serializable DOM instances. Put that state behind a client enhancement, progressive package adapter, or Vue island rather than trying to serialize the library instance.

Read [State and Reactivity](/guide/state), [Async Data](/guide/async-data), and [Third-party Packages](/guide/package-integration).

## Client enhancements

Not every browser feature is naturally an event handler. A chart, carousel, syntax highlighter, or analytics hook may need setup code tied to an element or route.

Resux exposes client-enhancement triggers including:

- `visible`,
- `interaction`,
- `idle`,
- `immediate`,
- `manual`,
- `page-load`.

The trigger is an architectural choice. For example:

- use `visible` when off-screen initialization can wait,
- use `interaction` when the user may never touch the feature,
- use `idle` for useful but non-critical work,
- use `immediate` only when initialization is required as soon as the route becomes active,
- use `manual` when application logic should decide,
- use `page-load` for behavior intentionally tied to initial load semantics.

Client enhancements may return cleanup logic. Cleanup is not optional design polish: route transitions and reinitialization can otherwise leak listeners, observers, or library instances.

Read [Package Integration](/guide/package-integration) and [Integration Cookbook](/guide/integration-cookbook).

## Third-party package modes

Package integration is explicit because package assumptions differ. Resux recognizes modes such as:

| Mode | Appropriate package shape |
| --- | --- |
| `ssr` | Can be imported/executed safely in SSR and bundled normally |
| `clientOnly` | Requires browser globals/DOM and should not execute on the server |
| `serverOnly` | Must stay out of browser output |
| `progressive` | Enhances existing server HTML rather than owning the whole page |

This matters because “installing an npm package” does not answer where the package should run.

## Reactivity is its own subsystem

Normal Resux runtime code uses Resux's reactivity implementation. Public primitives include familiar names such as:

```ts
ref
reactive
computed
watch
watchEffect
readonly
toRef
toRefs
unref
isRef
isReactive
isReadonly
nextTick
```

Familiar names do not mean the entire Vue runtime is present. The reactivity package is deliberately separable from Vue component hydration.

Read [Reactivity API](/reference/reactivity).

## Media architecture

Images and video are renderer/runtime concerns rather than `resuxjs/ui` components.

`ResuxImg`, `ResuxPicture`, and `ResuxVideo` are template primitives handled by the Resux rendering pipeline. That allows features such as:

- transformed image URLs,
- responsive candidates,
- priority/preload information,
- lazy/deferred loading metadata,
- placeholders,
- picture/source output,
- video loading/control metadata,
- and server-side transformation endpoints.

Image transformation depends on `sharp` in the current framework package. Video transformation paths that require media transcoding depend on `ffmpeg` being available in the deployment environment.

Read [Images and Media](/media/), [Images](/media/images), [Image Optimization](/media/optimization), and [Video](/media/video).

## Icons and fonts

Icons and fonts have dedicated package surfaces because their problems are different from generic UI primitives.

- `resuxjs/icons` handles icon registry/provider/runtime concerns.
- `resuxjs/fonts` handles font definitions, head/style generation, preload/performance/CSP considerations.

Keeping these packages separate helps avoid pretending that an `RxIcon` text primitive is the same thing as the full SVG icon system.

## Server architecture

Resux server features are integrated with h3/Nitro-style server infrastructure, but application code should use the documented Resux/server contracts rather than reaching into internal objects without need.

Server capabilities include:

- API routes,
- custom server handlers,
- server middleware,
- server plugins,
- request query/body/header helpers,
- Node handler output,
- deployment-specific Nitro/build output.

Read [Server API](/guide/server-api), [Node Handler API](/reference/node), and [Deployment](/guide/deployment).

## Deployment architecture

The same application source may target different output environments. Resux therefore separates application semantics from deployment generation.

Supported target resolution includes:

- Node,
- Vercel,
- Netlify,
- Cloudflare,
- static output,
- and automatic target selection where configured.

A deployment adapter is not merely a hosting tutorial. It determines build/output conventions, runtime dependencies, handlers, and configuration expected by the target platform.

## What happens at build time vs request time vs browser time

| Concern | Build time | Request time | Browser time |
| --- | --- | --- | --- |
| Discover files/routes | Yes | Uses generated result | No |
| Compile templates/handlers | Yes | Uses artifacts | Imports generated handlers as needed |
| Run page setup | Compile preparation only | Yes for SSR | Resumed/route-specific work as applicable |
| Render initial HTML | No | Yes | Already present |
| Serialize route state | No | Yes | Read/resume |
| Route middleware | Generate manifests | Server middleware path | Client middleware path where configured |
| Reactive DOM update | Generate bindings | Render initial value | Update affected bindings |
| Vue island | Bundle island | May SSR island markup | Vue owns/hydrates island boundary |
| Image transform | Generate/configure routes | Transform/cache endpoint may run | Browser requests resulting URL |
| Client enhancement | Generate manifest | Register metadata | Runs at its trigger |

The exact implementation has more detail, but this table is a useful first diagnostic model.

## Choosing the correct model

Before adding a feature, ask these questions in order:

1. **Can this be plain server-rendered HTML?** Use normal Resux markup.
2. **Does it need resumable interaction tied to application state?** Use normal Resux state/handlers where supported.
3. **Does a browser-only library need to enhance existing HTML?** Use a client enhancement/progressive package model.
4. **Does it genuinely require Vue component semantics or a Vue library?** Use a Vue island.
5. **Is it server-only?** Keep it in server routes/middleware/plugins and out of serialized/public state.
6. **Is it an application-wide build concern?** Consider a module/Kit extension.

This decision process usually produces smaller and clearer runtime boundaries than starting by putting everything in one Vue island.

## Where to continue

- [Request Lifecycle](/guide/request-lifecycle) — trace one request from URL to interaction.
- [Resumability Deep Dive](/guide/resumability-deep-dive) — understand handlers, state, bindings, and event delegation.
- [Code to Browser](/guide/code-to-browser) — follow authored code through generated output.
- [Debugging Mental Model](/guide/debugging-mental-model) — identify which subsystem owns a failure.
- [Source Map](/reference/source-map) — connect public packages and docs to implementation/test files.
