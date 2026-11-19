#!/usr/bin/env python3
"""The Commons Bookstore — template-v2 T1 site builder (8 files, 6 core pages).
Facts only, source-gated (card t_b3c6cb99): Kansas City Star 2026-11-17 (Noelle
Alviz-Gransee) + GBP listing (phone) + makefullystudios.com (email provenance).
Design: paper/ink letterpress title-page identity — deliberately NOT the dark
espresso sibling look. No photos used (press photos are the Star's).
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public")

SITE = "The Commons"
SITE_T = "The Commons Bookstore"          # search-disambiguating title form
CITY = "Kansas City, MO"
ORIGIN = "https://commons-bookstore-kc-demo.up.railway.app"   # pinned demo host
ADDR_STREET = "5508 Troost Ave"
ADDR_FULL = "5508 Troost Ave, Kansas City, MO 64110"
ADDR_CITY = "Kansas City, MO 64110"
EMAIL = "hello@makefullystudios.com"
PHONE_D = "(816) 200-1545"
PHONE_T = "+18162001545"
PHONE_LD = "+1-816-200-1545"
LAT, LON = 39.0269358, -94.5739132         # Nominatim: 5508 Troost Ave, KC MO 64110
HOURS = "Wed–Sat, 11am–7pm"
NEWS_URL = "https://www.kansascity.com/news/business/openings-closings/article318067776.html"
MAP_Q = "5508%20Troost%20Ave%2C%20Kansas%20City%2C%20MO%2064110"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=5508%20Troost%20Ave%2C%20Kansas%20City%2C%20MO%2064110"
MAP_VIEW = "https://www.google.com/maps?q=" + MAP_Q
BUILT = "BUILT-2026-11-19"

# ------------------------------------------------------------------ shared parts
def head(title, desc, path, noindex=False):
    canonical = ORIGIN + path
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<!-- {BUILT} -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_T}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
  <div class="wrap headrow">
    <a class="brand" href="/">The Commons<span class="brandtag">Bookstore · 5508 Troost Ave · Kansas City</span></a>
    <nav aria-label="Main">
      <a href="/">Home</a>
      <a href="/shelves">The shelves</a>
      <a href="/nonfiction">Nonfiction</a>
      <a href="/kids-and-events">Kids &amp; events</a>
      <a class="btn ghost sm" href="/contact">Say hello</a>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOTER = f"""</main>
<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <h4>The Commons</h4>
        <address class="nap">Nonfiction-first bookstore · {ADDR_STREET}<br>
        {ADDR_CITY}<br>
        Open {HOURS}<br>
        <a href="tel:{PHONE_T}">{PHONE_D}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></address>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/shelves">The shelves</a></li>
          <li><a href="/nonfiction">Nonfiction &amp; big ideas</a></li>
          <li><a href="/kids-and-events">Kids &amp; events</a></li>
          <li><a href="/contact">Visit &amp; contact</a></li>
          <li><a href="/privacy">Privacy</a></li>
        </ul>
      </div>
      <div>
        <h4>Find Us</h4>
        <ul>
          <li><a href="{DIRS}" target="_blank" rel="noopener">Get directions</a></li>
          <li><a href="{MAP_VIEW}" target="_blank" rel="noopener">See the map</a></li>
          <li><a href="mailto:{EMAIL}">Email the shop</a></li>
        </ul>
      </div>
    </div>
    <div class="footline"><span>© 2026 The Commons · {ADDR_STREET}, {ADDR_CITY}</span>
    <span>Opened November 11, 2026 · {HOURS}</span></div>
  </div>
</footer>
</body>
</html>
"""

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'

def breadcrumb(trail):
    items = ", ".join(f'{{"@type":"ListItem","position":{i+1},"name":{json.dumps(n)},"item":{json.dumps(ORIGIN+p)}}}' for i,(n,p) in enumerate(trail))
    return ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":json.loads("["+items+"]")})

def faq(pairs):
    q = [{"@type":"Question","name":n,"acceptedAnswer":{"@type":"Answer","text":a}} for n,a in pairs]
    return {"@type":"FAQPage","mainEntity":q}

def crumbbar(trail):
    parts = ' › '.join(f'<a href="{p}">{n}</a>' if i < len(trail)-1 else n for i,(n,p) in enumerate(trail))
    return f'<nav class="crumbs" aria-label="Breadcrumb">{parts}</nav>\n'

STORE_LD = {
  "@context":"https://schema.org","@type":"BookStore",
  "name":"The Commons",
  "alternateName":["The Commons Bookstore","Commons Bookstore"],
  "description":"Nonfiction-focused independent bookstore with children's titles, gifts and community events, opened November 11, 2026 at 5508 Troost Ave, Kansas City, MO.",
  "url":ORIGIN+"/",
  "telephone":PHONE_LD,
  "image":ORIGIN+"/og.png",
  "foundingDate":"2026-11-11",
  "address":{"@type":"PostalAddress","streetAddress":ADDR_STREET,"addressLocality":"Kansas City","addressRegion":"MO","postalCode":"64110","addressCountry":"US"},
  "geo":{"@type":"GeoCoordinates","latitude":LAT,"longitude":LON},
  "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Wednesday","Thursday","Friday","Saturday"],"opens":"11:00","closes":"19:00"}],
  "hasMap":MAP_VIEW,
}

FAQS = [
  ("When is The Commons open?",
   "Wednesday through Saturday, 11am to 7pm. The bookstore opened November 11, 2026 at 5508 Troost Ave."),
  ("What kind of books do you carry?",
   "Mostly nonfiction — memoirs and biographies, books on society, culture and power, elections and politics and systems — plus historical fiction, cookbooks, psychology, travel, United States history, children's books and gifts."),
  ("Where exactly is the store?",
   "5508 Troost Ave, Kansas City, MO 64110 — on the block with Hi-Hope's Ice Cream and Blackhole Bakery."),
  ("Is there a children's section?",
   "Yes — a children's reading nook and children's titles of all ages throughout the shop."),
  ("Do you host events?",
   "Events are being planned: discussions led by people with community expertise, and craft events like cross-stitching or make-your-own zine workshops. Email " + EMAIL + " to join one or propose a topic."),
]

def faq_markup():
    rows = "".join(f"<div class='fq'><h3>{q}</h3><p>{a}</p></div>" for q,a in FAQS)
    return rows

# ------------------------------------------------------------------ pages
def page_home():
    h = head(
      "The Commons Bookstore — Nonfiction, Kids' Books & Community, Kansas City MO",
      "New nonfiction-focused bookstore on Troost Ave, Kansas City MO. Memoirs, society and power, politics, kids' books and gifts. Open Wed–Sat, 11am–7pm.",
      "/")
    body = f"""<section class="hero">
  <div class="wrap titlepage">
    <p class="eyebrow">Nonfiction-first bookstore · opened Nov 11, 2026 · Kansas City, MO</p>
    <h1>Books for people asking better questions.</h1>
    <p class="lede">The Commons is a new nonfiction-focused bookstore on Troost Avenue —
    memoirs and biographies, books on society, culture and power, politics and systems,
    plus children's titles, historical fiction, cookbooks and gifts.</p>
    <p class="colophon">Open {HOURS} · {ADDR_FULL} · <a href="tel:{PHONE_T}">{PHONE_D}</a></p>
    <p class="ctarow"><a class="btn" href="/shelves">Browse the shelves</a>
    <a class="btn ghost" href="/contact">Visit &amp; contact</a></p>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow">What's on the shelves</p>
    <h2>A shop sorted by the questions it asks</h2>
    <p class="narrow-l">Owner Anna Jordan-Douglass shelved the store around the way she reads:
    interesting people first, then the systems around them. Every section is her own curation,
    chosen for readers who want to dig into “how did we get to where we are today?”</p>
    <div class="grid">
      <a class="scard" style="--c:var(--brick)" href="/nonfiction">
        <span class="spine"></span>
        <h3>Nonfiction &amp; big ideas</h3>
        <p>Memoirs and biographies, society/culture/power, racism and systemic issues,
        elections, politics and systems — the heart of the shop.</p><span class="more">See the shelves →</span></a>
      <a class="scard" style="--c:var(--green)" href="/kids-and-events">
        <span class="spine"></span>
        <h3>Children's books &amp; the reading nook</h3>
        <p>Titles for all ages, a dedicated reading nook, and a shop built next door to a studio
        that designs media with children.</p><span class="more">See the shelves →</span></a>
      <a class="scard" style="--c:var(--gold)" href="/kids-and-events">
        <span class="spine"></span>
        <h3>Community events (coming)</h3>
        <p>Discussion nights led by locals with real expertise, cross-stitch, make-your-own
        zine workshops — being scheduled now.</p><span class="more">See the plan →</span></a>
      <a class="scard" style="--c:var(--navy)" href="/shelves">
        <span class="spine"></span>
        <h3>Historical fiction, cookbooks, travel &amp; gifts</h3>
        <p>Psychology, United States history and well-chosen gifts sprinkled through
        the whole store.</p><span class="more">See the shelves →</span></a>
    </div>
  </div>
</section>
<section class="band">
  <div class="wrap narrow">
    <p class="eyebrow">The story behind the counter</p>
    <blockquote>“It started to drive what became this idea of I have to pivot my thinking
    a little bit, but also how do I use my skills to make sure people care about learning?”
    And then: “one day it hit me that I love books and I could just do all of that,
    but in the context of a bookstore.”</blockquote>
    <p class="cite">Anna Jordan-Douglass, founder of The Commons — to The Kansas City Star,
    <a href="{NEWS_URL}" target="_blank" rel="noopener">November 17, 2026</a></p>
    <p>The Commons shares its Troost Avenue building with Makefully, the educational media
    company Jordan-Douglass founded — co-designed with children, and at work with organizations
    like PBS KIDS and Fred Rogers Productions. The bookshop grew from the same instinct:
    education, connection and community, in one welcoming room.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow">Good to know before you visit</p>
    <h2>Questions, answered</h2>
    <div class="qlist">{faq_markup()}</div>
    <p class="ctarow"><a class="btn" href="/contact">Plan your visit</a></p>
  </div>
</section>
"""
    meta = (ld(STORE_LD)
      + ld({"@context":"https://schema.org", **faq(FAQS)})
      + breadcrumb([("The Commons Bookstore","/")]))
    return h + body + meta + FOOTER

def page_shelves():
    h = head(
      "The Shelves — Every Section at The Commons Bookstore, Kansas City MO",
      "Browse every section of The Commons bookstore on Troost Ave: memoirs, society and power, politics, history, cookbooks, psychology, travel, children's books and gifts.",
      "/shelves")
    secs = [
      ("brick", "Memoirs &amp; biographies", "The “interesting people” wall — lives told from the inside, sorted by what they can teach."),
      ("green", "Society, culture &amp; power", "Books on scandalous people and stories, racism, and systemic issues — the section next to the biographies."),
      ("gold", "Elections, politics &amp; systems", "A lot on how power actually operates: elections, politics and the systems that shape them."),
      ("navy", "United States history &amp; historical fiction", "Digging deeper into how we got here — nonfiction history alongside strong historical fiction."),
      ("plum", "Psychology &amp; the mind", "Titles on how people think, feel and change."),
      ("brick", "Cookbooks &amp; food writing", "Because a good kitchen book belongs on a good shelf."),
      ("green", "Travel", "Elsewhere, for when Troost isn't enough."),
      ("gold", "Children's books", "Titles for all ages throughout the shop, with a children's reading nook of their own."),
      ("navy", "Gifts", "Well-chosen gifts sprinkled throughout — easy to find, hard to put back down."),
    ]
    rows = "".join(f'<div class="srow srow-{c}"><h3>{t}</h3><p>{d}</p></div>' for c,t,d in secs)
    items = [{"@type":"ListItem","position":i+1,"name":t.replace("&amp;","and")} for i,(c,t,d) in enumerate(secs)]
    body = f"""{crumbbar([("Home","/"),("The shelves","/shelves")])}
<section>
  <div class="wrap">
    <p class="eyebrow">The shelves</p>
    <h1>Every section, on purpose</h1>
    <p class="lede">The Commons is mostly nonfiction — but “mostly” hides how deliberate the
    shelves are. The selection is curated, section by section, by the shop's owner. Here is
    the whole store at a glance.</p>
    <div class="shelves">{rows}</div>
    <p>Two corners deserve their own page: the <a href="/nonfiction">nonfiction core</a> —
    memoirs, society and power, politics and systems — and the
    <a href="/kids-and-events">children's books and the events being planned</a>.</p>
    <p class="ctarow"><a class="btn" href="/contact">Ask for a recommendation</a></p>
  </div>
</section>
"""
    meta = (ld({"@context":"https://schema.org","@type":"ItemList","name":"The shelves at The Commons Bookstore","itemListElement":items})
      + breadcrumb([("Home","/"),("The shelves","/shelves")]))
    return h + body + meta + FOOTER

def page_nonfiction():
    h = head(
      "Nonfiction, Memoirs & Big Ideas — The Commons Bookstore, Kansas City MO",
      "The nonfiction core of The Commons on Troost Ave: memoirs and biographies, society culture and power, racism and systemic issues, elections, politics and systems.",
      "/nonfiction")
    body = f"""{crumbbar([("Home","/"),("The shelves","/shelves"),("Nonfiction & big ideas","/nonfiction")])}
<section>
  <div class="wrap">
    <p class="eyebrow">The core of the shop</p>
    <h1>Nonfiction, memoirs &amp; the big questions</h1>
    <p class="lede">Walk in looking for a good memoir and you'll find the whole reason this
    store exists: books about how people, and the systems around them, actually work.</p>
    <h2>Sorted the way the owner reads</h2>
    <dl class="ruled">
      <div><dt>Interesting people — memoirs &amp; biographies</dt>
      <dd>Lives worth learning from, told from the inside. This is the first wall the shop
      organized, and still its center of gravity.</dd></div>
      <div><dt>Society, culture &amp; power</dt>
      <dd>“Books on a range of topics from scandalous people or stories to books on racism
      or systemic issues” — the section next to the biographies.</dd></div>
      <div><dt>Elections, politics &amp; systems</dt>
      <dd>A lot on how decisions get made and who they get made for.</dd></div>
      <div><dt>The long view</dt>
      <dd>United States history, psychology and travel — shelved alongside, because
      “there's a lot that is digging deeper into, ‘how did we get to where we are today?’
      There's some good stuff in there.”</dd></div>
    </dl>
    <p class="cite">Quotations: Anna Jordan-Douglass describing her own shelves,
    The Kansas City Star, <a href="{NEWS_URL}" target="_blank" rel="noopener">Nov 17, 2026</a>.</p>
  </div>
</section>
<section class="band">
  <div class="wrap narrow">
    <p class="eyebrow">Reading lists, made on request</p>
    <blockquote>“I've kind of sorted a lot of books (by): interesting people, memoirs and
    biographies, and then the section next to that: society, culture, and power.”</blockquote>
    <p>Tell us the question you're chewing on and we'll point you at the shelf —
    at the counter, or by email at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <p class="ctarow"><a class="btn" href="/contact">Ask the shop</a></p>
  </div>
</section>
"""
    svc = {"@context":"https://schema.org","@type":"Service",
      "serviceType":"Book curation — nonfiction, memoirs and ideas",
      "name":"Nonfiction, memoirs & big ideas",
      "description":"Curated nonfiction: memoirs and biographies, society/culture/power, racism and systemic issues, elections and politics and systems, United States history.",
      "provider":{"@type":"BookStore","name":"The Commons","url":ORIGIN+"/","telephone":PHONE_LD,
        "address":{"@type":"PostalAddress","streetAddress":ADDR_STREET,"addressLocality":"Kansas City","addressRegion":"MO","postalCode":"64110","addressCountry":"US"}},
      "areaServed":{"@type":"City","name":"Kansas City"},"url":ORIGIN+"/nonfiction"}
    meta = (ld(svc)
      + breadcrumb([("Home","/"),("The shelves","/shelves"),("Nonfiction & big ideas","/nonfiction")]))
    return h + body + meta + FOOTER

def page_kids():
    h = head(
      "Children's Books & Community Events — The Commons Bookstore, Kansas City MO",
      "A children's reading nook, titles for all ages, and community events in the works — discussions, cross-stitch and zine workshops — at The Commons, Kansas City MO.",
      "/kids-and-events")
    body = f"""{crumbbar([("Home","/"),("The shelves","/shelves"),("Kids & events","/kids-and-events")])}
<section>
  <div class="wrap">
    <p class="eyebrow">For young readers — and for gathering</p>
    <h1>Children's books &amp; community events</h1>
    <p class="lede">The Commons was built next door to a room where children help design
    media. Kids' books were never going to be an afterthought here.</p>
    <h2>The reading nook</h2>
    <p>Children's titles run throughout the shop, with a dedicated reading nook — small
    readers pick their own books, get comfortable, and read. It was the first corner of the
    store the Kansas City Star photographed when the shop opened November 11, 2026.</p>
    <h2>Next door: a studio co-designed with children</h2>
    <p>The bookshop shares its building with Makefully, the educational media company owner
    Anna Jordan-Douglass founded — a company that works with organizations like PBS KIDS and
    Fred Rogers Productions, and keeps a workshop room where children test and improve the
    games and designs. The shop's kids' shelf, and its attitude toward learning, grew from
    the same work.</p>
    <h2>Events in the works</h2>
    <p>Still early days — but the plan is already taking shape, in Anna's own words:</p>
    <dl class="ruled">
      <div><dt>Discussion nights</dt>
      <dd>“Where interesting people in the community can lead discussions on their
      expertise” — with room to let people gather and talk while they do something.</dd></div>
      <div><dt>Craft events</dt>
      <dd>Cross-stitching, make-your-own zine workshops and similar gatherings.</dd></div>
      <div><dt>Have a topic or a craft to teach?</dt>
      <dd>Email <a href="mailto:{EMAIL}">{EMAIL}</a> — the event schedule is being built
      now, and proposals are welcome.</dd></div>
    </dl>
    <p class="cite">Quotations: Anna Jordan-Douglass, The Kansas City Star,
    <a href="{NEWS_URL}" target="_blank" rel="noopener">Nov 17, 2026</a>.</p>
    <p class="ctarow"><a class="btn" href="/contact">Say hello to the shop</a></p>
  </div>
</section>
"""
    svc = {"@context":"https://schema.org","@type":"Service",
      "serviceType":"Children's books and community events",
      "name":"Children's books & community events",
      "description":"A children's reading nook and titles for all ages, plus planned community discussions and craft workshops like cross-stitch and make-your-own zines.",
      "provider":{"@type":"BookStore","name":"The Commons","url":ORIGIN+"/","telephone":PHONE_LD,
        "address":{"@type":"PostalAddress","streetAddress":ADDR_STREET,"addressLocality":"Kansas City","addressRegion":"MO","postalCode":"64110","addressCountry":"US"}},
      "areaServed":{"@type":"City","name":"Kansas City"},"url":ORIGIN+"/kids-and-events"}
    meta = (ld(svc)
      + breadcrumb([("Home","/"),("The shelves","/shelves"),("Kids & events","/kids-and-events")]))
    return h + body + meta + FOOTER

def page_contact():
    h = head(
      "Visit The Commons Bookstore — 5508 Troost Ave, Kansas City MO",
      "Find The Commons bookstore at 5508 Troost Ave, Kansas City MO 64110. Open Wed–Sat 11am–7pm. Call (816) 200-1545 or send the shop a note.",
      "/contact")
    body = f"""{crumbbar([("Home","/"),("Visit & contact","/contact")])}
<section>
  <div class="wrap">
    <p class="eyebrow">Come by</p>
    <h1>Visit The Commons</h1>
    <div class="visitgrid">
      <div class="vcard">
        <h3>The shop</h3>
        <p class="vlines">{ADDR_STREET}<br>{ADDR_CITY}<br>
        Open {HOURS}</p>
        <p class="vlines"><a href="tel:{PHONE_T}">{PHONE_D}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <span class="fine">(the studio shares this address — say “bookstore” and it reaches us)</span></p>
        <p class="vlines"><a href="{DIRS}" target="_blank" rel="noopener">Get directions</a> ·
        <a href="{MAP_VIEW}" target="_blank" rel="noopener">Open in Google Maps</a></p>
        <p>On the Troost block with Hi-Hope's Ice Cream and Blackhole Bakery —
        yes, that means the ice cream is next door.</p>
      </div>
      <div class="mapframe">
        <iframe src="{MAP_VIEW}&amp;output=embed" title="Map: The Commons Bookstore, {ADDR_FULL}" loading="lazy"></iframe>
      </div>
    </div>
  </div>
</section>
<section>
  <div class="wrap narrow">
    <p class="eyebrow">Or write to us</p>
    <h2>Send the shop a note</h2>
    <p>Looking for a title? Want a reading list? Have a craft or a topic for the first
    events? This form goes straight to the shop.</p>
    <form class="cform" action="/contact" method="post">
      <label for="f-name">Your name</label>
      <input id="f-name" name="name" type="text" maxlength="120" required autocomplete="name">
      <label for="f-phone">Phone <span class="opt">(optional)</span></label>
      <input id="f-phone" name="phone" type="tel" maxlength="60" autocomplete="tel">
      <label for="f-email">Email <span class="opt">(optional)</span></label>
      <input id="f-email" name="email" type="email" maxlength="120" autocomplete="email">
      <label for="f-message">Your message</label>
      <textarea id="f-message" name="message" rows="5" maxlength="4000" required></textarea>
      <p class="ctarow"><button class="btn" type="submit">Send note</button></p>
      <p class="fine">We reply by the method you give us. See our <a href="/privacy">privacy note</a> for what happens to what you send.</p>
    </form>
  </div>
</section>
"""
    meta = (ld(STORE_LD)
      + breadcrumb([("Home","/"),("Visit & contact","/contact")]))
    return h + body + meta + FOOTER

def page_privacy():
    h = head(
      "Privacy — The Commons Bookstore, Kansas City MO",
      "How The Commons bookstore handles what you send: no trackers, no cookies, no third-party scripts — just the contact note you write us.",
      "/privacy")
    body = f"""{crumbbar([("Home","/"),("Privacy","/privacy")])}
<section>
  <div class="wrap narrow">
    <p class="eyebrow">Plain words about your data</p>
    <h1>Privacy</h1>
    <p>This site sets no cookies and runs no third-party scripts, no analytics and no
    trackers. Pages are static; the stylesheet is served from this site.</p>
    <h2>What the contact form collects</h2>
    <p>The form asks for your name, and optionally your phone and email, plus your message.
    That information is delivered to the shop by an email service (Brevo) purely so the
    owner can answer you. It is used to reply to your note and nothing else — no lists,
    no advertising.</p>
    <h2>Map embed</h2>
    <p>The visit page embeds a Google Maps frame so you can find the shop. Google may log
    requests for that frame under its own privacy policy.</p>
    <h2>Hosting</h2>
    <p>The site is hosted on Railway. Server logs record basic request and contact-form
    events to keep the site running.</p>
    <h2>Questions</h2>
    <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and the shop will answer.</p>
  </div>
</section>
"""
    meta = breadcrumb([("Home","/"),("Privacy","/privacy")])
    return h + body + meta + FOOTER

def page_thanks():
    h = head(
      "Thank you — The Commons",
      "Your note has reached The Commons bookstore, Kansas City MO.",
      "/thanks", noindex=True)
    body = """<section>
  <div class="wrap narrow">
    <p class="eyebrow">Message sent</p>
    <h1>Thank you — your note is on its way to the shop</h1>
    <p>The Commons answers Wed–Sat, while the store is open. If it's urgent,
    the counter phone is the fastest way to a human.</p>
    <p class="ctarow"><a class="btn" href="/">Back to the front page</a></p>
  </div>
</section>
"""
    return h + body + FOOTER

def page_404():
    h = head(
      "Page not found — The Commons Bookstore",
      "That page moved or never existed. Find the shelves, the visit page or the front door of The Commons bookstore, Kansas City MO.",
      "/404", noindex=True)
    body = """<section>
  <div class="wrap narrow">
    <p class="eyebrow">404</p>
    <h1>This shelf is empty</h1>
    <p>The page you asked for isn't here. The useful doors are below:</p>
    <ul class="links404">
      <li><a href="/">Front page</a></li>
      <li><a href="/shelves">The shelves</a></li>
      <li><a href="/nonfiction">Nonfiction &amp; big ideas</a></li>
      <li><a href="/kids-and-events">Kids' books &amp; events</a></li>
      <li><a href="/contact">Visit &amp; contact</a></li>
    </ul>
  </div>
</section>
"""
    return h + body + FOOTER

# ------------------------------------------------------------------ assets
STYLE = """/* The Commons Bookstore — paper/ink letterpress identity (hand-rolled, no builders) */
:root{
  --paper:#f7f2e7; --paper2:#efe6d4; --card:#fffdf7;
  --ink:#241d14; --ink2:#463c2c; --mute:#6d6250;
  --rule:#d9cfba; --rule2:#a99b80;
  --brick:#a5432a; --green:#33604a; --gold:#8a6d35; --navy:#2d4a6b; --plum:#6b4a63;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  --sans:"Avenir Next",Avenir,"Helvetica Neue",Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{color-scheme:light}
body{background:var(--paper);color:var(--ink);font:17px/1.65 var(--serif)}
a{color:var(--brick)}
a:hover{color:var(--green)}
.wrap{max-width:1060px;margin:0 auto;padding:0 24px}
.narrow{max-width:720px}
.skip{position:absolute;left:-9999px}
.skip:focus{left:12px;top:12px;background:var(--brick);color:var(--paper);padding:8px 14px;z-index:9}

header{background:var(--paper);border-bottom:3px double var(--rule2)}
.headrow{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px 22px;padding-top:14px;padding-bottom:14px}
.brand{font:700 23px/1.1 var(--serif);color:var(--ink);text-decoration:none;display:flex;flex-direction:column;letter-spacing:.01em}
.brandtag{font:600 10px/1.6 var(--sans);letter-spacing:.22em;text-transform:uppercase;color:var(--mute);margin-top:4px}
nav{display:flex;flex-wrap:wrap;align-items:center;gap:4px 20px;font:600 13px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase}
nav a{color:var(--ink);text-decoration:none;padding:8px 0;border-bottom:1px solid transparent}
nav a:hover{color:var(--brick)}
nav a[aria-current="page"]{color:var(--brick);border-bottom-color:var(--brick)}

.btn{display:inline-block;background:var(--brick);color:var(--paper);font:700 14px/1.2 var(--sans);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;padding:14px 22px;border:1px solid var(--brick);border-radius:2px;cursor:pointer}
.btn:hover{background:var(--green);border-color:var(--green);color:var(--paper)}
.btn.ghost{background:transparent;color:var(--ink);border-color:var(--rule2)}
.btn.ghost:hover{border-color:var(--brick);color:var(--brick)}
.btn.sm{padding:9px 14px;font-size:12px}
button.btn{font-family:var(--sans)}
.ctarow{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}

.eyebrow{font:700 12px/1.8 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:var(--brick)}
h1{font:700 clamp(34px,5.4vw,56px)/1.08 var(--serif);letter-spacing:-.01em;margin:14px 0 18px;max-width:21ch}
h2{font:700 clamp(23px,3.4vw,33px)/1.2 var(--serif);margin:0 0 18px;max-width:26ch}
h3{font:700 21px/1.3 var(--serif);margin-bottom:10px}
p{margin:14px 0;max-width:70ch}
.narrow-l{max-width:62ch}
.lede{font-size:clamp(17px,2.2vw,20px);line-height:1.6;max-width:62ch;color:var(--ink2)}
.cite{font:600 13px/1.6 var(--sans);letter-spacing:.02em;color:var(--mute);max-width:62ch}
.fine{font:13px/1.6 var(--sans);color:var(--mute)}
.opt{font:600 11px/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}

main>section{padding:56px 0;border-bottom:1px solid var(--rule)}
main>section:last-of-type{border-bottom:none}

.hero{padding:72px 0}
.titlepage{border-top:3px double var(--rule2);border-bottom:3px double var(--rule2);padding:34px 0}
.colophon{font:600 13px/1.7 var(--sans);letter-spacing:.06em;color:var(--mute);text-transform:uppercase}

.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:26px}
.scard{display:block;background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:22px 22px 18px;text-decoration:none;color:inherit;position:relative;overflow:hidden}
.scard::before{content:"";position:absolute;left:0;top:0;bottom:0;width:7px;background:var(--c,var(--brick))}
.scard h3{color:var(--ink);margin:0 0 8px}
.scard p{font-size:15px;line-height:1.55;color:var(--ink2);margin:0 0 12px}
.scard .more{font:700 12px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--brick)}
.scard:hover{border-color:var(--rule2)}

.band{background:var(--ink);color:var(--paper)}
.band a{color:var(--gold)}
.band a:hover{color:var(--paper)}
.band .eyebrow{color:var(--gold)}
.band blockquote{font:700 clamp(21px,3vw,27px)/1.35 var(--serif);margin:6px 0 14px;max-width:36ch}
.band .cite{color:#bfb29a}
.band p{color:#e8dfcb;max-width:64ch}
blockquote{font:700 clamp(21px,3vw,27px)/1.35 var(--serif);margin:6px 0 14px;max-width:36ch}

.crumbs{font:600 12px/1.6 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--mute);margin-bottom:22px}
.crumbs a{color:var(--mute);text-decoration:none}
.crumbs a:hover{color:var(--brick)}

.dl,dl.ruled{margin:18px 0 10px}
dl.ruled>div{border-bottom:1px solid var(--rule);padding:14px 2px}
dl.ruled dt{font:700 17px/1.4 var(--serif);color:var(--ink)}
dl.ruled dd{font-size:16px;color:var(--ink2);margin:4px 0 0;max-width:66ch}

.shelves{display:grid;gap:2px;margin-top:22px;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.srow{display:grid;grid-template-columns:14px 1fr;gap:16px;align-items:baseline;padding:16px 2px;border-bottom:1px solid var(--rule)}
.srow:last-child{border-bottom:none}
.srow::before{content:"";width:7px;height:100%;min-height:26px;background:var(--c,var(--brick));display:block}
.srow h3{margin:0;font-size:19px}
.srow p{margin:2px 0 0;font-size:15px;color:var(--ink2)}
.srow-brick{--c:var(--brick)} .srow-green{--c:var(--green)} .srow-gold{--c:var(--gold)} .srow-navy{--c:var(--navy)} .srow-plum{--c:var(--plum)}

.qlist{display:grid;gap:18px;margin-top:10px}
.fq{border-left:3px solid var(--rule2);padding-left:16px}
.fq h3{margin-bottom:4px;font-size:19px}
.fq p{margin:0;font-size:16px;color:var(--ink2)}

.visitgrid{display:grid;grid-template-columns:minmax(300px,1.1fr) minmax(300px,1fr);gap:26px;align-items:start;margin-top:20px}
.vcard{background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:24px}
.vlines{margin:12px 0}
.mapframe{width:100%}
.mapframe iframe{width:100%;height:360px;border:1px solid var(--rule);border-radius:3px;display:block}

.cform{display:grid;gap:6px;margin-top:18px}
.cform label{font:700 12px/1.6 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);margin-top:12px}
.cform input,.cform textarea{width:100%;padding:11px 12px;font:16px/1.5 var(--serif);color:var(--ink);background:var(--card);border:1px solid var(--rule2);border-radius:2px}
.cform input:focus,.cform textarea:focus{outline:2px solid var(--brick);outline-offset:1px}
.cform textarea{resize:vertical}

.links404{margin:18px 0 6px;padding-left:20px}
.links404 li{margin:6px 0}

footer{background:var(--ink);color:#e8dfcb;border-top:4px double var(--rule2);padding:44px 0 26px}
footer h4{font:700 19px/1.3 var(--serif);color:var(--paper);margin-bottom:10px}
footer .nap{font:15px/1.7 var(--serif);font-style:normal;color:#cfc4ad}
footer ul{list-style:none}
footer li{margin:6px 0}
footer a{color:var(--gold);text-decoration:none}
footer a:hover{color:var(--paper)}
.fgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:26px}
.footline{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px 20px;border-top:1px solid rgba(247,242,231,.18);margin-top:30px;padding-top:16px;font:13px/1.6 var(--sans);letter-spacing:.02em;color:#b3a691}

@media (max-width:640px){
  .visitgrid{grid-template-columns:1fr}
  .mapframe iframe{height:300px}
  main>section{padding:42px 0}
  .hero{padding:52px 0}
  nav{gap:2px 14px;font-size:12px}
  .grid{grid-template-columns:1fr}
}
"""

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#f7f2e7"/><rect x="3" y="3" width="58" height="58" fill="none" stroke="#241d14" stroke-width="2"/><text x="32" y="43" font-family="Georgia,serif" font-size="34" font-weight="bold" fill="#241d14" text-anchor="middle">C</text><rect x="16" y="49" width="32" height="5" fill="#a5432a"/></svg>\n'

def main():
    os.makedirs(OUT, exist_ok=True)
    pages = {
      "index.html": page_home(),
      "shelves.html": page_shelves(),
      "nonfiction.html": page_nonfiction(),
      "kids-and-events.html": page_kids(),
      "contact.html": page_contact(),
      "privacy.html": page_privacy(),
      "thanks.html": page_thanks(),
      "404.html": page_404(),
    }
    for name, doc in pages.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
            fh.write(doc)
    open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(STYLE)
    open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8").write(FAVICON)
    core = ["/", "/shelves", "/nonfiction", "/kids-and-events", "/contact", "/privacy"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in core:
        sm += f"  <url><loc>{ORIGIN}{p}</loc><lastmod>2026-11-19</lastmod></url>\n"
    sm += "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
      "User-agent: *\nAllow: /\n\nSitemap: " + ORIGIN + "/sitemap.xml\n")
    for name, doc in pages.items():
        print(f"{name:24s} {len(doc)/1024:6.1f} KB")
    print("style.css", round(len(STYLE)/1024, 1), "KB")

if __name__ == "__main__":
    main()
