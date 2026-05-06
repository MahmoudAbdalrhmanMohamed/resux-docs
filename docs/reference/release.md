# Release and Publishing

Resux uses a safe release flow:

- CI runs on every push and pull request.
- npm publishing runs only for version tags (`vX.Y.Z`) or published GitHub Releases.
- Normal pushes to `main` do not publish.

At the time of this docs update (2026-05-07), npm `latest` for `resuxjs` is `0.2.23`.

## CI workflow

The CI workflow runs:

```sh
npm ci
npm run lint --if-present
npm run typecheck
npm run build
npm test
npm run pack:check --if-present
```

## Release workflow

Before creating a release tag, run the local quality gate:

```sh
npm install
npm run typecheck
npm run build
npm test
npm pack --dry-run
```

Then publish through Git tags:

1. Update version in `package.json` (for example `0.2.24`).
2. Commit the release changes.
3. Create tag `v0.2.24`.
4. Push commit and tag.
5. GitHub Actions validates the tag/version match and publishes to npm.

```sh
npm version 0.2.24
git push origin main
git push origin v0.2.24
```

## npm auth and provenance

The publish workflow expects:

- `NPM_TOKEN` in GitHub repository secrets.
- `id-token: write` permission for npm provenance.

Publishing uses:

```sh
npm publish --access public --provenance
```

## Safety checks in workflow

Publish job safeguards:

- Validates the tag format (`vX.Y.Z`).
- Validates tag version equals `package.json` version.
- Runs `npm ci` and `npm run pack:check`.
- Skips publish if the package version already exists on npm.
