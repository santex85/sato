#!/usr/bin/env python3
"""Собирает /root/projects/sato-page/index.html — лендинг Sato AI Studio на EN/RU/TH с переключателем (24.11.2026).
Тексты: content.py (EN, RU), th.json (TH через Typhoon, проверено обратным переводом). Без внешних скриптов; шрифты Google Fonts."""
import html
import json
import os
import sys

B = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B)
from content import C  # noqa: E402

TH = json.load(open(os.path.join(B, "th.json"), encoding="utf-8"))
L = {"en": {}, "ru": {}, "th": {}}
for k, en, ru in C:
    L["en"][k], L["ru"][k], L["th"][k] = en, ru, TH.get(k, en)
WA = os.environ.get("LANDING_WA", "")  # номер WhatsApp — только после «да» Александра


def t(k, tag="span", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-k="{k}">{html.escape(L["en"][k])}</{tag}>'


svc = "".join(
    f'<article class="card{" main" if i == 1 else ""}"><div class="ic">{ic}</div>{t(f"s{i}_t", "h3")}{t(f"s{i}_d", "p")}</article>'
    for i, ic in zip(range(1, 8), ["💬", "🛠", "🟩", "⚙️", "🤝", "🏗", "🤖"]))
how = "".join(f'<li><span class="n">{i}</span><div>{t(f"h{i}_t", "h3")}{t(f"h{i}_d", "p")}</div></li>' for i in range(1, 5))
prices = "".join(
    f'<div class="price{" hi" if i == 1 else ""}">{t(f"p{i}_t", "h3")}<div class="pv">{t(f"p{i}_v")}</div>{t(f"p{i}_d", "p")}</div>'
    for i in range(1, 5))
wa_btn = (f'<a class="btn wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{t("c_wa")}</a>' if WA else "")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sato AI Studio — guest assistants for hotels on Koh Samui</title>
<meta name="description" content="AI studio on Koh Samui: a guest assistant for hotels, villas and tour operators in WhatsApp, LINE and on your website, in English, Thai and Russian.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Noto+Sans+Thai:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f6f3ec;--card:#fffdf8;--ink:#1f2a27;--mut:#5d6a64;--acc:#1f6f5c;--acc2:#e6f0ec;--line:#e1dbcd}}
@media (prefers-color-scheme:dark){{:root{{--bg:#121816;--card:#1a2220;--ink:#e7ece9;--mut:#9fb0a8;--acc:#4fb89c;--acc2:#1e2c28;--line:#2a3430}}}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 Inter,'Noto Sans Thai',system-ui,sans-serif}}
:lang(th) body,body.th{{font-family:'Noto Sans Thai',Inter,system-ui,sans-serif}}
a{{color:var(--acc)}} .wrap{{max-width:1080px;margin:0 auto;padding:0 20px}}
header{{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
.bar{{display:flex;align-items:center;gap:18px;height:64px}} .logo{{font-weight:700;font-size:18px;color:var(--ink);text-decoration:none;display:flex;align-items:center;gap:10px}}
.logo i{{display:inline-block;width:30px;height:30px;border-radius:8px;background:var(--acc);color:#fff;font-style:normal;text-align:center;line-height:30px;font-size:15px}}
nav{{display:flex;gap:18px;margin-left:auto}} nav a{{color:var(--mut);text-decoration:none;font-size:15px}} nav a:hover{{color:var(--ink)}}
.lang{{display:flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}} .lang button{{border:0;background:transparent;color:var(--mut);padding:6px 11px;font:600 13px Inter,sans-serif;cursor:pointer}}
.lang button.on{{background:var(--acc);color:#fff}}
.hero{{padding-top:72px;padding-bottom:48px}} .kick{{color:var(--acc);font-weight:600;letter-spacing:.04em;text-transform:uppercase;font-size:13px}}
h1{{font-size:clamp(30px,5vw,50px);line-height:1.15;margin:12px 0 18px;max-width:820px}} .sub{{font-size:18px;color:var(--mut);max-width:760px}}
.cta{{display:flex;gap:12px;flex-wrap:wrap;margin:28px 0 22px}} .btn{{display:inline-block;padding:13px 20px;border-radius:12px;font-weight:600;text-decoration:none;border:1px solid var(--acc)}}
.btn.p{{background:var(--acc);color:#fff}} .btn.s{{color:var(--acc);background:transparent}}
.badges{{display:flex;gap:10px;flex-wrap:wrap}} .badges span{{background:var(--acc2);color:var(--ink);padding:7px 12px;border-radius:999px;font-size:14px}}
section{{padding:56px 0;border-top:1px solid var(--line)}} h2{{font-size:clamp(24px,3.4vw,34px);margin:0 0 26px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px}} .card.main{{border-color:var(--acc);box-shadow:0 0 0 1px var(--acc) inset}}
.card h3{{margin:10px 0 8px;font-size:19px}} .card p{{margin:0;color:var(--mut)}} .ic{{font-size:26px}}
ol.steps{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}}
.steps li{{display:flex;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px}} .steps h3{{margin:0 0 6px;font-size:17px}} .steps p{{margin:0;color:var(--mut);font-size:15px}}
.n{{flex:none;width:34px;height:34px;border-radius:50%;background:var(--acc);color:#fff;font-weight:700;display:grid;place-items:center}}
.prices{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}} .price{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px}}
.price.hi{{border:2px solid var(--acc)}} .price h3{{margin:0 0 10px;font-size:17px}} .pv{{font-size:26px;font-weight:700;color:var(--acc);margin-bottom:8px}} .price p{{margin:0;color:var(--mut);font-size:15px}}
.pay{{margin-top:18px;color:var(--mut)}} .who{{max-width:820px;color:var(--mut);font-size:17px}}
.contact{{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:30px}} .contact p{{color:var(--mut);max-width:640px}}
.btns{{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px}} .btn.line{{background:#06c755;border-color:#06c755;color:#fff}} .btn.wa{{background:#25d366;border-color:#25d366;color:#fff}} .btn.mail{{color:var(--acc)}}
footer{{padding:30px 0 40px;color:var(--mut);font-size:14px}}
@media (max-width:760px){{nav{{display:none}} .hero{{padding-top:44px;padding-bottom:32px}} .sub{{font-size:16px}}}}
</style>
</head>
<body>
<header><div class="wrap bar">
<a class="logo" href="#top"><i>S</i>Sato AI Studio</a>
<nav><a href="#services">{t("nav_services")}</a><a href="#how">{t("nav_how")}</a><a href="#prices">{t("nav_prices")}</a><a href="#contact">{t("nav_contact")}</a></nav>
<div class="lang" role="group" aria-label="Language"><button data-l="en">EN</button><button data-l="ru">RU</button><button data-l="th">ไทย</button></div>
</div></header>
<main id="top">
<div class="wrap hero">
{t("hero_kicker", "div", "kick")}
{t("hero_title", "h1")}
{t("hero_sub", "p", "sub")}
<div class="cta"><a class="btn p" href="#contact">{t("hero_cta")}</a><a class="btn s" href="#services">{t("hero_cta2")}</a></div>
<div class="badges">{t("badge1")}{t("badge2")}{t("badge3")}</div>
</div>
<section id="services"><div class="wrap">{t("svc_title", "h2")}<div class="grid">{svc}</div></div></section>
<section id="how"><div class="wrap">{t("how_title", "h2")}<ol class="steps">{how}</ol></div></section>
<section id="prices"><div class="wrap">{t("price_title", "h2")}<div class="prices">{prices}</div>{t("pay", "p", "pay")}</div></section>
<section id="who"><div class="wrap">{t("who_title", "h2")}{t("who_d", "p", "who")}</div></section>
<section id="contact"><div class="wrap"><div class="contact">{t("contact_title", "h2")}{t("contact_d", "p")}
<div class="btns"><a class="btn line" href="https://line.me/R/ti/p/@809fhrze" target="_blank" rel="noopener">{t("c_line")}</a>{wa_btn}<a class="btn mail" href="mailto:prenoagent@gmail.com?subject=Free%20check">{t("c_mail")}: prenoagent@gmail.com</a></div>
</div></div></section>
</main>
<footer><div class="wrap">{t("footer")}</div></footer>
<script>
const L={json.dumps(L, ensure_ascii=False)};
function setLang(l){{
  if(!L[l]) l="en";
  document.documentElement.lang=l; document.body.classList.toggle("th", l==="th");
  document.querySelectorAll("[data-k]").forEach(e=>{{const v=L[l][e.dataset.k]; if(v) e.textContent=v;}});
  document.querySelectorAll(".lang button").forEach(b=>b.classList.toggle("on", b.dataset.l===l));
  try{{localStorage.setItem("lang",l)}}catch(e){{}}
}}
document.querySelectorAll(".lang button").forEach(b=>b.addEventListener("click",()=>setLang(b.dataset.l)));
let start="en"; try{{start=localStorage.getItem("lang")||""}}catch(e){{}}
if(!start){{const n=(navigator.language||"en").slice(0,2); start=(n==="th"||n==="ru")?n:"en";}}
const q=new URLSearchParams(location.search).get("lang"); if(q) start=q;
setLang(start);
</script>
</body>
</html>
"""
open(os.path.join(os.path.dirname(B), "index.html"), "w", encoding="utf-8").write(page)
print("index.html:", len(page), "знаков; WhatsApp:", "есть" if WA else "нет (ждёт «да»)")
