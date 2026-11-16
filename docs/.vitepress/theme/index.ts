import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import RxComponentPreview from './components/RxComponentPreview.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('RxComponentPreview', RxComponentPreview)
  }
} satisfies Theme
