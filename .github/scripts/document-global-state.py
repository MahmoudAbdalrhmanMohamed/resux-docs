from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


composables_path = Path("docs/reference/composables.md")
composables = composables_path.read_text()
composables = replace_once(
    composables,
    '''## Resumable state

### `useState<T>(key, factory?)`

Create or retrieve a scope state ref:

```ts
const cartCount = useState<number>('cart-count', () => 0)
cartCount.value++
```

The key must be stable. Values that cross SSR/browser boundaries must be JSON-serializable.
''',
    '''## Resumable state

### `useState<T>(key, factory?)`

Create or retrieve a named ref owned by the current rendered component scope:

```ts
const draftStep = useState<number>('draft-step', () => 0)
draftStep.value++
```

Calling `useState` again with the same key inside that component scope returns the same ref. A different component scope using the same key receives a different ref.

Use `ref` or `reactive` when named serialization is unnecessary. The key must be stable and the value must be JSON-serializable.

### `useGlobalState<T>(key, factory?)`

Create or retrieve an app-wide serialized ref shared by all Resux component scopes:

```ts
const session = useGlobalState('session', () => ({
  user: null as null | { id: string; name: string },
  authenticated: false
}))
```

Components using the same key receive the same ref. The first factory initializes the key; later factories for that key are ignored.

During SSR, the registry belongs only to the current request. The values are serialized once under `payload.globalState`, restored as shared browser refs, and preserved during Resux client navigation. A mutation refreshes rendered scopes so bindings in separate components remain synchronized.

Global-state values must be JSON-serializable. Keep credentials, database clients, DOM nodes, sockets, functions, and other runtime-only objects outside global state.
''',
    "composables state reference",
)
composables_path.write_text(composables)


resumability_path = Path("docs/guide/resumability-handlers.md")
resumability = resumability_path.read_text()
resumability = replace_once(
    resumability,
    '''A scope may contain:

- component/module id,
- serializable props,
- `useState` values,
- resolved async data,
- pending and error state,
- and references to generated browser modules.''',
    '''A scope may contain:

- component/module id,
- serializable props,
- component-scoped `useState` values,
- resolved async data,
- pending and error state,
- and references to generated browser modules.

The application payload may also contain `useGlobalState` values once under `payload.globalState`.''',
    "serialized payload description",
)
resumability = replace_once(
    resumability,
    '''::: tip Scope, not global state
`useState` values belong to one rendered component scope. The same key used by another component instance does not overwrite this scope. For ordinary component-local UI state that does not require named serialization, prefer `ref` or `reactive`.
:::''',
    '''::: tip Scoped and global state
`useState` values belong to one rendered component scope. The same key used by another component instance does not overwrite this scope.

Use `useGlobalState` when multiple component scopes intentionally need the same serialized ref. For ordinary local UI state that does not require named serialization, prefer `ref` or `reactive`.
:::''',
    "scope tip",
)
resumability_path.write_text(resumability)

Path(".github/workflows/document-global-state.yml").unlink(missing_ok=True)
Path(".github/scripts/document-global-state.py").unlink(missing_ok=True)
