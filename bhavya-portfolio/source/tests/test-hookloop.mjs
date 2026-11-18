import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
const URL = 'http://localhost:8080/hookloop/_preview.html', OUT = '/home/claude/work/cache/hookloop-shots/';
const b = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
for (const kind of ['desktop', 'm390', 'm375']) {
  const mobile = kind !== 'desktop';
  const ctx = await b.newContext({ viewport: kind === 'desktop' ? { width: 1440, height: 900 } : { width: kind === 'm375' ? 375 : 390, height: kind === 'm375' ? 667 : 844 }, isMobile: mobile, hasTouch: mobile });
  const p = await ctx.newPage(); const errs = [], bad = [];
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  p.on('response', r => { if (r.status() >= 400) bad.push(r.status() + ' ' + r.url()); });
  await p.goto(URL); await p.waitForTimeout(2200);
  const ov = async t => { const o = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); if (o > 0) console.log(kind, 'OVERFLOW', t, o); };
  await ov('top');
  if (kind !== 'm375') await p.screenshot({ path: OUT + kind + '-top.png' });
  console.log(kind, 'hero playing:', await p.evaluate(() => !document.getElementById('v-hero').paused), 'tc:', await p.textContent('.player[data-for="v-hero"] .tc'));
  // gallery filters
  await p.click('#f-brand [data-b="dabara"]'); console.log(kind, 'dabara:', await p.textContent('#gcount'));
  await p.click('#f-format [data-f="story"]'); console.log(kind, 'dabara+story:', await p.textContent('#gcount'));
  await p.click('#f-brand [data-b="all"]'); console.log(kind, 'all stories:', await p.textContent('#gcount'));
  await p.click('#f-format [data-f="all"]');
  // lightbox
  await p.click('#grid [data-open="mettle-05-story-tomorrow"]'); await p.waitForTimeout(400);
  console.log(kind, 'lb:', await p.textContent('#lb-title'), '|', await p.textContent('#lb-fmt'), '|', await p.textContent('#lb-cnt'));
  await p.click('#lb-zones'); await p.waitForTimeout(150); console.log(kind, 'zones on:', await p.evaluate(() => !document.getElementById('lb-zonelayer').hidden));
  if (kind !== 'm375') await p.screenshot({ path: OUT + kind + '-lightbox.png' });
  await p.keyboard.press('ArrowRight'); await p.waitForTimeout(200); console.log(kind, 'next ->', await p.textContent('#lb-title'));
  const imgOk = await p.evaluate(() => { const i = document.getElementById('lb-img'); return i.complete && i.naturalWidth > 0; });
  console.log(kind, 'lb img loaded', imgOk);
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); console.log(kind, 'lb closed', !(await p.evaluate(() => document.getElementById('lb').open)));
  // motion players
  await p.locator('#motion').scrollIntoViewIfNeeded(); await p.waitForTimeout(300);
  await p.click('.player[data-for="v-dabara"] .pp'); await p.waitForTimeout(1300);
  console.log(kind, 'dabara playing', await p.evaluate(() => !document.getElementById('v-dabara').paused), 'hero paused', await p.evaluate(() => document.getElementById('v-hero').paused), 'tc', await p.textContent('.player[data-for="v-dabara"] .tc'));
  await p.click('.player[data-for="v-dabba"] .pp'); await p.waitForTimeout(600);
  console.log(kind, 'dabba playing, dabara paused:', await p.evaluate(() => !document.getElementById('v-dabba').paused && document.getElementById('v-dabara').paused));
  if (kind !== 'm375') await p.screenshot({ path: OUT + kind + '-motion.png' });
  // all images in grid loaded?
  await p.evaluate(async () => { for (const i of document.querySelectorAll('img')) { i.loading = 'eager'; } });
  await p.waitForTimeout(1200);
  const broken = await p.evaluate(() => [...document.querySelectorAll('img')].filter(i => !i.complete || !i.naturalWidth).map(i => i.src));
  console.log(kind, 'broken imgs', broken.length, 'bad responses', bad, 'errors', errs.length ? errs : 'none');
  await ov('end');
  await ctx.close();
}
await b.close();
