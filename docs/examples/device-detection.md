# Device Detection

**Lab-backed example:** [`pages/features/device.vue`](https://github.com/MahmoudAbdalrhmanMohamed/resux-lab/blob/main/pages/features/device.vue) · [Open the live page](https://resux-lab.vercel.app/features/device)

The Resux Lab exercises the current-device helper and the standalone user-agent parser side by side. That makes it useful for testing both request-derived device flags and explicit parsing.

## Read the current device

```vue
<script setup>
import { useDevice } from 'resuxjs'

const device = useDevice()
</script>

<template>
  <p>Mobile: {{ device.isMobile }}</p>
  <p>Tablet: {{ device.isTablet }}</p>
  <p>Desktop: {{ device.isDesktop }}</p>
  <p>iOS: {{ device.isIos }}</p>
  <p>Android: {{ device.isAndroid }}</p>
</template>
```

Use these flags for progressive adaptation, not as a substitute for responsive CSS. Layout should still respond to the actual viewport and user preferences.

## Parse a specific user-agent string

```vue
<script setup>
import { parseUserAgent } from 'resuxjs'
import { computed, ref } from 'vue'

const customUa = ref(
  'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15'
)

const parsed = computed(() => parseUserAgent(customUa.value))
</script>
```

The lab lets you edit the user-agent string and immediately inspect flags such as `isIos` and `isMobile`.

## Treat detection as a hint

User-agent strings can be missing, modified or ambiguous. Avoid making authorization, security or irreversible business decisions from device detection. Prefer capability detection when the feature depends on an actual browser API.

## Related

- [Execution Contexts](/guide/execution-contexts)
- [Server API](/guide/server-api)
- [Core API](/reference/core)
- [Current Limits](/reference/limits)
