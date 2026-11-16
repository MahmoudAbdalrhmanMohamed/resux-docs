# Example: Interactive OTP Verification Flow (`RxVerificationCode`)

Demonstrates a complete two-factor authentication (2FA) screen using `<RxVerificationCode>` from `resuxjs/ui`, including automatic submission on `@complete`, status choreography (`idle` → `verifying` → `success` / `error`), and digit masking.

<RxComponentPreview component="RxVerificationCode" title="Live Interactive OTP Verification Demo" />

```vue
<!-- pages/auth/verify.vue -->
<script setup lang="ts">
import { ref } from 'resuxjs'
import {
  RxCard,
  RxVerificationCode,
  RxButton,
  RxBadge,
  RxAlert,
  type VerificationCodeStatus
} from 'resuxjs/ui'
import { navigateClient } from 'resuxjs/runtime/router'

const otp = ref('')
const status = ref<VerificationCodeStatus>('idle')
const maskDigits = ref(false)

async function handleComplete(code: string) {
  status.value = 'verifying'
  try {
    const res = await $fetch<{ verified: boolean }>('/api/auth/verify-otp', {
      method: 'POST',
      body: { code }
    })
    if (res.verified) {
      status.value = 'success'
      setTimeout(() => {
        navigateClient('/dashboard', { viewTransition: true })
      }, 650)
    } else {
      status.value = 'error'
    }
  } catch {
    status.value = 'error'
  }
}
</script>

<template>
  <main class="max-w-md mx-auto py-12">
    <RxCard variant="elevated" class="space-y-5">
      <div class="flex items-center justify-between">
        <h1 class="text-lg font-bold">Two-Factor Authentication</h1>
        <RxBadge variant="primary">Halal Guard</RxBadge>
      </div>

      <p class="text-sm opacity-80">
        Enter the 6-digit one-time verification code sent to your registered device.
      </p>

      <RxVerificationCode
        v-model="otp"
        :length="6"
        :status="status"
        :mask="maskDigits"
        auto-focus
        verifying-text="Checking cryptographic signature..."
        success-text="Identity verified — redirecting..."
        error-text="The verification code is invalid or expired"
        @complete="handleComplete"
      />

      <div class="flex items-center justify-between pt-2">
        <RxButton variant="ghost" size="sm" @click="maskDigits = !maskDigits">
          {{ maskDigits ? 'Show Digits' : 'Mask Digits' }}
        </RxButton>
        <RxButton variant="outline" size="sm" @click="otp = ''; status = 'idle'">
          Clear Code
        </RxButton>
      </div>
    </RxCard>
  </main>
</template>
```
