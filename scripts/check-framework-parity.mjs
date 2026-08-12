import { existsSync, readFileSync } from 'node:fs'
import path from 'node:path'

const docsRoot = path.resolve('docs')
const frameworkRoot = path.resolve(
  process.argv[2] || process.env.RESUX_FRAMEWORK_ROOT || '.framework/resux'
)
const packagePath = path.join(frameworkRoot, 'package.json')

if (!existsSync(packagePath)) {
  console.error(`Framework package.json not found at ${packagePath}`)
  console.error('Pass the Resux checkout path as the first argument or set RESUX_FRAMEWORK_ROOT.')
  process.exit(1)
}

const frameworkPackage = JSON.parse(readFileSync(packagePath, 'utf8'))
const packageName = frameworkPackage.name
const exportMap = frameworkPackage.exports || {}

if (typeof packageName !== 'string' || !packageName) {
  console.error('Framework package.json is missing a valid package name.')
  process.exit(1)
}

const publicSpecifiers = Object.keys(exportMap)
  .filter((key) => key === '.' || key.startsWith('./'))
  .map((key) => key === '.' ? packageName : `${packageName}/${key.slice(2)}`)
  .sort()

const coverageFiles = [
  'docs/reference/packages.md',
  'docs/reference/coverage.md'
]

const expectedDestinations = new Map([
  [packageName, 'docs/reference/api-index.md'],
  [`${packageName}/node`, 'docs/reference/node.md'],
  [`${packageName}/globals`, 'docs/reference/composables.md'],
  [`${packageName}/runtime`, 'docs/reference/runtime.md'],
  [`${packageName}/reactivity`, 'docs/reference/reactivity.md'],
  [`${packageName}/compiler`, 'docs/reference/compiler.md'],
  [`${packageName}/create`, 'docs/reference/create.md'],
  [`${packageName}/i18n`, 'docs/reference/i18n.md'],
  [`${packageName}/ui`, 'docs/reference/ui.md'],
  [`${packageName}/icons`, 'docs/icons/index.md'],
  [`${packageName}/fonts`, 'docs/fonts/index.md'],
  [`${packageName}/kit`, 'docs/reference/kit.md'],
  [`${packageName}/core`, 'docs/reference/core.md'],
  [`${packageName}/halal`, 'docs/reference/halal.md'],
  [`${packageName}/package.json`, 'docs/reference/packages.md']
])

const failures = []

for (const coverageFile of coverageFiles) {
  const absolutePath = path.resolve(coverageFile)
  if (!existsSync(absolutePath)) {
    failures.push(`${coverageFile} does not exist.`)
    continue
  }

  const source = readFileSync(absolutePath, 'utf8')
  const missing = publicSpecifiers.filter((specifier) => !source.includes(`\`${specifier}\``))

  if (missing.length > 0) {
    failures.push(`${coverageFile} is missing exports: ${missing.join(', ')}`)
  }
}

for (const specifier of publicSpecifiers) {
  const destination = expectedDestinations.get(specifier)

  if (!destination) {
    failures.push(`No documentation destination is mapped for public export ${specifier}.`)
    continue
  }

  if (!existsSync(path.resolve(destination))) {
    failures.push(`Documentation destination for ${specifier} does not exist: ${destination}`)
  }
}

for (const [specifier, destination] of expectedDestinations) {
  if (!publicSpecifiers.includes(specifier)) {
    failures.push(`Stale documentation mapping: ${specifier} -> ${destination} is no longer a public package export.`)
  }
}

const requiredLandingPages = [
  'index.md',
  'guide/getting-started.md',
  'guide/framework-tour.md',
  'guide/architecture-deep-dive.md',
  'components/index.md',
  'media/index.md',
  'fonts/index.md',
  'icons/index.md',
  'reference/api-index.md',
  'reference/coverage.md',
  'reference/source-map.md'
]

for (const relativePath of requiredLandingPages) {
  const absolutePath = path.join(docsRoot, relativePath)
  if (!existsSync(absolutePath)) {
    failures.push(`Required documentation landing page is missing: docs/${relativePath}`)
  }
}

if (failures.length > 0) {
  console.error('Framework/docs parity check failed:')
  for (const failure of failures) {
    console.error(`  - ${failure}`)
  }
  process.exit(1)
}

console.log(`Framework/docs parity OK: ${publicSpecifiers.length} public export specifiers are covered and mapped to documentation pages.`)
