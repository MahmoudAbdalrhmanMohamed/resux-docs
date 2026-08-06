# Code to Browser

This guide follows one small Resux component line by line: from the code you write, through compilation and server rendering, to the exact work the browser performs after a click.

The generated snippets below are **conceptual and simplified**. Internal module names, payload fields, and DOM marker attributes may change. Use them to understand the flow, not as public APIs.

## The complete example

```vue
<script setup lang="ts">
const count = useState('counter', () => 0)
const doubled = computed(() => count.value * 2)

function increment() {
  count.value++
}
</script>

<template>
  <section>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubled }}</p>
    <button @click="increment" :disabled="count >= 10">
      Add
    </button>
  </section>
</template>
```

<div class="resux-pipeline" role="list" aria-label="Resux code pipeline">
  <div class="resux-pipeline-step" role="listitem"><strong>1. Author</strong><span>You write one SFC.</span></div>
  <div class="resux-pipeline-arrow" aria-hidden="true">→</div>
  <div class="resux-pipeline-step" role="listitem"><strong>2. Compile</strong><span>Resux builds server and browser records.</span></div>
  <div class="resux-pipeline-arrow" aria-hidden="true">→</div>
  <div class="resux-pipeline-step" role="listitem"><strong>3. Render</strong><span>The server returns HTML and a small payload.</span></div>
  <div class="resux-pipeline-arrow" aria-hidden="true">→</div>
  <div class="resux-pipeline-step" role="listitem"><strong>4. Resume</strong><span>The browser loads behavior only when needed.</span></div>
</div>

## Line-by-line map

| Authored line | Compiler meaning | Server work | Browser work |
| --- | --- | --- | --- |
| `useState('counter', () => 0)` | Create named, component-scoped resumable state | Create the ref for this rendered scope and serialize its JSON-safe value | Restore the same scoped ref when the component resumes |
| `computed(() => count.value * 2)` | Create derived reactive state | Evaluate it when the template reads it | Re-evaluate it only after a dependency changes |
| `function increment()` | Register a browser-safe handler candidate | Keep handler metadata; do not run it | Import and run it after the matching click |
| `{{ count }}` | Create a dynamic text binding | Render the initial text | Patch only this text when `count` changes |
| `{{ doubled }}` | Create another dynamic text binding | Render the initial derived value | Patch it after `count` invalidates the computed value |
| `@click="increment"` | Normalize the shortcut to Resux event metadata | Render a resumable handler marker | A shared delegated listener finds the marker |
| `:disabled="count >= 10"` | Normalize the shortcut to a dynamic attribute binding | Render the initial disabled state | Add or remove the attribute after updates |

## Step 1: parse the SFC

Resux uses Vue compiler packages to parse the `.vue` file, but the normal component does not become a hydrated Vue application.

The compiler separates:

- the setup script,
- the template tree,
- event handlers,
- dynamic expressions,
- styles,
- and page metadata when the file is a page.

The concise template syntax is normalized:

```vue
<button @click="increment" :disabled="count >= 10">
```

means the same Resux operations as:

```vue
<button rx-on:click="increment" rx-bind:disabled="count >= 10">
```

`@event` and `:binding` are authoring shortcuts. The compiler stores one normalized event and binding model after parsing.

## Step 2: create the compiled component model

The real generated source is optimized and may change. Conceptually, Resux records information similar to this:

```ts
{
  id: 'components/counter',
  setup: serverSetupFunction,
  template: [
    { type: 'text-binding', expression: 'count' },
    { type: 'text-binding', expression: 'doubled' },
    { type: 'event', name: 'click', handler: 'increment' },
    { type: 'attribute-binding', name: 'disabled', expression: 'count >= 10' }
  ],
  browserHandlers: {
    increment: 'generated handler module'
  }
}
```

Three design choices matter here:

1. Static HTML remains static and needs no browser expression.
2. Dynamic bindings receive stable internal identifiers so they can be found later.
3. Handler code is separated so it can be imported on demand instead of joining one large page bundle.

## Step 3: run setup on the server

For the initial request, Resux creates a component scope and executes setup.

```ts
const count = useState('counter', () => 0)
```

The key belongs to this rendered component scope. The same key used by another component instance does not overwrite it.

```ts
const doubled = computed(() => count.value * 2)
```

The computed value is lazy. It is evaluated because the server template reads it, and its value is cached until `count` changes.

The handler is defined, but no click has happened, so the server does not run it.

## Step 4: render HTML

The server evaluates the template with `count = 0` and `doubled = 0`.

A simplified result looks like this:

```html
<section>
  <p data-resux-binding="count">Count: 0</p>
  <p data-resux-binding="doubled">Double: 0</p>
  <button
    data-resux-handler="increment"
    data-resux-binding="disabled"
  >
    Add
  </button>
</section>
```

The `data-resux-*` names above are explanatory placeholders. The important idea is that the browser receives usable HTML plus small markers for the dynamic parts. It does not receive an empty shell that must wait for a full application bundle before showing content.

## Step 5: serialize only resumable data

Because `count` uses `useState`, its current value crosses the server/browser boundary.

A simplified scope payload looks like this:

```json
{
  "scopes": {
    "s0": {
      "module": "components/counter",
      "state": {
        "counter": 0
      }
    }
  }
}
```

Only JSON-compatible values belong in resumable state. Do not place functions, DOM nodes, class instances, sockets, streams, database clients, `Map`, or `Set` in `useState` or `useGlobalState`.

## Step 6: boot without full hydration

On page load, the browser runtime:

1. reads the Resux payload,
2. installs shared delegated event listeners,
3. prepares routing and client plugins,
4. and leaves handler modules unloaded until they are needed.

The browser does **not** walk the whole page to recreate a hydrated Vue component tree.

## Step 7: resume after the click

When the user clicks **Add**:

1. the shared click listener receives the event,
2. the event path is checked for Resux handler metadata,
3. the generated handler module is imported if it is not cached,
4. scope `s0` is reconstructed from the payload,
5. `increment()` runs,
6. `count.value` changes from `0` to `1`,
7. `doubled` becomes dirty,
8. dependent bindings are scheduled for update.

Conceptually, only this authored line performs the mutation:

```ts
count.value++
```

The reactivity graph determines everything that depends on it.

## Step 8: patch only affected DOM

Resux re-evaluates the marked expressions:

```ts
count          // 1
count * 2      // 2
count >= 10    // false
```

The resulting DOM becomes:

```html
<p>Count: 1</p>
<p>Double: 2</p>
<button>Add</button>
```

Static elements are not rebuilt. Unrelated components do not rerender. This is the performance goal of resumability plus fine-grained reactivity.

## Choose the smallest state tool

The counter uses `useState` to make the serialization step visible. In application code, choose the smallest scope that satisfies the requirement.

| Requirement | Use |
| --- | --- |
| One ordinary local value | `ref` |
| Related local fields or an object | `reactive` |
| A value derived from reactive state | `computed` |
| Named component state that must be serialized and resumed | `useState` |
| One intentionally shared value across component scopes | `useGlobalState` |
| Server data with pending and error state | `useAsyncData` or `useFetch` |

Do not use `useState` as a default replacement for `ref`. Do not use `useGlobalState` for a button, modal, tab, or form field owned by one component.

## Follow the flow while debugging

Use this order when a value is correct on the server but wrong after interaction:

1. Confirm the authored expression and handler use supported syntax.
2. Check compiler diagnostics and source locations.
3. Confirm the value is JSON-compatible when it crosses the boundary.
4. Inspect the rendered HTML for a dynamic binding or handler marker.
5. Run `resux dev --trace-resume` to follow handler loading and scope restoration.
6. Check that the handler mutates a tracked ref or reactive property.
7. Confirm cleanup is returned for timers, observers, listeners, and client enhancements.

Continue with [Rendering Lifecycle](/guide/rendering-lifecycle), [Resumability and Handlers](/guide/resumability-handlers), [State and Reactivity](/guide/state), and the [Compiler Reference](/reference/compiler).
