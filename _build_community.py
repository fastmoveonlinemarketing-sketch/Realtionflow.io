# -*- coding: utf-8 -*-
import re
f='relationflow_features.html'; s=open(f).read()
def svg(p): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'

CSS = r'''<style>
/* ================= COMMUNITY (.co-) ================= */
.co-sec{padding:clamp(64px,8vw,116px) 0;background:#fff;position:relative;overflow:hidden}
.co-sec.alt{background:var(--bg-alt)}
.co-wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.co-center{text-align:center;max-width:780px;margin:0 auto}
.co-h2{font-size:clamp(1.9rem,4vw,3rem);line-height:1.06;letter-spacing:-0.035em;font-weight:700;margin:18px 0 0}
.co-sub{font-size:clamp(1.02rem,1.4vw,1.2rem);color:var(--muted);line-height:1.6;margin:16px auto 0;max-width:660px}
.co-dark{position:relative;overflow:hidden;border-radius:var(--radius-lg);margin:0 48px;color:#fff;padding:clamp(56px,7vw,96px) 0;background:radial-gradient(78% 88% at 50% -10%,rgba(37,99,235,.3),transparent 55%),linear-gradient(180deg,#070b14,#05070d)}
.co-dark::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(1px 1px at 18% 30%,rgba(255,255,255,.5),transparent),radial-gradient(1px 1px at 72% 22%,rgba(255,255,255,.4),transparent),radial-gradient(1.5px 1.5px at 42% 72%,rgba(255,255,255,.45),transparent),radial-gradient(1px 1px at 86% 64%,rgba(255,255,255,.35),transparent),radial-gradient(1px 1px at 12% 82%,rgba(255,255,255,.45),transparent)}
.co-dark>.co-wrap{position:relative;z-index:1}
.co-dark .co-h2{color:#fff}.co-dark .co-sub{color:#b6c0d4}.co-dark .serif{color:#fff}
.co-dark .eyebrow{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.02));color:#cfe0ff;border-color:rgba(255,255,255,.14)}
@media(max-width:680px){.co-dark{margin:0 16px}}
.co-reveal{opacity:0;transform:translateY(26px);transition:opacity .8s cubic-bezier(.16,.8,.3,1),transform .8s cubic-bezier(.16,.8,.3,1)}
.co-reveal.in{opacity:1;transform:none}
.co-av{width:30px;height:30px;border-radius:50%;color:#fff;font-size:.64rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0}
/* pillars */
.co-pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:48px}
.co-pillar{background:#fff;border:1px solid var(--line);border-radius:20px;padding:30px;box-shadow:var(--shadow-sm);transition:transform .25s,box-shadow .25s,border-color .25s}
.co-pillar:hover{transform:translateY(-5px);box-shadow:var(--shadow-md);border-color:var(--accent-light)}
.co-pillar .pi{width:54px;height:54px;border-radius:15px;background:var(--accent-soft);color:var(--accent-dark);display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.co-pillar .pi svg{width:27px;height:27px}
.co-pillar h3{font-size:1.18rem;letter-spacing:-0.02em}
.co-pillar p{color:var(--muted);font-size:.95rem;line-height:1.55;margin-top:9px}
@media(max-width:860px){.co-pillars{grid-template-columns:1fr}}
/* roadmap board */
.co-board{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:46px}
.co-col-h{display:flex;align-items:center;gap:8px;font-size:.74rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:#9aa6bd;margin-bottom:12px;padding:0 4px}
.co-col-h .dotc{width:8px;height:8px;border-radius:50%}
.co-rcard{background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:14px;margin-bottom:10px}
.co-rcard b{font-size:.86rem;color:#fff;display:block;line-height:1.35}
.co-rcard .up{display:inline-flex;align-items:center;gap:6px;margin-top:10px;font-size:.72rem;font-weight:700;color:#9ec0ff;background:rgba(125,169,255,.14);border:1px solid rgba(125,169,255,.25);border-radius:999px;padding:4px 10px}
.co-rcard .up.done{color:#34d399;background:rgba(52,211,153,.14);border-color:rgba(52,211,153,.3)}
@media(max-width:860px){.co-board{grid-template-columns:1fr 1fr}}
/* usecase cards */
.co-uc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:46px}
.co-uccard{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:var(--shadow-sm);display:flex;flex-direction:column;transition:transform .22s,box-shadow .22s,border-color .22s}
.co-uccard:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--accent-light)}
.co-uccard .cat{align-self:flex-start;font-size:.64rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--accent-dark);background:var(--accent-soft);border-radius:999px;padding:4px 10px}
.co-uccard h3{font-size:1.05rem;letter-spacing:-0.01em;margin:13px 0 0}
.co-uccard p{font-size:.86rem;color:var(--muted-2);line-height:1.5;margin:8px 0 16px}
.co-uccard .meta{display:flex;align-items:center;gap:9px;margin-top:auto;padding-top:14px;border-top:1px solid var(--line)}
.co-uccard .meta .nm{font-size:.78rem;font-weight:600}
.co-uccard .meta .uses{margin-left:auto;font-size:.74rem;color:var(--muted-2);font-weight:600;display:inline-flex;align-items:center;gap:5px}
@media(max-width:860px){.co-uc-grid{grid-template-columns:1fr}}
/* testimonials */
.co-quotes{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:46px}
.co-quote{background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px;box-shadow:var(--shadow-sm)}
.co-quote .stars{color:#f5b301;font-size:.95rem;letter-spacing:2px}
.co-quote p{font-size:1rem;line-height:1.55;margin:14px 0 18px;color:var(--text)}
.co-quote .by{display:flex;align-items:center;gap:11px}
.co-quote .by .nm{font-size:.86rem;font-weight:700}
.co-quote .by .ro{font-size:.76rem;color:var(--muted-2)}
@media(max-width:860px){.co-quotes{grid-template-columns:1fr}}
/* join channels + stats */
.co-channels{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:46px}
.co-ch{display:flex;flex-direction:column;gap:10px;background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:22px;transition:transform .22s,border-color .22s}
.co-ch:hover{transform:translateY(-4px);border-color:rgba(125,169,255,.4)}
.co-ch .ci{width:46px;height:46px;border-radius:13px;background:rgba(125,169,255,.16);color:#9ec7ff;display:flex;align-items:center;justify-content:center}
.co-ch .ci svg{width:24px;height:24px}
.co-ch b{font-size:.98rem;color:#fff}
.co-ch span{font-size:.8rem;color:#9aa6bd;line-height:1.45}
.co-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:30px;padding-top:34px;border-top:1px solid rgba(255,255,255,.1)}
.co-stat{text-align:center}
.co-stat b{font-size:clamp(1.8rem,3.4vw,2.5rem);font-weight:700;letter-spacing:-0.04em;background:linear-gradient(135deg,#e6efff,#5b8def);-webkit-background-clip:text;background-clip:text;color:transparent;display:block}
.co-stat span{font-size:.8rem;color:#9aa6bd;margin-top:5px;display:block}
.co-join-cta{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:38px}
@media(max-width:860px){.co-channels{grid-template-columns:1fr 1fr}.co-stats{grid-template-columns:1fr 1fr}}
</style>'''

AV=['#2563eb,#1d4ed8','#0ea5e9,#2563eb','#6366f1,#1d4ed8','#0891b2,#2563eb','#7c3aed,#4f46e5','#0d9488,#2563eb']
def av(initials,i): return '<span class="co-av" style="background:linear-gradient(135deg,%s)">%s</span>'%(AV[i%len(AV)],initials)

# SEC1 vision
pillars=[('Mitbestimmen','&Uuml;ber neue Features abstimmen und die Roadmap aktiv mitgestalten &ndash; eure Stimme z&auml;hlt.',svg('<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>')),
 ('Praxis teilen','Eure besten Workflows, Prompts und Vorlagen mit der Community teilen.',svg('<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/>')),
 ('Gemeinschaft','Euch vernetzen, voneinander lernen und gemeinsam wachsen.',svg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/>'))]
sec1=('<section class="co-sec"><div class="co-wrap co-center co-reveal">'
 '<span class="eyebrow"><span class="dot"></span>Community</span>'
 '<h2 class="co-h2">Features von der Community f&uuml;r die <span class="serif">Community</span>.</h2>'
 '<p class="co-sub">Unsere Vision: ein offenes &Ouml;kosystem, in dem die Community die Entwicklung von Relationflow mitbestimmt, echte Use Cases aus der Praxis teilt und gemeinsam eine starke Gemeinschaft aufbaut.</p></div>'
 '<div class="co-wrap"><div class="co-pillars co-reveal">'
 +''.join('<div class="co-pillar"><div class="pi">%s</div><h3>%s</h3><p>%s</p></div>'%(ic,t,d) for t,d,ic in pillars)
 +'</div></div></section>')

# SEC2 roadmap (dark)
cols=[('Vorgeschlagen','#7da9ff',[('Excel-Export f&uuml;r Reports','248'),('Outlook-Add-in','191')]),
      ('Geplant','#a78bfa',[('Sprachdiktat im Chat','412'),('Team-Analytics','305')]),
      ('In Arbeit','#fbbf24',[('Mobile App','587'),('&Ouml;ffentliche API v2','364')]),
      ('Live','#34d399',[('BYOM Fine-Tuning','done'),('Audit-Export','done')])]
def rcard(title,votes):
    if votes=='done':
        return '<div class="co-rcard"><b>%s</b><span class="up done">&#10003; Live</span></div>'%title
    return '<div class="co-rcard"><b>%s</b><span class="up">&#9650; %s</span></div>'%(title,votes)
board=''.join('<div class="co-col"><div class="co-col-h"><span class="dotc" style="background:%s"></span>%s</div>%s</div>'%(c,name,''.join(rcard(t,v) for t,v in cards)) for name,c,cards in cols)
sec2=('<section class="co-dark"><div class="co-wrap">'
 '<div class="co-center co-reveal"><span class="eyebrow"><span class="dot"></span>Open Roadmap</span>'
 '<h2 class="co-h2">Ihr entscheidet, was als <span class="serif">N&auml;chstes</span> kommt.</h2>'
 '<p class="co-sub">Schlagt Features vor, stimmt ab und verfolgt live, woran wir arbeiten. Die meistgew&uuml;nschten Ideen kommen zuerst.</p></div>'
 '<div class="co-board co-reveal">'+board+'</div></div></section>')

# SEC3 use-case library
ucs=[('Vertrieb','Angebots-Generator','Aus Gespr&auml;chsnotizen ein fertiges Angebot &ndash; in Minuten.','SK','1.240'),
     ('Recht','DSGVO-Vertragscheck','Vertr&auml;ge automatisch auf kritische Klauseln pr&uuml;fen.','TM','980'),
     ('Marketing','Social-Content-Kalender','Wochenplan inkl. Captions in eurer Markenstimme.','JR','1.530'),
     ('HR','Onboarding-Assistent','Individuelle Einarbeitungspl&auml;ne auf Knopfdruck.','LB','760'),
     ('IT','Incident-Analyse','Logs analysieren und Ursachen vorschlagen lassen.','FK','540'),
     ('Operations','Rechnungs-Extraktor','Daten aus Rechnungen ziehen und pr&uuml;fen.','NV','1.100')]
uccards=''.join('<div class="co-uccard"><span class="cat">%s</span><h3>%s</h3><p>%s</p><div class="meta">%s<span class="nm">%s</span><span class="uses">&#9889; %s Nutzungen</span></div></div>'%(cat,t,d,av(au,i),au,uses) for i,(cat,t,d,au,uses) in enumerate(ucs))
sec3=('<section class="co-sec"><div class="co-wrap co-center co-reveal">'
 '<span class="eyebrow"><span class="dot"></span>Use-Case-Bibliothek</span>'
 '<h2 class="co-h2">Echte Use Cases aus der <span class="serif">Praxis</span>.</h2>'
 '<p class="co-sub">Von der Community geteilt, sofort einsatzbereit: bew&auml;hrte Vorlagen und Workflows, die wirklich funktionieren.</p></div>'
 '<div class="co-wrap"><div class="co-uc-grid co-reveal">'+uccards+'</div></div></section>')

# SEC4 testimonials
quotes=[('&bdquo;Endlich ein Tool, das mit uns w&auml;chst. Unser Feature-Vorschlag war sechs Wochen sp&auml;ter live.&ldquo;','Lena Brandt','Vertriebsleitung','LB'),
        ('&bdquo;Die geteilten Vorlagen haben uns Wochen an Arbeit gespart &ndash; ein echter Wissensschatz.&ldquo;','Tom Mahler','IT-Leiter','TM'),
        ('&bdquo;Man sp&uuml;rt, dass hier eine Gemeinschaft steht und nicht nur ein Produkt.&ldquo;','Anna Reuter','Head of Marketing','AR')]
qcards=''.join('<div class="co-quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>%s</p><div class="by">%s<div><div class="nm">%s</div><div class="ro">%s</div></div></div></div>'%(q,av(ini,i+1),nm,ro) for i,(q,nm,ro,ini) in enumerate(quotes))
sec4=('<section class="co-sec alt"><div class="co-wrap co-center co-reveal">'
 '<span class="eyebrow"><span class="dot"></span>Stimmen aus der Community</span>'
 '<h2 class="co-h2">Was die Community <span class="serif">sagt</span>.</h2></div>'
 '<div class="co-wrap"><div class="co-quotes co-reveal">'+qcards+'</div></div></section>')

# SEC5 join (dark)
chans=[('Community-Forum','Fragen stellen, Antworten finden, mitdiskutieren.',svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>')),
       ('Discord-Server','Im Austausch mit anderen Teams &ndash; in Echtzeit.',svg('<circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><path d="M7.5 7.5C9 7 10.5 7 12 7s3 0 4.5 .5c2 4 2 7 1.5 9.5-1 .8-2.3 1.3-3.5 1.5l-1-2M7.5 7.5C5.5 11.5 5.5 14.5 6 17c1 .8 2.3 1.3 3.5 1.5l1-2"/>')),
       ('Meetups &amp; Webinare','Live lernen, Best Practices teilen, netzwerken.',svg('<rect x="2" y="5" width="14" height="14" rx="2"/><path d="M22 8l-6 4 6 4z"/>')),
       ('Open Roadmap','Abstimmen und live verfolgen, was als N&auml;chstes kommt.',svg('<path d="M9 18l6-6-6-6"/><circle cx="5" cy="12" r="1.5"/>'))]
chancards=''.join('<div class="co-ch"><div class="ci">%s</div><b>%s</b><span>%s</span></div>'%(ic,t,d) for t,d,ic in chans)
stats=[('8500','+','Community-Mitglieder'),('1200','+','geteilte Vorlagen'),('340','','umgesetzte Ideen'),('52','','Events pro Jahr')]
statcards=''.join('<div class="co-stat"><b><span class="co-count" data-to="%s">0</span>%s</b><span>%s</span></div>'%(v,suf,l) for v,suf,l in stats)
sec5=('<section class="co-dark"><div class="co-wrap">'
 '<div class="co-center co-reveal"><span class="eyebrow"><span class="dot"></span>Mitmachen</span>'
 '<h2 class="co-h2">Werde Teil der <span class="serif">Community</span>.</h2>'
 '<p class="co-sub">Gestalte mit, lerne von anderen und bring deine Use Cases ein. Der Zugang ist offen f&uuml;r alle.</p></div>'
 '<div class="co-channels co-reveal">'+chancards+'</div>'
 '<div class="co-stats co-reveal">'+statcards+'</div>'
 '<div class="co-join-cta co-reveal"><a href="#" class="btn btn-primary">Community beitreten</a><a href="#" class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.25)">Roadmap ansehen</a></div>'
 '</div></section>')

JS = '''<script>
(function(){
 var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target);}})},{threshold:.12});
 document.querySelectorAll('.co-reveal').forEach(function(el){ro.observe(el);});
 var seen=new WeakSet();
 function cnt(el){var to=parseInt(el.dataset.to,10),t0=null;requestAnimationFrame(function go(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1500,1);el.textContent=Math.floor((1-Math.pow(1-p,3))*to).toLocaleString('de-DE');if(p<1)requestAnimationFrame(go);else el.textContent=to.toLocaleString('de-DE');});}
 var co=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!seen.has(e.target)){seen.add(e.target);cnt(e.target);}})},{threshold:.4});
 document.querySelectorAll('.co-count').forEach(function(el){co.observe(el);});
})();
</script>'''

block=CSS+sec1+sec2+sec3+sec4+sec5+JS
assert s.count('<section><div class="cta-band">')==1
s=s.replace('<section><div class="cta-band">', block+'<section><div class="cta-band">',1)
open(f,'w').write(s)
print('co-sec:',s.count('class="co-sec"'),'co-dark:',s.count('class="co-dark"'),'pillars:',s.count('co-pillar"'),'uccards:',s.count('co-uccard'),'quotes:',s.count('class="co-quote"'),'channels:',s.count('class="co-ch"'))
print('div',s.count('<div'),s.count('</div>'),'sec',len(re.findall(r'<section',s)),s.count('</section>'),'style',s.count('<style>'),s.count('</style>'),'script',s.count('<script>'),s.count('</script>'))
