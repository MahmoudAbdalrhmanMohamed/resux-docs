# Contributing to the Documentation

Resux documentation is treated as part of the framework product. A page should be accurate enough to use as reference, structured enough to scan quickly, and explicit about runtime ownership, limitations, accessibility, security, and browser cost where those details matter.

Documentation changes must be checked against the actual Resux source, package export map, tests, generated templates, CLI help, and—when the claim is release-specific—the published package behavior.

## Local setup

```sh
npm ci
npm run dev
```

Use Node.js 22 locally when possible so local validation matches documentation CI.

## Validate before opening a pull request

```sh
npm run check:framework-parity
npm run build
```

The parity check verifies that current public package exports remain covered and mapped to documentation destinations. The VitePress build validates rendering and internal documentation links.

## Source-of-truth order

Use this order when documentation and implementation disagree:

1. Current framework source and public export map.
2. Tests that assert observable behavior.
3. Generated starter templates and CLI help.
4. Released package behavior for release-specific claims.
5. Existing documentation only after comparison with the sources above.

Do not copy behavior from Nuxt, Vue, another framework, or an older Resux page and present it as implemented Resux behavior without source evidence.

## Documentation page model

Important guide, component, media, module, and API pages should answer the relevant parts of the following model. Not every short reference page needs every heading, but important product surfaces should not stop at a symbol list.

### 1. Purpose

Explain what the feature solves and why it exists.

### 2. Runtime ownership

State where the behavior runs:

- build/compiler,
- server/SSR,
- resumable browser runtime,
- progressive client enhancement,
- Vue island,
- or a combination of those boundaries.

### 3. Basic usage

Show the smallest realistic working example before advanced options.

### 4. API and defaults

Document the complete relevant surface:

- props,
- options,
- parameters,
- return values,
- events,
- slots,
- types,
- defaults,
- aliases,
- generated attributes or output when important.

### 5. Behavior

Explain the observable result. For framework-level features this can include HTML output, serialized payloads, generated modules, request behavior, caching, preloads, or navigation behavior.

### 6. SSR, resumability, and client cost

Make it clear whether the feature works entirely from server HTML, requires a resumable handler, installs progressive enhancement, or requires Vue hydration/island ownership.

### 7. Accessibility and security

Document application responsibilities and missing built-in behavior explicitly. A component name such as `Modal`, `Dropdown`, or `Tooltip` is not evidence that a complete WAI-ARIA interaction pattern exists.

### 8. Limitations and common mistakes

Say what the current implementation does **not** do. Prefer a clear limitation over an implied capability.

### 9. Related material

Link to the deeper guide, API reference, examples, source-map page, or adjacent feature instead of duplicating large explanations.

## Component-page definition of done

A public UI component page is complete when the source supports and the page documents, where applicable:

- component purpose and native/root element,
- import and aliases,
- all public props and defaults,
- verified built-in variants/styles,
- emitted events versus native fallthrough listeners,
- slots,
- `v-model` or internal-state behavior,
- `unstyled` behavior,
- SSR and Vue-island ownership,
- keyboard/focus/accessibility behavior,
- motion and reduced-motion behavior,
- browser runtime cost,
- limitations,
- basic and advanced examples.

Never infer design-system behavior from a component name alone.

## Guide-page definition of done

A substantial guide should include:

- a clear user goal,
- prerequisites when needed,
- a minimal path to success,
- realistic code or file examples,
- runtime/architecture notes when relevant,
- failure modes or troubleshooting notes,
- links to exact reference pages,
- and current limitations.

## API-reference definition of done

A public API reference should include:

- package/import location,
- signature or shape,
- parameter/prop descriptions,
- defaults,
- return value or emitted behavior,
- execution context,
- minimal example,
- and links to the guide that explains the feature conceptually.

## Visual and structural rules

- Keep one H1 per page.
- Lead with a short explanation before long tables.
- Prefer descriptive H2/H3 headings that work in the right-side outline.
- Put the simplest useful example before advanced configuration.
- Keep tables focused on comparison/reference; use prose for important tradeoffs.
- Use `tip`, `warning`, and `danger` blocks only when they change a developer decision.
- Link to dedicated pages instead of maintaining duplicate long sections.
- Use consistent product names: Resux, `resuxjs`, Resux template primitives, and Vue islands.
- Do not use screenshots when code or semantic HTML explains the same behavior more clearly.

## Writing rules

- Do not hard-code npm `latest` as a permanent version claim.
- Distinguish source-branch behavior from published behavior.
- State whether an API is server, browser, Vue, build-time, or resumable.
- Use complete examples with correct return shapes and imports.
- Document security, cleanup, cache, and lifecycle boundaries where applicable.
- Do not claim automatic email, upload, review, optimization, accessibility, or runtime behavior that does not exist.
- Prefer exact Resux terminology over borrowing terminology that implies behavior from another framework.

## Pull requests

Include:

- the framework source/ref used,
- pages changed,
- behavior corrected or added,
- navigation/design changes when relevant,
- validation commands and results,
- and any dependency on an unmerged framework pull request.

A documentation redesign should preserve useful source-aligned detail. Do not trade technical accuracy for shorter pages or visual polish.
