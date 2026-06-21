# -*- coding: utf-8 -*-
import re, glob

CHEV='<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>'
def sg(p): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'
IC={
 'grid':sg('<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>'),
 'bot':sg('<rect x="4" y="7" width="16" height="12" rx="3"/><path d="M12 7V4M9 13h.01M15 13h.01"/>'),
 'users':sg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/>'),
 'chat':sg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
 'book':sg('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>'),
 'cube':sg('<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>'),
 'shield':sg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),
 'gauge':sg('<circle cx="12" cy="12" r="9"/><path d="M12 12l4-2"/><path d="M12 12v.01"/>'),
 'briefcase':sg('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>'),
 'scale':sg('<path d="M12 3v18M7 21h10M5 7h14M5 7l-2.5 6a3 3 0 0 0 5 0L5 7zm14 0l-2.5 6a3 3 0 0 0 5 0L19 7z"/>'),
 'health':sg('<path d="M3 12h4l2 5 4-10 2 5h6"/>'),
 'bank':sg('<path d="M3 21h18M5 10h14M12 3l8 5H4l8-5zM6 10v8M10 10v8M14 10v8M18 10v8"/>'),
 'landmark':sg('<path d="M3 21h18M4 9h16M12 3l8 4H4l8-4zM7 9v8M11 9v8M15 9v8M19 9v8"/>'),
 'trend':sg('<path d="M3 17l6-6 4 4 8-8"/><path d="M16 7h5v5"/>'),
 'mega':sg('<path d="M3 11l15-5v12L3 13z"/><path d="M7 13v3a2 2 0 0 0 4 0"/>'),
 'support':sg('<path d="M4 14a8 8 0 0 1 16 0"/><rect x="2" y="14" width="4" height="6" rx="1.5"/><rect x="18" y="14" width="4" height="6" rx="1.5"/>'),
 'gear':sg('<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>'),
 'code':sg('<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>'),
 'hr':sg('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M19 8v6M22 11h-6"/>'),
 'pen':sg('<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>'),
 'bookopen':sg('<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'),
 'help':sg('<circle cx="12" cy="12" r="9"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>'),
 'chart':sg('<path d="M3 3v18h18"/><rect x="7" y="11" width="3" height="6"/><rect x="12" y="7" width="3" height="10"/><rect x="17" y="13" width="3" height="4"/>'),
 'video':sg('<rect x="2" y="5" width="14" height="14" rx="2"/><path d="M22 8l-6 4 6 4z"/>'),
}
FEATURES=[('relationflow_feature_multimodell.html','Multi-Modell Access','grid'),('relationflow_feature_agents.html','Intelligente Agents','bot'),('relationflow_feature_spaces.html','Spaces &amp; Collaboration','users'),('relationflow_feature_chat.html','Enterprise Chat','chat'),('relationflow_feature_rag.html','Wissensdatenbank (RAG)','book'),('relationflow_feature_byom.html','Bring Your Own Model (BYOM)','cube'),('relationflow_feature_audit.html','Versionierung &amp; Audit','shield'),('relationflow_feature_cockpit.html','KI-Cockpit','gauge')]
BRANCHEN=[('relationflow_loesung_kmu.html','Allgemeine KMU','briefcase'),('relationflow_loesung_recht.html','Rechtsanw&auml;lte &amp; Juristen','scale'),('relationflow_loesung_medizin.html','Medizin &amp; Gesundheit','health'),('relationflow_loesung_finanz.html','Finanzsektor &amp; Banking','bank'),('relationflow_loesung_verwaltung.html','&Ouml;ffentliche Verwaltung','landmark')]
ABTEILUNGEN=[('relationflow_uc_vertrieb.html','Vertrieb &amp; Sales','trend'),('relationflow_uc_marketing.html','Marketing &amp; Content','mega'),('relationflow_uc_support.html','Customer Support','support'),('relationflow_uc_operations.html','Operations','gear'),('relationflow_uc_it.html','IT &amp; Entwicklung','code'),('relationflow_uc_hr.html','HR &amp; Recruiting','hr')]
RESSOURCEN=[('#','Blog &amp; Insights','pen'),('#','Dokumentation &amp; API-Docs','bookopen'),('#','Help Center','help'),('#','Case Studies','chart'),('#','Webinare &amp; Events','video')]

def ddlink(href,label,ic): return '<a class="dd-link" href="%s"><span class="dd-ic">%s</span><b>%s</b></a>'%(href,IC[ic],label)
def mmlink(href,label,ic): return '<a href="%s"><span class="mm-ic">%s</span>%s</a>'%(href,IC[ic],label)

def nav_links(active):
    fa=' active' if active=='features' else ''
    la=' active' if active=='loesungen' else ''
    sa=' active' if active=='sicherheit' else ''
    pa=' active' if active=='preise' else ''
    feats=''.join(ddlink(*x) for x in FEATURES)
    bran=''.join(ddlink(*x) for x in BRANCHEN)
    abt=''.join(ddlink(*x) for x in ABTEILUNGEN)
    res=''.join(ddlink(*x) for x in RESSOURCEN)
    return ('<div class="nav-links">'
      '<div class="nav-item"><a class="nav-link%s" href="relationflow_features.html">Features %s</a>'
      '<div class="dropdown single"><div class="dd-items">%s</div></div></div>'
      '<div class="nav-item"><span class="nav-link%s" tabindex="0">L&ouml;sungen %s</span>'
      '<div class="dropdown duo"><div class="dd-group"><div class="dd-col-title">Branchen</div><div class="dd-items">%s</div></div>'
      '<div class="dd-group"><div class="dd-col-title">Abteilungen</div><div class="dd-items">%s</div></div></div></div>'
      '<div class="nav-item"><span class="nav-link" tabindex="0">Ressourcen %s</span>'
      '<div class="dropdown single"><div class="dd-items">%s</div></div></div>'
      '<a href="relationflow_sicherheit.html" class="nav-link%s">Sicherheit</a>'
      '<a href="relationflow_preise.html" class="nav-link%s">Preise</a>'
      '</div>')%(fa,CHEV,feats,la,CHEV,bran,abt,CHEV,res,sa,pa)

def mm_home():
    feats=''.join(mmlink(*x) for x in FEATURES)
    bran=''.join(mmlink(*x) for x in BRANCHEN)
    abt=''.join(mmlink(*x) for x in ABTEILUNGEN)
    res=''.join(mmlink(*x) for x in RESSOURCEN)
    return ('<div class="mobile-menu" id="mobileMenu">'
      '<div class="mm-group"><div class="mm-head"><a href="relationflow_features.html">Features</a> <span>+</span></div><div class="mm-sub">%s</div></div>'
      '<div class="mm-group"><div class="mm-head">L&ouml;sungen <span>+</span></div><div class="mm-sub"><div class="mm-subhead">Branchen</div>%s<div class="mm-subhead">Abteilungen</div>%s</div></div>'
      '<div class="mm-group"><div class="mm-head">Ressourcen <span>+</span></div><div class="mm-sub">%s</div></div>'
      '<div class="mm-group"><div class="mm-head"><a href="relationflow_sicherheit.html">Sicherheit</a></div></div>'
      '<div class="mm-group"><div class="mm-head"><a href="relationflow_preise.html">Preise</a></div></div>'
      '<div class="mm-cta"><a href="#" class="btn btn-ghost">Login</a><a href="#preise" class="btn btn-primary">Kostenlos starten</a></div>'
      '</div>')%(feats,bran,abt,res)

INJECT=('.dropdown.duo{width:min(600px,92vw);display:grid;grid-template-columns:1fr 1fr;gap:10px}'
 '.dropdown.single{width:320px}'
 '.dd-group .dd-col-title{font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-2);font-weight:700;padding:8px 12px 6px}'
 '.dd-items .dd-link{flex-direction:row;align-items:center;gap:11px}'
 '.dd-ic{width:34px;height:34px;border-radius:9px;background:var(--accent-soft);color:var(--accent-dark);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:background .15s,color .15s}'
 '.dd-ic svg{width:18px;height:18px}'
 '.dd-link:hover .dd-ic{background:var(--accent);color:#fff}'
 '.mm-subhead{font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-2);font-weight:700;padding:10px 10px 2px}'
 '.mm-sub a{display:flex;align-items:center;gap:10px}'
 '.mm-ic{width:26px;height:26px;border-radius:7px;background:var(--accent-soft);color:var(--accent-dark);display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}'
 '.mm-ic svg{width:15px;height:15px}')

files=[f for f in glob.glob('relationflow_*.html') if 'variante' not in f]+['index.html']
for f in files:
    s=open(f).read(); orig=s
    fn=f
    if fn=='index.html': fn='relationflow_website.html'
    active=''
    if fn=='relationflow_features.html': active='features'
    elif fn.startswith('relationflow_loesung_') or fn.startswith('relationflow_uc_') or fn=='relationflow_anwendungsfaelle.html': active='loesungen'
    elif fn=='relationflow_sicherheit.html': active='sicherheit'
    elif fn=='relationflow_preise.html': active='preise'

    # desktop nav-links
    s2=re.sub(r'<div class="nav-links">.*</div>\s*<div class="nav-cta">', nav_links(active)+'<div class="nav-cta">', s, count=1, flags=re.S)
    if s2==s: print('!! nav-links not replaced in',f)
    s=s2

    # CSS inject (idempotent)
    if '.dd-ic{' not in s:
        s=s.replace('</head>','<style>'+INJECT+'</style></head>',1)

    # mobile menu
    if 'class="mm-group"' in s:
        s=re.sub(r'<div class="mobile-menu" id="mobileMenu">.*?<div class="mm-cta">.*?</div>\s*</div>', mm_home(), s, count=1, flags=re.S)
    else:
        # flat: merge Anwendungsfälle + Lösungen into single Lösungen link
        s=re.sub(r'<a href="[^"]*">Anwendungsf&auml;lle</a>\s*<a href="[^"]*">L&ouml;sungen</a>', '<a href="relationflow_anwendungsfaelle.html">L&ouml;sungen</a>', s, count=1)
        s=re.sub(r'<a href="[^"]*">Anwendungsfälle</a>\s*<a href="[^"]*">Lösungen</a>', '<a href="relationflow_anwendungsfaelle.html">Lösungen</a>', s, count=1)

    if s!=orig: open(f,'w').write(s); print('upd',f)
    else: print('--',f)
