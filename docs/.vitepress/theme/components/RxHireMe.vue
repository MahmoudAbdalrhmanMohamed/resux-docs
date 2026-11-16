<script setup lang="ts">
import { ref } from 'vue'

const copied = ref(false)
const email = 'mahnoudhouda5632@gmail.com'

function copyEmail() {
  if (typeof navigator !== 'undefined' && navigator.clipboard?.writeText) {
    navigator.clipboard.writeText(email)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2500)
  }
}
</script>

<template>
  <div id="hire-me" class="resux-home-section">
    <div class="resux-hire-card">
      <div class="resux-hire-status">
        <span class="resux-hire-status-dot"></span>
        Available for Hire &amp; Consulting
      </div>

      <h2 class="resux-home-title" style="margin-top: 8px;">
        Need an Experienced Full-Stack &amp; Framework Architect?
      </h2>

      <p class="resux-home-lead">
        Hi, I’m <strong>Mahmoud Abdalrahman Mohamed</strong> — creator and lead architect of <strong>Resux</strong>. I help engineering teams and founders design and deliver ultra-fast web applications, high-performance Vue 3 &amp; Nuxt 3/4 architectures, resumable rendering pipelines, and custom developer tooling.
      </p>

      <div class="resux-hire-services">
        <div class="resux-hire-service-item">
          <strong>⚡ Full-Stack &amp; Modern Frontend</strong>
          <p>Production engineering with Vue 3, Nuxt, TypeScript, Vite, Nitro, and Tailwind CSS. Complex SPAs, SSR, and resumable architectures.</p>
        </div>
        <div class="resux-hire-service-item">
          <strong>🚀 Performance &amp; Core Web Vitals</strong>
          <p>Eliminating FOUC/CLS, sub-second TTFB, metric-adjusted font overrides, streaming SSR, bundle size reduction, and asset pipelines.</p>
        </div>
        <div class="resux-hire-service-item">
          <strong>🛠️ Frameworks &amp; Developer Tooling</strong>
          <p>Custom Vite plugins, CLI toolkits, AST transforms, compiler pipelines, design systems, and headless component libraries.</p>
        </div>
      </div>

      <div class="resux-hire-actions">
        <a class="resux-hire-btn-primary" href="mailto:mahnoudhouda5632@gmail.com?subject=Work%20Inquiry%20from%20Resux%20Docs">
          ✉️ Get in Touch (Email Me)
        </a>
        <button type="button" class="resux-hire-btn-secondary" @click="copyEmail" :aria-label="copied ? 'Email copied' : 'Copy email address'">
          {{ copied ? '✅ Email Copied!' : '📋 Copy Email' }}
        </button>
        <a class="resux-hire-btn-secondary" href="https://github.com/MahmoudAbdalrhmanMohamed" target="_blank" rel="noopener noreferrer">
          🐙 GitHub Profile
        </a>
        <span class="resux-hire-meta">
          Direct: <strong>mahnoudhouda5632@gmail.com</strong> · Open to Full-time, Contract &amp; Consulting Worldwide
        </span>
      </div>
    </div>
  </div>
</template>
