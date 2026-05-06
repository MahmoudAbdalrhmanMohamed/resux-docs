# Contributing to Docs

Resux is moving quickly, so docs should stay close to the source.

## Edit locally

```sh
git clone https://github.com/MahmoudAbdalrhmanMohamed/resux-docs.git
cd resux-docs
npm install
npm run dev
```

## Docs principles

- Prefer exact examples over vague explanation.
- Mark stable core vs experimental limits clearly.
- Keep terminology consistent: Resux component, resumable handler, Vue island, route payload, runtime config.
- Add examples for every new feature.
- Update reference pages when globals, CLI commands, or file conventions change.

## Page checklist

Before merging a docs change:

- Does it show a complete code example?
- Does it explain server vs browser behavior?
- Does it mention serialization rules if state is involved?
- Does it link to related guide and reference pages?
- Does `npm run build` pass?

## Publish

Push to `main`. The GitHub Actions workflow builds VitePress and deploys to GitHub Pages.
