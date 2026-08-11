# Images

`<ResuxImg>` is Resux's first-party image template primitive. It produces a native `<img>` while integrating Resux URL transformation, responsive candidates, SSR preloads, deferred lazy loading, placeholders, and fallback metadata.

## Basic usage

```vue
<ResuxImg
  src="/images/product.jpg"
  alt="Black mechanical keyboard"
  width="800"
  height="600"
/>
```

Always treat `alt` as content, not decoration metadata. Use a meaningful description when the image conveys information, and an empty string when the image is purely decorative and surrounding content already carries the meaning.

## Local, public, and remote sources

The source can be a project-served path or an HTTP(S) URL accepted by the configured provider/server path:

```vue
<ResuxImg src="/images/local.jpg" alt="Local image" />
<ResuxImg src="https://cdn.example.com/photo.jpg" alt="Remote photo" />
```

Remote transformation/proxying causes the server to fetch a URL on behalf of the client; see [Remote media security](./optimization.md#remote-source-security).

## Dimensions and aspect ratio

```vue
<ResuxImg
  src="/images/hero.jpg"
  alt="Dashboard"
  width="1200"
  height="675"
/>
```

When both dimensions are known, Resux also derives an inline `aspect-ratio` style unless your own style/placeholder style already declares one. This helps reserve layout space and reduce cumulative layout shift.

## Loading defaults

The renderer resolves loading from `priority`, `loading`, and `lazy`:

- `priority` defaults to `false`.
- Without an explicit `loading`/`lazy` override, a non-priority image resolves to lazy loading.
- A priority image resolves to eager loading and defaults fetch priority to `high`.
- Explicit `loading="lazy"` or `lazy` enables Resux's deferred-lazy data-attribute path.

```vue
<ResuxImg src="/images/card.jpg" alt="Card preview" loading="lazy" />
```

## Priority / LCP image

For the likely Largest Contentful Paint image:

```vue
<ResuxImg
  src="/images/hero.jpg"
  alt="Product dashboard"
  width="1440"
  height="810"
  priority
  preload
  fetchpriority="high"
  loading="eager"
  decoding="async"
/>
```

`priority` makes preload default to true unless `preload` is set separately. During server rendering, Resux registers an image preload and includes `imagesrcset`/`imagesizes` when available.

Do not mark every image priority; competing high-priority/preload requests can make the real LCP resource slower.

## Decoding

`decoding` defaults to `async`:

```vue
<ResuxImg src="/images/photo.jpg" alt="Photo" decoding="async" />
```

You may forward another browser-supported value when there is a measured reason to do so.

## Placeholder

The implementation accepts placeholder modes/sources. Examples include built-in generated data-URI modes:

```vue
<ResuxImg src="/images/hero.jpg" alt="Hero" placeholder="blur" />
<ResuxImg src="/images/hero.jpg" alt="Hero" placeholder="skeleton" />
<ResuxImg src="/images/hero.jpg" alt="Hero" placeholder="spinner" />
```

`placeholder="true"`/boolean true uses the default placeholder. A media URL/data URI can also be used as the placeholder source. Placeholder class/style hooks are available through `placeholder-class` and `placeholder-style`.

Resux marks placeholder state with media data attributes so the client enhancement can remove/transition the placeholder as the real image loads.

## Fallback source

`fallback-src` (and the `fallback` alias read by the renderer) supplies fallback metadata/source behavior:

```vue
<ResuxImg
  src="/images/preferred.webp"
  fallback-src="/images/fallback.jpg"
  alt="Product"
/>
```

The fallback is not a promise that every network/format failure can be detected server-side; test the actual client error behavior required by your application.

## Core image props

The Resux template renderer recognizes the following image-oriented inputs:

| Prop | Purpose |
| --- | --- |
| `src` | Original source URL/path. |
| `alt` | Native alternative text; defaults to empty string in render input. |
| `width` / `height` | Intrinsic dimensions and transform candidates. Positive numeric values are normalized. |
| `sizes` | Native responsive sizes string; also used to derive width candidates. |
| `widths` | Explicit responsive width candidate list. |
| `densities` | Pixel-density candidate list; config default can supply it, otherwise `[1, 2]`. |
| `loading` | Native loading mode and deferred-lazy decision. |
| `lazy` | Boolean lazy override. |
| `root-margin` | Intersection margin used by deferred lazy image enhancement; default `0px 0px`. |
| `threshold` | Lazy IntersectionObserver threshold clamped to `0..1`; default `0`. |
| `decoding` | Native decoding; default `async`. |
| `fetchpriority` / `fetchPriority` | Native fetch priority; priority images default to `high`. |
| `priority` | Convenience signal for eager/high-priority/preload defaults. |
| `preload` | Whether SSR registers an image preload. |
| `provider` | Image provider name. |
| `cache` | Transformation cache policy. |
| `quality` | Transform quality. |
| `fit` | Transform fit mode. |
| `format` | Requested output format. |
| `formats` | Multiple output formats, primarily useful with picture generation. |
| `modifiers` | Additional provider/transformation modifiers. |
| `placeholder` | Placeholder mode, text, URL, data URI, or boolean. |
| `placeholder-class` | Class merged onto placeholder state. |
| `placeholder-style` | Inline placeholder style. |
| `fallback-src` / `fallback` | Fallback source. |

Non-reserved attributes are forwarded to the output image, with normalizations for names such as `className`, `referrerPolicy`, and `crossOrigin`.

## Responsive output

See [Responsive Images](./responsive-images.md) for the exact `widths`, `sizes`, density, and `<picture>` rules.

## Styling

`ResuxImg` is not a `resuxjs/ui` component and has no `unstyled` prop. Style the native image normally:

```vue
<ResuxImg class="hero-image" src="/images/hero.jpg" alt="Hero" />
```

## Accessibility

- Always make an explicit `alt` decision.
- Provide width/height where practical to reduce layout movement.
- Do not put important text only inside an image.
- Placeholder SVGs are loading presentation; the final image's `alt` remains the semantic source.
- If an image is a link/control, the surrounding interactive element needs a useful accessible name.

## SSR / resumability / client behavior

The final/initial native `<img>` is generated by the Resux renderer. Normal eager/native behavior works from server HTML. Deferred lazy mode stores the eventual source/srcset/sizes in `data-rx-lazy-*` / `data-*` attributes and uses a tiny initial placeholder source until Resux client media enhancement activates it.

This does not require wrapping the image in a Vue island.

## Related

- [Responsive Images](./responsive-images.md)
- [Image Optimization](./optimization.md)
- [Video](./video.md)
- [Avatar](/components/avatar)
