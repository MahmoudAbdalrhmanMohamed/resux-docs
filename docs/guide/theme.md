# Dark and Light Theme (`resuxjs/theme`)

`resuxjs/theme` adds dark and light mode with no flash on page load. It is opt-in: nothing is added to your app until you list the module.

It is a module, not part of the client bootstrap. The bootstrap stays the same size, and an app that does not list the module pays nothing.

## Enable it

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/theme', {
      colors: {
        light: { bg: '#f6f7f9', fg: '#1b1f23' },
        dark: { bg: '#0f1419', fg: '#e8ecef' }
      },
      themeColor: { light: '#f6f7f9', dark: '#0f1419' }
    }]
  ]
})
```

Use the variables in any CSS:

```css
body {
  background: var(--bg);
  color: var(--fg);
}
```

## What the module adds to every page

- One small inline `<script>` in `<head>` that sets the mode before the first paint. A reload does not flash the wrong mode.
- One inline `<style>` with your color variables: light values on `:root`, dark values on the dark selector.
- Optional `<meta name="theme-color">` tags, one per mode, each with a `prefers-color-scheme` media query so system mode works without JavaScript.

## Options

| Option | Default | Meaning |
| --- | --- | --- |
| `defaultTheme` | `"system"` | Preference used until the visitor chooses: `"light"`, `"dark"` or `"system"`. |
| `fallback` | `"light"` | Mode used when the preference is `"system"` and the browser reports none. |
| `storageKey` | `"resux-theme"` | `localStorage` key that holds the visitor's choice. |
| `attribute` | `"class"` | How the mode appears on `<html>`: `"class"` or `"data-theme"`. |
| `colors` | none | CSS variables per mode: `{ light: {...}, dark: {...} }`. Keys without a leading `--` get one. |
| `themeColor` | none | Browser UI color per mode: `{ light: '#fff', dark: '#000' }`. |
| `colorScheme` | `true` | Set the CSS `color-scheme` property on `<html>` to the active mode. |
| `disableTransition` | `false` | Turn off CSS transitions for one frame while the mode switches. |

Variable values are checked. A value containing `;`, `{`, `}`, `<`, `>` or a CSS comment marker is ignored, because it is written into an inline `<style>`.

## How the mode is exposed

- `attribute: "class"` toggles `dark` and `light` classes on `<html>`.
- `attribute: "data-theme"` sets `data-theme="light"` or `data-theme="dark"` on `<html>`.

The visitor's choice is stored in `localStorage` as `"light"`, `"dark"` or `"system"`. If storage is blocked, the choice still works for the current page session but is not remembered. The mode also follows system changes while the preference is `"system"`, and changes made in another tab.

## Toggle button

Import `useTheme` from the module. It is an explicit import, like `googleFont` from `resuxjs/fonts`.

```vue
<script setup lang="ts">
import { useTheme } from 'resuxjs/theme'

const label = ref('')

function toggle() {
  const theme = useTheme()
  theme.toggle()
  label.value = theme.resolved
}
</script>

<template>
  <button @click="toggle">Theme: {{ label }}</button>
</template>
```

`useTheme()` returns:

| Member | Meaning |
| --- | --- |
| `preference` | What the visitor chose: `"light"`, `"dark"` or `"system"`. |
| `resolved` | The mode applied right now. |
| `forced` | The mode forced by the current page, or `null`. |
| `set(preference)` | Choose `"light"`, `"dark"` or `"system"`. |
| `toggle()` | Switch between light and dark. Does nothing on a forced page. |
| `subscribe(listener)` | Call `listener` after every change. Returns an unsubscribe function. |

`preference`, `resolved` and `forced` are plain getters, not reactive values. To show the mode in a template, copy it into a `ref` in the handler as above, or use `subscribe`.

On the server `useTheme()` returns fixed values (`"system"`, `"light"`, not forced). Do not render its state into the server HTML.

## Force a mode on one page

```vue
<script setup lang="ts">
import { forceTheme } from 'resuxjs/theme'

useHead(forceTheme('light'))
</script>
```

The page is shown in that mode on first load and after client navigation. Navigating away restores the visitor's mode. The saved choice is not changed. When a mode is forced, the matching `theme-color` meta is the one in effect.

## Tailwind CSS

Make Tailwind's `dark:` variant follow the class on `<html>`.

Tailwind v3 (3.4.1 and later):

```js
// tailwind.config.js
export default {
  darkMode: 'selector'
}
```

Tailwind v4:

```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```

If you use `attribute: "data-theme"`, match that selector instead:

```css
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

## Static deploys

The script and styles are part of the rendered HTML, so the static target needs no server for the theme to work.

## Content Security Policy

The script and the style are inline. They receive the request nonce when the page has one. A policy that does not allow inline scripts and styles also blocks Resux's own inline payload, so use a policy that allows inline for now:

```ts
['resux:security', {
  contentSecurityPolicy: "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
}]
```
