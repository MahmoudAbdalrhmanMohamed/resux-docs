# Project Creation API (`resuxjs/create`)

`resuxjs/create` is the Node-only programmatic entry point behind the Resux project creator. Most users should run `create-resuxjs` / `resux init`; tooling can call the exported functions directly.

::: warning Node/CLI environment
This entry imports Node filesystem, process, readline, child-process, OS, path, and URL APIs. Do not import it into browser/runtime application code.
:::

## Exports

```ts
import {
  runCreateResux,
  assertSafeCreateTarget
} from 'resuxjs/create'
```

## `runCreateResux()`

```ts
function runCreateResux(
  args?: string[]
): Promise<void>
```

When `args` is omitted it uses `process.argv.slice(2)`. The function owns the interactive prompt lifecycle, resolves the target directory, validates destructive operations, copies the starter template, applies feature scaffolds, optionally installs dependencies, and prints the next steps.

```ts
import { runCreateResux } from 'resuxjs/create'

await runCreateResux([
  'my-app',
  '--template', 'full',
  '--features', 'tailwind,server-api,tests',
  '--package-manager', 'pnpm',
  '--install',
  '--yes'
])
```

### Supported template names

The current creator recognizes:

```txt
minimal
default
full
i18n
pwa
media
package-compatibility
dashboard
```

### Supported feature names

```txt
seo
i18n
media
pwa
tailwind
package-compatibility
server-api
tests
```

Feature values supplied through `--features` are comma-separated, trimmed, lower-cased, validated, and de-duplicated.

### Important arguments

| Argument | Behavior |
| --- | --- |
| `<target-dir>` | Destination directory. Only one positional target is accepted. |
| `-h`, `--help` | Print creator help and return. |
| `-y`, `--yes` | Use non-interactive/default answers where applicable. |
| `--install` / `--no-install` | Explicit dependency-install decision. |
| `--force` | Allow cleanup of a non-empty target after safety checks. |
| `--template <name>` / `--template=<name>` | Select one verified starter template. |
| `--features <list>` / `--features=<list>` | Add verified starter features. |
| `--package-manager <name>`, `--pm <name>` | Select `npm`, `pnpm`, `yarn`, or `bun`. |
| `--hreflang` / `--no-hreflang` | Explicit alternate-language-link scaffold decision when relevant. |

Unknown flags and unexpected extra positional arguments throw instead of being silently ignored.

### Non-interactive defaults

When `--yes` is used or the process cannot prompt:

- target defaults to `resux-app` when omitted;
- starter template defaults to `default` when omitted;
- package manager is detected when not supplied;
- optional prompts use their implemented defaults rather than inventing answers.

Use explicit arguments in automation when reproducibility matters.

## `assertSafeCreateTarget()`

```ts
function assertSafeCreateTarget(
  root: string,
  cwd: string,
  force: boolean
): void
```

This helper protects the creator's destructive `--force` cleanup path.

When `force` is false it returns immediately. When `force` is true it resolves the target and refuses protected locations including:

- the filesystem root;
- the current user's home directory;
- the current working directory itself;
- any ancestor directory that contains the current working directory.

```ts
import { assertSafeCreateTarget } from 'resuxjs/create'

assertSafeCreateTarget(
  '/work/projects/new-resux-app',
  '/work/projects',
  true
)
```

This exported check is only part of the creator's safety model. `runCreateResux()` also verifies path components against symbolic links and checks target-directory identity while destructive cleanup runs. Calling `assertSafeCreateTarget()` by itself does not perform those later filesystem checks.

## Errors

Creation errors reject the returned promise. Examples include:

- invalid template/package-manager/feature values;
- unknown options;
- a second positional directory;
- a non-empty target without `--force`;
- protected or symlinked destructive targets;
- filesystem/template/install failures.

The executable wrapper catches the rejection, prints the message, and sets a non-zero exit code. Programmatic callers own their own error handling.

## Related

- [Getting Started](/guide/getting-started)
- [CLI](./cli.md)
- [Project Structure](/guide/project-structure)
- [Testing and Quality](/guide/testing-quality)
