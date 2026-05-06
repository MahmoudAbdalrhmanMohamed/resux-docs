# Resux Docs

Documentation site for [Resux](https://github.com/MahmoudAbdalrhmanMohamed/resux), the resumable web framework published as `resuxjs`.

The docs describe a stable v1 core (compiler subset, SSR, resumable runtime, routing, CLI) and clearly mark experimental areas (Vue islands escape hatch and unsupported Vue syntax outside the documented subset).

## Local development

```sh
npm install
npm run dev
```

## Production build

```sh
npm run build
npm run preview
```

The site is built with VitePress and is configured for GitHub Pages at `/resux-docs/`.

## What is inside

- Full getting-started flow for `npx resuxjs@latest init`
- Core concept map for Resux components, payloads, scopes, route payloads, handlers, plugins, modules, route rules, and islands
- Rendering lifecycle guide from compile time through browser interaction
- Resumability and handler guide for safe state, captures, patches, modifiers, and mounted work
- Execution context, app shell/error, dev/build output, and security/caching concept guides
- Resux component language guide
- CLI reference
- Global composables reference
- Release and publishing reference (CI + tag-based npm publish flow)
- Routing, layouts, middleware, plugins, modules, server API, deployment, and troubleshooting docs
- Brand page with logo usage and color palette
- GitHub Actions workflow for publishing to Pages
