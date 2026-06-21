import re

src = open('relationflow_uc_vertrieb.html').read()

# ---------- custom CSS ----------
CSS = r'''
/* ================= ANWENDUNGSFÄLLE PAGE ================= */
.af-wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.af-ey{display:inline-flex;align-items:center;gap:8px;font-size:.74rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent-dark);background:var(--accent-soft);border:1px solid var(--accent-soft-2);padding:7px 14px;border-radius:999px}
.af-ey .dot{width:6px;height:6px;border-radius:50%;background:var(--accent)}
.af-h2{font-size:clamp(1.9rem,3.6vw,2.9rem);line-height:1.06;letter-spacing:-0.03em;font-weight:700;margin:18px 0 0}
.af-sub{font-size:clamp(1rem,1.3vw,1.16rem);color:var(--muted);max-width:640px;margin:16px 0 0;line-height:1.55}
.af-center{text-align:center}.af-center .af-sub{margin-left:auto;margin-right:auto}
.af-sec{padding:clamp(72px,9vw,120px) 0}
.af-dark{position:relative;overflow:hidden;color:#fff;border-radius:var(--radius-lg);margin:0 48px;padding:clamp(64px,8vw,104px) 0}
.af-dark .af-ey{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.02));color:#cfe0ff;border-color:rgba(255,255,255,.14)}
.af-dark .af-sub{color:#b6c0d4}.af-dark .serif{color:#fff}
@media(max-width:680px){.af-dark{margin:0 16px}}

/* 1. HERO */
.af-hero{position:relative;overflow:hidden;padding:clamp(80px,11vw,150px) 0 clamp(48px,6vw,84px);text-align:center}
.af-hero h1{font-size:clamp(2.4rem,6vw,4.4rem);line-height:1.02;letter-spacing:-0.045em;font-weight:700;margin:22px auto 0;max-width:14ch}
.af-hero .lead{margin:20px auto 0;max-width:620px}
.af-hero-cta{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:30px}
.af-float{position:absolute;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.af-chip{position:absolute;display:inline-flex;align-items:center;gap:7px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px 13px;font-size:.78rem;font-weight:600;box-shadow:var(--shadow-md);white-space:nowrap;color:var(--text);opacity:.0;animation:afFloatIn .8s ease forwards,afBob 6s ease-in-out infinite}
.af-chip i{width:8px;height:8px;border-radius:50%;background:var(--accent)}
@keyframes afFloatIn{to{opacity:1}}
@keyframes afBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.af-hero .af-wrap{position:relative;z-index:2}
.af-statrow{display:flex;gap:clamp(20px,4vw,64px);justify-content:center;flex-wrap:wrap;margin-top:48px}
.af-stat{text-align:center}
.af-stat b{display:block;font-size:clamp(2rem,4vw,3rem);font-weight:700;letter-spacing:-0.04em;background:linear-gradient(120deg,var(--accent),var(--accent-light));-webkit-background-clip:text;background-clip:text;color:transparent}
.af-stat span{font-size:.82rem;color:var(--muted-2);font-weight:600}

/* 2. DEPT SWITCHER */
.af-deptbar{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:42px}
.af-deptbar button{display:inline-flex;align-items:center;gap:9px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:11px 18px;font:inherit;font-size:.9rem;font-weight:600;color:var(--muted);cursor:pointer;transition:all .2s}
.af-deptbar button .di{width:22px;height:22px;display:flex;align-items:center;justify-content:center;color:var(--accent)}
.af-deptbar button .di svg{width:17px;height:17px}
.af-deptbar button.on{background:var(--text);color:#fff;border-color:var(--text)}
.af-deptbar button.on .di{color:var(--accent-light)}
.af-panel{display:none;margin-top:36px}
.af-panel.on{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(24px,4vw,52px);align-items:center;animation:afFade .4s ease}
@keyframes afFade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.af-panel h3{font-size:clamp(1.4rem,2.4vw,2rem);letter-spacing:-0.03em;margin:6px 0 0}
.af-panel .pdesc{color:var(--muted);margin:12px 0 22px;line-height:1.55}
.af-uclist{display:flex;flex-direction:column;gap:10px}
.af-ucrow{display:flex;align-items:flex-start;gap:13px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;box-shadow:var(--shadow-sm);transition:transform .18s,box-shadow .18s}
.af-ucrow:hover{transform:translateX(4px);box-shadow:var(--shadow-md)}
.af-ucrow .ck{flex-shrink:0;width:26px;height:26px;border-radius:8px;background:var(--accent-soft);color:var(--accent-dark);display:flex;align-items:center;justify-content:center}
.af-ucrow .ck svg{width:15px;height:15px}
.af-ucrow b{font-size:.96rem}.af-ucrow p{font-size:.83rem;color:var(--muted-2);margin:3px 0 0}
.af-ucrow .tm{margin-left:auto;flex-shrink:0;font-size:.7rem;font-weight:700;color:#16a34a;background:#dcf7e6;border-radius:999px;padding:4px 9px;white-space:nowrap}
.af-pvis{position:relative;border-radius:var(--radius-lg);overflow:hidden;border:1px solid var(--line);background:linear-gradient(180deg,#0b1220,#070b14);box-shadow:var(--shadow-lg);min-height:380px;color:#fff;padding:22px}
.af-pvis .vbar{display:flex;align-items:center;gap:7px;margin-bottom:18px}
.af-pvis .vbar i{width:9px;height:9px;border-radius:50%}
.af-pvis .vbar .vt{margin-left:6px;font-size:.74rem;color:#9aa6bd;font-weight:600}
.af-pvis .vmsg{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:13px;padding:13px 15px;font-size:.85rem;line-height:1.5;margin-bottom:11px}
.af-pvis .vmsg.u{background:rgba(37,99,235,.18);border-color:rgba(125,169,255,.3)}
.af-pvis .vmsg .who{font-size:.66rem;text-transform:uppercase;letter-spacing:.1em;color:#7da9ff;font-weight:700;margin-bottom:5px}
.af-pvis .vtag{display:inline-flex;align-items:center;gap:6px;font-size:.7rem;font-weight:600;color:#cfe0ff;background:rgba(255,255,255,.08);border-radius:999px;padding:5px 11px;margin:2px 5px 2px 0}
@media(max-width:860px){.af-panel.on{grid-template-columns:1fr}}

/* 3. WORKDAY TIMELINE */
.af-day{margin-top:48px;position:relative}
.af-dayline{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;position:relative}
.af-dayline::before{content:"";position:absolute;left:0;right:0;top:34px;height:3px;background:linear-gradient(90deg,var(--accent-light),var(--accent));border-radius:2px;z-index:0}
.af-dnode{position:relative;z-index:1;text-align:center}
.af-dnode .dt{display:inline-flex;align-items:center;justify-content:center;width:70px;height:70px;border-radius:50%;background:#fff;border:3px solid var(--accent);color:var(--accent-dark);font-weight:700;font-size:1rem;box-shadow:var(--shadow-md);margin-bottom:16px}
.af-dcard{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 14px;box-shadow:var(--shadow-sm);text-align:left}
.af-dcard .dl{font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;color:var(--accent-dark);font-weight:700}
.af-dcard b{display:block;font-size:.92rem;margin:6px 0 5px}
.af-dcard p{font-size:.8rem;color:var(--muted-2);line-height:1.45}
@media(max-width:860px){.af-dayline{grid-template-columns:1fr}.af-dayline::before{left:34px;top:0;bottom:0;right:auto;width:3px;height:auto}.af-dnode{display:flex;gap:16px;text-align:left}.af-dnode .dt{margin-bottom:0}.af-dcard{flex:1}}

/* 4. MATRIX */
.af-matrix{margin-top:42px;overflow-x:auto}
.af-mtable{width:100%;border-collapse:separate;border-spacing:8px;min-width:680px}
.af-mtable th{font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted-2);font-weight:700;padding:8px;text-align:center}
.af-mtable th.rowh,.af-mtable td.rowh{text-align:left;font-weight:700;color:var(--text);font-size:.9rem;white-space:nowrap}
.af-cell{border-radius:12px;padding:14px 8px;text-align:center;font-weight:700;font-size:.82rem;color:#fff;position:relative}
.af-cell small{display:block;font-size:.62rem;font-weight:600;opacity:.85;margin-top:2px}
.af-l1{background:#bcd0ff;color:var(--accent-dark)}.af-l2{background:#6f9bf2}.af-l3{background:var(--accent)}.af-l4{background:var(--accent-dark)}
.af-mleg{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:22px;font-size:.78rem;color:var(--muted)}
.af-mleg span{display:inline-flex;align-items:center;gap:7px}
.af-mleg i{width:14px;height:14px;border-radius:4px}

/* 5. FLOW BLUEPRINT */
.af-flow{margin-top:48px;display:grid;grid-template-columns:repeat(5,1fr);gap:10px;align-items:stretch;position:relative}
.af-fnode{background:linear-gradient(180deg,#fff,#f6f8fc);border:1px solid var(--line);border-radius:18px;padding:20px 16px;text-align:center;box-shadow:var(--shadow-sm);position:relative}
.af-fnode .fi{width:46px;height:46px;border-radius:13px;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;background:var(--accent-soft);color:var(--accent-dark)}
.af-fnode .fi svg{width:24px;height:24px}
.af-fnode b{display:block;font-size:.92rem}.af-fnode p{font-size:.76rem;color:var(--muted-2);margin-top:5px;line-height:1.4}
.af-fnode .fnum{position:absolute;top:-10px;left:50%;transform:translateX(-50%);width:24px;height:24px;border-radius:50%;background:var(--accent);color:#fff;font-size:.72rem;font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 10px -2px rgba(37,99,235,.6)}
.af-flow .af-arr{align-self:center;display:flex;align-items:center;justify-content:center;color:var(--accent);position:absolute}
.af-flowsvg{grid-column:1/-1;height:0}
@media(max-width:860px){.af-flow{grid-template-columns:1fr;gap:26px}}

/* 6. GALLERY MARQUEE */
.af-gal{margin-top:42px;display:flex;flex-direction:column;gap:14px}
.af-mqrow{display:flex;gap:12px;width:max-content;animation:afMarq 42s linear infinite}
.af-mqrow.rev{animation-direction:reverse}
.af-mqwrap{overflow:hidden;-webkit-mask:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.af-gchip{display:inline-flex;align-items:center;gap:9px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:11px 16px;font-size:.85rem;font-weight:600;white-space:nowrap;box-shadow:var(--shadow-sm)}
.af-gchip .gi{width:7px;height:7px;border-radius:50%;background:var(--accent)}
@keyframes afMarq{to{transform:translateX(-50%)}}
@media(prefers-reduced-motion:reduce){.af-mqrow{animation:none}}

/* 7. INDUSTRY */
.af-indgrid{margin-top:42px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.af-ind{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow-sm);transition:transform .18s,box-shadow .18s,border-color .18s}
.af-ind:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--accent-light)}
.af-ind .ihd{display:flex;align-items:center;gap:12px;margin-bottom:14px}
.af-ind .ii{width:44px;height:44px;border-radius:13px;background:var(--accent-soft);color:var(--accent-dark);display:flex;align-items:center;justify-content:center}
.af-ind .ii svg{width:23px;height:23px}
.af-ind h4{font-size:1.05rem;letter-spacing:-0.02em}
.af-ind ul{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px}
.af-ind li{display:flex;gap:9px;font-size:.85rem;color:var(--muted);line-height:1.4}
.af-ind li::before{content:"";flex-shrink:0;width:16px;height:16px;margin-top:1px;border-radius:5px;background:var(--accent-soft);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' fill='none' stroke='%231d4ed8' stroke-width='3' viewBox='0 0 24 24'%3E%3Cpath d='M20 6L9 17l-5-5'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:center}
@media(max-width:860px){.af-indgrid{grid-template-columns:1fr}}

/* 8. STORY SPOTLIGHT (dark) */
.af-story-bg{background:radial-gradient(60% 70% at 30% 20%,rgba(37,99,235,.28),transparent 60%),linear-gradient(180deg,#06080f,#070b14)}
.af-story{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5vw,60px);align-items:center;margin-top:8px}
.af-story .sq{font-family:Lora,serif;font-style:italic;font-size:clamp(1.4rem,2.6vw,2.1rem);line-height:1.35;color:#fff}
.af-story .sby{margin-top:20px;display:flex;align-items:center;gap:12px}
.af-story .sav{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent-dark));display:flex;align-items:center;justify-content:center;font-weight:700;color:#fff}
.af-story .sby b{display:block;font-size:.9rem}.af-story .sby span{font-size:.78rem;color:#9aa6bd}
.af-storymetrics{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.af-sm{background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:22px}
.af-sm b{font-size:clamp(1.8rem,3.4vw,2.6rem);font-weight:700;letter-spacing:-0.04em;color:#fff;display:block}
.af-sm .sl{font-size:.78rem;color:#9aa6bd;margin-top:4px}
@media(max-width:860px){.af-story{grid-template-columns:1fr}.af-storymetrics{margin-top:6px}}

/* 9. IMPACT BOARD (dark) */
.af-board-bg{background:radial-gradient(50% 60% at 50% 0%,rgba(37,99,235,.26),transparent 60%),linear-gradient(180deg,#05070d,#070b14)}
.af-bgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:42px}
.af-btile{background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:24px;position:relative;overflow:hidden}
.af-btile b{font-size:clamp(1.9rem,3.6vw,2.8rem);font-weight:700;letter-spacing:-0.04em;color:#fff;display:block}
.af-btile .bl{font-size:.8rem;color:#9aa6bd;margin-top:6px}
.af-btile .bspark{position:absolute;right:0;bottom:0;width:60%;opacity:.5}
.af-tape{margin-top:30px;overflow:hidden;-webkit-mask:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);mask:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.af-tapetrack{display:inline-flex;gap:34px;white-space:nowrap;animation:afMarq 36s linear infinite;color:#b6c0d4;font-size:.84rem;font-weight:600}
.af-tapetrack span{display:inline-flex;align-items:center;gap:9px}
.af-tapetrack span::before{content:"";width:6px;height:6px;border-radius:50%;background:#34d399}
@media(max-width:860px){.af-bgrid{grid-template-columns:1fr 1fr}}

/* 10. VS COMPARISON */
.af-vs{margin-top:42px}
.af-vstoggle{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:26px}
.af-vstoggle button{border:1px solid var(--line);background:#fff;border-radius:999px;padding:9px 16px;font:inherit;font-size:.84rem;font-weight:600;color:var(--muted);cursor:pointer;transition:all .2s}
.af-vstoggle button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.af-vsgrid{display:grid;grid-template-columns:1fr 1fr;gap:18px;max-width:880px;margin:0 auto}
.af-vscard{border-radius:20px;padding:26px;border:1px solid var(--line)}
.af-vscard.bad{background:linear-gradient(160deg,#fff6f6,#fdedef);border-color:#f3d4d8}
.af-vscard.good{background:linear-gradient(160deg,#f2f7ff,#eef3ff)}
.af-vscard .vh{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1.05rem;margin-bottom:16px}
.af-vscard .vh .vt{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;padding:3px 9px;border-radius:999px}
.af-vscard.bad .vt{background:#fde2e4;color:#dc2626}.af-vscard.good .vt{background:#dcf7e6;color:#16a34a}
.af-vsitem{display:flex;gap:11px;font-size:.88rem;color:var(--muted);line-height:1.5;padding:9px 0;border-top:1px solid rgba(0,0,0,.05)}
.af-vsitem:first-of-type{border-top:0}
.af-vsitem .vmk{flex-shrink:0;width:20px;height:20px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.7rem}
.af-vscard.bad .vmk{background:#fde2e4;color:#dc2626}.af-vscard.good .vmk{background:#dcf7e6;color:#16a34a}
.af-vsfoot{margin-top:18px;font-size:.82rem;font-weight:700}
.af-vscard.bad .af-vsfoot{color:#dc2626}.af-vscard.good .af-vsfoot{color:#16a34a}
@media(max-width:680px){.af-vsgrid{grid-template-columns:1fr}}
'''

# ---------- helper data ----------
def svg(p): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'
IC = {
 'sales': svg('<path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/>'),
 'mkt': svg('<path d="M3 11l18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 0 1-5.8-1.6"/>'),
 'supp': svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
 'ops': svg('<circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1l2-1.6-2-3.4-2.3 1a7 7 0 0 0-1.7-1l-.3-2.5h-4l-.3 2.5a7 7 0 0 0-1.7 1l-2.3-1-2 3.4 2 1.6a7 7 0 0 0 0 2l-2 1.6 2 3.4 2.3-1a7 7 0 0 0 1.7 1l.3 2.5h4l.3-2.5a7 7 0 0 0 1.7-1l2.3 1 2-3.4-2-1.6a7 7 0 0 0 .1-1z"/>'),
 'it': svg('<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>'),
 'hr': svg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/>'),
}

depts = [
 ('sales','Vertrieb &amp; Sales','sales','Schneller vom Lead zum Abschluss',
   'Angebote, Follow-ups und CRM-Pflege laufen halbautomatisch &ndash; das Team konzentriert sich aufs Verkaufen.',
   [('Angebote in Minuten','Aus Gesprächsnotizen wird ein fertiges Angebot.','−85% Zeit'),
    ('Lead-Qualifizierung','Eingehende Anfragen automatisch bewerten &amp; routen.','3× schneller'),
    ('Follow-up-Sequenzen','Personalisierte Nachfassmails auf Knopfdruck.','+22% Antwortrate'),
    ('Battlecards &amp; Einwände','Live-Argumente gegen Wettbewerber im Gespräch.','sofort'),
    ('CRM-Pflege','Notizen werden automatisch strukturiert eingetragen.','−4 Std/Woche')],
   [('u','Vertrieb','Erstelle ein Angebot für die Müller GmbH, 50 Lizenzen, Pro-Plan.'),
    ('a','Relationflow','Angebot erstellt &ndash; inkl. Mengenrabatt, AGB und Gültigkeit. Soll ich es als PDF an Herrn Müller senden?')],
   ['Angebots-Agent','CRM-Sync','Battlecards','E-Mail-Vorlagen']),
 ('mkt','Marketing &amp; Content','mkt','Content, der skaliert',
   'Kampagnen, Blogartikel und Social Posts in eurer Markenstimme &ndash; konsistent über alle Kanäle.',
   [('Blog &amp; SEO','Recherchierte Artikel im Marken-Ton.','5× Output'),
    ('Social-Kalender','Wochenplan inkl. Captions &amp; Hashtags.','−70% Zeit'),
    ('Kampagnen-Briefings','Aus einer Idee ein vollständiges Briefing.','sofort'),
    ('Newsletter','Segmentierte Mails aus Produktupdates.','+18% Open-Rate'),
    ('Bild-Konzepte','Moodboards &amp; Visual-Ideen pro Kampagne.','schneller')],
   [('u','Marketing','Schreib 3 LinkedIn-Posts zum Launch unseres DSGVO-Features.'),
    ('a','Relationflow','Hier sind 3 Varianten in eurer Tonalität &ndash; Hook, Nutzen, CTA. Möchtest du Hashtags und ein Bildkonzept dazu?')],
   ['Content-Agent','Marken-Stimme','SEO-Check','Bildkonzepte']),
 ('supp','Customer Support','supp','Antworten, die treffen',
   'Tickets werden vorqualifiziert, beantwortet und eskaliert &ndash; mit Zugriff auf euer gesamtes Firmenwissen.',
   [('Antwort-Entwürfe','Aus Ticket + Wissensbasis ein Antwortvorschlag.','−60% AHT'),
    ('Wissens-Suche','Sofortantwort aus Doku &amp; Handbüchern.','sofort'),
    ('Stimmungsanalyse','Frustrierte Kund:innen automatisch priorisieren.','schneller'),
    ('Mehrsprachig','Antworten in 20+ Sprachen, on-brand.','24/7'),
    ('Makro-Erstellung','Wiederkehrende Fälle als Vorlage.','skaliert')],
   [('u','Support','Kunde meldet Login-Fehler nach Update. Was antworten?'),
    ('a','Relationflow','Vorschlag erstellt &ndash; mit Schritt-für-Schritt-Lösung aus eurer Doku. Tonfall: freundlich-lösungsorientiert. Senden?')],
   ['Ticket-Agent','Wissensbasis','Sentiment','Übersetzung']),
 ('ops','Operations','ops','Prozesse, die sich selbst erledigen',
   'Von der Rechnungsprüfung bis zum Reporting &ndash; Routinearbeit läuft im Hintergrund, sauber dokumentiert.',
   [('Dokument-Extraktion','Daten aus Rechnungen &amp; PDFs ziehen.','−90% Tippen'),
    ('Report-Generierung','Wochen- &amp; Monatsreports automatisch.','−6 Std/Woche'),
    ('Prozess-SOPs','Abläufe in klare Anleitungen übersetzen.','konsistent'),
    ('Datenabgleich','Tabellen prüfen &amp; Abweichungen melden.','fehlerfrei'),
    ('Meeting-Protokolle','Notizen &amp; To-dos automatisch.','sofort')],
   [('u','Operations','Fasse die 12 Lieferanten-Rechnungen zusammen und markiere Abweichungen.'),
    ('a','Relationflow','Zusammenfassung erstellt &ndash; 2 Rechnungen über Budget, 1 doppelt. Tabelle &amp; Audit-Log liegen bereit.')],
   ['Dokument-Agent','Report-Builder','Audit-Log','Daten-Check']),
 ('it','IT &amp; Entwicklung','it','Mehr Zeit fürs Wesentliche',
   'Code-Reviews, Doku und First-Level-Support &ndash; das Team gewinnt Fokus für echte Entwicklung.',
   [('Code-Erklärung','Legacy-Code verständlich dokumentiert.','schneller'),
    ('Review-Assistent','Pull-Requests vorprüfen &amp; kommentieren.','−40% Zeit'),
    ('Doku-Generierung','Technische Doku aus dem Code.','aktuell'),
    ('Incident-Hilfe','Logs analysieren, Ursachen vorschlagen.','MTTR ↓'),
    ('Interner Helpdesk','IT-Fragen mit Firmenkontext beantworten.','24/7')],
   [('u','IT','Erkläre diese Funktion und schlage Verbesserungen vor.'),
    ('a','Relationflow','Funktion analysiert &ndash; Zweck, Risiken, 3 Optimierungen. Soll ich einen Doku-Eintrag &amp; Tests vorschlagen?')],
   ['Code-Agent','Review-Bot','Doku-Sync','Log-Analyse']),
 ('hr','HR &amp; Recruiting','hr','Menschen statt Papierkram',
   'Stellenanzeigen, Bewerber-Screening und Onboarding &ndash; HR gewinnt Zeit für echte Begegnung.',
   [('Stellenanzeigen','Aus Stichpunkten eine fertige Anzeige.','−80% Zeit'),
    ('CV-Screening','Lebensläufe gegen Anforderungen matchen.','fair &amp; schnell'),
    ('Interview-Leitfäden','Strukturierte Fragen pro Rolle.','konsistent'),
    ('Onboarding-Pläne','Individuelle Einarbeitung in Minuten.','reibungslos'),
    ('Policy-Antworten','HR-Fragen aus dem Handbuch beantworten.','sofort')],
   [('u','HR','Erstelle eine Stellenanzeige für eine:n Senior Buchhalter:in.'),
    ('a','Relationflow','Anzeige erstellt &ndash; inkl. Benefits, inklusiver Sprache &amp; SEO. Möchtest du einen passenden Interview-Leitfaden dazu?')],
   ['Recruiting-Agent','CV-Match','Onboarding','HR-Wissen']),
]

def ck(): return '<span class="ck"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></span>'

def dept_button(d, on):
    return f'<button data-d="{d[0]}" class="{"on" if on else ""}"><span class="di">{IC[d[2]]}</span>{d[1]}</button>'

def dept_panel(d, on):
    rows=''.join(f'<div class="af-ucrow">{ck()}<div><b>{t}</b><p>{p}</p></div><span class="tm">{m}</span></div>' for t,p,m in d[5])
    msgs=''.join(f'<div class="af-vmsg {"u" if w=="u" else ""}"><div class="who">{who}</div>{txt}</div>' for w,who,txt in d[6])
    tags=''.join(f'<span class="af-vtag">{t}</span>' for t in d[7])
    return (f'<div class="af-panel {"on" if on else ""}" data-p="{d[0]}">'
            f'<div><span class="af-ey"><span class="dot"></span>{d[1]}</span><h3>{d[3]}</h3>'
            f'<p class="pdesc">{d[4]}</p><div class="af-uclist">{rows}</div></div>'
            f'<div class="af-pvis"><div class="vbar"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i>'
            f'<i style="background:#28c840"></i><span class="vt">Relationflow · {d[1].split(" ")[0]}</span></div>'
            f'{msgs}<div style="margin-top:14px">{tags}</div></div></div>')

dept_buttons=''.join(dept_button(d,i==0) for i,d in enumerate(depts))
dept_panels=''.join(dept_panel(d,i==0) for i,d in enumerate(depts))

# section 1 hero chips
chips=[('Angebote schreiben','6%','14%'),('Tickets beantworten','78%','20%'),('Reports erstellen','12%','64%'),
       ('Code dokumentieren','84%','70%'),('CVs screenen','40%','10%'),('Social Posts','62%','82%'),
       ('Rechnungen prüfen','24%','40%'),('Newsletter','88%','40%')]
chip_html=''.join(f'<span class="af-chip" style="left:{x};top:{y};animation-delay:{i*0.25}s,{i*0.4}s"><i></i>{t}</span>' for i,(t,x,y) in enumerate(chips))

# section 3 workday
day=[('08','Start','Tagesplanung','Agenten fassen über Nacht eingegangene Mails &amp; Tickets zusammen.'),
     ('10','Vertrieb','Angebote raus','Aus Calls werden Angebote &ndash; das Team folgt nur noch nach.'),
     ('13','Content','Kampagne live','Blog, Social &amp; Newsletter entstehen parallel, on-brand.'),
     ('15','Ops','Reporting','Wochenzahlen automatisch zusammengestellt &amp; geprüft.'),
     ('17','Wissen','Audit &amp; Ablage','Alles versioniert, dokumentiert und revisionssicher abgelegt.')]
day_html=''.join(f'<div class="af-dnode"><div class="dt">{t}</div><div class="af-dcard"><div class="dl">{lbl}</div><b>{ti}</b><p>{p}</p></div></div>' for t,lbl,ti,p in day)

# section 4 matrix
mcols=['Zeit sparen','Qualität','Skalierung','Compliance']
mrows=[('Vertrieb',[('af-l4','−85%','Zeit'),('af-l3','hoch',''),('af-l3','3×',''),('af-l2','gut','')]),
       ('Marketing',[('af-l3','−70%','Zeit'),('af-l4','sehr hoch',''),('af-l4','5×',''),('af-l2','gut','')]),
       ('Support',[('af-l4','−60%','AHT'),('af-l3','hoch',''),('af-l4','24/7',''),('af-l3','stark','')]),
       ('Operations',[('af-l4','−90%','Aufwand'),('af-l3','hoch',''),('af-l3','robust',''),('af-l4','Audit','')]),
       ('IT',[('af-l3','−40%','Zeit'),('af-l3','hoch',''),('af-l2','solide',''),('af-l4','sicher','')]),
       ('HR',[('af-l4','−80%','Zeit'),('af-l3','fair',''),('af-l2','wachsend',''),('af-l4','konform','')])]
mhead='<tr><th class="rowh">Abteilung</th>'+''.join(f'<th>{c}</th>' for c in mcols)+'</tr>'
mbody=''.join('<tr><td class="rowh">'+r+'</td>'+''.join(f'<td><div class="af-cell {cls}">{v}{("<small>"+s+"</small>") if s else ""}</div></td>' for cls,v,s in cells)+'</tr>' for r,cells in mrows)

# section 5 flow
flow=[('1',svg('<path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/>'),'Auslöser','Eine Frage, ein Dokument oder ein Event.'),
      ('2',svg('<rect x="4" y="7" width="16" height="12" rx="3"/><path d="M12 7V4M9 13h.01M15 13h.01"/>'),'Agent','Wählt Aufgabe, Tools &amp; Schritte.'),
      ('3',svg('<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>'),'Bestes Modell','GPT, Claude, Gemini, Mistral oder euer eigenes.'),
      ('4',svg('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5z"/>'),'Firmenwissen','RAG zieht Kontext aus euren Dokumenten.'),
      ('5',svg('<path d="M20 6L9 17l-5-5"/>'),'Ergebnis','Geprüft, versioniert, im Audit-Log.')]
flow_html=''.join(f'<div class="af-fnode"><span class="fnum">{n}</span><div class="fi">{ic}</div><b>{t}</b><p>{p}</p></div>' for n,ic,t,p in flow)

# section 6 gallery
g1=['Angebote erstellen','Tickets beantworten','Blogartikel schreiben','Rechnungen prüfen','CVs screenen','Meeting-Protokolle','Verträge analysieren','Social-Posts','Code dokumentieren','Reports bauen','Follow-up-Mails','Übersetzungen']
g2=['Stellenanzeigen','SOPs schreiben','Wettbewerbsanalyse','Newsletter','Onboarding-Pläne','Datenabgleich','Battlecards','Produkttexte','FAQ pflegen','Log-Analyse','Briefings','Interview-Leitfäden']
def galrow(items, rev):
    chips=''.join(f'<span class="af-gchip"><span class="gi"></span>{t}</span>' for t in items*2)
    return f'<div class="af-mqwrap"><div class="af-mqrow {rev}">{chips}</div></div>'

# section 7 industry
inds=[('Kanzleien &amp; Recht','it',['Vertrags- &amp; Klauselanalyse','Schriftsatz-Entwürfe','Mandanten-FAQ','Recherche mit Quellen']),
      ('Medizin &amp; Gesundheit','supp',['Arztbrief-Entwürfe','Anamnese-Strukturierung','Patienten-Aufklärung','Abrechnungs-Checks']),
      ('Finanz &amp; Banking','ops',['Report-Automatisierung','Compliance-Prüfung','Markt-Briefings','Kunden-Kommunikation']),
      ('Industrie &amp; Fertigung','ops',['Wartungs-SOPs','Lieferanten-Mails','Qualitäts-Doku','Schichtprotokolle']),
      ('Handel &amp; E-Commerce','mkt',['Produktbeschreibungen','Support-Antworten','Kampagnen-Content','Retouren-Analyse']),
      ('Öffentliche Verwaltung','hr',['Bürger-Anfragen','Akten-Zusammenfassung','Formular-Hilfe','Protokolle'])]
def indcard(name, icon, items):
    lis=''.join(f'<li>{i}</li>' for i in items)
    return f'<div class="af-ind"><div class="ihd"><span class="ii">{IC[icon]}</span><h4>{name}</h4></div><ul>{lis}</ul></div>'
ind_html=''.join(indcard(*i) for i in inds)

# section 9 board
btiles=[('count','Std','0','120000',' ','Stunden pro Jahr gespart'),
        ('count','','0','48000',' ','Angebote &amp; Dokumente erstellt'),
        ('count','%','0','99','','DSGVO-konforme Anfragen'),
        ('count','','0','60','+','Use Cases produktiv im Einsatz')]
def btile(suf,pre,frm,to,sym,lbl):
    return f'<div class="af-btile"><b><span class="count" data-to="{to}" data-suffix="{suf}">0</span></b><div class="bl">{lbl}</div></div>'
board_html=''.join(btile(*[t[1],'',t[2],t[3],'',t[5]]) for t in btiles)
tape_items=['11 Angebote heute erstellt','2.480 Tickets beantwortet','340 Reports generiert','58 CVs gescreent','920 Dokumente analysiert','100% EU-gehostet']
tape_html=''.join(f'<span>{t}</span>' for t in tape_items*2)

# section 10 vs
vs_cases={
 'Angebot erstellen':[('Manuell','bad',['Daten aus Mails zusammensuchen','Vorlage manuell füllen','Rabatte &amp; AGB nachschlagen','45&ndash;90 Minuten pro Angebot'],'⌀ 60 Min'),
                      ('Mit Relationflow','good',['Agent zieht Kontext automatisch','Angebot in Marken-Layout','Rabattlogik &amp; AGB integriert','Fertig in unter 5 Minuten'],'⌀ 4 Min')],
 'Ticket beantworten':[('Manuell','bad',['Wissensbasis durchsuchen','Antwort selbst formulieren','In Fremdsprache übersetzen','Hohe Bearbeitungszeit'],'⌀ 12 Min'),
                       ('Mit Relationflow','good',['Sofort-Vorschlag aus Doku','On-brand &amp; mehrsprachig','Eskalation automatisch erkannt','Nur noch prüfen &amp; senden'],'⌀ 3 Min')],
 'Report erstellen':[('Manuell','bad',['Daten aus Tools exportieren','In Tabellen zusammenführen','Text manuell schreiben','Stunden pro Woche'],'⌀ 6 Std'),
                     ('Mit Relationflow','good',['Daten automatisch gebündelt','Auswertung &amp; Text generiert','Versioniert &amp; geprüft','Minuten statt Stunden'],'⌀ 20 Min')],
}
def vs_panel(name, data, on):
    cards=''
    for title,cls,items,foot in data:
        its=''.join(f'<div class="af-vsitem"><span class="vmk">{"✕" if cls=="bad" else "✓"}</span>{i}</div>' for i in items)
        tag='Vorher' if cls=='bad' else 'Mit Relationflow'
        cards+=f'<div class="af-vscard {cls}"><div class="vh"><span class="vt">{tag}</span>{title}</div>{its}<div class="af-vsfoot">{foot}</div></div>'
    return f'<div class="af-vspanel {"on" if on else ""}" data-vs="{name}" style="{"" if on else "display:none"}"><div class="af-vsgrid">{cards}</div></div>'
vs_buttons=''.join(f'<button data-vs="{n}" class="{"on" if i==0 else ""}">{n}</button>' for i,n in enumerate(vs_cases))
vs_panels=''.join(vs_panel(n,d,i==0) for i,(n,d) in enumerate(vs_cases.items()))

# ---------- assemble body ----------
BODY = f'''<section class="af-hero"><div class="af-float">{chip_html}</div><div class="af-wrap">
<span class="af-ey"><span class="dot"></span>Anwendungsfälle</span>
<h1>Wofür Teams Relationflow <span class="serif">wirklich</span> nutzen.</h1>
<p class="lead">Von Vertrieb bis HR, von der Kanzlei bis zur Verwaltung &ndash; über 60 konkrete Anwendungsfälle, die heute schon Stunden sparen. DSGVO-konform, im Team, mit allen Top-Modellen.</p>
<div class="af-hero-cta"><a href="#" class="btn btn-primary">Kostenlos starten</a><a href="#dept" class="btn btn-ghost">Use Cases entdecken</a></div>
<div class="af-statrow">
<div class="af-stat"><b>6</b><span>Abteilungen</span></div>
<div class="af-stat"><b><span class="count" data-to="60">0</span>+</b><span>Use Cases</span></div>
<div class="af-stat"><b>8+</b><span>KI-Modelle</span></div>
<div class="af-stat"><b>100%</b><span>EU &amp; DSGVO</span></div>
</div></div></section>

<section class="af-sec" id="dept"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Nach Abteilung</span>
<h2 class="af-h2">Jedes Team hat seine <span class="serif">Lieblings-Use-Cases</span>.</h2>
<p class="af-sub">Wähle eine Abteilung und sieh, was Relationflow dort konkret übernimmt &ndash; inklusive Live-Beispiel.</p>
<div class="af-deptbar" id="afDeptBar">{dept_buttons}</div></div>
<div class="af-wrap" id="afPanels">{dept_panels}</div></section>

<section class="af-sec" style="background:var(--bg-alt)"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Ein Arbeitstag</span>
<h2 class="af-h2">Acht Stunden, <span class="serif">automatisiert</span> begleitet.</h2>
<p class="af-sub">So fügt sich Relationflow in einen ganz normalen Arbeitstag ein &ndash; vom ersten Kaffee bis zum Feierabend.</p></div>
<div class="af-wrap"><div class="af-day"><div class="af-dayline">{day_html}</div></div></div></section>

<section class="af-sec"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Wirkungs-Matrix</span>
<h2 class="af-h2">Wo der Hebel <span class="serif">am größten</span> ist.</h2>
<p class="af-sub">Jede Abteilung profitiert anders. Die Matrix zeigt, wo Relationflow den stärksten Effekt entfaltet.</p></div>
<div class="af-wrap"><div class="af-matrix"><table class="af-mtable"><thead>{mhead}</thead><tbody>{mbody}</tbody></table></div>
<div class="af-mleg"><span><i class="af-l1"></i> spürbar</span><span><i class="af-l2"></i> stark</span><span><i class="af-l3"></i> sehr stark</span><span><i class="af-l4"></i> maximal</span></div></div></section>

<section class="af-sec" style="background:var(--bg-alt)"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Blueprint</span>
<h2 class="af-h2">Wie aus einer Frage ein <span class="serif">Ergebnis</span> wird.</h2>
<p class="af-sub">Jeder Anwendungsfall folgt demselben sicheren Ablauf &ndash; nachvollziehbar von Auslöser bis Audit-Log.</p></div>
<div class="af-wrap"><div class="af-flow">{flow_html}</div></div></section>

<section class="af-sec"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Galerie</span>
<h2 class="af-h2">Über 60 Use Cases. <span class="serif">Ein</span> Workspace.</h2>
<p class="af-sub">Ein Auszug dessen, was Teams heute schon mit Relationflow erledigen.</p></div>
<div class="af-gal">{galrow(g1,'')}{galrow(g2,'rev')}</div></section>

<section class="af-sec" style="background:var(--bg-alt)"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Nach Branche</span>
<h2 class="af-h2">Gemacht für <span class="serif">regulierte</span> Branchen.</h2>
<p class="af-sub">Wo Datenschutz und Nachvollziehbarkeit zählen, spielt Relationflow seine Stärken aus.</p></div>
<div class="af-wrap"><div class="af-indgrid">{ind_html}</div></div></section>

<section class="af-sec"><div class="af-wrap"><div class="af-dark af-story-bg"><div class="af-wrap">
<div class="af-story"><div><span class="af-ey"><span class="dot"></span>Kundenstory</span>
<p class="sq" style="margin-top:22px">&bdquo;Was früher einen halben Tag dauerte, erledigt unser Vertrieb jetzt vor dem Mittagessen &ndash; und die Qualität ist besser.&ldquo;</p>
<div class="sby"><div class="sav">SK</div><div><b>Sabine Krüger</b><span>Vertriebsleitung, Mittelständler (180 MA)</span></div></div></div>
<div class="af-storymetrics">
<div class="af-sm"><b>−85%</b><div class="sl">Zeit pro Angebot</div></div>
<div class="af-sm"><b>+22%</b><div class="sl">Abschlussquote</div></div>
<div class="af-sm"><b>4 Std</b><div class="sl">gespart pro Tag &amp; Team</div></div>
<div class="af-sm"><b>1 Tag</b><div class="sl">bis produktiv</div></div></div></div>
</div></div></div></section>

<section class="af-sec"><div class="af-wrap"><div class="af-dark af-board-bg"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Live-Wirkung</span>
<h2 class="af-h2" style="color:#fff">Was Teams Woche für Woche <span class="serif">realisieren</span>.</h2>
<p class="af-sub">Aggregierte Effekte über alle Anwendungsfälle hinweg.</p>
<div class="af-bgrid">{board_html}</div>
<div class="af-tape"><div class="af-tapetrack">{tape_html}</div></div>
</div></div></div></section>

<section class="af-sec" style="background:var(--bg-alt)"><div class="af-wrap af-center">
<span class="af-ey"><span class="dot"></span>Vorher / Nachher</span>
<h2 class="af-h2">Derselbe Job. <span class="serif">Ein Bruchteil</span> der Zeit.</h2>
<p class="af-sub">Wähle einen Anwendungsfall und vergleiche den Aufwand &ndash; manuell gegen Relationflow.</p>
<div class="af-vstoggle" id="afVsToggle">{vs_buttons}</div></div>
<div class="af-wrap" id="afVsPanels">{vs_panels}</div></section>
'''

JS = '''
<script>
(function(){
 var bar=document.getElementById('afDeptBar');
 if(bar){bar.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
  bar.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
  var d=b.dataset.d;document.querySelectorAll('#afPanels .af-panel').forEach(function(p){p.classList.toggle('on',p.dataset.p===d)});});}
 var vt=document.getElementById('afVsToggle');
 if(vt){vt.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
  vt.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
  var n=b.dataset.vs;document.querySelectorAll('#afVsPanels .af-vspanel').forEach(function(p){var on=p.dataset.vs===n;p.classList.toggle('on',on);p.style.display=on?'':'none';});});}
 // count-up
 var seen=new WeakSet();
 function run(el){var to=parseFloat(el.dataset.to),suf=el.dataset.suffix||'',t0=null;
  function step(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1400,1);var v=Math.floor((1-Math.pow(1-p,3))*to);
   el.textContent=v.toLocaleString('de-DE')+suf;if(p<1)requestAnimationFrame(step);else el.textContent=to.toLocaleString('de-DE')+suf;}
  requestAnimationFrame(step);}
 var io=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting&&!seen.has(e.target)){seen.add(e.target);run(e.target);}})},{threshold:.4});
 document.querySelectorAll('.count').forEach(function(el){io.observe(el)});
})();
</script>
'''

# ---------- splice into base ----------
s = src
s = re.sub(r'<title>.*?</title>', '<title>Anwendungsfälle – relationflow.io</title>', s, 1)
s = re.sub(r'(<meta name="description" content=").*?(")',
           r'\1Über 60 konkrete KI-Anwendungsfälle für Vertrieb, Marketing, Support, Operations, IT und HR – DSGVO-konform mit Relationflow.\2', s, 1)
# inject CSS
s = s.replace('</style></head>', CSS + '\n</style></head>', 1)
# replace body sections (uc-hero .. before footer)
s = re.sub(r'<section class="uc-hero">.*?(?=<footer)', BODY, s, count=1, flags=re.S)
# add JS before </body>
s = s.replace('</body>', JS + '</body>', 1)

open('relationflow_anwendungsfaelle.html','w').write(s)

import re as r2
print('sections', s.count('</section>'), len(r2.findall(r'<section', s)))
print('div', s.count('<div'), s.count('</div>'))
print('panels', s.count('class="af-panel'), 'depts', s.count('data-d='), 'vs', s.count('data-vs='))
