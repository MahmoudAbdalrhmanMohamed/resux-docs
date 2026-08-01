# Testing and Quality

Resux applications should validate both ordinary TypeScript behavior and framework-specific compilation/build behavior.

## Recommended checks

```sh
npm run typecheck
resux check
resux build
```

`resux check` validates project structure and generated prerequisites. `resux build` validates SFC compilation, resumability rules, package modes, server output, and deployment integration.

## Starter tests

The create command can add test starter files:

```sh
npx create-resuxjs@latest my-app --features tests
```

Vitest is a natural choice for unit tests because the framework itself uses it, but applications may use another runner.

## Unit-test pure logic

Move data transforms and validation into `utils/`, `shared/`, or server utilities so they can be tested without a browser.

```ts
import { describe, expect, it } from 'vitest'
import { normalizeTitle } from '../utils/title'

describe('normalizeTitle', () => {
  it('trims titles', () => {
    expect(normalizeTitle('  Resux  ')).toBe('Resux')
  })
})
```

## Test server handlers

Handlers are ordinary functions around an event object. Test core behavior directly and add integration tests for HTTP response semantics.

## Test resumability

Important scenarios include:

- server-rendered initial state,
- first interaction module loading,
- DOM binding patches,
- conditional watcher dependency cleanup,
- route-payload navigation,
- enhancement activation and cleanup,
- and serialized async errors.

## CI example

```yaml
- run: npm ci
- run: npm run typecheck
- run: resux check --json
- run: npm run build
- run: npm test
```

## Documentation and package checks

Framework and module maintainers should also dry-run package output and inspect generated manifests. Documentation CI should build VitePress so broken internal links fail before merge.
