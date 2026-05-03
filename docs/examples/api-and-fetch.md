# Example: API and Fetch

This example shows SSR-safe internal API calls.

## API endpoint

```ts
// server/api/status.ts
export default defineEventHandler(() => {
  return {
    ok: true,
    framework: 'resux',
    time: new Date().toISOString()
  }
})
```

## SSR page fetch

```vue
<script setup lang="ts">
type Status = {
  ok: boolean
  framework: string
  time: string
}

const { data, error } = await useAsyncData('status', ({ signal }) => {
  return $fetch<Status>('/api/status', { signal })
})
</script>

<template>
  <main>
    <h1>System status</h1>
    <p v-if="error">{{ error.message }}</p>
    <pre v-if="data">{{ data }}</pre>
  </main>
</template>
```

## Native fetch with apiURL

```ts
const response = await fetch(apiURL('/api/status'))
const status = await response.json()
```

Use `$fetch` when you want JSON parsing and internal URL resolution in one helper.
