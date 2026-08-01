# Media Optimization Example

## Responsive image

```vue
<ResuxImg
  src="/images/hero.jpg"
  alt="Product preview"
  width="1200"
  height="675"
  sizes="(max-width: 768px) 100vw, 1200px"
  format="webp"
  quality="80"
  cache="7d"
  loading="eager"
  fetchpriority="high"
/>
```

The image builder creates a deterministic generated route for the transform. `sharp` performs resizing/format conversion on the server.

## Art direction

```vue
<ResuxPicture
  :sources="[
    { media: '(max-width: 640px)', src: '/images/hero-mobile.jpg', width: 640 },
    { media: '(min-width: 641px)', src: '/images/hero.jpg', width: 1200 }
  ]"
  src="/images/hero.jpg"
  alt="Product preview"
/>
```

## Deferred video

```vue
<ResuxVideo
  src="/videos/demo.mp4"
  poster="/images/demo-poster.jpg"
  load-strategy="page-ready"
  controls-mode="custom"
  format="webm"
  quality="720"
  cache="7d"
/>
```

Video transforms require `ffmpeg` in `PATH` or `RESUX_FFMPEG_PATH`.

## Operational safeguards

- Keep source media under trusted origins.
- Limit transform dimensions and cache duration.
- Monitor CPU, memory, source size, and request rates.
- Pre-generate popular variants when traffic is high.
- Use CDN/reverse-proxy caching in front of deterministic generated URLs.
