import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Resux',
  description: 'Resumable web framework with a stable v1 core, Vue-like SFCs, and zero default hydration.',
  base: '/resux-docs/',
  cleanUrls: true,
  lastUpdated: true,
  metaChunk: true,
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/resux-docs/logo-mark.svg' }],
    ['meta', { name: 'theme-color', content: '#111827' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Resux Documentation' }],
    ['meta', { property: 'og:description', content: 'Build server-rendered Vue-like apps that resume only when users interact.' }],
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
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Guide', link: '/guide/what-is-resux' },
      { text: 'Reference', link: '/reference/cli' },
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
          { text: 'What is Resux?', link: '/guide/what-is-resux' },
          { text: 'Core Concepts', link: '/guide/core-concepts' },
          { text: 'Getting Started', link: '/guide/getting-started' },
          { text: 'Execution Contexts', link: '/guide/execution-contexts' },
          { text: 'Project Structure', link: '/guide/project-structure' },
          { text: 'Mental Model', link: '/guide/mental-model' }
        ]
      },
      {
        text: 'Core Guide',
        collapsed: false,
        items: [
          { text: 'Rendering Lifecycle', link: '/guide/rendering-lifecycle' },
          { text: 'Resumability and Handlers', link: '/guide/resumability-handlers' },
          { text: 'App Shell and Errors', link: '/guide/app-shell-errors' },
          { text: 'Components', link: '/guide/components' },
          { text: 'Template Syntax', link: '/guide/template-syntax' },
          { text: 'State', link: '/guide/state' },
          { text: 'Async Data', link: '/guide/async-data' },
          { text: 'Routing', link: '/guide/routing' },
          { text: 'Layouts', link: '/guide/layouts' },
          { text: 'Head and SEO', link: '/guide/head-seo' },
          { text: 'Runtime Config', link: '/guide/runtime-config' },
          { text: 'Plugins', link: '/guide/plugins' },
          { text: 'Middleware', link: '/guide/middleware' },
          { text: 'Server API', link: '/guide/server-api' },
          { text: 'Modules and Route Rules', link: '/guide/modules-route-rules' },
          { text: 'Security and Caching', link: '/guide/security-caching' },
          { text: 'Dev Server and Build Output', link: '/guide/dev-build-output' },
          { text: 'Vue Islands', link: '/guide/vue-islands' },
          { text: 'Deployment', link: '/guide/deployment' },
          { text: 'Troubleshooting', link: '/guide/troubleshooting' }
        ]
      },
      {
        text: 'Reference',
        collapsed: false,
        items: [
          { text: 'CLI', link: '/reference/cli' },
          { text: 'Composables and Globals', link: '/reference/composables' },
          { text: 'Release and Publishing', link: '/reference/release' },
          { text: 'Configuration', link: '/reference/configuration' },
          { text: 'File Conventions', link: '/reference/file-conventions' },
          { text: 'Runtime Internals', link: '/reference/runtime' },
          { text: 'Compiler Internals', link: '/reference/compiler' },
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
      message: 'Stable v1 core docs for Resux, with experimental areas clearly marked.',
      copyright: 'Copyright (c) 2026 Resux contributors'
    },
    editLink: {
      pattern: 'https://github.com/MahmoudAbdalrhmanMohamed/resux-docs/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    }
  },
  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    },
    lineNumbers: true
  }
})
