# API and Fetch Example

## Handler

```ts
// server/api/tasks.ts
export default defineEventHandler(async (event) => {
  if (event.method === 'GET') {
    return [{ id: 1, title: 'Learn Resux', done: false }]
  }

  if (event.method === 'POST') {
    const body = await readBody<{ title: string }>(event)
    if (!body.title?.trim()) {
      return new Response('Title is required', { status: 400 })
    }

    setHeader(event, 'cache-control', 'no-store')
    return { id: Date.now(), title: body.title.trim(), done: false }
  }

  return new Response('Method not allowed', { status: 405 })
})
```

## Page

```vue
<script setup lang="ts">
const tasks = await useFetch<Array<{ id: number; title: string; done: boolean }>>('/api/tasks')
const title = useState('new-task-title', () => '')
const saving = ref(false)

async function addTask() {
  if (!title.value.trim() || saving.value) return
  saving.value = true
  try {
    const created = await $fetch<{ id: number; title: string; done: boolean }>('/api/tasks', {
      method: 'POST',
      body: { title: title.value }
    })
    tasks.data.value = [...(tasks.data.value ?? []), created]
    title.value = ''
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <form @submit.prevent="addTask">
    <input v-model="title" />
    <button :disabled="saving">Add</button>
  </form>

  <p v-if="tasks.pending">Loading…</p>
  <p v-else-if="tasks.error">{{ tasks.error.message }}</p>
  <ul v-else>
    <li v-for="task in tasks.data" :key="task.id">{{ task.title }}</li>
  </ul>
</template>
```

`useFetch` returns refs for resource state. `$fetch` returns the parsed response directly.
