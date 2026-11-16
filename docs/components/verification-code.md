# VerificationCode (RxVerificationCode)

Interactive multi-cell OTP / 2FA verification code input (`1..12` cells) with numeric/alphanumeric filtering, paste handling, masking, and choreographed `verifying` / `success` / `error` status transitions.

## Live Interactive Preview — See How It Looks

Use the interactive canvas below to preview how `RxVerificationCode` looks and behaves in real time:

<RxComponentPreview component="RxVerificationCode" title="VerificationCode (RxVerificationCode) — Live Visual Preview" />

## Import

```ts
import { RxVerificationCode } from 'resuxjs/ui'
// Equivalent alias:
import { ResuxVerificationCode } from 'resuxjs/ui'
```

## Complete Runnable Example

```vue
<script setup lang="ts">
import { ref } from 'resuxjs'
import { RxVerificationCode, RxButton, RxBadge } from 'resuxjs/ui'
import type { VerificationCodeStatus } from 'resuxjs/ui'

const code = ref('')
const status = ref<VerificationCodeStatus>('idle')
const masked = ref(false)

async function verifyCode(val: string) {
  status.value = 'verifying'
  await new Promise((r) => setTimeout(r, 900))
  status.value = val === '2026' ? 'success' : 'error'
}

function resetFlow() {
  code.value = ''
  status.value = 'idle'
}
</script>

<template>
  <div class="space-y-4 max-w-md">
    <div class="flex items-center justify-between">
      <span class="text-sm font-medium">Enter 4-digit security code (Try <code>2026</code>)</span>
      <RxBadge :variant="status === 'success' ? 'success' : status === 'error' ? 'error' : 'default'">
        {{ status }}
      </RxBadge>
    </div>

    <RxVerificationCode
      v-model="code"
      :length="4"
      :status="status"
      :mask="masked"
      verifying-text="Validating token with Halal Guard..."
      success-text="Session verified and resumed"
      error-text="Invalid code — try entering 2026"
      @complete="verifyCode"
    />

    <div class="flex flex-wrap gap-2 pt-1">
      <RxButton size="sm" variant="secondary" @click="masked = !masked">
        {{ masked ? 'Show Digits' : 'Mask Digits' }}
      </RxButton>
      <RxButton size="sm" variant="outline" @click="resetFlow">Reset</RxButton>
    </div>
  </div>
</template>
```

## Rendered DOM Structure (`rx-*` Classes)

When rendered on the server or client with default styling (`:unstyled="false"`), `RxVerificationCode` produces the following HTML structure (`rx-verification-code > input + .rx-verification-code-cells (.rx-verification-code-cell) | .rx-verification-code-status`):

```html
<div
  class="rx-verification-code is-focused"
  data-phase="idle"
  data-status="idle"
  data-disabled="false"
  data-length="4"
  style="--rx-otp-length: 4"
>
  <div class="rx-verification-code-cells" aria-hidden="true">
    <span class="rx-verification-code-cell is-filled" data-filled="true">2</span>
    <span class="rx-verification-code-cell is-filled" data-filled="true">0</span>
    <span class="rx-verification-code-cell is-active" data-active="true"></span>
    <span class="rx-verification-code-cell"></span>
  </div>
</div>
```

## Props

| Prop | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `modelValue` | `string` | `''` | No | Current verification code value (`v-model`). |
| `length` | `number` | `4` | No | Number of character cells (clamped between `1` and `12`). |
| `status` | `'idle' \| 'verifying' \| 'success' \| 'error'` | `'idle'` | No | Controls cell collapse choreography, status orb, and error alert. |
| `mode` | `'numeric' \| 'alphanumeric'` | `'numeric'` | No | Restricts input to digits (`0-9`) or alphanumeric characters (`A-Z0-9`). |
| `mask` | `boolean` | `false` | No | Masks filled characters with `•` bullets for privacy. |
| `autoFocus` | `boolean` | `false` | No | Automatically focuses the hidden OTP input on mount. |
| `disabled` | `boolean` | `false` | No | Disables input interaction. |
| `verifyingText` | `string` | `'Verifying...'` | No | Status message announced and displayed when `status === 'verifying'`. |
| `successText` | `string` | `'Verified and secure'` | No | Status message announced and displayed when `status === 'success'`. |
| `errorText` | `string` | `'The verification code is invalid'` | No | Alert message displayed below cells when `status === 'error'`. |
| `ariaLabel` | `string` | `'Verification code'` | No | Accessible label for the hidden `<input autocomplete="one-time-code">`. |
| `unstyled` | `boolean` | `false` | No | Removes default `rx-verification-code*` classes. |

## Events

| Event | Payload | Description |
| --- | --- | --- |
| `update:modelValue` | `string` | Emitted whenever sanitized characters change. |
| `change` | `string` | Emitted alongside `update:modelValue`. |
| `complete` | `string` | Emitted automatically once all `length` cells are filled. |
| `focus` | `FocusEvent` | Emitted when the OTP input receives focus. |
| `blur` | `FocusEvent` | Emitted when the OTP input loses focus. |

## Slots

This component does not expose named or default slots.

## Headless / Tailwind `unstyled` Mode

Pass `:unstyled="true"` to strip default `rx-*` classes and supply your own utility classes:

```vue
<RxVerificationCode unstyled class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium">
  Custom Styled RxVerificationCode
</RxVerificationCode>
```

## SSR, Resumability & Accessibility

- **Server-Side Rendering**: Renders deterministic HTML during SSR with zero client layout shift.
- **Resumability**: Event handlers (`@click`, `v-model` updates) serialize cleanly across Resux server/client boundaries.
- **Keyboard & Screen Readers**: Preserves native focus rings, ARIA state attributes, and semantic HTML tags.
