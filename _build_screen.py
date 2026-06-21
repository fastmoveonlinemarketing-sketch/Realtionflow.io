# -*- coding: utf-8 -*-
import re
f='relationflow_anwendungsfaelle.html'
s=open(f).read()

def sg(p,w=2): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>'%(w,p)
brain='<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 3A2.5 2.5 0 0 0 7 5.5 2.5 2.5 0 0 0 5 8a2.5 2.5 0 0 0 0 4 2.5 2.5 0 0 0 1 4.5A2.5 2.5 0 0 0 9.5 21 1.5 1.5 0 0 0 11 19.5V4.5A1.5 1.5 0 0 0 9.5 3z"/><path d="M14.5 3A2.5 2.5 0 0 1 17 5.5 2.5 2.5 0 0 1 19 8a2.5 2.5 0 0 1 0 4 2.5 2.5 0 0 1-1 4.5A2.5 2.5 0 0 1 14.5 21 1.5 1.5 0 0 1 13 19.5V4.5A1.5 1.5 0 0 1 14.5 3z"/></svg>'
side_icons=[sg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
 sg('<rect x="4" y="7" width="16" height="12" rx="3"/><path d="M12 7V4M9 13h.01M15 13h.01"/>'),
 sg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'),
 sg('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5z"/>'),
 sg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>')]
side='<aside class="ds-side">'+''.join('<span class="si%s">%s</span>'%(' on' if i==0 else '',ic) for i,ic in enumerate(side_icons))+'</aside>'
models=('<div class="ds-models">'
 '<span class="mc" data-m="gpt"><i style="background:#10a37f"></i>GPT-4o</span>'
 '<span class="mc on" data-m="claude"><i style="background:#d97757"></i>Claude</span>'
 '<span class="mc" data-m="gemini"><i style="background:#4285f4"></i>Gemini</span>'
 '<span class="mc" data-m="mistral"><i style="background:#ff7000"></i>Mistral</span></div>')
lock=sg('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')

MARKUP=('<div class="ds-stage"><div class="ds-glow"></div>'
 '<div class="dept-screen" id="deptScreen">'
 '<div class="ds-top"><span class="tl"><i class="dr"></i><i class="dy"></i><i class="dg"></i></span>'
 '<span class="ds-url">'+lock+'app.relationflow.io &middot; <b id="dsDept">Vertrieb &amp; Sales</b></span>'
 '<span class="ds-avs"><i class="a1">SK</i><i class="a2">MV</i><i class="a3">JR</i></span>'
 '<span class="ds-live">Live</span></div>'
 '<div class="ds-main">'+side+
 '<div class="ds-chat">'+models+
 '<div class="ds-msg u"><div class="ds-bub" id="dsPrompt"></div><span class="ds-uav">DU</span></div>'
 '<div class="ds-msg a"><span class="ds-aav">'+brain+'</span><div class="ds-acol">'
 '<div class="ds-nm">Relationflow <span class="ds-badge"><i></i><b id="dsModel">Claude</b> &middot; auto</span></div>'
 '<div class="ds-bub a" id="dsAnswer"></div><div class="ds-tools" id="dsTools"></div><div class="ds-src" id="dsSrc"></div>'
 '</div></div></div></div></div>'
 '<div class="ds-fl ds-fl1"><span class="fi">&#10003;</span>DSGVO-konform</div>'
 '<div class="ds-fl ds-fl2"><span class="fi spark">&#9889;</span><b id="dsFloat">&minus;85% Zeit</b></div>'
 '</div>')

CSS='<style>'+''.join([
'.ds-stage{position:relative;width:min(640px,100%);margin:38px auto 0}',
'.ds-glow{position:absolute;inset:-14% -8% -20%;z-index:0;background:radial-gradient(50% 50% at 50% 38%,rgba(37,99,235,.4),transparent 70%);filter:blur(48px);opacity:.7;animation:dsGlow 6s ease-in-out infinite alternate}',
'@keyframes dsGlow{to{opacity:1;transform:scale(1.06)}}',
'.dept-screen{position:relative;z-index:2;border-radius:22px;background:linear-gradient(180deg,#ffffff,#f7f9ff);border:1px solid var(--line);box-shadow:0 46px 104px -34px rgba(25,38,90,.5),0 10px 28px -14px rgba(25,38,90,.2);overflow:hidden;text-align:left}',
'.dept-screen::before{content:"";position:absolute;left:0;right:0;top:0;height:2px;z-index:5;background:linear-gradient(90deg,#10a37f,#2563eb,#d97757,#ff7000)}',
'.ds-top{display:flex;align-items:center;gap:9px;padding:12px 15px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,#fbfcfe,#f4f6fb)}',
'.ds-top .tl{display:flex;gap:6px}.ds-top .tl i{width:11px;height:11px;border-radius:50%}.ds-top .dr{background:#ff5f57}.ds-top .dy{background:#febc2e}.ds-top .dg{background:#28c840}',
'.ds-url{display:flex;align-items:center;gap:7px;margin-left:6px;font-size:.74rem;color:var(--muted-2);font-weight:600;background:#fff;border:1px solid var(--line);border-radius:8px;padding:5px 11px;white-space:nowrap;overflow:hidden}',
'.ds-url svg{width:12px;height:12px;color:#16a34a;flex-shrink:0}.ds-url b{color:var(--text)}',
'.ds-avs{margin-left:auto;display:flex}',
'.ds-avs i{width:24px;height:24px;border-radius:50%;border:2px solid #fff;margin-left:-7px;font-size:.56rem;font-weight:700;color:#fff;display:flex;align-items:center;justify-content:center;font-style:normal}',
'.ds-avs .a1{background:linear-gradient(135deg,#5b8def,#1d4ed8)}.ds-avs .a2{background:linear-gradient(135deg,#f0883e,#d9622b)}.ds-avs .a3{background:linear-gradient(135deg,#3aa0f0,#2b6dd9)}',
'.ds-live{font-size:.62rem;font-weight:700;color:#16a34a;display:flex;align-items:center;gap:5px;flex-shrink:0}',
'.ds-live::before{content:"";width:7px;height:7px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 3px rgba(34,197,94,.2);animation:dsPulse 1.6s infinite}',
'@keyframes dsPulse{50%{box-shadow:0 0 0 5px rgba(34,197,94,.04)}}',
'.ds-main{display:grid;grid-template-columns:56px 1fr;height:328px}',
'.ds-side{border-right:1px solid var(--line);background:linear-gradient(180deg,#fbfcff,#f3f6fd);display:flex;flex-direction:column;align-items:center;gap:6px;padding:14px 0}',
'.ds-side .si{width:34px;height:34px;border-radius:11px;display:flex;align-items:center;justify-content:center;color:var(--muted-2)}',
'.ds-side .si svg{width:18px;height:18px}.ds-side .si.on{background:var(--accent-soft);color:var(--accent-dark)}',
'.ds-chat{padding:16px 18px;display:flex;flex-direction:column;gap:11px;overflow:hidden}',
'.ds-models{display:flex;gap:7px;flex-wrap:wrap}',
'.ds-models .mc{display:inline-flex;align-items:center;gap:6px;font-size:.68rem;font-weight:700;color:var(--muted-2);background:#fff;border:1px solid var(--line);border-radius:999px;padding:5px 11px;transition:all .25s}',
'.ds-models .mc i{width:8px;height:8px;border-radius:50%}',
'.ds-models .mc.on{color:#fff;background:var(--text);border-color:var(--text);box-shadow:0 6px 16px -6px rgba(0,0,0,.4)}',
'.ds-msg{display:flex;gap:10px;align-items:flex-end}.ds-msg.u{justify-content:flex-end}',
'.ds-uav{width:28px;height:28px;border-radius:9px;background:linear-gradient(135deg,#5b8def,#1d4ed8);color:#fff;font-size:.6rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0}',
'.ds-aav{width:30px;height:30px;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent-dark));display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 8px 18px -8px rgba(37,99,235,.7)}.ds-aav svg{width:17px;height:17px}',
'.ds-bub{font-size:.86rem;line-height:1.5;padding:11px 14px;border-radius:14px;max-width:84%}',
'.ds-msg.u .ds-bub{background:linear-gradient(135deg,var(--accent),var(--accent-dark));color:#fff;border-bottom-right-radius:5px;box-shadow:0 10px 24px -12px rgba(37,99,235,.7)}',
'.ds-acol{display:flex;flex-direction:column;gap:7px;max-width:88%}',
'.ds-nm{font-size:.62rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted-2);font-weight:700;display:flex;align-items:center;gap:8px}',
'.ds-badge{display:inline-flex;align-items:center;gap:5px;text-transform:none;letter-spacing:0;color:var(--accent-dark);background:var(--accent-soft);border:1px solid var(--accent-soft-2);border-radius:999px;padding:2px 8px;font-size:.62rem;font-weight:700}',
'.ds-badge i{width:6px;height:6px;border-radius:50%;background:var(--accent)}',
'.ds-bub.a{background:var(--bg-alt);border:1px solid var(--line);border-bottom-left-radius:5px;color:var(--text)}',
'.ds-cur{display:inline-block;width:2px;height:1em;background:var(--accent);vertical-align:-2px;margin-left:1px;animation:dsBlink .8s step-end infinite}',
'@keyframes dsBlink{50%{opacity:0}}',
'.ds-tools{display:flex;gap:6px;flex-wrap:wrap}',
'.ds-tools .tch{font-size:.64rem;font-weight:600;color:var(--accent-dark);background:#fff;border:1px solid var(--accent-soft-2);border-radius:999px;padding:4px 9px;opacity:0;transform:translateY(5px);transition:all .35s}',
'.ds-tools .tch.show{opacity:1;transform:none}',
'.ds-src{display:flex;gap:6px;flex-wrap:wrap}',
'.ds-src span{font-size:.6rem;font-weight:600;color:var(--muted-2);background:var(--bg-alt);border:1px solid var(--line);border-radius:999px;padding:3px 8px}',
'.ds-fl{position:absolute;z-index:6;display:flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--line);border-radius:13px;box-shadow:0 18px 40px -16px rgba(25,38,90,.45);padding:9px 13px;font-size:.76rem;font-weight:700;color:var(--text)}',
'.ds-fl .fi{width:22px;height:22px;border-radius:7px;background:#dcf7e6;color:#16a34a;display:flex;align-items:center;justify-content:center;font-size:.7rem}',
'.ds-fl .fi.spark{background:var(--accent-soft);color:var(--accent-dark)}',
'.ds-fl1{top:15%;right:-16px;animation:dsBob 5s ease-in-out infinite}',
'.ds-fl2{bottom:12%;left:-18px;animation:dsBob 5.6s ease-in-out infinite .4s}',
'@keyframes dsBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}',
'@media(max-width:600px){.ds-fl{display:none}.ds-main{grid-template-columns:1fr;height:auto;min-height:310px}.ds-side{display:none}}',
'@media(prefers-reduced-motion:reduce){.ds-glow,.ds-fl,.ds-live::before{animation:none}}',
])+'</style>'

JS=('var _dt0=document.getElementById("deptTabs");'
 'var _EX={'
 'sales:{n:"Vertrieb & Sales",m:"claude",mn:"Claude",p:"Erstelle ein Angebot für die Müller GmbH aus dem Call-Protokoll.",a:"Angebot erstellt — inkl. Mengenrabatt, AGB und Gültigkeit. Soll ich es als PDF senden?",tools:["🔎 Wissensbasis","🧮 Angebots-Tool","✓ CRM-Sync"],s:["Protokoll_Müller.pdf","Preisliste 2026"],metric:"−85% Zeit"},'
 'mkt:{n:"Marketing & Content",m:"gpt",mn:"GPT-4o",p:"Schreib 3 LinkedIn-Posts zum Launch unseres DSGVO-Features.",a:"3 Varianten in eurer Tonalität — Hook, Nutzen, CTA. Soll ich ein Bildkonzept ergänzen?",tools:["✍️ Marken-Stimme","🔎 SEO-Check","🖼️ Bildkonzept"],s:["Markenstimme","Produkt-Update"],metric:"5× Output"},'
 'support:{n:"Customer Support",m:"claude",mn:"Claude",p:"Kunde meldet Login-Fehler nach dem Update. Was antworten?",a:"Antwort-Entwurf mit Schritt-für-Schritt-Lösung aus eurer Doku. Tonfall: freundlich. Senden?",tools:["📚 Hilfe-Doku","🌐 Übersetzung","✓ Eskalation"],s:["Hilfe-Doku","Ticket #4821"],metric:"−60% AHT"},'
 'ops:{n:"Operations",m:"mistral",mn:"Mistral",p:"Fasse die 12 Lieferanten-Rechnungen zusammen und markiere Abweichungen.",a:"Zusammengefasst: 2 über Budget, 1 doppelt. Tabelle und Audit-Log liegen bereit.",tools:["📄 Extraktion","📊 Report","✓ Audit-Log"],s:["12 Rechnungen","Audit-Log"],metric:"−90% Aufwand"},'
 'it:{n:"IT & Entwicklung",m:"gpt",mn:"GPT-4o",p:"Erkläre diese Legacy-Funktion und schlage Verbesserungen vor.",a:"Zweck, Risiken und 3 Optimierungen analysiert. Soll ich Doku und Tests vorschlagen?",tools:["💻 Code-Analyse","🧪 Tests","📘 Doku"],s:["repo/auth.js","Changelog"],metric:"MTTR ↓"},'
 'hr:{n:"HR & Recruiting",m:"gemini",mn:"Gemini",p:"Erstelle eine Stellenanzeige für eine:n Senior Buchhalter:in.",a:"Anzeige erstellt — inkl. Benefits, inklusiver Sprache und SEO. Interview-Leitfaden dazu?",tools:["📋 Rollen-Vorlage","⚖️ Bias-Check","✓ DSGVO"],s:["Rollen-Vorlage","Benefits"],metric:"−80% Zeit"}};'
 'var _dsP=document.getElementById("dsPrompt"),_dsA=document.getElementById("dsAnswer"),_dsD=document.getElementById("dsDept"),_dsS=document.getElementById("dsSrc"),_dsModel=document.getElementById("dsModel"),_dsTools=document.getElementById("dsTools"),_dsFloat=document.getElementById("dsFloat"),_typeT=null;'
 'function _screen(k){var e=_EX[k];if(!e||!_dsP)return;if(_typeT){clearTimeout(_typeT);_typeT=null;}'
 '_dsD.textContent=e.n;_dsP.textContent=e.p;if(_dsModel)_dsModel.textContent=e.mn;if(_dsFloat)_dsFloat.textContent=e.metric;'
 'var sc=document.getElementById("deptScreen");if(sc)sc.querySelectorAll(".mc").forEach(function(c){c.classList.toggle("on",c.dataset.m===e.m)});'
 '_dsTools.innerHTML="";_dsS.innerHTML="";_dsA.innerHTML="";var cur=document.createElement("span");cur.className="ds-cur";_dsA.appendChild(cur);var i=0;'
 '(function tp(){if(i<e.a.length){cur.insertAdjacentText("beforebegin",e.a.charAt(i));i++;_typeT=setTimeout(tp,16);}else{cur.remove();'
 '_dsTools.innerHTML=e.tools.map(function(x){return "<span class=\\"tch\\">"+x+"</span>";}).join("");'
 '[].forEach.call(_dsTools.children,function(ch,ix){setTimeout(function(){ch.classList.add("show")},120+ix*150);});'
 '_dsS.innerHTML=e.s.map(function(x){return "<span>"+x+"</span>";}).join("");}})();}'
 'if(_dsP){var _sk=["sales","mkt","support","ops","it","hr"],_si=0,_st=null,_sseen=false;function _sgo(){_si=(_si+1)%_sk.length;_screen(_sk[_si]);}_screen("sales");var _sw=document.getElementById("deptScreen");if("IntersectionObserver" in window&&_sw){var _sio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!_sseen){_sseen=true;_st=setInterval(_sgo,5200);}})},{threshold:.3});_sio.observe(_sw);}else{_st=setInterval(_sgo,5200);}}'
 'if(_dt0){var _tb=[].slice.call(_dt0.querySelectorAll(".tab")),_ti=0,_tt=null,_tstop=false;function _setTab(b){_dt0.querySelectorAll(".tab").forEach(function(x){x.classList.toggle("active",x===b)});var d=b.dataset.tab;document.querySelectorAll(".dept-panel").forEach(function(p){p.classList.toggle("active",p.dataset.panel===d)});}_dt0.addEventListener("click",function(e){var b=e.target.closest(".tab");if(!b)return;_tstop=true;if(_tt){clearInterval(_tt);_tt=null;}_setTab(b);});function _tgo(){_ti=(_ti+1)%_tb.length;_setTab(_tb[_ti]);}function _tstart(){if(!_tstop&&!_tt&&_tb.length)_tt=setInterval(_tgo,3500);}if("IntersectionObserver" in window){var _tio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)_tstart();})},{threshold:.2});_tio.observe(_dt0);}else{_tstart();}}')

# replace old markup
s=re.sub(r'<div class="ds-stage">.*?id="dsFloat">.*?</div></div>', MARKUP, s, count=1, flags=re.S) if '<div class="ds-stage">' in s else re.sub(r'<div class="dept-screen" id="deptScreen">.*?id="dsSrc"></div></div></div></div></div>', MARKUP, s, count=1, flags=re.S)
# replace old CSS block
s=re.sub(r'<style>\.dept-screen\{.*?</style>', CSS, s, count=1, flags=re.S)
# replace old JS
s=re.sub(r'var _dt0=document\.getElementById\([\'\"]deptTabs[\'\"]\);var _EX=.*?else\{_tstart\(\);\}\}', JS, s, count=1, flags=re.S)

open(f,'w').write(s)
print('stage:',s.count('ds-stage'),'mc chips:',s.count('class="mc"')+s.count('class="mc on"'),'tools id:',s.count('id="dsTools"'),'float:',s.count('id="dsFloat"'))
print('div',s.count('<div'),s.count('</div>'),'style',s.count('<style>'),s.count('</style>'),'script',s.count('<script>'),s.count('</script>'))
