# Release and Publishing

This page documents the framework repository's intended npm release process, not application deployment.

## Current stable release

The current stable framework release is `resuxjs@0.3.10`, tagged as `v0.3.10`.

Applications should normally install the latest stable release with:

```sh
npm install resuxjs@latest
```

## CI versus publishing

Normal pull requests and unrelated `main` pushes run validation without publishing npm packages.

The repository's `npm-publish.yml` workflow also watches release metadata on `main`. When the package version changes and the corresponding version tag is missing, the workflow validates the release, creates the matching `vX.Y.Z` tag, and publishes through npm Trusted Publishing. Existing tag, GitHub Release, and manual-dispatch release paths remain supported.

Every publish path must verify that the resolved tag matches `package.json` before publishing.

## Required validation

Before publishing:

```sh
npm ci
npm run typecheck
npm run build
npm test
npm run pack:check
```

Package validation should verify native optional bindings, generated declarations, bundled output, templates, and `npm pack --dry-run` contents.

## Version and tag

For a new release, update the package metadata consistently before pushing `main`. The release workflow derives the version tag from `package.json` for an eligible `main` release-metadata push.

A manual/tag-driven release can still use an explicit tag such as:

```sh
git tag v0.3.10
git push origin v0.3.10
```

Use the actual intended version. Never move or reuse a version that has already been published to npm.

## Trusted Publishing

The repository release workflow uses npm Trusted Publishing through GitHub OIDC with provenance rather than a long-lived `NPM_TOKEN`.

Configure the npm trusted publisher for every package published by the workflow:

- repository: `MahmoudAbdalrhmanMohamed/resux`
- workflow: `npm-publish.yml`
- the correct npm package name

Trusted Publisher configuration is package-specific. Publishing `resuxjs` successfully does not automatically authorize a separate npm package such as `create-resuxjs`.

## One-time passwords

Automation should not attempt interactive OTP publishing. An OTP error indicates the workflow is using token/interactive authentication rather than a correctly configured trusted publisher, or the trusted publisher configuration does not match the workflow and package.

## Documentation coordination

Framework documentation can describe source behavior before it reaches npm only when the change clearly states the dependency. Merge/release source changes before publishing docs that present them as generally available.

## Recovery

If a release fails:

1. inspect the exact workflow job and npm authentication mode,
2. confirm Trusted Publishing is configured for the specific npm package that failed,
3. do not reuse or move an already published version,
4. fix CI/configuration,
5. create a new patch version when package contents changed,
6. keep provenance and tag/package versions aligned.
