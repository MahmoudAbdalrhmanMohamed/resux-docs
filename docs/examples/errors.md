# Error Handling

**Lab-backed example:** [`pages/features/errors.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/pages/features/errors.vue) · [Open the live page](https://resux-lab.vercel.app/features/errors)

The lab verifies two related APIs from `resuxjs`: `createError()` for constructing a structured error and `useError()` for reading the active application error.

## Create a structured error

```vue
<script setup>
import { createError, useError } from 'resuxjs'
import { ref } from 'vue'

const activeError = useError()
const message = ref('')

function triggerLocalError() {
  const error = createError({
    statusCode: 400,
    message: 'Invalid request parameters'
  })

  message.value = `${error.statusCode}: ${error.message}`
}
</script>
```

`createError()` creates the error object; constructing it does not automatically mean you have thrown it or replaced the current app error. Choose whether to display, return or throw the result based on the boundary you are working in.

## Show local and active error state separately

```vue
<template>
  <button @click="triggerLocalError">Create Error</button>
  <p>{{ message }}</p>
  <p>Active Error: {{ activeError ? activeError.message : 'None' }}</p>
</template>
```

This separation is useful while debugging: a locally constructed validation error and the application-level active error are not necessarily the same thing.

## Production guidance

For route-level failures, pair these APIs with the app error shell and server response behavior described in the error guide. Do not expose internal stack traces, secrets or database details in user-facing error messages.

## Related

- [App Shell and Errors](/guide/app-shell-errors)
- [Server API](/guide/server-api)
- [Troubleshooting](/guide/troubleshooting)
- [Core API](/reference/core)
