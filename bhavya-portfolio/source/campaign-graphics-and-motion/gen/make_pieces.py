import json, os
BASE = '/home/claude/work/cache/hookloop-src/'
PIECES = BASE + 'pieces/'
head = lambda css, extra='': f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../fonts.css"><link rel="stylesheet" href="../{css}"><style>{extra}</style></head>'

open(BASE + 'brand-dabara.css', 'w').write(""":root{--chicory:#2E1B13;--chicory-2:#48291C;--rose:#E9708D;--rose-2:#F6C3D0;--rose-soft:#FDEBF0;--steel:#D5DBE0;--steel-2:#EEF1F4;--leaf:#1F6B47;--white:#fff;--d:'Shrikhand';--b:'Bricolage Grotesque'}
*{box-sizing:border-box;margin:0;padding:0}html,body{overflow:hidden}
body{position:relative;font-family:var(--b);-webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums}
.post{width:1080px;height:1350px}.story{width:1080px;height:1920px}.sq{width:1080px;height:1080px}
.logo{font-family:var(--d);font-size:60px;line-height:1}
.abs{position:absolute}""")

open(BASE + 'brand-barsaati.css', 'w').write(""":root{--ink:#172238;--ink-2:#2A3A5C;--rain:#7FA3C9;--mist:#E4ECF4;--umbrella:#F2B33D;--paper:#FBFAF6;--d:'Young Serif';--t:'Newsreader'}
*{box-sizing:border-box;margin:0;padding:0}html,body{overflow:hidden}
body{position:relative;font-family:var(--t);-webkit-font-smoothing:antialiased}
.post{width:1080px;height:1350px}.story{width:1080px;height:1920px}.sq{width:1080px;height:1080px}
.rain{background-image:repeating-linear-gradient(105deg,transparent 0 46px,rgba(127,163,201,.32) 46px 48px,transparent 48px 97px)}
.rain-dark{background-image:repeating-linear-gradient(105deg,transparent 0 46px,rgba(127,163,201,.18) 46px 48px,transparent 48px 97px)}
.mark{font-family:var(--d);font-size:40px;line-height:1;display:flex;align-items:center;gap:14px}
.mark i{display:block;width:34px;height:34px;border-radius:50% 50% 0 0;border:5px solid currentColor;border-bottom:0;position:relative}
.mark i::after{content:"";position:absolute;left:50%;top:26px;width:5px;height:22px;background:currentColor;margin-left:-2.5px;border-radius:0 0 6px 6px}
.abs{position:absolute}""")

open(BASE + 'brand-dabba.css', 'w').write(""":root{--tomato:#E8432E;--turmeric:#FFC93C;--leaf:#2F9E44;--ink:#161616;--sky:#8FD3F4;--white:#fff;--d:'Bagel Fat One';--b:'Mukta'}
*{box-sizing:border-box;margin:0;padding:0}html,body{overflow:hidden}
body{position:relative;width:1280px;height:720px;font-family:var(--b);-webkit-font-smoothing:antialiased}
.abs{position:absolute}
.title{font-family:var(--d);line-height:.92;color:var(--white);-webkit-text-stroke:0;text-shadow:0 8px 0 var(--ink)}
.chan{display:flex;align-items:center;gap:12px;font-family:var(--d);font-size:34px;color:var(--ink)}
.chan b{display:inline-grid;place-items:center;width:52px;height:52px;border-radius:14px;background:var(--ink);color:var(--turmeric);font-size:30px}
.badge{display:grid;place-items:center;border-radius:50%;font-family:var(--d);text-align:center;line-height:.9}""")

P = []
def piece(pid, w, h, html):
    open(PIECES + pid + '.html', 'w').write(html)
    P.append({'id': pid, 'file': pid + '.html', 'w': w, 'h': h})

ART = '<script src="../dabara-art.js" defer></script>'
POUR = '''<svg viewBox="0 0 520 420" width="100%" height="100%" aria-hidden="true"><g stroke="rgba(255,255,255,.45)" stroke-width="2" fill="none"><path d="M470 92v234"/><path d="M460 92h20M460 326h20"/></g><text x="482" y="216" fill="rgba(255,255,255,.8)" font-size="17" font-family="Bricolage Grotesque" font-weight="700" transform="rotate(90 482 216)" text-anchor="middle">about 30 cm</text><g transform="translate(330 40) rotate(-38)"><path d="M0 0h70l-8 104H8z" fill="#E4E8EC"/><path d="M0 0h70" stroke="#AEB7BF" stroke-width="7" stroke-linecap="round"/><path d="M14 14l5 80" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".55"/></g><path d="M336 70 C 300 110, 262 190, 252 300" stroke="#7A4A2C" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M336 70 C 300 110, 262 190, 252 300" stroke="#C99A6B" stroke-width="4" fill="none" stroke-linecap="round" stroke-dasharray="10 8"/><ellipse cx="250" cy="388" rx="150" ry="18" fill="#000" opacity=".25"/><ellipse cx="250" cy="318" rx="148" ry="24" fill="#9AA4AD"/><path d="M196 228h108l-12 136h-84z" fill="#E4E8EC"/><ellipse cx="250" cy="231" rx="54" ry="10" fill="#E8CFAF"/><path d="M212 246l9 104" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".55"/><path d="M102 318c0 0 60 22 148 22s148-22 148-22l-22 44c-6 12-18 20-32 20H156c-14 0-26-8-32-20z" fill="#CBD2D8"/><path d="M102 318c0 0 60 22 148 22s148-22 148-22" stroke="#AEB7BF" stroke-width="6" fill="none" stroke-linecap="round"/><g fill="#F4E3CC"><circle cx="236" cy="228" r="5"/><circle cx="252" cy="226" r="6"/><circle cx="268" cy="229" r="4.5"/></g></svg>'''

# ---------------- Dabara ----------------
piece('dabara-01-tonic-launch', 1080, 1350, head('brand-dabara.css', '''
body{background:var(--rose-2);color:var(--chicory)}
.lg{left:72px;top:70px;color:var(--chicory)}
.when{right:72px;top:78px;font-size:30px;font-weight:700;background:var(--chicory);color:var(--rose-2);padding:10px 24px;border-radius:999px}
h1{left:66px;top:200px;width:640px;font-family:var(--d);font-weight:400;font-size:150px;line-height:1.02}
.glass{right:10px;top:330px;width:620px;height:620px}
.badge{left:96px;top:760px;width:250px;height:250px;border-radius:50%;background:var(--rose);display:grid;place-items:center;text-align:center;transform:rotate(-9deg)}
.badge b{font-family:var(--d);font-weight:400;font-size:92px;line-height:.9;display:block}
.badge span{font-size:28px;font-weight:700}
.foot{left:0;right:0;bottom:0;height:250px;background:var(--chicory);color:var(--white);padding:52px 72px;display:grid;gap:14px}
.foot p{font-size:40px;font-weight:600;line-height:1.2;max-width:900px}
.foot small{font-size:30px;color:var(--rose-2);font-weight:600}
''') + f'''<body class="post"><span class="abs logo lg">Dabara</span><span class="abs when">From Friday</span>
<h1 class="abs">Kaapi Tonic is back.</h1><div class="abs glass" data-art="tonic"></div>
<div class="abs badge"><div><b>₹180</b><span>a glass</span></div></div>
<div class="abs foot"><p>Cold decoction floated on tonic and ice, with a twist of orange peel.</p><small>Order ahead for pickup: link in bio</small></div>{ART}</body></html>''')

rows = [('tonic', 'Kaapi Tonic', 'Decoction on tonic, orange peel', '₹180'), ('iced', 'Cold Kaapi', 'Shaken with milk and jaggery', '₹150'), ('sherbet', 'Nannari Sherbet', 'Sarsaparilla, lime and soda', '₹110')]
piece('dabara-02-cold-story', 1080, 1920, head('brand-dabara.css', '''
body{background:var(--chicory);color:var(--white)}
.lg{left:80px;top:250px;color:var(--rose)}
h1{left:76px;top:360px;width:900px;font-family:var(--d);font-weight:400;font-size:132px;line-height:1.02;color:var(--rose-2)}
.list{left:80px;right:80px;top:720px;display:grid;gap:34px}
.row{display:grid;grid-template-columns:220px 1fr auto;gap:36px;align-items:center}
.pic{width:220px;height:220px;border-radius:44px;background:var(--steel-2);padding:14px}
.nm{font-size:56px;font-weight:800;line-height:1.05}
.ds{font-size:32px;color:var(--rose-2);opacity:.85;margin-top:8px}
.pr{font-family:var(--d);font-size:64px;color:var(--rose)}
.cta{left:80px;right:80px;top:1540px;height:110px;border-radius:999px;background:var(--rose);color:var(--chicory);display:grid;place-items:center;font-size:40px;font-weight:800}
''') + '<body class="story"><span class="abs logo lg">Dabara</span><h1 class="abs">Three ways to drink it cold</h1><div class="abs list">' +
  ''.join(f'<div class="row"><div class="pic" data-art="{a}"></div><div><div class="nm">{n}</div><div class="ds">{d}</div></div><div class="pr">{p}</div></div>' for a, n, d, p in rows) +
  f'</div><div class="abs cta">Order ahead for pickup: link in bio</div>{ART}</body></html>')

piece('dabara-03-bun-square', 1080, 1080, head('brand-dabara.css', '''
body{background:var(--steel);color:var(--chicory)}
.bun{left:-40px;top:250px;width:640px;height:640px}
h1{left:560px;top:150px;width:460px;font-family:var(--d);font-weight:400;font-size:104px;line-height:1.02}
.sub{left:564px;top:700px;width:440px;font-size:36px;font-weight:600;line-height:1.25}
.sub b{display:block;font-family:var(--d);font-weight:400;font-size:64px;color:var(--rose);margin-top:14px;-webkit-text-stroke:0}
.lg{left:72px;top:70px;color:var(--chicory)}
.stamp{right:72px;top:70px;font-size:28px;font-weight:800;border:4px solid var(--chicory);border-radius:12px;padding:6px 16px;transform:rotate(4deg)}
''') + f'<body class="sq"><span class="abs logo lg">Dabara</span><span class="abs stamp">Sells out by noon</span><div class="abs bun" data-art="bun"></div><h1 class="abs">Cardamom buns, warm at 7.</h1><p class="abs sub">Swirled with cardamom sugar, baked every morning at 6:30.<b>₹140</b></p>{ART}</body></html>')

piece('dabara-04-pour-reel-cover', 1080, 1920, head('brand-dabara.css', '''
body{background:var(--chicory);color:var(--white)}
.lg{left:80px;top:250px;color:var(--rose)}
.pour{left:40px;top:560px;width:1000px;height:808px}
h1{left:80px;top:360px;width:920px;font-family:var(--d);font-weight:400;font-size:120px;line-height:1.02;color:var(--rose-2)}
.sub{left:80px;top:1400px;width:900px;font-size:44px;font-weight:600;line-height:1.25}
.time{left:80px;top:1530px;font-size:34px;font-weight:800;background:var(--leaf);padding:10px 22px;border-radius:12px}
''') + f'<body class="story"><span class="abs logo lg">Dabara</span><h1 class="abs">Why we pour from 30 cm</h1><div class="abs pour">{POUR}</div><p class="abs sub">The froth, the cooling, the show. Filter kaapi explained in 20 seconds.</p><span class="abs time">0:20</span></body></html>')

menu = [('tonic', 'Kaapi Tonic', '180'), ('iced', 'Cold Kaapi', '150'), ('latte', 'Iced Jaggery Latte', '210'), ('rosemilk', 'Rose Milk', '130'), ('sherbet', 'Nannari Sherbet', '110')]
piece('dabara-05-cold-menu', 1080, 1350, head('brand-dabara.css', '''
body{background:var(--rose-soft);color:var(--chicory)}
.lg{left:72px;top:70px;color:var(--rose)}
h1{left:72px;top:170px;font-family:var(--d);font-weight:400;font-size:150px;line-height:1}
.sub{left:76px;top:356px;font-size:34px;font-weight:600}
.menu{left:72px;right:72px;top:450px;display:grid;gap:22px}
.it{display:grid;grid-template-columns:120px auto 1fr auto;gap:22px;align-items:center}
.ic{width:120px;height:120px;background:var(--white);border-radius:28px;padding:6px}
.nm{font-size:48px;font-weight:800}
.ld{border-bottom:5px dotted rgba(46,27,19,.35);height:0;align-self:center;margin-top:10px}
.pr{font-family:var(--d);font-size:58px}
.new{font-size:24px;font-weight:800;background:var(--leaf);color:var(--white);padding:4px 12px;border-radius:8px;margin-left:12px;vertical-align:8px}
.foot{left:72px;right:72px;bottom:64px;border-top:4px solid var(--chicory);padding-top:24px;font-size:32px;font-weight:600;display:flex;justify-content:space-between}
''') + '<body class="post"><span class="abs logo lg">Dabara</span><h1 class="abs">Cold menu</h1><p class="abs sub">Summer, all day, every day.</p><div class="abs menu">' +
  ''.join(f'<div class="it"><div class="ic" data-art="{a}"></div><div class="nm">{n}{"<span class=new>New</span>" if a=="latte" else ""}</div><div class="ld"></div><div class="pr">₹{p}</div></div>' for a, n, p in menu) +
  f'</div><div class="abs foot"><span>Oat milk on any drink, +₹40</span><span>Prices include GST</span></div>{ART}</body></html>')

# ---------------- Barsaati Books ----------------
books = [('Puddle Maps', 'Ira Menon', '#F2B33D', '#172238', 22), ('Salt and Monsoon', 'D. Fernandes', '#7FA3C9', '#172238', -3), ('Three Umbrellas', 'Kavya Rao', '#E4ECF4', '#172238', 4), ('The Tin Roof Year', 'Arjun Lal', '#C9573A', '#FBFAF6', -2)]
piece('barsaati-01-club', 1080, 1350, head('brand-barsaati.css', '''
body{background-color:var(--mist);color:var(--ink)}
.mk{left:72px;top:70px;color:var(--ink)}
h1{left:68px;top:180px;width:900px;font-family:var(--d);font-weight:400;font-size:132px;line-height:.98}
.sub{left:72px;top:610px;width:860px;font-style:italic;font-size:46px;line-height:1.2;color:var(--ink-2)}
.stack{left:72px;right:72px;top:780px;display:grid;gap:14px}
.sp{height:92px;border-radius:6px;display:flex;align-items:center;justify-content:space-between;padding:0 30px;font-family:var(--d);font-size:38px;box-shadow:inset 0 -6px 0 rgba(0,0,0,.08)}
.sp small{font-family:var(--t);font-size:26px;font-style:italic;opacity:.85}
.foot{left:72px;right:72px;bottom:62px;display:flex;justify-content:space-between;font-size:32px;font-weight:600;border-top:3px solid var(--ink);padding-top:22px}
''') + '<body class="post rain"><div class="abs mk mark"><i></i>Barsaati Books</div><h1 class="abs">Monsoon Reading Club</h1><p class="abs sub">Four books. Four rainy Sundays. One very long chai.</p><div class="abs stack">' +
  ''.join(f'<div class="sp" style="background:{bg};color:{fg};margin-left:{abs(o)*6}px;transform:rotate({o/10}deg)"><span>{t}</span><small>{a}</small></div>' for t, a, bg, fg, o in books) +
  '</div><div class="abs foot"><span>Starts Sunday 5 July, 5 pm</span><span>Free to join</span></div></body></html>')

piece('barsaati-02-july-book', 1080, 1350, head('brand-barsaati.css', '''
body{background-color:var(--ink);color:var(--paper)}
.mk{left:72px;top:70px;color:var(--paper)}
.no{right:72px;top:74px;font-size:32px;font-style:italic;color:var(--rain)}
.lab{left:72px;top:190px;font-size:40px;font-style:italic;color:var(--umbrella)}
.cover{left:72px;top:270px;width:520px;height:760px;background:var(--umbrella);color:var(--ink);padding:48px 44px;display:flex;flex-direction:column;box-shadow:24px 24px 0 rgba(0,0,0,.25)}
.cover h2{font-family:var(--d);font-weight:400;font-size:104px;line-height:.95}
.cover .au{margin-top:auto;font-size:34px;font-style:italic}
.cover svg{width:100%;height:240px;margin-top:40px}
.notes{left:650px;top:290px;width:360px;display:grid;gap:30px}
.notes div b{display:block;font-family:var(--d);font-weight:400;font-size:58px;line-height:1;color:var(--umbrella)}
.notes div span{font-size:30px;line-height:1.25;color:var(--mist)}
.foot{left:72px;right:72px;bottom:64px;font-size:40px;line-height:1.25;font-style:italic;color:var(--mist)}
''') + '''<body class="post rain-dark"><div class="abs mk mark"><i></i>Barsaati Books</div><span class="abs no">1 of 4</span><p class="abs lab">July's book</p>
<div class="abs cover"><h2>Puddle Maps</h2><svg viewBox="0 0 400 200" aria-hidden="true"><g fill="none" stroke="#172238" stroke-width="5" stroke-linecap="round"><ellipse cx="120" cy="120" rx="90" ry="26"/><ellipse cx="290" cy="80" rx="70" ry="20"/><ellipse cx="250" cy="160" rx="50" ry="14"/><path d="M40 40l20 30M140 20l14 26M330 140l18 28" stroke-width="4"/></g></svg><span class="au">Ira Menon</span></div>
<div class="abs notes"><div><b>212</b><span>pages, read over four weeks</span></div><div><b>10%</b><span>off club books at our counter</span></div><div><b>5 July</b><span>first meeting, 5 pm</span></div></div>
<p class="abs foot">A city mapped by where the water collects. Swipe for the reading plan.</p></body></html>'''
)

piece('barsaati-03-sunday-story', 1080, 1920, head('brand-barsaati.css', '''
body{background:var(--umbrella);color:var(--ink)}
.mk{left:80px;top:250px;color:var(--ink)}
.big{left:74px;top:380px;width:940px;font-family:var(--d);font-weight:400;font-size:190px;line-height:.92}
.copy{left:80px;top:840px;width:900px;font-size:54px;line-height:1.2}
.copy em{font-style:italic}
.card{left:80px;right:80px;top:1170px;background:var(--ink);color:var(--paper);border-radius:28px;padding:44px 48px;display:grid;gap:12px}
.card b{font-family:var(--d);font-weight:400;font-size:62px;color:var(--umbrella)}
.card span{font-size:36px;line-height:1.25;color:var(--mist)}
.drops{right:80px;top:250px;width:220px;height:120px}
''') + '''<body class="story"><div class="abs mk mark"><i></i>Barsaati Books</div>
<svg class="abs drops" viewBox="0 0 220 120" aria-hidden="true"><g fill="#172238"><path d="M30 10c10 20 18 32 18 44a18 18 0 0 1-36 0c0-12 8-24 18-44z"/><path d="M110 40c8 16 14 26 14 35a14 14 0 0 1-28 0c0-9 6-19 14-35z" opacity=".6"/><path d="M180 0c10 20 18 32 18 44a18 18 0 0 1-36 0c0-12 8-24 18-44z" opacity=".35"/></g></svg>
<p class="abs big">Sunday, 5 pm</p>
<p class="abs copy">Monsoon Reading Club meets in the back room. Bring an umbrella, not a chair. <em>We have chairs.</em></p>
<div class="abs card"><b>Save a seat</b><span>Reply "club" to this story and we'll keep one for you. Twelve seats, first come.</span></div></body></html>'''
)

piece('barsaati-04-quote', 1080, 1080, head('brand-barsaati.css', '''
body{background-color:var(--ink);color:var(--paper)}
.mk{left:72px;top:70px;color:var(--rain)}
.q{left:72px;right:72px;top:210px;font-style:italic;font-size:76px;line-height:1.14;font-weight:400}
.q::before{content:"\\201C";display:block;font-family:var(--d);font-style:normal;font-size:200px;line-height:.6;color:var(--umbrella);margin-bottom:10px}
.src{left:72px;bottom:72px;font-size:32px;color:var(--rain)}
.src b{font-family:var(--d);font-weight:400;color:var(--umbrella);font-size:36px}
''') + '<body class="sq rain-dark"><div class="abs mk mark"><i></i>Barsaati Books</div><p class="abs q">In July the whole city walks a little slower, and so do its sentences.</p><p class="abs src"><b>Puddle Maps</b>, chapter 2. Monsoon Reading Club, week 1.</p></body></html>')

# ---------------- Dabba Diaries (YouTube thumbnails) ----------------
bowl = lambda x, y, top: f'<g transform="translate({x} {y})"><ellipse cx="0" cy="58" rx="120" ry="16" fill="#161616" opacity=".18"/><path d="M-120 0h240c0 50-50 64-120 64S-120 50-120 0z" fill="#fff"/><path d="M-120 0h240c0 50-50 64-120 64S-120 50-120 0z" fill="none" stroke="#161616" stroke-width="7"/><ellipse cx="0" cy="0" rx="120" ry="30" fill="{top}" stroke="#161616" stroke-width="7"/>'
def flakes(seed, cols):
    import random
    r = random.Random(seed); out = ''
    for i in range(26):
        x = r.uniform(-90, 90); y = r.uniform(-16, 12); c = r.choice(cols)
        out += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r.uniform(5,9):.0f}" ry="{r.uniform(3,5):.0f}" fill="{c}"/>'
    return out + '</g>'
piece('dabba-01-poha', 1280, 720, head('brand-dabba.css', '''
body{background:var(--turmeric)}
.t{left:56px;top:70px;font-size:150px}
.t span{display:block;color:var(--tomato)}
.bowls{left:560px;top:250px;width:700px;height:420px}
.badge{left:64px;top:470px;width:170px;height:170px;background:var(--tomato);color:var(--white);font-size:56px;transform:rotate(-8deg);border:7px solid var(--ink)}
.chan{left:270px;top:560px}
''') + f'''<body><h1 class="abs title t">Poha,<span>3 ways</span></h1>
<svg class="abs bowls" viewBox="0 0 700 420" aria-hidden="true">{bowl(150,300,'#F7D774')}{flakes(1,['#F2C14E','#E9B53C','#5E9B4A','#C8324B'])}{bowl(420,210,'#F4E1A6')}{flakes(2,['#EAD48E','#D9534F','#2F9E44','#8B5A2B'])}{bowl(560,340,'#F5C04A')}{flakes(3,['#F0B429','#E8432E','#2F9E44','#FFF4CC'])}</svg>
<div class="abs badge">15<br>MIN</div><div class="abs chan"><b>D</b>Dabba Diaries</div></body></html>''')

dabba = '''<svg viewBox="0 0 360 460" aria-hidden="true"><g stroke="#161616" stroke-width="8" stroke-linejoin="round">
<rect x="40" y="320" width="280" height="110" rx="26" fill="#D7DDE2"/><rect x="40" y="200" width="280" height="110" rx="26" fill="#E9EDF0"/><rect x="40" y="80" width="280" height="110" rx="26" fill="#D7DDE2"/>
<path d="M60 80c0-40 240-40 240 0" fill="#C2CAD0"/><path d="M180 26v36" fill="none"/><rect x="150" y="10" width="60" height="22" rx="11" fill="#FFC93C"/>
<path d="M20 120v290M340 120v290" fill="none" stroke-width="10"/></g>
<g fill="#fff" opacity=".7"><rect x="64" y="96" width="14" height="78" rx="7"/><rect x="64" y="216" width="14" height="78" rx="7"/><rect x="64" y="336" width="14" height="78" rx="7"/></g></svg>'''
piece('dabba-02-tiffins', 1280, 720, head('brand-dabba.css', '''
body{background:var(--leaf)}
.t{left:60px;top:76px;font-size:132px;color:var(--turmeric)}
.t span{display:block;color:var(--white)}
.stack{left:830px;top:120px;width:360px;height:460px;transform:rotate(6deg)}
.badge{left:620px;top:84px;width:150px;height:150px;background:var(--turmeric);color:var(--ink);font-size:42px;border:7px solid var(--ink);transform:rotate(10deg)}
.week{left:64px;top:470px;display:flex;gap:10px}
.week span{width:84px;height:84px;border-radius:18px;background:rgba(255,255,255,.18);border:5px solid var(--ink);display:grid;place-items:center;font-family:var(--d);font-size:34px;color:var(--white)}
.chan{left:64px;top:600px;color:var(--white)}
.chan b{background:var(--turmeric);color:var(--ink)}
''') + f'<body><h1 class="abs title t">5 tiffins<span>₹100 each</span></h1><div class="abs badge">WEEK<br>1</div><div class="abs stack">{dabba}</div><div class="abs week"><span>M</span><span>T</span><span>W</span><span>T</span><span>F</span></div><div class="abs chan"><b>D</b>Dabba Diaries</div></body></html>')

cooker = '''<svg viewBox="0 0 520 440" aria-hidden="true"><g stroke="#161616" stroke-width="9" stroke-linejoin="round" stroke-linecap="round">
<ellipse cx="230" cy="402" rx="200" ry="22" fill="#161616" opacity=".15" stroke="none"/>
<path d="M60 170h340v170c0 40-30 64-70 64H130c-40 0-70-24-70-64z" fill="#D7DDE2"/>
<path d="M40 170h380" fill="none"/><path d="M90 170c0-60 280-60 280 0" fill="#C2CAD0"/>
<rect x="210" y="90" width="40" height="34" rx="8" fill="#161616"/><path d="M230 90V64" fill="none"/>
<path d="M400 190h96" fill="none" stroke-width="20"/><path d="M400 190h96" fill="none" stroke="#2F9E44" stroke-width="10"/>
<path d="M210 40c-12-16 12-24 0-40M250 40c-12-16 12-24 0-40" fill="none" stroke="#fff" stroke-width="7"/></g>
<g transform="translate(130 250)"><path d="M0 0h200v70c0 10-8 18-18 18H18C8 88 0 80 0 70z" fill="#B7742E" stroke="#161616" stroke-width="8"/><path d="M10 10h180" stroke="#8A5634" stroke-width="10" stroke-linecap="round"/></g></svg>'''
piece('dabba-03-banana-bread', 1280, 720, head('brand-dabba.css', '''
body{background:var(--sky)}
.t{left:60px;top:70px;font-size:128px;color:var(--white)}
.t span{display:block;color:var(--turmeric)}
.cooker{left:700px;top:180px;width:520px;height:440px}
.tag{left:64px;top:470px;font-size:44px;font-weight:800;background:var(--ink);color:var(--white);padding:10px 26px;border-radius:16px;transform:rotate(-3deg)}
.badge{left:930px;top:40px;width:150px;height:150px;background:var(--tomato);color:var(--white);font-size:44px;border:7px solid var(--ink);transform:rotate(12deg)}
.chan{left:64px;top:600px}
''') + f'<body><h1 class="abs title t">No-oven<span>banana bread</span></h1><div class="abs cooker">{cooker}</div><span class="abs tag">Pressure cooker method</span><div class="abs badge">EASY</div><div class="abs chan"><b>D</b>Dabba Diaries</div></body></html>')

# merge with the existing mettle list
existing = [p for p in json.load(open(BASE + 'pieces.json')) if p['id'].startswith('mettle')]
json.dump(existing + P, open(BASE + 'pieces.json', 'w'), indent=1)
print(len(existing) + len(P), 'pieces')
