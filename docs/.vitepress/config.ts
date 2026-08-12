import { defineConfig } from 'vitepress'

const startHere = [
  { text: 'What is Resux?', link: '/guide/what-is-resux' },
  { text: 'Getting Started', link: '/guide/getting-started' },
  { text: 'Framework Tour', link: '/guide/framework-tour' },
  { text: 'Core Concepts', link: '/guide/core-concepts' },
  { text: 'Project Structure', link: '/guide/project-structure' },
  { text: 'Mental Model', link: '/guide/mental-model' }
]

const applicationGuide = [
  { text: 'Components', link: '/guide/components' },
  { text: 'Template Syntax', link: '/guide/template-syntax' },
  { text: 'State and Reactivity', link: '/guide/state' },
  { text: 'Async Data', link: '/guide/async-data' },
  { text: 'Routing', link: '/guide/routing' },
  { text: 'Layouts', link: '/guide/layouts' },
  { text: 'Head and SEO', link: '/guide/head-seo' },
  { text: 'Runtime Config', link: '/guide/runtime-config' }
]

const architectureGuide = [
  { text: 'Architecture Deep Dive', link: '/guide/architecture-deep-dive' },
  { text: 'Request Lifecycle', link: '/guide/request-lifecycle' },
  { text: 'Rendering Lifecycle', link: '/guide/rendering-lifecycle' },
  { text: 'Resumability Deep Dive', link: '/guide/resumability-deep-dive' },
  { text: 'Resumability and Handlers', link: '/guide/resumability-handlers' },
  { text: 'Code to Browser', link: '/guide/code-to-browser' },
  { text: 'Execution Contexts', link: '/guide/execution-contexts' },
  { text: 'Debugging Mental Model', link: '/guide/debugging-mental-model' }
]

const platformGuide = [
  { text: 'Plugins', link: '/guide/plugins' },
  { text: 'Middleware', link: '/guide/middleware' },
  { text: 'Server API', link: '/guide/server-api' },
  { text: 'Modules and Route Rules', link: '/guide/modules-route-rules' },
  { text: 'Third-party Packages', link: '/guide/package-integration' },
  { text: 'Integration Cookbook', link: '/guide/integration-cookbook' },
  { text: 'CSS and Tailwind', link: '/guide/css-tailwind' },
  { text: 'TypeScript and Generated Types', link: '/guide/typescript-generated-types' },
  { text: 'Testing and Quality', link: '/guide/testing-quality' }
]

const operationsGuide = [
  { text: 'i18n and Localization', link: '/guide/i18n' },
  { text: 'Vue Islands', link: '/guide/vue-islands' },
  { text: 'UI and Motion', link: '/guide/ui-animations' },
  { text: 'App Shell and Errors', link: '/guide/app-shell-errors' },
  { text: 'Security and Caching', link: '/guide/security-caching' },
  { text: 'Halal Core', link: '/guide/halal-core' },
  { text: 'Dev Server and Build Output', link: '/guide/dev-build-output' },
  { text: 'Deployment', link: '/guide/deployment' },
  { text: 'Troubleshooting', link: '/guide/troubleshooting' }
]

const componentForms = [
  { text: 'Button', link: '/components/button' },
  { text: 'Input', link: '/components/input' },
  { text: 'Textarea', link: '/components/textarea' },
  { text: 'Select', link: '/components/select' },
  { text: 'DatePicker', link: '/components/date-picker' },
  { text: 'Switch', link: '/components/switch' }
]

const componentContent = [
  { text: 'Card', link: '/components/card' },
  { text: 'Badge', link: '/components/badge' },
  { text: 'Avatar', link: '/components/avatar' },
  { text: 'Alert', link: '/components/alert' },
  { text: 'Skeleton', link: '/components/skeleton' },
  { text: 'Divider', link: '/components/divider' },
  { text: 'Kbd', link: '/components/kbd' }
]

const componentOverlays = [
  { text: 'Accordion', link: '/components/accordion' },
  { text: 'Tabs', link: '/components/tabs' },
  { text: 'Popover', link: '/components/popover' },
  { text: 'Dropdown', link: '/components/dropdown' },
  { text: 'Tooltip', link: '/components/tooltip' },
  { text: 'Modal', link: '/components/modal' }
]

const componentMotion = [
  { text: 'Motion', link: '/components/motion' },
  { text: 'Reveal', link: '/components/reveal' },
  { text: 'AutoAnimate', link: '/components/auto-animate' },
  { text: 'UI Icon', link: '/components/icon' }
]

const apiReference = [
  { text: 'Public API Index', link: '/reference/api-index' },
  { text: 'Package Exports', link: '/reference/packages' },
  { text: 'Composables and Globals', link: '/reference/composables' },
  { text: 'Reactivity API', link: '/reference/reactivity' },
  { text: 'UI Package API', link: '/reference/ui' },
  { text: 'i18n API', link: '/reference/i18n' },
  { text: 'Resux Kit API', link: '/reference/kit' },
  { text: 'Core API', link: '/reference/core' },
  { text: 'Lifecycle Hooks', link: '/reference/hooks' },
  { text: 'Runtime Internals', link: '/reference/runtime' },
  { text: 'Compiler API', link: '/reference/compiler' },
  { text: 'Project Creation API', link: '/reference/create' },
  { text: 'Node Handler API', link: '/reference/node' },
  { text: 'Halal Core API', link: '/reference/halal' },
  { text: 'CLI', link: '/reference/cli' },
  { text: 'Configuration', link: '/reference/configuration' },
  { text: 'File Conventions', link: '/reference/file-conventions' }
]

export default defineConfig({
  title: 'Resux',
  description: 'Professional, source-aligned documentation for the Resux resumable web framework.',
  base: '/resux-docs/',
  cleanUrls: true,
  lastUpdated: true,
  metaChunk: true,
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/resux-docs/logo-mark.svg' }],
    ['meta', { name: 'theme-color', content: '#0b0f19' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Resux Documentation' }],
    ['meta', { property: 'og:description', content: 'Learn Resux through guides, architecture deep dives, production examples, and exact public API reference.' }],
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
    outline: { level: [2, 3], label: 'On this page' },
    docFooter: { prev: 'Previous', next: 'Next' },
    lastUpdated: { text: 'Updated' },
    returnToTopLabel: 'Back to top',
    sidebarMenuLabel: 'Documentation',
    darkModeSwitchLabel: 'Appearance',
    nav: [
      {
        text: 'Learn',
        items: [
          { text: 'Getting Started', link: '/guide/getting-started' },
          { text: 'Framework Tour', link: '/guide/framework-tour' },
          { text: 'Core Concepts', link: '/guide/core-concepts' },
          { text: 'Architecture', link: '/guide/architecture-deep-dive' },
          { text: 'Resumability', link: '/guide/resumability-deep-dive' }
        ]
      },
      {
        text: 'Platform',
        items: [
          { text: 'UI Components', link: '/components/' },
          { text: 'Images and Video', link: '/media/' },
          { text: 'Fonts', link: '/fonts/' },
          { text: 'Icons', link: '/icons/' },
          { text: 'Deployment', link: '/guide/deployment' }
        ]
      },
      { text: 'Reference', link: '/reference/api-index' },
      { text: 'Examples', link: '/examples/counter' },
      {
        text: 'Ecosystem',
        items: [
          { text: 'npm package', link: 'https://www.npmjs.com/package/resuxjs' },
          { text: 'Framework source', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux' },
          { text: 'Compatibility lab', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux-lab' },
          { text: 'Docs source', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux-docs' }
        ]
      }
    ],
    sidebar: {
      '/guide/': [
        { text: 'Start Here', collapsed: false, items: startHere },
        { text: 'Build an Application', collapsed: false, items: applicationGuide },
        { text: 'Architecture and Runtime', collapsed: true, items: architectureGuide },
        { text: 'Platform and Extensions', collapsed: true, items: platformGuide },
        { text: 'Advanced and Operations', collapsed: true, items: operationsGuide }
      ],
      '/components/': [
        {
          text: 'UI Components',
          collapsed: false,
          items: [
            { text: 'Overview', link: '/components/' },
            { text: 'Component Anatomy', link: '/components/component-anatomy' }
          ]
        },
        { text: 'Forms and Input', collapsed: false, items: componentForms },
        { text: 'Content and Feedback', collapsed: true, items: componentContent },
        { text: 'Disclosure and Overlays', collapsed: true, items: componentOverlays },
        { text: 'Motion and Utility', collapsed: true, items: componentMotion },
        {
          text: 'Related',
          collapsed: true,
          items: [
            { text: 'UI Package API', link: '/reference/ui' },
            { text: 'UI and Motion Guide', link: '/guide/ui-animations' },
            { text: 'Vue Islands', link: '/guide/vue-islands' }
          ]
        }
      ],
      '/media/': [
        {
          text: 'Images and Media',
          collapsed: false,
          items: [
            { text: 'Overview', link: '/media/' },
            { text: 'Images', link: '/media/images' },
            { text: 'Responsive Images', link: '/media/responsive-images' },
            { text: 'Image Optimization', link: '/media/optimization' },
            { text: 'Video', link: '/media/video' }
          ]
        },
        {
          text: 'Related',
          collapsed: true,
          items: [
            { text: 'Media Example', link: '/examples/media-optimization' },
            { text: 'Deployment', link: '/guide/deployment' },
            { text: 'Security and Caching', link: '/guide/security-caching' }
          ]
        }
      ],
      '/fonts/': [
        {
          text: 'Fonts',
          collapsed: false,
          items: [
            { text: 'Overview', link: '/fonts/' },
            { text: 'Configuration', link: '/fonts/configuration' },
            { text: 'Performance and CSP', link: '/fonts/performance' }
          ]
        },
        {
          text: 'Related',
          collapsed: true,
          items: [
            { text: 'CSS and Tailwind', link: '/guide/css-tailwind' },
            { text: 'Performance', link: '/guide/security-caching' }
          ]
        }
      ],
      '/icons/': [
        {
          text: 'Icons',
          collapsed: false,
          items: [
            { text: 'Overview', link: '/icons/' },
            { text: 'Usage and Registry', link: '/icons/usage' },
            { text: 'Configuration', link: '/icons/configuration' },
            { text: 'Runtime Loading', link: '/icons/runtime' }
          ]
        },
        {
          text: 'Related',
          collapsed: true,
          items: [
            { text: 'UI Icon Primitive', link: '/components/icon' },
            { text: 'UI Components', link: '/components/' }
          ]
        }
      ],
      '/reference/': [
        { text: 'API Reference', collapsed: false, items: apiReference },
        {
          text: 'Implementation and Coverage',
          collapsed: true,
          items: [
            { text: 'Documentation Coverage', link: '/reference/coverage' },
            { text: 'Framework Source Map', link: '/reference/source-map' },
            { text: 'Current Limits', link: '/reference/limits' },
            { text: 'Release and Publishing', link: '/reference/release' }
          ]
        }
      ],
      '/examples/': [
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
        }
      ],
      '/community/': [
        {
          text: 'Project',
          collapsed: false,
          items: [
            { text: 'Contributing to Docs', link: '/community/contributing' },
            { text: 'Brand System', link: '/brand' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/MahmoudAbdalrhmanMohamed/resux' }
    ],
    footer: {
      message: 'Source-aligned documentation for the Resux resumable web framework.',
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
