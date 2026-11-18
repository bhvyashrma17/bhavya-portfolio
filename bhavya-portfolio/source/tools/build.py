"""Build sites: inline subsetted fonts, copy assets, and write a local preview that mimics the artifact skeleton."""
import os, re, shutil, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from fonts import site_css

SRC = '/home/claude/work/src'
DIST = '/home/claude/work/dist'
SKELETON_HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
  '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
  '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
  'body{margin:0;font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;background:#fafaf9}img{max-width:100%}'
  '[hidden]{display:none!important}</style></head><body>')
SKELETON_TAIL = '</body></html>'
BLOCKED_TERMS = []  # add regexes here to stop a build if a word must never appear

def build(site):
    sdir, ddir = os.path.join(SRC, site), os.path.join(DIST, site)
    os.makedirs(ddir, exist_ok=True)
    html = open(os.path.join(sdir, 'index.html'), encoding='utf-8').read()
    for pat in BLOCKED_TERMS:
        if re.search(pat, html, re.I):
            raise SystemExit(f'Blocked term {pat} found in {site}')
    html = html.replace('/*@@FONTS@@*/', site_css(site))
    cfg = json.load(open(os.path.join(os.path.dirname(__file__), 'config.json')))
    for k, v in cfg.items():
        if v:
            html = html.replace('{{' + k + '}}', v)
    open(os.path.join(ddir, 'index.html'), 'w', encoding='utf-8').write(html)
    open(os.path.join(ddir, '_preview.html'), 'w', encoding='utf-8').write(SKELETON_HEAD + html + SKELETON_TAIL)
    # copy asset folders/files (everything except index.html)
    for name in os.listdir(sdir):
        if name == 'index.html' or name.startswith('_'):
            continue
        sp, dp = os.path.join(sdir, name), os.path.join(ddir, name)
        if os.path.isdir(sp):
            shutil.copytree(sp, dp, dirs_exist_ok=True)
        else:
            shutil.copy2(sp, dp)
    print(f'built {site}: {round(len(html)/1024)} KB')

if __name__ == '__main__':
    for s in (sys.argv[1:] or sorted(os.listdir(SRC))):
        build(s)
