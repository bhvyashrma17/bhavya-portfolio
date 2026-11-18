// Usage: node shoot.mjs jobs.json   — each job: {url, out, w, h, dpr, full, mobile, steps:[{click|fill|press|wait|eval|scroll}], clip}
import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const browser = await chromium.launch();
const errors = [];
for (const j of jobs) {
  const ctx = await browser.newContext({ viewport: { width: j.w || 1440, height: j.h || 900 }, deviceScaleFactor: j.dpr || 1,
    isMobile: !!j.mobile, hasTouch: !!j.mobile, reducedMotion: j.reduced ? 'reduce' : 'no-preference', colorScheme: j.scheme || 'light' });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(`[${j.out}] pageerror: ${e.message}`));
  page.on('console', m => { if (m.type() === 'error') errors.push(`[${j.out}] console: ${m.text()}`); });
  await page.goto(j.url, { waitUntil: 'load' });
  if (j.clearStorage) { await page.evaluate(() => { try { localStorage.clear(); } catch(e){} }); await page.reload({ waitUntil: 'load' }); }
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(j.settle ?? 600);
  for (const s of (j.steps || [])) {
    if (s.click) await page.click(s.click, { timeout: 5000 });
    if (s.tap) await page.tap(s.tap, { timeout: 5000 });
    if (s.fill) await page.fill(s.fill, s.value);
    if (s.press) await page.keyboard.press(s.press);
    if (s.select) await page.selectOption(s.select, s.value);
    if (s.eval) await page.evaluate(s.eval);
    if (s.scroll) await page.evaluate(sel => { const el = document.querySelector(sel); if (el) el.scrollIntoView({ block: 'start' }); }, s.scroll);
    if (s.scrollY !== undefined) await page.evaluate(y => window.scrollTo(0, y), s.scrollY);
    if (s.wait) await page.waitForTimeout(s.wait);
    if (s.shot) await page.screenshot({ path: s.shot, fullPage: !!s.full });
  }
  if (j.out) await page.screenshot({ path: j.out, fullPage: !!j.full, clip: j.clip });
  if (j.report) { const r = await page.evaluate(j.report); console.log(`[${j.out}] report:`, JSON.stringify(r)); }
  await ctx.close();
}
await browser.close();
if (errors.length) { console.log('ERRORS:\n' + errors.join('\n')); } else { console.log('ok, no page errors'); }
