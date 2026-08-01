# Media and Optimization

Resux includes resumable image and video components plus server-side transformation routes. The goal is to render useful HTML immediately while delaying expensive media work until it is needed.

## Built-in components

The main media elements are:

- `<ResuxImg>` for responsive images and lazy loading
- `<ResuxPicture>` for art direction and multiple sources
- `<ResuxVideo>` for controlled loading, posters, and optional transformation

These are Resux components, not Vue runtime components.

## Image URL builder

Use `useResuxImage()` to generate a Resux image URL:

```ts
const image = useResuxImage()

const hero = image('/images/hero.jpg', {
  width: 1200,
  height: 675,
  quality: 82,
  format: 'webp',
  fit: 'cover',
  cache: '7d'
})
```

Supported fit values are:

```ts
'cover' | 'contain' | 'fill' | 'inside' | 'outside'
```

Image settings can also be supplied globally:

```ts
export default defineResuxConfig({
  image: {
    provider: 'resux',
    quality: 82,
    format: 'webp',
    cache: '7d',
    densities: [1, 2],
    providers: {
      cdn: {
        baseURL: 'https://cdn.example.com',
        modifiers: { quality: 80 }
      }
    }
  }
})
```

## Image transform behavior

The server image route accepts a local absolute path or an HTTP(S) URL and can apply:

- width from 1 to 8192
- height from 1 to 8192
- quality from 1 to 100
- output format
- fit mode
- additional provider modifiers

Resux uses `sharp` for image transformations. When a transform was requested but `sharp` cannot perform it, the route returns an error instead of pretending the original file satisfies the requested output.

Transformed responses can receive long immutable caching. Original passthrough requests use a shorter cache policy.

## Generated image cache

When persistent image caching is requested, Resux can write generated assets under its generated image area together with metadata describing:

- the transform key
- creation and expiry times
- original source
- generated path
- width, height, quality, format, fit, and extra modifiers
- source file modification details when available

Cache durations accept booleans, seconds, or duration strings such as:

```ts
true
3600
'30m'
'12h'
'7d'
'2w'
```

Do not commit generated image cache files unless your deployment process explicitly treats them as build artifacts.

## `<ResuxImg>`

```vue
<template>
  <ResuxImg
    src="/images/product.jpg"
    alt="Product photograph"
    width="800"
    height="600"
    format="webp"
    quality="82"
    loading="lazy"
  />
</template>
```

Always provide meaningful `alt` text, intrinsic dimensions where possible, and a source that the production server can access.

## `<ResuxPicture>`

Use `<ResuxPicture>` when different viewport conditions need different files or formats:

```vue
<template>
  <ResuxPicture>
    <source media="(min-width: 900px)" srcset="/images/hero-wide.avif" type="image/avif" />
    <source srcset="/images/hero-mobile.webp" type="image/webp" />
    <ResuxImg src="/images/hero-mobile.jpg" alt="Application dashboard" />
  </ResuxPicture>
</template>
```

## `<ResuxVideo>` loading strategies

```vue
<template>
  <ResuxVideo
    src="/media/intro.webm"
    poster="/media/intro-poster.webp"
    load-strategy="page-ready"
    controls-mode="none"
    autoplay
    muted
    loop
    playsinline
  />
</template>
```

Loading strategies:

| Strategy | Behavior |
| --- | --- |
| `eager` | Load immediately |
| `lazy` | Use browser lazy behavior where available |
| `visible` | Begin loading when the element approaches the viewport |
| `page-ready` | Render the poster in SSR and delay the video request until the page load event |

Control modes:

```ts
'custom' | 'native' | 'none'
```

Autoplay normally requires `muted` and `playsinline` on mobile browsers.

## Video transformations

The Resux video route supports MP4 and WebM output and optional target vertical quality. Transform examples include `720` or `720p`.

Video transformation requires `ffmpeg`:

```sh
export RESUX_FFMPEG_PATH=/absolute/path/to/ffmpeg
```

When the variable is not set, Resux attempts to find `ffmpeg` on `PATH`. A requested transform fails visibly when no usable binary is available.

## Remote media security

Media proxying means the server fetches a source on behalf of the browser. Treat provider configuration carefully:

- allow only trusted origins at the application or reverse-proxy layer
- do not expose private-network resources through user-controlled URLs
- apply request-size and timeout controls at infrastructure level
- avoid passing credentials in source URLs
- use a CDN for high-volume public media

## Production checklist

- Install the native `sharp` build supported by the deployment platform.
- Install or provide `ffmpeg` only when video transformation is used.
- Confirm generated media directories are writable when runtime caching is enabled.
- Put immutable transformed media behind a CDN where possible.
- Set `alt`, dimensions, poster files, and loading strategy deliberately.
- Test remote-source restrictions and error behavior before launch.
