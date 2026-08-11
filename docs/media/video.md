# Video

`<ResuxVideo>` is Resux's first-party video template primitive. It can render useful server HTML, native or Resux custom controls, multiple sources/quality metadata, posters, loading strategies, and optional server transformation paths.

## Basic native-controls video

```vue
<ResuxVideo
  src="/media/intro.webm"
  poster="/media/intro-poster.webp"
  controls-mode="native"
  preload="metadata"
/>
```

Use native controls when they satisfy the product requirement. They come with mature browser keyboard, accessibility, fullscreen, volume, seeking, and media-state behavior without recreating all of that UI yourself.

## Multiple sources

The renderer accepts source records with `src`, optional `type`, and optional quality label metadata:

```vue
<ResuxVideo
  :sources="[
    { src: '/media/intro-1080.webm', type: 'video/webm', quality: '1080p' },
    { src: '/media/intro-720.mp4', type: 'video/mp4', quality: '720p' }
  ]"
  poster="/media/intro.webp"
  controls-mode="native"
/>
```

Use explicit MIME `type` values when serving multiple formats so the browser can avoid unnecessary probes.

## Poster

A poster gives SSR/initial paint a useful frame before video data arrives:

```vue
<ResuxVideo
  src="/media/demo.mp4"
  poster="/media/demo-poster.webp"
  preload="metadata"
/>
```

Optimize the poster as carefully as a normal image; on a video-heavy landing page it may become an important paint resource.

## Loading strategies

The existing Resux media API supports these documented strategies:

| Strategy | Behavior |
| --- | --- |
| `eager` | Begin video loading immediately. |
| `lazy` | Prefer deferred/browser-lazy behavior where the media path supports it. |
| `visible` | Begin loading as the media approaches/enters the viewport. |
| `page-ready` | Keep SSR poster/initial structure and delay the video request until page load. |

```vue
<ResuxVideo
  src="/media/background.webm"
  poster="/media/background.webp"
  load-strategy="page-ready"
  muted
  playsinline
/>
```

Choose based on whether the video is immediately useful. A below-the-fold explainer should not compete with the page's LCP image, CSS, fonts, and critical JavaScript.

## Controls modes

The documented control modes are:

```ts
type ResuxVideoControlsMode = 'custom' | 'native' | 'none'
```

### Native

Prefer this for reliability/accessibility unless you need a product-specific control surface.

```vue
<ResuxVideo src="/media/demo.mp4" controls-mode="native" />
```

### Custom

The runtime can render Resux custom controls including play/pause, seek, current/duration time, mute/volume, optional speed/quality controls, fullscreen, and optional interaction/skip zones according to configured props/runtime behavior.

The generated controls use native `<button>`/`<input type="range">` elements with labels such as `Play video`, `Seek video`, `Volume`, and `Toggle fullscreen`.

Custom controls require Resux client media JavaScript to synchronize against the native `<video>` element. Test keyboard interaction, range-input behavior, focus visibility, fullscreen errors, and mobile browser restrictions on your supported browser matrix.

### None

Use only when interaction is intentionally unavailable or provided elsewhere:

```vue
<ResuxVideo
  src="/media/ambient.webm"
  controls-mode="none"
  autoplay
  muted
  loop
  playsinline
/>
```

## Autoplay

Modern browsers generally restrict autoplay with sound. For decorative/ambient autoplay, combine:

```vue
<ResuxVideo autoplay muted loop playsinline controls-mode="none" />
```

Do not make essential information depend on autoplay succeeding. Respect user preferences and avoid unexpected audio.

## Preload

Native `preload` is a hint, not a guaranteed browser command. Common values are `none`, `metadata`, and `auto`. For videos that are not immediately played, `metadata` or `none` often reduces competition for initial bandwidth.

## Captions and subtitles

The safest baseline is native `<track>` content inside the video composition when the template API allows child markup for your case:

```vue
<ResuxVideo src="/media/talk.mp4" controls-mode="native">
  <track
    kind="captions"
    src="/media/talk.en.vtt"
    srclang="en"
    label="English"
    default
  />
</ResuxVideo>
```

Test the generated output for your exact template version. Captions should represent speech and relevant sound; subtitles alone may not be sufficient for deaf/hard-of-hearing users.

## Accessibility

- Prefer native controls for the broadest default semantics.
- Supply captions for spoken/audio content.
- Provide a text alternative/transcript when appropriate.
- Never autoplay audible media unexpectedly.
- Ensure custom control labels remain meaningful as state changes (play vs pause, mute vs unmute).
- Test keyboard-only seeking/volume/fullscreen flows.
- Ensure focus does not disappear when custom controls hide/show.
- Avoid rapid motion/flashing and respect reduced-motion/user preferences in surrounding UI.

## Video transformations

Resux's server video path supports transformed MP4/WebM output and optional target vertical quality/resolution behavior. Transformation requires FFmpeg.

```sh
export RESUX_FFMPEG_PATH=/absolute/path/to/ffmpeg
```

When `RESUX_FFMPEG_PATH` is absent, the runtime can attempt to find `ffmpeg` on `PATH`. If a requested transform needs FFmpeg and no usable binary is available, treat that as a deployment error rather than silently assuming transformation succeeded.

## Remote video security

The same server-proxy concerns as images apply, often with much larger payloads:

- restrict allowed remote origins;
- block private/metadata network targets;
- configure timeouts and maximum sizes;
- avoid user-controlled credential-bearing URLs;
- use CDN/object storage for public delivery;
- do not transcode untrusted arbitrary inputs without resource controls.

## SSR / resumability / client behavior

`ResuxVideo` is handled by the Resux renderer, so initial video/poster/source/control structure can be in SSR output. Loading strategies and custom controls can then be progressively enhanced by Resux's client media runtime. It does not require wrapping the entire player in a Vue island just to use first-party media behavior.

A third-party player library may still require a [client enhancement or Vue island](/guide/integration-cookbook) depending on that library's architecture.

## Related

- [Images](./images.md)
- [Image Optimization](./optimization.md)
- [Integration Cookbook](/guide/integration-cookbook)
- [Security and Caching](/guide/security-caching)
