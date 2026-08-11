import { existsSync, readFileSync } from 'node:fs'
import path from 'node:path'

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

const documentationFiles = [
  'docs/reference/packages.md',
  'docs/reference/coverage.md'
]

const failures = []

for (const documentationFile of documentationFiles) {
  const source = readFileSync(path.resolve(documentationFile), 'utf8')
  const missing = publicSpecifiers.filter((specifier) => !source.includes(`\`${specifier}\``))

  if (missing.length > 0) {
    failures.push({ documentationFile, missing })
  }
}

if (failures.length > 0) {
  for (const failure of failures) {
    console.error(`Missing framework exports in ${failure.documentationFile}:`)
    for (const specifier of failure.missing) {
      console.error(`  - ${specifier}`)
    }
  }
  process.exit(1)
}

console.log(`Framework/docs package parity OK: ${publicSpecifiers.length} public export specifiers covered.`)
