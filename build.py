"""Génère les pages du concept TraderSZ (HTML statique, CSS partagé)."""
from pathlib import Path
import time
V = str(int(time.time()))
R = Path(__file__).parent
PAGES = [("index.html", "Home"), ("free-resources.html", "Free resources"), ("method.html", "Method"), ("premium.html", "Premium"), ("about.html", "About")]
X = "https://x.com/trader1sz"; YT = "https://www.youtube.com/@TraderSZ"; REG = "https://tradersz.com/register/"; LOGIN = "https://www.tradersz.com/login/"

def head(title, desc):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — TraderSZ</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Raleway:wght@500;600;700;800&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<script>(function(){{var p=localStorage.getItem("tz-theme")||"dark";var t=p==="auto"?(matchMedia("(prefers-color-scheme: light)").matches?"light":"dark"):p;document.documentElement.setAttribute("data-theme",t);document.documentElement.setAttribute("data-pref",p)}})()</script>
<link rel="stylesheet" href="assets/site.css?v={V}"></head><body>'''

def nav(cur):
    links = "".join(f'<li><a href="{f}" class="{"on" if f == cur else ""}">{n}</a></li>' for f, n in PAGES[1:])
    return f'''<nav class="top"><div class="wrap"><a href="index.html"><img src="assets/logo_thumb.png" alt="TraderSZ"></a><ul>{links}</ul>
<div class="navcta"><div class="theme" role="group" aria-label="Theme">
<button data-t="light"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><span>Light</span></button>
<button data-t="dark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><span>Dark</span></button>
<button data-t="auto"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="14" rx="2"/><path d="M8 22h8"/></svg><span>Auto</span></button></div><a class="btn btn-g" href="{LOGIN}">Log in</a><a class="btn btn-p" href="premium.html">Join premium</a></div></div></nav>'''

XSVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.6 8.7L23 22h-6.8l-5.3-6.9L4.8 22H1.7l8.1-9.3L0 2h7l4.8 6.3L18.9 2zm-1.2 18h1.9L6.4 3.9H4.4L17.7 20z"/></svg>'

def band():
    return f'''<div class="band"><div class="wrap"><div><div class="eyebrow">Premium access</div><h2>Trade the week with the full picture.</h2></div>
<div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn btn-p" href="premium.html">See what's included · £77.99/mo</a><a class="btn btn-g" href="{X}" target="_blank">{XSVG} Follow @trader1sz</a></div></div></div>'''

def footer():
    return f'''<footer><div class="wrap"><div class="cols">
<div><img src="assets/logo_thumb.png" alt="TraderSZ" style="height:32px;opacity:.9"><p class="disc">Trading involves substantial risk and is not suitable for every investor. Nothing on this site is financial advice or a recommendation to buy or sell any instrument. Past performance is not indicative of future results. TraderSZ is GDPR compliant; personal data is used only to administer your enquiry or membership and is removed on request.</p></div>
<div><h4>Site</h4><ul><li><a href="free-resources.html">Free resources</a></li><li><a href="method.html">Method</a></li><li><a href="premium.html">Premium</a></li><li><a href="about.html">About</a></li></ul></div>
<div><h4>Follow</h4><ul><li><a href="{X}" target="_blank" class="x">{XSVG} @trader1sz</a></li><li><a href="{YT}" target="_blank">YouTube · TraderSZ</a></li><li><a href="https://www.tradingview.com/ideas/tradersz" target="_blank">TradingView</a></li></ul></div>
<div><h4>Members</h4><ul><li><a href="{LOGIN}">Log in</a></li><li><a href="{REG}">Register</a></li><li><a href="https://www.tradersz.com/cigar-lounge/">Cigar Lounge</a></li></ul></div></div>
<div class="bottom"><span>© 2026 TraderSZ. All rights reserved.</span><span><a href="https://www.tradersz.com/disclaimer/">Disclaimer</a> · <a href="https://www.tradersz.com/terms-conditions/">Terms</a> · <a href="https://www.tradersz.com/privacy-policy/">Privacy</a></span></div></div></footer>
<script>(function(){{var b=document.querySelectorAll(".theme button");function apply(p){{localStorage.setItem("tz-theme",p);var t=p==="auto"?(matchMedia("(prefers-color-scheme: light)").matches?"light":"dark"):p;document.documentElement.setAttribute("data-theme",t);b.forEach(function(x){{x.classList.toggle("on",x.dataset.t===p)}})}}b.forEach(function(x){{x.onclick=function(){{apply(x.dataset.t)}}}});apply(localStorage.getItem("tz-theme")||"dark");matchMedia("(prefers-color-scheme: light)").addEventListener("change",function(){{if(localStorage.getItem("tz-theme")==="auto")apply("auto")}})}})()</script></body></html>'''

def candles():
    return '''<svg viewBox="0 0 640 360" style="position:absolute;inset:0;width:100%;height:100%" preserveAspectRatio="none">
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5bd3c7" stop-opacity=".18"/><stop offset="1" stop-color="#5bd3c7" stop-opacity="0"/></linearGradient></defs>
<g stroke="rgba(255,255,255,.06)"><path d="M0 90H640M0 180H640M0 270H640"/></g>
<path d="M0 250 L80 230 L160 245 L240 190 L320 205 L400 150 L480 165 L560 110 L640 125 V360 H0Z" fill="url(#g)"/>
<g stroke-width="2" stroke="#ff6b6b" fill="#ff6b6b"><path d="M40 170v80"/><rect x="34" y="185" width="12" height="40"/><path d="M120 150v70"/><rect x="114" y="160" width="12" height="40"/><path d="M280 125v70"/><rect x="274" y="140" width="12" height="38"/><path d="M440 95v60"/><rect x="434" y="105" width="12" height="35"/></g>
<g stroke-width="2" stroke="#39d98a" fill="#39d98a"><path d="M80 180v70"/><rect x="74" y="195" width="12" height="40"/><path d="M160 200v60"/><rect x="154" y="210" width="12" height="35"/><path d="M200 140v90"/><rect x="194" y="150" width="12" height="60"/><path d="M240 120v60"/><rect x="234" y="130" width="12" height="35"/><path d="M320 150v70"/><rect x="314" y="160" width="12" height="45"/><path d="M360 100v80"/><rect x="354" y="110" width="12" height="55"/><path d="M400 90v60"/><rect x="394" y="100" width="12" height="35"/><path d="M480 110v60"/><rect x="474" y="120" width="12" height="40"/><path d="M520 60v80"/><rect x="514" y="70" width="12" height="55"/><path d="M560 50v60"/><rect x="554" y="60" width="12" height="35"/><path d="M600 70v70"/><rect x="594" y="80" width="12" height="45"/></g>
<path d="M0 230 L640 112" stroke="#5bd3c7" stroke-dasharray="6 6" stroke-width="1.5" fill="none"/>
<rect x="560" y="52" width="70" height="18" rx="4" fill="#5bd3c7"/><text x="595" y="65" font-size="11" font-family="Lato" font-weight="700" fill="#06241f" text-anchor="middle">BTCUSD</text></svg>'''

PLAY = '<span style="position:absolute;inset:0;display:grid;place-items:center"><span style="width:76px;height:76px;border-radius:50%;background:rgba(91,211,199,.95);display:grid;place-items:center;box-shadow:0 20px 50px rgba(0,0,0,.5)"><svg width="26" height="26" viewBox="0 0 24 24" fill="#06241f"><path d="M7 4l13 8-13 8z"/></svg></span></span>'

def line(pts): return f'<svg viewBox="0 0 300 90" preserveAspectRatio="none"><polyline fill="none" stroke="#5bd3c7" stroke-width="2" points="{pts}"/></svg>'
UP = "0,70 30,62 60,66 90,48 120,52 150,36 180,40 210,24 240,30 270,14 300,18"; DN = "0,30 30,38 60,28 90,46 120,40 150,58 180,50 210,62 240,54 270,70 300,64"; MID = "0,60 30,56 60,62 90,50 120,54 150,44 180,48 210,38 240,42 270,30 300,34"

def icon(d): return f'<div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{d}</svg></div>'
I_CAL = icon('<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/>'); I_CH = icon('<path d="M4 19V5M4 15l5-5 4 4 7-8"/>'); I_SEND = icon('<path d="M4 4l16 8-16 8 4-8z"/>'); I_LIVE = icon('<circle cx="12" cy="12" r="9"/><path d="M8 12h8M12 8v8"/>')


def xpost(text, meta, href):
    return f'''<a class="quote" href="{href}" target="_blank" style="gap:12px"><div class="who"><div class="av">SZ</div><div><b>TraderSZ</b>@trader1sz · {meta}</div></div><p style="font-size:15px">{text}</p></a>'''
XFEED = '''<div style="display:grid;gap:16px">''' + xpost("If you missed #Bitcoin for Ledges live stream you can catch the recording here. Covered: $BTC $SOL $ZEC $PUMP $ICP and a few others.", "Pinned · Oct 20, 2026 · 139.9K views", "https://x.com/trader1sz/status/2112655441423483107") + xpost("Just saying how it is based on the SOL/xxx and SOL/USD charts. Until that proves otherwise it says SOL should do well. Open to being wrong, and will change mind at the time if the time comes.", "Nov 7, 2026", "https://x.com/trader1sz") + f'''<a class="btn btn-g" href="{X}" target="_blank" style="justify-self:start">{XSVG} See all posts on X</a></div>'''

SEEN = f'''<section class="alt"><div class="wrap"><div class="eyebrow">Seen on X</div><h2>Charts first, opinions second. Since 2014.</h2>
<p class="lead">Public analysis is posted every day to one of the largest trading audiences on X. Premium members get the private feed, where the same ideas are managed through the week.</p>
<div class="grid g3" style="margin-top:40px;align-items:start">
<div style="display:grid;gap:22px">
<div class="card"><div class="amount" style="font-size:44px">693K<span style="font-size:16px"> followers</span></div><p style="margin-top:8px">on X, <a href="{X}" target="_blank" style="color:var(--accent)">@trader1sz</a>, posting since October 2014.</p></div>
<div class="card"><div class="amount" style="font-size:44px">60K+<span style="font-size:16px"> subscribers</span></div><p style="margin-top:8px">on YouTube, home of the <i>Bitcoin for Ledges</i> live streams.</p></div>
<div class="quote"><p>“You did call the top on $PONS akhi, I remember well. Too many of the CT shills were saying it was going to moon.”</p><div class="who"><div class="av">C</div><div><b>ChimpZoo</b>@ThinkingBitmex · reply on X, Nov 2026</div></div></div>
</div>
<div style="grid-column:span 2" class="card"><div class="eyebrow" style="margin-bottom:16px">Latest from X</div>{XFEED}</div>
</div></div></section>'''

# ---------- HOME ----------
home = head("Pure price action", "TraderSZ: price action analysis on FX, crypto, indices and commodities. Weekly outlook, trade journals, private feed.") + nav("index.html") + f'''
<header class="hero"><div class="wrap"><div>
<div class="eyebrow">FX · Crypto · Indices · Commodities</div>
<h1>Read the market in <em>its own language.</em></h1>
<p>Pure price action, charted live and explained in full. Weekly outlooks, trade journals and a private feed where every idea is managed in real time, from entry to exit.</p>
<div class="cta"><a class="btn btn-p" href="premium.html">Join premium · £77.99/mo</a><a class="btn btn-g" href="free-resources.html">▶ Watch free analysis</a></div>
<div class="note"><b>Not a signal service.</b> You learn how the chart is read, you see the trades taken, and you make your own decisions.</div></div>
<a class="player" href="https://player.vimeo.com/video/240484992" target="_blank"><span class="tag">How we approach the market · 4:31</span>{candles()}{PLAY}<span style="position:absolute;left:14px;bottom:14px;font-size:13px;color:var(--muted);z-index:2">Weekly outlook · recorded live</span></a>
</div></header>
<div class="ticker"><div class="wrap"><div><b>1</b> weekly outlook live, with Q&amp;A</div><div><b>3</b> trade-journal videos a week</div><div><b>24/7</b> private X feed, setups in real time</div><div><b>693K</b> followers on X</div></div></div>
<section><div class="wrap"><div class="eyebrow">What premium gives you</div><h2>Everything a week of trading needs, on one page.</h2>
<p class="lead">The content has always been here. Premium simply puts it in order: plan the week, follow the trades, review what happened, ask your questions.</p>
<div class="grid g4" style="margin-top:44px">
<a class="card" href="premium.html">{I_CAL}<h3>Weekly outlook</h3><p>One live session at the end of each trading week to map the week ahead, followed by open Q&amp;A.</p></a>
<a class="card" href="premium.html">{I_CH}<h3>Trade journals</h3><p>Up to three videos a week going over the trades taken, the reasoning behind them and the setups forming next.</p></a>
<a class="card" href="premium.html">{I_SEND}<h3>Private X feed</h3><p>Chart setups posted as price unfolds, and the same ideas updated and managed in real time during the week.</p></a>
<a class="card" href="premium.html">{I_LIVE}<h3>Live sessions</h3><p>Regular sessions through the month to ask questions and cover instruments the week's videos did not.</p></a>
</div></div></section>
{SEEN}
<section><div class="wrap two" style="display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:start">
<div><div class="eyebrow">The method</div><h2>No indicators. Just price, structure and patience.</h2><p class="lead">Every video follows the same discipline, so you learn to see what we see rather than wait for a call.</p><a class="btn btn-g" href="method.html" style="margin-top:24px">Read the method →</a></div>
<div class="steps">
<div class="step"><div><h3>Map the structure</h3><p>Higher-timeframe levels first: where price has turned before, where liquidity sits, where the week is likely to be decided.</p></div></div>
<div class="step"><div><h3>Wait for price to speak</h3><p>A setup is only a setup once price confirms it at the level. We show the ones we take and the ones we skip, and why.</p></div></div>
<div class="step"><div><h3>Journal every trade</h3><p>Entries, exits, management and mistakes, on video, during the week. The review is where the learning happens.</p></div></div>
</div></div></section>
<section class="alt" style="padding-top:72px"><div class="wrap"><div class="eyebrow">Free resources</div><h2>Start with the free library.</h2><p class="lead">Public videos and chart breakdowns by market. No account needed.</p>
<div class="grid g3" style="margin-top:44px">
<a class="card" href="free-resources.html#crypto"><div style="display:flex;justify-content:space-between;align-items:center"><h3 style="margin:0">Crypto</h3><span style="color:var(--accent);font-weight:700;font-size:14px">Videos · Charts →</span></div><div class="chart">{line(UP)}</div></a>
<a class="card" href="free-resources.html#fx"><div style="display:flex;justify-content:space-between;align-items:center"><h3 style="margin:0">FX</h3><span style="color:var(--accent);font-weight:700;font-size:14px">Videos · Charts →</span></div><div class="chart">{line(DN)}</div></a>
<a class="card" href="free-resources.html#stocks"><div style="display:flex;justify-content:space-between;align-items:center"><h3 style="margin:0">Stocks &amp; indices</h3><span style="color:var(--accent);font-weight:700;font-size:14px">Videos · Charts →</span></div><div class="chart">{line(MID)}</div></a>
</div></div></section>
{band()}
''' + footer()

# ---------- FREE RESOURCES ----------
def vid(chip, title, desc, pts, href):
    th = line(pts).replace("viewBox", 'style="opacity:.5" viewBox')
    return f'<a class="vid" href="{href}" target="_blank"><div class="thumb">{th}</div><div><span class="chip">{chip}</span><h3>{title}</h3><p>{desc}</p></div></a>'
free = head("Free resources", "Free price action videos and chart breakdowns on crypto, FX, stocks and indices by TraderSZ.") + nav("free-resources.html") + f'''
<header class="phero"><div class="wrap"><div class="eyebrow">Free resources</div><h1>The public library. <em>No account needed.</em></h1><p>Videos and chart breakdowns by market, plus the concepts used in every one of them. Start here, then decide if premium is for you.</p>
<div class="tabs"><a href="#crypto" class="on">Crypto</a><a href="#fx">FX</a><a href="#stocks">Stocks &amp; indices</a><a href="#concepts">Concepts</a></div></div></header>
<section id="crypto" style="padding-bottom:48px"><div class="wrap"><div class="eyebrow">Crypto</div><h2>Bitcoin and the majors, week by week.</h2><p class="lead">Public outlooks from the <i>Bitcoin for Ledges</i> live streams and standalone chart breakdowns.</p>
<div style="margin-top:28px">
{vid("Live stream", "Bitcoin for Ledges · latest recording", "Weekly live outlook on BTC, SOL, ZEC and others, recorded on YouTube.", UP, YT)}
{vid("Charts", "Crypto chart breakdowns", "Marked-up charts with the levels that matter, updated as the week unfolds.", MID, "https://www.tradersz.com/crypto-charts/")}
{vid("Videos", "Crypto video library", "Every public crypto video, newest first.", DN, "https://www.tradersz.com/crypto-videos/")}
</div></div></section>
<section id="fx" class="alt"><div class="wrap"><div class="eyebrow">FX</div><h2>Majors, crosses and the dollar.</h2>
<div style="margin-top:28px">
{vid("Charts", "FX chart breakdowns", "DXY, EUR, GBP, JPY and the crosses, with higher-timeframe structure first.", DN, "https://www.tradersz.com/fx-charts/")}
{vid("Videos", "FX video library", "Public FX analysis and trade reviews.", MID, "https://www.tradersz.com/fx-videos/")}
</div></div></section>
<section id="stocks" style="padding-bottom:48px"><div class="wrap"><div class="eyebrow">Stocks &amp; indices</div><h2>ES, NQ and the names that move them.</h2>
<div style="margin-top:28px">
{vid("Charts", "Stocks &amp; indices charts", "Index futures and single names, same method, same levels.", UP, "https://www.tradersz.com/stocks-charts/")}
{vid("Videos", "Stocks video library", "Public stock and index analysis.", MID, "https://www.tradersz.com/stock-videos/")}
</div></div></section>
<section id="concepts" class="alt"><div class="wrap two" style="display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center">
<div><div class="eyebrow">Concepts</div><h2>The vocabulary behind every video.</h2><p class="lead">Structure, liquidity, ledges, triggers: short explanations of the terms used in the analysis, so nothing in a video is a mystery.</p><a class="btn btn-g" href="https://www.tradersz.com/concepts/" style="margin-top:24px">Open the concepts →</a></div>
<div class="grid g2"><div class="card"><h3 style="margin:0 0 6px">Ledges</h3><p>Where price paused before, and where it is likely to react again.</p></div><div class="card"><h3 style="margin:0 0 6px">Structure</h3><p>Higher highs, lower lows, and what a break of either actually means.</p></div><div class="card"><h3 style="margin:0 0 6px">Triggers</h3><p>The confirmation at a level that turns an idea into a trade.</p></div><div class="card"><h3 style="margin:0 0 6px">Management</h3><p>Partial exits, stops, and when to leave a trade alone.</p></div></div>
</div></section>
{band()}''' + footer()

# ---------- METHOD ----------
method = head("Method", "How TraderSZ reads the market: pure price action, structure, patience, and a journal of every trade.") + nav("method.html") + f'''
<header class="phero"><div class="wrap"><div class="eyebrow">The method</div><h1>No indicators. <em>Just price, structure and patience.</em></h1><p>Over a decade of reading charts the same way, across FX, crypto, indices and commodities. This is how every video, every live session and every post is built.</p></div></header>
<section><div class="wrap two" style="display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start">
<div class="steps">
<div class="step"><div><h3>Map the structure</h3><p>Start from the higher timeframes. Where has price turned before? Where is liquidity resting? Where will the week most likely be decided? Levels are drawn before the week opens, not after.</p></div></div>
<div class="step"><div><h3>Wait for price to speak</h3><p>A level is not a trade. A setup only exists once price confirms it at the level, with a trigger you can name. The videos show the ones taken and the ones skipped, and why.</p></div></div>
<div class="step"><div><h3>Manage, don't hope</h3><p>Partial exits, stops that move for a reason, and the discipline to leave a working trade alone. Management is shown live in the private feed as it happens.</p></div></div>
<div class="step"><div><h3>Journal every trade</h3><p>Entries, exits, mistakes and lessons, on video, during the week. Reviewing is where the learning actually happens, for members and for us.</p></div></div>
</div>
<div style="display:grid;gap:22px">
<div class="card"><div class="eyebrow" style="margin-bottom:10px">Why pure price action</div><p style="color:var(--ink);font-size:17px">Indicators are derived from price, with a delay. Reading price directly removes the delay and the false confidence. One chart, one language, every market.</p></div>
<div class="card"><div class="eyebrow" style="margin-bottom:10px">What you will not find here</div><ul class="ticks" style="margin:0"><li>Buy and sell signals to copy blindly</li><li>Guaranteed returns or performance promises</li><li>A new system every month</li></ul></div>
<div class="card"><div class="eyebrow" style="margin-bottom:10px">What you will</div><ul class="ticks" style="margin:0"><li>The same process, applied every week, in public</li><li>Trades explained before, during and after</li><li>Questions answered live</li></ul></div>
</div></div></section>
<section class="alt"><div class="wrap"><div class="eyebrow">Markets</div><h2>One method, four markets.</h2>
<div class="grid g4" style="margin-top:36px">
<div class="card"><h3 style="margin:0 0 6px">Crypto</h3><p>BTC, ETH, SOL and the names in play. The <i>Bitcoin for Ledges</i> live stream every week.</p></div>
<div class="card"><h3 style="margin:0 0 6px">FX</h3><p>Majors, crosses and the dollar index, where structure is cleanest.</p></div>
<div class="card"><h3 style="margin:0 0 6px">Indices</h3><p>ES, NQ and the levels that decide the session.</p></div>
<div class="card"><h3 style="margin:0 0 6px">Commodities</h3><p>Gold, oil and whatever is trending, when the chart is readable.</p></div>
</div></div></section>
{band()}''' + footer()

# ---------- PREMIUM ----------
premium = head("Premium access", "TraderSZ premium: weekly outlook live, trade-journal videos, private X feed and live sessions. £77.99 a month.") + nav("premium.html") + f'''
<header class="phero"><div class="wrap"><div class="eyebrow">Premium access</div><h1>Trade the week <em>with the full picture.</em></h1><p>Everything that makes the week readable: the outlook before it starts, the trades as they happen, the review when it ends, and a live room for your questions.</p></div></header>
<section><div class="wrap"><div class="price">
<div><span class="pill">Premium access</span><div class="amount" style="margin:18px 0 6px">£77.99 <span>/ month</span></div>
<p class="muted">Renews every 30 days. Pay by card, or in Bitcoin by messaging <a href="{X}" style="color:var(--accent)">@trader1sz</a>.</p>
<div style="display:flex;gap:14px;margin-top:26px;flex-wrap:wrap"><a class="btn btn-p" href="{REG}">Join premium</a><a class="btn btn-g" href="{LOGIN}">Member log in</a></div>
<p class="note" style="margin-top:18px"><b>Not a signal service.</b> Decisions, sizing and risk remain yours.</p></div>
<div><h3 style="font-size:20px">Included every month</h3><ul>
<li>Weekly outlook video, live with Q&amp;A, for the week ahead</li><li>Up to three trade-journal videos a week</li><li>Private X feed with chart setups in real time</li><li>Regular live sessions across the month</li><li>Access to the Cigar Lounge member area</li><li>Full free library, FX, crypto, stocks and concepts</li></ul></div>
</div></div></section>
<section class="alt"><div class="wrap"><div class="eyebrow">A week inside</div><h2>What a member's week looks like.</h2>
<div class="grid g4" style="margin-top:36px">
<div class="card"><span class="chip">Sunday</span><h3 style="margin:6px 0">Outlook, live</h3><p>The week ahead mapped on every market, levels drawn, then open Q&amp;A.</p></div>
<div class="card"><span class="chip">Mon – Fri</span><h3 style="margin:6px 0">Private feed</h3><p>Setups posted as price reaches the levels. Entries, stops and management updated in real time.</p></div>
<div class="card"><span class="chip">Midweek</span><h3 style="margin:6px 0">Trade journals</h3><p>Up to three videos on the trades taken, what worked, what did not, and what is forming next.</p></div>
<div class="card"><span class="chip">Monthly</span><h3 style="margin:6px 0">Live sessions</h3><p>Ask anything. Cover the instruments the week missed. Watch charts being read in real time.</p></div>
</div></div></section>
<section><div class="wrap" style="max-width:820px"><div class="eyebrow">Questions</div><h2>Before you join.</h2><div style="margin-top:28px">
<details open><summary>Is this a signal service?</summary><p>No. You see the analysis, the trades taken and the reasoning, so you can learn to read price yourself. Decisions, sizing and risk remain yours.</p></details>
<details><summary>Which markets are covered?</summary><p>FX, crypto, indices and commodities. Live sessions through the month pick up any instrument the week's videos did not cover.</p></details>
<details><summary>How is the content delivered?</summary><p>Videos and live sessions inside the member area, plus a private X feed. Add your X handle when you register so access can be granted.</p></details>
<details><summary>Can I pay in Bitcoin?</summary><p>Yes. Message @trader1sz on X to arrange it; otherwise the £77.99 monthly plan renews automatically every 30 days.</p></details>
<details><summary>Can I cancel?</summary><p>Membership renews every 30 days and can be stopped from your account before the next renewal.</p></details>
</div></div></section>
{band()}''' + footer()

# ---------- ABOUT ----------
about = head("About", "TraderSZ: price action trader, posting charts since 2014.") + nav("about.html") + f'''
<header class="phero"><div class="wrap two" style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center">
<div><div class="eyebrow">About</div><h1>SZ. <em>Charts since 2014.</em></h1><p>Over a decade reading charts, one of the most followed price action traders on X. The charts have always been public. The site is where the full process lives.</p>
<div style="display:flex;gap:14px;margin-top:26px;flex-wrap:wrap"><a class="btn btn-p" href="{X}" target="_blank">{XSVG} Follow @trader1sz</a><a class="btn btn-g" href="{YT}" target="_blank">YouTube</a></div></div>
<div class="grid g2"><div class="card"><div class="amount" style="font-size:40px">2014</div><p style="margin-top:6px">posting charts on X</p></div><div class="card"><div class="amount" style="font-size:40px">693K</div><p style="margin-top:6px">followers on X</p></div><div class="card"><div class="amount" style="font-size:40px">60K+</div><p style="margin-top:6px">YouTube subscribers</p></div><div class="card"><div class="amount" style="font-size:40px">4</div><p style="margin-top:6px">markets, one method</p></div></div>
</div></header>
<section><div class="wrap two" style="display:grid;grid-template-columns:1fr 1fr;gap:56px">
<div><div class="eyebrow">The story</div><h2>Charts first, opinions second.</h2><p class="lead" style="margin-bottom:16px">TraderSZ started as a chart account. Levels, structure, no noise. It grew because the charts were posted before the move, not after, and because the misses were posted too.</p><p class="lead">The premium side exists for one reason: the public feed shows the chart, the private side shows the whole trade, from the plan on Sunday to the review on Friday.</p></div>
<div class="quote" style="align-self:start"><p>“You did call the top on $PONS akhi, I remember well. Too many of the CT shills were saying it was going to moon.”</p><div class="who"><div class="av">C</div><div><b>ChimpZoo</b>@ThinkingBitmex · reply on X, Nov 2026</div></div></div>
</div></section>
<section class="alt"><div class="wrap"><div class="eyebrow">Live from X</div><h2>The public feed.</h2>
<div class="card" style="margin-top:28px">{XFEED}</div></div></section>
{band()}''' + footer()

for name, html in (("index.html", home), ("free-resources.html", free), ("method.html", method), ("premium.html", premium), ("about.html", about)):
    (R / name).write_text(html)
print("ok")
