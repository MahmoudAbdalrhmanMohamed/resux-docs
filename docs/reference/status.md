# Project Status: Stable 0.5

Resux 0.5 is the current **stable** line. The current release is **0.5.0**. The 0.4 line stays installable by exact version (`resuxjs@0.4.0`).

The 0.5 line is published under the `latest` npm tag. The framework has passed a substantial CI and packaging hardening pass, but Resux is still pre-1.0: APIs can change between minor releases, and breaking changes are documented in the changelog.

## Release channels

| Channel | Version line | npm tag | Best fit |
| --- | --- | --- | --- |
| Stable | 0.5.x | `latest` | New and existing projects. The older 0.3.x line stays installable by exact version |
| Prerelease | Upcoming versions with a prerelease suffix | `next` | Testing upcoming releases before they become stable |

0.4 started as a public beta (`0.4.0-beta.1` through `0.4.0-beta.8`). The betas added the v1 font engine (`fontless` + `fontaine`), the modular v1 icon system, native View Transitions API support, route CSS preloading before DOM swap, critical `<meta>` tag ordering and reactive head descriptors, hero video page-ready poster persistence, `.env.local` / `.env` loading across the CLI and Halal Core, reactivity collection instrumentation with ref unwrapping, head `<meta>` deduplication, template refs in resumable client handlers, camelCase `<Transition>` / `<TransitionGroup>` SSR support, `<ClientEnhance>` injection hardening, and Vercel Node runtime clamping. `0.4.0` is the first stable release of the line. On top of the betas it adds a client runtime parity and hardening pass (collections, refs, watchers and the scheduler, readonly views, i18n, package cache keys, and development-time serializability checks), compiler fixes for `rx` directive attribute values and arrow function parameters, deploy option scoping, and a build-time secret scan of public `runtimeConfig` that now covers nested objects at any depth.

0.5 started as a public beta (`0.5.0-beta.1` and `0.5.0-beta.2`). It added named and scoped slots, native DOM events on a component tag, client-created components inside `v-if` and `v-for` (kept across re-renders, updated in place when their props change), and a much smaller resume bootstrap on pages without deferred targets. `0.5.0` is the first stable release of the line. It requires Node.js `>=22.19.0` and has a clean `npm audit`, a lint step and Chromium tests in CI. See the changelog for the full list.

Create a new app:

```sh
npx create-resuxjs@latest my-app
cd my-app
npm install
npm run dev
```

For a repeatable setup, pin the exact release:

```sh
npx create-resuxjs@0.5.0 my-app
```

## Where to use Resux 0.5

Resux 0.5 is appropriate for:

- learning and evaluation;
- demos and prototypes;
- compatibility testing;
- deployment experiments;
- performance testing with realistic applications;
- non-critical applications where you can pin versions and test upgrades;
- finding and reporting production-readiness issues.

It is still pre-1.0, so it does not promise a frozen API or long-term compatibility for every current behavior.

## What is already validated

The framework CI currently covers:

- production quality and package checks;
- Node.js 22.19 and Node.js 24 (Resux 0.5 requires Node.js `>=22.19.0`);
- browser (Chromium) resumability tests: server-rendered and client-created components, slots, emits, `:is` and native events;
- Windows and macOS portability;
- minimal, default, full, i18n, PWA, media, package-compatibility, and dashboard starters;
- Node, static, Netlify, Vercel, and Cloudflare deployment targets;
- package contents and npm release contracts;
- runtime bundle budgets;
- regression coverage for security-sensitive media and path handling.

The framework also includes bounded route/icon caches and request concurrency controls, plus protections around remote media fetching and filesystem paths.

That is useful evidence, but CI cannot replace testing across independent applications and workloads.

## Using Resux 0.5 in production-like environments

Before running Resux in staging or a real application:

1. pin the exact Resux version;
2. run your own integration and end-to-end tests;
3. test the deployment target you actually use;
4. verify the features your app depends on, especially server APIs, media, caching, i18n, resumability, and Vue islands;
5. review [Current Limits](/reference/limits);
6. monitor runtime errors and resource usage;
7. test framework upgrades before shipping them.

For business-critical systems with strict support or compatibility requirements, evaluate Resux 0.5 in a limited-risk environment before making it a core dependency.

## What still needs broader evidence

Before Resux can make a stable 1.0 claim, it needs more experience outside its own test suite, including:

- longer-running production workloads;
- more third-party package integrations;
- upgrade experience across several releases;
- clearer measured coverage reporting;
- documented deprecation and API-stability rules;
- continued security review;
- feedback from developers who were not involved in building the framework.

## Reporting a problem

A useful bug report should include:

- the exact Resux version;
- Node.js version and operating system;
- deployment target;
- a minimal reproduction;
- expected and actual behavior;
- whether the issue happens in development, production build, or both.

Security issues should follow the framework security policy instead of being posted publicly with exploit details.

## Related pages

- [Getting Started](/guide/getting-started)
- [Current Limits](/reference/limits)
- [Testing and Quality](/guide/testing-quality)
- [Deployment](/guide/deployment)
- [Release and Publishing](/reference/release)
