# Halal Core API (`resuxjs/halal`)

`resuxjs/halal` re-exports Resux Halal Core's programmatic policy, scanner/evaluator, lifecycle enforcement, runtime-content guard, signed review-memory, AI-classification, integrity, CLI-runner, and reporting utilities.

Read [Resux Halal Core](/guide/halal-core) first for the status model, guard lifecycle, report signing, review workflow, security model, limitations, and the important statement that this subsystem is software policy tooling—not a fatwa or religious certification.

::: warning Environment
Most project-scanning, report, enforcement, configuration-loading, integrity, and CLI APIs are Node/server/build tooling. Runtime-content evaluation can call a configured remote AI endpoint. Do not bundle this package wholesale into browser code.
:::

## Status types

```ts
type HalalGuardStatus =
  | 'allowed'
  | 'warning'
  | 'review_required'
  | 'blocked'

interface HalalCheckResult {
  status: HalalGuardStatus
  riskLevel: 'low' | 'medium' | 'high' | 'critical'
  categories: string[]
  confidence: number
  reasons: string[]
  matchedFiles: string[]
  matchedSnippets: string[]
  recommendedAction: string
  explanation?: string
  signature?: string
  createdDate?: string
}
```

Do not interpret `confidence` as religious/legal certainty; it is an evaluator/classifier confidence field.

## Policy API

### Main types

```ts
interface ReviewContact {
  name: string
  email: string
}

interface ReviewEvidence {
  type: string
  path: string
  description: string
}

interface StricterRules {
  blockAiChatWithoutModeration?: boolean
  blockUnmoderatedUserUploads?: boolean
  [key: string]: boolean | undefined
}

interface HalalAIConfig {
  enabled?: boolean
  strict?: boolean
  blockProductionBuild?: boolean
  scanRoutes?: boolean
  scanMeta?: boolean
  scanContent?: boolean
  scanExternalLinks?: boolean
  scanRuntimeConfig?: boolean
  scanDependencies?: boolean
  categories?: Record<string, 'block' | 'warn' | 'review' | 'allow'>
}

interface ResuxHalalPolicy {
  projectName?: string
  projectType?: string
  description?: string
  reviewContact?: ReviewContact
  stricterRules?: StricterRules
  additionalBlockedCategories?: string[]
  evidence?: ReviewEvidence[]
  internalTeamNotes?: string
  halalAI?: HalalAIConfig
}
```

### `defineResuxHalalPolicy()`

```ts
function defineResuxHalalPolicy(
  config: ResuxHalalPolicy
): ResuxHalalPolicy
```

The helper validates the policy and returns it. It is not a no-op identity helper because validation rejects configured attempts to disable/bypass protected core behavior.

```ts
import { defineResuxHalalPolicy } from 'resuxjs/halal'

export default defineResuxHalalPolicy({
  projectName: 'Education portal',
  projectType: 'education',
  halalAI: {
    strict: true
  }
})
```

### `validatePolicyConfig()`

```ts
function validatePolicyConfig(
  config: Record<string, any>
): ResuxHalalPolicy
```

Rejected top-level bypass fields currently include `enabled`, `mode`, `ignoreCoreRules`, `allowBlockedCategories`, `disableHarmDetection`, `removeDefaultRules`, and `halalGuard`. `halalAI.enabled: false` is also rejected by the current validator.

### Configuration loaders

```ts
function loadMainResuxConfig(
  appRoot: string
): Promise<Record<string, any>>

function loadProjectPolicy(
  appRoot: string
): Promise<ResuxHalalPolicy>
```

`loadProjectPolicy()` combines supported main-config context with the first found `resux.halal.config.ts|js|mjs`, then validates the result.

## Project scanner and rule evaluator

### `scanProject()`

```ts
function scanProject(appRoot: string): {
  routes: string[]
  pages: string[]
  components: string[]
  apiRoutes: unknown
  metadata: unknown
  envNames: string[]
  dependencies: Record<string, string>
  i18nWords: string[]
  contentTexts: Array<{ file: string; text: string }>
  endpoints: string[]
}
```

The exact subordinate scanner result types are inferred from their implementations; callers should normally pass the returned object directly to `evaluateRules()` rather than depending on undocumented extra scanner fields.

The scanner reads `.gitignore` through the exported `getGitignoredPaths(appRoot)` helper in its implementation module, while the package entry point explicitly exports `scanProject`.

### `evaluateRules()`

```ts
function evaluateRules(
  scannedData: {
    routes: string[]
    pages: string[]
    components: string[]
    metadata: {
      title?: string
      description?: string
      meta?: Record<string, string>
    }
    envNames: string[]
    dependencies: Record<string, string>
    i18nWords: string[]
    contentTexts: Array<{ file: string; text: string }>
    endpoints: string[]
  },
  policy: ResuxHalalPolicy
): HalalCheckResult
```

Use `scanProject()` + `evaluateRules()` when you need the same local scanner/rule engine programmatically without running a guard that may terminate the process.

## Lifecycle enforcement

```ts
function enforceDevGuard(
  appRoot: string,
  outDir: string
): Promise<void>

function enforceBuildGuard(
  appRoot: string,
  outDir: string
): Promise<void>

function enforcePreviewGuard(outDir: string): void
function enforceProductionServerGuard(outDir: string): void
function enforceDeploymentGuard(outDir: string): void
```

These functions are enforcement APIs, not pure validators. Outside the detected test environment they can print reports/errors and call `process.exit(1)` when integrity, report verification, policy status, strict mode, or review approval blocks the requested operation.

Production-server and deployment guards require authenticated on-disk report verification. See the [Halal Core guide](/guide/halal-core#report-integrity-and-authentication).

### `registerHalalCoreHooks()`

```ts
function registerHalalCoreHooks(
  hooks: any,
  appRoot: string,
  outDir: string
): void
```

The helper registers build/dev guard callbacks when the supplied object exposes `hook()`. This is a low-level integration helper; normal framework commands already run the appropriate guard paths.

## Runtime-content API

### Content and option types

```ts
type HalalRuntimeContentKind =
  | 'dynamic_page'
  | 'advertisement'
  | 'api_response'
  | 'user_content'

interface HalalRuntimeContent {
  id?: string
  kind: HalalRuntimeContentKind
  route?: string
  title?: string
  text?: string
  url?: string
  advertiser?: string
  payload?: unknown
  metadata?: Record<string, unknown>
}

interface HalalRuntimeAiOptions {
  enabled?: boolean
  endpoint?: string
  apiKey?: string
  model?: string
  requireForAds?: boolean
  requireForDynamicContent?: boolean
}

interface HalalRuntimeGuardOptions {
  policy?: ResuxHalalPolicy
  strict?: boolean
  ai?: HalalRuntimeAiOptions
  reviewSecret?: string
  reviewedDecisions?: SignedHalalRuntimeDecision[]
  maxContentCharacters?: number
}
```

### `evaluateHalalRuntimeContent()`

```ts
function evaluateHalalRuntimeContent(
  content: HalalRuntimeContent,
  options?: HalalRuntimeGuardOptions
): Promise<HalalRuntimeDecision>
```

The evaluator:

1. canonically serializes/inspects the runtime content;
2. calculates a SHA-256 content fingerprint;
3. runs local project-style rules over the normalized content/route/domain data;
4. escalates truncated/uninspectable content to review requirements;
5. checks valid signed reviewed-memory decisions;
6. short-circuits local blocked results;
7. optionally uses the runtime AI classifier;
8. finalizes `allowed` according to status and strict mode.

Advertisements require AI unless `requireForAds` is explicitly false; other content requires it only when `requireForDynamicContent` is true. If required verification is unavailable, the current result becomes `review_required` rather than silently allowed.

### `createHalalRuntimeGuard()`

```ts
function createHalalRuntimeGuard(
  options?: HalalRuntimeGuardOptions
): {
  check(content: HalalRuntimeContent): Promise<HalalRuntimeDecision>
  checkDynamicPage(content: Omit<HalalRuntimeContent, 'kind'>): Promise<HalalRuntimeDecision>
  checkAd(content: Omit<HalalRuntimeContent, 'kind'>): Promise<HalalRuntimeDecision>
  assertAllowed(content: HalalRuntimeContent): Promise<HalalRuntimeDecision>
  filterAds<T extends Omit<HalalRuntimeContent, 'kind'>>(
    ads: readonly T[]
  ): Promise<{
    allowed: T[]
    rejected: Array<{ ad: T; decision: HalalRuntimeDecision }>
  }>
}
```

`assertAllowed()` throws `HalalRuntimeBlockedError`, whose `decision` field contains the rejected decision.

## Runtime serialization

```ts
type RuntimeContentInspectionIssue =
  | 'max_depth'
  | 'unreadable_object'
  | 'unreadable_property'

interface PreparedRuntimeContent {
  canonical: string
  localText: string
  aiText: string
  truncated: boolean
  maxCharacters: number
  inspectionIssues: RuntimeContentInspectionIssue[]
}

function serializeRuntimeContent(
  content: HalalRuntimeContent,
  maxCharacters?: number
): string

function prepareRuntimeContent(
  content: HalalRuntimeContent,
  maxCharacters?: number
): PreparedRuntimeContent

function serializeRuntimeContentCanonical(
  content: HalalRuntimeContent
): string
```

The default scan limit is 20,000 characters. AI text is redacted before truncation; local text comes from canonical content before AI redaction. Canonical serialization has bounded depth and records uninspectable content instead of silently pretending every object was fully read.

## Signed reviewed memory

```ts
interface HalalRuntimeReviewInput {
  status: 'allowed' | 'warning' | 'review_required' | 'blocked'
  categories?: string[]
  reason: string
  reviewerId: string
  expiresAt?: string
}

function createRuntimeContentFingerprint(
  content: HalalRuntimeContent,
  maxContentCharacters?: number
): string

function createSignedHalalRuntimeDecision(
  content: HalalRuntimeContent,
  review: HalalRuntimeReviewInput,
  secret?: string
): SignedHalalRuntimeDecision

function verifySignedHalalRuntimeDecision(
  decision: unknown,
  secret?: string
): decision is SignedHalalRuntimeDecision

function findReviewedRuntimeDecision(
  content: HalalRuntimeContent,
  decisions: readonly SignedHalalRuntimeDecision[] | undefined,
  secret?: string,
  maxContentCharacters?: number
): SignedHalalRuntimeDecision | undefined
```

The runtime review secret environment name is `RESUX_HALAL_REVIEW_SECRET`. Signed runtime decisions are content-fingerprint-specific; verification also validates schema, timestamps/expiry, and signature. Do not reuse this mechanism as a generic application signing API.

## Runtime AI classifier

```ts
function classifyRuntimeContentWithAi(
  content: HalalRuntimeContent,
  serializedContent: string,
  localResult: HalalCheckResult,
  options?: HalalRuntimeAiOptions
): Promise<HalalCheckResult | null>
```

The classifier uses an explicit/configured endpoint/API key (or the framework's environment variables), validates the endpoint, enforces a timeout, sends redacted/serialized content plus local findings, validates the returned JSON classification, and fails closed to a review requirement when AI is required and the request/configuration fails.

Never expose the AI API key in public runtime config or browser bundles.

## Integrity

```ts
function verifyCoreIntegrity(appRoot: string): boolean
```

The current check verifies presence of critical Halal Core source/runtime files in the installed framework tree. A false result is used by dev/build enforcement to stop the protected command.

## CLI and reporting utility exports

The package also explicitly exports command-runner/utility functions used by the framework CLI and developer tooling:

- `runHalalCheck`
- `runHalalReport`
- `runHalalExplain`
- `runHalalSubmitReview`
- `runHalalVerifyReview`
- `formatBrowserOverlayScript`

These are CLI/report integration surfaces. Prefer the documented `resux halal ...` commands unless you are building CLI tooling around Resux; do not call them from page/component/browser code.

## Security notes

- Project scanners and guards can access local project files; run them only against intended application roots.
- Runtime AI configuration can contain an API key; keep it server-side.
- Signed review secrets are authentication material; store them in secret management, never source control/client config.
- A valid signature proves knowledge of the configured secret, not reviewer qualifications.
- Local/AI policy classification can have false positives/negatives and contextual cases still require qualified review.

## Related

- [Halal Core guide](/guide/halal-core)
- [CLI](./cli.md)
- [Security and Caching](/guide/security-caching)
- [Core API](./core.md)
- [Node Handler](./node.md)
