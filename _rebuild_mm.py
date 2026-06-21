# -*- coding: utf-8 -*-
import re
f='relationflow_features.html'
s=open(f).read()

def svg(p): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'
LG={'gpt':'#10a37f','claude':'#d97757','gemini':'#4285f4','mistral':'#ff7000','byom':'#1d4ed8'}
SH={'gpt':'G4','claude':'Cl','gemini':'Ge','mistral':'Mi','byom':'Ei'}
NAME={'gpt':'GPT-4o','claude':'Claude','gemini':'Gemini','mistral':'Mistral','byom':'Eigenes'}
order=['gpt','claude','gemini','mistral','byom']

CSS = r'''<style>
/* ================= MULTI-MODELL DEEP-DIVE (.mm-) ================= */
.mm-sec{padding:clamp(62px,8vw,110px) 0;position:relative;overflow:hidden;background:#fff}
.mm-sec.alt{background:var(--bg-alt)}
.mm-wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.mm-center{text-align:center;max-width:800px;margin-left:auto;margin-right:auto}
.mm-ey{display:inline-flex;align-items:center;gap:8px;font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent-dark);background:var(--accent-soft);border:1px solid var(--accent-soft-2);padding:7px 14px;border-radius:999px}
.mm-ey i{width:6px;height:6px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 4px var(--accent-soft)}
.mm-h2{font-size:clamp(2rem,4.6vw,3.5rem);line-height:1.04;letter-spacing:-0.04em;font-weight:700;margin:20px 0 0}
.mm-lead{font-size:clamp(1.05rem,1.5vw,1.3rem);color:var(--muted);line-height:1.6;margin:18px auto 0;max-width:680px}
.mm-kick{font-size:.78rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent-dark)}
.mm-phead{max-width:660px;margin-bottom:6px}
.mm-phead.mm-center{margin-left:auto;margin-right:auto}
.mm-ph2{font-size:clamp(1.5rem,3vw,2.3rem);line-height:1.1;letter-spacing:-0.03em;font-weight:700;margin:14px 0 0}
.mm-psub{color:var(--muted);font-size:1.05rem;line-height:1.6;margin:14px 0 0;max-width:600px}
.mm-phead.mm-center .mm-psub{margin-left:auto;margin-right:auto}
.mm-reveal{opacity:0;transform:translateY(28px);transition:opacity .85s cubic-bezier(.16,.8,.3,1),transform .85s cubic-bezier(.16,.8,.3,1)}
.mm-reveal.in{opacity:1;transform:none}
/* dark section = breite & margin wie Steuerung */
.mm-darksec{position:relative;overflow:hidden;border-radius:var(--radius-lg);margin:0 48px;color:#fff;padding:clamp(54px,7vw,94px) 0;background:radial-gradient(70% 80% at 30% 10%,rgba(37,99,235,.28),transparent 60%),linear-gradient(180deg,#070b14,#05070d)}
.mm-darksec::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(1px 1px at 18% 30%,rgba(255,255,255,.5),transparent),radial-gradient(1px 1px at 72% 22%,rgba(255,255,255,.4),transparent),radial-gradient(1.5px 1.5px at 42% 72%,rgba(255,255,255,.45),transparent),radial-gradient(1px 1px at 86% 64%,rgba(255,255,255,.35),transparent),radial-gradient(1px 1px at 12% 82%,rgba(255,255,255,.45),transparent)}
.mm-darksec>.mm-wrap{position:relative;z-index:1}
@media(max-width:680px){.mm-darksec{margin:0 16px}}
.mm-hero-viz{display:grid;grid-template-columns:1fr auto 1fr;gap:clamp(20px,4vw,56px);align-items:center;margin:54px auto 0;max-width:880px}
.mm-side{text-align:center}
.mm-side .lab{font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:16px}
.mm-side.bad .lab{color:#dc2626}.mm-side.good .lab{color:var(--accent-dark)}
.mm-lonely{width:96px;height:96px;border-radius:24px;margin:0 auto;background:#fff;border:1px solid var(--line);box-shadow:var(--shadow-sm);display:flex;align-items:center;justify-content:center;color:#9aa3ad;font-weight:700;position:relative;filter:grayscale(.4)}
.mm-lonely::after{content:"nur 1 Modell";position:absolute;bottom:-26px;left:0;right:0;font-size:.72rem;color:var(--muted-2);font-weight:600}
.mm-cluster{position:relative;width:200px;height:130px;margin:0 auto}
.mm-cluster .nd{position:absolute;width:46px;height:46px;border-radius:13px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:.62rem;box-shadow:0 10px 22px -8px rgba(37,99,235,.6);animation:mmPop .5s both}
.mm-cluster svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.mm-cluster .ln{stroke:var(--accent-light);stroke-width:1.5;stroke-dasharray:4 5;animation:mmDash 1s linear infinite;opacity:.6}
@keyframes mmDash{to{stroke-dashoffset:-18}}
@keyframes mmPop{from{opacity:0;transform:scale(.5)}to{opacity:1;transform:none}}
.mm-arrow{font-size:1.6rem;color:var(--accent);font-weight:700}
@media(max-width:760px){.mm-hero-viz{grid-template-columns:1fr}.mm-arrow{transform:rotate(90deg)}}
.mm-prob-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.mm-prob{background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:24px;position:relative;overflow:hidden}
.mm-prob .pi{width:44px;height:44px;border-radius:12px;background:rgba(220,38,38,.16);color:#ff8b8b;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.mm-prob .pi svg{width:23px;height:23px}
.mm-prob h4{font-size:1.05rem;letter-spacing:-0.01em;color:#fff}
.mm-prob p{font-size:.88rem;color:#9aa6bd;line-height:1.5;margin-top:7px}
.mm-prob .tagx{position:absolute;top:18px;right:18px;font-size:.62rem;font-weight:700;color:#ff8b8b;background:rgba(220,38,38,.14);border-radius:999px;padding:3px 9px}
@media(max-width:860px){.mm-prob-grid{grid-template-columns:1fr}}
.mm-models{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:40px}
.mm-model{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px 16px;box-shadow:var(--shadow-sm);text-align:center;transition:transform .25s,box-shadow .25s,border-color .25s}
.mm-model:hover{transform:translateY(-5px);box-shadow:var(--shadow-md);border-color:var(--accent-light)}
.mm-model .ml{width:46px;height:46px;border-radius:13px;margin:0 auto 12px;color:#fff;font-weight:700;font-size:.84rem;display:flex;align-items:center;justify-content:center}
.mm-model b{font-size:.96rem;display:block}
.mm-model .role{font-size:.78rem;color:var(--accent-dark);font-weight:600;margin-top:3px}
.mm-model p{font-size:.78rem;color:var(--muted-2);line-height:1.45;margin-top:9px}
@media(max-width:860px){.mm-models{grid-template-columns:1fr 1fr}}
.mm-matrix{margin-top:36px;overflow-x:auto;padding-bottom:6px}
.mm-mtable{display:grid;grid-template-columns:1.5fr repeat(5,1fr);gap:8px;min-width:720px}
.mm-mhead{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:var(--muted-2);text-align:center;padding:8px 4px;display:flex;align-items:center;justify-content:center;gap:6px}
.mm-mhead .lg{width:18px;height:18px;border-radius:5px;color:#fff;font-size:.5rem;font-weight:700;display:flex;align-items:center;justify-content:center}
.mm-rowh{font-weight:700;font-size:.9rem;display:flex;align-items:center;padding-left:4px}
.mm-cell{display:flex;align-items:center;justify-content:center;border:1px solid var(--line);border-radius:12px;padding:14px 6px;background:#fff;position:relative}
.mm-cell.best{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
.mm-cell.best::after{content:"\2605";position:absolute;top:4px;right:6px;font-size:.6rem;color:var(--accent)}
.mm-meter{display:flex;gap:3px}
.mm-meter i{width:9px;height:16px;border-radius:3px;background:var(--bg-alt)}
.mm-meter i.on{background:linear-gradient(180deg,var(--accent-light),var(--accent))}
.mm-cell.best .mm-meter i.on{background:linear-gradient(180deg,var(--accent),var(--accent-dark))}
.mm-mcap{text-align:center;font-size:.95rem;color:var(--muted);margin-top:22px}
.mm-mcap b{color:var(--text)}
.mm-pipe{display:grid;grid-template-columns:1fr auto auto auto 1fr;align-items:center;gap:12px;margin-top:36px}
.mm-node{background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.13);border-radius:16px;padding:18px;min-height:96px;display:flex;flex-direction:column;justify-content:center}
.mm-node .t{font-size:.64rem;text-transform:uppercase;letter-spacing:.1em;color:#7da9ff;font-weight:700;margin-bottom:6px}
.mm-node b{font-size:.92rem;line-height:1.4;color:#fff}
.mm-node-core{align-items:center;text-align:center;background:radial-gradient(circle at 40% 30%,#5b8def,#1e40af);border:none;box-shadow:0 18px 40px -16px rgba(37,99,235,.8);min-width:128px}
.mm-node-core b{font-size:1rem}.mm-node-core small{font-size:.6rem;color:rgba(255,255,255,.78);letter-spacing:.04em;display:block;margin-top:3px}
.mm-node-out b{color:#fff;font-size:1.05rem}.mm-node-out .t.r{color:#9aa6bd;text-transform:none;letter-spacing:0;font-size:.78rem;font-weight:500;margin-top:7px;margin-bottom:0}
.mm-flow{display:flex;gap:6px;justify-content:center}
.mm-flow .mm-dot{width:7px;height:7px;border-radius:50%;background:#7da9ff;opacity:.3}
.mm-pipe.go .mm-flow .mm-dot{animation:mmDot 1.1s ease-in-out}
.mm-flow .mm-dot:nth-child(2){animation-delay:.12s}.mm-flow .mm-dot:nth-child(3){animation-delay:.24s}
@keyframes mmDot{0%,100%{opacity:.3;transform:none}40%{opacity:1;transform:translateY(-4px)}}
.mm-modelbar{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:28px}
.mm-rm{display:inline-flex;align-items:center;gap:7px;font-size:.82rem;font-weight:600;color:#b6c0d4;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);border-radius:999px;padding:8px 14px;transition:all .3s}
.mm-rm .d{width:9px;height:9px;border-radius:50%}
.mm-rm.on{color:#fff;background:rgba(37,99,235,.28);border-color:var(--accent-light);box-shadow:0 0 0 3px rgba(37,99,235,.18)}
@media(max-width:760px){.mm-pipe{grid-template-columns:1fr}}
.mm-scen{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.mm-sc{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:var(--shadow-sm);transition:transform .22s,box-shadow .22s}
.mm-sc:hover{transform:translateY(-4px);box-shadow:var(--shadow-md)}
.mm-sc .si{width:42px;height:42px;border-radius:12px;background:var(--accent-soft);color:var(--accent-dark);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.mm-sc .si svg{width:22px;height:22px}
.mm-sc .task{font-size:.95rem;font-weight:700;letter-spacing:-0.01em}
.mm-sc .arrow{display:flex;align-items:center;gap:8px;margin:12px 0 6px;font-size:.82rem;color:var(--muted-2)}
.mm-sc .win{display:inline-flex;align-items:center;gap:7px;font-weight:700;font-size:.86rem;color:var(--accent-dark);background:var(--accent-soft);border-radius:999px;padding:5px 12px}
.mm-sc .win .d{width:8px;height:8px;border-radius:50%}
.mm-sc p{font-size:.82rem;color:var(--muted-2);line-height:1.5;margin-top:10px}
@media(max-width:860px){.mm-scen{grid-template-columns:1fr}}
.mm-cmp{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:40px}
.mm-col{border-radius:20px;padding:28px;border:1px solid var(--line)}
.mm-col.one{background:linear-gradient(180deg,#fff7f7,#fdeef0);border-color:#f3d4d8}
.mm-col.multi{background:linear-gradient(180deg,#f1f6ff,#eaf1ff)}
.mm-col .ch{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1.1rem;margin-bottom:20px}
.mm-col .ch .tag{font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;padding:4px 10px;border-radius:999px}
.mm-col.one .tag{background:#fde2e4;color:#dc2626}.mm-col.multi .tag{background:#dcf7e6;color:#16a34a}
.mm-metric{margin:14px 0}
.mm-metric .ml{display:flex;justify-content:space-between;font-size:.82rem;font-weight:600;margin-bottom:6px}
.mm-metric .ml .v{font-variant-numeric:tabular-nums}
.mm-barwrap .mm-track{height:9px;border-radius:999px;background:rgba(0,0,0,.06);overflow:hidden}
.mm-track i{display:block;height:100%;width:0;border-radius:999px;transition:width 1.3s cubic-bezier(.2,.8,.2,1)}
.mm-col.one .mm-track i{background:linear-gradient(90deg,#f0a3aa,#dc2626)}
.mm-col.multi .mm-track i{background:linear-gradient(90deg,var(--accent-light),var(--accent))}
@media(max-width:760px){.mm-cmp{grid-template-columns:1fr}}
.mm-nums{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:40px}
.mm-num{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 22px;box-shadow:var(--shadow-sm);text-align:center}
.mm-num b{font-size:clamp(2rem,4vw,2.9rem);font-weight:700;letter-spacing:-0.04em;line-height:1;background:linear-gradient(135deg,var(--accent),var(--accent-dark));-webkit-background-clip:text;background-clip:text;color:transparent;display:block}
.mm-num .l{font-weight:600;font-size:.92rem;margin-top:9px}
.mm-num .s{font-size:.78rem;color:var(--muted-2);margin-top:5px}
@media(max-width:860px){.mm-nums{grid-template-columns:1fr 1fr}}
.mm-close{text-align:center}
.mm-close .big{font-family:Lora,serif;font-style:italic;font-size:clamp(1.5rem,3.4vw,2.4rem);line-height:1.32;color:#fff;max-width:820px;margin:0 auto}
.mm-close .big span{font-style:normal;color:#7da9ff;font-weight:700;font-family:inherit}
.mm-close .sub{color:#9aa6bd;margin-top:20px;font-size:1.02rem}
.mm-close .cta{margin-top:30px;display:inline-flex;gap:12px;flex-wrap:wrap;justify-content:center}
@media(prefers-reduced-motion:reduce){.mm-cluster .ln,.mm-pipe.go .mm-flow .mm-dot{animation:none}}
</style>'''

# matrix
dims=[('Komplexes Reasoning',[3,3,2,2,2]),('Sehr lange Kontexte',[2,3,2,1,2]),('Code & Technik',[3,3,2,2,1]),
      ('Bilder & Multimodal',[2,2,3,1,1]),('Geschwindigkeit',[2,2,2,3,2]),('Kosten-Effizienz',[1,2,2,3,3]),
      ('EU & Datenhoheit',[1,1,1,2,3])]
def meter(v): return '<span class="mm-meter">'+''.join('<i class="on"></i>' if i<v else '<i></i>' for i in range(3))+'</span>'
mhead='<div class="mm-mhead">Stärke je Aufgabe</div>'+''.join('<div class="mm-mhead"><span class="lg" style="background:%s">%s</span>%s</div>'%(LG[k],SH[k],NAME[k]) for k in order)
mrows=''
for dim,vals in dims:
    best=max(vals)
    mrows+='<div class="mm-rowh">%s</div>'%dim+''.join('<div class="mm-cell%s">%s</div>'%(' best' if v==best else '',meter(v)) for v in vals)
matrix='<div class="mm-matrix mm-reveal"><div class="mm-mtable">'+mhead+mrows+'</div></div>'

models_data=[('gpt','Der Allrounder','Stark im Reasoning und bei vielschichtigen Aufgaben.'),('claude','Der Tiefdenker','Brilliert bei langen Dokumenten und feinen Nuancen.'),('gemini','Der Multimodale','Versteht Bilder, Tabellen und Medien nativ.'),('mistral','Der Sprinter','Extrem schnell & günstig – ideal für Massenaufgaben.'),('byom','Euer Eigenes','On-premise, EU, voll unter eurer Kontrolle.')]
models='<div class="mm-models mm-reveal">'+''.join('<div class="mm-model"><div class="ml" style="background:%s">%s</div><b>%s</b><div class="role">%s</div><p>%s</p></div>'%(LG[k],SH[k],NAME[k],r,d) for k,r,d in models_data)+'</div>'

probs=[('Blinde Flecken','Jedes Modell hat Schwächen. Bei einem Anbieter erbt ihr alle – ohne Ausweg.',svg('<circle cx="12" cy="12" r="3"/><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7a9.8 9.8 0 0 1-5-1.3"/><path d="M3 3l18 18"/>')),
 ('Vendor Lock-in','Preise, Limits oder Bedingungen ändern sich – und ihr seid gebunden.',svg('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')),
 ('Ausfälle','Ein Anbieter hat eine Störung – euer ganzes Team steht still.',svg('<path d="M18.4 5.6A9 9 0 1 0 21 12"/><path d="M21 3v6h-6"/>')),
 ('Suboptimale Ergebnisse','Ihr nutzt für jede Aufgabe dasselbe Werkzeug – statt das jeweils beste.',svg('<path d="M3 3v18h18"/><path d="M7 14l3-3 2 2 5-6"/>')),
 ('Kostenfalle','Ein teures Premium-Modell für simple Massenaufgaben verbrennt Budget.',svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')),
 ('Innovations-Stillstand','Morgen kommt ein besseres Modell – Wechsel? Großes Migrationsprojekt.',svg('<path d="M13 2L3 14h7l-1 8 10-12h-7z"/>'))]
prob_cards='<div class="mm-prob-grid">'+''.join('<div class="mm-prob"><span class="tagx">Risiko</span><div class="pi">%s</div><h4>%s</h4><p>%s</p></div>'%(ic,t,d) for t,d,ic in probs)+'</div>'

modelbar=''.join('<span class="mm-rm" data-m="%s"><span class="d" style="background:%s"></span>%s</span>'%(k,LG[k],NAME[k]) for k in order)
routing_inner='''<div class="mm-pipe go" id="mmPipe">
<div class="mm-node"><span class="t">Eure Aufgabe</span><b id="mmPrompt">&bdquo;Analysiere diesen 80-seitigen Vertrag und finde Risiken.&ldquo;</b></div>
<div class="mm-flow"><span class="mm-dot"></span><span class="mm-dot"></span><span class="mm-dot"></span></div>
<div class="mm-node mm-node-core"><b>Smart-Select</b><small>analysiert &amp; routet</small></div>
<div class="mm-flow"><span class="mm-dot"></span><span class="mm-dot"></span><span class="mm-dot"></span></div>
<div class="mm-node mm-node-out"><span class="t">Bestes Modell</span><b id="mmModel">Claude</b><div class="t r" id="mmReason">Bester Umgang mit langen Dokumenten.</div></div>
</div>
<div class="mm-modelbar" id="mmModelbar">'''+modelbar+'</div>'

scen_data=[('Langer Vertrag, 80 Seiten','claude','Große Kontextfenster, präzise bei Klauseln.',svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>')),
 ('Produktfoto analysieren','gemini','Nativ multimodal – sieht, was im Bild steckt.',svg('<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="M21 15l-5-5L5 21"/>')),
 ('1.000 Produkttexte','mistral','Schnell und günstig bei großen Mengen.',svg('<path d="M13 2L3 14h7l-1 8 10-12h-7z"/>')),
 ('Sensible Patientendaten','byom','Bleibt on-premise – volle Datenhoheit.',svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>')),
 ('Mehrstufige Logikaufgabe','gpt','Starkes Reasoning über viele Schritte.',svg('<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/>')),
 ('Schneller Chat-Entwurf','gpt','Ausgewogen und sofort einsatzbereit.',svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'))]
scen='<div class="mm-scen mm-reveal">'+''.join('<div class="mm-sc"><div class="si">%s</div><div class="task">%s</div><div class="arrow">wird gelöst von</div><span class="win"><span class="d" style="background:%s"></span>%s</span><p>%s</p></div>'%(ic,task,LG[k],NAME[k],why) for task,k,why,ic in scen_data)+'</div>'

def metric(label,one,multi):
    return ('<div class="mm-metric"><div class="ml"><span>%s</span><span class="v">%s</span></div><div class="mm-barwrap"><div class="mm-track"><i data-w="%d"></i></div></div></div>'%(label,one[0],one[1]),
            '<div class="mm-metric"><div class="ml"><span>%s</span><span class="v">%s</span></div><div class="mm-barwrap"><div class="mm-track"><i data-w="%d"></i></div></div></div>'%(label,multi[0],multi[1]))
rws=[metric('Ergebnis-Qualität',('Begrenzt',55),('Optimal',96)),metric('Ausfallsicherheit',('Single Point of Failure',30),('Automatischer Fallback',99)),metric('Kosten-Effizienz',('Oft zu teuer',45),('Richtiges Modell pro Task',88)),metric('Zukunftssicherheit',('Lock-in',35),('Jederzeit erweiterbar',97))]
compare='<div class="mm-cmp mm-reveal"><div class="mm-col one"><div class="ch"><span class="tag">Nur 1 Modell</span>Single-Model</div>'+''.join(r[0] for r in rws)+'</div><div class="mm-col multi"><div class="ch"><span class="tag">Multi-Modell</span>Relationflow</div>'+''.join(r[1] for r in rws)+'</div></div>'

nums=[('40','%','bessere Ergebnisse','durch das jeweils beste Modell'),('0','','Vendor Lock-in','jederzeit Modelle wechseln'),('99.9','%','Verfügbarkeit','dank automatischem Fallback'),('45','%','geringere Kosten','richtiges Modell pro Aufgabe')]
def numcard(v,suf,l,sl):
    dec=' data-dec="1"' if '.' in v else ''
    return '<div class="mm-num"><b><span class="mm-count" data-to="%s"%s>0</span>%s</b><div class="l">%s</div><div class="s">%s</div></div>'%(v,dec,suf,l,sl)
numbers='<div class="mm-nums mm-reveal">'+''.join(numcard(*n) for n in nums)+'</div>'

intro_inner='''<div class="mm-center mm-reveal"><span class="mm-ey"><i></i>Multi-Modell &middot; Tiefenanalyse</span>
<h2 class="mm-h2">Ein Modell f&uuml;r alles? Das ist, als h&auml;ttet ihr <span class="serif">nur einen</span> Mitarbeiter.</h2>
<p class="mm-lead">Kein KI-Modell ist in allem das beste. Wer sich auf eines festlegt, verschenkt Qualit&auml;t, riskiert Ausf&auml;lle und zahlt drauf. Multi-Modell hei&szlig;t: f&uuml;r jede Aufgabe automatisch das st&auml;rkste Modell &ndash; sicher in einer Plattform.</p>
<div class="mm-hero-viz">
<div class="mm-side bad"><div class="lab">Single-Model</div><div class="mm-lonely">1</div></div>
<div class="mm-arrow">&rarr;</div>
<div class="mm-side good"><div class="lab">Multi-Modell</div><div class="mm-cluster">
<svg><line class="ln" x1="100" y1="65" x2="30" y2="22"/><line class="ln" x1="100" y1="65" x2="170" y2="22"/><line class="ln" x1="100" y1="65" x2="20" y2="105"/><line class="ln" x1="100" y1="65" x2="180" y2="105"/></svg>
<div class="nd" style="left:77px;top:42px;background:linear-gradient(135deg,#5b8def,#1e40af);width:50px;height:50px;font-size:.66rem">Hub</div>
<div class="nd" style="left:8px;top:0;background:#10a37f;animation-delay:.1s">G4</div>
<div class="nd" style="left:150px;top:0;background:#d97757;animation-delay:.2s">Cl</div>
<div class="nd" style="left:0;top:84px;background:#4285f4;animation-delay:.3s">Ge</div>
<div class="nd" style="left:158px;top:84px;background:#ff7000;animation-delay:.4s">Mi</div>
</div></div>
</div></div>'''

def light(head, body, alt=False):
    return '<section class="mm-sec%s"><div class="mm-wrap">%s%s</div></section>'%(' alt' if alt else '', head, body)
def dark(inner):
    return '<section class="mm-darksec"><div class="mm-wrap">%s</div></section>'%inner

def phead(kick,h,sub,kickcolor=None,center=False,dark=False):
    kc=' style="color:%s"'%kickcolor if kickcolor else ''
    hc=' style="color:#fff"' if dark else ''
    sc=' style="color:#9aa6bd"' if dark else ''
    cc=' mm-center' if center else ''
    return '<div class="mm-phead%s mm-reveal"><span class="mm-kick"%s>%s</span><h3 class="mm-ph2"%s>%s</h3><p class="mm-psub"%s>%s</p></div>'%(cc,kc,kick,hc,h,sc,sub)

SECTIONS = (
 '<section class="mm-sec"><div class="mm-wrap">'+intro_inner+'</div></section>'
 + dark(phead('Das Risiko','Nur ein Modell zu nutzen, ist 2026 ein teurer Fehler.','Wer alles auf einen Anbieter setzt, kauft sich dessen Schw&auml;chen mit ein &ndash; und gibt Qualit&auml;t, Sicherheit und Geld freiwillig auf.',kickcolor='#ff8b8b',dark=True)+prob_cards)
 + light(phead('Die L&ouml;sung','F&uuml;nf Spezialisten statt einem Generalisten.','Jedes Modell hat eine Superkraft. Multi-Modell hei&szlig;t: ihr nutzt sie alle &ndash; je nach Aufgabe.'), models, alt=True)
 + light(phead('Der Beweis','Kein Modell f&uuml;hrt &uuml;berall.','Diese Matrix zeigt es schwarz auf wei&szlig;: Je nach Aufgabe gewinnt ein anderes Modell. Genau deshalb braucht ihr alle.'), matrix+'<p class="mm-mcap">In <b>jeder</b> Zeile gewinnt ein anderes Modell &ndash; ein einzelnes Modell ist nie &uuml;berall vorne.</p>')
 + dark(phead('Smart-Select','Die richtige Wahl trifft Relationflow automatisch.','Ihr schreibt einfach eure Aufgabe. Smart-Select analysiert sie und leitet sie an das Modell, das sie am besten l&ouml;st &ndash; in Echtzeit.',kickcolor='#7da9ff',dark=True)+routing_inner)
 + light(phead('In der Praxis','Dieselbe Plattform &ndash; immer das passende Modell.','Konkrete Aufgaben aus dem Arbeitsalltag und das Modell, das sie am besten l&ouml;st.'), scen, alt=True)
 + light(phead('Der direkte Vergleich','Single-Model gegen Multi-Modell.',''), compare)
 + light(phead('Der Nutzen in Zahlen','Was Multi-Modell konkret bringt.','',center=True), numbers, alt=True)
 + dark('<div class="mm-close mm-reveal"><p class="big">Mit nur einem KI-Modell zu arbeiten hei&szlig;t, freiwillig auf <span>Qualit&auml;t, Sicherheit und Geld</span> zu verzichten.</p><p class="sub">Relationflow gibt euch alle f&uuml;hrenden Modelle &ndash; plus eure eigenen &ndash; in einer sicheren, DSGVO-konformen Oberfl&auml;che.</p><div class="cta"><a href="#" class="btn btn-primary">Kostenlos starten</a><a href="#" class="btn btn-ghost">Demo buchen</a></div></div>')
)

JS = '''<script>
(function(){
 var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target);}})},{threshold:.12});
 document.querySelectorAll('.mm-reveal').forEach(function(el){ro.observe(el);});
 document.querySelectorAll('.mm-barwrap').forEach(function(w){var s=false;var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!s){s=true;w.querySelectorAll('i[data-w]').forEach(function(i){i.style.width=i.dataset.w+'%';});}})},{threshold:.35});o.observe(w);});
 var cs=new WeakSet();
 function cnt(el){var to=parseFloat(el.dataset.to),dec=el.dataset.dec,t0=null;requestAnimationFrame(function go(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1500,1);var e=1-Math.pow(1-p,3);var v=dec?(e*to).toFixed(1):Math.floor(e*to);el.textContent=(''+v).replace('.',',');if(p<1)requestAnimationFrame(go);else el.textContent=(''+(dec?to.toFixed(1):to)).replace('.',',');});}
 var co=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!cs.has(e.target)){cs.add(e.target);cnt(e.target);}})},{threshold:.4});
 document.querySelectorAll('.mm-count').forEach(function(el){co.observe(el);});
 var ex=[
  {p:'„Analysiere diesen 80-seitigen Vertrag und finde Risiken.“',m:'claude',mn:'Claude',r:'Bester Umgang mit langen Dokumenten & Nuancen.'},
  {p:'„Beschreibe, was auf diesem Produktfoto zu sehen ist.“',m:'gemini',mn:'Gemini',r:'Stark bei Bildern & multimodalen Aufgaben.'},
  {p:'„Erzeuge 1.000 Produkttexte – schnell und günstig.“',m:'mistral',mn:'Mistral',r:'Sehr schnell & kosteneffizient bei Massen.'},
  {p:'„Verarbeite diese sensiblen Patientendaten.“',m:'byom',mn:'Eigenes EU-Modell',r:'Bleibt on-premise – maximale Datenhoheit.'},
  {p:'„Löse diese komplexe mehrstufige Logikaufgabe.“',m:'gpt',mn:'GPT-4o',r:'Starkes Reasoning bei vielschichtigen Aufgaben.'}
 ];
 var pi=document.getElementById('mmPrompt'),mo=document.getElementById('mmModel'),rs=document.getElementById('mmReason'),bar=document.getElementById('mmModelbar'),pipe=document.getElementById('mmPipe');
 var idx=0;
 function tick(){var e=ex[idx];if(pi)pi.textContent=e.p;if(mo)mo.textContent=e.mn;if(rs)rs.textContent=e.r;if(bar)bar.querySelectorAll('.mm-rm').forEach(function(c){c.classList.toggle('on',c.dataset.m===e.m);});if(pipe){pipe.classList.remove('go');void pipe.offsetWidth;pipe.classList.add('go');}idx=(idx+1)%ex.length;}
 var started=false;if(pipe){var po=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!started){started=true;tick();setInterval(tick,3000);}})},{threshold:.3});po.observe(pipe);}
})();
</script>'''

# remove old mm block and insert new
pat=re.compile(r'<style>\s*/\* =+ MULTI-MODELL DEEP-DIVE.*?</script>', re.S)
m=pat.search(s)
assert m, 'old mm block not found'
s=s[:m.start()]+CSS+SECTIONS+JS+s[m.end():]
open(f,'w').write(s)
print('mm-sec:',s.count('class="mm-sec"'),'mm-darksec:',s.count('class="mm-darksec"'))
print('div',s.count('<div'),s.count('</div>'),'sec',len(re.findall(r'<section',s)),s.count('</section>'),'style',s.count('<style>'),s.count('</style>'),'script',s.count('<script>'),s.count('</script>'))
