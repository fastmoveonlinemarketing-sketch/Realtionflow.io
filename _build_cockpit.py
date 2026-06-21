import re
src=open('relationflow_feature_agents.html').read()
ctrcss=open('/tmp/ctrcss2.txt').read().strip()
ctrsec=open('/tmp/ctrsec2.txt').read().strip()
# normalize section: remove reduced padding inline style for the subpage
ctrsec=ctrsec.replace(' style="padding-top:clamp(20px,3vw,44px)"','')

def svg(p): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'

cards=[
 (svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),'Echtzeit-Übersicht','Auslastung, Anfragen und Modelle live im Blick.'),
 (svg('<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>'),'Modell-Steuerung','Aktive Modelle pro Team verwalten &ndash; alle EU-gehostet.'),
 (svg('<path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/>'),'Verbrauch &amp; Kosten','Token, Latenz und Kosten transparent pro Space.'),
 (svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),'Compliance-Status','DSGVO-, EU- und Audit-Status auf einen Blick.'),
 (svg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'),'Agenten-Aktivität','Was jeder Agent gerade tut &ndash; in Echtzeit.'),
 (svg('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5z"/>'),'Audit-Log','Jede Aktion versioniert und revisionssicher.'),
]
grid_cards=''.join(f'<div class="uc"><span class="ic">{ic}</span><div><b>{t}</b><p>{p}</p></div></div>' for ic,t,p in cards)

hero='<section class="uc-hero"><div class="wrap"><span class="eyebrow"><span class="dot"></span>KI-Cockpit</span><h1>Alles im <span class="serif">Blick</span>. Alles im Griff.</h1><p class="lead">Das KI-Cockpit bündelt Modelle, Agenten, Verbrauch und Compliance in einer Live-Ansicht &ndash; volle Kontrolle über euren KI-Workspace, in Echtzeit.</p><div class="uc-cta"><a href="#" class="btn btn-primary">Kostenlos starten</a><a href="#" class="btn btn-ghost">Demo buchen</a></div><div class="stats"><div class="stat"><div class="n">1</div><div class="l">zentrale Ansicht</div><div class="s">für alles</div></div><div class="stat"><div class="n">Live</div><div class="l">Echtzeit-Daten</div><div class="s">Sekundentakt</div></div><div class="stat"><div class="n">100%</div><div class="l">Audit-fähig</div><div class="s">revisionssicher</div></div></div></div></section>'

sec1='<section class="section"><div class="wrap"><div class="sec-center"><span class="eyebrow"><span class="dot"></span>Kernfunktionen</span><h2 style="margin-top:18px">Was das KI-Cockpit <span class="serif">kann</span>.</h2></div><div class="ucg">'+grid_cards+'</div></div></section>'

# section 2 = Kontrollzentrum (live cockpit visual)
sec2='<section class="section">'+ctrsec+'</section>'

faq='<section class="section"><div class="wrap"><div class="sec-center"><span class="eyebrow"><span class="dot"></span>Häufige Fragen</span><h2 style="margin-top:18px">Fragen zum KI-Cockpit.</h2></div><div class="faq-list" id="faqList"><div class="faq-item"><div class="faq-q"><span class="num">01</span> Welche Daten zeigt das Cockpit?<span class="pm">+</span></div><div class="faq-a"><div>Auslastung, Anfragen pro Woche, aktive Modelle, Verbrauch sowie Compliance- und Audit-Status &ndash; alles in Echtzeit.</div></div></div><div class="faq-item"><div class="faq-q"><span class="num">02</span> Kann ich Modelle direkt steuern?<span class="pm">+</span></div><div class="faq-a"><div>Ja. Pro Team und Space legt ihr fest, welche Modelle aktiv und erlaubt sind &ndash; ausschließlich EU-gehostet.</div></div></div><div class="faq-item"><div class="faq-q"><span class="num">03</span> Ist das Cockpit auditierbar?<span class="pm">+</span></div><div class="faq-a"><div>Jede Aktion wird versioniert und im Audit-Log protokolliert &ndash; revisionssicher und DSGVO-konform.</div></div></div></div></div></section>'

cta='<section><div class="cta-band"><div class="wrap"><h2>Bereit, euer KI-Cockpit <span class="serif">live</span> zu sehen?</h2><p>Starte kostenlos &ndash; ohne Kreditkarte. Oder buche eine Demo an euren eigenen Prozessen.</p><div class="cta-cta"><a href="#" class="btn btn-light">Kostenlos starten</a><a href="#" class="btn btn-outline-light">Demo buchen</a></div></div></div></section>'

body=hero+sec1+sec2+faq+cta

s=src
s=re.sub(r'<title>.*?</title>','<title>KI-Cockpit – relationflow.io</title>',s,1)
s=re.sub(r'(<meta name="description" content=").*?(")',r'\1Das KI-Cockpit von Relationflow: Modelle, Agenten, Verbrauch und Compliance in einer Live-Ansicht. DSGVO-konform und auditierbar.\2',s,1)
s=s.replace('</style></head>','\n/* ===== KI-Cockpit (Kontrollzentrum) ===== */\n'+ctrcss+'\n</style></head>',1)
s=re.sub(r'<section class="uc-hero">.*?(?=<footer)', body, s, count=1, flags=re.S)
open('relationflow_feature_cockpit.html','w').write(s)
print('sec',s.count('</section>'),len(re.findall(r'<section',s)),'div',s.count('<div'),s.count('</div>'),'ctr',s.count('class="ctr '),'vblink',s.count('@keyframes vblink'))
