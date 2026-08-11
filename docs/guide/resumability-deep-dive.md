# Resumability Deep Dive

Resumability is the architectural idea at the center of normal Resux components. This page explains what that means in practical terms: **what the server produces, what the browser receives, how an interaction becomes active, what must be serializable, and where the model stops and another runtime should take over**.

If you only need to build an application, [Resumability and Handlers](/guide/resumability-handlers) is the shorter guide. This page is for understanding and debugging the machinery behind it.

## The problem resumability is solving

Server-side rendering can deliver useful HTML quickly, but an interactive page also needs browser behavior. One common approach is hydration:

```text
server renders component tree
        ↓
HTML reaches browser
        ↓
client loads component runtime/code
        ↓
client recreates or walks the component tree
        ↓
client attaches behavior to the existing DOM
```

Resux's normal component model tries to avoid requiring the whole server-rendered tree to become live immediately. Instead, the server output carries enough information for the browser to continue from the rendered result when a specific piece of behavior is needed.

Conceptually:

```text
server renders HTML + resumability metadata
        ↓
browser displays existing HTML
        ↓
small runtime installs navigation/delegation/enhancement support
        ↓
user interacts
        ↓
required handler/scope is loaded and reconstructed
        ↓
only affected bindings are updated
```

This does **not** mean “Resux pages never use JavaScript.” It means JavaScript ownership is more targeted.

## Three things the server must leave behind

For later interaction to work without rebuilding the entire component tree, the browser needs three categories of information.

### 1. Existing DOM

The HTML is already the rendered view. The browser should not need to rerender the page merely to discover what it looks like.

### 2. Serializable state/scope information

A later handler may need values that existed when the server rendered the component. Those values must be representable in a form the browser can safely reconstruct.

### 3. Identity metadata

The runtime needs to connect:

- an event to its generated handler,
- a handler to the scope/state it needs,
- a reactive expression to the DOM binding/block it updates.

The compiler creates this relationship ahead of time.

## Compile-time responsibility

Resumability is not implemented by the browser runtime alone. The compiler does a large part of the work before the application runs.

The compiler can identify supported template structure such as:

- text/interpolation bindings,
- dynamic attributes,
- events,
- `if`/`for` blocks,
- HTML bindings,
- setup expressions,
- and the values a generated handler refers to.

That information allows it to emit stable binding/block/handler metadata.

The important lesson is:

> If the compiler cannot safely describe how an interaction can resume, the correct answer is usually to change the pattern or use another explicit runtime boundary—not to assume the browser will magically reconstruct arbitrary JavaScript state.

## Server rendering is the first execution

Consider a simplified counter:

```vue
<script setup>
const count = ref(0)
const increment = () => count.value++
</script>

<template>
  <button @click="increment">
    Count: {{ count }}
  </button>
</template>
```

The exact generated code is an implementation detail, but conceptually the server can:

1. create the initial `count` state,
2. evaluate the template,
3. render `Count: 0`,
4. record which text binding depends on `count`,
5. record that the click points to generated handler code,
6. serialize the state/scope data needed to continue later.

The server has already executed enough of the component to produce the user-visible result.

## Browser startup is not the second full render

When the HTML arrives, a normal Resux component does not require Vue to mount the component and re-run it as a Vue tree.

The browser runtime instead establishes framework-wide facilities such as:

- delegated event handling,
- route/navigation support,
- access to the serialized payload,
- resumable scope/state registries,
- client-plugin/middleware/enhancement manifests,
- media/client enhancements when needed.

The exact work depends on the page and build, but the important distinction is that the existing HTML is the starting point.

## Event delegation

A resumable event does not require a dedicated eagerly-installed listener object for every server-rendered element.

At a high level, delegated handling works like this:

```text
click occurs
  ↓
shared event layer receives it
  ↓
runtime walks/identifies relevant event metadata
  ↓
handler module identity is resolved
  ↓
module is imported if necessary
  ↓
scope/state is resumed
  ↓
handler executes
```

This design allows the server to render many interactive-looking elements without requiring all their handler modules to execute during initial browser startup.

## Handler code and captures

The difficult part of resumability is not detecting a click. It is recreating the context the handler expects.

A closure in ordinary JavaScript can capture almost anything:

```ts
const client = new SomeDatabaseClient()
const stream = createNonSerializableStream()
const element = document.querySelector('#x')

const handler = () => {
  // these values may not be reconstructable later
}
```

A resumable handler cannot assume arbitrary server objects or ephemeral local objects will exist in the browser later.

### Good capture shapes

Values such as these are naturally compatible with serialization/reconstruction:

- strings,
- numbers,
- booleans,
- null,
- arrays of serializable values,
- plain records of serializable values,
- framework state that is explicitly represented in the Resux payload.

### Risky or invalid capture shapes

Examples that require another design include:

- database/network client instances,
- file handles and streams,
- DOM nodes created on the server,
- functions that are not represented as generated/importable handler code,
- class instances whose identity/prototype is required,
- cyclic object graphs without framework support,
- secret server credentials,
- browser-only library instances.

The exact compiler diagnostics are the source of truth for what is accepted today. The mental model is more durable: **capture data, not opaque live process state**.

## State serialization is also a security boundary

Serializability is not only a technical constraint. Anything intentionally sent in a route/page payload becomes browser-visible.

Never put these into public/resumable state:

- API secrets,
- database credentials,
- private signing keys,
- internal authorization tokens that the browser should not possess,
- sensitive server-only objects converted to strings merely to bypass a serialization error.

Use server APIs, middleware, or server-only modules to keep private authority on the server.

## Binding metadata

After a handler mutates state, Resux needs to update the existing page.

The compiler already knows which template expressions correspond to which generated binding identifiers. The runtime can therefore update marked regions instead of asking a full component renderer to rediscover the entire component tree.

Conceptually:

```text
count.value++
    ↓
reactive dependency invalidated
    ↓
expression for binding B is reevaluated
    ↓
DOM node/range associated with B is patched
```

Different binding types can require different updates:

- text content,
- attributes/properties,
- conditional blocks,
- repeated blocks,
- HTML content,
- other supported generated structures.

This is why the compiler and runtime are tightly connected: **reactivity alone does not know where authored template expressions live in DOM; compilation supplies that map**.

## Reactivity after resume

Normal Resux runtime code uses the custom `resuxjs/reactivity` implementation. Public primitives include:

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

When a resumed scope becomes active, reactive dependencies can continue to drive the bindings owned by that scope.

Familiar API names should not be confused with full Vue component lifecycle semantics. Resux reactivity is a subsystem that can operate without mounting a Vue component tree.

## `useState()` and application state

`useState()` is useful when state needs an application/runtime identity rather than being only a local transient value. The server can seed the state and serialize the relevant value, while later route/interactions can retrieve the state through the runtime registry.

The key questions are still:

- Is the value serializable?
- Is it safe to expose to the browser?
- Is its key/identity stable enough for the intended lifecycle?
- Should it survive only the current route/scope, or does the application expect longer ownership?

Read [State and Reactivity](/guide/state) and [Composables and Globals](/reference/composables) for the current API contract.

## Async data and resumability

`useAsyncData()` and `useFetch()` have a different job from local event handlers. Their resource shape contains reactive `data`, `pending`, and `error` state, but the initial request can often run during SSR.

That avoids a common pattern where the server sends a loading shell and the browser immediately repeats a request that could have been completed before the HTML was sent.

Conceptually:

```text
server request
  ↓
async handler/fetch runs
  ↓
HTML rendered with resolved data
  ↓
resource state serialized
  ↓
browser resumes with existing result
```

Later navigation or explicit refetching may execute additional browser/server requests according to the API being used.

Read [Async Data](/guide/async-data).

## Route navigation is another resume boundary

Same-origin navigation can request a new route payload and replace active route content without performing a traditional full-page navigation.

The browser must then transition framework ownership correctly:

1. run relevant client middleware,
2. obtain the new route payload,
3. dispose route-owned enhancements/resources from the previous route,
4. install/render the next route's HTML/content,
5. update head/style/payload state,
6. register the next route's handlers/enhancements.

A route transition therefore creates a natural lifetime boundary for resumable scopes and client enhancements.

## Client enhancements are not the same thing as resumable events

Some browser libraries do not fit a “click handler mutates serializable state” model. They may need to instantiate a chart, editor, map, observer, carousel, or player around a DOM element.

Resux provides client-enhancement triggers such as:

- `visible`,
- `interaction`,
- `idle`,
- `immediate`,
- `manual`,
- `page-load`.

An enhancement setup can also return cleanup logic. Use this model when the browser feature owns an imperative object that should **not** be serialized as Resux state.

Example mental model:

```text
server: render <div data-chart ...> accessible fallback/content
browser: wait until visible
browser: dynamically import chart package
browser: instantiate chart on the existing element
route leaves: destroy chart/listeners
```

That is progressive enhancement, not component-tree hydration.

## When a Vue island is the right answer

Resumability is not a requirement that every library be forced into the normal Resux compiler model.

Use a Vue island when the feature genuinely depends on:

- a Vue component package,
- Vue component lifecycle behavior,
- Vue provide/inject semantics within the island,
- a complex Vue-owned widget tree,
- existing Vue code whose migration cost is not justified.

Inside the island, Vue owns the subtree. Keep the island boundary deliberate and preferably smaller than the entire page when only one region needs Vue.

The `resuxjs/ui` package is itself implemented with Vue `defineComponent()`, so UI package components belong to this category.

## Resumability does not make every operation lazy

A page can still execute work eagerly when you ask it to. Examples include:

- server setup/data needed to render HTML,
- browser code registered with an immediate/page-load trigger,
- a large Vue island that mounts immediately,
- priority image/media requests,
- client plugins that intentionally run at startup.

Resumability gives the framework an architecture for targeted continuation; good performance still depends on choosing reasonable boundaries.

## A detailed interaction trace

Imagine a product page with an “Add to cart” action.

### During SSR

1. The route is resolved.
2. Product data is loaded.
3. Cart summary state is read/created.
4. The template renders product HTML and the current cart count.
5. The compiler-generated event identity is emitted on/around the action.
6. The cart state needed by the interaction is represented in the payload.
7. The binding for the cart-count text already has an identity.

### Before the user clicks

The product name, price, image, and current cart count are already visible. The add-to-cart handler does not need to have executed in the browser just to display them.

### When the user clicks

1. The delegated event layer receives the click.
2. Resux resolves the generated handler module.
3. The handler is imported if not already available.
4. The relevant cart state/scope is resumed.
5. The handler changes state and/or calls an API.
6. Reactive dependencies update the cart-count binding.
7. Other unrelated product-page components do not need to become live merely because this handler executed.

### If the handler calls the server

Keep authority on the server. The client may request “add product X,” but the server should still validate the session, product, quantity, permissions, and resulting cart state.

Resumability does not move security validation to the browser.

## Common misunderstandings

### “`.vue` means Vue hydrates it”

Not for normal Resux pages/components. The compiler consumes a supported Vue-like SFC syntax, but runtime ownership is Resux unless you explicitly use a Vue island.

### “No hydration means no browser runtime”

Incorrect. Delegated events, route navigation, enhancements, deferred media, and islands can all require browser code.

### “Serializable means safe”

Incorrect. A secret string is serializable but still must not be sent to the browser.

### “Everything should be an event handler”

Incorrect. Imperative browser libraries often fit client enhancements or Vue islands better.

### “Resumability means no work until a click”

Incorrect. SSR and data needed to produce the page still run. Other configured browser features may also start earlier.

## Debugging a failed interaction

Work through the system in this order.

### 1. Did compilation succeed?

A compiler error is different from a runtime error. Fix unsupported syntax, unsafe captures, or malformed template constructs first.

### 2. Is the expected HTML present after SSR?

If the initial markup/value is wrong, the problem may be server setup, routing, async data, rendering, or serialization—not event resume.

### 3. Is event metadata present in the generated output?

If not, inspect how the event expression was authored and what the compiler emitted.

### 4. Can the handler module load?

A failed dynamic import, wrong deployment asset path, or stale build can look like a “click does nothing” problem.

### 5. Can the scope/state be reconstructed?

Serialization/capture problems can surface here.

### 6. Does state change but DOM stay stale?

Then inspect reactivity/binding generation rather than the event itself.

### 7. Is a third-party library actually the owner?

If the interaction depends on an imperative browser package or Vue component, make sure it is inside the correct enhancement/island boundary.

See [Debugging Mental Model](/guide/debugging-mental-model) for a subsystem-by-subsystem checklist.

## Design checklist

Before shipping a new interactive feature, verify:

- the server can render useful initial HTML,
- resumable state is serializable,
- no server secrets are serialized,
- handler captures are reconstructable,
- DOM bindings are generated for the values that must update,
- browser-only packages are behind an explicit client boundary,
- Vue is used only where Vue actually owns the feature,
- client enhancements have cleanup when they allocate resources,
- route transitions do not leave stale listeners/instances,
- accessibility still works before/without optional enhancement where practical.

## Related

- [Architecture Deep Dive](/guide/architecture-deep-dive)
- [Request Lifecycle](/guide/request-lifecycle)
- [Code to Browser](/guide/code-to-browser)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [State and Reactivity](/guide/state)
- [Vue Islands](/guide/vue-islands)
- [Compiler API](/reference/compiler)
- [Runtime Internals](/reference/runtime)
