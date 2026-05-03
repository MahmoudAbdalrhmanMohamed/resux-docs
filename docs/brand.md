# Brand System

Resux should feel fast, technical, and futuristic without losing readability.

## Logo

<div class="logo-wall">
  <div><img src="/logo.svg" alt="Resux full logo" /></div>
  <div><img src="/logo-mark.svg" alt="Resux mark" style="max-width: 128px" /></div>
</div>

The mark combines:

- A resumability loop for pause/resume behavior.
- A plus/cross shape for composition and framework primitives.
- Cyan, violet, and mint gradients for runtime energy.

## Color palette

<div class="brand-grid">
  <div class="brand-card"><div class="brand-swatch" style="background:#070A13"></div><strong>Ink Core</strong><br><code>#070A13</code><br>Primary dark base.</div>
  <div class="brand-card"><div class="brand-swatch" style="background:#111827"></div><strong>Slate Engine</strong><br><code>#111827</code><br>Panels and docs surfaces.</div>
  <div class="brand-card"><div class="brand-swatch" style="background:#7C3AED"></div><strong>Resux Violet</strong><br><code>#7C3AED</code><br>Main brand action color.</div>
  <div class="brand-card"><div class="brand-swatch" style="background:#22D3EE"></div><strong>Runtime Cyan</strong><br><code>#22D3EE</code><br>Runtime and link accent.</div>
  <div class="brand-card"><div class="brand-swatch" style="background:#10B981"></div><strong>Resume Mint</strong><br><code>#10B981</code><br>Success and resume state.</div>
  <div class="brand-card"><div class="brand-swatch" style="background:#F59E0B"></div><strong>Signal Amber</strong><br><code>#F59E0B</code><br>Warnings and callouts.</div>
  <div class="brand-card"><div class="brand-swatch" style="background:#F8FAFC"></div><strong>Cloud Text</strong><br><code>#F8FAFC</code><br>High-contrast text.</div>
  <div class="brand-card"><div class="brand-swatch" style="background:#94A3B8"></div><strong>Muted Steel</strong><br><code>#94A3B8</code><br>Secondary text.</div>
</div>

## Gradients

Primary gradient:

```css
linear-gradient(120deg, #7C3AED 20%, #06B6D4 58%, #10B981 95%)
```

Dark hero glow:

```css
radial-gradient(circle at 50% 50%, rgba(124, 58, 237, 0.28), rgba(6, 182, 212, 0.18), transparent 68%)
```

## Usage rules

- Use the mark alone for favicons, social icons, and compact nav.
- Use the full logo for hero areas and Open Graph images.
- Keep enough clear space around the mark: at least one quarter of the mark width.
- Prefer dark backgrounds for brand-heavy moments.
- Use violet for primary actions and cyan for links or runtime highlights.

## Asset paths

```txt
docs/public/logo.svg
docs/public/logo-mark.svg
docs/public/og-image.svg
```
