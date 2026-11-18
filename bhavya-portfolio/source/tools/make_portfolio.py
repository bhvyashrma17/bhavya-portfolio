import json, html
E = html.escape
URL = {
  'mettle': 'https://claude.ai/artifact/3oue5CCFioWZMHKvE2PW9s',
  'dabara': 'https://claude.ai/artifact/H35uoNJntNNtEisLWQa5ze',
  'fringe': 'https://claude.ai/artifact/ERUT3vy2m5NwzQ7sfqzAmq',
  'hookloop': 'https://claude.ai/artifact/MwSKVmupab5pkS8MBVythX',
  'cleartrade': 'https://cleartrade.in',
}
WA = 'https://wa.me/917500124113?text=Hi%20Bhavya%2C%20I%20saw%20your%20portfolio%20and%20would%20like%20to%20talk%20about%20a%20project.'
CASES = [
 dict(id='cleartrade', name='ClearTrade', tag='Real project, in progress', kind='Product, in progress',
  index='Export platform for Indian businesses. Live and in development.',
  sum='An export operating system for Indian businesses. Exporters find markets and buyers for free, and when they are ready to ship, a ClearTrade agent handles the paperwork, customs, freight and payment with them.',
  problem='Exporting means juggling buyer research, documents, customs, freight and payment across email, spreadsheets and agents. Smaller exporters often can\'t see which countries already buy their product, or what a deal involves before they start.',
  built=['Market search by HS code, built on customs-recorded trade history, free and without an account','Buyer discovery and a saved lead list for free accounts','An eight-stage deal pipeline, from readiness to payment, that an agent works through with the exporter','A paid plan with a one-time commitment fee for agent-led deals','Sample results for markets, buyers and shipment documents, clearly marked as samples'],
  role='Design and development. ClearTrade is my own product and is live at cleartrade.in.',
  stack='Live web product with free search, accounts and a paid plan.',
  cta='Visit cleartrade.in', theme='--bg:#0E0F12;--fg:#EDEDF0;--mute:#A3A3AD;--acc:#8B7CF6;--rule:rgba(255,255,255,.14);--frame:#000;--btn-fg:#0E0F12',
  caps=('Home page, desktop', 'Home page, phone', 'Market finder, desktop', 'Market finder, phone'),
  note='Screenshots taken from the live site on 8 October 2026. The deal, scores and buyers shown on the site are its own labelled examples, not results.',
  dw=800, dh=500, mw=750, mh=1624),
 dict(id='mettle', name='Mettle Strength Club', tag='Independent project, concept demo', kind='Concept demo',
  index='Gym website with a programme browser and a membership price builder.',
  sum='A website for a fictional strength club, built around the two things gym visitors look for: what they would do there, and what it costs.',
  problem='Many gym sites hide the timetable in a PDF and the prices behind "contact us", so visitors leave before they ask. This concept puts programmes, class times and an honest price calculator on the first visit.',
  built=['Programme browser with search and filters for goal, experience and format','Programme sheets with who it is for, a typical week, a sample session and class times','Weekly timetable with day tabs on phones and per-programme filtering','Membership builder that prices coaching, days, off-peak, commitment and extras as you choose, including GST','Trial and membership request forms with validation, clearly marked as demos that send nothing','A working rest timer in the opening section, because it is a gym'],
  role='Concept, design, copy and front-end development.',
  stack='HTML, CSS and vanilla JavaScript, no framework. Responsive, keyboard accessible and respects reduced motion.',
  cta='View live project', theme='--bg:#0F2B24;--fg:#ECEDE8;--mute:#A3B5AA;--acc:#C9A45C;--rule:rgba(236,237,232,.16);--frame:#08140F;--btn-fg:#0F2B24',
  caps=('Opening section with the rest timer', 'Phone view', 'Membership builder with a live price', 'Programme sheet on a phone'),
  dw=1440, dh=900, mw=780, mh=1688),
 dict(id='fringe', name='Fringe Hair Studio', tag='Independent project, concept demo', kind='Concept demo',
  index='Salon booking flow with live availability and real salon rules.',
  sum='An appointment-booking flow for a fictional hair, colour and brow studio, from choosing services to a confirmation.',
  problem='Booking a salon by phone or DM means back-and-forth about free times, prices that change by stylist, and colour clients who forget the patch test.',
  built=['Service picker for up to three services, with durations and running totals','Stylist choice with level-based pricing, or "any available"','Calendar and start times worked out from opening hours, each stylist\'s day off and existing appointments','The 48-hour patch-test rule for colour and lash tints, explained wherever it blocks a date','An appointment-book view that draws your slot among the day\'s bookings','Review, a demo confirmation with copyable details, and "My bookings" to change the time or cancel'],
  role='Concept, interaction design, booking logic and front-end development.',
  stack='HTML, CSS and vanilla JavaScript. Availability is generated per stylist and day, and demo bookings stay in the browser.',
  cta='View live project', theme='--bg:#DCE9E1;--fg:#1B2320;--mute:#4A5751;--acc:#6E1D2D;--rule:rgba(27,35,32,.16);--frame:#1B2320;--btn-fg:#FFFFFF',
  caps=('Choosing services, desktop', 'Phone view', 'Date, time and the appointment book', 'Demo confirmation on a phone'),
  dw=1440, dh=900, mw=780, mh=1688),
 dict(id='dabara', name='Dabara Coffee House', tag='Independent project, concept demo', kind='Concept demo',
  index='Café menu with search, dietary filters and an order-ahead basket.',
  sum='A menu and pickup-ordering website for a fictional South Indian coffee bar.',
  problem='Café menus online are often a photo or a PDF: hard to read on a phone, impossible to filter, and no way to order ahead.',
  built=['A 26-item menu with search, category chips and sorting','Dietary filters for no egg, vegan, gluten-free and nut-free, with veg and egg marks','Item options that change the price, such as oat milk','A basket drawer with quantities, pickup times that follow opening hours, and GST','A demo order confirmation that says plainly nothing was sent or paid','Illustrations drawn for every item, and a basket that is kept between visits'],
  role='Concept, illustration, design and front-end development.',
  stack='HTML, CSS and vanilla JavaScript, with hand-drawn SVG illustrations.',
  cta='View live project', theme='--bg:#2E1B13;--fg:#FFFFFF;--mute:#D9C8BF;--acc:#E9708D;--rule:rgba(255,255,255,.16);--frame:#140B07;--btn-fg:#2E1B13',
  caps=('Opening section, desktop', 'Menu search on a phone', 'Basket and pickup details', 'Demo order confirmation'),
  dw=1440, dh=900, mw=780, mh=1688),
 dict(id='hookloop', name='Hookloop Social Studio', tag='Independent project, concept demo', kind='Concept demo',
  index='Social campaigns and motion pieces for four fictional brands.',
  sum='A social design and motion showcase for a fictional content studio, with four campaigns for fictional brands.',
  problem='Social design is judged at phone size and in motion, so flat mockups undersell it. This showcase presents finished pieces at their real sizes, and motion that plays.',
  built=['20 original graphics: feed posts, carousels, stories, reel covers, squares and YouTube thumbnails','Campaigns for Mettle and Dabara (the demos above), a bookshop and a cooking channel','A gallery with brand and format filters, a lightbox with keyboard and swipe, and a safe-zone overlay','Three motion pieces rendered frame by frame at 30 fps, with custom players and timecode'],
  role='Art direction, graphic design, motion design and front-end development.',
  stack='Graphics built in HTML, CSS and SVG and rendered at exact pixel sizes; motion encoded as H.264 video. No stock images.',
  cta='View live project', theme='--bg:#131415;--fg:#ECEDE9;--mute:#A6AAA4;--acc:#EF4126;--rule:rgba(255,255,255,.14);--frame:#000;--btn-fg:#131415',
  caps=('Opening section with the reel playing', 'Phone view', 'Lightbox with safe zones shown', 'Gallery filtered to one brand'),
  dw=1440, dh=900, mw=780, mh=1688),
]
def ul(items): return '<ul class="built">' + ''.join(f'<li>{E(i)}</li>' for i in items) + '</ul>'
def case(c):
    i = c['id']
    note = f'<p class="note">{E(c["note"])}</p>' if c.get('note') else ''
    return f'''
<article class="case" id="{i}" style="{c['theme']}" aria-labelledby="{i}-h">
  <div class="wrap">
    <header class="case-head">
      <div>
        <p class="tag">{E(c['tag'])}</p>
        <h2 id="{i}-h">{E(c['name'])}</h2>
      </div>
      <div class="case-intro">
        <p class="sum">{E(c['sum'])}</p>
        <p class="case-cta"><a class="btn btn-acc" href="{URL[i]}" target="_blank" rel="noopener">{E(c['cta'])}<span class="sr"> (opens in a new tab)</span></a></p>
      </div>
    </header>
    <div class="shots">
      <figure class="desk"><img src="shots/{i}-desk.webp" width="{c['dw']}" height="{c['dh']}" alt="{E(c['name'])}: {E(c['caps'][0].lower())}" loading="lazy"><figcaption>{E(c['caps'][0])}</figcaption></figure>
      <figure class="mob"><img src="shots/{i}-mob.webp" width="{c['mw']}" height="{c['mh']}" alt="{E(c['name'])}: {E(c['caps'][1].lower())}" loading="lazy"><figcaption>{E(c['caps'][1])}</figcaption></figure>
    </div>
    <div class="facts">
      <section><h3>The problem</h3><p>{E(c['problem'])}</p></section>
      <section><h3>{'What is live' if i == 'cleartrade' else 'What I built'}</h3>{ul(c['built'])}</section>
      <section><h3>My role</h3><p>{E(c['role'])}</p><h3>Built with</h3><p>{E(c['stack'])}</p></section>
    </div>
    <div class="shots alt">
      <figure class="mob"><img src="shots/{i}-mob-2.webp" width="{c['mw']}" height="{c['mh']}" alt="{E(c['name'])}: {E(c['caps'][3].lower())}" loading="lazy"><figcaption>{E(c['caps'][3])}</figcaption></figure>
      <figure class="desk"><img src="shots/{i}-desk-2.webp" width="{c['dw']}" height="{c['dh']}" alt="{E(c['name'])}: {E(c['caps'][2].lower())}" loading="lazy"><figcaption>{E(c['caps'][2])}</figcaption></figure>
    </div>
    {note}
  </div>
</article>'''

index_rows = ''.join(f'''<li><a href="#{c['id']}"><img src="shots/{c['id']}-thumb.webp" width="640" height="400" alt="" loading="lazy"><span class="nm">{E(c['name'])}</span><span class="ds">{E(c['index'])}</span><span class="kd{' real' if c['id']=='cleartrade' else ''}">{E(c['kind'])}</span></a></li>''' for c in CASES)

SERVICES = [
 ('Website design', 'Sites that explain what you do and what it costs, designed for phones first.', ['Page structure and copy edits', 'Visual design in your brand', 'Layouts checked on real phone sizes'], [('mettle', 'Mettle'), ('dabara', 'Dabara')]),
 ('Full-stack development', 'Booking, ordering, accounts and dashboards that load fast and work for everyone.', ['Front end and back end', 'Forms, bookings and connections to the tools you already use', 'Launch and handover'], [('cleartrade', 'ClearTrade'), ('fringe', 'Fringe')]),
 ('Social-media design', 'Posts, carousels, stories and thumbnails in your brand, at the right size for each platform.', ['A template set you can reuse', 'Campaign graphics for launches and offers', 'Files ready to post'], [('hookloop', 'Hookloop gallery')]),
 ('Video and content editing', 'Short reels and motion graphics that still make sense with the sound off.', ['Editing, captions and covers', 'Animated type and product moments', 'Intros for channels'], [('hookloop', 'Hookloop motion')]),
]
services = ''.join(f'''<li><h3>{E(t)}</h3><p>{E(d)}</p><ul>{''.join(f'<li>{E(x)}</li>' for x in inc)}</ul><p class="proof">See it in {' and '.join(f'<a href="#{a}">{E(n)}</a>' for a, n in see)}</p></li>''' for t, d, inc, see in SERVICES)

page = f'''<title>Bhavya Sharma Studio</title>
<meta name="description" content="Bhavya Sharma designs and builds websites, web apps and social content for small businesses. Selected work: ClearTrade and four working concept demos.">
<style>
/*@@FONTS@@*/
/* Layout: a quiet paper index with the name set large, then each project as a full-bleed slab in its own colours, so the work carries the page */
:root{{
  --paper:#F3F3EF; --ink:#111111; --ink-2:#5B5B57; --line:#D6D6CF; --white:#FFFFFF;
  --sans:'Mona Sans','Helvetica Neue',Arial,sans-serif;
  color-scheme:light;
}}
*,*::before,*::after{{box-sizing:border-box}}
html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}*,*::before,*::after{{animation:none!important;transition-duration:0s!important}}}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:17px;line-height:1.55;font-variation-settings:"wdth" 100}}
a{{color:inherit}}
button{{font:inherit;color:inherit}}
:focus-visible{{outline:2px solid currentColor;outline-offset:3px}}
h1,h2,h3{{margin:0;text-wrap:balance}}
p{{margin:0}}
ul{{margin:0;padding:0}}
.wrap{{width:min(1280px,100%);margin-inline:auto;padding-inline:clamp(16px,4vw,48px)}}
.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
.skip{{position:absolute;left:16px;top:-60px;background:var(--ink);color:var(--white);padding:10px 14px;border-radius:8px;z-index:50;text-decoration:none}}
.skip:focus{{top:12px}}

.btn{{display:inline-flex;align-items:center;justify-content:center;gap:.5em;min-height:46px;padding:0 20px;border-radius:999px;border:1.5px solid currentColor;font-weight:650;font-size:15.5px;text-decoration:none;cursor:pointer;background:transparent;white-space:nowrap}}
.btn-ink{{background:var(--ink);border-color:var(--ink);color:var(--white)}}
.btn-ink:hover{{background:#2B2B2B}}
.btn-acc{{background:var(--acc);border-color:var(--acc);color:var(--btn-fg)}}
.btn-acc:hover{{filter:brightness(1.08)}}
.btn.sm{{min-height:40px;padding:0 16px;font-size:14.5px}}

.top{{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;background:rgba(243,243,239,.9);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid transparent;transition:border-color .2s}}
.top.scrolled{{border-bottom-color:var(--line)}}
.top .wrap{{display:flex;align-items:center;gap:22px;min-height:64px}}
.me{{font-weight:750;font-size:17px;text-decoration:none;font-variation-settings:"wdth" 112;letter-spacing:-.01em}}
.top nav{{display:flex;gap:22px;margin-left:auto;font-size:15px;font-weight:550}}
.top nav a{{text-decoration:none;color:var(--ink-2);padding-block:8px}}
.top nav a:hover{{color:var(--ink)}}
@media (max-width:760px){{.top nav{{display:none}}.top .btn{{margin-left:auto}}}}

.hero{{padding-block:clamp(36px,6vw,84px) clamp(40px,6vw,72px)}}
.name{{font-size:clamp(52px,12vw,176px);line-height:.86;letter-spacing:-.035em;font-weight:800;font-variation-settings:"wdth" 125;white-space:nowrap;animation:ink 1.3s cubic-bezier(.2,.8,.2,1) .1s both}}
.name span{{display:inline}}
@keyframes ink{{from{{font-variation-settings:"wdth" 125,"wght" 200;opacity:.2}}to{{font-variation-settings:"wdth" 125,"wght" 800;opacity:1}}}}
@media (max-width:700px){{.name span{{display:block}}}}
.hero-grid{{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:24px 64px;margin-top:clamp(24px,4vw,44px);align-items:start}}
@media (max-width:900px){{.hero-grid{{grid-template-columns:1fr}}}}
.role{{font-size:clamp(21px,2.3vw,30px);line-height:1.28;font-weight:500;letter-spacing:-.01em;max-width:24em}}
.reach{{display:grid;gap:14px}}
.reach-row{{display:grid;gap:8px;padding-top:12px;border-top:1px solid var(--line)}}
.reach-row .k{{font-size:13.5px;font-weight:650;color:var(--ink-2)}}
.reach-row .v{{font-size:19px;font-weight:600;user-select:all;overflow-wrap:anywhere}}
.reach-row .acts{{display:flex;flex-wrap:wrap;gap:8px}}

.index{{padding-block:clamp(40px,6vw,72px) clamp(56px,8vw,96px);border-top:1px solid var(--line)}}
.index h2,.sec h2{{font-size:clamp(32px,4vw,52px);letter-spacing:-.02em;font-weight:750;font-variation-settings:"wdth" 112}}
.idx{{list-style:none;margin-top:28px;display:grid}}
.idx a{{display:grid;grid-template-columns:150px minmax(0,1.1fr) minmax(0,1.6fr) auto;gap:8px 28px;align-items:center;padding:14px 0;border-top:1px solid var(--line);text-decoration:none}}
.idx li:last-child a{{border-bottom:1px solid var(--line)}}
.idx img{{width:150px;height:auto;border-radius:8px;display:block;transition:transform .25s ease}}
.idx a:hover img{{transform:translateY(-3px) rotate(-1deg)}}
.idx .nm{{font-size:clamp(20px,2vw,26px);font-weight:700;letter-spacing:-.01em;font-variation-settings:"wdth" 108}}
.idx .ds{{color:var(--ink-2);font-size:16px}}
.idx .kd{{font-size:13.5px;font-weight:650;border:1.5px solid var(--line);border-radius:999px;padding:4px 12px;white-space:nowrap}}
.idx .kd.real{{background:var(--ink);border-color:var(--ink);color:var(--white)}}
@media (max-width:860px){{.idx a{{grid-template-columns:110px minmax(0,1fr);gap:4px 16px}}.idx img{{width:110px;grid-row:span 3}}.idx .ds{{font-size:15px}}.idx .kd{{justify-self:start}}}}

.case{{background:var(--bg);color:var(--fg);padding-block:clamp(56px,8vw,112px);scroll-margin-top:64px}}
.case-head{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px 56px;align-items:end;margin-bottom:clamp(28px,4vw,48px)}}
@media (max-width:900px){{.case-head{{grid-template-columns:1fr}}}}
.tag{{display:inline-block;font-size:13.5px;font-weight:650;border:1.5px solid var(--rule);border-radius:999px;padding:4px 12px;margin-bottom:16px;color:var(--mute)}}
.case h2{{font-size:clamp(44px,6.4vw,96px);line-height:.92;letter-spacing:-.03em;font-weight:800;font-variation-settings:"wdth" 112}}
.sum{{font-size:clamp(18px,1.7vw,22px);line-height:1.4}}
.case-cta{{margin-top:20px}}
.shots{{display:grid;grid-template-columns:minmax(0,3.3fr) minmax(0,1fr);gap:clamp(14px,2.4vw,32px);align-items:end}}
.shots.alt{{grid-template-columns:minmax(0,1fr) minmax(0,3.3fr);margin-top:clamp(36px,5vw,64px)}}
.shots figure{{margin:0;min-width:0}}
.shots img{{display:block;width:100%;height:auto;background:var(--rule)}}
.shots .desk img{{border-radius:12px;box-shadow:0 24px 60px -28px rgba(0,0,0,.55);outline:1px solid var(--rule)}}
.shots .mob img{{border-radius:26px;border:6px solid var(--frame);box-shadow:0 24px 50px -24px rgba(0,0,0,.6)}}
.shots figcaption{{font-size:13.5px;color:var(--mute);margin-top:10px}}
@media (max-width:640px){{.shots,.shots.alt{{grid-template-columns:1fr 1fr}}.shots .desk{{grid-column:1 / -1}}.shots .mob{{grid-column:1 / span 1}}.shots.alt .mob{{order:2}}.shots .mob img{{border-width:4px;border-radius:20px}}}}
.facts{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px clamp(24px,4vw,56px);margin-top:clamp(36px,5vw,64px);padding-top:28px;border-top:1px solid var(--rule)}}
@media (max-width:900px){{.facts{{grid-template-columns:1fr}}}}
.facts h3{{font-size:14px;font-weight:700;color:var(--acc);margin-bottom:10px;letter-spacing:.01em}}
.facts h3:not(:first-child){{margin-top:22px}}
.facts p{{font-size:16.5px}}
.built{{list-style:none;display:grid;gap:9px;font-size:16px}}
.built li{{padding-left:18px;position:relative}}
.built li::before{{content:"";position:absolute;left:0;top:.62em;width:7px;height:7px;border-radius:50%;background:var(--acc)}}
.note{{margin-top:28px;font-size:13.5px;color:var(--mute);max-width:60em}}

.sec{{padding-block:clamp(64px,9vw,120px);border-top:1px solid var(--line)}}
.sec-head{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px 56px;align-items:end;margin-bottom:clamp(28px,4vw,44px)}}
.sec-head p{{color:var(--ink-2);max-width:34em}}
@media (max-width:760px){{.sec-head{{grid-template-columns:1fr}}}}
.svc{{list-style:none;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 clamp(24px,4vw,56px)}}
@media (max-width:760px){{.svc{{grid-template-columns:1fr}}}}
.svc > li{{padding:24px 0 30px;border-top:2px solid var(--ink);display:grid;gap:10px;align-content:start}}
.svc h3{{font-size:clamp(24px,2.4vw,32px);font-weight:750;letter-spacing:-.015em;font-variation-settings:"wdth" 110}}
.svc ul{{list-style:none;display:grid;gap:6px;font-size:15.5px;color:var(--ink-2)}}
.svc ul li::before{{content:"+ ";font-weight:700;color:var(--ink)}}
.proof{{font-size:15px;font-weight:600}}
.proof a{{text-underline-offset:3px}}
.steps{{list-style:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;counter-reset:s}}
@media (max-width:900px){{.steps{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:520px){{.steps{{grid-template-columns:1fr}}}}
.steps li{{counter-increment:s;display:grid;gap:8px;align-content:start}}
.steps li::before{{content:counter(s);font-size:44px;font-weight:800;line-height:1;font-variation-settings:"wdth" 75;color:var(--ink-2)}}
.steps h3{{font-size:21px;font-weight:700}}
.steps p{{color:var(--ink-2);font-size:15.5px}}
.about{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:24px 64px}}
@media (max-width:860px){{.about{{grid-template-columns:1fr}}}}
.about .txt{{display:grid;gap:16px;font-size:18px;max-width:38em}}
.contact{{background:var(--ink);color:var(--white);padding-block:clamp(64px,9vw,120px)}}
.contact h2{{font-size:clamp(40px,6vw,84px);letter-spacing:-.03em;font-weight:800;font-variation-settings:"wdth" 118;line-height:.95}}
.contact .lead{{margin-top:16px;color:#BDBDB8;font-size:18px;max-width:30em}}
.crow{{display:grid;grid-template-columns:200px minmax(0,1fr) auto;gap:10px 24px;align-items:center;padding:20px 0;border-top:1px solid #333}}
.crow:last-of-type{{border-bottom:1px solid #333}}
.crow .k{{font-size:14px;font-weight:650;color:#A9A9A4}}
.crow .v{{font-size:clamp(20px,2.4vw,28px);font-weight:650;letter-spacing:-.01em;user-select:all;overflow-wrap:anywhere}}
.crow .acts{{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end}}
.contact .btn{{color:var(--white)}}
.contact .btn-light{{background:var(--white);border-color:var(--white);color:var(--ink)}}
@media (max-width:760px){{.crow{{grid-template-columns:1fr}}.crow .acts{{justify-content:flex-start}}}}
.copied{{font-size:14px;color:#9BE3B3;min-height:1.4em;margin-top:14px}}
footer{{background:var(--ink);color:#8F8F8A;font-size:14px;padding-block:0 48px}}
footer .wrap{{display:grid;gap:10px;border-top:1px solid #333;padding-top:28px}}
footer p{{max-width:64em}}
</style>

<a class="skip" href="#work">Skip to the work</a>
<header class="top" id="top-bar">
  <div class="wrap">
    <a class="me" href="#start">Bhavya Sharma</a>
    <nav aria-label="Main"><a href="#work">Work</a><a href="#services">Services</a><a href="#about">About</a><a href="#contact">Contact</a></nav>
    <a class="btn btn-ink sm" href="{WA}" target="_blank" rel="noopener">WhatsApp me<span class="sr"> (opens WhatsApp in a new tab)</span></a>
  </div>
</header>

<main id="start">
<section class="hero" aria-labelledby="hero-name">
  <div class="wrap">
    <h1 class="name" id="hero-name"><span>Bhavya</span> <span>Sharma</span></h1>
    <div class="hero-grid">
      <p class="role">Designer and developer. I make websites, web apps and social content for small businesses, from the first sketch to the live site.</p>
      <div class="reach">
        <div class="reach-row"><span class="k">WhatsApp or call</span><span class="v">+91 75001 24113</span><span class="acts"><a class="btn btn-ink sm" href="{WA}" target="_blank" rel="noopener">Open WhatsApp</a><button type="button" class="btn sm" data-copy="+91 75001 24113">Copy number</button></span></div>
        <div class="reach-row"><span class="k">Email</span><span class="v">bhvyashrma@icloud.com</span><span class="acts"><a class="btn sm" href="mailto:bhvyashrma@icloud.com?subject=Project%20enquiry">Write an email</a><button type="button" class="btn sm" data-copy="bhvyashrma@icloud.com">Copy email</button></span></div>
      </div>
    </div>
    <p class="copied" id="copied-hero" role="status" aria-live="polite"></p>
  </div>
</section>

<section class="index" id="work" aria-labelledby="work-h">
  <div class="wrap">
    <h2 id="work-h">Selected work</h2>
    <ul class="idx">{index_rows}</ul>
  </div>
</section>
{''.join(case(c) for c in CASES)}

<section class="sec" id="services" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="svc-h">Services</h2><p>One person for the website, the system behind it, and the posts and videos that send people to it.</p></div>
    <ul class="svc">{services}</ul>
  </div>
</section>

<section class="sec" id="process" aria-labelledby="proc-h">
  <div class="wrap">
    <div class="sec-head"><h2 id="proc-h">How a project runs</h2><p>Four steps, with something real to look at from the second one.</p></div>
    <ol class="steps">
      <li><h3>A short call</h3><p>We talk through what the business needs and what a good result looks like. I send a written brief back.</p></li>
      <li><h3>Design</h3><p>You see real pages in the browser early, on your own phone, and we adjust them together.</p></li>
      <li><h3>Build</h3><p>I build and test on phones and desktops, and connect the forms and tools the business needs.</p></li>
      <li><h3>Launch</h3><p>I put the site live, show you how updates work, and hand over everything you paid for.</p></li>
    </ol>
  </div>
</section>

<section class="sec" id="about" aria-labelledby="about-h">
  <div class="wrap about">
    <h2 id="about-h">About</h2>
    <div class="txt">
      <p>I'm Bhavya Sharma, a designer and full-stack developer. I work across the whole job: the website, the system behind it, and the social posts and videos that point people to it. That keeps a small business's brand consistent, and one person answers the WhatsApp.</p>
      <p>My current product is ClearTrade, an export platform for Indian businesses. The other four projects on this page are independent concept demos with fictional brands. I built them to show how I would approach a gym, a salon, a café and a social campaign, and every interaction in them works.</p>
    </div>
  </div>
</section>
</main>

<section class="contact" id="contact" aria-labelledby="contact-h">
  <div class="wrap">
    <h2 id="contact-h">Start with a message</h2>
    <p class="lead">Tell me about the business and what you need. WhatsApp is quickest.</p>
    <div style="margin-top:36px">
      <div class="crow"><span class="k">WhatsApp or call</span><span class="v">+91 75001 24113</span><span class="acts"><a class="btn btn-light sm" href="{WA}" target="_blank" rel="noopener">Open WhatsApp</a><button type="button" class="btn sm" data-copy="+91 75001 24113">Copy number</button></span></div>
      <div class="crow"><span class="k">Email</span><span class="v">bhvyashrma@icloud.com</span><span class="acts"><a class="btn sm" href="mailto:bhvyashrma@icloud.com?subject=Project%20enquiry">Write an email</a><button type="button" class="btn sm" data-copy="bhvyashrma@icloud.com">Copy email</button></span></div>
      <div class="crow"><span class="k">Other email</span><span class="v">knownconstant@gmail.com</span><span class="acts"><button type="button" class="btn sm" data-copy="knownconstant@gmail.com">Copy email</button></span></div>
    </div>
    <p class="copied" id="copied" role="status" aria-live="polite"></p>
  </div>
</section>
<footer>
  <div class="wrap">
    <p>&copy; 2026 Bhavya Sharma. ClearTrade is a real product in progress. Mettle, Fringe, Dabara and Hookloop are independent concept demos with fictional brands; nothing on those sites books, sells or sends anything.</p>
    <p>Typeface: Mona Sans, used under the SIL Open Font License 1.1.</p>
  </div>
</footer>

<script>
(() => {{
'use strict';
const bar = document.getElementById('top-bar');
const onScroll = () => bar.classList.toggle('scrolled', scrollY > 8);
addEventListener('scroll', onScroll, {{ passive: true }}); onScroll();
/* fit the name to the column at its widest weight */
function fitName(){{
  const h = document.getElementById('hero-name'), box = h.parentElement, cs = getComputedStyle(box);
  const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  const lines = getComputedStyle(h.querySelector('span')).display === 'block' ? [...h.querySelectorAll('span')].map(s => s.textContent) : [h.textContent.replace(/\\s+/g, ' ').trim()];
  const probe = document.createElement('span');
  probe.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;font-size:100px;font-weight:800;letter-spacing:-.035em;font-variation-settings:"wdth" 125;font-family:' + getComputedStyle(h).fontFamily;
  document.body.appendChild(probe);
  let w = 0; lines.forEach(t => {{ probe.textContent = t; w = Math.max(w, probe.getBoundingClientRect().width); }});
  probe.remove();
  if (w) h.style.fontSize = Math.max(44, Math.min(200, Math.floor(100 * avail / w * .99))) + 'px';
}}
if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitName); else fitName();
let ft; addEventListener('resize', () => {{ clearTimeout(ft); ft = setTimeout(fitName, 120); }});
/* copy buttons: clipboard inside the click, with a select-the-text fallback */
document.addEventListener('click', e => {{
  const b = e.target.closest('[data-copy]'); if (!b) return;
  const text = b.dataset.copy, out = b.closest('#contact') ? document.getElementById('copied') : document.getElementById('copied-hero');
  const ok = () => {{ out.textContent = 'Copied ' + text; const was = b.textContent; b.textContent = 'Copied'; setTimeout(() => {{ b.textContent = was; }}, 1600); }};
  const fallback = () => {{ const v = b.closest('.crow, .reach-row').querySelector('.v'); const r = document.createRange(); r.selectNodeContents(v); const s = getSelection(); s.removeAllRanges(); s.addRange(r); out.textContent = 'Selected. Press copy on your keyboard or menu.'; }};
  try {{ navigator.clipboard.writeText(text).then(ok, fallback); }} catch (err) {{ fallback(); }}
}});
}})();
</script>
'''
open('/home/claude/work/src/portfolio/index.html', 'w').write(page)
print('written', len(page))
