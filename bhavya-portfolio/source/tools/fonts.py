"""Subset open-source (OFL) fonts from @fontsource packages and emit @font-face CSS with data: URIs.
The OFL permits embedding; name tables (copyright/licence) are retained in every subset."""
import base64, io, os, hashlib, json
from fontTools import subset
from fontTools.ttLib import TTFont

BASE = '/home/claude/work/fontpkgs/node_modules'
CACHE = '/home/claude/work/cache/fonts'
os.makedirs(CACHE, exist_ok=True)

TEXT_UNICODES = list(range(0x20, 0x7F)) + list(range(0xA0, 0x100)) + [
    0x2013, 0x2014, 0x2018, 0x2019, 0x201A, 0x201C, 0x201D, 0x2022, 0x2026, 0x2032, 0x2033,
    0x2212, 0x2191, 0x2193, 0x2190, 0x2192, 0x2197, 0x2116, 0x2122, 0x20AC]

def _subset(path, unicodes):
    key = hashlib.md5((path + json.dumps(unicodes)).encode()).hexdigest()
    out = os.path.join(CACHE, key + '.woff2')
    if os.path.exists(out):
        return open(out, 'rb').read()
    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['*']
    opts.name_IDs = ['*']          # keep copyright + licence strings
    opts.name_legacy = True
    opts.name_languages = ['*']
    opts.hinting = False
    opts.desubroutinize = True
    opts.notdef_outline = True
    font = TTFont(path)
    cmap = font.getBestCmap()
    have = [u for u in unicodes if u in cmap]
    if not have:
        return None
    s = subset.Subsetter(opts)
    s.populate(unicodes=have)
    s.subset(font)
    buf = io.BytesIO()
    font.flavor = 'woff2'
    font.save(buf)
    data = buf.getvalue()
    open(out, 'wb').write(data)
    return data

def face(family, pkg, latin_file, ext_file=None, weight='400', style='normal', stretch=None):
    """Return @font-face CSS (latin text subset + optional ext subset containing only the rupee sign)."""
    css = []
    lat = _subset(f'{BASE}/{pkg}/files/{latin_file}', TEXT_UNICODES)
    rng = 'U+0020-007E, U+00A0-00FF, U+2013-2014, U+2018-201D, U+2022, U+2026, U+2032-2033, U+2212, U+2190-2197, U+2116, U+2122, U+20AC'
    def block(data, urange):
        b64 = base64.b64encode(data).decode()
        extra = f'font-stretch:{stretch};' if stretch else ''
        return (f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};{extra}font-display:swap;"
                f"src:url(data:font/woff2;base64,{b64}) format('woff2');unicode-range:{urange}}}")
    css.append(block(lat, rng))
    if ext_file:
        ext = _subset(f'{BASE}/{pkg}/files/{ext_file}', [0x20B9])
        if ext:
            css.append(block(ext, 'U+20B9'))
    return '\n'.join(css)

SITES = {
  'portfolio': lambda: '\n'.join([
     face('Mona Sans', '@fontsource-variable/mona-sans', 'mona-sans-latin-standard-normal.woff2', 'mona-sans-latin-ext-standard-normal.woff2', '200 900', 'normal', '75% 125%'),
  ]),
  'mettle': lambda: '\n'.join([
     face('Big Shoulders Display', '@fontsource-variable/big-shoulders-display', 'big-shoulders-display-latin-wght-normal.woff2', 'big-shoulders-display-latin-ext-wght-normal.woff2', '100 900'),
     face('Instrument Sans', '@fontsource-variable/instrument-sans', 'instrument-sans-latin-standard-normal.woff2', None, '400 700', 'normal', '75% 100%'),
     face('IBM Plex Mono', '@fontsource/ibm-plex-mono', 'ibm-plex-mono-latin-400-normal.woff2', 'ibm-plex-mono-latin-ext-400-normal.woff2', '400'),
  ]),
  'dabara': lambda: '\n'.join([
     face('Shrikhand', '@fontsource/shrikhand', 'shrikhand-latin-400-normal.woff2', 'shrikhand-latin-ext-400-normal.woff2', '400'),
     face('Bricolage Grotesque', '@fontsource-variable/bricolage-grotesque', 'bricolage-grotesque-latin-wght-normal.woff2', 'bricolage-grotesque-latin-ext-wght-normal.woff2', '200 800'),
  ]),
  'fringe': lambda: '\n'.join([
     face('Gloock', '@fontsource/gloock', 'gloock-latin-400-normal.woff2', 'gloock-latin-ext-400-normal.woff2', '400'),
     face('Albert Sans', '@fontsource-variable/albert-sans', 'albert-sans-latin-wght-normal.woff2', 'albert-sans-latin-ext-wght-normal.woff2', '100 900'),
  ]),
  'hookloop': lambda: '\n'.join([
     face('Anybody', '@fontsource-variable/anybody', 'anybody-latin-standard-normal.woff2', 'anybody-latin-ext-standard-normal.woff2', '100 900', 'normal', '50% 150%'),
     face('Hanken Grotesk', '@fontsource-variable/hanken-grotesk', 'hanken-grotesk-latin-wght-normal.woff2', None, '100 900'),
     face('Azeret Mono', '@fontsource-variable/azeret-mono', 'azeret-mono-latin-wght-normal.woff2', None, '100 900'),
  ]),
}

def site_css(name):
    return SITES[name]()

if __name__ == '__main__':
    for n in SITES:
        c = site_css(n)
        print(n, round(len(c)/1024), 'KB of CSS')
