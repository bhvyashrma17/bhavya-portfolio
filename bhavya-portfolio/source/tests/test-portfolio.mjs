import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
const URL = 'http://localhost:8080/portfolio/_preview.html', OUT = '/home/claude/work/cache/portfolio-shots/';
const b = await chromium.launch();
for (const kind of ['desktop', 'm390', 'm375']) {
  const mobile = kind !== 'desktop';
  const ctx = await b.newContext({ viewport: kind === 'desktop' ? { width: 1440, height: 900 } : { width: kind === 'm375' ? 375 : 390, height: 844 }, isMobile: mobile, hasTouch: mobile });
  const p = await ctx.newPage(); const errs = [], bad = [];
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  p.on('response', r => { if (r.status() >= 400) bad.push(r.status() + ' ' + r.url()); });
  await p.goto(URL); await p.waitForTimeout(1600);
  const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
  await p.evaluate(async () => { document.querySelectorAll('img').forEach(i => i.loading = 'eager'); }); await p.waitForTimeout(1500);
  const broken = await p.evaluate(() => [...document.querySelectorAll('img')].filter(i => !i.complete || !i.naturalWidth).map(i => i.src));
  const links = await p.evaluate(() => [...document.querySelectorAll('a[href^="http"], a[href^="mailto"]')].map(a => a.href));
  const anchors = await p.evaluate(() => [...document.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute('href')).filter(h => h.length > 1 && !document.querySelector(h)));
  console.log(kind, 'overflow', ov, 'broken', broken.length, 'bad', bad, 'errors', errs, 'dead anchors', anchors);
  if (kind === 'desktop') console.log([...new Set(links)].join('\n'));
  await p.screenshot({ path: OUT + kind + '-full.png', fullPage: true });
  await ctx.close();
}
await b.close();
