# UI Package Reference (`resuxjs/ui`)

`resuxjs/ui` is an optional Vue UI and motion package. This page documents the package-level public API. Every component has a dedicated page in the [UI component catalog](/components/).

::: warning Runtime boundary
All `Rx*` / `Resux*` components in this package are Vue `defineComponent` components. Use them inside a [Vue island](/guide/vue-islands) or another explicit Vue runtime boundary. They are not zero-hydration Resux template primitives.
:::

## Import surface

```ts
import uiModule, {
  defineUiTokens,
  isReducedMotion,
  useAnimate,
  vAnime,
  vAnimate,
  RxButton,
  ResuxButton
} from 'resuxjs/ui'
```

## Module options

```ts
export interface ResuxUiModuleOptions {
  css?: string[]
  tokens?: Record<string, string>
  defaultStyles?: boolean
  animations?: {
    enabled?: boolean
    defaultPreset?: string
  }
}
```

| Option | Default | Behavior |
| --- | --- | --- |
| `css` | `[]` | Calls the module CSS registration hook for each configured path. |
| `tokens` | `{}` | Stored in public runtime UI configuration. Arbitrary token keys are **not** automatically converted into built-in component CSS variables. |
| `defaultStyles` | `true` | Injects the built-in `rx-*` primitive stylesheet when enabled. |
| `animations.enabled` | `true` | Controls injection of the package's animation CSS definitions. |
| `animations.defaultPreset` | `'fade-up'` | Exposed as runtime animation configuration. |

Example:

```ts
export default defineResuxConfig({
  modules: [
    ['resuxjs/ui', {
      css: ['/assets/css/ui-overrides.css'],
      defaultStyles: true,
      tokens: {
        accent: '#03c8bf'
      },
      animations: {
        enabled: true,
        defaultPreset: 'fade-up'
      }
    }]
  ]
})
```

## `defineUiTokens(tokens)`

Typed identity helper for token records:

```ts
export function defineUiTokens<T extends Record<string, string>>(tokens: T): T
```

```ts
const tokens = defineUiTokens({
  accent: '#03c8bf',
  surface: '#0f172a'
})
```

The helper returns the same object. It does not generate CSS by itself.

## `AnimationPreset`

```ts
type AnimationPreset =
  | 'fade-up'
  | 'fade-down'
  | 'scale-in'
  | 'slide-in-left'
  | 'slide-in-right'
  | 'pulse-glow'
  | 'bounce-in'
```

These names have verified keyframes in `useAnimate()`.

## `AnimateOptions`

```ts
export interface AnimateOptions {
  type?: AnimationPreset
  duration?: number
  delay?: number
  easing?: string
  fill?: FillMode
}
```

Defaults used by `useAnimate()`:

- `type: 'fade-up'`
- `duration: 400`
- `delay: 0`
- `easing: 'cubic-bezier(0.16, 1, 0.3, 1)'`
- `fill: 'both'`

## `isReducedMotion()`

```ts
export function isReducedMotion(): boolean
```

Returns `false` outside a browser. In a browser it checks:

```txt
(prefers-reduced-motion: reduce)
```

Use this for browser-owned motion that should respect the user's reduced-motion preference.

## `useAnimate(element, options)`

```ts
export function useAnimate(
  target: HTMLElement | Element | null,
  options?: AnimateOptions
): Animation | null
```

The helper returns `null` when:

- there is no browser `window`;
- `target` is null;
- reduced motion is requested;
- the target does not expose `Element.animate`.

Otherwise it invokes the Web Animations API and returns the resulting `Animation`.

```ts
const animation = useAnimate(element, {
  type: 'fade-up',
  duration: 500,
  delay: 100,
  easing: 'ease-out',
  fill: 'forwards'
})
```

The caller owns cancellation/lifecycle when using the imperative helper directly.

## `vAnime` / `vAnimate`

`vAnimate` is an alias of `vAnime`.

The Vue directive:

- reads either a preset string or options object;
- uses `IntersectionObserver` when available;
- starts animation as the element approaches/enters the viewport;
- disconnects its observer after activation;
- cancels an active animation and disconnects the observer during unmount cleanup;
- falls back to immediate animation when `IntersectionObserver` is unavailable.

Example in Vue-owned markup:

```vue
<div v-anime="{ type: 'fade-up', duration: 500 }">
  Content
</div>
```

The directive is a Vue directive; do not present it as a native Resux template directive.

## Public components

Every `Rx*` component has an equivalent `Resux*` alias.

| Component | Dedicated reference |
| --- | --- |
| `RxButton` / `ResuxButton` | [Button](/components/button) |
| `RxInput` / `ResuxInput` | [Input](/components/input) |
| `RxTextarea` / `ResuxTextarea` | [Textarea](/components/textarea) |
| `RxSelect` / `ResuxSelect` | [Select](/components/select) |
| `RxDatePicker` / `ResuxDatePicker` | [DatePicker](/components/date-picker) |
| `RxSwitch` / `ResuxSwitch` | [Switch](/components/switch) |
| `RxCard` / `ResuxCard` | [Card](/components/card) |
| `RxBadge` / `ResuxBadge` | [Badge](/components/badge) |
| `RxAvatar` / `ResuxAvatar` | [Avatar](/components/avatar) |
| `RxAlert` / `ResuxAlert` | [Alert](/components/alert) |
| `RxSkeleton` / `ResuxSkeleton` | [Skeleton](/components/skeleton) |
| `RxDivider` / `ResuxDivider` | [Divider](/components/divider) |
| `RxKbd` / `ResuxKbd` | [Kbd](/components/kbd) |
| `RxAccordion` / `ResuxAccordion` | [Accordion](/components/accordion) |
| `RxTabs` / `ResuxTabs` | [Tabs](/components/tabs) |
| `RxPopover` / `ResuxPopover` | [Popover](/components/popover) |
| `RxDropdown` / `ResuxDropdown` | [Dropdown](/components/dropdown) |
| `RxTooltip` / `ResuxTooltip` | [Tooltip](/components/tooltip) |
| `RxModal` / `ResuxModal` | [Modal](/components/modal) |
| `RxMotion` / `ResuxMotion` | [Motion](/components/motion) |
| `RxReveal` / `ResuxReveal` | [Reveal](/components/reveal) |
| `RxAutoAnimate` / `ResuxAutoAnimate` | [AutoAnimate](/components/auto-animate) |
| `RxIcon` / `ResuxIcon` | [UI Icon primitive](/components/icon) |

## Important implementation boundaries

### `RxReveal`

It runs a mount-time animation. It does **not** use viewport observation. For IntersectionObserver-triggered Vue animation, use `vAnime` / `vAnimate`.

### `RxAutoAnimate`

It runs a one-time `scale-in` animation after mount. It does **not** observe child insertion/removal/reordering or layout changes.

### UI `RxIcon`

It renders text like `[check]`; it is not the SVG registry/provider component. For SVG icons use [`resuxjs/icons`](/icons/).

## Styling and `unstyled`

Most UI components expose `unstyled`. When true, component-specific Resux classes are omitted while user attributes/classes still pass through according to Vue attribute inheritance.

The default stylesheet is intentionally simple. Do not infer undeclared design-token behavior from the presence of `tokens` configuration.

## Accessibility

Native-element primitives inherit useful browser semantics. Several custom widgets are intentionally small and currently lack parts of complete ARIA interaction patterns. The dedicated component pages identify those limitations explicitly.

Do not claim full keyboard/focus/screen-reader behavior without source/tests demonstrating it.

## SSR / hydration cost

Component markup may be rendered through Vue SSR, but interaction/state/mount hooks require the Vue runtime boundary. The cost is the island/subtree, not an imaginary Resux zero-JS component contract.

For built-in resumable media, see [Images and Media](/media/).

## Related

- [Component catalog](/components/)
- [UI and Motion guide](/guide/ui-animations)
- [Vue Islands](/guide/vue-islands)
- [Current Limits](/reference/limits)
