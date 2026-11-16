# Example: Server API & `$fetch` with Runtime Validation

Demonstrates `defineServerHandler` with strict runtime POST body validation (`400` on missing/malformed `title`) paired with `useAsyncData` and dedicated submission error handling on the client.

```ts
// server/api/tasks.ts
import { defineServerHandler, readBody, setHeader } from 'resuxjs/server'

interface Task {
  id: number
  title: string
  done: boolean
}

const tasksStore: Task[] = [
  { id: 1, title: 'Upgrade fonts engine to fontless 1.3.4', done: true },
  { id: 2, title: 'Add interactive UI previews to resux-docs', done: false }
]

export default defineServerHandler(async (event) => {
  if (event.method === 'GET') {
    return tasksStore
  }

  if (event.method === 'POST') {
    const body = await readBody< unknown >(event)
    const rawTitle =
      body && typeof body === 'object' && 'title' in body && typeof (body as { title?: unknown }).title === 'string'
        ? (body as { title: string }).title.trim()
        : ''

    if (!rawTitle) {
      return new Response(JSON.stringify({ error: 'A non-empty string title is required' }), {
        status: 400,
        headers: { 'content-type': 'application/json' }
      })
    }

    setHeader(event, 'cache-control', 'no-store')
    const created: Task = { id: Date.now(), title: rawTitle, done: false }
    tasksStore.push(created)
    return created
  }

  return new Response('Method Not Allowed', { status: 405 })
})
```

```vue
<!-- pages/tasks.vue -->
<script setup lang="ts">
import { ref } from 'resuxjs'
import { useAsyncData, $fetch } from 'resuxjs/runtime'
import { RxCard, RxInput, RxButton, RxAlert, RxBadge } from 'resuxjs/ui'

interface Task {
  id: number
  title: string
  done: boolean
}

const tasks = await useAsyncData<Task[]>('tasks-list', ({ signal }) =>
  $fetch('/api/tasks', { signal })
)

const title = ref('')
const saving = ref(false)
const submitError = ref('')

async function addTask() {
  if (!title.value.trim() || saving.value) return
  saving.value = true
  submitError.value = ''
  try {
    const created = await $fetch<Task>('/api/tasks', {
      method: 'POST',
      body: { title: title.value }
    })
    tasks.data.value = [...(tasks.data.value ?? []), created]
    title.value = ''
  } catch (err) {
    submitError.value = err instanceof Error ? err.message : 'Failed to create task. Please try again.'
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <RxCard class="space-y-4 max-w-lg">
    <div class="flex items-center justify-between">
      <h2 class="font-bold text-base">Release Checklist</h2>
      <RxBadge variant="primary">{{ tasks.data.value?.length ?? 0 }} items</RxBadge>
    </div>

    <form class="flex gap-2" @submit.prevent="addTask">
      <RxInput v-model="title" placeholder="Add a release task..." :disabled="saving" />
      <RxButton type="submit" variant="primary" :disabled="saving">
        {{ saving ? 'Saving...' : 'Add' }}
      </RxButton>
    </form>

    <RxAlert v-if="submitError" variant="error" title="Submission Failed" dismissible @dismiss="submitError = ''">
      {{ submitError }}
    </RxAlert>

    <ul class="space-y-2">
      <li v-for="task in tasks.data.value" :key="task.id" class="flex items-center justify-between text-sm p-2 rounded border border-slate-200/60">
        <span>{{ task.title }}</span>
        <RxBadge :variant="task.done ? 'success' : 'default'">{{ task.done ? 'Done' : 'Pending' }}</RxBadge>
      </li>
    </ul>
  </RxCard>
</template>
```
