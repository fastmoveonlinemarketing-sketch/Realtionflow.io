# -*- coding: utf-8 -*-
import re
f='relationflow_anwendungsfaelle.html'; s=open(f).read()
def svg(p): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'

cols=[('Zeit sparen',svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')),
      ('Qualität',svg('<path d="M12 2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17.6 5.9 20.4l1.5-6.8L2.2 9l6.9-.7z"/>')),
      ('Skalierung',svg('<path d="M3 17l6-6 4 4 8-8"/><path d="M16 7h5v5"/>')),
      ('Compliance',svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>'))]
GR={'trend':'#3b82f6,#1d4ed8','mega':'#0ea5e9,#2563eb','support':'#6366f1,#4338ca','gear':'#0891b2,#1d4ed8','code':'#7c3aed,#4f46e5','hr':'#0d9488,#2563eb'}
IC={'trend':svg('<path d="M3 17l6-6 4 4 8-8"/><path d="M16 7h5v5"/>'),
    'mega':svg('<path d="M3 11l15-5v12L3 13z"/><path d="M7 13v3a2 2 0 0 0 4 0"/>'),
    'support':svg('<path d="M4 14a8 8 0 0 1 16 0"/><rect x="2" y="14" width="4" height="6" rx="1.5"/><rect x="18" y="14" width="4" height="6" rx="1.5"/>'),
    'gear':svg('<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>'),
    'code':svg('<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>'),
    'hr':svg('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M19 8v6M22 11h-6"/>')}
rows=[('Vertrieb','trend',[('−85%','Zeit',4),('hoch','Qualität',3),('3×','Output',3),('gut','Basis',2)]),
      ('Marketing','mega',[('−70%','Zeit',3),('sehr hoch','Qualität',4),('5×','Output',4),('gut','Basis',2)]),
      ('Support','support',[('−60%','AHT',4),('hoch','Qualität',3),('24/7','Verfügbar',4),('stark','Audit',3)]),
      ('Operations','gear',[('−90%','Aufwand',4),('hoch','Qualität',3),('robust','Stabil',3),('Audit','Konform',4)]),
      ('IT','code',[('−40%','Zeit',3),('hoch','Qualität',3),('solide','Stabil',2),('sicher','Konform',4)]),
      ('HR','hr',[('−80%','Zeit',4),('fair','Qualität',3),('wachsend','Stabil',2),('konform','Konform',4)])]

def cell(v,u,l,best,delay):
    star='<span class="wm-star">&#9733;</span>' if best else ''
    return ('<div class="wm-cell l%d%s" style="--d:%.2fs">%s<div class="wm-v">%s</div><div class="wm-u">%s</div>'
            '<div class="wm-meter">%s</div></div>')%(l,(' best' if best else ''),delay,star,v,u,''.join('<i class="%s"></i>'%('on' if i<l else '') for i in range(4)))

grid='<div class="wm-corner"><b>Abteilung</b><span>&times; Wirkung</span></div>'
grid+=''.join('<div class="wm-colh"><span class="ci">%s</span><b>%s</b></div>'%(ic,n) for n,ic in cols)
for r,(name,key,cells) in enumerate(rows):
    grid+='<div class="wm-rowh"><span class="ri" style="background:linear-gradient(135deg,%s)">%s</span><b>%s</b></div>'%(GR[key],IC[key],name)
    best=max(c[2] for c in cells)
    for c,(v,u,l) in enumerate(cells):
        grid+=cell(v,u,l,l==best,(r+c)*0.05)

block=('<div class="af-wrap"><div class="wm-shell mm-reveal">'
 '<div class="wm-wrap"><div class="wm-grid" id="wmGrid">'+grid+'</div></div>'
 '<div class="wm-foot"><div class="wm-scale"><span>spürbar</span><div class="wm-sbar"></div><span>maximal</span></div>'
 '<div class="wm-note"><span class="wm-dotpulse"></span>In jeder Spalte zeigt sich: jede Abteilung profitiert &ndash; nur unterschiedlich stark.</div></div>'
 '</div></div></section>')

CSS='<style>'+''.join([
'.wm-shell{position:relative;margin-top:44px;background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.015));border:1px solid rgba(255,255,255,.1);border-radius:24px;padding:clamp(20px,3vw,34px);box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 40px 90px -50px rgba(0,0,0,.9)}',
'.wm-shell::before{content:"";position:absolute;inset:0;border-radius:24px;pointer-events:none;background:radial-gradient(60% 50% at 80% 0%,rgba(37,99,235,.18),transparent 60%)}',
'.wm-wrap{position:relative;overflow-x:auto;scrollbar-width:none}.wm-wrap::-webkit-scrollbar{display:none}',
'.wm-grid{display:grid;grid-template-columns:190px repeat(4,1fr);gap:10px;min-width:780px}',
'.wm-corner{display:flex;flex-direction:column;justify-content:flex-end;padding:10px 6px 12px}',
'.wm-corner b{font-size:.82rem;color:#fff;font-weight:700}.wm-corner span{font-size:.66rem;color:#7e8aa3;font-weight:600;margin-top:2px}',
'.wm-colh{display:flex;flex-direction:column;align-items:center;gap:8px;justify-content:flex-end;padding:10px 6px 12px;text-align:center}',
'.wm-colh .ci{width:38px;height:38px;border-radius:11px;background:rgba(125,169,255,.14);border:1px solid rgba(125,169,255,.22);color:#a8c7ff;display:flex;align-items:center;justify-content:center}',
'.wm-colh .ci svg{width:19px;height:19px}.wm-colh b{font-size:.78rem;color:#dbe3f2;font-weight:700;letter-spacing:.01em}',
'.wm-rowh{display:flex;align-items:center;gap:11px;padding:0 6px}',
'.wm-rowh .ri{width:38px;height:38px;border-radius:11px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;box-shadow:0 8px 18px -8px rgba(37,99,235,.7)}',
'.wm-rowh .ri svg{width:19px;height:19px}.wm-rowh b{font-size:.94rem;color:#fff;font-weight:700;letter-spacing:-0.01em}',
'.wm-cell{position:relative;overflow:hidden;border-radius:15px;padding:15px 12px 12px;min-height:104px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;border:1px solid rgba(255,255,255,.08);opacity:0;transform:translateY(12px) scale(.95);transition:opacity .55s cubic-bezier(.16,.8,.3,1),transform .55s cubic-bezier(.16,.8,.3,1),box-shadow .3s,border-color .3s}',
'.wm-grid.in .wm-cell{opacity:1;transform:none;transition-delay:var(--d)}',
'.wm-cell:hover{border-color:rgba(125,169,255,.5);box-shadow:0 16px 36px -18px rgba(37,99,235,.8);transform:translateY(-3px)}',
'.wm-cell.l1{background:linear-gradient(160deg,rgba(125,169,255,.12),rgba(125,169,255,.04))}',
'.wm-cell.l2{background:linear-gradient(160deg,rgba(37,99,235,.28),rgba(37,99,235,.12))}',
'.wm-cell.l3{background:linear-gradient(160deg,rgba(37,99,235,.5),rgba(37,99,235,.24))}',
'.wm-cell.l4{background:linear-gradient(150deg,#3b82f6,#1d4ed8);border-color:rgba(125,169,255,.55);box-shadow:0 18px 40px -20px rgba(37,99,235,.9)}',
'.wm-cell.l4::after{content:"";position:absolute;width:80px;height:80px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.4),transparent 70%);top:-30px;right:-24px;pointer-events:none}',
'.wm-v{font-size:1.18rem;font-weight:800;letter-spacing:-0.03em;line-height:1}',
'.wm-cell.l1 .wm-v{color:#cfe0ff}.wm-cell.l2 .wm-v{color:#fff}.wm-cell.l3 .wm-v,.wm-cell.l4 .wm-v{color:#fff}',
'.wm-u{font-size:.62rem;text-transform:uppercase;letter-spacing:.08em;font-weight:700;margin-top:5px;opacity:.75}',
'.wm-cell.l1 .wm-u{color:#9fb3d8}.wm-cell .wm-u{color:rgba(255,255,255,.8)}',
'.wm-meter{display:flex;gap:3px;margin-top:10px}',
'.wm-meter i{width:14px;height:4px;border-radius:2px;background:rgba(255,255,255,.16)}',
'.wm-meter i.on{background:rgba(255,255,255,.9)}.wm-cell.l1 .wm-meter i.on{background:#7da9ff}',
'.wm-star{position:absolute;top:8px;right:9px;font-size:.66rem;color:#ffd76a;text-shadow:0 0 8px rgba(255,200,60,.7)}',
'.wm-foot{display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;margin-top:24px}',
'.wm-scale{display:flex;align-items:center;gap:11px;font-size:.72rem;font-weight:600;color:#9aa6bd}',
'.wm-sbar{width:160px;height:8px;border-radius:999px;background:linear-gradient(90deg,rgba(125,169,255,.25),#3b82f6,#1d4ed8);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}',
'.wm-note{display:flex;align-items:center;gap:9px;font-size:.82rem;color:#b6c0d4;max-width:440px}',
'.wm-dotpulse{width:9px;height:9px;border-radius:50%;background:#7da9ff;flex-shrink:0;box-shadow:0 0 0 0 rgba(125,169,255,.5);animation:wmPulse 2s infinite}',
'@keyframes wmPulse{0%{box-shadow:0 0 0 0 rgba(125,169,255,.5)}70%{box-shadow:0 0 0 8px rgba(125,169,255,0)}100%{box-shadow:0 0 0 0 rgba(125,169,255,0)}}',
'@media(max-width:860px){.wm-foot{flex-direction:column;align-items:flex-start}}',
'@media(prefers-reduced-motion:reduce){.wm-grid.in .wm-cell{transition-delay:0s}.wm-dotpulse{animation:none}}',
])+'</style>'

# replace old matrix block (af-matrix table + legend) up to the section close
pat=re.compile(r'<div class="af-wrap"><div class="af-matrix">.*?</div></div></section>', re.S)
s2,n=pat.subn(block, s)
print('matrix replaced:',n)
s=s2
s=s.replace('</head>', CSS+'</head>',1)
# reveal script for wmGrid
js='<script>(function(){var g=document.getElementById("wmGrid");if(!g)return;if("IntersectionObserver" in window){var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){g.classList.add("in");o.disconnect();}})},{threshold:.2});o.observe(g);}else{g.classList.add("in");}})();</script>'
s=s.replace('</body>', js+'</body>',1)
open(f,'w').write(s)
print('wm cells:',s.count('class="wm-cell'),'best:',s.count('wm-cell l4 best')+s.count(' best"'))
import re as r;print('div',s.count('<div'),s.count('</div>'),'sec',len(r.findall(r'<section',s)),s.count('</section>'),'script',s.count('<script>'),s.count('</script>'))
