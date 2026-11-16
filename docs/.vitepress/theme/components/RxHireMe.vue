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
      <div class="resux-hire-status-row">
        <div class="resux-hire-status">
          <span class="resux-hire-status-dot"></span>
          Available for Hire &amp; Consulting
        </div>
        <div class="resux-hire-tags">
          <span class="resux-tech-pill node">Node.js</span>
          <span class="resux-tech-pill nest">NestJS</span>
          <span class="resux-tech-pill">TypeScript</span>
          <span class="resux-tech-pill">Vue 3 &amp; Nuxt</span>
          <span class="resux-tech-pill">Resux Architect</span>
        </div>
      </div>

      <h2 class="resux-home-title" style="margin-top: 10px;">
        Need an Experienced Full-Stack &amp; Framework Architect?
      </h2>

      <p class="resux-home-lead">
        Hi, I’m <strong>Mahmoud Abdalrahman Mohamed</strong> — creator and lead architect of <strong>Resux</strong>. I build scalable backend architectures and high-performance frontends using <strong>Node.js</strong>, <strong>NestJS</strong>, <strong>TypeScript</strong>, <strong>Vue 3</strong>, and <strong>Nuxt 3/4</strong>. I help engineering teams and founders design mission-critical APIs, microservices, resumable SSR pipelines, and high-throughput real-time systems.
      </p>

      <div class="resux-hire-services">
        <div class="resux-hire-service-item">
          <strong>
            <svg class="resux-service-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
            </svg>
            Node.js &amp; NestJS Backend Architecture
          </strong>
          <p>Production enterprise services using NestJS, modular dependency injection, RESTful &amp; GraphQL APIs, microservices, WebSockets, background job queues, and robust auth/RBAC flows.</p>
        </div>
        <div class="resux-hire-service-item">
          <strong>
            <svg class="resux-service-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
            </svg>
            Full-Stack &amp; Modern Frontend
          </strong>
          <p>Production engineering with Vue 3, Nuxt, TypeScript, Vite, Nitro, and Tailwind CSS. Complex SPAs, SSR streaming, and resumable architectures.</p>
        </div>
        <div class="resux-hire-service-item">
          <strong>
            <svg class="resux-service-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z" />
              <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z" />
            </svg>
            Performance, Caching &amp; Core Web Vitals
          </strong>
          <p>Sub-second TTFB, PostgreSQL &amp; Redis caching layers, zero-CLS font metrics, asset bundling optimization, streaming SSR, and database query tuning.</p>
        </div>
        <div class="resux-hire-service-item">
          <strong>
            <svg class="resux-service-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" />
            </svg>
            Frameworks, CLIs &amp; Developer Tooling
          </strong>
          <p>Custom Vite/Rollup plugins, CLI toolkits, AST code transforms, build compiler pipelines, design systems, and headless component libraries.</p>
        </div>
      </div>

      <div class="resux-hire-actions">
        <a class="resux-hire-btn-primary" href="mailto:mahnoudhouda5632@gmail.com?subject=Work%20Inquiry%20from%20Resux%20Docs%20(Node.js%20/%20NestJS%20/%20Full-Stack)">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2" />
            <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
          </svg>
          <span>Get in Touch (Email Me)</span>
        </a>
        <button type="button" class="resux-hire-btn-secondary" @click="copyEmail" :aria-label="copied ? 'Email copied' : 'Copy email address'">
          <svg v-if="copied" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12" />
          </svg>
          <svg v-else width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
          </svg>
          <span>{{ copied ? 'Email Copied!' : 'Copy Email' }}</span>
        </button>
        <a class="resux-hire-btn-secondary" href="https://github.com/MahmoudAbdalrhmanMohamed" target="_blank" rel="noopener noreferrer">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" />
          </svg>
          <span>GitHub Profile</span>
        </a>
        <span class="resux-hire-meta">
          Direct: <strong>mahnoudhouda5632@gmail.com</strong> · Open to Full-time, Contract &amp; Consulting Worldwide
        </span>
      </div>
    </div>
  </div>
</template>
