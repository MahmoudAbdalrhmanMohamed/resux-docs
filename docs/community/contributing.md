# Contributing to the Documentation

Documentation changes should be checked against the actual Resux source, package export map, tests, generated templates, and CLI help.

## Local setup

```sh
npm ci
npm run dev
```

## Validate

```sh
npm run build
```

The VitePress build validates rendering and internal links.

## Source-of-truth order

1. Current framework source and public export map.
2. Tests that assert behavior.
3. Generated starter templates and CLI help.
4. Released package behavior for release-specific claims.
5. Existing documentation only after comparison with the above.

## Writing rules

- Do not hard-code npm `latest` as permanent.
- Distinguish source-branch behavior from published behavior.
- State whether an API is server, browser, Vue, build-time, or resumable.
- Use complete runnable examples with correct return shapes.
- Document security and cleanup boundaries.
- Do not claim automatic email/upload/review behavior that does not exist.
- Prefer links to dedicated guides over duplicating long explanations.

## Pull requests

Include:

- the framework source/ref used,
- pages changed,
- behavior corrected or added,
- validation commands and results,
- and any dependency on an unmerged framework PR.
