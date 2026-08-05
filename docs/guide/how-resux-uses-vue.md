# How Resux Uses Vue

Resux deliberately uses parts of the Vue ecosystem without turning every Resux component into a hydrated Vue application.

That distinction is central to the framework:

- `.vue` single-file components are the authoring format.
- Vue compiler packages parse the SFC and template grammar.
- Resux transforms the parsed result into its own template model, server modules, resumable handlers, payload, and DOM patches.
- The Vue runtime is loaded only for explicit Vue islands.

## Dependency map

| Package | Why Resux uses it | Used in normal browser runtime? |
| --- | --- | --- |
| `@vue/compiler-sfc` | Parse `<template>`, `<script setup>`, and `<style>` blocks; compile scoped CSS | No |
| `@vue/compiler-dom` | Parse template elements, expressions, bindings, events, and directives | No |
| `@vitejs/plugin-vue` | Build explicit components under `islands/vue` | Only for Vue-island bundles |
| `vue` | Mount opt-in Vue islands and support Vue tooling | Not for normal Resux components |
| Vite | Build browser handler modules, Vue-island entries, CSS, and assets | Build/dev tooling |

## Compilation pipeline

A normal page such as `pages/index.vue` moves through these stages.

### 1. File discovery

The Resux compiler discovers pages, layouts, components, plugins, middleware, APIs, and Vue islands using file conventions.

### 2. SFC parsing

`@vue/compiler-sfc` separates the component into template, setup script, and style blocks. This gives Resux a stable parser for the familiar `.vue` format.

### 3. Resux directive normalization

Public Resux templates use the branded `rx-*` prefix and official shortcuts for events and bindings:

```vue
<button @click="save" :disabled="pending">Save</button>
<p rx-if="error">{{ error.message }}</p>
```

The explicit forms are equivalent:

```vue
<button rx-on:click="save" rx-bind:disabled="pending">Save</button>
```

Before the Vue template parser runs, Resux converts only branded directive attribute names to the equivalent internal Vue-parser spelling. For example, `rx-if` becomes `v-if` internally and `rx-on:click` becomes `v-on:click` internally. The `@event` and `:binding` shortcuts are already parser-level shorthand and compile into the same Resux event and binding model.

This is a parser adapter, not a runtime dependency. Script strings, CSS, comments, visible text, and attribute values are not rewritten.

### 4. Resux template compilation

`@vue/compiler-dom` produces an AST. Resux then creates its own serializable template nodes for:

- static and dynamic attributes,
- text and interpolation bindings,
- events and modifiers,
- conditional blocks,
- list blocks,
- text/HTML/model behavior,
- generated binding IDs,
- and expression closures.

Unknown or unsupported behavior fails during compilation instead of silently hydrating the whole component.

### 5. Setup analysis

The TypeScript-based compiler analyzes `<script setup>` to identify:

- top-level bindings,
- imports,
- refs that should auto-unwrap in templates,
- event handlers,
- resumable captures,
- page metadata,
- and unsupported non-serializable captures.

Normal component code receives Resux APIs such as `ref`, `reactive`, `computed`, `useFetch`, and `useState` through the generated setup context.

### 6. Server output

Resux emits server component modules and a route manifest. The server runtime executes setup, renders HTML, adds binding markers, and serializes JSON-compatible scope data into the Resux payload.

### 7. Browser resume

The browser does not run a whole-app Vue hydration pass. Resux installs delegated event handling, imports the generated component handler when needed, reconstructs the relevant scope, runs the handler, and applies only the resulting binding patches.

### 8. Vue islands

Files under `islands/vue` are different. They are compiled by the normal Vue Vite plugin and mounted with `createApp`. Their state and lifecycle belong to Vue.

```vue
<!-- A normal Resux page -->
<template>
  <VueIsland
    name="ChartWidget"
    :props="{ series }"
  />
</template>
```

Only the island container pays the Vue runtime cost. The surrounding page stays server-rendered and resumable.

## Resux reactivity versus Vue reactivity

Normal Resux components use the reactivity implementation exported by `resuxjs` and `resuxjs/reactivity`. Its API is intentionally familiar—`ref`, `reactive`, `computed`, `watch`, and related helpers—but those values are owned and serialized by the Resux runtime.

Inside a Vue island, import reactivity from `vue` because that component is managed by Vue:

```vue
<script setup lang="ts">
import { ref } from 'vue'

const open = ref(false)
</script>
```

Do not pass live refs, functions, DOM nodes, or class instances across the island boundary. Pass JSON-compatible props.

## Official shortcuts and migration compatibility

For normal Resux components:

- `@event` is the official shortcut for `rx-on:event`.
- `:binding` is the official shortcut for `rx-bind:binding`.
- The full and shortcut forms are equally supported and emit the same Resux model.
- Existing `v-*` syntax remains available for gradual migration.

Only `v-*` should be considered compatibility syntax. The event and binding shortcuts are part of the recommended Resux authoring experience.

There is currently no removal date for `v-*` compatibility syntax.

## Practical rule

Use a normal Resux component first. Choose a Vue island only when the widget truly needs the Vue runtime, a Vue-only library, or lifecycle behavior outside the documented Resux compiler subset.
