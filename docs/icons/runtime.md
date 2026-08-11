# Icon Runtime Loading

The icon component resolves local registry data first and uses remote fetching only when needed.

## Resolution flow

For an icon name:

1. Look in `iconRegistry`.
2. If registry data exists, render it.
3. Otherwise resolve the component/runtime API provider.
4. If eager, start remote loading after the Vue component mounts.
5. If lazy and `IntersectionObserver` exists, wait until the icon approaches the viewport.
6. Parse compatible returned SVG/path data into the component's constrained `IconData` representation.
7. Cache successful data and render the resulting paths.
8. On failure, keep/fall back safely rather than injecting arbitrary raw remote markup directly as the component template.

## `fetchIconifyIcon()`

The package exports the remote helper used by the component:

```ts
import { fetchIconifyIcon } from 'resuxjs/icons'

const icon = await fetchIconifyIcon(
  'ph:check-circle',
  'https://api.iconify.design'
)
```

Use the helper only when you actually need programmatic icon resolution. Component use normally handles this flow.

## Cache and request deduplication

The implementation keeps caches keyed by provider + icon name and tracks pending fetches so concurrent requests for the same remote icon/provider can share work rather than issuing identical requests.

Provider identity is part of the key, so the same icon name from two configured providers does not incorrectly share one provider's response.

## Stale-request protection

When component input changes while a request is still in flight, the implementation protects against an older response overwriting a newer name/provider state.

This matters for reactive lists/search results where icon names can change quickly.

## Lazy loading

```vue
<Icon name="ph:image" lazy />
```

or:

```vue
<Icon name="ph:image" loading="lazy" />
```

When lazy and `IntersectionObserver` is available, the component observes its SVG/root region and starts fetching as it approaches the viewport (the implementation uses a positive root margin). Without observer support, it falls back to loading instead of leaving the icon permanently unresolved.

Lazy affects **remote fetching**. A local `iconRegistry` hit already has its path data and does not need a network delay.

## SSR behavior

### Registry icon

A locally registered icon has data available synchronously and can render complete SVG path data through Vue's server-rendering path.

### Remote icon

Remote fetching is a client mount/lazy behavior in the current component. SSR does not make a remote Iconify request to fill an unknown icon before HTML is sent. The server/client output therefore begins from the component's fallback representation until client resolution succeeds.

For important above-the-fold icons, put the required SVG data in `iconRegistry` instead of depending on remote fetch after mount.

## Failure handling

Remote failure should be expected as a normal network condition. Keep critical labels/actions understandable without the icon. For example:

```vue
<button type="button">
  <Icon name="remote:set-name" />
  Continue
</button>
```

The text remains useful if the remote icon cannot load.

## Performance

- Prefer local registry entries for frequently used/critical icons.
- Lazy-load below-the-fold remote icons.
- Avoid rendering hundreds of unique remote icons at once.
- Keep icon names stable so caches can be reused.
- Do not configure a provider that redirects every icon request through a high-latency service without measuring it.
- Use normal CSS/currentColor instead of duplicating color-specific SVG copies.

## Accessibility

Remote vs local loading must not change the accessible meaning of the control. The SVG defaults to decorative `aria-hidden="true"`; accessible labels should be owned by surrounding text/control semantics.

## Related

- [Icons overview](./index.md)
- [Usage and Registry](./usage.md)
- [Configuration](./configuration.md)
- [Vue Islands](/guide/vue-islands)
