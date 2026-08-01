# Progressive Package Example

This example loads a DOM library only when a target becomes visible and disposes it when the page changes.

## Configure package mode

```ts
export default defineResuxConfig({
  packages: {
    mode: {
      'chart-library': 'progressive'
    },
    css: {
      'chart-library': ['chart-library/styles.css']
    },
    diagnostics: true
  }
})
```

## Enhancement

```ts
// enhancements/sales-chart.client.ts
export default defineClientEnhancement('sales-chart', async (target, context) => {
  const library = await useClientPackage<typeof import('chart-library')>('chart-library')
  const instance = library.createChart(target, context.options)

  return () => {
    instance.destroy()
  }
})
```

## Activate from a component

```vue
<script setup lang="ts">
onMounted(async () => {
  await useClientEnhancement('sales-chart', {
    target: '#sales-chart',
    trigger: 'visible',
    options: {
      labels: ['Jan', 'Feb', 'Mar'],
      values: [10, 18, 25]
    }
  })
})
</script>

<template>
  <div id="sales-chart" aria-label="Sales chart"></div>
</template>
```

## Debug

```sh
resux inspect enhancements --json
resux inspect packages --json
resux inspect bundles --json
```

The actual package API is illustrative. Follow the cleanup API provided by the package you integrate.
