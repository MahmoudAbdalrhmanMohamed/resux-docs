# Resux Halal Core

Resux Halal Core is a mandatory, framework-level safety and compliance subsystem built directly into the ResuxJS core. It automatically inspects project content, metadata, routes, endpoints, and dependencies to prevent the framework from being used for illegal, harmful, deceptive, or *haram* (religiously prohibited in Islamic ethics) applications.

---

## Why Resux Blocks Prohibited Projects
As web technologies scale, frameworks carry an ethical responsibility regarding how they are utilized. ResuxJS implements this safety subsystem to ensure that official compiler builds, developer tools, and deployment adapters are not used to build platforms that facilitate:
- **Haram Businesses**: Gambling, usury (riba) banking, payday loan schemes, adult services, and alcohol/tobacco/vape distribution.
- **Criminal Activities**: Phishing kits, credentials harvesters, scams, counterfeit markets, and money laundering tools.
- **Cyber Abuse**: Ransomware, spy tools, keyloggers, and botnets.
- **Violence & Harm**: Weapons marketplaces, bomb fabrication, suicide encouragement, and human trafficking.

---

## How Scanning Works (Offline-First)
The safety scanner operates locally during `resux dev`, `resux build`, `resux preview`, and `resux deploy` commands.

- **Routing & Pages**: Scans component names, file paths under `/pages` and `/server`, and router parameters.
- **Dependency Audit**: Inspects packages inside `package.json` to block malicious extensions or usury/gambling dependencies.
- **Metadata Inspection**: Evaluates page SEO titles, description tags, and layout attributes.
- **Environment Names**: Scans env variable names (e.g. `CASINO_API_KEY`). It **never** reads, exports, or evaluates the actual secret values.
- **Content Redaction**: Large files are truncated to the first 100KB during evaluations, ignoring binary media files and paths matched in `.gitignore`.

---

## Privacy & Security Guarantees
Your privacy is fully protected:
1. **Local-First Execution**: The default rule evaluator runs offline and does not transmit data to external services.
2. **Strict Redaction**: In optional AI-assisted verification modes, source code is run through an AST summarizer that replaces credentials, keys, passwords, and private tokens with `[REDACTED]`. No secrets are ever sent to LLMs.
3. **No Hidden Telemetry**: The safety subsystem does not execute stealthy project uploads. All evaluations and report files are saved locally in the `.resux/` folder.

---

## Config Policy (`resux.halal.config.ts`)
Developers can declare project categories, contact information, and supplementary stricter rules:

```ts
import { defineResuxHalalPolicy } from 'resux'

export default defineResuxHalalPolicy({
  projectName: 'Islamic Finance Education',
  projectType: 'education',
  description: 'An academic blog explaining the economics of riba-free investments.',
  stricterRules: {
    blockAiChatWithoutModeration: true
  },
  reviewContact: {
    name: 'Compliance lead',
    email: 'compliance@example.com'
  }
})
```

### Prohibited Fields
You cannot weaken or bypass the safety engine. Setting `enabled: false`, `mode: 'off'`, or `ignoreCoreRules: true` will cause validation checks to fail and prevent command execution.

---

## Review Workflow for False Positives
Projects that match policy categories under benign contexts (e.g., educational cybersecurity sites discussing phishing, or news blogs reporting on conflict violence) are flagged as `review_required`.

To authorize these builds:
1. Run `resux halal submit-review` to package a local metadata request bundle.
2. Submit the bundle to your compliance authority for audit.
3. Place the received, signed cryptographically verified `halal-review-approval.json` file in your project root.
4. Subsequent builds will verify the signature and proceed successfully.

---

## Limitations & Open-Source Reality
- **Forks**: As ResuxJS is open-source, developers can fork the framework and remove this safety module locally. However, the official package distributions, NPM releases, CLI tools, and deployment adapters will strictly require and enforce it.
- **Static Analysis**: Keyword matching can occasionally flag false positives, which are handled gracefully via the signed review workflow.
- **Disclaimers**: The safety subsystem operates as an automated ethical filter, not as an official fatwa engine.
