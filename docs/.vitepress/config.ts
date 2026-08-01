import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Resux',
  description: 'Complete documentation for the Resux compiler, SSR and resumable runtime, application platform, modules, packages, media, deployment, and safety tooling.',
  base: '/resux-docs/',
  cleanUrls: true,
  lastUpdated: true,
  metaChunk: true,
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/resux-docs/logo-mark.svg' }],
    ['meta', { name: 'theme-color', content: '#111827' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Resux Documentation' }],
    ['meta', { property: 'og:description', content: 'Learn the complete Resux framework: compiler, resumability, routing, server APIs, modules, packages, media, deployment, and safety.' }],
    ['meta', { property: 'og:image', content: 'https://mahmoudabdalrhmanmohamed.github.io/resux-docs/og-image.png' }],
    ['meta', { property: 'og:image:type', content: 'image/png' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:image', content: 'https://mahmoudabdalrhmanmohamed.github.io/resux-docs/og-image.png' }]
  ],
  themeConfig: {
    logo: '/logo-mark.svg',
    siteTitle: 'Resux',
    search: { provider: 'local' },
    nav: [
      { text: 'Guide', link: '/guide/framework-tour' },
      { text: 'Reference', link: '/reference/api-index' },
      { text: 'Examples', link: '/examples/counter' },
      { text: 'Brand', link: '/brand' },
      {
        text: 'Links',
        items: [
          { text: 'npm package', link: 'https://www.npmjs.com/package/resuxjs' },
          { text: 'Source repo', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux' },
          { text: 'Docs repo', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux-docs' }
        ]
      }
    ],
    sidebar: [
      {
        text: 'Start Here',
        collapsed: false,
        items: [
          { text: 'Framework Tour', link: '/guide/framework-tour' },
          { text: 'What is Resux?', link: '/guide/what-is-resux' },
          { text: 'Core Concepts', link: '/guide/core-concepts' },
          { text: 'Getting Started', link: '/guide/getting-started' },
          { text: 'Execution Contexts', link: '/guide/execution-contexts' },
          { text: 'Project Structure', link: '/guide/project-structure' },
          { text: 'Mental Model', link: '/guide/mental-model' }
        ]
      },
      {
        text: 'Application Guide',
        collapsed: false,
        items: [
          { text: 'Rendering Lifecycle', link: '/guide/rendering-lifecycle' },
          { text: 'Resumability and Handlers', link: '/guide/resumability-handlers' },
          { text: 'App Shell and Errors', link: '/guide/app-shell-errors' },
          { text: 'Components', link: '/guide/components' },
          { text: 'Template Syntax', link: '/guide/template-syntax' },
          { text: 'State and Reactivity', link: '/guide/state' },
          { text: 'Async Data', link: '/guide/async-data' },
          { text: 'Routing', link: '/guide/routing' },
          { text: 'Layouts', link: '/guide/layouts' },
          { text: 'Head and SEO', link: '/guide/head-seo' },
          { text: 'Runtime Config', link: '/guide/runtime-config' }
        ]
      },
      {
        text: 'Platform and Extension',
        collapsed: false,
        items: [
          { text: 'Plugins', link: '/guide/plugins' },
          { text: 'Middleware', link: '/guide/middleware' },
          { text: 'Server API', link: '/guide/server-api' },
          { text: 'Modules and Route Rules', link: '/guide/modules-route-rules' },
          { text: 'Third-party Packages', link: '/guide/package-integration' },
          { text: 'CSS and Tailwind', link: '/guide/css-tailwind' },
          { text: 'TypeScript and Generated Types', link: '/guide/typescript-generated-types' },
          { text: 'Testing and Quality', link: '/guide/testing-quality' }
        ]
      },
      {
        text: 'Optional Features',
        collapsed: false,
        items: [
          { text: 'Media and Optimization', link: '/guide/media' },
          { text: 'Icons', link: '/guide/icons' },
          { text: 'Fonts', link: '/guide/fonts' },
          { text: 'i18n and Localization', link: '/guide/i18n' },
          { text: 'UI and Motion', link: '/guide/ui-animations' },
          { text: 'Vue Islands', link: '/guide/vue-islands' }
        ]
      },
      {
        text: 'Operations and Safety',
        collapsed: false,
        items: [
          { text: 'Security and Caching', link: '/guide/security-caching' },
          { text: 'Halal Core', link: '/guide/halal-core' },
          { text: 'Dev Server and Build Output', link: '/guide/dev-build-output' },
          { text: 'Deployment', link: '/guide/deployment' },
          { text: 'Troubleshooting', link: '/guide/troubleshooting' }
        ]
      },
      {
        text: 'Reference',
        collapsed: false,
        items: [
          { text: 'Package Exports', link: '/reference/packages' },
          { text: 'Public API Index', link: '/reference/api-index' },
          { text: 'CLI', link: '/reference/cli' },
          { text: 'Composables and Globals', link: '/reference/composables' },
          { text: 'Configuration', link: '/reference/configuration' },
          { text: 'File Conventions', link: '/reference/file-conventions' },
          { text: 'Lifecycle Hooks', link: '/reference/hooks' },
          { text: 'Runtime Internals', link: '/reference/runtime' },
          { text: 'Compiler Internals', link: '/reference/compiler' },
          { text: 'Release and Publishing', link: '/reference/release' },
          { text: 'Current Limits', link: '/reference/limits' }
        ]
      },
      {
        text: 'Examples',
        collapsed: false,
        items: [
          { text: 'Counter', link: '/examples/counter' },
          { text: 'Blog Routes', link: '/examples/blog' },
          { text: 'API and Fetch', link: '/examples/api-and-fetch' },
          { text: 'Auth Middleware', link: '/examples/auth-middleware' },
          { text: 'Progressive Package', link: '/examples/progressive-package' },
          { text: 'Media Optimization', link: '/examples/media-optimization' },
          { text: 'Docker Deployment', link: '/examples/docker' }
        ]
      },
      {
        text: 'Project',
        collapsed: false,
        items: [
          { text: 'Brand System', link: '/brand' },
          { text: 'Contributing to Docs', link: '/community/contributing' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux' }
    ],
    footer: {
      message: 'Complete Resux source-aligned documentation with stable and experimental boundaries documented explicitly.',
      copyright: 'Copyright (c) 2026 Resux contributors'
    },
    editLink: {
      pattern: 'https://github.com/MahmoudAbdalrhmanMohamed/resux-docs/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    }
  },
  markdown: {
    theme: { light: 'github-light', dark: 'github-dark' },
    lineNumbers: true
  }
})
