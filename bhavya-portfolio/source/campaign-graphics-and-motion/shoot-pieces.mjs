// Render graphic pieces to PNG at exact pixel size (deviceScaleFactor 1).
// Usage: node shoot-pieces.mjs pieces.json [filter-substring]
// pieces.json: [{id, file, w, h}]  file is relative to cache/hookloop-src/pieces/
import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const list = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const only = process.argv[3] || '';
const OUT = '/home/claude/work/cache/hookloop-tmp/png';
fs.mkdirSync(OUT, { recursive: true });
const browser = await chromium.launch();
const problems = [];
for (const p of list) {
  if (only && !p.id.includes(only)) continue;
  const ctx = await browser.newContext({ viewport: { width: p.w, height: p.h }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  page.on('pageerror', e => problems.push(`${p.id}: pageerror ${e.message}`));
  page.on('console', m => { if (m.type() === 'error') problems.push(`${p.id}: console ${m.text()}`); });
  page.on('requestfailed', r => problems.push(`${p.id}: failed ${r.url()}`));
  page.on('response', r => { if (r.status() >= 400) problems.push(`${p.id}: ${r.status()} ${r.url()}`); });
  await page.goto(`http://localhost:8090/cache/hookloop-src/pieces/${p.file}`, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => !document.querySelector('[data-fit]') || document.documentElement.dataset.fitted === '1', null, { timeout: 5000 });
  // report any declared family that failed to load
  const bad = await page.evaluate(() => Array.from(document.fonts).filter(f => f.status === 'error').map(f => f.family));
  if (bad.length) problems.push(`${p.id}: font errors ${bad.join(',')}`);
  await page.waitForTimeout(150);
  const size = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight]);
  if (size[0] > p.w || size[1] > p.h) problems.push(`${p.id}: overflow ${size.join('x')} > ${p.w}x${p.h}`);
  await page.screenshot({ path: `${OUT}/${p.id}.png`, clip: { x: 0, y: 0, width: p.w, height: p.h } });
  await ctx.close();
  process.stdout.write(p.id + ' ');
}
await browser.close();
console.log('\n' + (problems.length ? 'PROBLEMS:\n' + problems.join('\n') : 'ok'));
