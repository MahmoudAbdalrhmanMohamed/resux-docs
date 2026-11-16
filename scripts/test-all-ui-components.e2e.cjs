const { chromium } = require('E:/resux-projects/resux-lab/node_modules/playwright');

const COMPONENT_ROUTES = [
  '/',
  '/components/',
  '/components/button',
  '/components/input',
  '/components/textarea',
  '/components/select',
  '/components/date-picker',
  '/components/verification-code',
  '/components/switch',
  '/components/card',
  '/components/badge',
  '/components/avatar',
  '/components/alert',
  '/components/skeleton',
  '/components/divider',
  '/components/kbd',
  '/components/accordion',
  '/components/tabs',
  '/components/popover',
  '/components/dropdown',
  '/components/tooltip',
  '/components/modal',
  '/components/motion',
  '/components/reveal',
  '/components/auto-animate',
  '/components/icon',
  '/components/teleport',
  '/components/transition',
  '/components/component-anatomy'
];

async function run() {
  console.log(`Starting Playwright test run across ${COMPONENT_ROUTES.length} routes...`);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });

  const failures = [];
  let tested = 0;

  for (const route of COMPONENT_ROUTES) {
    const url = `http://localhost:5173/resux-docs${route}`;
    const pageErrors = [];
    const consoleErrors = [];

    const pageErrorHandler = err => pageErrors.push(err.message);
    const consoleHandler = msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    };

    page.on('pageerror', pageErrorHandler);
    page.on('console', consoleHandler);

    try {
      const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 8000 });
      const status = resp ? resp.status() : 0;
      if (status >= 400) {
        failures.push({ route, issue: `HTTP status ${status}` });
      }

      // Check if preview component exists (except on root /)
      if (route !== '/') {
        const previewEl = await page.$('.rx-preview-container');
        if (!previewEl) {
          failures.push({ route, issue: 'Missing .rx-preview-container' });
        } else {
          // Verify tab switching works
          const codeTab = await page.$('.rx-mode-tab:has-text("Vue Code")');
          if (codeTab) {
            await codeTab.click();
            await page.waitForTimeout(50);
            const codeBlock = await page.$('.rx-code-block');
            if (!codeBlock) {
              failures.push({ route, issue: 'Vue Code tab did not render code block' });
            }
            // Switch back to Preview
            const previewTab = await page.$('.rx-mode-tab:has-text("Preview")');
            if (previewTab) await previewTab.click();
          }
        }
      }

      if (pageErrors.length > 0) {
        failures.push({ route, issue: `Page errors: ${pageErrors.join('; ')}` });
      }
      if (consoleErrors.length > 0) {
        failures.push({ route, issue: `Console errors: ${consoleErrors.join('; ')}` });
      }

      tested++;
      process.stdout.write(`✓ [${tested}/${COMPONENT_ROUTES.length}] ${route}\n`);
    } catch (err) {
      failures.push({ route, issue: `Navigation exception: ${err.message}` });
    } finally {
      page.off('pageerror', pageErrorHandler);
      page.off('console', consoleHandler);
    }
  }

  // Also test dark mode toggle on /components/
  try {
    await page.goto('http://localhost:5173/resux-docs/components/', { waitUntil: 'networkidle' });
    await page.evaluate(() => document.documentElement.classList.add('dark'));
    await page.waitForTimeout(300);
    await page.screenshot({ path: 'C:/Users/origin/.gemini/antigravity/brain/d38151d9-7104-4626-969e-e91ffb7c56a5/components-suite-dark-verified.png' });
    console.log('✓ Captured components-suite-dark-verified.png');

    // Test mobile viewport
    await page.setViewportSize({ width: 375, height: 812 });
    await page.waitForTimeout(300);
    await page.screenshot({ path: 'C:/Users/origin/.gemini/antigravity/brain/d38151d9-7104-4626-969e-e91ffb7c56a5/components-suite-mobile-verified.png' });
    console.log('✓ Captured components-suite-mobile-verified.png');
  } catch (err) {
    failures.push({ route: 'dark/mobile screenshots', issue: err.message });
  }

  await browser.close();

  console.log('\n========================================');
  console.log(`Results: ${tested - failures.length}/${tested} routes passed`);
  if (failures.length > 0) {
    console.error('Failures encountered:');
    for (const f of failures) {
      console.error(`- ${f.route}: ${f.issue}`);
    }
    process.exit(1);
  } else {
    console.log('ALL UI COMPONENT ROUTES PASSED PLAYWRIGHT VERIFICATION! 🎉');
    process.exit(0);
  }
}

run();
