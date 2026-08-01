# File Conventions Reference

## Resux components

| Path | Meaning |
| --- | --- |
| `app.vue` or `app/app.vue` | app shell |
| `error.vue` or `app/error.vue` | error component |
| `pages/**/*.vue` or `app/pages/**/*.vue` | routes |
| `layouts/**/*.vue` or `app/layouts/**/*.vue` | layouts |
| `components/**/*.vue` or `app/components/**/*.vue` | components |
| `islands/vue/**/*.vue` | Vue runtime islands |

## Support files

| Path | Meaning |
| --- | --- |
| `plugins/**/*.ts` | app plugins |
| `app/plugins/**/*.ts` | nested app plugins |
| `middleware/**/*.ts` | route middleware |
| `app/middleware/**/*.ts` | nested route middleware |
| `enhancements/**/*.ts` | client enhancements |
| `client-enhancements/**/*.ts` | client enhancements |
| `server/middleware/**/*.ts` | request middleware |
| `server/plugins/**/*.ts` | server plugins |
| `server/api/**/*.ts` | `/api` handlers |
| `server/routes/**/*.ts` | custom handlers |

## Auto-import directories

- `composables/`
- `utils/`
- `shared/`
- `server/utils/`
- module-added import directories

Exports from these directories contribute to generated import declarations and package analysis.

## Mode suffixes

- `.client.ts`
- `.server.ts`
- no suffix for all mode
- `.global.ts` for global route middleware

Suffixes can be combined according to the support-file parser.

## Route filenames

```txt
index.vue          index route
about.vue          static route
[id].vue           dynamic segment
[...slug].vue      catch-all segment
```

The same bracket rules apply to server handler discovery.

## Configuration and types

| File | Meaning |
| --- | --- |
| `resux.config.ts` | main app config |
| `resux.halal.config.ts` | safety policy |
| `nitro.config.ts` | Nitro configuration |
| `env.d.ts` | app/global type entry |
| `types/**/*.d.ts` | app augmentation |
| `.env.example` | environment variable names |

## Assets

- `public/` maps directly to root URLs.
- `assets/` contains source CSS/media and is served through a protected `/assets` mapping where needed.
- `assets/css/tailwind.css` activates the managed Tailwind pipeline when dependencies are available.

## Generated paths

- `.resux/`
- `.resux-nitro/`
- `.nitro/`
- `.output/`
- `.resux-generated/`

Do not commit or edit generated output unless a specific deployment workflow requires an artifact outside source control.
