# Image Optimization

Resux's default image provider generates transformation URLs served from `/__resux/image`. The image runtime supports dimensions, quality, format, fit, provider modifiers, optional generated-cache metadata, and responsive URL generation.

## `useResuxImage()`

`useResuxImage()` returns the same style of image URL builder used by the template renderer.

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

### Signature

```ts
function useResuxImage(): ResuxImageBuilder

type ResuxImageBuilder = (
  src: string,
  options?: UseResuxImageOptions
) => string
```

### `UseResuxImageOptions`

| Property | Type | Description |
| --- | --- | --- |
| `provider` | `string` | Provider/config key. |
| `modifiers` | `ResuxImageModifiers` | Additional merged provider modifiers. |
| `width` | `number` | Requested transform width. |
| `height` | `number` | Requested transform height. |
| `quality` | `number` | Requested output quality. |
| `fit` | `ResuxImageFit` | Resize fit. |
| `format` | `string` | Requested output format. |
| `cache` | `ResuxImageCacheInput` | Cache duration/policy input. |

`ResuxImageFit` is:

```ts
type ResuxImageFit =
  | 'cover'
  | 'contain'
  | 'fill'
  | 'inside'
  | 'outside'
```

`ResuxImageModifiers` also allows provider-specific string/number/boolean keys. `format: false` and `quality: false` are recognized as explicit disabling values when modifiers are normalized.

## Global configuration

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
        modifiers: {
          quality: 80
        }
      }
    }
  }
})
```

The resolved modifier order allows provider defaults and global quality/format to be combined with per-call options/modifiers; more specific call values override the broader defaults.

## Provider URL behavior

- Provider `resux` defaults to `/__resux/image`.
- Provider `vercel` defaults to `/_vercel/image`.
- A configured provider can supply `baseURL`.
- Provider base URLs containing a `{src}` token are handled as source templates by the builder.

Do not assume an arbitrary third-party CDN understands Resux query names. A custom base URL/provider must match the transformation contract expected by that service.

## Transformation bounds

The built-in server path validates image transformation inputs. The current documented bounds include:

- width: 1–8192
- height: 1–8192
- quality: 1–100
- fit: `cover | contain | fill | inside | outside`

The implementation uses `sharp` for real image transformations. When a requested transform cannot be performed, Resux should fail rather than silently claim that an untouched original satisfies the requested output.

## Sharp deployment requirement

If your production path uses Resux image transformation, install a Sharp build compatible with the deployment OS/architecture. A development machine's native package result is not proof that a serverless/edge deployment has the same binary support.

Test the production target declared in your Resux deployment configuration.

## Cache input

The cache option accepts:

```ts
type ResuxImageCacheInput =
  | boolean
  | string
  | number
  | {
      maxAge?: number | string
      expiresIn?: number | string
      ttl?: number | string
    }
```

Duration strings used by the current media path include values such as:

```txt
30m
12h
7d
2w
```

Generated image cache metadata can record the transform key, creation/expiry timestamps, source, generated path, modifier settings, and source-file modification details where available.

Generated caches are build/runtime artifacts; do not commit them unless your deployment process explicitly treats them as deployable artifacts.

### Serverless and read-only deployments

Do not design a production image cache around writing into the deployed application directory. Vercel Functions and similar stateless/serverless runtimes may expose application files from a read-only deployment filesystem, so a request-time transform must not depend on creating `public/_resux/generated/**` inside that deployment.

On stateless Node deployments, Resux keeps the generated/hash URL contract but performs the transform through the stateless image endpoint and returns the bytes directly. The requested cache TTL is expressed through browser/shared-cache headers so the CDN can persist the public response without requiring a writable application directory.

On local development or a long-running Node server with a writable project directory, generated-media disk caching can still be used as a local/runtime optimization.

This distinction is intentional:

- **local / persistent Node:** disk cache may reduce repeated transform work;
- **serverless / stateless Node:** transform response + CDN cache, no deployment-directory writes;
- **external image provider/CDN:** follow that provider's cache contract instead of Resux disk-cache behavior.

For Vercel, prefer CDN caching for public transformed responses rather than `/var/task` filesystem writes. A cached transform should remain valid for the TTL requested by `cache`; it should not silently become a one-year browser cache merely because the stateless transform endpoint is used internally.

## Remote-source security

`/__resux/image` can cause server-side network access for remote inputs. This is a security boundary, not just a performance feature.

Production guidance:

- allow only trusted remote origins at the application/reverse-proxy layer;
- block private-network/metadata endpoints from user-controlled URLs;
- enforce request and response size limits;
- enforce timeouts;
- never put credentials in image source URLs;
- apply CDN caching for public high-volume transformed assets;
- validate provider base URLs and CSP/network policies.

The framework's URL builder does not replace infrastructure-level SSRF controls.

## Performance checklist

- Declare width and height.
- Use `sizes` that matches layout.
- Prefer modern formats only when your transform/deployment path supports them.
- Tune quality visually; do not automatically set 100.
- Keep LCP images eager/high priority; lazy-load below-the-fold media.
- Cache immutable transformations for long periods when source versioning makes that safe.
- Avoid transforming the same source into excessive near-identical widths.
- Put public transformed output behind a CDN where appropriate.
- On serverless hosts, prefer CDN response caching over request-time writes to the deployed application filesystem.

## Related

- [Images](./images.md)
- [Responsive Images](./responsive-images.md)
- [Video](./video.md)
- [Security and Caching](/guide/security-caching)
