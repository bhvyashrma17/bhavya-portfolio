// Static server for Bhavya Sharma's portfolio on Railway. No dependencies.
const http = require('http');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const ROOT = path.join(__dirname, 'public');
const PORT = process.env.PORT || 3000;
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json', '.txt': 'text/plain; charset=utf-8', '.svg': 'image/svg+xml', '.ico': 'image/x-icon',
  '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.mp4': 'video/mp4', '.webm': 'video/webm', '.woff2': 'font/woff2'
};
const COMPRESS = new Set(['.html', '.css', '.js', '.json', '.svg', '.txt']);

function send404(res) {
  const file = path.join(ROOT, '404.html');
  fs.readFile(file, (err, buf) => {
    res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(err ? 'Not found' : buf);
  });
}

const server = http.createServer((req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') { res.writeHead(405, { Allow: 'GET, HEAD' }); return res.end(); }
  let pathname;
  try { pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname); } catch (e) { res.writeHead(400); return res.end(); }
  if (pathname.includes('\0')) { res.writeHead(400); return res.end(); }
  let file = path.normalize(path.join(ROOT, pathname));
  if (file !== ROOT && !file.startsWith(ROOT + path.sep)) { res.writeHead(403); return res.end(); }

  fs.stat(file, (err, st) => {
    if (!err && st.isDirectory()) {
      if (!pathname.endsWith('/')) { res.writeHead(301, { Location: pathname + '/' }); return res.end(); }
      file = path.join(file, 'index.html');
    }
    fs.stat(file, (err2, st2) => {
      if (err2 || !st2.isFile()) return send404(res);
      const ext = path.extname(file).toLowerCase();
      const headers = {
        'Content-Type': TYPES[ext] || 'application/octet-stream',
        'Cache-Control': ext === '.html' ? 'no-cache' : 'public, max-age=604800',
        'X-Content-Type-Options': 'nosniff',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
        'Accept-Ranges': 'bytes',
        'Last-Modified': st2.mtime.toUTCString()
      };
      const range = req.headers.range;
      if (range && /^bytes=\d*-\d*$/.test(range)) {
        let [s, e] = range.slice(6).split('-');
        let start = s === '' ? st2.size - Number(e) : Number(s);
        let end = s === '' || e === '' ? st2.size - 1 : Math.min(Number(e), st2.size - 1);
        if (isNaN(start) || start < 0 || start > end || start >= st2.size) {
          res.writeHead(416, { 'Content-Range': 'bytes */' + st2.size }); return res.end();
        }
        res.writeHead(206, { ...headers, 'Content-Range': `bytes ${start}-${end}/${st2.size}`, 'Content-Length': end - start + 1 });
        if (req.method === 'HEAD') return res.end();
        return fs.createReadStream(file, { start, end }).pipe(res);
      }
      if (COMPRESS.has(ext) && /\bgzip\b/.test(req.headers['accept-encoding'] || '')) {
        res.writeHead(200, { ...headers, 'Content-Encoding': 'gzip', Vary: 'Accept-Encoding' });
        if (req.method === 'HEAD') return res.end();
        return fs.createReadStream(file).pipe(zlib.createGzip()).pipe(res);
      }
      res.writeHead(200, { ...headers, 'Content-Length': st2.size });
      if (req.method === 'HEAD') return res.end();
      fs.createReadStream(file).pipe(res);
    });
  });
});
server.listen(PORT, '0.0.0.0', () => console.log('Portfolio running on port ' + PORT));
