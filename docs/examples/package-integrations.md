# Package Integrations

**Lab-backed examples:** [`pages/package-tests/`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/tree/main/pages/package-tests) · [Open the live package matrix](https://resux-lab.vercel.app/package-tests)

Resux Lab contains a compatibility matrix for packages that belong in different execution modes. The important lesson is not a particular library name; it is choosing whether a dependency can run during SSR or should progressively enhance already-useful server HTML.

## Compatibility patterns exercised by the lab

| Pattern | Lab examples | Goal |
| --- | --- | --- |
| SSR-safe import | `date-fns`, `lodash-es` | Produce useful server HTML with no client package boot required |
| Visible enhancement | Swiper, Chart.js, ECharts, video, highlight.js | Keep fallback HTML visible, enhance when the UI reaches the viewport |
| Idle enhancement | GSAP, Anime.js | Delay non-critical visual polish |
| Interaction enhancement | Missing-package diagnostic | Load only after pointer/focus/interaction |
| Immediate enhancement | Trigger fixture | Run after the browser runtime scan |
| Page-load enhancement | Trigger fixture | Wait for the full `window.load` event |
| Manual enhancement | Trigger fixture | Let application code activate explicitly |
| Client-only boundary | Map fixture | Preserve an SSR textual fallback while a browser-only widget initializes |

## Progressive content with `ClientEnhance`

```vue
<ClientEnhance
  name="swiper-carousel"
  trigger="visible"
  demo="swiper"
  :options="{ navigation: true, pagination: true }"
>
  <!-- Useful SSR HTML stays visible first. -->
</ClientEnhance>
```

Use this shape when server-rendered content is meaningful by itself and the package adds richer behavior afterward.

## Non-critical polish can wait for idle time

```vue
<ClientEnhance
  name="animation-demo"
  trigger="idle"
  demo="animation"
>
  <article>Readable before animation JavaScript arrives.</article>
</ClientEnhance>
```

The lab applies this pattern to GSAP and Anime.js so motion does not become a prerequisite for readable content.

## SSR-safe utilities should stay simple

```ts
import { format } from 'date-fns'

const publishedAt = format(new Date('2026-05-26'), 'PPP')
```

When a package has no browser-only assumptions and its output is useful during SSR, a normal server-safe import can be the best option.

## Manual activation

```ts
const controller = await useClientEnhancement('manual-demo', {
  target: '#manual-enhancement-target',
  trigger: 'manual'
})

await controller.activate()
```

Manual mode is appropriate when a domain event—not visibility, idle time or page load—should decide when the package starts.

## Keep fallback content meaningful

The lab deliberately preserves SSR content for charts, maps, markdown, code highlighting, video and carousels. If package loading fails, users and crawlers should still receive useful information wherever practical.

## Related

- [Third-party Packages](/guide/package-integration)
- [Integration Cookbook](/guide/integration-cookbook)
- [Execution Contexts](/guide/execution-contexts)
- [Progressive Package example](./progressive-package.md)
