# Icon Usage and Registry

## Component imports and availability

In Resux, `<Icon>` (with alias `<ResuxIcon>`) is automatically available in your templates when `resuxjs/icons` is enabled. You can also import it explicitly:

```ts
import { Icon, ResuxIcon } from 'resuxjs/icons'
```

## Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `string` | *(required)* | Icon identifier. Accepts collection prefix (`'lucide:mail'`), built-in alias (`'mail'`), custom alias (`'github'`), or local SVG (`'custom:logo'`). |
| `size` | `string \| number` | `'1em'` | Icon dimensions (width and height). Numeric values are converted to px. |
| `mode` | `'svg' \| 'css'` | `'svg'` | Rendering mode. `'svg'` produces an inline SVG; `'css'` produces an ultra-lightweight `<span>` with CSS `mask`. |
| `ssr` | `boolean` | `true` | When `false`, defers icon rendering until client mount. |
| `lazy` | `boolean` | `false` | Defers remote icon fetching until element is near the viewport using `IntersectionObserver`. |
| `loading` | `'eager' \| 'lazy'` | `'eager'` | Alternative shorthand for lazy loading (`loading="lazy"`). |
| `apiProvider` | `string` | `''` | Override the remote Iconify API endpoint for this specific icon. |
| `class` | `string` | `''` | Custom CSS class names applied to the root icon element. |

## Sizing and Colors

### Sizing

Icons default to `1em`, allowing them to match the font size of surrounding text:

```vue
<!-- Matches font size -->
<p class="text-xl">
  <Icon name="lucide:sparkles" /> Featured Item
</p>

<!-- Explicit size override -->
<Icon name="lucide:check" size="24" />
<Icon name="lucide:check" size="2rem" />
```

### Color inheritance

Icons render with `fill="currentColor"` (in SVG mode) or `background-color: currentColor` (in CSS mode), so they automatically inherit the parent text color:

```vue
<button class="text-blue-600 hover:text-blue-800">
  <Icon name="lucide:download" /> Download Report
</button>
```

## Compile-Time Inlining

Resux features a Vite transform plugin (`createIconsVitePlugin`) that inspects your templates at build time. When it encounters statically named icons that exist in offline collections, custom SVGs, or built-in registries:

```vue
<!-- Source template -->
<Icon name="lucide:check" size="1.5rem" class="text-green-500" />
```

The compiler replaces the `<Icon>` component directly with the inlined `<svg>` markup:

```html
<!-- Compiled output in production -->
<svg xmlns="http://www.w3.org/2000/svg" width="1.5rem" height="1.5rem" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="resux-icon inline-block shrink-0 align-middle text-green-500" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>
```

This delivers **instant rendering during SSR and 0 B client JavaScript overhead**.

## CSS Mode (`mode="css"`)

For monochrome UI icons, CSS mode produces a single `<span>` using CSS `mask-image`:

```vue
<Icon name="lucide:arrow-right" mode="css" size="1.25rem" />
```

Rendered HTML:

```html
<span class="resux-icon resux-icon-css inline-block shrink-0 align-middle" style="width: 1.25rem; height: 1.25rem; display: inline-block; background-color: currentColor; mask-image: url('data:image/svg+xml,...'); mask-size: 100% 100%;" aria-hidden="true"></span>
```

CSS mode is ideal for lists, tables, and data grids where hundreds of icons share the same DOM structure.

## Local SVG Directory (`custom:*`)

Drop any `.svg` file into `./assets/icons/`:

```txt
assets/icons/
  brand/
    mark.svg
  logo.svg
```

Use them in templates with the `custom:` prefix:

```vue
<Icon name="custom:logo" size="32" />
<Icon name="custom:brand/mark" size="24" />
```

Resux cleans the SVG, strips hard-coded fills/strokes if appropriate, normalizes the viewBox, and caches the result for instant rendering.

## Extending the In-Memory Registry

You can also register custom SVGs programmatically via `registerStaticIcon`:

```ts
import { registerStaticIcon } from 'resuxjs/icons'

registerStaticIcon('app:heart', {
  viewBox: '0 0 24 24',
  paths: [
    { d: 'M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z' }
  ]
})
```

## Related

- [Icons overview](./index.md)
- [Configuration](./configuration.md)
- [Runtime Loading and SSR](./runtime.md)
