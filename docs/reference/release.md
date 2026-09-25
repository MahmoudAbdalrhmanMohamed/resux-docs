# Release and Publishing

This page documents the framework repository's npm release process, not application deployment.

## Release channels

Resux uses separate npm channels while the framework is pre-1.0:

| Channel | npm tag | Intended use |
| --- | --- | --- |
| Stable 0.3 line | `latest` | Existing stable installs |
| Public beta 0.4 line | `next` | Evaluation, real-world testing, compatibility feedback |

The stable line is currently `resuxjs@0.3.11`. The public-beta line begins with `0.4.0-beta.1`.

Install stable:

```sh
npm install resuxjs@latest
```

Install public beta:

```sh
npm install resuxjs@next
```

Prerelease versions do **not** replace `latest`; the publish workflow maps versions containing a prerelease suffix to `next`.

## CI versus publishing

Normal pull requests and branch pushes run validation only. They do not publish npm packages.

The framework's `.github/workflows/npm-publish.yml` workflow runs when a **GitHub Release is published**. The release must point to a tag matching the package version exactly, such as `v0.4.0-beta.1`, and that tagged commit must be reachable from `main`.

The workflow validates the release artifact before any publish step.

## Required release validation

The release workflow verifies:

- package/version metadata alignment;
- framework and `create-resuxjs` version alignment;
- the `create-resuxjs` dependency range on `resuxjs`;
- dependency baseline checks;
- TypeScript/build output;
- framework tests;
- runtime bundle budgets;
- generated fixtures and templates;
- package contract and `npm pack` contents;
- Node, static, Netlify, Vercel, and Cloudflare deployment outputs;
- npm artifact names before publication.

The normal CI matrix additionally covers supported Node runtimes and Windows/macOS portability.

## Version and tag contract

A release version must be synchronized across:

- root `package.json`;
- root `package-lock.json`;
- `packages/create-resuxjs/package.json`;
- the `create-resuxjs` dependency on `resuxjs`.

Then create a GitHub Release for the exact matching tag:

```txt
package version: 0.4.0-beta.1
release tag:     v0.4.0-beta.1
npm dist-tag:    next
```

Stable versions without a prerelease suffix publish under `latest`.

Never move, overwrite, or reuse a version already published to npm.

## Trusted Publishing

The release workflow uses npm Trusted Publishing through GitHub OIDC and publishes with provenance instead of relying on a long-lived `NPM_TOKEN`.

Trusted Publisher configuration is package-specific. Both `resuxjs` and `create-resuxjs` must be authorized for:

- repository: `MahmoudAbdalrhmanMohamed/resux`;
- workflow: `npm-publish.yml`;
- the matching npm package.

The workflow intentionally fails if `create-resuxjs` has never been bootstrapped on npm, because Trusted Publishing must be configured against an existing package.

## Documentation coordination

Living documentation tracks current framework source, but release-specific pages must clearly distinguish source behavior from published package behavior.

When a feature depends on an unreleased framework change, do not present it as available on `latest`. Use the public-beta channel or an explicit version when appropriate.

## Recovery

If a release fails:

1. inspect the exact release-validation or publish job;
2. confirm the tag matches the package version;
3. confirm the tagged commit is reachable from `main`;
4. confirm Trusted Publishing is configured for the package that failed;
5. do not reuse or move a version already published to npm;
6. fix the source or release configuration and publish a new version when package contents changed;
7. keep provenance, tags, package metadata, and documentation aligned.
