import { readdirSync, readFileSync, statSync } from 'node:fs'
import path from 'node:path'

const docsRoot = path.resolve('docs')
const configPath = path.join(docsRoot, '.vitepress', 'config.ts')
const configSource = readFileSync(configPath, 'utf8')

function collectMarkdownFiles(directory) {
  const files = []

  for (const entry of readdirSync(directory)) {
    if (entry === '.vitepress' || entry === 'public') continue

    const absolute = path.join(directory, entry)
    const stats = statSync(absolute)

    if (stats.isDirectory()) {
      files.push(...collectMarkdownFiles(absolute))
    } else if (entry.endsWith('.md')) {
      files.push(absolute)
    }
  }

  return files
}

function routeForFile(file) {
  const relative = path.relative(docsRoot, file).replaceAll(path.sep, '/')

  if (relative === 'index.md') return '/'
  if (relative.endsWith('/index.md')) {
    return `/${relative.slice(0, -'index.md'.length)}`
  }

  return `/${relative.slice(0, -'.md'.length)}`
}

const markdownFiles = collectMarkdownFiles(docsRoot)
const failures = []

if (!configSource.includes('sidebar: globalSidebar')) {
  failures.push({
    file: 'docs/.vitepress/config.ts',
    route: 'themeConfig.sidebar must use globalSidebar so every section is visible from every page'
  })
}

for (const file of markdownFiles) {
  const route = routeForFile(file)
  const singleQuoted = `'${route}'`
  const doubleQuoted = `"${route}"`

  if (!configSource.includes(singleQuoted) && !configSource.includes(doubleQuoted)) {
    failures.push({
      file: path.relative(process.cwd(), file).replaceAll(path.sep, '/'),
      route
    })
  }
}

if (failures.length > 0) {
  console.error('Documentation pages missing from the global VitePress navigation:')
  for (const failure of failures) {
    console.error(`  - ${failure.file} -> ${failure.route}`)
  }
  console.error('Keep themeConfig.sidebar global and add every docs route to docs/.vitepress/config.ts.')
  process.exit(1)
}

console.log(`Global documentation sidebar coverage OK: all ${markdownFiles.length} Markdown pages are linked.`)
