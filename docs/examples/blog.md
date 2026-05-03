# Example: Blog Routes

Create static and dynamic blog pages with file routing.

## Route files

```txt
pages/blog/index.vue
pages/blog/[slug].vue
```

## Blog index

```vue
<script setup lang="ts">
const posts = [
  { slug: 'hello-resux', title: 'Hello Resux' },
  { slug: 'resumability', title: 'Resumability in practice' }
]
</script>

<template>
  <main>
    <h1>Blog</h1>
    <ul>
      <li v-for="post in posts">
        <ResuxLink :to="`/blog/${post.slug}`">
          {{ post.title }}
        </ResuxLink>
      </li>
    </ul>
  </main>
</template>
```

## Blog detail

```vue
<script setup lang="ts">
const route = useRoute()

const { data: post, error } = await useAsyncData('post', () => {
  return $fetch(`/api/posts/${route.params.slug}`)
})

useSeoMeta({
  title: post.value?.title,
  description: post.value?.description
})
</script>

<template>
  <article>
    <p v-if="error">{{ error.message }}</p>
    <template v-if="post">
      <h1>{{ post.title }}</h1>
      <p>{{ post.description }}</p>
    </template>
  </article>
</template>
```

## API route

```ts
// server/api/posts/[slug].ts
export default defineEventHandler((event) => {
  return {
    slug: event.params.slug,
    title: `Post ${event.params.slug}`,
    description: 'Loaded from a Resux API route.'
  }
})
```
