# Framework Source Map

The documentation is intended to be **source-aligned**. This page tells maintainers and advanced users where a documented concept lives in the Resux repository, which public package exposes it, and which tests are useful when verifying a claim.

Use this page when:

- a docs sentence feels ambiguous,
- a feature has changed on `main`,
- an npm release and source branch differ,
- you are adding a new public API,
- you are fixing a regression,
- you want to know whether something is public API or only an implementation detail.

## Source of truth order

When sources disagree, use this order:

1. **Current framework source and tests** for what `main` actually implements.
2. **The installed/published package version** for what a consumer can use from a particular release.
3. **These docs** as the explanation of that implementation.
4. Examples/marketing text only after they agree with the implementation.

The docs should never invent an API because Nuxt, Vue, React, Qwik, or another framework has a similarly named feature.

## Package boundary

The framework package is `resuxjs`. The current source package exposes these public package specifiers through `package.json`:

| Import specifier | Main source area | What it represents |
| --- | --- | --- |
| `resuxjs` | `src/index.ts` / runtime-facing exports | Main framework entry |
| `resuxjs/node` | `src/node.ts`, server/deploy integration | Node handler/server entry |
| `resuxjs/globals` | `src/globals.ts` | Runtime/global convenience exports |
| `resuxjs/runtime` | `src/runtime/index.ts` | Runtime types, composables, server/browser/app APIs |
| `resuxjs/reactivity` | `src/reactivity/` | Custom reactive primitives |
| `resuxjs/compiler` | `src/compiler/` | Compiler APIs and implementation |
| `resuxjs/create` | `src/create.ts` | Project/template creation API |
| `resuxjs/i18n` | `src/i18n/` | Localization/route translation support |
| `resuxjs/ui` | `src/ui/index.ts` | Optional Vue UI + motion primitives |
| `resuxjs/icons` | `src/icons/index.ts` | SVG icon system/registry/provider/runtime |
| `resuxjs/fonts` | `src/fonts/index.ts` | Font configuration/head/style support |
| `resuxjs/kit` | `src/kit/index.ts` | Module/extension authoring helpers |
| `resuxjs/core` | `src/core/` | Core config/hooks/module-container infrastructure |
| `resuxjs/halal` | `src/halal.ts`, `src/halal-core/` | Optional policy/integrity subsystem |
| `resuxjs/package.json` | `package.json` | Package metadata |

The exact export map in the framework `package.json` is authoritative. The docs repository also contains a parity check that verifies public package specifiers appear in the package/coverage references.

## Current source version vs npm version

The framework source `package.json` should be checked whenever docs are updated. At the time this source map was introduced, the source package reports `0.3.3`.

Do not assume that npm's `latest` tag always points to the same commit as repository `main`. A feature can be:

- implemented on `main`,
- documented against `main`,
- but not yet present in the currently published package.

For user-facing release questions, verify the installed/published version rather than relying on this page's historical version number.

## Compiler

### Source

```text
src/compiler/
  adapter.ts
  dev-warnings.ts
  directives.ts
  implementation.ts
  index.ts
```

### Public entry

```ts
import ... from 'resuxjs/compiler'
```

### Responsibilities

The compiler area is where to verify claims about:

- the supported SFC/template subset,
- template AST/transform behavior,
- interpolation/attribute bindings,
- event extraction and generated handlers,
- resumability/capture rules,
- supported directives,
- scoped style compilation,
- compiler diagnostics and developer warnings,
- generated server/browser artifacts.

### Tests

Useful tests include:

```text
tests/compiler.test.ts
tests/compiler-path-regressions.test.ts
tests/dev-warnings.test.ts
tests/rx-directives.test.ts
```

### Docs

- [Compiler API](/reference/compiler)
- [Template Syntax](/guide/template-syntax)
- [Code to Browser](/guide/code-to-browser)
- [Resumability Deep Dive](/guide/resumability-deep-dive)

## Runtime

### Source

```text
src/runtime/index.ts
```

The runtime file is intentionally broad. It contains much of the contract connecting server rendering, browser resume/navigation, application composables, route state, modules/packages, media behavior, and generated/runtime types.

### Public entries

```ts
import ... from 'resuxjs/runtime'
import ... from 'resuxjs/globals'
```

and many high-level APIs are re-exported through the main package/build environment.

### Responsibilities to verify here

- route/runtime types,
- `useState`, async data/fetch behavior,
- router/navigation APIs,
- head/SEO/runtime config,
- plugins/middleware/module contracts,
- client enhancements,
- third-party package modes/adapters,
- server event helpers,
- serialization/payload structures,
- browser runtime generation/behavior,
- image/picture/video renderer/runtime contracts,
- app-provide/injection contracts,
- route payload/navigation behavior.

### Tests

```text
tests/runtime.test.ts
tests/runtime-boundaries.test.ts
tests/runtime-concurrency-regressions.test.ts
tests/runtime-performance-regressions.test.ts
tests/runtime-state-registry.test.ts
tests/global-state.test.ts
tests/use-fetch-identity-regressions.test.ts
tests/client-enhancement-lifecycle.test.ts
tests/client-enhancement-shared-target.test.ts
```

### Docs

- [Runtime Internals](/reference/runtime)
- [Composables and Globals](/reference/composables)
- [Request Lifecycle](/guide/request-lifecycle)
- [Architecture Deep Dive](/guide/architecture-deep-dive)
- [Package Integration](/guide/package-integration)
- [Media](/media/)

## Reactivity

### Source

```text
src/reactivity/
  computed.ts
  effect.ts
  reactive.ts
  readonly.ts
  ref.ts
  scheduler.ts
  types.ts
  utils.ts
  watch.ts
  index.ts
```

### Public entry

```ts
import {
  ref,
  reactive,
  computed,
  watch,
  watchEffect,
  readonly,
  toRef,
  toRefs,
  nextTick
} from 'resuxjs/reactivity'
```

The runtime also re-exports many of these primitives.

### What to verify here

- dependency tracking,
- ref/reactive behavior,
- computed invalidation,
- watch/watchEffect scheduling,
- readonly behavior,
- `toRef`/`toRefs`,
- scheduler and next-tick behavior,
- array/edge-case behavior.

### Tests

```text
tests/reactivity.test.ts
tests/reactivity-regressions.test.ts
tests/reactivity-edge-cases.test.ts
tests/reactivity-array-regressions.test.ts
tests/generated-reactivity-regressions.test.ts
```

### Docs

- [State and Reactivity](/guide/state)
- [Reactivity API](/reference/reactivity)

## UI and motion

### Source

```text
src/ui/index.ts
```

### Public entry

```ts
import ... from 'resuxjs/ui'
```

### Critical runtime boundary

The UI package imports Vue's `defineComponent`, `h`, lifecycle/ref helpers, and implements `Rx*` components as Vue components. This is the source of truth for the statement that `resuxjs/ui` belongs inside a Vue runtime boundary rather than being a zero-hydration Resux template primitive.

### Components/APIs to verify here

The source contains the UI module/options, animation presets, motion helpers/directive, and component definitions such as:

- `RxMotion`,
- `RxReveal`,
- `RxAutoAnimate`,
- `RxButton`,
- `RxCard`,
- `RxBadge`,
- `RxInput`,
- `RxSelect`,
- `RxDatePicker`,
- `RxPopover`,
- `RxAvatar`,
- `RxAlert`,
- `RxAccordion`,
- `RxTooltip`,
- `RxDropdown`,
- `RxTabs`,
- `RxTextarea`,
- `RxSwitch`,
- `RxSkeleton`,
- `RxDivider`,
- `RxKbd`,
- `RxModal`,
- `RxIcon`,
- matching `Resux*` aliases,
- `useAnimate()`,
- `vAnime` / `vAnimate`,
- `isReducedMotion()`,
- UI module/tokens configuration.

The component source should be checked for exact root elements, prop defaults, emitted events, internal state, accessibility attributes, and limitations.

### Tests

```text
tests/ui.test.ts
tests/ui-regressions.test.ts
tests/ui-browser-boundary.test.ts
```

### Docs

- [UI Components](/components/)
- [Component Anatomy](/components/component-anatomy)
- [UI Package API](/reference/ui)
- [UI and Motion Guide](/guide/ui-animations)

## Icons

### Source

```text
src/icons/index.ts
```

### Public entry

```ts
import ... from 'resuxjs/icons'
```

### Verify here

- icon definitions/registry,
- collection/provider configuration,
- name resolution,
- remote/provider loading,
- runtime loading/lazy behavior,
- cache behavior,
- SVG/rendering behavior,
- icon component/options.

### Tests

```text
tests/icons-regressions.test.ts
```

### Docs

- [Icons](/icons/)
- [Usage and Registry](/icons/usage)
- [Configuration](/icons/configuration)
- [Runtime Loading](/icons/runtime)

## Fonts

### Source

```text
src/fonts/index.ts
```

### Public entry

```ts
import ... from 'resuxjs/fonts'
```

### Verify here

- font family/source configuration,
- local/remote source normalization,
- generated CSS/head output,
- preload behavior,
- display/weight/style handling,
- runtime/module configuration.

### Tests

```text
tests/fonts.test.ts
```

### Docs

- [Fonts](/fonts/)
- [Font Configuration](/fonts/configuration)
- [Font Performance and CSP](/fonts/performance)

## i18n

### Source

```text
src/i18n/index.ts
src/i18n/shared.ts
```

### Public entry

```ts
import ... from 'resuxjs/i18n'
```

### Verify here

- locale configuration,
- translation lookup,
- route locale resolution,
- shared server/browser normalization,
- translated text/raw behavior.

### Tests

```text
tests/i18n.test.ts
```

### Docs

- [i18n and Localization](/guide/i18n)
- [i18n API](/reference/i18n)

## Core and module container

### Source

```text
src/core/
  config.ts
  hooks.ts
  module-container.ts
  resux.ts
  index.ts
```

### Public entry

```ts
import ... from 'resuxjs/core'
```

### Verify here

- core Resux instance creation/config,
- hook container semantics,
- module registration/execution,
- extension lifecycle,
- core configuration shapes.

### Docs

- [Core API](/reference/core)
- [Lifecycle Hooks](/reference/hooks)
- [Modules and Route Rules](/guide/modules-route-rules)

## Resux Kit

### Source

```text
src/kit/index.ts
```

### Public entry

```ts
import ... from 'resuxjs/kit'
```

### Verify here

Helper APIs intended for modules/extensions, including convenience wrappers around the module context/build contribution model.

### Docs

- [Resux Kit API](/reference/kit)
- [Modules and Route Rules](/guide/modules-route-rules)

## Project creation

### Source

```text
src/create.ts
src/create-bin.ts
packages/create-resuxjs/
templates/
```

### Public/CLI surfaces

```ts
import ... from 'resuxjs/create'
```

and commands exposed by `resuxjs`, `resux`, `create-resux`, and `create-resuxjs` package bins.

### Verify here

- template selection,
- generated directory/file structure,
- package metadata/scripts,
- initial config,
- safety/overwrite rules,
- generated default app examples.

### Tests/scripts

```text
tests/cli-generated-dirs.test.ts
tests/create-safety-regressions.test.ts
scripts/test-templates.mjs
```

### Docs

- [Getting Started](/guide/getting-started)
- [Project Creation API](/reference/create)
- [CLI](/reference/cli)
- [Project Structure](/guide/project-structure)

## CLI

### Source

```text
src/cli.ts
src/bin.ts
```

The CLI source is a major orchestration layer and also interacts with build/deploy/media/config behavior.

### Verify here

- command names/options,
- build/dev/preview behavior,
- generated output paths,
- deployment command wiring,
- inspect/check commands,
- configuration loading,
- media/build orchestration.

### Docs

- [CLI](/reference/cli)
- [Dev Server and Build Output](/guide/dev-build-output)
- [Deployment](/guide/deployment)

## Deployment

### Source

```text
src/deploy/
  common.ts
  types.ts
  node.ts
  static.ts
  vercel.ts
  netlify.ts
  cloudflare.ts
  runtime-dependencies.ts
  index.ts
```

### Verify here

- deploy target selection,
- target-specific files/configuration,
- runtime dependency collection,
- server/static output conventions,
- Nitro/preset integration.

### Tests/scripts

```text
tests/deploy.test.ts
scripts/verify-deploy-targets.mjs
scripts/verify-vercel-output.mjs
```

### Docs

- [Deployment](/guide/deployment)
- [Node Handler API](/reference/node)

## Node/server integration

### Source

```text
src/node.ts
src/nitro-server/index.ts
src/deploy/
```

Server helper/runtime behavior is also implemented within `src/runtime/index.ts` and h3/Nitro integration.

### Public entry

```ts
import ... from 'resuxjs/node'
```

### Docs

- [Node Handler API](/reference/node)
- [Server API](/guide/server-api)

## Images and video

There is no standalone `src/media/` directory in the current source tree. That is important when auditing the docs: media is implemented through the **runtime/renderer/CLI/build pipeline**, with image/video configuration and template primitive behavior living alongside those systems.

### Source areas to inspect

```text
src/runtime/index.ts
src/cli.ts
package.json            # sharp dependency
scripts/ / deploy code  # output/runtime validation where relevant
```

`src/runtime/index.ts` defines image configuration types such as:

- `ResuxImageFit`,
- `ResuxImageCacheInput`,
- `ResuxImageModifiers`,
- `ResuxImageProviderConfig`,
- `ResuxImageConfig`,
- `UseResuxImageOptions`,
- `ResuxImageBuilder`.

The renderer/runtime source is also where template behavior for `ResuxImg`, `ResuxPicture`, and `ResuxVideo` should be verified.

The current package depends on `sharp`, which supports image transformation. Video transformation paths documented as requiring transcoding depend on external `ffmpeg` availability.

### Docs

- [Images and Media](/media/)
- [Images](/media/images)
- [Responsive Images](/media/responsive-images)
- [Image Optimization](/media/optimization)
- [Video](/media/video)

## Halal Core

### Source

```text
src/halal.ts
src/halal-core/
  ai/
  cli/
  crypto/
  report/
  review/
  rules/
  runtime/
  scanner/
  tamper/
  config.ts
  enforce.ts
  lifecycle.ts
  status.ts
```

### Public entry

```ts
import ... from 'resuxjs/halal'
```

### Verify here

- scanning categories/rules,
- project/runtime scanning,
- report generation/signing/verification,
- manual review workflow,
- AI-classification support,
- sensitive-data redaction,
- production integrity/auth behavior.

### Tests

```text
tests/halal-core.test.ts
tests/halal-ai-regressions.test.ts
tests/halal-integrity-regressions.test.ts
tests/halal-production-auth.test.ts
tests/halal-runtime-guard.test.ts
tests/halal-runtime-security-regressions.test.ts
tests/halal-scanner-regressions.test.ts
```

### Docs

- [Halal Core](/guide/halal-core)
- [Halal Core API](/reference/halal)

## Templates are part of framework behavior

The `templates/` directory is not merely promotional sample code. Generated projects inherit decisions from those templates, including:

- initial app shell,
- layouts,
- pages,
- middleware,
- plugins,
- server APIs,
- config,
- CSS/public assets,
- deployment examples,
- TypeScript declarations.

When docs say “a newly created project contains X,” verify the selected template and create logic rather than assuming every template has the same files.

## Tests are part of documentation research

Source code tells you what an implementation *appears* to do. Tests tell you which edge cases are intentionally protected.

When documenting a subtle behavior, search for a regression test before writing a broad rule. Particularly useful test categories include:

- `*-regressions.test.ts`,
- runtime boundary tests,
- compiler directive/warning tests,
- package/deployment tests,
- UI/browser-boundary tests,
- state/concurrency tests.

A docs claim that contradicts a targeted regression test is probably wrong or stale.

## Public API vs implementation detail

Not every exported TypeScript symbol inside a source file is necessarily intended as a stable top-level application API.

Treat these as stronger evidence of supported public API:

1. exported through a `package.json` public specifier,
2. present in generated `.d.ts`/entry exports,
3. covered by tests,
4. documented in the public API reference,
5. used by generated templates/examples.

Treat internal helper names, generated metadata attribute names, payload internals, and private build functions as implementation details unless the public contract explicitly guarantees them.

This matters especially for resumability metadata: docs should explain **what the metadata accomplishes** without promising that a particular private `data-*` attribute name will never change.

## How to update docs when source changes

For each framework change:

1. identify changed public exports/types/CLI/config behavior,
2. identify the source subsystem,
3. inspect associated tests,
4. search docs for the old name/behavior,
5. update the API reference,
6. update the conceptual guide if the mental model changed,
7. update examples,
8. update current limitations/accessibility notes,
9. run framework/docs parity checks,
10. build the docs site and check links.

A new API is not fully documented if it appears only in an export table. Users need to know **why to use it, where it runs, how it composes with the framework, and what its current boundaries are**.

## Related

- [Documentation Coverage](/reference/coverage)
- [Package Exports](/reference/packages)
- [Public API Index](/reference/api-index)
- [Architecture Deep Dive](/guide/architecture-deep-dive)
- [Debugging Mental Model](/guide/debugging-mental-model)
