# Resux Docs

Documentation site for [Resux](https://github.com/MahmoudAbdalrhmanMohamed/resux), the resumable web framework published as `resuxjs`.

The site documents the complete framework surface rather than only the basic component syntax: compiler, SSR/runtime lifecycle, resumability, reactivity, routing, server APIs, modules, package integration, media processing, optional modules, CLI tooling, deployment, security, and Halal Core.

The documentation avoids hard-coding a permanent npm `latest` version because that value becomes stale. Release-specific behavior should be checked against the installed package and its release notes.

## Local development

```sh
npm ci
npm run dev
```

## Production build

```sh
npm run build
npm run preview
```

The site uses VitePress and is configured for GitHub Pages at `/resux-docs/`.

## Documentation map

- `docs/guide/framework-tour.md` — complete framework architecture and reading order
- `docs/guide/` — concepts and practical feature guides
- `docs/reference/packages.md` — public package/subpath exports
- `docs/reference/cli.md` — all framework commands and important options
- `docs/reference/configuration.md` — framework and module configuration
- `docs/reference/composables.md` — globals, reactivity, data, navigation, server, i18n, media, and package APIs
- `docs/reference/runtime.md` — SSR and resume runtime internals
- `docs/reference/compiler.md` — SFC compilation, manifests, handlers, and output
- `docs/reference/limits.md` — compatibility and production boundaries
- `docs/examples/` — end-to-end usage examples
- `docs/public/llms.txt` — machine-readable documentation index

## Areas explicitly covered

- HTML-first SSR and resumable event handlers
- focused Vue-like SFC support and Vue island boundaries
- Resux-native reactivity and serialized state
- file routing, layouts, route middleware, server middleware, and APIs
- plugins, build-time modules, route rules, Vite/Nitro extension hooks
- SSR/client-only/server-only/progressive third-party packages
- image and video optimization with `sharp` and optional `ffmpeg`
- i18n, icons, fonts, UI primitives, and animations
- Node, Docker, Nitro, Vercel, Netlify, Cloudflare, and static deployment configuration
- security headers, caching, diagnostics, and health checks
- Halal Core reports, manual `review_required` workflow, HMAC signing, and limitations

## Source-of-truth rules

When changing documentation:

1. Verify public exports against `resux/package.json` and `src/**/index.ts`.
2. Verify commands and options against the CLI source and generated starter scripts.
3. Verify configuration against public types and the code that consumes each field.
4. Mark source-only or experimental behavior clearly.
5. Never claim an external service, notification, upload, or security guarantee exists unless the implementation actually provides it.
6. Run the VitePress build to catch broken links and invalid Markdown.

## Contributing

Create a branch, update the relevant guide/reference pages, and run:

```sh
npm ci
npm run build
```

Keep examples copy-pasteable, explain execution context, and include limitations for features that depend on provider behavior, native binaries, remote services, or manual review.
