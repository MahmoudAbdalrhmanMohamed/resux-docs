# Template Syntax

Resux templates look familiar, but they are compiled into a resumable DOM model. This page lists the current stable compiler subset.

## Text and interpolation

```vue
<template>
  <h1>Hello {{ name }}</h1>
</template>
```

Refs from `useState`, `useAsyncData`, `useFetch`, Vue `ref`, and `computed` are auto-unwrapped in templates. In script, keep using `.value`.

## Static attributes

```vue
<template>
  <section class="card" id="hero">
    Content
  </section>
</template>
```

## Dynamic attributes

```vue
<template>
  <button :disabled="pending" :aria-label="label">
    Submit
  </button>
</template>
```

Dynamic attributes are patched when the resumed scope changes.

## Class and style bindings

Dynamic class arrays/objects and style objects are supported:

```vue
<template>
  <div :class="['card', { active, muted: pending }]" :style="{ opacity: pending ? 0.6 : 1 }">
    Status
  </div>
</template>
```

## Events

Named handlers:

```vue
<button @click="increment">Add</button>
```

Inline expressions:

```vue
<button @click="count.value++">Add</button>
```

Supported modifier groups include:

- Control modifiers: `.prevent`, `.stop`, `.self`, `.once`.
- Accepted but delegated modifiers: `.capture`, `.passive`.
- System modifiers: `.ctrl`, `.shift`, `.alt`, `.meta`, `.exact`.
- Mouse modifiers: `.left`, `.middle`, `.right`.
- Key filters: `.enter`, `.tab`, `.delete`, `.esc`, `.escape`, `.space`, `.up`, `.down`, `.left`, `.right`.

```vue
<form @submit.prevent="save">
  <button>Save</button>
</form>
```

::: warning Delegated runtime
Even when `.capture` or `.passive` is accepted by the compiler, the browser runtime still uses delegated resumable listeners.
:::

## Conditional rendering

```vue
<p v-if="error">{{ error.message }}</p>
<p v-if="!error">Ready</p>
```

`v-show` maps to a dynamic hidden state:

```vue
<p v-show="open">Visible when open</p>
```

## Text and HTML directives

```vue
<p v-text="message" />
<div v-html="safeHtml" />
```

`v-html` output is sanitized by Resux before rendering.

## Form model

Basic `v-model` is supported for assignable expressions.

```vue
<script setup lang="ts">
const message = useState('message', () => '')
const accepted = useState('accepted', () => false)
</script>

<template>
  <input v-model="message" />
  <input type="checkbox" v-model="accepted" />
</template>
```

The compiler expects an assignable expression, such as `message`, `message.value`, `form.name`, or `form['name']`.

## Lists

```vue
<ul>
  <li v-for="item in items" :key="item.id">
    {{ item.title }}
  </li>
</ul>
```

Index variables are supported:

```vue
<li v-for="(item, index) in items">
  {{ index }} - {{ item.title }}
</li>
```

## Built-in tags

| Tag | Purpose |
| --- | --- |
| `<ResuxPage />` | Renders the active page inside `app.vue`. |
| `<ResuxLayout />` | Renders the selected layout. |
| `<slot />` | Renders layout slot content. |
| `<ResuxLink to="/path">` | Renders as `<a href="/path">` and is intercepted for client navigation. |
| `<VueIsland />` | Mounts a Vue runtime island. |

## Unsupported syntax

Unsupported Vue directives and patterns should fail at compile time. Resux does this intentionally so the app does not silently switch to full hydration.
