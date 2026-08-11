# Request Lifecycle: URL to HTML to Interaction

This guide follows a Resux application through one complete request. The goal is to answer a practical question:

> **When something happens in my app, which part of Resux is responsible for it?**

We will trace a page from the incoming URL, through routing and server rendering, into the browser, through a click, and finally through a client-side route transition.

## The short version

A normal page can be pictured like this:

```text
Browser requests /products/42
        ↓
server receives request
        ↓
route + middleware are resolved
        ↓
app/layout/page setup runs
        ↓
state and async data are resolved
        ↓
head/styles/media metadata are collected
        ↓
HTML + Resux payload are returned
        ↓
browser displays HTML immediately
        ↓
Resux installs delegated/navigation/enhancement support
        ↓
user clicks an interactive element
        ↓
only the required handler/scope is resumed
        ↓
reactive DOM bindings update
```

The sections below explain each stage in more detail.

## Example application

Imagine this route:

```text
pages/products/[id].vue
```

The page:

- loads product `42`,
- renders a product image,
- shows the current cart count,
- has an “Add to cart” button,
- sets SEO metadata,
- and links to `/cart`.

We will use that example throughout the lifecycle.

## Stage 0: build preparation

Long before the first HTTP request, the build/dev pipeline discovers the application structure and compiles source files.

This stage can include:

- page/layout/component discovery,
- plugin and middleware discovery,
- server-handler discovery,
- module contributions,
- SFC/template compilation,
- generated handler modules,
- generated route/component manifests,
- generated styles/head information,
- generated templates/types,
- Vite/Nitro extension,
- deployment output preparation.

The request does **not** start by parsing every application source file from scratch. It executes prepared framework/application artifacts.

If a template feature is unsupported or a resumable capture cannot be represented safely, the best place to catch it is usually compilation/build time.

## Stage 1: request enters the server

The browser requests:

```text
GET /products/42?ref=homepage
```

The server establishes a request/route context. Conceptually, route information includes values such as:

```ts
{
  path: '/products/42',
  params: { id: '42' },
  query: { ref: 'homepage' }
}
```

Depending on environment and request, context can also include information such as origin/user-agent data.

This context is the foundation for route matching, middleware, data loading, SEO, and other request-specific behavior.

## Stage 2: file route matching

The file:

```text
pages/products/[id].vue
```

matches `/products/42`, and the dynamic segment becomes `params.id`.

Route matching also determines page metadata such as:

- layout choice,
- route middleware,
- title/meta configuration,
- other supported route metadata.

If the route cannot be found, the request moves into the not-found/error path rather than normal page rendering.

Read [Routing](/guide/routing) for file naming and parameter rules.

## Stage 3: middleware

Middleware runs before the final route is accepted/rendered.

Typical jobs include:

- authentication checks,
- redirects,
- locale decisions,
- access control,
- logging/request annotation,
- route policy.

A route middleware result may continue, redirect, or abort according to the current runtime contract.

### Why middleware is early

Suppose `/products/42` is private. It is wasteful and unsafe to fully render the page and only then discover that the visitor must be redirected.

Middleware establishes whether the route should proceed before expensive/application-specific work is finalized.

### Server vs client navigation

The same conceptual route policy can have different execution paths during:

- the initial server request,
- later client-side navigation.

Do not assume code that reads a Node-only object can also run during browser navigation. Read [Execution Contexts](/guide/execution-contexts) and [Middleware](/guide/middleware).

## Stage 4: app shell and layout selection

The active page does not render in isolation. Resux can compose:

```text
app.vue
  └─ layout
      └─ page
```

The app shell can provide site-level structure, while the selected layout wraps the page-specific content.

For the product example:

```text
app.vue
  └─ layouts/shop.vue
      └─ pages/products/[id].vue
```

A page may choose a named layout or disable layout use according to the supported page-meta API.

If rendering throws, `error.vue` / framework error handling can replace the normal page path.

Read [Layouts](/guide/layouts) and [App Shell and Errors](/guide/app-shell-errors).

## Stage 5: setup and application state

The page's supported setup logic executes for the render context.

For example:

```ts
const route = useRoute()
const cartCount = useState('cart-count', () => 0)
```

The important architectural point is that this is **the server's first real execution of the page**, not merely a static template substitution pass.

State created here may contribute to:

- rendered HTML,
- the serialized route payload,
- later resumed interactions.

### State must have the correct ownership

Ask whether a value is:

- request/server-only,
- safe resumable/public state,
- async-data state,
- Vue-island state,
- or a browser-only library instance.

Do not force all of these categories through `useState()`.

## Stage 6: async data and fetch

The product page needs product data before rendering useful content.

Conceptually:

```ts
const product = await useAsyncData('product', () => {
  return $fetch(`/api/products/${route.params.id}`)
})
```

The exact API usage depends on the application and current documented signatures, but the lifecycle idea is stable:

1. server-side data work can happen before HTML is finalized,
2. the resolved resource contributes to the render,
3. resource state can be represented in the payload,
4. the browser does not need to begin from an empty loading shell merely because the data API is reactive.

### Avoid accidental duplicate authority

If the product API validates permissions, the server API remains responsible for those permissions. SSR calling the API does not remove the need for validation on later client requests.

Read [Async Data](/guide/async-data) and [Server API](/guide/server-api).

## Stage 7: head and SEO composition

While rendering the page, Resux can collect head information such as:

- title,
- meta tags,
- links,
- styles,
- HTML attributes,
- SEO-specific metadata.

For the product page this might produce:

```text
<title>Mechanical Keyboard – Store</title>
<meta name="description" content="...">
<meta property="og:image" content="...">
```

This work belongs on the server for the initial request so crawlers and browsers receive meaningful document metadata with the HTML response.

During later client navigation, the browser route runtime must update head state to match the new route.

Read [Head and SEO](/guide/head-seo).

## Stage 8: media resolution

The page contains something like:

```vue
<ResuxImg
  :src="product.image"
  :alt="product.name"
  width="1200"
  height="900"
  sizes="(max-width: 768px) 100vw, 50vw"
/>
```

The Resux renderer can resolve image behavior while it generates native markup. Depending on options/configuration this can include:

- transformed URLs,
- responsive `srcset` candidates,
- `sizes`,
- density candidates,
- lazy/deferred metadata,
- placeholders,
- preload/fetch priority,
- provider/cache configuration.

This does not require turning the image into a Vue component.

Read [Images](/media/images) and [Responsive Images](/media/responsive-images).

## Stage 9: template rendering

The active app/layout/page tree is rendered to HTML.

A simplified output might look conceptually like:

```html
<main>
  <h1>Mechanical Keyboard</h1>
  <img ...>
  <p>$129</p>
  <button data-resux-event="...">Add to cart</button>
  <span data-resux-binding="...">0 items</span>
  <a href="/cart">View cart</a>
</main>
```

The exact generated attributes are internal and can change. The architectural point is that HTML can contain **identity metadata** that connects later browser behavior to compiler-generated handlers/bindings.

### Why render first?

The user should receive useful document content even before every optional interaction module has executed in the browser.

## Stage 10: payload serialization

The server also emits/associates a Resux payload with the route.

The payload can contain the browser-visible information required to continue from the server result, such as:

- route state,
- serializable app/state values,
- async-data results/status,
- runtime/public configuration,
- generated handler/scope identities,
- client plugin/middleware/enhancement metadata,
- route/module information needed by navigation/resume.

### Payload is browser-visible

This has a security consequence:

> Never serialize a secret just because JavaScript can stringify it.

Server credentials, private tokens, signing keys, database objects, and other private authority belong in server-only code.

## Stage 11: HTTP response is sent

The response now contains enough information for the browser to display the page and later activate its intended behavior.

At this moment, the user can already see the server-rendered page.

The response is not waiting for Vue to mount every normal Resux component before it becomes meaningful.

## Stage 12: browser bootstrap

The Resux browser runtime starts from the existing server result.

Depending on the page/configuration it can establish:

- payload/state access,
- delegated events,
- same-origin navigation interception/support,
- route/client middleware support,
- client plugins,
- client enhancement triggers,
- deferred media behavior,
- resumable scope registries.

This is framework bootstrap, but it is **not equivalent to hydrating a normal Vue component tree**.

## Stage 13: the page sits idle

This stage is easy to overlook.

The user may read the product page for ten seconds and never click anything. During that period:

- the server-rendered product content remains useful,
- a below-the-fold image may stay deferred,
- an interaction-triggered package may stay unloaded,
- a click handler module may stay unloaded,
- an off-screen client enhancement may not initialize.

This is where choosing good activation triggers can translate architecture into real browser cost savings.

## Stage 14: user clicks “Add to cart”

Now an interaction needs to become active.

Conceptually:

```text
click event
  ↓
delegated Resux event layer
  ↓
generated event identity
  ↓
load handler module if needed
  ↓
resume required state/scope
  ↓
execute handler
  ↓
reactive dependencies update DOM bindings
```

The browser does not need to make the product image, page heading, footer, and every unrelated component live simply because this button was clicked.

Read [Resumability Deep Dive](/guide/resumability-deep-dive).

## Stage 15: handler talks to the server

A real cart action normally calls a server endpoint.

For example, conceptually:

```text
POST /api/cart
{ productId: 42, quantity: 1 }
```

The server should validate:

- the authenticated session,
- product identity,
- quantity limits,
- inventory/business rules,
- pricing/authorization rules,
- final cart mutation.

The browser can be resumable and efficient without becoming trusted authority.

## Stage 16: reactive update

Assume the server request succeeds and the handler increments `cartCount`.

The Resux reactivity layer invalidates the dependent expression, and the runtime updates the generated DOM binding associated with the cart-count output.

Conceptually:

```text
cartCount: 0 → 1
        ↓
computed/watch/effect dependencies as applicable
        ↓
cart-count template expression reevaluated
        ↓
existing binding changes to “1 item”
```

This is a targeted DOM update. It is not a requirement to rerender the entire document.

## Stage 17: user navigates to `/cart`

The user activates a normal same-origin link/navigation.

A client route transition can proceed roughly as follows:

1. determine the destination,
2. run relevant browser route middleware,
3. request the Resux route payload/document data for `/cart`,
4. handle redirect/error results,
5. dispose route-owned resources/enhancements from the product route,
6. replace/update route content,
7. update route state and head/styles,
8. install/register the cart route's handler/enhancement metadata,
9. update browser history.

The browser now has the next server-derived route state without requiring a full Vue app hydration architecture.

## What gets disposed?

Route transitions matter because browser features can allocate resources:

- event listeners,
- observers,
- timers,
- third-party widget instances,
- subscriptions,
- route-owned enhancement state.

Client enhancements can return cleanup logic. Vue islands have Vue lifecycle ownership. Resux resumable/runtime scopes also have framework lifetime boundaries.

If a library continues acting on DOM after its route disappeared, suspect missing cleanup or incorrect ownership.

## Error path

Failures can occur at different layers, and they should not be treated as one generic “page failed.”

### Route not found

The router cannot match an application page/server route.

### Middleware abort/redirect

The route was intentionally prevented or redirected.

### Setup/data error

Application setup, async data, or server logic throws/fails.

### Render error

The active component/app shell cannot produce output.

### Handler resume error

Initial HTML was correct, but a later interaction cannot load/reconstruct/execute.

### Navigation error

The current page works, but fetching or applying the next route fails.

### Vue island error

Only the explicit Vue-owned boundary fails to mount/hydrate/execute.

These symptoms point to different source areas. See [Debugging Mental Model](/guide/debugging-mental-model).

## Initial load vs client navigation

A useful comparison:

| Concern | Initial request | Client navigation |
| --- | --- | --- |
| URL arrives through | HTTP document request | Router/history/navigation |
| Route matching | Server | Browser/server route flow |
| Server middleware | Yes | When route payload/server work is requested |
| Client middleware | Not the primary first gate | Can run before/around client transition |
| Page data | Resolved for SSR | Next route payload/fetch flow |
| HTML | Returned in document | Replaced/updated from next route result |
| Head | Included in response | Updated in document |
| Handler metadata | Included/registered | Replaced/registered for next route |
| Full page reload | Yes, this is initial document | Not normally required for supported same-origin navigation |

## Where Vue islands fit into this lifecycle

Suppose the product page contains a complex Vue-based review editor.

The outer page still follows the normal Resux lifecycle. At the island boundary:

```text
Resux SSR/page
  ├─ product markup (Resux-owned)
  ├─ add-to-cart handler (Resux resumable)
  └─ review editor island
       └─ Vue-owned subtree/runtime
```

The island may SSR and then hydrate/mount according to the island integration, while the surrounding page remains owned by Resux.

This is why “the project uses Vue” and “the whole page hydrates as Vue” are not the same statement.

## Where `resuxjs/ui` fits

`resuxjs/ui` components are Vue components. If you use `RxModal` for a product dialog, that modal belongs inside the Vue-owned boundary that renders it.

If the page only needs a styled static badge, using native Resux markup may be cheaper than introducing a Vue island solely for `RxBadge`.

Read [Component Anatomy](/components/component-anatomy).

## Where third-party packages fit

A package can enter the lifecycle in several ways:

- **SSR package**: usable while rendering/server bundling.
- **server-only package**: used only in server code.
- **client-only package**: loaded only in browser code.
- **progressive package**: enhances server HTML after a trigger.
- **Vue package**: typically belongs inside a Vue island.

The package's runtime assumptions—not its popularity—should determine the integration mode.

## Request-lifecycle debugging checklist

When something breaks, identify the last stage that definitely worked.

1. **Build succeeded?** If no, compiler/config/module/build problem.
2. **Route matched?** If no, file routing/middleware problem.
3. **Correct initial data?** If no, state/async/server API problem.
4. **Correct initial HTML?** If no, SSR/template/layout problem.
5. **Correct head/media URLs?** If no, renderer/config/provider problem.
6. **Browser bootstrap healthy?** If no, asset/runtime/deployment problem.
7. **Click metadata/handler loads?** If no, resumability/generated asset problem.
8. **Handler runs?** If no, capture/scope/application error.
9. **State changes?** If no, handler/reactivity problem.
10. **DOM changes?** If no, binding/reactivity problem.
11. **Next route works?** If no, client navigation/middleware/payload problem.
12. **Resources disappear on route leave?** If no, cleanup/lifetime problem.

## Related

- [Architecture Deep Dive](/guide/architecture-deep-dive)
- [Resumability Deep Dive](/guide/resumability-deep-dive)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [Code to Browser](/guide/code-to-browser)
- [Debugging Mental Model](/guide/debugging-mental-model)
- [Execution Contexts](/guide/execution-contexts)
