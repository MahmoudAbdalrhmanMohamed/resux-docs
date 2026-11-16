<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps<{
  component: string
  title?: string
}>()

const activeTab = ref<'preview' | 'html'>('preview')
const variant = ref('primary')
const size = ref('md')
const disabled = ref(false)
const inputVal = ref('mahmoud@resux.dev')
const textareaVal = ref('Resux 0.4.0-beta.7 brings native View Transitions, Fontless 1.3.4 metrics, and compile-time SVG icons.')
const selectVal = ref('eu-central-1')
const dateVal = ref('2026-11-20')
const switchVal = ref(true)
const otpVal = ref('2026')
const otpStatus = ref<'idle' | 'verifying' | 'success' | 'error'>('idle')
const otpMask = ref(false)
const alertDismissed = ref(false)
const accordionOpen = ref(true)
const activeSubTab = ref('ssr')
const popoverOpen = ref(true)
const dropdownOpen = ref(true)
const tooltipVisible = ref(true)
const modalOpen = ref(true)
const motionKey = ref(1)
const autoItems = ref(['resuxjs/runtime', 'resuxjs/ui', 'resuxjs/icons', 'resuxjs/fonts'])
const teleportDisabled = ref(false)
const transitionVisible = ref(true)

const otpCells = computed(() => {
  const chars = otpVal.value.slice(0, 4).split('')
  return [0, 1, 2, 3].map((i) => chars[i] || '')
})
</script>

<template>
  <div class="rx-doc-preview" style="border: 1px solid var(--resux-border); border-radius: 0.75rem; overflow: hidden; margin: 1.25rem 0; background: var(--resux-surface);">
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.65rem 1rem; background: var(--resux-surface-muted); border-bottom: 1px solid var(--resux-border);">
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <span class="rx-badge rx-badge-primary">Live UI Preview</span>
        <strong style="font-size: 0.85rem;">{{ title || component }}</strong>
      </div>
      <div style="display: flex; gap: 0.35rem;">
        <button class="rx-tab-btn" :class="{ active: activeTab === 'preview' }" @click="activeTab = 'preview'">Interactive Canvas</button>
        <button class="rx-tab-btn" :class="{ active: activeTab === 'html' }" @click="activeTab = 'html'">Inspect DOM Classes</button>
      </div>
    </div>

    <div v-if="activeTab === 'preview'" style="padding: 1.5rem;">
      <!-- RxButton -->
      <div v-if="component === 'RxButton'" style="display: flex; flex-direction: column; gap: 1rem;">
        <div style="display: flex; flex-wrap: wrap; gap: 0.65rem; align-items: center;">
          <button type="button" :disabled="disabled" :class="`rx-btn rx-btn-${variant} rx-btn-${size}`">
            {{ variant.toUpperCase() }} ({{ size }})
          </button>
          <button type="button" class="rx-btn rx-btn-primary rx-btn-md">Primary</button>
          <button type="button" class="rx-btn rx-btn-secondary rx-btn-md">Secondary</button>
          <button type="button" class="rx-btn rx-btn-outline rx-btn-md">Outline</button>
          <button type="button" class="rx-btn rx-btn-ghost rx-btn-md">Ghost</button>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; font-size: 0.75rem; padding-top: 0.75rem; border-top: 1px dashed var(--resux-border);">
          <span>Variant:</span>
          <button v-for="v in ['primary','secondary','outline','ghost']" :key="v" class="rx-btn rx-btn-secondary rx-btn-sm" @click="variant = v">{{ v }}</button>
          <span style="margin-left: 0.5rem;">Size:</span>
          <button v-for="s in ['sm','md','lg']" :key="s" class="rx-btn rx-btn-secondary rx-btn-sm" @click="size = s">{{ s }}</button>
          <button class="rx-btn rx-btn-outline rx-btn-sm" @click="disabled = !disabled">disabled={{ disabled }}</button>
        </div>
      </div>

      <!-- RxInput -->
      <div v-else-if="component === 'RxInput'" style="max-width: 24rem; display: flex; flex-direction: column; gap: 0.65rem;">
        <input v-model="inputVal" type="text" placeholder="Enter developer email..." class="rx-input" :disabled="disabled" />
        <div style="font-size: 0.8rem; opacity: 0.8;">Bound <code>v-model</code> value: <code>{{ inputVal }}</code></div>
      </div>

      <!-- RxTextarea -->
      <div v-else-if="component === 'RxTextarea'" style="max-width: 28rem; display: flex; flex-direction: column; gap: 0.65rem;">
        <textarea v-model="textareaVal" rows="3" class="rx-input rx-textarea"></textarea>
        <div style="font-size: 0.8rem; opacity: 0.8;">Character count: <strong>{{ textareaVal.length }}</strong></div>
      </div>

      <!-- RxSelect -->
      <div v-else-if="component === 'RxSelect'" style="max-width: 22rem; display: flex; flex-direction: column; gap: 0.65rem;">
        <div class="rx-select" data-disabled="false">
          <select v-model="selectVal" class="rx-select-native">
            <option value="eu-central-1">Frankfurt (eu-central-1)</option>
            <option value="eu-west-2">London (eu-west-2)</option>
            <option value="us-east-1">US East (us-east-1)</option>
          </select>
          <span class="rx-select-arrow" aria-hidden="true">▾</span>
        </div>
        <div style="font-size: 0.8rem; opacity: 0.8;">Selected region: <code>{{ selectVal }}</code></div>
      </div>

      <!-- RxDatePicker -->
      <div v-else-if="component === 'RxDatePicker'" style="max-width: 18rem; display: flex; flex-direction: column; gap: 0.65rem;">
        <input v-model="dateVal" type="date" class="rx-input rx-datepicker" />
        <div style="font-size: 0.8rem; opacity: 0.8;">Selected ISO Date: <code>{{ dateVal }}</code></div>
      </div>

      <!-- RxSwitch -->
      <div v-else-if="component === 'RxSwitch'" style="display: flex; align-items: center; gap: 0.85rem;">
        <button type="button" role="switch" :aria-checked="switchVal" :data-state="switchVal ? 'checked' : 'unchecked'" class="rx-switch" :class="{ checked: switchVal }" @click="switchVal = !switchVal">
          <span class="rx-switch-thumb" aria-hidden="true"></span>
        </button>
        <span style="font-size: 0.875rem; font-weight: 600;">{{ switchVal ? 'Enabled (data-state="checked")' : 'Disabled (data-state="unchecked")' }}</span>
      </div>

      <!-- RxVerificationCode -->
      <div v-else-if="component === 'RxVerificationCode'" style="display: flex; flex-direction: column; gap: 1rem;">
        <div class="rx-verification-code is-focused" :data-status="otpStatus">
          <div v-if="otpStatus === 'idle' || otpStatus === 'error'" class="rx-verification-code-cells">
            <span v-for="(c, idx) in otpCells" :key="idx" class="rx-verification-code-cell" :class="{ 'is-filled': !!c, 'is-active': idx === otpVal.length }">
              {{ c ? (otpMask ? '•' : c) : '' }}
            </span>
          </div>
          <div v-else class="rx-verification-code-status" :class="`is-${otpStatus}`" role="status">
            <span>{{ otpStatus === 'verifying' ? '⏳ Verifying...' : '✓ Verified and secure' }}</span>
          </div>
          <span v-if="otpStatus === 'error'" class="rx-verification-code-error" role="alert">The verification code is invalid</span>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
          <input v-model="otpVal" maxlength="4" placeholder="Type 4 digits..." class="rx-input" style="max-width: 9rem;" />
          <button v-for="st in (['idle','verifying','success','error'] as const)" :key="st" class="rx-btn rx-btn-secondary rx-btn-sm" @click="otpStatus = st">status={{ st }}</button>
          <button class="rx-btn rx-btn-outline rx-btn-sm" @click="otpMask = !otpMask">mask={{ otpMask }}</button>
        </div>
      </div>

      <!-- RxCard -->
      <div v-else-if="component === 'RxCard'" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 1rem;">
        <div class="rx-card">
          <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <strong>Default RxCard</strong>
            <span class="rx-badge rx-badge-success">Active</span>
          </div>
          <p style="font-size: 0.825rem; margin: 0; opacity: 0.8;">Standard surface card with border token and subtle elevation.</p>
        </div>
        <div class="rx-card rx-card-elevated">
          <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <strong>Elevated RxCard</strong>
            <span class="rx-badge rx-badge-primary">v0.4</span>
          </div>
          <p style="font-size: 0.825rem; margin: 0; opacity: 0.8;">Enhanced shadow elevation for featured metrics and callouts.</p>
        </div>
      </div>

      <!-- RxBadge -->
      <div v-else-if="component === 'RxBadge'" style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
        <span class="rx-badge rx-badge-default">default</span>
        <span class="rx-badge rx-badge-primary">primary</span>
        <span class="rx-badge rx-badge-success">success</span>
        <span class="rx-badge rx-badge-warning">warning</span>
        <span class="rx-badge rx-badge-error">error</span>
      </div>

      <!-- RxAvatar -->
      <div v-else-if="component === 'RxAvatar'" style="display: flex; align-items: center; gap: 1.25rem;">
        <div class="rx-avatar rx-avatar-sm"><span class="rx-avatar-fallback">SM</span><span class="rx-avatar-status rx-status-online"></span></div>
        <div class="rx-avatar rx-avatar-md"><span class="rx-avatar-fallback">MA</span><span class="rx-avatar-status rx-status-busy"></span></div>
        <div class="rx-avatar rx-avatar-lg"><span class="rx-avatar-fallback">RX</span><span class="rx-avatar-status rx-status-away"></span></div>
      </div>

      <!-- RxAlert -->
      <div v-else-if="component === 'RxAlert'" style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div v-if="!alertDismissed" class="rx-alert rx-alert-info" role="alert">
          <div class="rx-alert-title">Info Alert (Dismissible)</div>
          <div class="rx-alert-content">Route CSS preloading is active before DOM swaps.</div>
          <button class="rx-alert-close" @click="alertDismissed = true">×</button>
        </div>
        <div class="rx-alert rx-alert-success" role="alert">
          <div class="rx-alert-title">Success Alert</div>
          <div class="rx-alert-content">All 31 package exports verified against docs/reference/packages.md.</div>
        </div>
        <button v-if="alertDismissed" class="rx-btn rx-btn-outline rx-btn-sm" style="align-self: flex-start;" @click="alertDismissed = false">Restore Dismissed Alert</button>
      </div>

      <!-- RxSkeleton -->
      <div v-else-if="component === 'RxSkeleton'" style="display: flex; align-items: center; gap: 0.85rem; max-width: 22rem;">
        <div class="rx-skeleton" style="width: 3rem; height: 3rem; border-radius: 9999px;"></div>
        <div style="flex: 1; display: flex; flex-direction: column; gap: 0.5rem;">
          <div class="rx-skeleton" style="width: 75%; height: 0.9rem; border-radius: 0.375rem;"></div>
          <div class="rx-skeleton" style="width: 50%; height: 0.75rem; border-radius: 0.375rem;"></div>
        </div>
      </div>

      <!-- RxDivider -->
      <div v-else-if="component === 'RxDivider'" style="max-width: 24rem;">
        <div style="font-size: 0.85rem;">Server-Side Rendered Shell</div>
        <div class="rx-divider rx-divider-horizontal"><span class="rx-divider-label">RESUMABLE BOUNDARY</span></div>
        <div style="font-size: 0.85rem;">Client Event Handler Payload</div>
      </div>

      <!-- RxKbd -->
      <div v-else-if="component === 'RxKbd'" style="display: flex; gap: 1rem; align-items: center;">
        <span>Command Palette: <kbd class="rx-kbd">Ctrl</kbd> + <kbd class="rx-kbd">K</kbd></span>
        <span>Save &amp; Build: <kbd class="rx-kbd">⌘</kbd> + <kbd class="rx-kbd">S</kbd></span>
      </div>

      <!-- RxAccordion -->
      <div v-else-if="component === 'RxAccordion'" style="max-width: 28rem;">
        <div class="rx-accordion">
          <button class="rx-accordion-header" @click="accordionOpen = !accordionOpen">
            <span>What is Resux Resumability?</span>
            <span>{{ accordionOpen ? '-' : '+' }}</span>
          </button>
          <div v-if="accordionOpen" class="rx-accordion-body">
            Resux serializes component state and event handlers on the server so the browser can resume interactivity without re-executing component setup trees on load.
          </div>
        </div>
      </div>

      <!-- RxTabs -->
      <div v-else-if="component === 'RxTabs'" style="max-width: 28rem;">
        <div class="rx-tabs">
          <div class="rx-tabs-header">
            <button class="rx-tab-btn" :class="{ active: activeSubTab === 'ssr' }" @click="activeSubTab = 'ssr'">SSR Stream</button>
            <button class="rx-tab-btn" :class="{ active: activeSubTab === 'vt' }" @click="activeSubTab = 'vt'">View Transitions</button>
            <button class="rx-tab-btn" :class="{ active: activeSubTab === 'icons' }" @click="activeSubTab = 'icons'">Static Icons</button>
          </div>
        </div>
        <div class="rx-card" style="margin-top: 0.75rem; font-size: 0.85rem;">
          <span v-if="activeSubTab === 'ssr'">Active Tab: <strong>SSR Stream</strong> — HTML-first rendering with serialized state.</span>
          <span v-else-if="activeSubTab === 'vt'">Active Tab: <strong>View Transitions</strong> — Smooth native page swaps.</span>
          <span v-else>Active Tab: <strong>Static Icons</strong> — 0 KB build-time SVG inlining.</span>
        </div>
      </div>

      <!-- RxPopover -->
      <div v-else-if="component === 'RxPopover'">
        <div class="rx-popover">
          <div><button class="rx-btn rx-btn-outline rx-btn-sm" @click="popoverOpen = !popoverOpen">{{ popoverOpen ? 'Close Popover' : 'Open Popover' }}</button></div>
          <div v-if="popoverOpen" class="rx-popover-content" style="min-width: 14rem; font-size: 0.825rem;">
            <strong>Popover Content</strong>
            <p style="margin: 0.25rem 0 0; opacity: 0.8;">Toggled via the <code>#trigger</code> slot and <code>update:open</code> event.</p>
          </div>
        </div>
      </div>

      <!-- RxDropdown -->
      <div v-else-if="component === 'RxDropdown'">
        <div class="rx-dropdown">
          <div><button class="rx-btn rx-btn-secondary rx-btn-sm" @click="dropdownOpen = !dropdownOpen">Actions Menu ▾</button></div>
          <ul v-if="dropdownOpen" class="rx-dropdown-menu">
            <li class="rx-dropdown-item" @click="dropdownOpen = false">Verify Framework Parity</li>
            <li class="rx-dropdown-item" @click="dropdownOpen = false">Build Production Output</li>
            <li class="rx-dropdown-item" @click="dropdownOpen = false">Inspect Halal Report</li>
          </ul>
        </div>
      </div>

      <!-- RxTooltip -->
      <div v-else-if="component === 'RxTooltip'" style="padding-top: 1.75rem;">
        <div class="rx-tooltip-wrapper" @mouseenter="tooltipVisible = true" @mouseleave="tooltipVisible = false">
          <button class="rx-btn rx-btn-outline rx-btn-sm">Hover or Focus Target</button>
          <div v-if="tooltipVisible" class="rx-tooltip rx-tooltip-top">Zero-CLS Fontaine fallback metrics enabled</div>
        </div>
      </div>

      <!-- RxModal -->
      <div v-else-if="component === 'RxModal'">
        <button v-if="!modalOpen" class="rx-btn rx-btn-primary rx-btn-sm" @click="modalOpen = true">Open RxModal</button>
        <div v-if="modalOpen" class="rx-modal-backdrop" @click.self="modalOpen = false">
          <div class="rx-modal-content">
            <h3 style="margin-top: 0; font-size: 1rem;">Confirm Production Deploy</h3>
            <p style="font-size: 0.85rem; opacity: 0.85;">Ready to deploy <code>resuxjs@0.4.0-beta.7</code> with signed Halal Core verification?</p>
            <div style="display: flex; justify-content: flex-end; gap: 0.5rem; margin-top: 1rem;">
              <button class="rx-btn rx-btn-ghost rx-btn-sm" @click="modalOpen = false">Cancel</button>
              <button class="rx-btn rx-btn-primary rx-btn-sm" @click="modalOpen = false">Deploy Now</button>
            </div>
          </div>
        </div>
      </div>

      <!-- RxMotion / RxReveal / RxAutoAnimate -->
      <div v-else-if="component === 'RxMotion' || component === 'RxReveal' || component === 'RxAutoAnimate'" style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; gap: 0.5rem;">
          <button class="rx-btn rx-btn-secondary rx-btn-sm" @click="motionKey++">Replay Animation</button>
          <button v-if="component === 'RxAutoAnimate'" class="rx-btn rx-btn-primary rx-btn-sm" @click="autoItems.push(`resuxjs/pkg-${autoItems.length + 1}`)">+ Add Item</button>
        </div>
        <div :key="motionKey" class="rx-card" style="transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
          <strong>{{ component }} Live Preview (Run #{{ motionKey }})</strong>
          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem;">
            <span v-for="item in autoItems" :key="item" class="rx-badge rx-badge-primary">{{ item }}</span>
          </div>
        </div>
      </div>

      <!-- RxIcon / Teleport / Transition fallback -->
      <div v-else style="display: flex; align-items: center; justify-content: space-between; gap: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <span class="rx-icon" style="font-size: 1.1rem; color: var(--vp-c-brand-1); font-weight: 700;">[check]</span>
          <span class="rx-badge rx-badge-success">{{ component }} Active</span>
        </div>
        <button class="rx-btn rx-btn-outline rx-btn-sm" @click="transitionVisible = !transitionVisible">Toggle State</button>
      </div>
    </div>

    <div v-else style="padding: 1rem; background: var(--resux-surface-muted); font-family: var(--vp-font-family-mono); font-size: 0.8rem;">
      <div>Rendered Component: <code>&lt;{{ component }} /&gt;</code></div>
      <div style="margin-top: 0.35rem; opacity: 0.8;">Pass <code>:unstyled="true"</code> to strip default <code>rx-*</code> classes for custom Tailwind styling.</div>
    </div>
  </div>
</template>
