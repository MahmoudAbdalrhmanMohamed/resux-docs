# Media and Optimization

Resux has first-party resumable/SSR-first image and video primitives. The deep media documentation now lives in a dedicated section:

- [Images and Media overview](/media/)
- [`ResuxImg`](/media/images)
- [Responsive images and `ResuxPicture`](/media/responsive-images)
- [`useResuxImage()`, providers, transforms, caching and security](/media/optimization)
- [`ResuxVideo`, loading, controls, captions and FFmpeg transforms](/media/video)

This guide URL is kept as a stable entry point for existing links.

## Runtime model

`ResuxImg`, `ResuxPicture`, and `ResuxVideo` are handled by the **Resux template renderer**. They are not `resuxjs/ui` Vue components. Resux can therefore emit meaningful native media HTML during SSR and progressively enhance deferred loading/custom controls without requiring a Vue island around the whole media element.

```vue
<ResuxImg
  src="/images/hero.jpg"
  alt="Product dashboard"
  width="1200"
  height="675"
  sizes="100vw"
  priority
/>
```

Read [Images](/media/images) for placeholders/lazy behavior and [Image Optimization](/media/optimization) for the `/__resux/image` transformation path.
