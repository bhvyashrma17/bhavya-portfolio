import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
const URL = 'http://localhost:8080/fringe/_preview.html';
const OUT = '/home/claude/work/cache/fringe-shots/';
const b = await chromium.launch();
const log = (...a) => console.log(...a);
async function run(kind){
  const mobile = kind !== 'desktop';
  const vp = kind === 'desktop' ? { width: 1440, height: 900 } : kind === 'm375' ? { width: 375, height: 667 } : { width: 390, height: 844 };
  const ctx = await b.newContext({ viewport: vp, isMobile: mobile, hasTouch: mobile, timezoneId: 'Asia/Kolkata' });
  const p = await ctx.newPage(); const errs = [];
  p.on('pageerror', e => errs.push('pageerror ' + e.message)); p.on('console', m => { if (m.type() === 'error') errs.push('console ' + m.text()); });
  await p.goto(URL); await p.waitForTimeout(500);
  const overflow = async tag => { const o = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); if (o > 0) log(kind, 'OVERFLOW', tag, o); };
  await overflow('start');
  if (kind === 'desktop') await p.screenshot({ path: OUT + 'd-top.png' });
  if (kind === 'm390') await p.screenshot({ path: OUT + 'm-top.png' });
  // step 1: add gloss (colour) -> patch question appears; brow disabled
  await p.click('label[for="s-gloss"]');
  log(kind, 'services', await p.evaluate(() => [...document.querySelectorAll('.svc input:checked')].map(i => i.value).join(',')), 'patchQ', !!(await p.$('.patch-q')), 'thread disabled', await p.$eval('#s-thread', el => el.disabled));
  await p.click('#next'); await p.waitForTimeout(300);
  log(kind, 'step2 stylists enabled', await p.evaluate(() => [...document.querySelectorAll('input[name=stylist]:not(:disabled)')].map(i => i.value).join(',')));
  await p.click('label[for="t-lavanya"]');
  await p.click('#next'); await p.waitForTimeout(300);
  // step 3: first enabled date
  const days = await p.evaluate(() => [...document.querySelectorAll('.day[data-iso]')].map(d => [d.dataset.iso, d.getAttribute('aria-disabled')]));
  const firstOk = days.find(d => d[1] !== 'true');
  const firstBad = days.find(d => d[1] === 'true');
  log(kind, 'month days', days.length, 'first ok', firstOk && firstOk[0], 'first unavailable', firstBad && firstBad[0]);
  if (firstBad) { await p.$eval('.day[data-iso="' + firstBad[0] + '"]', el => el.click()); log(kind, 'why:', await p.textContent('#day-msg')); }
  await p.click('.day[data-iso="' + firstOk[0] + '"]'); await p.waitForTimeout(200);
  const chips = await p.$$eval('.chip', cs => cs.map(c => c.textContent));
  log(kind, 'chips', chips.length, chips.slice(0, 6).join(' '));
  await p.click('.chip >> nth=1'); await p.waitForTimeout(200);
  if (kind === 'desktop') await p.screenshot({ path: OUT + 'd-time.png' });
  if (kind === 'm390') { await p.screenshot({ path: OUT + 'm-time.png', fullPage: false }); }
  await overflow('step3');
  await p.click('#next'); await p.waitForTimeout(300);
  // step 4: validation
  await p.click('#next'); log(kind, 'name err:', await p.textContent('#f-name-err'));
  await p.fill('#f-name', 'Priya Nair'); await p.fill('#f-phone', '12345'); await p.click('#next');
  log(kind, 'phone err:', await p.textContent('#f-phone-err'));
  await p.fill('#f-phone', '98765 43210'); await p.fill('#f-email', 'priya@'); await p.click('#next');
  log(kind, 'email err:', await p.textContent('#f-email-err'));
  await p.fill('#f-email', ''); await p.click('#next'); await p.waitForTimeout(300);
  log(kind, 'review title', await p.textContent('#step-title'), '| next btn', await p.textContent('#next'));
  await p.click('#next'); await p.waitForTimeout(300);
  const ref = await p.textContent('.ref');
  log(kind, 'done', await p.textContent('#done-title'), ref, '| warn:', (await p.textContent('.demo-warn')).slice(0, 60));
  if (kind === 'desktop') await p.screenshot({ path: OUT + 'd-done.png' });
  if (kind === 'm390') await p.screenshot({ path: OUT + 'm-done.png' });
  await p.click('#copy'); await p.waitForTimeout(200); log(kind, 'copy btn ->', await p.textContent('#copy'), !!(await p.$('#copy-ta')));
  // my bookings: change time then cancel
  await p.click('#mine-btn'); await p.waitForTimeout(350);
  log(kind, 'mine count', await p.$$eval('.bk', x => x.length));
  await p.click('[data-move]'); await p.waitForTimeout(600);
  log(kind, 'after change: step', await p.textContent('#step-title'), 'notice', !!(await p.$('.notice')));
  const d2 = await p.evaluate(() => [...document.querySelectorAll('.day[data-iso]:not([aria-disabled="true"])')].map(d => d.dataset.iso)[1]);
  await p.click('.day[data-iso="' + d2 + '"]'); await p.click('.chip >> nth=0'); await p.click('#next'); await p.waitForTimeout(250);
  await p.click('#next'); await p.waitForTimeout(250); await p.click('#next'); await p.waitForTimeout(250);
  log(kind, 'moved:', await p.textContent('#done-title'), await p.textContent('.ref') === ref ? 'same ref' : 'NEW REF');
  await p.click('#mine-btn'); await p.waitForTimeout(350);
  await p.click('[data-cancel]'); await p.click('[data-yes]'); await p.waitForTimeout(200);
  log(kind, 'after cancel count', await p.$$eval('.bk', x => x.length));
  await p.keyboard.press('Escape'); await p.waitForTimeout(300);
  log(kind, 'dialog closed', !(await p.evaluate(() => document.getElementById('mine').open)));
  await overflow('end');
  log(kind, 'errors', errs.length ? errs : 'none');
  await ctx.close();
}
await run('desktop'); await run('m390'); await run('m375');
// storage blocked
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addInitScript(() => { Object.defineProperty(window, 'localStorage', { configurable: true, get() { throw new DOMException('blocked', 'SecurityError'); } }); });
const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto(URL); await p.waitForTimeout(300);
await p.click('#next'); await p.click('#next'); await p.waitForTimeout(200);
const ok = await p.evaluate(() => [...document.querySelectorAll('.day[data-iso]:not([aria-disabled="true"])')][0].dataset.iso);
await p.click('.day[data-iso="' + ok + '"]'); await p.click('.chip >> nth=0'); await p.click('#next');
await p.fill('#f-name', 'Test User'); await p.fill('#f-phone', '9876543210'); await p.click('#next'); await p.click('#next'); await p.waitForTimeout(200);
console.log('storage blocked -> done:', await p.textContent('#done-title'), 'errors', errs);
await b.close();
