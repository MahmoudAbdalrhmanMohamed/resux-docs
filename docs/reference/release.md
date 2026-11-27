# Release and Publishing

This page explains how Resux framework releases are published to npm. It is separate from application deployment.

## Release channels

Resux currently uses two npm channels:

| Channel | npm tag | Intended use |
| --- | --- | --- |
| Stable 0.5 line | `latest` | New and existing projects |
| Prereleases | `next` | Testing upcoming releases before they become stable |

The stable line is currently `resuxjs@0.5.0`. Older lines stay installable by exact version, for example `resuxjs@0.4.0` (Node.js `>=20.19.0`) or `resuxjs@0.3.11`.

The 0.4 line started as a public beta with `0.4.0-beta.1` and reached stable with **`0.4.0`**. The 0.4 betas added the v1 font engine (`fontless` + `fontaine`), the modular v1 icon system, native View Transitions API support, route CSS preloading before DOM swap, critical `<meta>` tag ordering and reactive head descriptors, hero video page-ready poster persistence, `.env.local` / `.env` loading across the CLI and Halal Core, reactivity collection instrumentation with ref unwrapping, head `<meta>` deduplication, template refs in resumable client handlers, camelCase `<Transition>` / `<TransitionGroup>` SSR support, `<ClientEnhance>` injection hardening, and Vercel Node runtime clamping. `0.4.0` is the first stable release of the line. On top of the betas it adds a client runtime parity and hardening pass (collections, refs, watchers and the scheduler, readonly views, i18n, package cache keys, and development-time serializability checks), compiler fixes for `rx` directive attribute values and arrow function parameters, deploy option scoping, and a build-time secret scan of public `runtimeConfig` that now covers nested objects at any depth.

The 0.5 line started as a public beta with `0.5.0-beta.1` and reached stable with **`0.5.0`**. It adds named and scoped slots, native DOM events on a component tag, client-created components inside `v-if` and `v-for`, a much smaller resume bootstrap, and requires Node.js `>=22.19.0`. See the changelog for details.

Install the stable channel:

```sh
npm install resuxjs@latest
```

Install the newest prerelease, when one is published (see `npm view resuxjs dist-tags` for what `next` points to):

```sh
npm install resuxjs@next
```

Pin the exact version when you need a repeatable environment:

```sh
npm install resuxjs@0.5.0
```

Prereleases do not replace `latest`; versions with a prerelease suffix are published under `next`.

## When publishing happens

Normal pull requests and branch pushes only run validation. They do not publish packages.

The framework's `.github/workflows/npm-publish.yml` workflow starts when a **GitHub Release is published**.

The release tag must match the package version exactly. For example:

```txt
package version: 0.5.0
release tag:     v0.5.0
npm dist-tag:    latest
```

The tagged commit must also be reachable from `main`.

## What is checked before publishing

The release workflow verifies:

- package and version metadata;
- version alignment between `resuxjs` and `create-resuxjs`;
- the `create-resuxjs` dependency on `resuxjs`;
- dependency baseline checks;
- TypeScript and build output;
- framework tests;
- runtime bundle budgets;
- generated fixtures and starter templates;
- package contracts and `npm pack` contents;
- Node, static, Netlify, Vercel, and Cloudflare deployment output;
- expected npm artifact names.

The regular CI matrix also checks supported Node.js versions plus Windows and macOS portability.

## Version alignment

A release version needs to stay synchronized across:

- root `package.json`;
- root `package-lock.json`;
- `packages/create-resuxjs/package.json`;
- the `create-resuxjs` dependency on `resuxjs`.

Stable versions without a prerelease suffix publish under `latest`.

Never move, overwrite, or reuse a version that has already been published to npm.

## Trusted Publishing

Resux uses npm Trusted Publishing through GitHub OIDC and publishes with provenance instead of relying on a long-lived `NPM_TOKEN`.

Trusted Publisher configuration is package-specific. Both `resuxjs` and `create-resuxjs` need authorization for:

- repository: `MahmoudAbdalrhmanMohamed/resux`;
- workflow: `npm-publish.yml`;
- the matching npm package.

## Release recovery

If publishing fails:

1. inspect the failed validation or publish job;
2. check that the release tag matches the package version;
3. make sure the tagged commit is reachable from `main`;
4. verify Trusted Publishing for the package that failed;
5. do not reuse a version that is already on npm;
6. fix the source or release configuration;
7. publish a new version if package contents changed.

The `0.4.0-beta.2` release is an example of this recovery process: the publishing workflow was corrected and a new prerelease version was used instead of rewriting an already published release.

## Keeping docs and packages aligned

Living documentation should follow the current framework source, but release-specific claims must say which published version they apply to.

If a feature only exists on an unreleased branch, do not document it as available on `latest` or `next` until the matching package has been published.
