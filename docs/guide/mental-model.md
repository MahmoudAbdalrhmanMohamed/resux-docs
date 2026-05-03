# Mental Model

Resux apps feel like small Vue/Nuxt-style apps, but the runtime model is different.

## Compile time

The compiler reads `.vue` files and turns them into two kinds of modules:

- Server modules that render HTML and create the serialized payload.
- Client handler modules that can be imported later when an event happens.

It also creates a manifest with:

- Routes from `pages/`.
- Components from `components/`.
- Layouts from `layouts/`.
- Plugins and middleware.
- Server handlers and request middleware.
- Vue island entries.
- Runtime config and route rules.

## Request time

When a request arrives:

1. Resux applies security headers and route-rule headers.
2. Request middleware may continue, redirect, abort, return a `Response`, return JSON, or write directly to the Node response.
3. Server API and server routes are matched before page rendering.
4. Route middleware can redirect or abort page navigation.
5. The page and layout tree renders to HTML.
6. Head entries are merged.
7. The payload is serialized into `window.__RESUX__`.

## Browser time

The browser starts with HTML and a tiny runtime.

- Links can be prefetched on hover or focus.
- Same-origin links are intercepted for client-side navigation.
- Route payloads are fetched from `/__resux/route`.
- Matching layouts can stay in place while the page slot swaps.
- Resumed page scopes are cleared when no longer needed.
- Component handlers are imported only when the user interacts.

## State is explicit

Only resumable, serializable data should live in `useState` and `useAsyncData`. Non-serializable values should stay outside resumable handlers or inside Vue islands.

Good:

```ts
const count = useState('count', () => 0)
```

Risky:

```ts
const socket = new WebSocket('wss://example.com')

function send() {
  socket.send('hello')
}
```

If a handler captures values that cannot be resumed safely, Resux should fail during compilation.
