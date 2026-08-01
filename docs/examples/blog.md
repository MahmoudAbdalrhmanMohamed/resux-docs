# Blog Routes Example

## Files

```txt
pages/blog/index.vue
pages/blog/[slug].vue
server/api/posts/index.ts
server/api/posts/[slug].ts
```

## Blog list

```vue
<script setup lang="ts">
useSeoMeta({ title: 'Blog', description: 'Latest posts' })

const posts = await useFetch<Array<{ slug: string; title: string }>>('/api/posts')
</script>

<template>
  <main>
    <h1>Blog</h1>
    <p v-if="posts.pending">Loading…</p>
    <p v-else-if="posts.error">Could not load posts.</p>
    <ul v-else>
      <li v-for="post in posts.data" :key="post.slug">
        <ResuxLink :to="`/blog/${post.slug}`">{{ post.title }}</ResuxLink>
      </li>
    </ul>
  </main>
</template>
```

## Post page

```vue
<script setup lang="ts">
const route = useRoute()
const post = await useFetch<{ title: string; body: string }>(
  `/api/posts/${route.params.slug}`
)

if (!post.data.value) {
  throw createError({ statusCode: 404, message: 'Post not found' })
}

useSeoMeta({
  title: post.data.value.title,
  description: post.data.value.body.slice(0, 150)
})
</script>

<template>
  <article>
    <h1>{{ post.data.title }}</h1>
    <p>{{ post.data.body }}</p>
  </article>
</template>
```

Do not put unsanitized user HTML into `v-html`. Render structured content or sanitize it with an application policy.
