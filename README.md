# Resux Docs

Documentation site for [Resux](https://github.com/MahmoudAbdalrhmanMohamed/resux), the experimental resumable web framework published as `resuxjs`.

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
- Routing, layouts, middleware, plugins, modules, server API, deployment, and troubleshooting docs
- Brand page with logo usage and color palette
- GitHub Actions workflow for publishing to Pages
