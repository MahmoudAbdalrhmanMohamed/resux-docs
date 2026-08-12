# Examples

This section turns real Resux Lab regression pages into focused recipes you can copy into an application. The examples are intentionally tied to code that runs in [`resux-lab`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab), rather than inventing APIs only for documentation.

## Framework fundamentals

| Example | What it demonstrates | Lab source |
| --- | --- | --- |
| [Counter](./counter.md) | Minimal resumable interaction | Framework example |
| [State and Resumable Handlers](./state-resumability.md) | `useState()`, multiple handler actions, lazy interaction | `pages/state.vue` |
| [Forms and `v-model`](./forms.md) | Inputs, select, checkbox, submit and reset state | `pages/forms.vue` |
| [API and Fetch](./api-and-fetch.md) | Server API calls and async data | Existing example |
| [Blog Routes](./blog.md) | File routes and dynamic pages | Existing example |
| [Auth Middleware](./auth-middleware.md) | Route middleware | Existing example |
| [Error Handling](./errors.md) | `useError()` and `createError()` | `pages/features/errors.vue` |
| [Device Detection](./device-detection.md) | `useDevice()` and `parseUserAgent()` | `pages/features/device.vue` |

## Runtime boundaries and performance

| Example | What it demonstrates | Lab source |
| --- | --- | --- |
| [Vue Island](./vue-island.md) | Keep Vue runtime ownership inside a nested widget | `pages/vue-island.vue`, `islands/vue/IslandCounter.vue` |
| [Performance Measurements](./performance.md) | Measure a state patch and repeated API requests in the browser | `pages/performance.vue` |
| [Progressive Package](./progressive-package.md) | Progressive client enhancement | Existing example |
| [Package Integrations](./package-integrations.md) | Visible, idle, interaction, immediate, page-load, manual and SSR package patterns | `pages/package-tests/` |

## Media and deployment

| Example | What it demonstrates | Lab source |
| --- | --- | --- |
| [Media Optimization](./media-optimization.md) | Image transformation and delivery | Existing example |
| [Media Placeholders and Picture](./media-placeholders.md) | Blur, skeleton, spinner, custom placeholders, picture formats and fallback images | `pages/media-test/images.vue` |
| [Docker Deployment](./docker.md) | Container deployment | Existing example |

## Use the lab as executable documentation

The compatibility lab is useful for more than screenshots. Its pages are exercised by end-to-end regression tests covering framework features, media, package integrations and layout behavior. When a docs example is marked **Lab-backed**, use the linked lab file as the executable reference and the documentation page as the explanation of why the pattern works.

- [Resux Lab repository](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab)
- [Live Resux Lab](https://resux-lab.vercel.app/)
- [Integration Cookbook](/guide/integration-cookbook)
- [Execution Contexts](/guide/execution-contexts)
