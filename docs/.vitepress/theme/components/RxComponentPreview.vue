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
  { id: 'RxButton', name: 'Button' },
  { id: 'RxInput', name: 'Input' },
  { id: 'RxSelect', name: 'Select' },
  { id: 'RxTextarea', name: 'Textarea' },
  { id: 'RxDatePicker', name: 'DatePicker' },
  { id: 'RxVerificationCode', name: 'OTP Code' },
  { id: 'RxSwitch', name: 'Switch' },
  { id: 'RxBadge', name: 'Badge' },
  { id: 'RxCard', name: 'Card' },
  { id: 'RxAvatar', name: 'Avatar' },
  { id: 'RxAlert', name: 'Alert' },
  { id: 'RxSkeleton', name: 'Skeleton' },
  { id: 'RxDivider', name: 'Divider' },
  { id: 'RxKbd', name: 'Kbd' },
  { id: 'RxAccordion', name: 'Accordion' },
  { id: 'RxTabs', name: 'Tabs' },
  { id: 'RxModal', name: 'Modal' },
  { id: 'RxPopover', name: 'Popover' },
  { id: 'RxDropdown', name: 'Dropdown' },
  { id: 'RxTooltip', name: 'Tooltip' },
  { id: 'RxMotion', name: 'Motion' },
  { id: 'RxIcon', name: 'Icon' },
  { id: 'Teleport', name: 'Teleport' },
  { id: 'Transition', name: 'Transition' }
]

const componentIcons: Record<string, string> = {
  RxButton: '<rect x="3" y="6" width="18" height="12" rx="3"/><path d="M8 12h8"/>',
  RxInput: '<rect x="3" y="5" width="18" height="14" rx="2"/><line x1="7" y1="12" x2="11" y2="12"/>',
  RxSelect: '<path d="M6 9l6 6 6-6"/>',
  RxTextarea: '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="7" y1="8" x2="17" y2="8"/><line x1="7" y1="12" x2="17" y2="12"/>',
  RxDatePicker: '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
  RxVerificationCode: '<rect x="2" y="6" width="4" height="12" rx="1"/><rect x="8" y="6" width="4" height="12" rx="1"/><rect x="14" y="6" width="4" height="12" rx="1"/><rect x="20" y="6" width="4" height="12" rx="1"/>',
  RxSwitch: '<rect x="2" y="6" width="20" height="12" rx="6"/><circle cx="16" cy="12" r="3"/>',
  RxBadge: '<path d="M12 2l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/>',
  RxCard: '<rect x="3" y="3" width="18" height="18" rx="3"/><line x1="3" y1="9" x2="21" y2="9"/>',
  RxAvatar: '<circle cx="12" cy="8" r="4"/><path d="M20 21a8 8 0 1 0-16 0"/>',
  RxAlert: '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>',
  RxSkeleton: '<rect x="3" y="4" width="18" height="4" rx="1"/><rect x="3" y="10" width="14" height="4" rx="1"/><rect x="3" y="16" width="10" height="4" rx="1"/>',
  RxDivider: '<line x1="3" y1="12" x2="21" y2="12"/>',
  RxKbd: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 10h2M11 10h2M15 10h2M8 14h8"/>',
  RxAccordion: '<path d="M4 6h16M4 12h16M4 18h16"/>',
  RxTabs: '<path d="M3 6h7l2 3h9v9a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z"/>',
  RxModal: '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>',
  RxPopover: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
  RxDropdown: '<polyline points="6 9 12 15 18 9"/>',
  RxTooltip: '<circle cx="12" cy="12" r="10"/><path d="M9 9a3 3 0 0 1 6 0c0 2-3 3-3 3"/><circle cx="12" cy="17" r="1"/>',
  RxMotion: '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>',
  RxIcon: '<circle cx="12" cy="12" r="10"/><polygon points="12 8 8 16 16 16"/>',
  Teleport: '<polyline points="13 2 13 9 20 9"/><path d="M22 13v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h8"/>',
  Transition: '<circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/>'
}

// Current component to render
const currentComp = computed(() => (isSuite.value ? activeComponent.value : props.component || 'RxButton'))

// View mode tabs
const viewMode = ref<'preview' | 'code' | 'dom'>('preview')
const codeCopied = ref(false)

// Global interaction feedback message
const feedbackMessage = ref('')
let feedbackTimer: ReturnType<typeof setTimeout> | undefined
function setFeedback(msg: string) {
  feedbackMessage.value = msg
  if (feedbackTimer) clearTimeout(feedbackTimer)
  feedbackTimer = setTimeout(() => { feedbackMessage.value = '' }, 3000)
}

// 1. Button State
const btnVariant = ref<'primary' | 'secondary' | 'outline' | 'ghost'>('primary')
const btnSize = ref<'sm' | 'md' | 'lg'>('md')
const btnDisabled = ref(false)
const btnLoading = ref(false)
const btnWithIcon = ref(false)
const btnClickCount = ref(0)
function handleBtnClick() {
  if (btnDisabled.value || btnLoading.value) return
  btnClickCount.value++
  setFeedback(`@click fired: count is ${btnClickCount.value}`)
}

// 2. Input State
const inputVal = ref('mahmoud@resux.dev')
const inputType = ref<'text' | 'email' | 'password' | 'search'>('email')
const inputStatus = ref<'default' | 'success' | 'error'>('default')
const inputDisabled = ref(false)

// 3. Select State
const selectVal = ref('eu-central-1')
const selectDisabled = ref(false)
const selectOptions = [
  { label: 'Frankfurt (eu-central-1)', value: 'eu-central-1' },
  { label: 'London (eu-west-2)', value: 'eu-west-2' },
  { label: 'US East (us-east-1)', value: 'us-east-1' },
  { label: 'Tokyo (ap-northeast-1)', value: 'ap-northeast-1' }
]

// 4. Textarea State
const textareaVal = ref('Resux 0.4.0-beta.7 introduces native View Transitions, compile-time SVG icons, and Zero-CLS font fallback metrics.')
const textareaRows = ref(3)
const textareaDisabled = ref(false)

// 5. DatePicker State
const dateVal = ref('2026-11-20')
const dateDisabled = ref(false)

// 6. Verification Code State
const otpVal = ref('2026')
const otpStatus = ref<'idle' | 'verifying' | 'success' | 'error'>('idle')
const otpMask = ref(false)
const otpDigits = ref(4)
const otpFocused = ref(false)
const otpInputRef = ref<HTMLInputElement | null>(null)

const otpCells = computed(() => {
  const chars = otpVal.value.slice(0, otpDigits.value).split('')
  return Array.from({ length: otpDigits.value }).map((_, i) => chars[i] || '')
})

function focusOtpInput() {
  otpInputRef.value?.focus()
  otpFocused.value = true
}

function handleOtpInput(event: Event) {
  const target = event.target as HTMLInputElement
  const sanitized = target.value.replace(/\D/g, '').slice(0, otpDigits.value)
  otpVal.value = sanitized
  target.value = sanitized
  otpStatus.value = 'idle'
  setFeedback(`Typed code: "${sanitized}" (${sanitized.length}/${otpDigits.value})`)
  if (sanitized.length === otpDigits.value) {
    simulateOtpVerify()
  }
}

function simulateOtpFill(code: string) {
  otpVal.value = code
  otpStatus.value = 'idle'
  if (otpInputRef.value) otpInputRef.value.value = code
  setFeedback(`Pasted OTP: "${code}"`)
  focusOtpInput()
}
function simulateOtpVerify() {
  otpStatus.value = 'verifying'
  setFeedback('Verifying code with server HMAC...')
  setTimeout(() => {
    if (otpVal.value === '2026') {
      otpStatus.value = 'success'
      setFeedback('Code verified successfully!')
    } else {
      otpStatus.value = 'error'
      setFeedback('Verification failed. Try "2026"')
    }
  }, 700)
}

// 7. Switch State
const switchVal = ref(true)
const switchDisabled = ref(false)

// 8. Card State
const cardVariant = ref<'default' | 'elevated' | 'outlined' | 'subtle'>('elevated')
const cardBookmarked = ref(false)

// 9. Badge State
const badgeVariant = ref<'default' | 'primary' | 'success' | 'warning' | 'error'>('primary')
const badgeWithDot = ref(true)

// 10. Avatar State
const avatarSize = ref<'sm' | 'md' | 'lg'>('md')
const avatarStatus = ref<'online' | 'busy' | 'away' | 'none'>('online')

// 11. Alert State
const alertDismissed = ref(false)
const alertVariant = ref<'info' | 'success' | 'warning' | 'error'>('info')

// 12. Skeleton State
const skeletonType = ref<'card' | 'text' | 'circle'>('card')

// 13. Divider State
const dividerLabel = ref('RESUMABILITY BOUNDARY')
const dividerOrientation = ref<'horizontal' | 'vertical'>('horizontal')

// 14. Kbd State
const kbdOs = ref<'mac' | 'win'>('mac')

// 15. Tabs & Accordion State
const activeSubTab = ref<'ssr' | 'vt' | 'icons'>('ssr')
const accordionOpen = ref(true)

// 16. Modal State
const modalOpen = ref(false)
const modalTitle = ref('Confirm Production Deploy')

// 17. Tooltip & Popover & Dropdown State
const tooltipHover = ref(false)
const tooltipPlacement = ref<'top' | 'bottom' | 'left' | 'right'>('top')
const popoverOpen = ref(false)
const dropdownOpen = ref(false)

// 18. Motion & Reveal & AutoAnimate State
const motionKey = ref(1)
const motionPreset = ref<'fade-up' | 'scale-in' | 'slide-in-left' | 'pulse-glow'>('fade-up')
const autoItems = ref(['@resuxjs/runtime', '@resuxjs/ui', '@resuxjs/icons', '@resuxjs/fonts'])
function addAutoItem() {
  autoItems.value.push(`@resuxjs/pkg-${autoItems.value.length + 1}`)
  setFeedback(`Added item #${autoItems.value.length}`)
}
function resetAutoItems() {
  autoItems.value = ['@resuxjs/runtime', '@resuxjs/ui', '@resuxjs/icons', '@resuxjs/fonts']
  setFeedback('Reset package list')
}
function removeAutoItem(index: number) {
  autoItems.value.splice(index, 1)
  setFeedback('Removed package')
}

// 19. Icon State
const iconName = ref<'check' | 'rocket' | 'zap' | 'shield'>('check')
const iconSize = ref<'20px' | '28px' | '36px' | '48px'>('28px')

// 20. Teleport State
const teleportActive = ref(true)

// 21. Transition State
const transitionShow = ref(true)
const transitionEffect = ref<'fade' | 'scale' | 'slide'>('fade')

// Reset all props for the current active component
function resetCurrentComp() {
  btnVariant.value = 'primary'
  btnSize.value = 'md'
  btnDisabled.value = false
  btnLoading.value = false
  btnWithIcon.value = false
  btnClickCount.value = 0

  inputVal.value = 'mahmoud@resux.dev'
  inputStatus.value = 'default'
  inputDisabled.value = false

  selectVal.value = 'eu-central-1'
  selectDisabled.value = false

  otpVal.value = '2026'
  otpStatus.value = 'idle'
  otpMask.value = false
  otpDigits.value = 4

  switchVal.value = true
  switchDisabled.value = false
  cardVariant.value = 'elevated'
  badgeVariant.value = 'primary'
  badgeWithDot.value = true
  avatarSize.value = 'md'
  avatarStatus.value = 'online'
  alertDismissed.value = false
  alertVariant.value = 'info'
  skeletonType.value = 'card'
  dividerLabel.value = 'RESUMABILITY BOUNDARY'
  dividerOrientation.value = 'horizontal'
  kbdOs.value = 'mac'
  activeSubTab.value = 'ssr'
  accordionOpen.value = true
  modalOpen.value = false
  popoverOpen.value = false
  dropdownOpen.value = false
  tooltipPlacement.value = 'top'
  iconName.value = 'check'
  iconSize.value = '28px'
  teleportActive.value = true
  transitionShow.value = true
  transitionEffect.value = 'fade'
  motionPreset.value = 'fade-up'
  motionKey.value++
  resetAutoItems()
  setFeedback('Reset component properties to standard defaults')
}

// Generate Dynamic Vue Code
const generatedVueCode = computed(() => {
  const c = currentComp.value
  if (c === 'RxButton') {
    const p: string[] = []
    if (btnVariant.value !== 'primary') p.push(`variant="${btnVariant.value}"`)
    if (btnSize.value !== 'md') p.push(`size="${btnSize.value}"`)
    if (btnDisabled.value) p.push(':disabled="true"')
    if (btnLoading.value) p.push(':loading="true"')
    const icon = btnWithIcon.value ? '<span class="icon">⚡</span> ' : ''
    return `<template>\n  <RxButton${p.length ? ' ' + p.join(' ') : ''} @click="onClick">\n    ${icon}Deploy Application\n  </RxButton>\n</template>\n\n<script setup lang="ts">\nimport { RxButton } from 'resuxjs/ui'\n\nfunction onClick() {\n  console.log('Button clicked!')\n}\n<\/script>`
  } else if (c === 'RxInput') {
    return `<template>\n  <RxInput\n    v-model="email"\n    type="${inputType.value}"\n    placeholder="Enter work email..."\n    :disabled="${inputDisabled.value}"\n  />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxInput } from 'resuxjs/ui'\n\nconst email = ref('${inputVal.value}')\n<\/script>`
  } else if (c === 'RxSelect') {
    return `<template>\n  <RxSelect\n    v-model="region"\n    :options="regions"\n    placeholder="Select deployment region"\n  />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxSelect } from 'resuxjs/ui'\n\nconst region = ref('${selectVal.value}')\nconst regions = [\n  { label: 'Frankfurt (eu-central-1)', value: 'eu-central-1' },\n  { label: 'London (eu-west-2)', value: 'eu-west-2' },\n  { label: 'US East (us-east-1)', value: 'us-east-1' }\n]\n<\/script>`
  } else if (c === 'RxTextarea') {
    return `<template>\n  <RxTextarea\n    v-model="notes"\n    :rows="${textareaRows.value}"\n    placeholder="Type release notes..."\n  />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxTextarea } from 'resuxjs/ui'\n\nconst notes = ref('${textareaVal.value}')\n<\/script>`
  } else if (c === 'RxDatePicker') {
    return `<template>\n  <RxDatePicker\n    v-model="targetDate"\n    placeholder="Target launch date"\n  />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxDatePicker } from 'resuxjs/ui'\n\nconst targetDate = ref('${dateVal.value}')\n<\/script>`
  } else if (c === 'RxVerificationCode') {
    return `<template>\n  <RxVerificationCode\n    v-model="otp"\n    :length="${otpDigits.value}"\n    :mask="${otpMask.value}"\n    :status="${otpStatus.value}"\n    @complete="verifyOtp"\n  />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxVerificationCode } from 'resuxjs/ui'\n\nconst otp = ref('${otpVal.value}')\nfunction verifyOtp(code: string) {\n  console.log('Verifying code:', code)\n}\n<\/script>`
  } else if (c === 'RxSwitch') {
    return `<template>\n  <RxSwitch v-model="enabled">\n    {{ enabled ? 'Transitions Active' : 'Transitions Off' }}\n  </RxSwitch>\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxSwitch } from 'resuxjs/ui'\n\nconst enabled = ref(${switchVal.value})\n<\/script>`
  } else if (c === 'RxCard') {
    return `<template>\n  <RxCard variant="${cardVariant.value}">\n    <template #header>\n      <h3>Production Health</h3>\n    </template>\n    <p>All 21 public exports validated against runtime test suites.</p>\n  </RxCard>\n</template>\n\n<script setup lang="ts">\nimport { RxCard } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxBadge') {
    return `<template>\n  <RxBadge variant="${badgeVariant.value}"${badgeWithDot.value ? ' :dot="true"' : ''}>\n    Status: Active\n  </RxBadge>\n</template>\n\n<script setup lang="ts">\nimport { RxBadge } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxAvatar') {
    return `<template>\n  <RxAvatar alt="Mahmoud Mohamed" size="${avatarSize.value}" status="${avatarStatus.value !== 'none' ? avatarStatus.value : ''}" />\n</template>\n\n<script setup lang="ts">\nimport { RxAvatar } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxAlert') {
    return `<template>\n  <RxAlert variant="${alertVariant.value}" :dismissible="true" @dismiss="onDismiss">\n    <template #title>Deployment Notice</template>\n    Native View Transitions and Zero-CLS font preloading active.\n  </RxAlert>\n</template>\n\n<script setup lang="ts">\nimport { RxAlert } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxSkeleton') {
    return `<template>\n  <RxSkeleton width="100%" height="2rem" rounded="0.5rem" />\n</template>\n\n<script setup lang="ts">\nimport { RxSkeleton } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxDivider') {
    return `<template>\n  <RxDivider label="${dividerLabel.value}" orientation="${dividerOrientation.value}" />\n</template>\n\n<script setup lang="ts">\nimport { RxDivider } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxKbd') {
    return `<template>\n  <div class="shortcut">\n    <span>Command Palette</span>\n    <RxKbd>${kbdOs.value === 'mac' ? '⌘' : 'Ctrl'}</RxKbd> + <RxKbd>K</RxKbd>\n  </div>\n</template>\n\n<script setup lang="ts">\nimport { RxKbd } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxAccordion') {
    return `<template>\n  <RxAccordion v-model:open="isOpen" title="What is Resux Resumability?">\n    Resux serializes component state and event handlers during SSR.\n  </RxAccordion>\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxAccordion } from 'resuxjs/ui'\n\nconst isOpen = ref(${accordionOpen.value})\n<\/script>`
  } else if (c === 'RxTabs') {
    return `<template>\n  <RxTabs v-model="tab" :items="tabs" />\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxTabs } from 'resuxjs/ui'\n\nconst tab = ref('${activeSubTab.value}')\nconst tabs = [\n  { label: 'SSR Stream', key: 'ssr' },\n  { label: 'View Transitions', key: 'vt' },\n  { label: 'Static Icons', key: 'icons' }\n]\n<\/script>`
  } else if (c === 'RxModal') {
    return `<template>\n  <RxButton @click="open = true">Open Confirm Dialog</RxButton>\n  <RxModal v-model:open="open" title="${modalTitle.value}">\n    <p>Deploy resuxjs@0.4.0-beta.7 to production?</p>\n  </RxModal>\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxModal, RxButton } from 'resuxjs/ui'\n\nconst open = ref(${modalOpen.value})\n<\/script>`
  } else if (c === 'RxDropdown') {
    return `<template>\n  <RxDropdown :items="menuItems" v-model:open="isOpen">\n    <template #trigger>\n      <RxButton variant="secondary">Actions Menu ▾</RxButton>\n    </template>\n  </RxDropdown>\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxDropdown, RxButton } from 'resuxjs/ui'\n\nconst isOpen = ref(${dropdownOpen.value})\nconst menuItems = [\n  { label: 'Verify Framework', action: () => console.log('Verify') },\n  { label: 'Deploy Production', action: () => console.log('Deploy') }\n]\n<\/script>`
  } else if (c === 'RxTooltip') {
    return `<template>\n  <RxTooltip text="Zero-CLS Fontaine fallback metrics enabled" placement="${tooltipPlacement.value}">\n    <RxButton variant="outline">Hover or Focus</RxButton>\n  </RxTooltip>\n</template>\n\n<script setup lang="ts">\nimport { RxTooltip, RxButton } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxPopover') {
    return `<template>\n  <RxPopover v-model:open="isOpen">\n    <template #trigger>\n      <RxButton variant="outline">Toggle Popover</RxButton>\n    </template>\n    <p>Rich interactive popover surface content.</p>\n  </RxPopover>\n</template>\n\n<script setup lang="ts">\nimport { ref } from 'resuxjs'\nimport { RxPopover, RxButton } from 'resuxjs/ui'\n\nconst isOpen = ref(${popoverOpen.value})\n<\/script>`
  } else if (c === 'RxIcon') {
    return `<template>\n  <RxIcon name="${iconName.value}" size="${iconSize.value}" />\n</template>\n\n<script setup lang="ts">\nimport { RxIcon } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxMotion' || c === 'RxReveal') {
    return `<template>\n  <RxMotion preset="${motionPreset.value}">\n    <div class="card">Smooth animated surface</div>\n  </RxMotion>\n</template>\n\n<script setup lang="ts">\nimport { RxMotion } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'RxAutoAnimate') {
    return `<template>\n  <RxAutoAnimate>\n    <div v-for="item in items" :key="item">{{ item }}</div>\n  </RxAutoAnimate>\n</template>\n\n<script setup lang="ts">\nimport { RxAutoAnimate } from 'resuxjs/ui'\n<\/script>`
  } else if (c === 'Teleport') {
    return `<template>\n  <Teleport to="#teleport-target" :disabled="${!teleportActive.value}">\n    <div class="banner">Teleported notification banner</div>\n  </Teleport>\n</template>`
  } else if (c === 'Transition') {
    return `<template>\n  <Transition name="${transitionEffect.value}">\n    <div v-if="visible" class="box">Animated Content</div>\n  </Transition>\n</template>`
  }
  return `<template>\n  <${c} />\n</template>\n\n<script setup lang="ts">\nimport { ${c} } from 'resuxjs/ui'\n<\/script>`
})

// Generate Rendered HTML
const generatedDomHtml = computed(() => {
  const c = currentComp.value
  if (c === 'RxButton') {
    return `<button type="button" class="rx-btn rx-btn-${btnVariant.value} rx-btn-${btnSize.value}${btnDisabled.value ? '" disabled' : '"'}>\n  ${btnWithIcon.value ? '<span class="rx-icon">⚡</span> ' : ''}${btnLoading.value ? '<span class="rx-btn-spinner"></span> ' : ''}Deploy Application\n</button>`
  } else if (c === 'RxInput') {
    return `<input type="${inputType.value}" value="${inputVal.value}" class="rx-input"${inputDisabled.value ? ' disabled' : ''} />`
  } else if (c === 'RxSelect') {
    return `<div class="rx-select" data-disabled="${selectDisabled.value}">\n  <select class="rx-select-native">\n    <option value="${selectVal.value}">${selectVal.value}</option>\n  </select>\n  <span class="rx-select-arrow" aria-hidden="true">▾</span>\n</div>`
  } else if (c === 'RxVerificationCode') {
    return `<div class="rx-verification-code is-focused" data-status="${otpStatus.value}">\n  <div class="rx-verification-code-cells">\n    ${otpCells.value.map(cell => `<span class="rx-verification-code-cell">${otpMask.value && cell ? '•' : cell}</span>`).join('\n    ')}\n  </div>\n</div>`
  } else if (c === 'RxSwitch') {
    return `<button type="button" role="switch" aria-checked="${switchVal.value}" data-state="${switchVal.value ? 'checked' : 'unchecked'}" class="rx-switch${switchVal.value ? ' checked' : ''}">\n  <span class="rx-switch-thumb" aria-hidden="true"></span>\n</button>`
  } else if (c === 'RxCard') {
    return `<div class="rx-card rx-card-${cardVariant.value}">\n  <div class="rx-card-header">Production Health</div>\n  <div class="rx-card-body">All 21 exports validated.</div>\n</div>`
  } else if (c === 'RxBadge') {
    return `<span class="rx-badge rx-badge-${badgeVariant.value}">\n  ${badgeWithDot.value ? '<span class="rx-badge-dot"></span> ' : ''}Status: Active\n</span>`
  }
  return `<div class="rx-${c.toLowerCase().replace('rx', '')}">\n  <!-- Rendered ${c} DOM elements -->\n</div>`
})

function copyCode(text: string) {
  if (typeof navigator !== 'undefined' && navigator.clipboard?.writeText) {
    navigator.clipboard.writeText(text)
    codeCopied.value = true
    setTimeout(() => { codeCopied.value = false }, 2000)
  }
}
</script>

<template>
  <div class="rx-preview-container">
    <!-- Header Toolbar -->
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
          <svg class="rx-tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z" />
            <circle cx="12" cy="12" r="3" />
          </svg>
          <span>Preview</span>
        </button>
        <button
          type="button"
          class="rx-mode-tab"
          :class="{ active: viewMode === 'code' }"
          @click="viewMode = 'code'"
        >
          <svg class="rx-tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="16 18 22 12 16 6" />
            <polyline points="8 6 2 12 8 18" />
          </svg>
          <span>Vue Code</span>
        </button>
        <button
          type="button"
          class="rx-mode-tab"
          :class="{ active: viewMode === 'dom' }"
          @click="viewMode = 'dom'"
        >
          <svg class="rx-tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="4 17 10 11 4 5" />
            <line x1="12" y1="19" x2="20" y2="19" />
          </svg>
          <span>Inspect DOM</span>
        </button>
      </div>
    </div>

    <!-- Suite Component Switcher Tray (Active when in suite mode) -->
    <div v-if="isSuite" class="rx-suite-tray" aria-label="Component Suite Selector">
      <div class="rx-suite-tray-label">Component:</div>
      <div class="rx-suite-tray-scroll">
        <button
          v-for="item in suiteComponents"
          :key="item.id"
          type="button"
          class="rx-suite-pill"
          :class="{ active: activeComponent === item.id }"
          @click="activeComponent = item.id"
        >
          <svg
            class="rx-suite-svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            v-html="componentIcons[item.id] || componentIcons.RxButton"
          ></svg>
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
              :class="`rx-btn rx-btn-${btnVariant} rx-btn-${btnSize}${btnLoading ? ' is-loading' : ''}`"
              @click="handleBtnClick"
            >
              <span v-if="btnWithIcon" class="rx-icon-inline" aria-hidden="true">⚡</span>
              <span v-if="btnLoading" class="rx-btn-spinner" aria-hidden="true"></span>
              <span>Deploy Application</span>
            </button>
          </div>
          <div class="rx-stage-feedback">
            <span class="rx-feedback-indicator" :class="{ pulse: btnClickCount > 0 }"></span>
            <span class="rx-feedback-text">{{ feedbackMessage || 'Click the button above to test real event dispatching' }}</span>
            <span v-if="btnClickCount > 0" class="rx-feedback-counter">Clicks: {{ btnClickCount }}</span>
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
              Two-way bound <code>v-model</code>: <code>{{ inputVal || '(empty)' }}</code> · Length: {{ inputVal.length }} chars
            </div>
          </div>
        </div>

        <!-- ==================== RxSelect ==================== -->
        <div v-else-if="currentComp === 'RxSelect'" class="rx-stage-inner">
          <div class="rx-form-group">
            <label class="rx-form-label">Deployment Region (RxSelect)</label>
            <div class="rx-select" :data-disabled="selectDisabled">
              <select v-model="selectVal" class="rx-select-native" :disabled="selectDisabled">
                <option v-for="opt in selectOptions" :key="opt.value" :value="opt.value">
                  {{ opt.label }}
                </option>
              </select>
              <span class="rx-select-arrow" aria-hidden="true">▾</span>
            </div>
            <div class="rx-form-hint">
              Active Selection: <code>{{ selectVal }}</code>
            </div>
          </div>
        </div>

        <!-- ==================== RxTextarea ==================== -->
        <div v-else-if="currentComp === 'RxTextarea'" class="rx-stage-inner">
          <div class="rx-form-group" style="max-width: 520px;">
            <label class="rx-form-label">
              <span>Release Notes</span>
              <span class="rx-form-counter">{{ textareaVal.length }} chars · {{ textareaVal.trim().split(/\s+/).filter(Boolean).length }} words</span>
            </label>
            <textarea
              v-model="textareaVal"
              :rows="textareaRows"
              :disabled="textareaDisabled"
              placeholder="Enter release notes..."
              class="rx-input rx-textarea"
            ></textarea>
            <div class="rx-form-hint">
              Auto-expandable responsive surface with <code>v-model</code> reactivity.
            </div>
          </div>
        </div>

        <!-- ==================== RxDatePicker ==================== -->
        <div v-else-if="currentComp === 'RxDatePicker'" class="rx-stage-inner rx-center-stage">
          <div class="rx-form-group" style="max-width: 320px;">
            <label class="rx-form-label">Launch Target Date</label>
            <input
              v-model="dateVal"
              type="date"
              :disabled="dateDisabled"
              class="rx-input rx-datepicker"
            />
            <div class="rx-form-hint">
              Selected ISO: <code>{{ dateVal }}</code>
            </div>
          </div>
        </div>

        <!-- ==================== RxVerificationCode (OTP) ==================== -->
        <div v-else-if="currentComp === 'RxVerificationCode'" class="rx-stage-inner rx-center-stage">
          <div
            class="rx-verification-code"
            :class="{ 'is-focused': otpFocused, 'is-error': otpStatus === 'error' }"
            :data-status="otpStatus"
            @click="focusOtpInput"
          >
            <!-- Real interactive native input capturing typing, backspace & paste -->
            <input
              ref="otpInputRef"
              :value="otpVal"
              type="text"
              inputmode="numeric"
              pattern="[0-9]*"
              :maxlength="otpDigits"
              autocomplete="one-time-code"
              class="rx-otp-hidden-native-input"
              aria-label="Verification code input"
              @input="handleOtpInput"
              @focus="otpFocused = true"
              @blur="otpFocused = false"
            />

            <!-- Visual cells displaying the characters with active caret -->
            <div v-if="otpStatus === 'idle' || otpStatus === 'error'" class="rx-verification-code-cells" aria-hidden="true">
              <span
                v-for="(c, idx) in otpCells"
                :key="idx"
                class="rx-verification-code-cell"
                :class="{
                  'is-filled': !!c,
                  'is-active': otpFocused && idx === Math.min(otpVal.length, otpDigits - 1)
                }"
              >
                {{ c ? (otpMask ? '•' : c) : '' }}
                <span v-if="otpFocused && idx === otpVal.length && !c" class="rx-otp-caret" aria-hidden="true"></span>
              </span>
            </div>

            <!-- Status view when verifying or verified -->
            <div v-else class="rx-verification-code-status" :class="`is-${otpStatus}`" role="status">
              <span class="rx-verification-code-orb" :class="`is-${otpStatus}`">
                <span v-if="otpStatus === 'success'" class="rx-verification-code-check">✓</span>
                <span v-else class="rx-verification-code-spinner"></span>
              </span>
              <span class="rx-verification-code-message">
                {{ otpStatus === 'verifying' ? 'Verifying code with server HMAC...' : '✓ Code verified securely' }}
              </span>
            </div>

            <span v-if="otpStatus === 'error'" class="rx-verification-code-error" role="alert">
              Invalid verification code. Try "2026".
            </span>
          </div>

          <!-- Typing helper instructions -->
          <div class="rx-stage-feedback" style="margin-top: 14px;">
            <span class="rx-feedback-indicator" :class="{ pulse: otpFocused }"></span>
            <span class="rx-feedback-text">
              {{ otpFocused ? `Active typing: "${otpVal || '(empty)'}" (${otpVal.length}/${otpDigits}) — Type numbers on keyboard` : 'Click the code boxes above to focus and type directly with your keyboard' }}
            </span>
          </div>

          <div class="rx-otp-quick-actions">
            <button type="button" class="rx-pill-action" @click="simulateOtpFill('2026')">
              Paste "2026"
            </button>
            <button type="button" class="rx-pill-action" @click="simulateOtpFill('9999')">
              Paste "9999" (Error)
            </button>
            <button type="button" class="rx-pill-action primary" @click="simulateOtpVerify">
              Submit Verification
            </button>
            <button type="button" class="rx-pill-action" @click="simulateOtpFill('')">
              Clear &amp; Type
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

        <!-- ==================== RxAvatar ==================== -->
        <div v-else-if="currentComp === 'RxAvatar'" class="rx-stage-inner rx-center-stage">
          <div style="display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap; justify-content: center;">
            <div :class="`rx-avatar rx-avatar-${avatarSize}`">
              <span class="rx-avatar-fallback">MA</span>
              <span v-if="avatarStatus !== 'none'" :class="`rx-avatar-status rx-status-${avatarStatus}`"></span>
            </div>
            <div class="rx-avatar rx-avatar-lg">
              <span class="rx-avatar-fallback">RX</span>
              <span class="rx-avatar-status rx-status-online"></span>
            </div>
            <div class="rx-avatar rx-avatar-md">
              <span class="rx-avatar-fallback">JD</span>
              <span class="rx-avatar-status rx-status-busy"></span>
            </div>
            <div class="rx-avatar rx-avatar-sm">
              <span class="rx-avatar-fallback">TS</span>
              <span class="rx-avatar-status rx-status-away"></span>
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
              @click="alertDismissed = true; setFeedback('Alert dismissed')"
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
              @click="alertDismissed = false; setFeedback('Alert restored')"
            >
              ↺ Restore Dismissed Alert
            </button>
          </div>
        </div>

        <!-- ==================== RxSkeleton ==================== -->
        <div v-else-if="currentComp === 'RxSkeleton'" class="rx-stage-inner rx-center-stage">
          <div v-if="skeletonType === 'card'" class="rx-card" style="max-width: 380px; width: 100%;">
            <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1rem;">
              <div class="rx-skeleton" style="width: 3rem; height: 3rem; border-radius: 9999px;"></div>
              <div style="flex: 1; display: flex; flex-direction: column; gap: 0.5rem;">
                <div class="rx-skeleton" style="width: 70%; height: 1rem; border-radius: 4px;"></div>
                <div class="rx-skeleton" style="width: 40%; height: 0.75rem; border-radius: 4px;"></div>
              </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.5rem;">
              <div class="rx-skeleton" style="width: 100%; height: 0.85rem; border-radius: 4px;"></div>
              <div class="rx-skeleton" style="width: 85%; height: 0.85rem; border-radius: 4px;"></div>
            </div>
          </div>
          <div v-else-if="skeletonType === 'text'" style="max-width: 380px; width: 100%; display: flex; flex-direction: column; gap: 0.6rem;">
            <div class="rx-skeleton" style="width: 100%; height: 1.1rem; border-radius: 4px;"></div>
            <div class="rx-skeleton" style="width: 90%; height: 1.1rem; border-radius: 4px;"></div>
            <div class="rx-skeleton" style="width: 65%; height: 1.1rem; border-radius: 4px;"></div>
          </div>
          <div v-else-if="skeletonType === 'circle'" style="display: flex; gap: 1rem; justify-content: center;">
            <div class="rx-skeleton" style="width: 3.5rem; height: 3.5rem; border-radius: 9999px;"></div>
            <div class="rx-skeleton" style="width: 3.5rem; height: 3.5rem; border-radius: 9999px;"></div>
            <div class="rx-skeleton" style="width: 3.5rem; height: 3.5rem; border-radius: 9999px;"></div>
          </div>
        </div>

        <!-- ==================== RxDivider ==================== -->
        <div v-else-if="currentComp === 'RxDivider'" class="rx-stage-inner" style="max-width: 480px; margin: 0 auto;">
          <div v-if="dividerOrientation === 'horizontal'" style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.875rem;">
            <div class="rx-card" style="padding: 10px 16px;">Server-Side Rendered Shell</div>
            <div class="rx-divider rx-divider-horizontal">
              <span v-if="dividerLabel" class="rx-divider-label">{{ dividerLabel }}</span>
            </div>
            <div class="rx-card" style="padding: 10px 16px;">Client Resumed Reactive Scope</div>
          </div>
          <div v-else style="display: flex; align-items: center; justify-content: center; height: 100px; gap: 1.5rem;">
            <span style="font-size: 0.85rem; color: var(--vp-c-text-2);">Left Pane</span>
            <div class="rx-divider rx-divider-vertical" style="height: 100%;">
              <span v-if="dividerLabel" class="rx-divider-label">{{ dividerLabel }}</span>
            </div>
            <span style="font-size: 0.85rem; color: var(--vp-c-text-2);">Right Pane</span>
          </div>
        </div>

        <!-- ==================== RxKbd ==================== -->
        <div v-else-if="currentComp === 'RxKbd'" class="rx-stage-inner rx-center-stage">
          <div style="display: flex; flex-direction: column; gap: 1rem; align-items: center;">
            <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; justify-content: center;">
              <span>Command Palette: <kbd class="rx-kbd">{{ kbdOs === 'mac' ? '⌘' : 'Ctrl' }}</kbd> + <kbd class="rx-kbd">K</kbd></span>
              <span>Deploy Project: <kbd class="rx-kbd">{{ kbdOs === 'mac' ? '⌥' : 'Alt' }}</kbd> + <kbd class="rx-kbd">D</kbd></span>
              <span>Dismiss: <kbd class="rx-kbd">Esc</kbd></span>
            </div>
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
            <span class="rx-icon-inline" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" />
                <path d="M3 9h18" />
              </svg>
            </span>
            <span>Open Modal Dialog</span>
          </button>

          <!-- Accessible Dialog Overlay -->
          <div v-if="modalOpen" class="rx-modal-backdrop" @click.self="modalOpen = false">
            <div class="rx-modal-content" role="dialog" aria-modal="true">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
                <h3 style="margin: 0; font-size: 1.05rem;">{{ modalTitle }}</h3>
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
                  @click="modalOpen = false; setFeedback('Deployment confirmed!')"
                >
                  Confirm Deploy
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- ==================== RxTooltip ==================== -->
        <div v-else-if="currentComp === 'RxTooltip'" class="rx-stage-inner rx-center-stage">
          <div
            class="rx-tooltip-wrapper"
            @mouseenter="tooltipHover = true"
            @mouseleave="tooltipHover = false"
          >
            <button type="button" class="rx-btn rx-btn-outline rx-btn-md">
              Hover for Tooltip (Placement: {{ tooltipPlacement }})
            </button>
            <div v-if="tooltipHover" :class="`rx-tooltip rx-tooltip-${tooltipPlacement}`" role="tooltip">
              Zero-CLS Fontaine metric overrides active
            </div>
          </div>
        </div>

        <!-- ==================== RxPopover ==================== -->
        <div v-else-if="currentComp === 'RxPopover'" class="rx-stage-inner rx-center-stage">
          <div class="rx-popover">
            <button
              type="button"
              class="rx-btn rx-btn-secondary rx-btn-md"
              @click="popoverOpen = !popoverOpen"
            >
              {{ popoverOpen ? 'Close Filter Popover' : 'Open Filter Popover ▾' }}
            </button>
            <div v-if="popoverOpen" class="rx-popover-content" style="min-width: 16rem;">
              <strong style="display: block; margin-bottom: 0.5rem;">Deployment Filters</strong>
              <div style="display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.825rem;">
                <label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
                  <input type="checkbox" checked /> SSR Streaming Enabled
                </label>
                <label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
                  <input type="checkbox" checked /> View Transitions
                </label>
                <label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
                  <input type="checkbox" /> Offline Font Fallbacks
                </label>
              </div>
            </div>
          </div>
        </div>

        <!-- ==================== RxDropdown ==================== -->
        <div v-else-if="currentComp === 'RxDropdown'" class="rx-stage-inner rx-center-stage">
          <div class="rx-dropdown">
            <button
              type="button"
              class="rx-btn rx-btn-secondary rx-btn-md"
              @click="dropdownOpen = !dropdownOpen"
            >
              {{ dropdownOpen ? 'Close Actions Menu' : 'Actions Menu ▾' }}
            </button>
            <ul v-if="dropdownOpen" class="rx-dropdown-menu" role="menu">
              <li class="rx-dropdown-item" @click="dropdownOpen = false; setFeedback('Selected: Verify Framework Parity')">
                Verify Framework Parity
              </li>
              <li class="rx-dropdown-item" @click="dropdownOpen = false; setFeedback('Selected: Build Production Output')">
                Build Production Output
              </li>
              <li class="rx-dropdown-item" @click="dropdownOpen = false; setFeedback('Selected: Inspect Halal Report')">
                Inspect Halal Report
              </li>
            </ul>
          </div>
        </div>

        <!-- ==================== RxMotion & RxReveal & RxAutoAnimate ==================== -->
        <div v-else-if="currentComp === 'RxMotion' || currentComp === 'RxReveal' || currentComp === 'RxAutoAnimate'" class="rx-stage-inner rx-center-stage">
          <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
            <button type="button" class="rx-btn rx-btn-secondary rx-btn-sm" @click="motionKey++">
              ↺ Replay Animation
            </button>
            <button v-if="currentComp === 'RxAutoAnimate'" type="button" class="rx-btn rx-btn-primary rx-btn-sm" @click="addAutoItem">
              + Add Item
            </button>
          </div>
          <div :key="motionKey" class="rx-card" style="max-width: 420px; width: 100%; transition: all 0.3s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <strong>{{ currentComp }} (Run #{{ motionKey }})</strong>
              <span class="rx-badge rx-badge-primary">{{ motionPreset }}</span>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
              <span
                v-for="(item, idx) in autoItems"
                :key="item"
                class="rx-badge rx-badge-secondary"
                style="cursor: pointer;"
                title="Click to remove"
                @click="removeAutoItem(idx)"
              >
                {{ item }} ✕
              </span>
            </div>
          </div>
        </div>

        <!-- ==================== RxIcon ==================== -->
        <div v-else-if="currentComp === 'RxIcon'" class="rx-stage-inner rx-center-stage">
          <div style="display: flex; gap: 2rem; align-items: center; justify-content: center; flex-wrap: wrap;">
            <div style="text-align: center;">
              <svg :style="`width: ${iconSize}; height: ${iconSize}; color: var(--vp-c-brand-1);`" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              <div style="font-size: 11px; margin-top: 4px; color: var(--vp-c-text-3);">[check]</div>
            </div>
            <div style="text-align: center;">
              <svg :style="`width: ${iconSize}; height: ${iconSize}; color: #10b981;`" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
                <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
              </svg>
              <div style="font-size: 11px; margin-top: 4px; color: var(--vp-c-text-3);">[rocket]</div>
            </div>
            <div style="text-align: center;">
              <svg :style="`width: ${iconSize}; height: ${iconSize}; color: #f59e0b;`" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
              </svg>
              <div style="font-size: 11px; margin-top: 4px; color: var(--vp-c-text-3);">[zap]</div>
            </div>
            <div style="text-align: center;">
              <svg :style="`width: ${iconSize}; height: ${iconSize}; color: #6366f1;`" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              </svg>
              <div style="font-size: 11px; margin-top: 4px; color: var(--vp-c-text-3);">[shield]</div>
            </div>
          </div>
        </div>

        <!-- ==================== Teleport ==================== -->
        <div v-else-if="currentComp === 'Teleport'" class="rx-stage-inner rx-center-stage">
          <div style="max-width: 440px; width: 100%; display: flex; flex-direction: column; gap: 1rem;">
            <div class="rx-card" style="border: 2px dashed var(--resux-border); text-align: center; padding: 16px;">
              <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--vp-c-text-3); font-weight: 750;">
                Target Container (#teleport-target)
              </span>
              <div v-if="teleportActive" style="margin-top: 8px;">
                <span class="rx-badge rx-badge-success">Content Teleported Successfully</span>
              </div>
            </div>
            <div style="text-align: center;">
              <button type="button" class="rx-btn rx-btn-secondary rx-btn-sm" @click="teleportActive = !teleportActive">
                {{ teleportActive ? 'Disable Teleport' : 'Enable Teleport' }}
              </button>
            </div>
          </div>
        </div>

        <!-- ==================== Transition ==================== -->
        <div v-else-if="currentComp === 'Transition'" class="rx-stage-inner rx-center-stage">
          <div style="display: flex; flex-direction: column; align-items: center; gap: 1rem;">
            <button type="button" class="rx-btn rx-btn-primary rx-btn-sm" @click="transitionShow = !transitionShow">
              {{ transitionShow ? 'Hide Animated Card' : 'Show Animated Card' }}
            </button>
            <div
              v-if="transitionShow"
              class="rx-card"
              style="padding: 16px 24px; transition: all 0.3s ease; text-align: center;"
            >
              <strong>Vue &lt;Transition&gt; Surface</strong>
              <p style="margin: 4px 0 0; font-size: 0.85rem; color: var(--vp-c-text-2);">
                Smooth entry and exit animations without client overhead.
              </p>
            </div>
          </div>
        </div>

        <!-- ==================== Fallback ==================== -->
        <div v-else class="rx-stage-inner rx-center-stage">
          <span class="rx-badge rx-badge-primary">{{ currentComp }} Ready</span>
        </div>
      </div>

      <!-- ==================== Interactive Controls Panel ==================== -->
      <div class="rx-controls-panel">
        <div class="rx-controls-header">
          <div class="rx-controls-heading">
            <svg class="rx-controls-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="3" />
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" />
            </svg>
            <span>Controls &amp; Interactive State: {{ currentComp }}</span>
          </div>
          <button type="button" class="rx-reset-btn" @click="resetCurrentComp">
            ↺ Reset Props
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

        <!-- Controls for RxSelect -->
        <div v-else-if="currentComp === 'RxSelect'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">PRESET OPTIONS</label>
            <div class="rx-segmented-control">
              <button
                v-for="opt in selectOptions"
                :key="opt.value"
                type="button"
                class="rx-seg-btn"
                :class="{ active: selectVal === opt.value }"
                @click="selectVal = opt.value"
              >
                {{ opt.value }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">STATE</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: selectDisabled }"
              @click="selectDisabled = !selectDisabled"
            >
              {{ selectDisabled ? '✓ Disabled' : 'Disabled' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxTextarea -->
        <div v-else-if="currentComp === 'RxTextarea'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ROWS HEIGHT</label>
            <div class="rx-segmented-control">
              <button
                v-for="r in [2, 3, 5]"
                :key="r"
                type="button"
                class="rx-seg-btn"
                :class="{ active: textareaRows === r }"
                @click="textareaRows = r"
              >
                {{ r }} rows
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">STATE</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: textareaDisabled }"
              @click="textareaDisabled = !textareaDisabled"
            >
              {{ textareaDisabled ? '✓ Disabled' : 'Disabled' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxDatePicker -->
        <div v-else-if="currentComp === 'RxDatePicker'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">PRESET DATES</label>
            <div class="rx-segmented-control">
              <button type="button" class="rx-seg-btn" @click="dateVal = '2026-11-20'">Nov 20, 2026</button>
              <button type="button" class="rx-seg-btn" @click="dateVal = '2026-12-01'">Dec 1, 2026</button>
              <button type="button" class="rx-seg-btn" @click="dateVal = '2027-01-01'">Jan 1, 2027</button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">STATE</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: dateDisabled }"
              @click="dateDisabled = !dateDisabled"
            >
              {{ dateDisabled ? '✓ Disabled' : 'Disabled' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxVerificationCode -->
        <div v-else-if="currentComp === 'RxVerificationCode'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">STATUS</label>
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
            <label class="rx-control-label">CELL COUNT</label>
            <div class="rx-segmented-control">
              <button
                v-for="d in [4, 6]"
                :key="d"
                type="button"
                class="rx-seg-btn"
                :class="{ active: otpDigits === d }"
                @click="otpDigits = d"
              >
                {{ d }} cells
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">MASKING</label>
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
            <label class="rx-control-label">CARD VARIANT</label>
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
            <label class="rx-control-label">STATUS DOT</label>
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

        <!-- Controls for RxAvatar -->
        <div v-else-if="currentComp === 'RxAvatar'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">SIZE</label>
            <div class="rx-segmented-control">
              <button
                v-for="s in (['sm', 'md', 'lg'] as const)"
                :key="s"
                type="button"
                class="rx-seg-btn"
                :class="{ active: avatarSize === s }"
                @click="avatarSize = s"
              >
                {{ s.toUpperCase() }}
              </button>
            </div>
          </div>

          <div class="rx-control-group">
            <label class="rx-control-label">STATUS INDICATOR</label>
            <div class="rx-segmented-control">
              <button
                v-for="st in (['online', 'busy', 'away', 'none'] as const)"
                :key="st"
                type="button"
                class="rx-seg-btn"
                :class="{ active: avatarStatus === st }"
                @click="avatarStatus = st"
              >
                {{ st }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxAlert -->
        <div v-else-if="currentComp === 'RxAlert'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">SEVERITY VARIANT</label>
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

        <!-- Controls for RxSkeleton -->
        <div v-else-if="currentComp === 'RxSkeleton'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">PLACEHOLDER SHAPE</label>
            <div class="rx-segmented-control">
              <button
                v-for="sk in (['card', 'text', 'circle'] as const)"
                :key="sk"
                type="button"
                class="rx-seg-btn"
                :class="{ active: skeletonType === sk }"
                @click="skeletonType = sk"
              >
                {{ sk }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxDivider -->
        <div v-else-if="currentComp === 'RxDivider'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ORIENTATION</label>
            <div class="rx-segmented-control">
              <button
                v-for="o in (['horizontal', 'vertical'] as const)"
                :key="o"
                type="button"
                class="rx-seg-btn"
                :class="{ active: dividerOrientation === o }"
                @click="dividerOrientation = o"
              >
                {{ o }}
              </button>
            </div>
          </div>
          <div class="rx-control-group">
            <label class="rx-control-label">LABEL TEXT</label>
            <div class="rx-segmented-control">
              <button type="button" class="rx-seg-btn" :class="{ active: dividerLabel === 'RESUMABILITY BOUNDARY' }" @click="dividerLabel = 'RESUMABILITY BOUNDARY'">Resumability</button>
              <button type="button" class="rx-seg-btn" :class="{ active: dividerLabel === 'SECTION DIVIDER' }" @click="dividerLabel = 'SECTION DIVIDER'">Section</button>
              <button type="button" class="rx-seg-btn" :class="{ active: dividerLabel === '' }" @click="dividerLabel = ''">None (Line only)</button>
            </div>
          </div>
        </div>

        <!-- Controls for RxKbd -->
        <div v-else-if="currentComp === 'RxKbd'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">KEYBOARD OS</label>
            <div class="rx-segmented-control">
              <button
                type="button"
                class="rx-seg-btn"
                :class="{ active: kbdOs === 'mac' }"
                @click="kbdOs = 'mac'"
              >
                macOS (⌘)
              </button>
              <button
                type="button"
                class="rx-seg-btn"
                :class="{ active: kbdOs === 'win' }"
                @click="kbdOs = 'win'"
              >
                Windows / Linux (Ctrl)
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxTabs -->
        <div v-else-if="currentComp === 'RxTabs'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ACTIVE TAB</label>
            <div class="rx-segmented-control">
              <button
                v-for="t in (['ssr', 'vt', 'icons'] as const)"
                :key="t"
                type="button"
                class="rx-seg-btn"
                :class="{ active: activeSubTab === t }"
                @click="activeSubTab = t"
              >
                {{ t.toUpperCase() }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxAccordion -->
        <div v-else-if="currentComp === 'RxAccordion'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">DISCLOSURE STATE</label>
            <div class="rx-segmented-control">
              <button
                type="button"
                class="rx-seg-btn"
                :class="{ active: accordionOpen }"
                @click="accordionOpen = true"
              >
                Open (Expanded)
              </button>
              <button
                type="button"
                class="rx-seg-btn"
                :class="{ active: !accordionOpen }"
                @click="accordionOpen = false"
              >
                Closed (Collapsed)
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxModal -->
        <div v-else-if="currentComp === 'RxModal'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">DIALOG TRIGGER</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: modalOpen }"
              @click="modalOpen = !modalOpen"
            >
              {{ modalOpen ? '✕ Close Dialog' : '🪟 Open Modal' }}
            </button>
          </div>
          <div class="rx-control-group">
            <label class="rx-control-label">HEADER TITLE PRESET</label>
            <div class="rx-segmented-control">
              <button type="button" class="rx-seg-btn" :class="{ active: modalTitle === 'Confirm Production Deploy' }" @click="modalTitle = 'Confirm Production Deploy'">Deploy</button>
              <button type="button" class="rx-seg-btn" :class="{ active: modalTitle === 'Delete Database Resource' }" @click="modalTitle = 'Delete Database Resource'">Delete</button>
              <button type="button" class="rx-seg-btn" :class="{ active: modalTitle === 'Upgrade Resux License' }" @click="modalTitle = 'Upgrade Resux License'">License</button>
            </div>
          </div>
        </div>

        <!-- Controls for RxPopover -->
        <div v-else-if="currentComp === 'RxPopover'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">POPOVER STATE</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: popoverOpen }"
              @click="popoverOpen = !popoverOpen"
            >
              {{ popoverOpen ? '✓ Open' : 'Closed' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxDropdown -->
        <div v-else-if="currentComp === 'RxDropdown'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">DROPDOWN MENU STATE</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: dropdownOpen }"
              @click="dropdownOpen = !dropdownOpen"
            >
              {{ dropdownOpen ? '✓ Open' : 'Closed' }}
            </button>
          </div>
        </div>

        <!-- Controls for RxTooltip -->
        <div v-else-if="currentComp === 'RxTooltip'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">PLACEMENT</label>
            <div class="rx-segmented-control">
              <button
                v-for="p in (['top', 'bottom', 'left', 'right'] as const)"
                :key="p"
                type="button"
                class="rx-seg-btn"
                :class="{ active: tooltipPlacement === p }"
                @click="tooltipPlacement = p"
              >
                {{ p }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxMotion / RxReveal -->
        <div v-else-if="currentComp === 'RxMotion' || currentComp === 'RxReveal'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ANIMATION PRESET</label>
            <div class="rx-segmented-control">
              <button
                v-for="pr in (['fade-up', 'scale-in', 'slide-in-left', 'pulse-glow'] as const)"
                :key="pr"
                type="button"
                class="rx-seg-btn"
                :class="{ active: motionPreset === pr }"
                @click="motionPreset = pr; motionKey++"
              >
                {{ pr }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for RxAutoAnimate -->
        <div v-else-if="currentComp === 'RxAutoAnimate'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">LIST ACTIONS</label>
            <div style="display: flex; gap: 8px;">
              <button type="button" class="rx-btn rx-btn-primary rx-btn-sm" @click="addAutoItem">+ Add Item</button>
              <button type="button" class="rx-btn rx-btn-secondary rx-btn-sm" @click="resetAutoItems">Reset List</button>
            </div>
          </div>
        </div>

        <!-- Controls for RxIcon -->
        <div v-else-if="currentComp === 'RxIcon'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ICON SIZE</label>
            <div class="rx-segmented-control">
              <button
                v-for="sz in (['20px', '28px', '36px', '48px'] as const)"
                :key="sz"
                type="button"
                class="rx-seg-btn"
                :class="{ active: iconSize === sz }"
                @click="iconSize = sz"
              >
                {{ sz }}
              </button>
            </div>
          </div>
        </div>

        <!-- Controls for Teleport -->
        <div v-else-if="currentComp === 'Teleport'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">TELEPORT STATE</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: teleportActive }"
              @click="teleportActive = !teleportActive"
            >
              {{ teleportActive ? '✓ Teleport Active' : 'Disabled (Inline)' }}
            </button>
          </div>
        </div>

        <!-- Controls for Transition -->
        <div v-else-if="currentComp === 'Transition'" class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">VISIBILITY</label>
            <button
              type="button"
              class="rx-chip-toggle"
              :class="{ active: transitionShow }"
              @click="transitionShow = !transitionShow"
            >
              {{ transitionShow ? '✓ Visible' : 'Hidden' }}
            </button>
          </div>
        </div>

        <!-- Generic / Fallback Controls -->
        <div v-else class="rx-controls-grid">
          <div class="rx-control-group">
            <label class="rx-control-label">ACTIVE COMPONENT</label>
            <span style="font-size: 0.85rem; color: var(--vp-c-brand-1); font-weight: 700;">
              {{ currentComp }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. Vue SFC Code View -->
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

    <!-- 3. Rendered DOM View -->
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
  display: inline-flex;
  align-items: center;
  gap: 6px;
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

.rx-tab-svg {
  width: 13px;
  height: 13px;
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

.rx-suite-svg {
  width: 13px;
  height: 13px;
  flex-shrink: 0;
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
  min-height: 180px;
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
  display: inline-flex;
  align-items: center;
  margin-right: 6px;
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

.rx-form-counter {
  font-size: 11px;
  color: var(--vp-c-text-3);
}

/* Real OTP Native Input Overlay */
.rx-otp-hidden-native-input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.001;
  border: none;
  background: transparent;
  color: transparent;
  cursor: text;
  z-index: 10;
  font-size: 16px;
  box-sizing: border-box;
}

.rx-verification-code {
  position: relative;
  cursor: text;
}

.rx-verification-code-cells {
  pointer-events: none;
  position: relative;
}

.rx-otp-caret {
  display: inline-block;
  width: 2px;
  height: 1.25rem;
  background: var(--vp-c-brand-1);
  animation: rx-caret-blink 1s ease infinite;
  margin-left: 1px;
}

@keyframes rx-caret-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
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

.rx-controls-svg {
  width: 14px;
  height: 14px;
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

/* Responsive Adaptations */
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
    justify-content: center;
  }

  .rx-controls-grid {
    grid-template-columns: 1fr;
  }

  .rx-preview-stage {
    padding: 24px 12px;
  }
}
</style>
