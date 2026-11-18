import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
const BASE = 'http://localhost:8080/', OUT = '/home/claude/work/cache/pshots/';
const b = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
const T = new Date('2026-10-14T10:30:00+05:30');
async function page(url, mobile){
  const ctx = await b.newContext({ viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 }, deviceScaleFactor: mobile ? 2 : 1, isMobile: mobile, hasTouch: mobile, timezoneId: 'Asia/Kolkata' });
  const p = await ctx.newPage(); await p.clock.install({ time: T });
  await p.goto(BASE + url); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(700);
  return { p, ctx };
}
const snap = async (p, name) => { await p.waitForTimeout(350); await p.screenshot({ path: OUT + name + '.png' }); console.log('shot', name); };
const scrollTo = async (p, sel, off = 0) => { await p.evaluate(([s, o]) => { const el = document.querySelector(s); window.scrollTo(0, el.getBoundingClientRect().top + scrollY - o); }, [sel, off]); await p.waitForTimeout(400); };

// Mettle
{ let { p, ctx } = await page('mettle/_preview.html', false); await snap(p, 'mettle-desk');
  await p.click('[data-choose="hypertrophy"]'); await p.waitForTimeout(900); await p.check('#x-recovery', { force: true }); await p.click('label:has(#c-6)'); await scrollTo(p, '#membership', 70); await snap(p, 'mettle-desk-2'); await ctx.close();
  ({ p, ctx } = await page('mettle/_preview.html', true)); await snap(p, 'mettle-mob');
  await scrollTo(p, '#programmes', 60); await p.click('[data-open="barbell"]'); await p.waitForTimeout(600); await snap(p, 'mettle-mob-2'); await ctx.close(); }
// Dabara
{ let { p, ctx } = await page('dabara/_preview.html', false); await snap(p, 'dabara-desk');
  await p.click('[data-add="bun"]'); await p.click('#opts-add'); await p.waitForTimeout(300); await p.click('[data-add="filter"]'); await p.click('#opts-add'); await p.waitForTimeout(300); await p.click('[data-add="podi"]'); await p.click('#opts-add'); await p.waitForTimeout(300);
  await p.click('#basket-btn'); await p.waitForTimeout(600); await p.fill('#o-name', 'Ananya'); await snap(p, 'dabara-desk-2'); await ctx.close();
  ({ p, ctx } = await page('dabara/_preview.html', true));
  await scrollTo(p, '#menu', 0); await p.fill('#q', 'kaapi'); await p.waitForTimeout(300); await p.click('[data-add="tonic"]'); await p.click('#opts-add'); await p.waitForTimeout(500); await snap(p, 'dabara-mob');
  await p.click('#mbar-btn'); await p.waitForTimeout(500); await p.fill('#o-name', 'Ananya'); await p.fill('#o-phone', '98765 43210'); await p.click('#place'); await p.waitForTimeout(500); await snap(p, 'dabara-mob-2'); await ctx.close(); }
// Fringe
{ let { p, ctx } = await page('fringe/_preview.html', false); await snap(p, 'fringe-desk');
  await p.click('label[for="s-gloss"]'); await p.click('label:has(#patch-yes)'); await p.click('#next'); await p.waitForTimeout(300); await p.click('#next'); await p.waitForTimeout(400);
  const d = await p.evaluate(() => [...document.querySelectorAll('.day[data-iso]:not([aria-disabled="true"])')][1].dataset.iso); await p.click('.day[data-iso="' + d + '"]'); await p.waitForTimeout(200);
  await p.click('.chip >> nth=2'); await scrollTo(p, '.times-book', 140); await snap(p, 'fringe-desk-2'); await ctx.close();
  ({ p, ctx } = await page('fringe/_preview.html', true)); await snap(p, 'fringe-mob');
  await p.click('#next'); await p.waitForTimeout(300); await p.click('#next'); await p.waitForTimeout(300);
  const d2 = await p.evaluate(() => [...document.querySelectorAll('.day[data-iso]:not([aria-disabled="true"])')][0].dataset.iso); await p.click('.day[data-iso="' + d2 + '"]'); await p.click('.chip >> nth=1'); await p.click('#next'); await p.waitForTimeout(300);
  await p.fill('#f-name', 'Ritika Jain'); await p.fill('#f-phone', '98200 12345'); await p.click('#next'); await p.waitForTimeout(300); await p.click('#next'); await p.waitForTimeout(500);
  await scrollTo(p, '.panel', 70); await snap(p, 'fringe-mob-2'); await ctx.close(); }
// Hookloop
{ let { p, ctx } = await page('hookloop/_preview.html', false); await p.waitForTimeout(2600); await snap(p, 'hookloop-desk');
  await p.click('#grid [data-open="dabara-02-cold-story"]'); await p.waitForTimeout(500); await p.click('#lb-zones'); await snap(p, 'hookloop-desk-2'); await ctx.close();
  ({ p, ctx } = await page('hookloop/_preview.html', true)); await p.waitForTimeout(2600); await snap(p, 'hookloop-mob');
  await scrollTo(p, '#gallery', 64); await p.click('#f-brand [data-b="mettle"]'); await p.waitForTimeout(600); await scrollTo(p, '#grid', 120); await p.waitForTimeout(600); await snap(p, 'hookloop-mob-2'); await ctx.close(); }
await b.close();
