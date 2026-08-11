# Images and Media

Resux includes first-party image and video rendering in the core template runtime. Unlike `resuxjs/ui` and `resuxjs/icons`, the media elements are **Resux template primitives**, not Vue components.

That distinction matters: Resux can emit useful image/video HTML during SSR and progressively enhance loading/controls without making an entire media subtree a Vue island.

## What is built in

| API | Purpose |
| --- | --- |
| [`<ResuxImg>`](./images.md) | Optimized/responsive image output with lazy/priority/placeholder behavior |
| [`<ResuxPicture>`](./responsive-images.md) | Multiple formats, art direction, generated `<source>` elements |
| [`useResuxImage()`](./optimization.md#useresuximage) | Build transformed image URLs directly |
| [`<ResuxVideo>`](./video.md) | Video sources, posters, loading strategies, native/custom controls and optional transforms |
| `/__resux/image` | Built-in image transformation/proxy endpoint used by the default provider |
| `/__resux/video` | Built-in video path used by Resux video transformation behavior |

Compatibility aliases for image rendering also exist in the template renderer for `NuxtImg`, `NuxtImage`, and `NuxtPicture`, but Resux documentation uses the Resux names so the runtime boundary is explicit.

## Start with the native performance model

For images:

```vue
<ResuxImg
  src="/images/hero.jpg"
  alt="Resux dashboard"
  width="1200"
  height="675"
  sizes="(max-width: 768px) 100vw, 1200px"
  format="webp"
  quality="82"
/>
```

For video:

```vue
<ResuxVideo
  src="/media/intro.webm"
  poster="/media/intro-poster.webp"
  controls-mode="native"
  preload="metadata"
/>
```

## SSR and resumability

Media rendering is designed to start from server HTML:

- `ResuxImg` produces a native `<img>` with transformed `src`, responsive metadata, dimensions, loading/decoding attributes, and Resux media data attributes.
- `ResuxPicture` emits a native `<picture>` containing manual and/or generated `<source>` elements plus the fallback image.
- `ResuxVideo` emits native video markup and can add Resux progressive enhancement data/controls according to its options.
- Priority image preloads are registered into head output instead of waiting for a Vue mount hook.
- Deferred lazy images keep the eventual URL/srcset in data attributes and begin with a tiny placeholder source until the client media enhancement activates them.

This is different from putting media inside a Vue-only component just to gain basic loading behavior.

## Configuration

Image configuration lives under `image`:

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

The default Resux provider builds URLs against `/__resux/image`; the special provider name `vercel` defaults to `/_vercel/image`. Provider entries can override the base URL and merge default modifiers.

## Choose the right page

- Learn all `ResuxImg` props and loading/placeholder behavior in [Images](./images.md).
- Learn `sizes`, width candidates, density candidates, formats, and `<picture>` in [Responsive Images](./responsive-images.md).
- Learn providers, transformation URL generation, caching, Sharp, remote-source security, and LCP guidance in [Image Optimization](./optimization.md).
- Learn sources, captions, autoplay, controls, loading, FFmpeg transforms, and accessibility in [Video](./video.md).

## Related

- [Performance guidance](/guide/security-caching)
- [Integration Cookbook](/guide/integration-cookbook)
- [Execution Contexts](/guide/execution-contexts)
- [Avatar UI component](/components/avatar)
