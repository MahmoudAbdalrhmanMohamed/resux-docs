# Template Syntax

Resux parses `.vue` templates with Vue compiler packages, then emits its own resumable template model. Public Resux directives use the branded `rx-*` prefix.

::: tip Compatibility
Existing `v-*`, `:prop`, and `@event` syntax remains accepted so projects can migrate gradually. New Resux code should prefer explicit `rx-bind:*` and `rx-on:*` forms.
:::

Read [How Resux Uses Vue](/guide/how-resux-uses-vue) for the complete compiler and runtime boundary.

## Text and interpolation

```vue
<template>
  <h1>Hello {{ user.name }}</h1>
</template>
```

Refs are auto-unwrapped in template expressions. Script code still uses `.value`.

## Static and dynamic attributes

```vue
<button
  id="save"
  rx-bind:disabled="pending"
  rx-bind:aria-label="label"
  rx-bind:class="['button', { active, loading: pending }]"
  rx-bind:style="{ opacity: pending ? 0.5 : 1 }"
>
  Save
</button>
```

Dynamic bindings become patch targets in the Resux runtime.

## Events

```vue
<button rx-on:click="increment">Add</button>
<button rx-on:click="count.value = 0">Reset</button>
<form rx-on:submit.prevent="save">...</form>
<input rx-on:keydown.enter.exact="search" />
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
<p rx-if="status === 'loading'">Loading</p>
<p rx-else-if="status === 'error'">Failed</p>
<p rx-else>Ready</p>
```

Adjacent `rx-if`, `rx-else-if`, and `rx-else` branches are compiled as one conditional chain.

## Visibility

```vue
<section rx-show="open">Panel</section>
```

`rx-show` patches visibility without removing the element.

## Lists

```vue
<li rx-for="(item, index) in items" rx-bind:key="item.id">
  {{ index }} — {{ item.title }}
</li>
```

List locals are tracked so expressions and inline handlers can reference the item and index.

## Text and HTML

```vue
<p rx-text="message" />
<div rx-html="trustedHtml" />
```

Only use `rx-html` with content you trust or sanitize. Framework rendering is not a substitute for application-specific HTML sanitization.

## Form model

```vue
<input rx-model="form.name" />
<input type="checkbox" rx-model="accepted" />
```

The model expression must be assignable, such as a ref, member expression, or indexed member expression.

## Slots

Named and scoped slots use the same branded directive convention:

```vue
<template rx-slot:header="{ title }">
  <h2>{{ title }}</h2>
</template>
```

Only the documented slot subset should be considered stable.

## Directive mapping

| Public Resux syntax | Internal parser spelling |
| --- | --- |
| `rx-if` | `v-if` |
| `rx-else-if` | `v-else-if` |
| `rx-else` | `v-else` |
| `rx-for` | `v-for` |
| `rx-show` | `v-show` |
| `rx-text` | `v-text` |
| `rx-html` | `v-html` |
| `rx-model` | `v-model` |
| `rx-bind:name` | `v-bind:name` |
| `rx-on:event` | `v-on:event` |
| `rx-slot:name` | `v-slot:name` |

The mapping happens only before parsing. The emitted Resux template model does not keep Vue directive objects.

## Template refs

Template ref bindings can be declared in setup and referenced from supported client work. Treat actual elements as browser-only values; never put DOM nodes into resumable state.

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

Supported in normal resumable components:

- plain CSS
- multiple style blocks
- scoped styles

Not supported there:

- `<style module>`
- `<style src>`
- preprocessors through `lang` such as Sass/Less

Use global CSS, Tailwind, modules that add CSS, or a Vue island when a different style pipeline is required.

## Unsupported directives

Unknown directives and unsupported SFC behavior should fail at compile time. Resux does not silently fall back to whole-component hydration.
