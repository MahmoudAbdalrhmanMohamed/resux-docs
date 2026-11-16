<script setup lang="ts">
import { ref, computed } from 'vue'

const props = withDefaults(
  defineProps<{
    component?: string
    title?: string
    suite?: boolean
  }>(),
  {
    component: 'RxButton',
    suite: false
  }
)

// Active component when in suite mode
const activeComponent = ref(props.component || 'RxButton')
const isSuite = computed(() => props.suite || props.component === 'RxSuite' || props.component === 'all')

const suiteComponents = [
  { id: 'RxButton', name: 'Button', icon: '🔘' },
  { id: 'RxInput', name: 'Input', icon: '✏️' },
  { id: 'RxVerificationCode', name: 'OTP Code', icon: '🔢' },
  { id: 'RxSwitch', name: 'Switch', icon: '🔀' },
  { id: 'RxBadge', name: 'Badge', icon: '🏷️' },
  { id: 'RxCard', name: 'Card', icon: '🃏' },
  { id: 'RxAlert', name: 'Alert', icon: '🔔' },
  { id: 'RxTabs', name: 'Tabs', icon: '📂' },
  { id: 'RxAccordion', name: 'Accordion', icon: '📜' },
  { id: 'RxModal', name: 'Modal', icon: '🪟' },
  { id: 'RxTooltip', name: 'Tooltip', icon: '💬' }
]

// Current component to render
const currentComp = computed(() => (isSuite.value ? activeComponent.value : props.component || 'RxButton'))

// View mode tabs
const viewMode = ref<'preview' | 'code' | 'dom'>('preview')
const codeCopied = ref(false)

// Interactive state for Button
const btnVariant = ref<'primary' | 'secondary' | 'outline' | 'ghost'>('primary')
const btnSize = ref<'sm' | 'md' | 'lg'>('md')
const btnDisabled = ref(false)
const btnLoading = ref(false)
const btnWithIcon = ref(false)
const btnClickCount = ref(0)
const lastActionText = ref('')

function handleBtnClick() {
  if (btnDisabled.value || btnLoading.value) return
  btnClickCount.value++
  lastActionText.value = `@click triggered (total: ${btnClickCount.value})`
}

function resetBtnProps() {
  btnVariant.value = 'primary'
  btnSize.value = 'md'
  btnDisabled.value = false
  btnLoading.value = false
  btnWithIcon.value = false
  btnClickCount.value = 0
  lastActionText.value = 'Props reset to defaults'
}

// Interactive state for Input
const inputVal = ref('mahmoud@resux.dev')
const inputType = ref<'text' | 'email' | 'password' | 'search'>('email')
const inputStatus = ref<'default' | 'success' | 'error'>('default')
const inputDisabled = ref(false)

// Interactive state for Verification Code (OTP)
const otpVal = ref('2026')
const otpStatus = ref<'idle' | 'verifying' | 'success' | 'error'>('idle')
const otpMask = ref(false)
const otpCells = computed(() => {
  const chars = otpVal.value.slice(0, 4).split('')
  return [0, 1, 2, 3].map((i) => chars[i] || '')
})

function simulateOtpFill(code: string) {
  otpVal.value = code
  otpStatus.value = 'idle'
}

function simulateOtpVerify() {
  otpStatus.value = 'verifying'
  setTimeout(() => {
    if (otpVal.value === '2026') {
      otpStatus.value = 'success'
    } else {
      otpStatus.value = 'error'
    }
  }, 900)
}

// Interactive state for Switch
const switchVal = ref(true)
const switchDisabled = ref(false)

// Interactive state for Card
const cardVariant = ref<'default' | 'elevated' | 'outlined' | 'subtle'>('elevated')
const cardBookmarked = ref(false)

// Interactive state for Badge
const badgeVariant = ref<'default' | 'primary' | 'success' | 'warning' | 'error'>('primary')
const badgeWithDot = ref(true)

// Interactive state for Alert
const alertDismissed = ref(false)
const alertVariant = ref<'info' | 'success' | 'warning' | 'error'>('info')

// Interactive state for Tabs & Accordion
const activeSubTab = ref<'ssr' | 'vt' | 'icons'>('ssr')
const accordionOpen = ref(true)

// Interactive state for Modal
const modalOpen = ref(false)

// Interactive state for Tooltip & Popover
const tooltipHover = ref(false)
const popoverOpen = ref(false)
const dropdownOpen = ref(false)

// Textarea & Select & DatePicker
const textareaVal = ref('Resux 0.4.0-beta.7 brings native View Transitions and zero-CLS metric font fallbacks.')
const selectVal = ref('eu-central-1')
const dateVal = ref('2026-11-20')
const motionKey = ref(1)

// Dynamic Vue SFC Code Generator
const generatedVueCode = computed(() => {
  const c = currentComp.value
  if (c === 'RxButton') {
    const propsList: string[] = []
    if (btnVariant.value !== 'primary') propsList.push(`variant="${btnVariant.value}"`)
    if (btnSize.value !== 'md') propsList.push(`size="${btnSize.value}"`)
    if (btnDisabled.value) propsList.push(':disabled="true"')
    if (btnLoading.value) propsList.push(':loading="true"')
    const propsStr = propsList.length ? ' ' + propsList.join(' ') : ''
    const iconStr = btnWithIcon.value ? '<span class="icon">⚡</span> ' : ''
    return `<template>\n  <RxButton${propsStr} @click="handleClick">\n    ${iconStr}Deploy Application\n  </RxButton>\n</template>\n\n<script setup lang="ts">\nimport { RxButton } from 'resuxjs/ui'\n\nfunction handleClick() {\n  console.log('Button clicked!')\n}\n<\/script>`
  } else if (c === 'RxInput') {
    const statusAttr = inputStatus.value !== 'default' ? ` status="${inputStatus.value}"` : ''
    const disabledAttr = inputDisabled.value ? ' :disabled="true"' : ''
    return `<template>\n  <RxInput\n    v-model="email"\n    type="${inputType.value}"\n    placeholder="Enter work email..."${statusAttr}${disabledAttr}\n  />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxInput } from 'resuxjs/ui'\n\nconst email = ref('${inputVal.value}')\n<\/script>`
  } else if (c === 'RxVerificationCode') {
    return `<template>\n  <RxVerificationCode\n    v-model="otpCode"\n    :digits="4"\n    :masked="${otpMask.value}"\n    :status="${otpStatus.value}"\n    @complete="onComplete"\n  />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxVerificationCode } from 'resuxjs/ui'\n\nconst otpCode = ref('${otpVal.value}')\nfunction onComplete(code: string) {\n  console.log('Submitted OTP:', code)\n}\n<\/script>`
  } else if (c === 'RxSwitch') {
    return `<template>\n  <RxSwitch v-model="enabled"${switchDisabled.value ? ' :disabled="true"' : ''}>\n    {{ enabled ? 'Active' : 'Disabled' }}\n  </RxSwitch>\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxSwitch } from 'resuxjs/ui'\n\nconst enabled = ref(${switchVal.value})\n<\/script>`
  } else if (c === 'RxCard') {
    return `<template>\n  <RxCard variant="${cardVariant.value}">\n    <template #header>\n      <h3>Production Health</h3>\n    </template>\n    <p>All 21 public exports validated against runtime test suites.</p>\n  </RxCard>\n</template>\n\n<script setup lang="ts">\nimport { RxCard } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxAlert') {
    return `<template>\n  <RxAlert variant="${alertVariant.value}" :dismissible="true">\n    <template #title>Deployment Notice</template>\n    Native View Transitions and Zero-CLS font preloading active.\n  </RxAlert>\n</template>\n\n<script setup lang="ts">\nimport { RxAlert } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxBadge') {
    return `<template>\n  <RxBadge variant="${badgeVariant.value}"${badgeWithDot.value ? ' :dot="true"' : ''}>\n    Status: Active\n  </RxBadge>\n</template>\n\n<script setup lang="ts">\nimport { RxBadge } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxTabs') {
    return `<template>\n  <RxTabs v-model="activeTab" :items="tabs" />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxTabs } from 'resuxjs/ui'\n\nconst activeTab = ref('${activeSubTab.value}')\nconst tabs = [\n  { label: 'SSR Stream', key: 'ssr' },\n  { label: 'View Transitions', key: 'vt' },\n  { label: 'Static Icons', key: 'icons' }\n]\n<\/script>`
  } else if (c === 'RxModal') {
    return `<template>\n  <RxButton @click="isOpen = true">Open Dialog</RxButton>\n  <RxModal v-model:open="isOpen" title="Confirm Deploy">\n    <p>Deploy resuxjs@0.4.0-beta.7 to production?</p>\n  </RxModal>\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxModal, RxButton } from 'resuxjs/ui'\n\nconst isOpen = ref(false)\n<\/script>`
  }
  return `<template>\n  <${c} />\n</template>\n\n<script setup lang="ts">\nimport { ${c} } from 'resuxjs/ui'\n<\/script>`
})

// Dynamic HTML / DOM representation
const generatedDomHtml = computed(() => {
  const c = currentComp.value
  if (c === 'RxButton') {
    const disabledAttr = btnDisabled.value ? ' disabled' : ''
    return `<button type="button" class="rx-btn rx-btn-${btnVariant.value} rx-btn-${btnSize.value}"${disabledAttr}>\n  ${btnWithIcon.value ? '<span class="rx-icon">⚡</span> ' : ''}${btnLoading.value ? '<span class="rx-spinner">⏳</span> ' : ''}Deploy Application\n</button>`
  } else if (c === 'RxInput') {
    const disabledAttr = inputDisabled.value ? ' disabled' : ''
    return `<div class="rx-input-wrapper" data-status="${inputStatus.value}">\n  <input type="${inputType.value}" value="${inputVal.value}" class="rx-input rx-input-${inputStatus.value}"${disabledAttr} />\n</div>`
  } else if (c === 'RxVerificationCode') {
    return `<div class="rx-verification-code is-focused" data-status="${otpStatus.value}">\n  <div class="rx-verification-code-cells">\n    ${otpCells.value.map((cell) => `<span class="rx-verification-code-cell">${otpMask.value && cell ? '•' : cell}</span>`).join('\n    ')}\n  </div>\n</div>`
  } else if (c === 'RxSwitch') {
    return `<button type="button" role="switch" aria-checked="${switchVal.value}" data-state="${switchVal.value ? 'checked' : 'unchecked'}" class="rx-switch${switchVal.value ? ' checked' : ''}">\n  <span class="rx-switch-thumb" aria-hidden="true"></span>\n</button>`
  } else if (c === 'RxCard') {
    return `<div class="rx-card rx-card-${cardVariant.value}">\n  <div class="rx-card-header"><h3>Production Health</h3></div>\n  <div class="rx-card-body"><p>All 21 public exports validated.</p></div>\n</div>`
  } else if (c === 'RxBadge') {
    return `<span class="rx-badge rx-badge-${badgeVariant.value}">\n  ${badgeWithDot.value ? '<span class="rx-badge-dot"></span> ' : ''}Status: Active\n</span>`
  } else if (c === 'RxAlert') {
    return `<div class="rx-alert rx-alert-${alertVariant.value}" role="alert">\n  <div class="rx-alert-title">Deployment Notice</div>\n  <div class="rx-alert-content">Native View Transitions active.</div>\n</div>`
  }
  return `<div class="rx-${c.toLowerCase().replace('rx', '')}">\n  <!-- Generated ${c} markup -->\n</div>`
})

function copyCode(text: string) {
  if (typeof navigator !== 'undefined' && navigator.clipboard?.writeText) {
    navigator.clipboard.writeText(text)
    codeCopied.value = true
    setTimeout(() => {
      codeCopied.value = false
    }, 2000)
  }
}
</script>

<template>
  <div class="rx-preview-container">
    <!-- Top Header Toolbar -->
    <div class="rx-preview-header">
      <div class="rx-preview-title-group">
        <span class="rx-preview-badge">Live UI Preview</span>
        <h3 class="rx-preview-title">
          {{ isSuite ? 'UI Suite Interactive Playground' : (title || currentComp) }}
        </h3>
        <span class="rx-preview-pkg-tag">resuxjs/ui</span>
      </div>

      <!-- Mode Switcher Tabs -->
      <div class="rx-preview-mode-tabs" role="tablist">
        <button
          type="button"
          class="rx-mode-tab"
          :class="{ active: viewMode === 'preview' }"
          @click="viewMode = 'preview'"
        >
          🎨 Preview
        </button>
        <button
          type="button"
          class="rx-mode-tab"
          :class="{ active: viewMode === 'code' }"
          @click="viewMode = 'code'"
        >
          📋 Vue Code
        </button>
        <button
          type="button"
          class="rx-mode-tab"
          :class="{ active: viewMode === 'dom' }"
          @click="viewMode = 'dom'"
        >
          🔍 Inspect DOM
        </button>
      </div>
    </div>

    <!-- Suite Component Switcher Tray (Active when in suite mode) -->
    <div v-if="isSuite" class="rx-suite-tray" aria-label="Component Suite Selector">
      <div class="rx-suite-tray-label">Select Component:</div>
      <div class="rx-suite-tray-scroll">
        <button
          v-for="item in suiteComponents"
          :key="item.id"
          type="button"
          class="rx-suite-pill"
          :class="{ active: activeComponent === item.id }"
          @click="activeComponent = item.id"
        >
          <span class="rx-suite-pill-icon">{{ item.icon }}</span>
          <span>{{ item.name }}</span>
        </button>
      </div>
    </div>

    <!-- 1. Interactive Canvas Stage View -->
    <div v-if="viewMode === 'preview'" class="rx-preview-stage-wrap">
      <div class="rx-preview-stage">
        <!-- ==================== RxButton ==================== -->
        <div v-if="currentComp === 'RxButton'" class="rx-stage-inner rx-center-stage">
          <div class="rx-stage-hero-item">
            <button
              type="button"
              :disabled="btnDisabled || btnLoading"
              :class="`rx-btn rx-btn-${btnVariant} rx-btn-${btnSize}`"
              @click="handleBtnClick"
            >
              <span v-if="btnWithIcon" class="rx-icon-inline" aria-hidden="true">⚡</span>
              <span v-if="btnLoading" class="rx-spinner-inline" aria-hidden="true">⏳</span>
              <span>Deploy Application</span>
            </button>
          </div>

          <!-- Live Event Feedback Toast -->
          <div class="rx-stage-feedback">
            <span class="rx-feedback-indicator" :class="{ pulse: btnClickCount > 0 }"></span>
            <span class="rx-feedback-text">
              {{ lastActionText || 'Click the button above to test real event handling' }}
            </span>
            <span v-if="btnClickCount > 0" class="rx-feedback-counter">
              Count: {{ btnClickCount }}
            </span>
          </div>
        </div>

        <!-- ==================== RxInput ==================== -->
        <div v-else-if="currentComp === 'RxInput'" class="rx-stage-inner">
          <div class="rx-form-group">
            <label class="rx-form-label">
              <span>Developer Email</span>
              <span v-if="inputStatus === 'success'" class="rx-label-status success">✓ Valid format</span>
              <span v-else-if="inputStatus === 'error'" class="rx-label-status error">✗ Needs @ and domain</span>
            </label>
            <div class="rx-input-container">
              <input
                v-model="inputVal"
                :type="inputType"
                :disabled="inputDisabled"
                placeholder="Enter work email..."
                class="rx-input"
                :class="{ 'is-success': inputStatus === 'success', 'is-error': inputStatus === 'error' }"
              />
              <button
                v-if="inputVal && !inputDisabled"
                type="button"
                class="rx-input-clear"
                title="Clear input"
                @click="inputVal = ''"
              >
                ✕
              </button>
            </div>
            <div class="rx-form-hint">
              Two-way bound: <code>{{ inputVal || '(empty)' }}</code> · Length: {{ inputVal.length }} chars
            </div>
          </div>
        </div>

        <!-- ==================== RxVerificationCode (OTP) ==================== -->
        <div v-else-if="currentComp === 'RxVerificationCode'" class="rx-stage-inner rx-center-stage">
          <div class="rx-verification-code is-focused" :data-status="otpStatus">
            <div v-if="otpStatus === 'idle' || otpStatus === 'error'" class="rx-verification-code-cells">
              <span
                v-for="(c, idx) in otpCells"
                :key="idx"
                class="rx-verification-code-cell"
                :class="{ 'is-filled': !!c, 'is-active': idx === otpVal.length }"
              >
                {{ c ? (otpMask ? '•' : c) : '' }}
              </span>
            </div>
            <div v-else class="rx-verification-code-status" :class="`is-${otpStatus}`" role="status">
              <span>{{ otpStatus === 'verifying' ? '⏳ Verifying code with server HMAC...' : '✓ Code verified securely' }}</span>
            </div>
            <span v-if="otpStatus === 'error'" class="rx-verification-code-error" role="alert">
              Invalid verification code. Try "2026".
            </span>
          </div>

          <div class="rx-otp-quick-actions">
            <button type="button" class="rx-pill-action" @click="simulateOtpFill('2026')">
              Paste "2026"
            </button>
            <button type="button" class="rx-pill-action" @click="simulateOtpFill('9999')">
              Paste "9999"
            </button>
            <button type="button" class="rx-pill-action primary" @click="simulateOtpVerify">
              Submit Verification
            </button>
            <button type="button" class="rx-pill-action" @click="simulateOtpFill('')">
              Clear
            </button>
          </div>
        </div>

        <!-- ==================== RxSwitch ==================== -->
        <div v-else-if="currentComp === 'RxSwitch'" class="rx-stage-inner rx-center-stage">
          <div class="rx-switch-demo-card">
            <div class="rx-switch-demo-info">
              <strong class="rx-switch-demo-title">Native View Transitions</strong>
              <p class="rx-switch-demo-desc">Enable smooth page swap animations across router navigation.</p>
            </div>
            <button
              type="button"
              role="switch"
              :aria-checked="switchVal"
              :data-state="switchVal ? 'checked' : 'unchecked'"
              :disabled="switchDisabled"
              class="rx-switch"
              :class="{ checked: switchVal }"
              @click="switchVal = !switchVal"
            >
              <span class="rx-switch-thumb" aria-hidden="true"></span>
            </button>
          </div>
          <div class="rx-stage-feedback" style="margin-top: 1rem;">
            <span>State: <strong>{{ switchVal ? 'Enabled (checked)' : 'Disabled (unchecked)' }}</strong> · role="switch" · aria-checked="{{ switchVal }}"</span>
          </div>
        </div>

        <!-- ==================== RxBadge ==================== -->
        <div v-else-if="currentComp === 'RxBadge'" class="rx-stage-inner rx-center-stage">
          <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; justify-content: center;">
            <span :class="`rx-badge rx-badge-${badgeVariant}`">
              <span v-if="badgeWithDot" class="rx-badge-dot" aria-hidden="true"></span>
              {{ badgeVariant.toUpperCase() }} BADGE
            </span>
            <span class="rx-badge rx-badge-primary">v0.4.0-beta.7</span>
            <span class="rx-badge rx-badge-success">● Halal Signed</span>
            <span class="rx-badge rx-badge-warning">⚠ Zero-CLS</span>
            <span class="rx-badge rx-badge-error">✕ Build Check</span>
          </div>
        </div>

        <!-- ==================== RxCard ==================== -->
        <div v-else-if="currentComp === 'RxCard'" class="rx-stage-inner">
          <div class="rx-card" :class="`rx-card-${cardVariant}`" style="max-width: 480px; margin: 0 auto;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span class="rx-badge rx-badge-primary">Card Surface</span>
                <strong style="font-size: 1rem;">Variant: {{ cardVariant }}</strong>
              </div>
              <button
                type="button"
                class="rx-btn rx-btn-ghost rx-btn-sm"
                @click="cardBookmarked = !cardBookmarked"
              >
                {{ cardBookmarked ? '★ Saved' : '☆ Save' }}
              </button>
            </div>
            <p style="margin: 0 0 1rem; color: var(--vp-c-text-2); font-size: 0.875rem; line-height: 1.6;">
              Encapsulates metrics, interactive forms, and navigation surfaces with Resux design tokens and semantic elevation.
            </p>
            <div style="display: flex; gap: 0.5rem; justify-content: flex-end;">
              <button type="button" class="rx-btn rx-btn-secondary rx-btn-sm">Docs</button>
              <button type="button" class="rx-btn rx-btn-primary rx-btn-sm">Explore</button>
            </div>
          </div>
        </div>

        <!-- ==================== RxAlert ==================== -->
        <div v-else-if="currentComp === 'RxAlert'" class="rx-stage-inner" style="max-width: 520px; margin: 0 auto;">
          <div v-if="!alertDismissed" :class="`rx-alert rx-alert-${alertVariant}`" role="alert">
            <div class="rx-alert-title">Framework Parity Verification</div>
            <div class="rx-alert-content">
              All 21 package export specifiers validated against framework source in <code>scripts/check-framework-parity.mjs</code>.
            </div>
            <button
              type="button"
              class="rx-alert-close"
              title="Dismiss alert"
              @click="alertDismissed = true"
            >
              ✕
            </button>
          </div>
          <div v-else style="text-align: center; padding: 1rem;">
            <p style="font-size: 0.875rem; color: var(--vp-c-text-2); margin-bottom: 0.75rem;">
              The alert was dismissed.
            </p>
            <button
              type="button"
              class="rx-btn rx-btn-outline rx-btn-sm"
              @click="alertDismissed = false"
            >
              ↺ Restore Dismissed Alert
            </button>
          </div>
        </div>

        <!-- ==================== RxTabs ==================== -->
        <div v-else-if="currentComp === 'RxTabs'" class="rx-stage-inner" style="max-width: 520px; margin: 0 auto;">
          <div class="rx-tabs">
            <div class="rx-tabs-header">
              <button
                type="button"
                class="rx-tab-btn"
                :class="{ active: activeSubTab === 'ssr' }"
                @click="activeSubTab = 'ssr'"
              >
                SSR Stream
              </button>
              <button
                type="button"
                class="rx-tab-btn"
                :class="{ active: activeSubTab === 'vt' }"
                @click="activeSubTab = 'vt'"
              >
                View Transitions
              </button>
              <button
                type="button"
                class="rx-tab-btn"
                :class="{ active: activeSubTab === 'icons' }"
                @click="activeSubTab = 'icons'"
              >
                Static Icons
              </button>
            </div>
          </div>
          <div class="rx-card" style="margin-top: 1rem; padding: 1.25rem;">
            <strong style="color: var(--vp-c-brand-1); display: block; margin-bottom: 0.25rem;">
              {{ activeSubTab === 'ssr' ? '⚡ HTML-First Server Streaming' : activeSubTab === 'vt' ? '🎬 Native View Transitions' : '🎨 Compile-Time SVG Inlining' }}
            </strong>
            <p style="margin: 0; font-size: 0.875rem; color: var(--vp-c-text-2); line-height: 1.6;">
              {{ activeSubTab === 'ssr' ? 'Serializes state and event handlers during SSR so the browser resumes without full client hydration.' : activeSubTab === 'vt' ? 'Enables smooth, hardware-accelerated cross-route view transitions with declarative <ResuxLink view-transition>.' : 'Replaces icons with zero-KB footprint inline SVGs during compilation.' }}
            </p>
          </div>
        </div>

        <!-- ==================== RxAccordion ==================== -->
        <div v-else-if="currentComp === 'RxAccordion'" class="rx-stage-inner" style="max-width: 520px; margin: 0 auto;">
          <div class="rx-accordion">
            <button
              type="button"
              class="rx-accordion-header"
              :aria-expanded="accordionOpen"
              @click="accordionOpen = !accordionOpen"
            >
              <span>What is Resux Resumability?</span>
              <span class="rx-accordion-icon">{{ accordionOpen ? '−' : '+' }}</span>
            </button>
            <div v-if="accordionOpen" class="rx-accordion-body">
              Resux serializes component state and event handlers on the server so the browser can resume interactivity without re-executing component setup trees on load.
            </div>
          </div>
        </div>

        <!-- ==================== RxModal ==================== -->
        <div v-else-if="currentComp === 'RxModal'" class="rx-stage-inner rx-center-stage">
          <button
            type="button"
            class="rx-btn rx-btn-primary rx-btn-md"
            @click="modalOpen = true"
          >
            🪟 Open Modal Dialog
          </button>

          <!-- Accessible Dialog Overlay -->
          <div v-if="modalOpen" class="rx-modal-backdrop" @click.self="modalOpen = false">
            <div class="rx-modal-content" role="dialog" aria-modal="true">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
                <h3 style="margin: 0; font-size: 1.05rem;">Confirm Production Deploy</h3>
                <button
                  type="button"
                  class="rx-alert-close"
                  @click="modalOpen = false"
                >
                  ✕
                </button>
              </div>
              <p style="font-size: 0.875rem; color: var(--vp-c-text-2); margin: 0 0 1.25rem; line-height: 1.6;">
                Ready to deploy <code>resuxjs@0.4.0-beta.7</code> with signed Halal Core verification and View Transitions?
              </p>
              <div style="display: flex; justify-content: flex-end; gap: 0.5rem;">
                <button
                  type="button"
                  class="rx-btn rx-btn-ghost rx-btn-sm"
                  @click="modalOpen = false"
                >
                  Cancel
                </button>
                <button
                  type="button"
                  class="rx-btn rx-btn-primary rx-btn-sm"
                  @click="modalOpen = false"
                >
                  Confirm Deploy
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- ==================== RxTooltip & Popover ==================== -->
        <div v-else-if="currentComp === 'RxTooltip' || currentComp === 'RxPopover'" class="rx-stage-inner rx-center-stage">
          <div style="display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap; justify-content: center;">
            <div
              class="rx-tooltip-wrapper"
              @mouseenter="tooltipHover = true"
              @mouseleave="tooltipHover = false"
            >
              <button type="button" class="rx-btn rx-btn-outline rx-btn-sm">
                Hover for Tooltip
              </button>
              <div v-if="tooltipHover" class="rx-tooltip rx-tooltip-top" role="tooltip">
                Zero-CLS Fontaine metric overrides active
              </div>
            </div>

            <div class="rx-popover">
              <button
                type="button"
                class="rx-btn rx-btn-secondary rx-btn-sm"
                @click="popoverOpen = !popoverOpen"
              >
                {{ popoverOpen ? 'Close Popover' : 'Open Popover ▾' }}
              </button>
              <div v-if="popoverOpen" class="rx-popover-content" style="min-width: 14rem;">
                <strong>Popover Surface</strong>
                <p style="margin: 0.35rem 0 0; font-size: 0.8rem; color: var(--vp-c-text-2);">
                  Toggled via the <code>#trigger</code> slot and <code>update:open</code> event.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- ==================== Default / Fallback ==================== -->
        <div v-else class="rx-stage-inner rx-center-stage">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span class="rx-badge rx-badge-success">✓ {{ currentComp }} Ready</span>
            <button
              type="button"
              class="rx-btn rx-btn-secondary rx-btn-sm"
              @click="motionKey++"
            >
              Test Action
            </button>
          </div>
        </div>
      </div>

      <!-- ==================== Interactive Controls Panel ==================== -->
      <div class="rx-controls-panel">
        <div class="rx-controls-header">
          <div class="rx-controls-heading">
            <span class="rx-controls-icon">⚙️</span>
            <span>Component Controls &amp; State</span>
          </div>
          <button
            v-if="currentComp === 'RxButton'"
            type="button"
            class="rx-reset-btn"
            @click="resetBtnProps"
          >
            ↺ Reset
          </button>
        </div>

        <!-- Controls for RxButton -->
        <div v-if="currentComp === 'RxButton'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">VARIANT</label>
            <div class="rx-segmented-control">
              <button
                v-for="v in (['primary', 'secondary', 'outline', 'ghost'] as const)"
                :key="v"
                type="button"
                class="rx-seg-btn"
                :class="{ active: btnVariant === v }"
                @click="btnVariant = v"
              >
                {{ v }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">SIZE</label>
            <div class="rx-segmented-control">
              <button
                v-for="s in (['sm', 'md', 'lg'] as const)"
                :key="s"
                type="button"
                class="rx-seg-btn"
                :class="{ active: btnSize === s }"
                @click="btnSize = s"
              >
                {{ s.toUpperCase() }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">STATE TOGGLES</label>
            <div class="rx-toggle-chips">
              <button
                type="button"
                class="rx-chip-toggle"
                :class="{ active: btnDisabled }"
                @click="btnDisabled = !btnDisabled"
              >
                {{ btnDisabled ? '✓ Disabled' : 'Disabled' }}
              </button>
              <button
                type="button"
                class="rx-chip-toggle"
                :class="{ active: btnLoading }"
                @click="btnLoading = !btnLoading"
              >
                {{ btnLoading ? '✓ Loading' : 'Loading' }}
              </button>
              <button
                type="button"
                class="rx-chip-toggle"
                :class="{ active: btnWithIcon }"
                @click="btnWithIcon = !btnWithIcon"
              >
                {{ btnWithIcon ? '✓ Icon: ⚡' : 'With Icon' }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxInput -->
        <div v-else-if="currentComp === 'RxInput'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">INPUT TYPE</label>
            <div class="rx-segmented-control">
              <button
                v-for="t in (['email', 'text', 'password', 'search'] as const)"
                :key="t"
                type="button"
                class="rx-seg-btn"
                :class="{ active: inputType === t }"
                @click="inputType = t"
              >
                {{ t }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">VALIDATION STATUS</label>
            <div class="rx-segmented-control">
              <button
                v-for="st in (['default', 'success', 'error'] as const)"
                :key="st"
                type="button"
                class="rx-seg-btn"
                :class="{ active: inputStatus === st }"
                @click="inputStatus = st"
              >
                {{ st }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">STATE</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: inputDisabled }"
              @click="inputDisabled = !inputDisabled"
            >
              {{ inputDisabled ? '✓ Disabled' : 'Disabled' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxVerificationCode -->
        <div v-else-if="currentComp === 'RxVerificationCode'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">VERIFICATION STATUS</label>
            <div class="rx-segmented-control">
              <button
                v-for="s in (['idle', 'verifying', 'success', 'error'] as const)"
                :key="s"
                type="button"
                class="rx-seg-btn"
                :class="{ active: otpStatus === s }"
                @click="otpStatus = s"
              >
                {{ s }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">MASK DIGITS</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: otpMask }"
              @click="otpMask = !otpMask"
            >
              {{ otpMask ? '✓ Masked (••••)' : 'Visible (2026)' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxCard -->
        <div v-else-if="currentComp === 'RxCard'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">SURFACE VARIANT</label>
            <div class="rx-segmented-control">
              <button
                v-for="v in (['default', 'elevated', 'outlined', 'subtle'] as const)"
                :key="v"
                type="button"
                class="rx-seg-btn"
                :class="{ active: cardVariant === v }"
                @click="cardVariant = v"
              >
                {{ v }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxBadge -->
        <div v-else-if="currentComp === 'RxBadge'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">BADGE VARIANT</label>
            <div class="rx-segmented-control">
              <button
                v-for="v in (['default', 'primary', 'success', 'warning', 'error'] as const)"
                :key="v"
                type="button"
                class="rx-seg-btn"
                :class="{ active: badgeVariant === v }"
                @click="badgeVariant = v"
              >
                {{ v }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">INDICATOR DOT</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: badgeWithDot }"
              @click="badgeWithDot = !badgeWithDot"
            >
              {{ badgeWithDot ? '✓ Dot Active' : 'No Dot' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxAlert -->
        <div v-else-if="currentComp === 'RxAlert'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ALERT SEVERITY</label>
            <div class="rx-segmented-control">
              <button
                v-for="v in (['info', 'success', 'warning', 'error'] as const)"
                :key="v"
                type="button"
                class="rx-seg-btn"
                :class="{ active: alertVariant === v }"
                @click="alertVariant = v"
              >
                {{ v }}
              </button>
            </div>
          </div>
        </div>

        <!-- Generic / Fallback Controls -->
        <div v-else class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ACTIVE PRIMITIVE</label>
            <span style="font-size: 0.85rem; color: var(--vp-c-brand-1); font-weight: 700;">
              {{ currentComp }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. Runnable Vue SFC Code View -->
    <div v-else-if="viewMode === 'code'" class="rx-code-panel">
      <div class="rx-code-header">
        <span>Vue SFC Code (Reactive to current props)</span>
        <button
          type="button"
          class="rx-copy-code-btn"
          @click="copyCode(generatedVueCode)"
        >
          {{ codeCopied ? '✅ Copied!' : '📋 Copy Code' }}
        </button>
      </div>
      <pre class="rx-code-block"><code>{{ generatedVueCode }}</code></pre>
    </div>

    <!-- 3. Rendered DOM Inspection View -->
    <div v-else-if="viewMode === 'dom'" class="rx-code-panel">
      <div class="rx-code-header">
        <span>Rendered HTML Output (Default <code>rx-*</code> Utility Tokens)</span>
        <button
          type="button"
          class="rx-copy-code-btn"
          @click="copyCode(generatedDomHtml)"
        >
          {{ codeCopied ? '✅ Copied!' : '📋 Copy Markup' }}
        </button>
      </div>
      <pre class="rx-code-block"><code>{{ generatedDomHtml }}</code></pre>
    </div>
  </div>
</template>

<style scoped>
/* ==========================================================================
   Modern, Interactive, 100% Responsive UI Component Preview Card
   ========================================================================== */
.rx-preview-container {
  margin: 1.5rem 0;
  border-radius: 16px;
  border: 1px solid var(--resux-border);
  background: var(--resux-surface);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05), var(--resux-shadow-sm);
  overflow: hidden;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.dark .rx-preview-container {
  background: var(--resux-surface-strong);
  border-color: color-mix(in srgb, var(--vp-c-brand-1) 22%, var(--resux-border));
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.25);
}

/* Header Toolbar */
.rx-preview-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 18px;
  background: var(--resux-surface-muted);
  border-bottom: 1px solid var(--resux-border);
}

.rx-preview-title-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.rx-preview-badge {
  display: inline-flex;
  align-items: center;
  padding: 3px 10px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 750;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  background: rgba(109, 93, 252, 0.15);
  color: var(--vp-c-brand-1);
  border: 1px solid rgba(109, 93, 252, 0.28);
}

.rx-preview-title {
  margin: 0 !important;
  font-size: 0.95rem !important;
  font-weight: 700 !important;
  color: var(--vp-c-text-1) !important;
  line-height: 1.2 !important;
}

.rx-preview-pkg-tag {
  font-family: var(--vp-font-family-mono);
  font-size: 11px;
  color: var(--vp-c-text-3);
  padding: 2px 6px;
  background: var(--resux-surface);
  border-radius: 4px;
  border: 1px solid var(--resux-border);
}

/* Mode Switcher Tabs */
.rx-preview-mode-tabs {
  display: inline-flex;
  align-items: center;
  background: var(--resux-surface);
  padding: 3px;
  border-radius: 10px;
  border: 1px solid var(--resux-border);
  gap: 2px;
}

.rx-mode-tab {
  padding: 5px 12px;
  font-size: 12px;
  font-weight: 650;
  border-radius: 7px;
  border: none;
  background: transparent;
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.rx-mode-tab:hover:not(.active) {
  color: var(--vp-c-text-1);
  background: var(--resux-surface-muted);
}

.rx-mode-tab.active {
  background: var(--vp-c-brand-1);
  color: #ffffff !important;
  box-shadow: 0 2px 8px rgba(109, 93, 252, 0.35);
}

/* Suite Selector Tray */
.rx-suite-tray {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 18px;
  background: var(--resux-surface);
  border-bottom: 1px solid var(--resux-border);
  overflow: hidden;
}

.rx-suite-tray-label {
  font-size: 11px;
  font-weight: 750;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--vp-c-text-3);
  white-space: nowrap;
}

.rx-suite-tray-scroll {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
  padding-bottom: 2px;
}

.rx-suite-tray-scroll::-webkit-scrollbar {
  display: none;
}

.rx-suite-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 600;
  border: 1px solid var(--resux-border);
  background: var(--resux-surface-muted);
  color: var(--vp-c-text-2);
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s ease;
}

.rx-suite-pill:hover:not(.active) {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-text-1);
}

.rx-suite-pill.active {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  font-weight: 750;
  box-shadow: 0 0 0 1px var(--vp-c-brand-1);
}

/* Preview Canvas Stage */
.rx-preview-stage {
  position: relative;
  min-height: 170px;
  padding: 36px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--resux-surface);
  background-image: radial-gradient(circle, var(--resux-border) 1px, transparent 1px);
  background-size: 20px 20px;
}

.dark .rx-preview-stage {
  background-color: rgba(11, 15, 25, 0.4);
}

.rx-stage-inner {
  width: 100%;
}

.rx-center-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.rx-stage-hero-item {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px;
}

.rx-icon-inline {
  display: inline-block;
  margin-right: 4px;
}

.rx-spinner-inline {
  display: inline-block;
  animation: spin 1s linear infinite;
  margin-right: 4px;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Live Event Feedback Bar */
.rx-stage-feedback {
  margin-top: 18px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 12px;
  border-radius: 9999px;
  background: var(--resux-surface-muted);
  border: 1px solid var(--resux-border);
  font-size: 11px;
  color: var(--vp-c-text-2);
}

.rx-feedback-indicator {
  width: 6px;
  height: 6px;
  border-radius: 9999px;
  background: #10b981;
}

.rx-feedback-indicator.pulse {
  animation: pulse-dot 1.2s ease infinite;
}

@keyframes pulse-dot {
  0% { transform: scale(0.9); opacity: 0.6; }
  50% { transform: scale(1.4); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.6; }
}

.rx-feedback-counter {
  font-weight: 750;
  color: var(--vp-c-brand-1);
}

/* Form Group Demo */
.rx-form-group {
  max-width: 380px;
  margin: 0 auto;
}

.rx-form-label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
  font-size: 12px;
  font-weight: 650;
  color: var(--vp-c-text-1);
}

.rx-label-status.success {
  color: #10b981;
  font-weight: 600;
}

.rx-label-status.error {
  color: #ef4444;
  font-weight: 600;
}

.rx-input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.rx-input-clear {
  position: absolute;
  right: 10px;
  border: none;
  background: transparent;
  color: var(--vp-c-text-3);
  font-size: 12px;
  cursor: pointer;
  padding: 2px 6px;
  border-radius: 4px;
}

.rx-input-clear:hover {
  color: var(--vp-c-text-1);
  background: var(--resux-surface-muted);
}

.rx-form-hint {
  margin-top: 6px;
  font-size: 11px;
  color: var(--vp-c-text-3);
}

/* OTP Quick Actions */
.rx-otp-quick-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  justify-content: center;
}

.rx-pill-action {
  padding: 4px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 600;
  border: 1px solid var(--resux-border);
  background: var(--resux-surface);
  color: var(--vp-c-text-1);
  cursor: pointer;
  transition: all 0.15s ease;
}

.rx-pill-action:hover {
  border-color: var(--vp-c-brand-1);
}

.rx-pill-action.primary {
  background: var(--vp-c-brand-1);
  color: #ffffff;
  border-color: var(--vp-c-brand-1);
}

/* Switch Demo Card */
.rx-switch-demo-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 16px 20px;
  border-radius: 12px;
  background: var(--resux-surface-muted);
  border: 1px solid var(--resux-border);
  max-width: 440px;
  width: 100%;
}

.rx-switch-demo-title {
  display: block;
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
  margin-bottom: 2px;
}

.rx-switch-demo-desc {
  margin: 0;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  line-height: 1.4;
}

/* Controls Panel */
.rx-controls-panel {
  border-top: 1px solid var(--resux-border);
  background: var(--resux-surface-muted);
  padding: 16px 20px;
}

.rx-controls-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.rx-controls-heading {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 750;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--vp-c-text-2);
}

.rx-controls-icon {
  font-size: 13px;
}

.rx-reset-btn {
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 6px;
  border: 1px solid var(--resux-border);
  background: var(--resux-surface);
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.15s ease;
}

.rx-reset-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.rx-controls-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 14px;
  align-items: start;
}

.rx-control-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.rx-control-label {
  font-size: 11px;
  font-weight: 750;
  color: var(--vp-c-text-3);
  letter-spacing: 0.04em;
}

.rx-segmented-control {
  display: inline-flex;
  flex-wrap: wrap;
  gap: 3px;
  background: var(--resux-surface);
  padding: 3px;
  border-radius: 9px;
  border: 1px solid var(--resux-border);
}

.rx-seg-btn {
  padding: 4px 10px;
  font-size: 12px;
  font-weight: 600;
  border-radius: 6px;
  border: none;
  background: transparent;
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.14s ease;
}

.rx-seg-btn:hover:not(.active) {
  color: var(--vp-c-text-1);
  background: var(--resux-surface-muted);
}

.rx-seg-btn.active {
  background: var(--vp-c-brand-1);
  color: #ffffff !important;
  font-weight: 750;
  box-shadow: 0 1px 4px rgba(109, 93, 252, 0.3);
}

.rx-toggle-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.rx-chip-toggle {
  padding: 5px 10px;
  font-size: 12px;
  font-weight: 600;
  border-radius: 8px;
  border: 1px solid var(--resux-border);
  background: var(--resux-surface);
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.14s ease;
}

.rx-chip-toggle:hover:not(.active) {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-text-1);
}

.rx-chip-toggle.active {
  background: var(--vp-c-brand-soft);
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  font-weight: 700;
}

/* Code & DOM Panels */
.rx-code-panel {
  padding: 16px;
  background: var(--resux-surface-muted);
}

.rx-code-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 12px;
  color: var(--vp-c-text-2);
  font-weight: 650;
}

.rx-copy-code-btn {
  padding: 4px 12px;
  border-radius: 6px;
  border: 1px solid var(--resux-border);
  background: var(--resux-surface);
  color: var(--vp-c-text-1);
  font-size: 12px;
  font-weight: 650;
  cursor: pointer;
  transition: all 0.15s ease;
}

.rx-copy-code-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.rx-code-block {
  margin: 0 !important;
  padding: 14px 16px !important;
  border-radius: 10px !important;
  background: var(--resux-surface) !important;
  border: 1px solid var(--resux-border) !important;
  font-family: var(--vp-font-family-mono) !important;
  font-size: 12.5px !important;
  line-height: 1.6 !important;
  color: var(--vp-c-text-1) !important;
  overflow-x: auto;
}

/* Modal Dialog */
.rx-modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
  padding: 16px;
}

.rx-modal-content {
  background: var(--resux-surface);
  border: 1px solid var(--resux-border);
  border-radius: 16px;
  padding: 24px;
  max-width: 440px;
  width: 100%;
  box-shadow: 0 20px 48px rgba(0, 0, 0, 0.35);
}

/* ==========================================================================
   Responsive Adaptations
   ========================================================================== */
@media (max-width: 768px) {
  .rx-preview-header {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }

  .rx-preview-mode-tabs {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }

  .rx-mode-tab {
    text-align: center;
    padding: 6px 4px;
    font-size: 11px;
  }

  .rx-controls-grid {
    grid-template-columns: 1fr;
  }

  .rx-preview-stage {
    padding: 24px 12px;
  }
}
</style>
