# Project Status: Public Beta

Resux is currently in **public beta**. The current beta release is **0.4.0-beta.2**.

The 0.4 line is meant for public evaluation, real-world testing, deployment checks, package compatibility work, and feedback before Resux reaches 1.0. The framework has passed a substantial CI and packaging hardening pass, but pre-1.0 APIs can still change as more applications uncover edge cases.

## Release channels

| Channel | Version line | npm tag | Best fit |
| --- | --- | --- | --- |
| Stable | 0.3.x | `latest` | Existing projects that want the current stable pre-beta line |
| Public beta | 0.4.x prereleases | `next` | New testing, feedback, and access to the latest hardening work |

The public beta started with `0.4.0-beta.1`. The current release, `0.4.0-beta.2`, fixes the npm publishing workflow used to complete the beta release. Framework runtime behavior is unchanged from beta.1.

Try the beta:

```sh
npx create-resuxjs@next my-app
cd my-app
npm install
npm run dev
```

For repeatable testing, pin the exact release:

```sh
npx create-resuxjs@0.4.0-beta.2 my-app
```

## What the beta is good for

Resux 0.4 is appropriate for:

- learning and evaluation;
- demos and prototypes;
- compatibility testing;
- deployment experiments;
- performance testing with realistic applications;
- non-critical applications where you can pin versions and test upgrades;
- finding and reporting production-readiness issues.

It is still pre-1.0, so it does not promise a frozen API or long-term compatibility for every current behavior.

## What is already validated

The framework CI currently covers:

- production quality and package checks;
- Node.js 20.19 and Node.js 22;
- Windows and macOS portability;
- minimal, default, full, i18n, PWA, media, package-compatibility, and dashboard starters;
- Node, static, Netlify, Vercel, and Cloudflare deployment targets;
- package contents and npm release contracts;
- runtime bundle budgets;
- regression coverage for security-sensitive media and path handling.

The framework also includes bounded route/icon caches and request concurrency controls, plus protections around remote media fetching and filesystem paths.

That is useful evidence, but CI cannot replace testing across independent applications and workloads.

## Using the beta in a production-like environment

If you want to evaluate Resux in staging or a real low-risk application:

1. pin the exact Resux version;
2. run your own integration and end-to-end tests;
3. test the deployment target you actually use;
4. verify the features your app depends on, especially server APIs, media, caching, i18n, resumability, and Vue islands;
5. review [Current Limits](/reference/limits);
6. monitor runtime errors and resource usage;
7. test framework upgrades before shipping them.

For business-critical systems with strict support or compatibility requirements, evaluate the beta in a limited-risk environment before making it a core dependency.

## What still needs broader evidence

Before Resux can make a stable 1.0 claim, it needs more experience outside its own test suite, including:

- longer-running production workloads;
- more third-party package integrations;
- upgrade experience across several releases;
- clearer measured coverage reporting;
- documented deprecation and API-stability rules;
- continued security review;
- feedback from developers who were not involved in building the framework.

## Reporting a problem

A useful bug report should include:

- the exact Resux version;
- Node.js version and operating system;
- deployment target;
- a minimal reproduction;
- expected and actual behavior;
- whether the issue happens in development, production build, or both.

Security issues should follow the framework security policy instead of being posted publicly with exploit details.

## Related pages

- [Getting Started](/guide/getting-started)
- [Current Limits](/reference/limits)
- [Testing and Quality](/guide/testing-quality)
- [Deployment](/guide/deployment)
- [Release and Publishing](/reference/release)
