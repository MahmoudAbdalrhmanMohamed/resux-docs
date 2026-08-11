# Responsive Images

Resux can generate either width-descriptor (`w`) or density-descriptor (`x`) `srcset` output and can generate `<picture>` sources for formats or art direction.

## Explicit width candidates

```vue
<ResuxImg
  src="/images/hero.jpg"
  alt="Dashboard"
  width="1600"
  height="900"
  :widths="[480, 768, 1024, 1440, 1600]"
  sizes="(max-width: 768px) 100vw, 80vw"
/>
```

When explicit `widths` are available, Resux builds URLs for those positive candidates and emits width descriptors. Candidate width is capped by the source/input `width` when one is supplied and by the implementation's 8192px transform bound.

When both base `width` and `height` exist, candidate heights preserve the declared aspect ratio.

## Candidates derived from `sizes`

If `widths` is absent but `sizes` is present, Resux parses positive `px` and `vw` values and derives candidate widths across an internal set of responsive viewport widths, expanded by the requested densities.

```vue
<ResuxImg
  src="/images/feature.jpg"
  alt="Feature"
  width="1400"
  height="875"
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 80vw, 1000px"
/>
```

This is pragmatic candidate generation, not a browser layout parser. Keep `sizes` understandable and test the resulting network choices in real viewports.

## Density srcset

If no width-candidate path is produced and an intrinsic `width` exists, Resux uses densities (configured or defaulting to `[1, 2]`):

```vue
<ResuxImg
  src="/icons/product.png"
  alt="Product"
  width="96"
  height="96"
  :densities="[1, 2, 3]"
/>
```

The generated transforms scale width and height by each density and emit `1x`, `2x`, and `3x` descriptors.

## `ResuxPicture`

`ResuxPicture` emits native `<picture>` markup with a fallback image.

### Multiple formats

```vue
<ResuxPicture
  src="/images/hero.jpg"
  alt="Dashboard"
  width="1200"
  height="675"
  :formats="['avif', 'webp']"
  sizes="100vw"
/>
```

When no explicit `sources` array is supplied, formats are converted into generated `<source>` elements with inferred image MIME types. The fallback image uses the fallback source/current source without forcing the multi-format list.

### Explicit art-direction sources

The renderer accepts a `sources` array of records with fields such as:

- `src`
- `srcset`
- `type`
- `media`
- `sizes`
- `width`
- `height`
- `widths`
- `quality`
- `format`
- `fit`
- `modifiers`

Example:

```vue
<ResuxPicture
  src="/images/hero-mobile.jpg"
  alt="Product dashboard"
  :sources="[
    {
      src: '/images/hero-wide.jpg',
      media: '(min-width: 900px)',
      format: 'avif',
      widths: [900, 1200, 1600]
    },
    {
      src: '/images/hero-mobile.jpg',
      format: 'webp',
      widths: [480, 768]
    }
  ]"
/>
```

The current renderer also preserves manually authored child `<source>` markup in the picture before generated sources, so low-level native composition remains possible.

## Lazy `<picture>` sources

When deferred lazy behavior is active, generated `<source>` entries store eventual values in `data-rx-lazy-srcset` / `data-srcset` (and lazy sizes metadata) instead of immediately attaching `srcset`. The fallback `<img>` follows the same deferred activation model.

## Preload and responsive metadata

For an image preload, Resux can include:

- `as="image"`
- `href`
- `fetchpriority`
- `imagesrcset`
- `imagesizes`
- type information when one explicit output format applies

That lets the browser discover the responsive priority image from head output without waiting for client JavaScript.

## Choosing `sizes`

Use `sizes` to describe the image's **rendered layout width**, not the physical source width. For example:

```vue
<ResuxImg
  src="/images/card.jpg"
  alt="Card"
  width="900"
  height="600"
  sizes="(max-width: 700px) 100vw, 420px"
/>
```

If the image renders around 420 CSS pixels on desktop, `420px` is a better sizes hint than `900px` just because the source is 900px wide.

## LCP guidance

For an above-the-fold hero:

1. declare stable dimensions;
2. give the browser an accurate `sizes` value;
3. generate enough width candidates without generating dozens of near-duplicates;
4. use `priority`/preload for the actual LCP candidate only;
5. avoid a lazy/deferred path for the LCP image;
6. verify the chosen resource in browser network and performance tooling.

## Related

- [Images](./images.md)
- [Image Optimization](./optimization.md)
