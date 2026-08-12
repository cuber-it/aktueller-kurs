import { defineConfig, devices } from '@playwright/test';

/**
 * Zielumgebung ueber LOTTOBUDE_URL umstellen:
 *   TN 1     https://playground.uc-it.de:10000
 *   TN 2     https://playground.uc-it.de:10001
 *   Review   https://playground.uc-it.de
 */
export default defineConfig({
  testDir: '.',
  fullyParallel: false,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never' }]],

  use: {
    baseURL: process.env.LOTTOBUDE_URL ?? 'https://playground.uc-it.de',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    locale: 'de-DE',
  },

  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
