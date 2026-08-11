# Icons (`resuxjs/icons`)

The deep icon documentation now lives in the dedicated [Icons](/icons/) section:

- [Overview](/icons/)
- [Usage and local registry](/icons/usage)
- [Configuration](/icons/configuration)
- [Remote/lazy runtime loading](/icons/runtime)

This guide URL remains as a stable entry point for existing links.

## Runtime boundary

`Icon` / `ResuxIcon` from `resuxjs/icons` are Vue SVG components. They belong inside a [Vue island](./vue-islands.md) or another explicit Vue runtime boundary.

The current module defaults are `collections: []`, `mode: 'svg'`, component name `Icon`, and `lazy: false`. Unknown registry icons can be fetched from the configured Iconify-compatible provider after client mount; local `iconRegistry` entries can render without that remote request.

```vue
<script setup lang="ts">
import { Icon } from 'resuxjs/icons'
</script>

<template>
  <Icon name="check" />
  <Icon name="ph:check-circle" lazy />
</template>
```

Do not confuse this with `RxIcon` from `resuxjs/ui`, which is a small text placeholder primitive rather than the SVG provider system.
