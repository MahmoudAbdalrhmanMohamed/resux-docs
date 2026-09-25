# Project Status: Public Beta

Resux is currently in **public beta**.

The 0.4 line is intended for evaluation, real-world application testing, deployment validation, and compatibility feedback before the stable 1.0 API contract. It is more mature than an experimental prototype, but pre-1.0 APIs can still change as production feedback exposes missing constraints or better abstractions.

## Release channels

| Channel | Version line | npm tag | Use it when |
| --- | --- | --- | --- |
| Stable | 0.3.x | `latest` | You want the current stable pre-beta package line |
| Public beta | 0.4.x prereleases | `next` | You want current hardening, features, and beta validation |

The first public-beta milestone is `0.4.0-beta.1`.

Try the beta with:

```sh
npx create-resuxjs@next my-app
cd my-app
npm install
npm run dev
```

For repeatable production-like tests, pin an exact prerelease instead of relying indefinitely on a moving dist-tag.

## What public beta means

Public beta means Resux is ready for:

- public evaluation and feedback;
- examples, demos, prototypes, and learning projects;
- non-critical real applications with normal engineering safeguards;
- compatibility testing with packages and deployment platforms;
- performance measurement against realistic workloads;
- bug reports and reproducible production-readiness findings.

It does **not** mean the project promises a frozen 1.0 API or long-term compatibility for every pre-1.0 behavior.

## Current release validation

The framework CI currently validates:

- strict production quality and package checks;
- Node.js 20.19 and Node.js 22 runtime compatibility;
- Windows and macOS portability;
- minimal, default, full, i18n, PWA, media, package-compatibility, and dashboard starters;
- Node, static, Netlify, Vercel, and Cloudflare deployment targets;
- release package contents and npm publishing contracts.

The production-hardening work also adds bounded route/icon caches and concurrency plus stricter remote-media and filesystem-path protections.

CI validation is important, but it is not a substitute for broader third-party production usage.

## Production guidance

For a production-like beta deployment:

1. pin the exact Resux version;
2. run your own integration and end-to-end tests;
3. test the deployment target you actually use;
4. verify server APIs, media transformations, caching, i18n, resumability, and any Vue islands your application depends on;
5. review [Current Limits](/reference/limits);
6. monitor errors and resource usage after deployment;
7. test framework upgrades before rolling them into a critical environment.

For business-critical systems with strict compatibility or support requirements, evaluate the beta in a staging or limited-risk workload before making it a core dependency.

## What needs more evidence before 1.0

The main remaining maturity work is not simply “make CI green.” Before a stable 1.0 claim, Resux needs broader evidence from independent applications, including:

- longer-running production workloads;
- more ecosystem/package integrations;
- upgrade experience across multiple releases;
- more measured test coverage visibility;
- documented deprecation and API-stability rules;
- continued security review and regression testing;
- feedback from developers who did not build the framework itself.

## Reporting problems

When reporting a beta issue, include:

- the exact Resux version;
- Node.js version and operating system;
- deployment target;
- minimal reproduction;
- expected and actual behavior;
- whether the issue occurs in development, production build, or both.

Security issues must follow the framework's security policy rather than being disclosed with exploit details in a public issue.

## Related pages

- [Getting Started](/guide/getting-started)
- [Current Limits](/reference/limits)
- [Testing and Quality](/guide/testing-quality)
- [Deployment](/guide/deployment)
- [Release and Publishing](/reference/release)
