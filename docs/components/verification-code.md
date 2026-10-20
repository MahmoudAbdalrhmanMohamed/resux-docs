# VerificationCode

`RxVerificationCode` (with alias `ResuxVerificationCode`) is an interactive pin-code input component exported by `resuxjs/ui`. It provides an animated, accessible pin-entry interface with numeric or alphanumeric input masking, smooth collapsing state transitions, verifying pulse indicators, and error shake animations.

::: warning Vue runtime boundary
`RxVerificationCode` is part of `resuxjs/ui` and belongs inside a [Vue island](/guide/vue-islands) or an explicit Vue runtime context.
:::

## Basic usage

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { RxVerificationCode, type VerificationCodeStatus } from 'resuxjs/ui'

const code = ref('')
const status = ref<VerificationCodeStatus>('idle')

async function handleComplete(completedCode: string) {
  status.value = 'verifying'
  try {
    const response = await fetch('/api/verify-code', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code: completedCode })
    })
    if (response.ok) {
      status.value = 'success'
    } else {
      status.value = 'error'
    }
  } catch {
    status.value = 'error'
  }
}
</script>

<template>
  <RxVerificationCode
    v-model="code"
    :length="6"
    mode="numeric"
    :status="status"
    @complete="handleComplete"
  />
</template>
```

## Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `modelValue` | `string` | `''` | Current verification code string. Supports `v-model`. |
| `length` | `number` | `6` | Total number of code input cells (typically 4, 6, or 8). |
| `mode` | `'numeric' \| 'alphanumeric'` | `'numeric'` | Input validation mode. `'numeric'` accepts digits `0-9`; `'alphanumeric'` accepts `A-Z, a-z, 0-9`. |
| `status` | `'idle' \| 'verifying' \| 'success' \| 'error'` | `'idle'` | Interactive status controlling animation states and status indicators. |
| `autofocus` | `boolean` | `false` | Automatically focus the first input cell on mount. |
| `disabled` | `boolean` | `false` | Disables input interaction and darkens cell borders. |
| `unstyled` | `boolean` | `false` | Omits default theme styling for custom CSS implementations. |
| `ariaLabel` | `string` | `'Verification code'` | Accessible label for screen readers. |
| `errorText` | `string` | `'The verification code is invalid'` | Accessible error message displayed and announced when `status="error"`. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `(value: string)` | Emitted whenever the code string changes. |
| `change` | `(value: string)` | Emitted when an input cell updates. |
| `complete` | `(value: string)` | Emitted when all cells are filled. Use this to trigger automated verification requests. |

## Interactive Animation States

1. **Cell Fill & Active Cell**:
   - As digits are entered, cells animate with a subtle fill gradient.
   - The active cell highlights with an accent border.
2. **Collapsing Phase**:
   - When transitioning into `'verifying'`, cells smoothly collapse together before revealing the status orb.
3. **Verifying Orb**:
   - A pulsing orb with a spinning loader indicates that the verification request is pending.
4. **Success State**:
   - The status orb transitions into a green checkmark (`✓`) with a confirmation message.
5. **Error Shake**:
   - On verification failure (`status="error"`), the input cells shake horizontally, highlight in red, and reveal the error text. Focus returns to the input cells so the user can easily re-type.
