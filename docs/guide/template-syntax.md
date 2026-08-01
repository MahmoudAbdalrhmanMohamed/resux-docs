# Template Syntax

Resux parses templates with Vue compiler packages and emits its own resumable template model. Only the documented subset should be considered supported.

## Text and interpolation

```vue
<template>
  <h1>Hello {{ user.name }}</h1>
</template>
```

Refs are auto-unwrapped in template expressions. Script code still uses `.value`.

## Attributes

```vue
<button
  id="save"
  :disabled="pending"
  :aria-label="label"
  :class="['button', { active, loading: pending }]"
  :style="{ opacity: pending ? 0.5 : 1 }"
>
  Save
</button>
```

Dynamic bindings become patch targets.

## Events

```vue
<button @click="increment">Add</button>
<button @click="count.value = 0">Reset</button>
<form @submit.prevent="save">...</form>
<input @keydown.enter.exact="search" />
```

Supported modifier groups include:

- control: `prevent`, `stop`, `self`, `once`
- delegated syntax: `capture`, `passive`
- system: `ctrl`, `shift`, `alt`, `meta`, `exact`
- mouse: `left`, `middle`, `right`
- key filters: `enter`, `tab`, `delete`, `esc`, `escape`, `space`, `up`, `down`, `left`, `right`

The browser runtime remains delegated even when capture/passive syntax is accepted.

## Conditional chains

```vue
<p v-if="status === 'loading'">Loading</p>
<p v-else-if="status === 'error'">Failed</p>
<p v-else>Ready</p>
```

Adjacent `v-if`, `v-else-if`, and `v-else` branches are compiled as one conditional block.

## `v-show`

```vue
<section v-show="open">Panel</section>
```

Resux patches visibility without removing the element.

## Lists

```vue
<li v-for="(item, index) in items" :key="item.id">
  {{ index }} — {{ item.title }}
</li>
```

List locals are tracked so expressions and inline handlers can reference the item and index.

## Text and HTML

```vue
<p v-text="message" />
<div v-html="trustedHtml" />
```

Only use `v-html` with content you trust or sanitize. Do not rely on framework rendering as a substitute for application-specific HTML sanitization policy.

## Form model

```vue
<input v-model="form.name" />
<input type="checkbox" v-model="accepted" />
```

The model expression must be assignable, such as a ref, member expression, or indexed member expression.

## Template refs

Template ref bindings can be declared in setup and referenced from supported client work. Treat actual elements as browser-only values; do not put DOM nodes into resumable state.

## Built-in application tags

- `<ResuxPage />`
- `<ResuxLayout />`
- `<ResuxLink />`
- `<ResuxImg />`
- `<ResuxPicture />`
- `<ResuxVideo />`
- `<VueIsland />`
- `<slot />`

## Styles

```vue
<style scoped>
.card { padding: 1rem; }
</style>
```

Supported:

- plain CSS
- multiple style blocks
- scoped styles

Not supported for normal resumable components:

- `<style module>`
- `<style src>`
- preprocessors through `lang` such as Sass/Less

Use global CSS, Tailwind, modules that add CSS, or Vue islands when a different style pipeline is required.

## Unsupported directives

Unknown directives and unsupported SFC behavior should fail at compile time. This is intentional: Resux does not silently fall back to whole-component hydration.
