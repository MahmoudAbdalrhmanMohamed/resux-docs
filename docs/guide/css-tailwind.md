# CSS and Tailwind

Resux supports component CSS, global CSS, module-added CSS, and an integrated Tailwind CLI workflow.

## Component styles

```vue
<style scoped>
.card {
  padding: 1rem;
  border-radius: 0.75rem;
}
</style>
```

Normal Resux components support plain CSS and scoped styles. They do not currently support style modules, style `src`, or style preprocessors through `lang`.

## Global CSS

```ts
export default defineResuxConfig({
  css: [
    '/assets/css/main.css',
    '/assets/css/theme.css'
  ]
})
```

Modules can call `addCss` to contribute global styles.

## Tailwind

When the app contains `assets/css/tailwind.css` and a compatible Tailwind CLI dependency, Resux detects the pipeline.

Development starts a watcher. Production creates minified output before the Resux/Vite bundle.

A common input:

```css
@import "tailwindcss";
```

Or use the syntax required by your installed Tailwind version.

## Configuration discovery

Resux uses the available Tailwind CLI and passes a config file when one is detected. Keep Tailwind versions and syntax aligned with the package you install.

## Avoid duplicate pipelines

Do not run a second Tailwind watcher with `concurrently` unless you have intentionally disabled or bypassed the Resux-managed input. Duplicate writers can cause unnecessary rebuilds or file races.

## CSS from packages

Configure package CSS explicitly when automatic discovery is insufficient:

```ts
packages: {
  css: {
    swiper: ['swiper/css', 'swiper/css/navigation']
  }
}
```

## Performance

- Keep global CSS intentional.
- Avoid loading UI package CSS on routes that never use it.
- Prefer immutable caching for built CSS assets.
- Use critical font and media strategies rather than large blocking stylesheets.
