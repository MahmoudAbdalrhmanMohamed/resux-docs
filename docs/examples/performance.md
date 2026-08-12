# Performance Measurements

**Lab-backed example:** [`pages/performance.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/pages/performance.vue) · [Open the live page](https://resux-lab.vercel.app/performance)

The lab includes intentionally small browser measurements for two questions: how long a local state patch takes and what repeated API latency looks like from the browser. These numbers are diagnostics, not a formal benchmark suite.

## Measure an interaction-side state patch

```vue
<script setup lang="ts">
const clicks = useState('perf-clicks', () => 0)
const last = useState('perf-last', () => 'No browser measurement yet')

function measureClick() {
  const start = performance.now()
  clicks.value++
  const end = performance.now()
  last.value = `${(end - start).toFixed(3)} ms state patch`
}
</script>
```

This measures the synchronous work around the state mutation in that browser. It does **not** include every cost involved in first interaction, module loading, rendering or network transfer.

## Measure repeated API requests

```ts
async function runApiBench() {
  const start = performance.now()
  let successful = 0

  for (let index = 0; index < 5; index++) {
    const response = await fetch(`/api/stats?source=browser-bench&n=${index}`)
    if (response.ok) successful++
  }

  const averageMs = (performance.now() - start) / 5
  console.log(`${averageMs.toFixed(2)} ms avg across ${successful} API calls`)
}
```

Sequential requests are useful for a quick smoke measurement, but use repeatable load/benchmark tooling when you need statistically meaningful server performance data.

## Measure the thing Resux is optimizing

For resumability work, inspect more than one timing number:

- initial HTML and critical assets,
- JavaScript requested before interaction,
- JavaScript requested by the first interaction,
- handler execution and binding patch cost,
- navigation cost,
- server/API latency,
- layout shift and media loading.

A fast local state mutation cannot compensate for a large unnecessary client bundle, and a small bundle cannot compensate for a slow API.

## Related

- [Resumability Deep Dive](/guide/resumability-deep-dive)
- [Rendering Lifecycle](/guide/rendering-lifecycle)
- [Security and Caching](/guide/security-caching)
- [Debugging Mental Model](/guide/debugging-mental-model)
