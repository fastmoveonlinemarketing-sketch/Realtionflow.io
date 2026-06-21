# -*- coding: utf-8 -*-
import re
f='relationflow_anwendungsfaelle.html'; s=open(f).read()
def sv(p): return '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'
I={
 'doc':sv('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>'),
 'search':sv('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>'),
 'mail':sv('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/>'),
 'chat':sv('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
 'chart':sv('<path d="M3 3v18h18M7 15l4-4 3 3 5-6"/>'),
 'shield':sv('<path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z"/>'),
 'clock':sv('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 'list':sv('<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>'),
 'globe':sv('<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>'),
 'check':sv('<path d="M9 11l3 3L22 4M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>'),
 'scale':sv('<path d="M12 3v18M7 21h10M5 7h14M5 7l-2.5 6a3 3 0 0 0 5 0L5 7zm14 0l-2.5 6a3 3 0 0 0 5 0L19 7z"/>'),
 'file2':sv('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 15l2 2 4-4"/>'),
 'cal':sv('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M3 10h18M8 2v4M16 2v4"/>'),
 'cart':sv('<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>'),
 'heart':sv('<path d="M3 12h4l2 5 4-10 2 5h6"/>'),
 'box':sv('<path d="M21 16V8a2 2 0 0 0-1-1.7l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.7l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.3 7L12 12l8.7-5"/>'),
 'bank':sv('<path d="M3 21h18M5 10h14M12 3l8 5H4l8-5zM6 10v8M10 10v8M14 10v8M18 10v8"/>'),
 'people':sv('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/>'),
}
TABS=[('recht','Recht',I['scale']),('medizin','Medizin',I['heart']),('finanz','Finanz',I['bank']),('industrie','Industrie',I['box']),('handel','Handel',I['cart']),('verwaltung','Verwaltung',sv('<path d="M3 21h18M4 9h16M12 3l8 4H4l8-4zM7 9v8M11 9v8M15 9v8M19 9v8"/>'))]
DATA={
'recht':[('Vertrags- &amp; Klauselanalyse','Risiken &amp; kritische Klauseln automatisch markieren.','scale'),('Schriftsatz-Entw&uuml;rfe','Erste Entw&uuml;rfe aus Akten &amp; Vorgaben.','doc'),('Mandanten-FAQ','H&auml;ufige Fragen rechtssicher beantworten.','chat'),('Rechts-Recherche','Mit Quellenangaben recherchieren.','search'),('Aktenzusammenfassung','Umfangreiche Akten in Minuten.','list'),('Fristen im Blick','Termine &amp; Fristen automatisch erfassen.','clock'),('Vertragsvorlagen','Standardvertr&auml;ge vorbereiten lassen.','file2'),('DSGVO-Pr&uuml;fung','Dokumente auf Datenschutz pr&uuml;fen.','shield'),('Rechnungstexte','Leistungen sauber formulieren.','mail')],
'medizin':[('Arztbrief-Entw&uuml;rfe','Befunde in strukturierte Briefe.','doc'),('Anamnese strukturieren','Gespr&auml;chsnotizen sauber ordnen.','list'),('Patienten-Aufkl&auml;rung','Verst&auml;ndliche Infos &amp; Bögen.','chat'),('Abrechnungs-Checks','Leistungen korrekt zuordnen.','check'),('Befund-Zusammenfassung','Lange Berichte komprimiert.','file2'),('Leitlinien-Recherche','Aktuelle Standards finden.','search'),('Terminorganisation','Planung &amp; Erinnerungen.','cal'),('Dokumentationspflicht','L&uuml;ckenlos &amp; revisionssicher.','shield'),('Praxis-FAQ','Patientenfragen automatisch.','chat')],
'finanz':[('Report-Automatisierung','Auswertungen auf Knopfdruck.','chart'),('Compliance-Pr&uuml;fung','Regeln &amp; Vorgaben checken.','shield'),('Markt-Briefings','T&auml;gliche Lage kompakt.','list'),('Kunden-Kommunikation','Mails &amp; Mitteilungen on-brand.','mail'),('Risikoanalysen','Kennzahlen schnell bewerten.','chart'),('Kreditunterlagen','Dokumente vorpr&uuml;fen.','file2'),('Regulatorik-Updates','&Auml;nderungen verst&auml;ndlich erkl&auml;rt.','globe'),('Produktbeschreibungen','Finanzprodukte klar erkl&auml;ren.','doc'),('Quartalsberichte','Zahlen &amp; Texte zusammenf&uuml;hren.','clock')],
'industrie':[('Wartungs-SOPs','Anleitungen automatisch erstellen.','file2'),('Lieferanten-Mails','Bestellungen &amp; Nachfragen.','mail'),('Qualit&auml;ts-Doku','Pr&uuml;fungen sauber dokumentieren.','check'),('Schichtprotokolle','&Uuml;bergaben automatisch.','list'),('Handb&uuml;cher &uuml;bersetzen','Mehrsprachig ohne Agentur.','globe'),('Sicherheits-Unterweisung','Inhalte verst&auml;ndlich aufbereiten.','shield'),('Bestellabwicklung','Daten aus Belegen ziehen.','box'),('Reklamationen','Antworten &amp; Ursachen.','chat'),('Datenbl&auml;tter','Technische Texte erzeugen.','doc')],
'handel':[('Produktbeschreibungen','SEO-Texte im Markenton.','doc'),('Support-Antworten','Schnell &amp; mehrsprachig.','chat'),('Kampagnen-Content','Social, Mail &amp; Ads.','mail'),('Retouren-Analyse','Muster &amp; Gr&uuml;nde erkennen.','chart'),('SEO-Optimierung','Keywords &amp; Meta-Daten.','search'),('Bewertungen auswerten','Feedback zusammenfassen.','list'),('Newsletter','Aus Produktdaten generiert.','mail'),('FAQ pflegen','Hilfeartikel automatisch.','check'),('Sortiments-Ideen','Trends &amp; L&uuml;cken finden.','cart')],
'verwaltung':[('B&uuml;rger-Anfragen','Schnell &amp; korrekt beantworten.','chat'),('Akten-Zusammenfassung','Vorg&auml;nge kompakt erfassen.','list'),('Formular-Hilfe','Antr&auml;ge verst&auml;ndlich erkl&auml;ren.','doc'),('Protokolle','Sitzungen automatisch festhalten.','file2'),('Bescheid-Entw&uuml;rfe','Standardf&auml;lle vorbereiten.','check'),('Mehrsprachige Infos','Inhalte barrierearm &uuml;bersetzen.','globe'),('Wissensdatenbank','Internes Wissen auffindbar.','search'),('Antragsbearbeitung','Daten pr&uuml;fen &amp; ordnen.','shield'),('Sitzungsvorlagen','Unterlagen vorstrukturieren.','cal')]}

tabs=''.join('<button class="tab%s" data-tab="%s">%s%s</button>'%(' active' if i==0 else '',k,ic,n) for i,(k,n,ic) in enumerate(TABS))
panels=''
for i,(k,n,ic) in enumerate(TABS):
    cards=''.join('<div class="uc-card"><span class="uc-ic">%s</span><div><b>%s</b><span>%s</span></div></div>'%(I[ik],t,d) for t,d,ik in DATA[k])
    panels+='<div class="br-panel%s" data-panel="%s"><div class="uc-grid">%s</div></div>'%(' active' if i==0 else '',k,cards)

sec=('<section class="af-sec dept-light" id="branche"><div class="af-wrap">'
 '<div class="af-center" style="margin:0 auto">'
 '<span class="af-ey"><span class="dot"></span>Nach Branche</span>'
 '<h2 class="af-h2">Gemacht f&uuml;r eure <span class="serif">Branche</span>.</h2>'
 '<p class="af-sub">W&auml;hle deine Branche und sieh, was Relationflow dort konkret &uuml;bernimmt &ndash; rechtssicher und DSGVO-konform.</p></div>'
 '<div class="seg-wrap"><div class="seg" id="branchTabs">'+tabs+'</div></div>'+panels+'</div></section>')

CSS='<style>.dept-light .br-panel{display:none}.dept-light .br-panel.active{display:block;animation:fadeUp .5s ease}</style>'
JS='<script>(function(){var _bt=document.getElementById("branchTabs");if(!_bt)return;var _bb=[].slice.call(_bt.querySelectorAll(".tab")),_bi=0,_btt=null,_bstop=false;function _bset(b){_bt.querySelectorAll(".tab").forEach(function(x){x.classList.toggle("active",x===b)});var d=b.dataset.tab;document.querySelectorAll(".br-panel").forEach(function(p){p.classList.toggle("active",p.dataset.panel===d)});}_bt.addEventListener("click",function(e){var b=e.target.closest(".tab");if(!b)return;_bstop=true;if(_btt){clearInterval(_btt);_btt=null;}_bset(b);});function _bgo(){_bi=(_bi+1)%_bb.length;_bset(_bb[_bi]);}function _bstart(){if(!_bstop&&!_btt&&_bb.length)_btt=setInterval(_bgo,3800);}if("IntersectionObserver" in window){var _bio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)_bstart();})},{threshold:.2});_bio.observe(_bt);}else{_bstart();}})();</script>'

pat=re.compile(r'<section\b[^>]*>(?:(?!</section>).)*?Nach Branche(?:(?!</section>).)*?</section>', re.S)
s2,n=pat.subn(sec, s)
print('Nach Branche replaced:',n)
s=s2
s=s.replace('</head>', CSS+'</head>',1)
s=s.replace('</body>', JS+'</body>',1)
open(f,'w').write(s)
print('branchTabs:',s.count('id="branchTabs"'),'br-panels:',s.count('class="br-panel'),'cards:',s.count('class="uc-card"'))
import re as r;print('div',s.count('<div'),s.count('</div>'),'sec',len(r.findall(r'<section',s)),s.count('</section>'),'script',s.count('<script>'),s.count('</script>'))
