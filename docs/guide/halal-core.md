# Resux Halal Core

Resux Halal Core is a framework-level project policy and safety subsystem. It scans a project, evaluates configured rules, produces reports, and can block development, builds, production startup, or deployment when the result requires action.

It is **not** an official Islamic fatwa, a religious certification, or a substitute for a qualified human reviewer. It is automated software-policy tooling with an explicit human-review path for uncertain cases.

## What it scans

The local scanner can inspect project information such as:

- page, component, server, and route file names
- supported source-text samples
- project metadata and policy description
- package names and dependencies
- routes and server endpoints
- environment variable **names**, not secret values
- configured evidence supplied by the project owner

Scanner safety behavior includes:

- binary and ignored files are skipped
- symbolic links are not followed
- traversal is constrained to the application root
- large text files are read only up to a bounded sample
- sensitive-looking values are redacted before optional remote classification

## Status model

Every evaluation returns one of four statuses:

| Status | Meaning | Default effect |
| --- | --- | --- |
| `allowed` | No blocking rule was detected | Continue |
| `warning` | A concern was detected but is not automatically blocked | Continue unless strict mode is enabled |
| `review_required` | Context is ambiguous and a signed human approval is required | Stop development/build until approval is valid |
| `blocked` | The project matches a blocking rule | Stop according to the active guard policy |

A result also includes a risk level, confidence value, categories, reasons, matched files/snippets, and a recommended action.

## When guards run

- `resux dev` runs a local project check before starting development.
- `resux build` scans the project and generates a report.
- `resux preview` verifies the report stored in the build output.
- Production server startup requires an authenticated report.
- Deployment guard validation requires an authenticated report.

Tests bypass process-exit enforcement when the framework detects its test environment.

## Generated reports

A build report is written to the selected output directory, normally `.resux`:

```txt
.resux/
  halal-report.json
  halal-report.md
```

`halal-report.json` is intended for tooling and deployment checks. `halal-report.md` is a readable summary.

Typical JSON shape:

```json
{
  "status": "review_required",
  "riskLevel": "high",
  "categories": ["example-category"],
  "confidence": 0.82,
  "reasons": ["The project needs contextual review."],
  "matchedFiles": ["pages/example.vue"],
  "matchedSnippets": ["redacted sample"],
  "recommendedAction": "Submit a review request.",
  "createdDate": "2026-08-01T00:00:00.000Z",
  "signature": "hmac-sha256:..."
}
```

Do not treat the confidence score as a religious or legal certainty. It describes classifier confidence only.

## Report integrity and authentication

Two signature modes exist:

- `sha256:` is an unkeyed checksum suitable for detecting accidental/local report edits.
- `hmac-sha256:` is an authenticated signature created with a private secret.

Production server and deployment guards require authenticated HMAC reports. Configure a secret with at least 32 characters before producing the production artifact:

```sh
export RESUX_HALAL_REPORT_SIGNING_SECRET="replace-with-a-long-random-private-secret"
```

Keep the same secret available wherever the production report is verified. Store it in CI/deployment secrets, never in source control or client runtime configuration.

The signature covers the complete report payload. Editing the status, reasons, categories, files, timestamp, or any other signed field invalidates verification.

## `review_required`: what actually happens

`review_required` does **not** currently email you, upload the project, create a GitHub issue, or contact a central Resux service.

The current workflow is local and manual:

1. The command prints the report and stops the protected action.
2. The developer runs:

   ```sh
   resux halal submit-review
   ```

3. Resux creates a local request bundle, normally:

   ```txt
   .resux/halal-review-request.json
   ```

4. The developer sends that file to the organization or person responsible for review.
5. The reviewer returns a signed file named:

   ```txt
   halal-review-approval.json
   ```

6. The developer places the approval in the application root.
7. Resux verifies the signature and review context before allowing the project to continue.

The request bundle includes project metadata, review contact details, evidence, a generated project summary, and a timestamp. It should be reviewed before sharing because it may still contain project information even though sensitive values are redacted.

## Review approval signing

Review approvals use a different secret from report signing:

```sh
export RESUX_HALAL_REVIEW_SIGNING_SECRET="replace-with-another-long-random-secret"
```

The secret must be at least 32 characters. Do not reuse the report secret.

Approval verification checks the signature and relevant context such as status, project identity/evidence context, and expiry. Invalid, expired, malformed, or mismatched approvals fail closed.

Verify a received approval with:

```sh
resux halal verify-review
```

## Project policy

Create `resux.halal.config.ts` when project context or a review contact must be declared:

```ts
import { defineResuxHalalPolicy } from 'resuxjs'

export default defineResuxHalalPolicy({
  projectName: 'Security Education Portal',
  projectType: 'education',
  description: 'A defensive training site explaining common attacks and prevention.',
  reviewContact: {
    name: 'Compliance lead',
    email: 'compliance@example.com'
  },
  evidence: [
    'The content is educational and does not provide operational abuse tooling.'
  ],
  halalAI: {
    strict: true,
    blockProductionBuild: true
  }
})
```

Policy configuration may make enforcement stricter. Core blocking behavior is not intended to be disabled through project configuration.

## Optional AI-assisted classification

The default evaluator is local-first. Optional remote AI classification must be explicitly configured.

Security requirements include:

- HTTPS endpoints are required; plain HTTP is permitted only for localhost development.
- URL credentials are rejected.
- requests have a timeout
- malformed or invalid responses fail closed
- secrets, bearer tokens, JWT-like values, passwords, API keys, private keys, and credential-bearing URLs are redacted

The timeout can be configured in milliseconds:

```sh
export RESUX_AI_TIMEOUT_MS=15000
```

Only send project summaries to a service you trust. Redaction reduces risk but cannot guarantee that every sensitive business detail is removed.

## CI example

```yaml
- name: Install
  run: npm ci

- name: Build Resux application
  env:
    RESUX_HALAL_REPORT_SIGNING_SECRET: ${{ secrets.RESUX_HALAL_REPORT_SIGNING_SECRET }}
    RESUX_HALAL_REVIEW_SIGNING_SECRET: ${{ secrets.RESUX_HALAL_REVIEW_SIGNING_SECRET }}
  run: npm run build
```

Do not expose these secrets to untrusted pull-request builds. Use the secret-handling rules of your CI provider.

## Notification automation

Automatic review delivery is not part of the current framework implementation. A future integration could upload the request as a protected workflow artifact and create a private GitHub issue or send an organization notification, but that requires a separate authenticated service/workflow and careful source-code privacy controls.

## Limitations

- Static scanning can produce false positives and false negatives.
- Contextual religious, legal, and ethical decisions require qualified human review.
- Open-source forks can modify or remove framework enforcement.
- A valid signature proves that a holder of the configured secret signed the payload; it does not prove the reviewer is qualified.
- Report files can contain project metadata and matched evidence. Protect them as internal build artifacts when appropriate.
