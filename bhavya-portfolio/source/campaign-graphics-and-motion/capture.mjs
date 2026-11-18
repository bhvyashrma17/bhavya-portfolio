// node capture.mjs <file> <cssW> <cssH> <outW> <seconds> <outdir> [fps]
import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const [file, cw, ch, ow, secs, outdir, fpsArg] = process.argv.slice(2);
const fps = +(fpsArg || 30), dsf = +ow / +cw;
fs.rmSync(outdir, { recursive: true, force: true }); fs.mkdirSync(outdir, { recursive: true });
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: +cw, height: +ch }, deviceScaleFactor: dsf });
const p = await ctx.newPage(); const errs = [];
p.on('pageerror', e => errs.push(e.message)); p.on('requestfailed', r => errs.push('failed ' + r.url()));
await p.goto('http://localhost:8090/cache/hookloop-src/motion/' + file, { waitUntil: 'load' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
const n = Math.round(+secs * fps);
for (let i = 0; i < n; i++) {
  await p.evaluate(t => render(t), i / fps);
  await p.screenshot({ path: `${outdir}/f${String(i).padStart(4, '0')}.png` });
}
await b.close();
console.log(file, n, 'frames', errs.length ? errs : 'ok');
