# Media Placeholders and Picture

**Lab-backed example:** [`pages/media-test/images.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/pages/media-test/images.vue) · [Open the live page](https://resux-lab.vercel.app/media-test/images)

The media regression page exercises several loading states at once: a priority hero with blur placeholder, lazy skeleton and spinner placeholders, a custom placeholder URL, a responsive `ResuxPicture`, and a missing-image fallback.

## Priority image with a blur placeholder

```vue
<ResuxImg
  src="/media-test/images/hero-wide.jpg"
  alt="Priority wide"
  width="1200"
  height="675"
  priority
  placeholder="blur"
  sizes="(min-width: 1024px) 560px, 100vw"
/>
```

Use `priority` selectively for an image that is genuinely important to the initial viewport. Width and height also give the browser an aspect ratio before the asset finishes loading.

## Lazy image with a skeleton

```vue
<ResuxImg
  src="/media-test/images/hero-square.jpg"
  alt="Lazy square"
  width="900"
  height="900"
  lazy
  placeholder="skeleton"
/>
```

The lab has a parallel spinner case. Choose a placeholder style that communicates loading without becoming visually distracting.

## Custom placeholder source

```vue
<ResuxImg
  src="/media-test/images/transparent-logo.png"
  alt="Custom placeholder"
  width="600"
  height="360"
  lazy
  placeholder="/media-test/images/resux-placeholder.svg"
/>
```

A custom asset is useful when the design system needs a branded or content-specific placeholder.

## Responsive picture with generated formats

```vue
<ResuxPicture
  src="/media-test/images/hero-large.jpg"
  alt="Responsive picture sample"
  widths="480,960,1440"
  formats="avif,webp"
  width="1440"
  height="810"
  lazy
  placeholder="blur"
/>
```

This combines width candidates and modern formats while preserving a fallback image in the generated picture structure.

## Missing-image fallback

```vue
<ResuxImg
  src="/media-test/images/missing-image.jpg"
  fallback-src="/media-test/images/resux-placeholder.jpg"
  alt="Missing image fallback"
  width="900"
  height="560"
  lazy
  placeholder="skeleton"
/>
```

A fallback protects presentation when an asset is unavailable, but it does not remove the need to monitor broken media URLs. Keep meaningful `alt` text appropriate to the final content rather than describing the loading mechanism.

## Related

- [Images](/media/images)
- [Responsive Images](/media/responsive-images)
- [Image Optimization](/media/optimization)
- [Media Optimization example](./media-optimization.md)
