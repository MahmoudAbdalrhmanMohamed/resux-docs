# Debugging Mental Model

When a Resux application fails, the fastest path is usually **not** “try random framework changes.” First determine which subsystem owns the symptom.

Resux has distinct compilation, server-rendering, resumability, navigation, reactivity, Vue-island, package, media, server, and deployment layers. A problem that looks identical in the UI can have a completely different cause depending on which layer last worked correctly.

This guide gives you a repeatable way to narrow failures before reading logs or source code.

## Start with one question

Ask:

> **What is the last thing I can prove worked?**

Examples:

- If `npm run build` fails, do not debug browser event delegation yet.
- If the correct HTML never reaches the browser, do not start by blaming reactivity.
- If HTML is correct but a click does nothing, focus on event metadata, generated handler loading, scope reconstruction, and browser errors.
- If state changes but the DOM does not, focus on reactive dependency/binding updates.
- If only a Vue island fails, do not assume the normal Resux renderer is broken.
- If local dev works but deployment returns missing JS chunks, inspect deployment/output paths before changing component code.

## Failure map

| Symptom | First subsystem to inspect |
| --- | --- |
| SFC/template fails during build | Compiler / supported syntax |
| Build cannot resolve an import | Package config / Vite / export path |
| Route returns 404 | File routing / route generation |
| Unexpected redirect/abort | Middleware |
| Initial HTML contains wrong value | Server setup / async data / render |
| Secret appears in page source/payload | Serialization/runtime-config ownership |
| Page HTML is right, click does nothing | Resumable event/handler loading |
| Click runs, state does not change | Handler/application logic/reactivity |
| State changes, DOM remains stale | Binding generation/reactive update |
| Client navigation fails, reload works | Client router/payload/middleware |
| Browser-only package crashes SSR | Package mode/runtime boundary |
| Vue component warns/fails to mount | Vue island / UI boundary |
| Image URL 404s or transform fails | Media config/provider/transform endpoint |
| Video transform fails in production | Media tooling/environment (`ffmpeg`) |
| Fonts blocked or missing | Font config/CSP/preload/CSS |
| Icons missing only at runtime | Icon registry/provider/cache/loading |
| Works locally, fails on hosting target | Deployment adapter/output/runtime dependency |
| Memory/listeners grow after navigation | Client-enhancement/island cleanup |

Use the table as a starting hypothesis, not as proof.

## Layer 1: compiler failures

Compiler failures happen before a usable application bundle exists.

Typical causes include:

- unsupported SFC/template syntax,
- unsupported directive/expression shape,
- resumability restrictions,
- unsafe/unrepresentable handler captures,
- invalid generated references,
- path/import problems discovered while compiling.

### What to inspect

1. Read the **first meaningful compiler error**, not only the final command exit.
2. Identify the exact source file and expression.
3. Compare the syntax with [Template Syntax](/guide/template-syntax).
4. Check whether the code assumes full Vue SFC/runtime semantics that normal Resux does not implement.
5. If the problem is a browser/Vue library, ask whether it belongs in a Vue island or client enhancement instead.

### Useful distinction

If code is valid Vue but rejected by Resux, that does not automatically mean the Resux compiler has a bug. Normal Resux deliberately supports a focused SFC subset rather than silently switching to full Vue hydration.

Read [Compiler API](/reference/compiler) and [How Resux Uses Vue](/guide/how-resux-uses-vue).

## Layer 2: discovery and routing

If the build succeeds but a page cannot be reached, inspect route discovery before page setup.

Check:

- file location under `pages/`,
- dynamic/catch-all naming,
- generated route path,
- middleware that may redirect/abort,
- route rules,
- module code that extends pages,
- stale build output after moving files.

### Debugging test

Try to separate **route not found** from **route matched but render failed**.

A clean framework 404 usually points to discovery/routing. A 500/error page with the expected route context points further down the lifecycle.

Read [Routing](/guide/routing) and [Modules and Route Rules](/guide/modules-route-rules).

## Layer 3: server setup and async data

If the route matches but the first HTML contains missing/wrong data, inspect server execution.

Questions:

- Did setup run with the expected route params/query?
- Did `useAsyncData()` / `useFetch()` resolve or report an error?
- Is the API endpoint itself returning the expected response?
- Did middleware change the request or route?
- Is a server-only environment variable available in the deployment environment?
- Is a value unexpectedly shared across requests when it should be request-local?

### Do not debug the browser first

Open/view the original HTML or server response. If the wrong value is already present before browser JavaScript executes, the bug is upstream of resumability.

Read [Async Data](/guide/async-data), [State](/guide/state), and [Server API](/guide/server-api).

## Layer 4: serialization and state ownership

A server-rendered value may need to continue in the browser. That creates both technical and security constraints.

### Technical symptoms

- state cannot be reconstructed,
- handler works on server assumptions but fails in browser,
- class/function/instance identity disappears,
- cyclic/non-JSON-like data produces an error or unusable payload.

### Security symptoms

- private tokens appear in page source,
- server runtime config leaks into browser-visible config,
- sensitive objects are manually stringified to “make resumability work.”

### Correct fix

Do not serialize opaque authority. Move private behavior behind a server API/middleware/server plugin and serialize only the result/state that the browser is allowed to know.

Read [Resumability Deep Dive](/guide/resumability-deep-dive), [Runtime Config](/guide/runtime-config), and [Security and Caching](/guide/security-caching).

## Layer 5: initial HTML rendering

If data is correct but markup is wrong, inspect template rendering/layout/head/style behavior.

Examples:

- conditional block rendered unexpectedly,
- repeated list misses items,
- attribute has wrong server value,
- wrong layout wraps the page,
- page title/meta is incorrect,
- scoped style is missing,
- app shell/error boundary is not what you expect.

### Isolation technique

Reduce the page temporarily to a small static expression using the same state. If that renders correctly, reintroduce the surrounding template structure until the problem reappears.

This helps distinguish a data problem from a template/block problem.

## Layer 6: browser bootstrap

If server HTML is correct but **all** client behavior is dead, inspect the browser runtime and built assets before individual handlers.

Check DevTools for:

- failed JS/chunk requests,
- wrong asset base path,
- CSP blocking scripts/modules,
- syntax/runtime errors during bootstrap,
- stale cached HTML referencing old chunks,
- deployment rewrites returning HTML for JS URLs,
- client plugin throwing before other runtime setup completes.

A single startup error can make many unrelated buttons appear broken.

## Layer 7: resumable event failures

If the page runtime generally works but one interaction does nothing, narrow the problem to that event.

Work through this sequence:

1. Is the expected event present in authored template code?
2. Did compilation succeed without downgrading/removing it?
3. Does generated/server HTML contain the framework event identity expected by the build?
4. Does the browser receive the event through delegation?
5. Can the generated handler module URL be resolved and imported?
6. Can the required scope/state be reconstructed?
7. Does the handler throw?
8. Does the handler mutate the value you think it mutates?

### Network tab clue

The first click may trigger a dynamic module request. A 404/HTML response/CSP error for that request is often a deployment or generated-asset problem, not a state problem.

Read [Resumability and Handlers](/guide/resumability-handlers).

## Layer 8: reactivity and DOM bindings

A particularly useful distinction is:

> **Did the state change, and did the DOM fail to reflect it?**

If yes, the event itself probably worked.

Inspect:

- whether the value is actually reactive,
- which computed/watch/effect depends on it,
- whether the template expression generated a binding,
- whether the correct resumed scope owns that binding,
- whether a block was disposed/replaced during navigation,
- whether imperative third-party code overwrote framework-owned DOM.

### Third-party DOM ownership

If a library directly replaces/moves nodes that Resux expects to update, define a clear boundary. Use a client enhancement or Vue island around the library-owned region rather than allowing two runtimes to mutate the same DOM unpredictably.

Read [Reactivity API](/reference/reactivity) and [Package Integration](/guide/package-integration).

## Layer 9: client navigation

A classic symptom is:

> “Directly opening `/account` works, but clicking a link to `/account` fails.”

That strongly suggests the server route itself exists, while the **client navigation path** differs.

Inspect:

- browser route middleware,
- destination route payload request,
- redirects/aborts,
- history/base URL handling,
- head/style update,
- route payload parsing,
- cleanup of the previous route,
- client plugin/enhancement errors during transition.

Try comparing the network responses for:

- a full document request,
- a client route payload/navigation request.

Read [Routing](/guide/routing) and [Request Lifecycle](/guide/request-lifecycle).

## Layer 10: Vue island and `resuxjs/ui` failures

If only a Vue-owned region is broken, debug it as an explicit runtime boundary.

Check:

- is the component actually inside a Vue island/runtime boundary?
- did the island's client bundle load?
- does the island expect browser APIs during SSR?
- are props crossing the boundary serializable/valid?
- is a Vue library assuming an app plugin/provider that was not installed in the island?
- is the UI component's behavior more limited than its name suggests?

### Important UI examples

Current UI primitives intentionally have different capability levels. For example:

- `RxAutoAnimate` is a one-time mount animation, not a mutation/layout animation engine,
- `RxReveal` animates on mount; it does not itself observe viewport visibility,
- `RxModal` is a small overlay primitive and does not imply a complete focus-trap/dialog system,
- `RxDropdown`/`RxSelect` should not be assumed to implement every production ARIA interaction pattern.

Read each component page rather than inferring behavior from the component name.

See [Component Anatomy](/components/component-anatomy) and [UI Components](/components/).

## Layer 11: third-party packages

When an npm package breaks, determine its runtime assumptions.

### “window is not defined” during SSR

The package probably executed in a server context despite requiring browser globals. Consider `clientOnly`, a progressive client enhancement, or a Vue island depending on ownership.

### CSS is missing

Check package CSS configuration/import and whether the package's styles are included in the intended build path.

### Package initializes twice

Check whether both a client plugin and enhancement/island initialize the same target, or whether cleanup is missing during navigation.

### Package mutates server-owned DOM

Create a clear ownership boundary instead of letting the package and Resux patch the same nodes.

Read [Third-party Packages](/guide/package-integration) and [Integration Cookbook](/guide/integration-cookbook).

## Layer 12: images and video

Media failures should be split into **markup**, **URL generation**, **transform endpoint**, and **browser loading**.

### Image is missing but URL looks correct

Open the generated URL directly. Inspect status/content type and remote-source/provider policy.

### Transform endpoint fails

Check:

- source path/remote URL,
- provider configuration,
- width/height/format modifiers,
- cache configuration,
- `sharp` availability/runtime compatibility,
- remote-source security restrictions.

### Responsive image selects an unexpected asset

Inspect the actual `srcset`, `sizes`, viewport/DPR, and candidate widths. The browser chooses the candidate; Resux provides the candidate set/hints.

### Video transformation fails

Check whether the requested path actually requires transcoding and whether `ffmpeg` is available on the host/runtime.

Read [Images](/media/images), [Responsive Images](/media/responsive-images), [Image Optimization](/media/optimization), and [Video](/media/video).

## Layer 13: fonts

If a font works locally but not in production, inspect:

- generated `@font-face`/head output,
- font URL and content type,
- deployment static-asset path,
- CORS for remote font hosts,
- CSP `font-src` / `style-src`,
- preload URL matching the actual font URL,
- selected family/weight/style.

The browser may silently fall back to another font while the page otherwise appears healthy, so use the computed-font information in DevTools.

Read [Fonts](/fonts/) and [Performance and CSP](/fonts/performance).

## Layer 14: icons

For icons, distinguish:

- registry resolution,
- local collection lookup,
- provider/remote request,
- cache/lazy runtime loading,
- SVG/render output.

If only remote icons fail, do not rewrite the `Icon` component first—inspect provider URL, CSP/network policy, and the runtime fetch response.

Read [Icons](/icons/) and [Runtime Loading](/icons/runtime).

## Layer 15: deployment

If the project passes local checks but fails only after deployment, compare **environment and generated output**, not just source code.

Check:

- selected deploy target/preset,
- Node/runtime version,
- environment variables,
- filesystem assumptions,
- static/public asset base paths,
- server handler routes/rewrites,
- runtime dependencies included in output,
- platform-specific config generated by the adapter,
- `sharp`/native binary compatibility where image transforms run,
- `ffmpeg` availability where video transforms run,
- CSP/CDN caching behavior,
- whether stale HTML references removed chunks.

Read [Deployment](/guide/deployment) and [Dev Server and Build Output](/guide/dev-build-output).

## Layer 16: leaks after navigation

If the app becomes slower after navigating around, suspect lifetime/cleanup problems.

Look for:

- duplicate window/document listeners,
- `IntersectionObserver` instances never disconnected,
- timers/intervals never stopped,
- third-party widgets never destroyed,
- repeated package initialization on the same target,
- stale Vue islands/enhancements still referencing removed DOM.

A client enhancement can return cleanup logic. Use it. Libraries that expose `destroy()`, `dispose()`, or equivalent should generally be cleaned up when the owning route/target disappears.

## A disciplined debugging workflow

Use this sequence before making large changes:

1. **Reproduce with one exact URL/action.**
2. **Record whether build succeeds.**
3. **Inspect the raw initial response/HTML.**
4. **Check server logs for request/setup/data errors.**
5. **Open browser console before interacting.**
6. **Inspect network failures during bootstrap.**
7. **Perform exactly one interaction and observe new requests/errors.**
8. **Verify state changed independently of DOM if possible.**
9. **Try direct navigation vs client navigation.**
10. **Identify runtime owner: Resux, Vue island, package enhancement, server, or media subsystem.**
11. **Reduce to the smallest failing example.**
12. **Only then inspect the relevant source/test area.**

This keeps one bug from turning into unrelated rewrites.

## Source/test areas by symptom

| Area | Source | Tests to look for |
| --- | --- | --- |
| Compiler/templates | `src/compiler/` | `tests/compiler*.test.ts`, directive/dev-warning tests |
| Reactivity | `src/reactivity/` | `tests/reactivity*.test.ts` |
| Runtime/resume/navigation | `src/runtime/` | `tests/runtime*.test.ts`, state/enhancement tests |
| UI | `src/ui/` | `tests/ui*.test.ts` |
| Icons | `src/icons/` | `tests/icons-regressions.test.ts` |
| Fonts | `src/fonts/` | `tests/fonts.test.ts` |
| i18n | `src/i18n/` | `tests/i18n.test.ts` |
| Deployment | `src/deploy/` | `tests/deploy.test.ts`, deploy verification scripts |
| Halal Core | `src/halal-core/` | `tests/halal-*.test.ts` |
| Package/runtime boundaries | runtime + package config | package/runtime-boundary tests |

See [Source Map](/reference/source-map) for the complete documentation-oriented map.

## What to include in a useful bug report

A high-quality report should state:

- Resux source/npm version,
- Node version,
- dev vs build/preview/deployed environment,
- deployment target if relevant,
- minimal route/component source,
- exact command,
- exact URL/action,
- first relevant compiler/server/browser error,
- whether raw SSR HTML is correct,
- whether full reload and client navigation behave differently,
- whether the feature is normal Resux, a Vue island/UI component, or a third-party enhancement.

That information usually cuts the search space dramatically.

## Related

- [Architecture Deep Dive](/guide/architecture-deep-dive)
- [Request Lifecycle](/guide/request-lifecycle)
- [Resumability Deep Dive](/guide/resumability-deep-dive)
- [Troubleshooting](/guide/troubleshooting)
- [Current Limits](/reference/limits)
- [Source Map](/reference/source-map)
