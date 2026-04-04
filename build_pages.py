#!/usr/bin/env python3
"""Build all remaining v2.5 pages for Tampa Concrete Pros."""

import os

SITE = "/Users/costa.demetral/Documents/Rank and Rent $/My-RR-Sites/Tampa Concrete Pros"
PHONE = "(813) 705-9021"
PHONE_TEL = "tel:+18137059021"
DOMAIN = "https://tampaconcretepros.com"
WEB3_KEY = "0219881f-13e5-4175-b720-517b8d10c028"
NAV_LINKS = """
    <ul class="nav__links" id="navLinks">
      <li><a href="/services/">Services</a></li>
      <li><a href="/about.html">About</a></li>
      <li><a href="/locations/brandon.html">Areas</a></li>
      <li><a href="/faq.html">FAQ</a></li>
      <li><a href="/contact.html">Contact</a></li>
      <li><a href="tel:+18137059021" class="nav__cta">Call Now</a></li>
    </ul>"""

NAV = f"""<nav class="nav" id="mainNav">
  <div class="nav__inner">
    <a href="/" class="nav__logo">Tampa <span>Concrete</span> Pros</a>
    {NAV_LINKS}
    <button class="nav__toggle" id="navToggle" aria-label="Open menu">
      <svg viewBox="0 0 24 24"><path d="M3 12h18M3 6h18M3 18h18" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/></svg>
    </button>
  </div>
</nav>"""

FOOTER_LINKS = """
      <div class="footer__col">
        <h4 class="footer__heading">Services</h4>
        <ul class="footer__links">
          <li><a href="/services/driveway-installation.html">Driveway Installation</a></li>
          <li><a href="/services/driveway-replacement.html">Driveway Replacement</a></li>
          <li><a href="/services/stamped-concrete.html">Stamped Concrete</a></li>
          <li><a href="/services/pool-decks.html">Pool Decks</a></li>
          <li><a href="/services/patios-walkways.html">Patios &amp; Walkways</a></li>
          <li><a href="/services/commercial.html">Commercial</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Company</h4>
        <ul class="footer__links">
          <li><a href="/about.html">About Us</a></li>
          <li><a href="/faq.html">FAQ</a></li>
          <li><a href="/contact.html">Contact</a></li>
          <li><a href="/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="/sitemap.xml">Sitemap</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Service Areas</h4>
        <ul class="footer__links">
          <li><a href="/locations/brandon.html">Brandon</a></li>
          <li><a href="/locations/riverview.html">Riverview</a></li>
          <li><a href="/locations/south-tampa.html">South Tampa</a></li>
          <li><a href="/locations/clearwater.html">Clearwater</a></li>
          <li><a href="/locations/st-pete.html">St. Petersburg</a></li>
        </ul>
      </div>"""

def footer():
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__col footer__col--brand">
        <div class="footer__brand-name">Tampa <span>Concrete</span> Pros</div>
        <p class="footer__brand-desc">Licensed and insured concrete contractors serving Tampa, Florida and surrounding areas.</p>
        <div class="footer__contact-item"><a href="tel:+18137059021">{PHONE}</a></div>
      </div>
      {FOOTER_LINKS}
    </div>
    <div class="footer__bottom">
      <span class="footer__copy">&copy; 2026 Tampa Concrete Pros. All rights reserved.</span>
      <div class="footer__legal">
        <a href="/privacy-policy.html">Privacy Policy</a>
        <a href="/terms-of-service.html">Terms of Service</a>
        <a href="/sitemap.xml">Sitemap</a>
      </div>
    </div>
  </div>
</footer>"""

MOBILE_CTA = """<div class="mobile-cta">
  <a href="tel:+18137059021" class="mobile-cta__btn mobile-cta__btn--call">
    <svg viewBox="0 0 256 256" fill="currentColor" width="20" height="20"><path d="M222.37,158.46l-47.11-21.11-.13-.06a16,16,0,0,0-15.17,1.4,8.12,8.12,0,0,0-.75.56L134.87,160c-15.42-7.49-31.34-23.29-38.83-38.51l20.78-24.71c.2-.25.39-.5.57-.77a16,16,0,0,0,1.32-15.06l0-.12L97.54,33.64a16,16,0,0,0-16.62-9.52A56.26,56.26,0,0,0,32,80c0,79.4,64.6,144,144,144a56.26,56.26,0,0,0,55.88-48.92A16,16,0,0,0,222.37,158.46Z"/></svg>
    Call Now
  </a>
  <a href="/contact.html#contact" class="mobile-cta__btn mobile-cta__btn--estimate">Free Estimate</a>
</div>"""

SCRIPTS = """<script>
document.documentElement.classList.add("js");
const nav = document.getElementById('mainNav');
window.addEventListener('scroll', () => { nav.classList.toggle('scrolled', window.scrollY > 60); }, { passive: true });
document.getElementById('navToggle').addEventListener('click', () => { document.getElementById('navLinks').classList.toggle('open'); });
const revealEls = document.querySelectorAll('.reveal');
if (revealEls.length) {
  const io = new IntersectionObserver(entries => entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } }), { threshold: 0.1 });
  revealEls.forEach(el => io.observe(el));
}
</script>"""

CLARITY = """<script type="text/javascript">
  (function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","vqc8myokjt");
</script>"""

SCHEMA_LB = """{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Tampa Concrete Pros",
    "telephone": "+18137059021",
    "url": "https://tampaconcretepros.com",
    "address": { "@type": "PostalAddress", "streetAddress": "1801 E Camelback Rd Ste 102", "addressLocality": "Phoenix", "addressRegion": "AZ", "postalCode": "85016", "addressCountry": "US" }
  }"""

def head(title, desc, canonical, og_title=None, schema_extra=""):
    og_t = og_title or title
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{og_t}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="{DOMAIN}/images/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{DOMAIN}/images/og-image.jpg">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.v2.5.css?v=1">
  <script type="application/ld+json">
  {SCHEMA_LB}
  </script>{schema_extra}
  {CLARITY}
</head>
<body>"""

def inner_hero(badge, title, title_span=None, subtitle=""):
    if title_span:
        h1 = f'<h1 class="hero__title">{title} <span>{title_span}</span></h1>'
    else:
        h1 = f'<h1 class="hero__title">{title}</h1>'
    return f"""<section class="hero hero--inner">
  <div class="container">
    <div class="hero__content">
      <span class="hero__badge">{badge}</span>
      {h1}
      <p class="hero__subtitle">{subtitle}</p>
    </div>
  </div>
</section>"""

def cta_section():
    return """<section class="cta-section">
  <div class="container" style="text-align:center;">
    <div class="reveal">
      <span class="hero__badge" style="margin-bottom:1.5rem;display:inline-block;">Free Estimates — No Obligation</span>
      <h2 class="section-title" style="color:white;margin-bottom:1rem;">Ready to Get Started?</h2>
      <p style="color:rgba(255,255,255,0.8);margin-bottom:2rem;max-width:560px;margin-left:auto;margin-right:auto;">Call us or request a free estimate online. We respond within 24 hours.</p>
      <div class="cta__buttons">
        <a href="/contact.html#contact" class="btn btn--white">Get Free Estimate</a>
        <a href="tel:+18137059021" class="btn btn--ghost">Call (813) 705-9021</a>
      </div>
    </div>
  </div>
</section>"""

def write_page(filepath, content):
    full_path = os.path.join(SITE, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f"  Written: {filepath}")


# ====================================================
# ABOUT
# ====================================================
def build_about():
    content = head(
        "About Tampa Concrete Pros | Tampa Bay Concrete Contractors",
        "Learn about Tampa Concrete Pros — licensed concrete contractors with 15+ years serving Tampa Bay. Quality driveways, pool decks, stamped concrete and more.",
        f"{DOMAIN}/about.html"
    ) + f"""
{NAV}
{inner_hero("About Us", "Tampa's Trusted Concrete", "Specialists", subtitle="We've been serving Tampa Bay homeowners and businesses since 2009 with expert concrete work, honest pricing, and lasting results.")}

<section class="why" style="background:var(--color-surface);">
  <div class="container">
    <div class="two-col-grid reveal">
      <div>
        <span class="section-label">Our Story</span>
        <h2 class="section-title">15+ Years Building Tampa's Concrete</h2>
        <p style="color:var(--color-text-light);line-height:1.8;margin-bottom:1.5rem;">Tampa Concrete Pros was founded with one mission: bring professional-grade concrete work to Tampa Bay homeowners at fair prices. We've grown from a small crew to a full-service company handling everything from residential driveways to large commercial projects.</p>
        <p style="color:var(--color-text-light);line-height:1.8;margin-bottom:2rem;">Our team knows Florida concrete. The heat, humidity, sandy soils, and intense UV rays require a different approach than up north. Every project uses Florida-specific concrete mixes, proper drainage planning, and UV-resistant sealants.</p>
        <div style="display:flex;gap:32px;flex-wrap:wrap;margin-bottom:2rem;">
          <div style="text-align:center;">
            <div style="font-size:2.5rem;font-weight:900;color:var(--color-accent);">500+</div>
            <div style="font-size:0.875rem;color:var(--color-text-light);font-weight:600;">Projects Completed</div>
          </div>
          <div style="text-align:center;">
            <div style="font-size:2.5rem;font-weight:900;color:var(--color-accent);">15+</div>
            <div style="font-size:0.875rem;color:var(--color-text-light);font-weight:600;">Years Experience</div>
          </div>
          <div style="text-align:center;">
            <div style="font-size:2.5rem;font-weight:900;color:var(--color-accent);">22</div>
            <div style="font-size:0.875rem;color:var(--color-text-light);font-weight:600;">Cities Served</div>
          </div>
        </div>
        <a href="/contact.html#contact" class="btn btn--primary">Get a Free Estimate</a>
      </div>
      <div style="background:white;border-radius:var(--radius-lg);padding:36px;box-shadow:var(--shadow-md);">
        <h3 style="font-size:1.25rem;font-weight:800;margin-bottom:20px;">Why Choose Us</h3>
        <div style="display:flex;flex-direction:column;gap:16px;">
          <div class="why__stat">
            <div class="why__stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor"><path d="M208,36H48A20,20,0,0,0,28,56v56c0,54.29,26.32,87.22,48.4,105.29,23.71,19.39,47.44,26,48.44,26.29a12.1,12.1,0,0,0,6.32,0c1-.28,24.73-6.9,48.44-26.29,22.08-18.07,48.4-51,48.4-105.29V56A20,20,0,0,0,208,36Z"/></svg></div>
            <div><strong>Fully Licensed &amp; Insured</strong><span>Florida state contractor license. Full liability and workers' comp on every job.</span></div>
          </div>
          <div class="why__stat">
            <div class="why__stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm64-88a8,8,0,0,1-8,8H128a8,8,0,0,1-8-8V72a8,8,0,0,1,16,0v48h48A8,8,0,0,1,192,128Z"/></svg></div>
            <div><strong>On-Time Delivery</strong><span>We schedule projects carefully and complete them on time, every time.</span></div>
          </div>
          <div class="why__stat">
            <div class="why__stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm-4,48a12,12,0,1,1-12,12A12,12,0,0,1,124,72Zm12,112a16,16,0,0,1-16-16V128a8,8,0,0,1,0-16,16,16,0,0,1,16,16v40a8,8,0,0,1,0,16Z"/></svg></div>
            <div><strong>Transparent Quotes</strong><span>Written estimates with no hidden fees. What we quote is what you pay.</span></div>
          </div>
          <div class="why__stat">
            <div class="why__stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="currentColor"><path d="M243.84,76.19a16,16,0,0,0-14.09-11.06l-57.78-4.29-21.94-53.87a16,16,0,0,0-29.7-.06L98.72,60.84,40.35,65.13A16,16,0,0,0,31.27,92.6L75.73,132,62.41,188.22a16,16,0,0,0,23.84,17.39L128,181.3l41.78,24.31a16,16,0,0,0,23.82-17.44l-13.29-56.2L224.6,92.6A16,16,0,0,0,243.84,76.19Z"/></svg></div>
            <div><strong>5-Star Rated</strong><span>Hundreds of satisfied Tampa Bay customers and glowing online reviews.</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{cta_section()}
{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page("about.html", content)


# ====================================================
# FAQ
# ====================================================
def build_faq():
    schema_faq = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {"@type":"Question","name":"How much does a concrete driveway cost in Tampa?","acceptedAnswer":{"@type":"Answer","text":"A standard concrete driveway in Tampa typically costs $6–$15 per square foot for a basic broom finish. Stamped or decorative concrete runs $12–$25 per square foot. Call us at (813) 705-9021 for a free on-site estimate."}},
      {"@type":"Question","name":"How long does concrete take to cure in Tampa's climate?","acceptedAnswer":{"@type":"Answer","text":"In Tampa's warm, humid climate, concrete reaches initial set within 24–48 hours. Light foot traffic is safe after 48 hours, vehicles after 7 days. Full cure takes approximately 28 days."}},
      {"@type":"Question","name":"Do you do stamped concrete in Tampa?","acceptedAnswer":{"@type":"Answer","text":"Yes! Stamped concrete is one of our most popular services in Tampa. We offer dozens of patterns including slate, cobblestone, flagstone, and wood plank, plus custom color options."}},
      {"@type":"Question","name":"Are you licensed and insured?","acceptedAnswer":{"@type":"Answer","text":"Yes. Tampa Concrete Pros carries a Florida state contractor license, full general liability insurance, and workers' compensation coverage on every project."}},
      {"@type":"Question","name":"How long does a concrete driveway installation take?","acceptedAnswer":{"@type":"Answer","text":"Most standard driveway installations take 2–4 days from excavation to final finish. Larger projects or those with complex stamping designs may take 5–7 days. We'll give you a specific timeline during your free estimate."}},
      {"@type":"Question","name":"Do you offer free estimates?","acceptedAnswer":{"@type":"Answer","text":"Absolutely. All estimates are free and come with no obligation. We typically schedule site visits within 48 hours of your inquiry."}}
    ]
  }
  </script>"""
    
    faqs = [
        ("How much does a concrete driveway cost in Tampa?", "A standard concrete driveway in Tampa typically costs $6–$15 per square foot for a basic broom finish. Stamped or decorative concrete runs $12–$25 per square foot. Factors include driveway size, site preparation needed, thickness, and your chosen finish. Contact us for a free, detailed on-site estimate."),
        ("How long does concrete take to cure in Tampa's climate?", "In Tampa's warm, humid Florida climate, concrete reaches initial set within 24–48 hours. Light foot traffic is typically safe after 48 hours, and vehicles can drive on a new driveway after 7 days. Full structural cure takes approximately 28 days. We apply professional-grade sealant to protect against Florida's intense UV rays and heavy rain."),
        ("Do you do stamped concrete in Tampa?", "Yes — stamped concrete is one of our most popular services. We offer dozens of patterns including slate, cobblestone, flagstone, wood plank, herringbone, and fan patterns. We can match virtually any color to complement your home's exterior."),
        ("Are you licensed and insured?", "Yes. Tampa Concrete Pros carries a Florida state contractor license, full general liability insurance, and workers' compensation coverage on every project. We can provide proof of insurance before any work begins."),
        ("How long does a concrete driveway installation take?", "Most standard driveway installations take 2–4 days from excavation to final finish. Larger projects or stamped designs may take 5–7 days. We'll provide a specific timeline during your free estimate."),
        ("Do you offer free estimates?", "Yes — all estimates are free with no obligation. We typically schedule site visits within 24–48 hours of your inquiry. Just call (813) 705-9021 or fill out our online form."),
        ("How do you prevent cracking in Tampa's sandy soil?", "Sandy soil requires thorough compaction before pouring. We compact the sub-base to industry standards, use appropriate slab thickness (usually 4–6 inches), place reinforcing rebar or fiber mesh, and control joints to direct any natural cracking away from the surface."),
        ("Do you replace existing concrete driveways?", "Yes. We handle full tear-out and replacement of failing driveways, including proper disposal of old concrete, re-grading for drainage, and installing your new slab to current specifications."),
        ("What types of concrete finishes do you offer?", "We offer broom finish (most common), exposed aggregate, stamped patterns, salt finish, smooth trowel finish, and colored concrete. We'll recommend the best option for your project and Florida's climate."),
        ("Do you serve areas outside Tampa?", "Yes — we serve all of Tampa Bay including Brandon, Riverview, Clearwater, St. Petersburg, South Tampa, Westchase, New Tampa, Wesley Chapel, Lutz, and many more communities."),
    ]
    
    faq_html = ""
    for q, a in faqs:
        faq_html += f"""<div class="faq-item reveal">
      <h3 class="faq-question">{q}</h3>
      <div class="faq-answer"><p>{a}</p></div>
    </div>"""
    
    content = head(
        "FAQ | Tampa Concrete Pros — Common Questions Answered",
        "Frequently asked questions about concrete driveways, stamped concrete, pool decks and patios in Tampa, FL. Get answers from local concrete experts.",
        f"{DOMAIN}/faq.html",
        schema_extra=schema_faq
    ) + f"""
{NAV}
{inner_hero("FAQ", "Common Questions", "About Concrete in Tampa", subtitle="Everything you need to know about concrete projects in the Tampa Bay area — costs, timelines, materials, and more.")}

<section class="why" style="background:var(--color-surface);">
  <div class="container" style="max-width:820px;">
    <div class="reveal" style="margin-bottom:2rem;">
      <span class="section-label">Questions &amp; Answers</span>
      <h2 class="section-title">Frequently Asked Questions</h2>
    </div>
    {faq_html}
    <div style="background:white;border-radius:var(--radius-lg);padding:32px;margin-top:3rem;text-align:center;">
      <h3 style="font-size:1.25rem;font-weight:800;margin-bottom:12px;">Have a Question We Didn't Answer?</h3>
      <p style="color:var(--color-text-light);margin-bottom:20px;">Call us directly or fill out a free estimate request. We're happy to walk you through any project.</p>
      <div class="cta__buttons" style="justify-content:center;">
        <a href="/contact.html#contact" class="btn btn--primary">Request Free Estimate</a>
        <a href="tel:+18137059021" class="btn btn--dark">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

{cta_section()}
{footer()}
{MOBILE_CTA}
<style>
.faq-item {{ background:white; border-radius:var(--radius-md); padding:28px; margin-bottom:16px; border:1px solid rgba(0,0,0,0.06); }}
.faq-question {{ font-size:1.0625rem; font-weight:700; color:var(--color-text); margin-bottom:12px; }}
.faq-answer {{ color:var(--color-text-light); line-height:1.8; }}
</style>
{SCRIPTS}
</body>
</html>"""
    write_page("faq.html", content)


# ====================================================
# THANK YOU
# ====================================================
def build_thankyou():
    content = head(
        "Thank You | Tampa Concrete Pros",
        "Thank you for contacting Tampa Concrete Pros. We'll be in touch within 24 hours to discuss your project.",
        f"{DOMAIN}/thank-you.html"
    ) + f"""
{NAV}
<section class="hero hero--inner" style="text-align:center;">
  <div class="container">
    <div class="hero__content" style="margin:0 auto;text-align:center;">
      <div style="margin-bottom:24px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="var(--color-accent)" width="72" height="72"><path d="M173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34ZM232,128A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88,88,0,1,0-88,88A88.1,88.1,0,0,0,216,128Z"/></svg>
      </div>
      <span class="hero__badge">Message Received!</span>
      <h1 class="hero__title">Thank You for <span>Reaching Out!</span></h1>
      <p class="hero__subtitle">We received your request and will be in touch within 24 hours to discuss your concrete project and schedule a free estimate.</p>
      <div style="margin-top:2rem;display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
        <a href="/" class="btn btn--primary">Back to Home</a>
        <a href="tel:+18137059021" class="btn btn--outline">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

{cta_section()}
{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page("thank-you.html", content)


# ====================================================
# PRIVACY POLICY
# ====================================================
def build_privacy():
    content = head(
        "Privacy Policy | Tampa Concrete Pros",
        "Privacy Policy for Tampa Concrete Pros. Learn how we collect, use, and protect your personal information.",
        f"{DOMAIN}/privacy-policy.html"
    ) + f"""
{NAV}
{inner_hero("Legal", "Privacy Policy", subtitle="Last updated: January 1, 2026")}

<section class="why" style="background:var(--color-surface);">
  <div class="container" style="max-width:820px;">
    <div class="reveal" style="background:white;border-radius:var(--radius-lg);padding:48px;box-shadow:var(--shadow-sm);">
      <h2>1. Information We Collect</h2>
      <p>We collect information you provide directly to us, including your name, phone number, email address, and property address when you request a quote or contact us through our website.</p>
      <h2 style="margin-top:2rem;">2. How We Use Your Information</h2>
      <p>We use the information we collect to: respond to your inquiry, provide estimates and services, communicate about your project, and improve our website and services. We do not sell your personal information to third parties.</p>
      <h2 style="margin-top:2rem;">3. Cookies</h2>
      <p>Our website may use cookies and similar tracking technologies to enhance your experience. You can instruct your browser to refuse cookies, though some features may not function properly as a result.</p>
      <h2 style="margin-top:2rem;">4. Data Security</h2>
      <p>We implement appropriate security measures to protect your personal information. However, no method of transmission over the internet is 100% secure.</p>
      <h2 style="margin-top:2rem;">5. Contact Us</h2>
      <p>If you have questions about this Privacy Policy, please contact us at <a href="tel:+18137059021" style="color:var(--color-accent);">{PHONE}</a> or via our <a href="/contact.html" style="color:var(--color-accent);">contact form</a>.</p>
    </div>
  </div>
</section>

{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page("privacy-policy.html", content)


# ====================================================
# TERMS OF SERVICE
# ====================================================
def build_terms():
    content = head(
        "Terms of Service | Tampa Concrete Pros",
        "Terms of Service for Tampa Concrete Pros website.",
        f"{DOMAIN}/terms-of-service.html"
    ) + f"""
{NAV}
{inner_hero("Legal", "Terms of Service", subtitle="Last updated: January 1, 2026")}

<section class="why" style="background:var(--color-surface);">
  <div class="container" style="max-width:820px;">
    <div class="reveal" style="background:white;border-radius:var(--radius-lg);padding:48px;box-shadow:var(--shadow-sm);">
      <h2>1. Use of Website</h2>
      <p>By using tampaconcretepros.com, you agree to these terms. The website is for informational purposes and requesting service quotes. You must not use the site for any unlawful purpose.</p>
      <h2 style="margin-top:2rem;">2. Information Accuracy</h2>
      <p>We strive to keep information accurate, but pricing, availability, and service details may change. Contact us directly to confirm current information.</p>
      <h2 style="margin-top:2rem;">3. Intellectual Property</h2>
      <p>All content on this website including text, images, and logos is the property of Tampa Concrete Pros and may not be reproduced without written permission.</p>
      <h2 style="margin-top:2rem;">4. Limitation of Liability</h2>
      <p>Tampa Concrete Pros shall not be liable for any indirect, incidental, or consequential damages arising from your use of this website.</p>
      <h2 style="margin-top:2rem;">5. Contact</h2>
      <p>Questions about these terms? Contact us at <a href="tel:+18137059021" style="color:var(--color-accent);">{PHONE}</a>.</p>
    </div>
  </div>
</section>

{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page("terms-of-service.html", content)


# ====================================================
# 404
# ====================================================
def build_404():
    content = head(
        "Page Not Found | Tampa Concrete Pros",
        "The page you're looking for doesn't exist. Return to Tampa Concrete Pros homepage.",
        f"{DOMAIN}/404.html"
    ) + f"""
{NAV}
<section class="hero hero--inner" style="text-align:center;">
  <div class="container">
    <div class="hero__content" style="margin:0 auto;text-align:center;">
      <h1 class="hero__title" style="font-size:5rem;">404</h1>
      <p class="hero__subtitle">Oops! This page doesn't exist. Let's get you back on solid ground.</p>
      <div style="margin-top:2rem;display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
        <a href="/" class="btn btn--primary">Go to Homepage</a>
        <a href="/contact.html#contact" class="btn btn--outline">Get Free Estimate</a>
      </div>
    </div>
  </div>
</section>
{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page("404.html", content)


# ====================================================
# SERVICES INDEX
# ====================================================
def build_services_index():
    services = [
        ("driveway-installation.html", "Driveway Installation", "New concrete driveways built for Tampa's climate with proper drainage and reinforcement.", "/images/services/driveway-installation.webp"),
        ("driveway-replacement.html", "Driveway Replacement", "Full tear-out and replacement of old, cracked, or failing driveways.", "/images/services/driveway-replacement.webp"),
        ("stamped-concrete.html", "Stamped Concrete", "Decorative concrete patterns and colors for driveways, patios, and pool decks.", "/images/services/stamped-concrete.webp"),
        ("pool-decks.html", "Pool Decks", "Slip-resistant, heat-reflective pool deck surfaces built for Florida living.", "/images/services/pool-decks.webp"),
        ("patios-walkways.html", "Patios & Walkways", "Durable outdoor living spaces and concrete pathways for Tampa homes.", "/images/services/patios-walkways.webp"),
        ("commercial.html", "Commercial Concrete", "Parking lots, warehouse floors, sidewalks, and large-scale concrete projects.", "/images/services/commercial.webp"),
    ]
    cards = ""
    for href, title, desc, img in services:
        cards += f"""<div class="bento__card reveal">
        <img src="{img}" alt="{title} Tampa" loading="lazy">
        <div class="bento__content">
          <h3 class="bento__title">{title}</h3>
          <p class="bento__desc">{desc}</p>
          <a href="/services/{href}" class="btn btn--white" style="margin-top:1rem;">Learn More</a>
        </div>
      </div>"""
    
    content = head(
        "Concrete Services in Tampa, FL | Tampa Concrete Pros",
        "Concrete services in Tampa FL: driveway installation, driveway replacement, stamped concrete, pool decks, patios, and commercial work. Free estimates.",
        f"{DOMAIN}/services/"
    ) + f"""
{NAV}
{inner_hero("All Services", "Concrete Services in", "Tampa, FL", subtitle="From residential driveways to commercial concrete — we do it all across Tampa Bay.")}

<section class="services" style="padding:var(--section-pad) 0;">
  <div class="container">
    <div class="bento" style="grid-template-columns:repeat(3,1fr);">
      {cards}
    </div>
  </div>
</section>

{cta_section()}
{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page("services/index.html", content)


# ====================================================
# SERVICE PAGES
# ====================================================
def build_service_page(filename, title, h1, badge, subtitle, hero_img, intro, benefits, faq_pairs):
    faq_html = ""
    for q, a in faq_pairs:
        faq_html += f"""<div class="faq-item reveal"><h3 class="faq-question">{q}</h3><div class="faq-answer"><p>{a}</p></div></div>"""
    
    benefits_html = ""
    for b in benefits:
        benefits_html += f"""<li style="display:flex;align-items:flex-start;gap:12px;margin-bottom:12px;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="var(--color-accent)" width="20" height="20" style="flex-shrink:0;margin-top:2px;"><path d="M173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34ZM232,128A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88,88,0,1,0-88,88A88.1,88.1,0,0,0,216,128Z"/></svg>
            <span style="color:var(--color-text-light);">{b}</span></li>"""
    
    schema_svc = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{title}",
    "provider": {{
      "@type": "LocalBusiness",
      "name": "Tampa Concrete Pros",
      "telephone": "+18137059021",
      "url": "https://tampaconcretepros.com"
    }},
    "areaServed": "Tampa, FL",
    "serviceType": "{title}"
  }}
  </script>"""
    
    content = head(
        f"{title} in Tampa, FL | Tampa Concrete Pros",
        f"{intro[:150]}...",
        f"{DOMAIN}/services/{filename}",
        schema_extra=schema_svc
    ) + f"""
{NAV}
{inner_hero(badge, h1[0], h1[1] if len(h1) > 1 else "", subtitle=subtitle)}

<section class="why" style="background:var(--color-surface);">
  <div class="container">
    <div class="two-col-grid reveal">
      <div>
        <span class="section-label">{badge}</span>
        <h2 class="section-title">{title} in Tampa Bay</h2>
        <p style="color:var(--color-text-light);line-height:1.8;margin-bottom:1.5rem;">{intro}</p>
        <ul style="list-style:none;padding:0;margin-bottom:2rem;">
          {benefits_html}
        </ul>
        <a href="/contact.html#contact" class="btn btn--primary">Get Free Estimate</a>
        <a href="tel:+18137059021" class="btn btn--dark" style="margin-left:12px;">Call {PHONE}</a>
      </div>
      <div style="border-radius:var(--radius-lg);overflow:hidden;min-height:360px;">
        <img src="{hero_img}" alt="{title} Tampa FL" style="width:100%;height:100%;object-fit:cover;">
      </div>
    </div>
  </div>
</section>

<section class="why" style="background:var(--color-white);">
  <div class="container" style="max-width:820px;">
    <div class="reveal" style="margin-bottom:2rem;">
      <span class="section-label">FAQ</span>
      <h2 class="section-title">Questions About {title}</h2>
    </div>
    {faq_html}
  </div>
</section>

{cta_section()}
{footer()}
{MOBILE_CTA}
<style>
.faq-item {{ background:var(--color-surface); border-radius:var(--radius-md); padding:28px; margin-bottom:16px; border:1px solid rgba(0,0,0,0.06); }}
.faq-question {{ font-size:1.0625rem; font-weight:700; color:var(--color-text); margin-bottom:12px; }}
.faq-answer {{ color:var(--color-text-light); line-height:1.8; }}
</style>
{SCRIPTS}
</body>
</html>"""
    write_page(f"services/{filename}", content)


# ====================================================
# LOCATION PAGES
# ====================================================
def build_location(slug, city, county, neighborhood_refs, faq_pairs, img_slug=None):
    img = img_slug or slug
    schema = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Tampa Concrete Pros",
    "telephone": "+18137059021",
    "url": "https://tampaconcretepros.com",
    "address": {{ "@type": "PostalAddress", "streetAddress": "1801 E Camelback Rd Ste 102", "addressLocality": "Phoenix", "addressRegion": "AZ", "postalCode": "85016", "addressCountry": "US" }},
    "areaServed": {{ "@type": "City", "name": "{city}", "containedInPlace": {{ "@type": "State", "name": "Florida" }} }}
  }}
  </script>"""
    
    faq_html = ""
    for q, a in faq_pairs:
        faq_html += f"""<div style="background:var(--color-surface);border-radius:var(--radius-md);padding:24px;margin-bottom:14px;border:1px solid rgba(0,0,0,0.06);"><h3 style="font-size:1rem;font-weight:700;margin-bottom:10px;">{q}</h3><p style="color:var(--color-text-light);font-size:0.9375rem;line-height:1.7;">{a}</p></div>"""
    
    other_areas = [
        ("brandon", "Brandon"), ("riverview", "Riverview"), ("south-tampa", "South Tampa"),
        ("westchase", "Westchase"), ("clearwater", "Clearwater"), ("st-pete", "St. Petersburg"),
        ("new-tampa", "New Tampa"), ("lutz", "Lutz"), ("temple-terrace", "Temple Terrace"),
    ]
    area_links = "\n".join([f'<li><a href="/locations/{s}.html" style="color:var(--color-accent);">Concrete in {c}</a></li>' for s, c in other_areas if s != slug])
    
    content = head(
        f"Concrete Contractors in {city}, FL | Tampa Concrete Pros",
        f"Expert concrete contractors serving {city}, FL. Driveways, stamped concrete, pool decks, and patios. Licensed, insured, free estimates. Call (813) 705-9021.",
        f"{DOMAIN}/locations/{slug}.html",
        schema_extra=schema
    ) + f"""
{NAV}

<section class="hero hero--inner">
  <div class="container">
    <div class="hero__content">
      <span class="hero__badge">Serving {city}, FL</span>
      <h1 class="hero__title">Concrete Services in <span>{city}</span></h1>
      <p class="hero__subtitle">Licensed concrete contractors serving {city} and surrounding {county} communities. Free estimates on driveways, pool decks, stamped concrete &amp; more.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:1.5rem;">
        <a href="/contact.html#contact" class="btn btn--primary">Get Free Estimate</a>
        <a href="tel:+18137059021" class="btn btn--outline">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

<section class="why" style="background:var(--color-surface);">
  <div class="container">
    <div class="two-col-grid reveal">
      <div>
        <span class="section-label">{city} Concrete</span>
        <h2 class="section-title">Why {city} Chooses Tampa Concrete Pros</h2>
        <p style="color:var(--color-text-light);line-height:1.8;margin-bottom:1.5rem;">We understand the specific challenges of concrete work in {city}. From the sandy soils and high water tables to intense Florida sun and afternoon storms, every project is built to handle {county}'s unique conditions.</p>
        <p style="color:var(--color-text-light);line-height:1.8;margin-bottom:2rem;">Whether you're in {neighborhood_refs}, our crews are ready with fast scheduling and professional results.</p>
        <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:8px;margin-bottom:2rem;">
          <li style="display:flex;align-items:center;gap:10px;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="var(--color-accent)" width="18" height="18"><path d="M173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34Z"/></svg><span>Free on-site estimates</span></li>
          <li style="display:flex;align-items:center;gap:10px;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="var(--color-accent)" width="18" height="18"><path d="M173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34Z"/></svg><span>Licensed and fully insured</span></li>
          <li style="display:flex;align-items:center;gap:10px;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="var(--color-accent)" width="18" height="18"><path d="M173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34Z"/></svg><span>48–72 hour scheduling</span></li>
          <li style="display:flex;align-items:center;gap:10px;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" fill="var(--color-accent)" width="18" height="18"><path d="M173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34Z"/></svg><span>Florida-grade concrete mixes</span></li>
        </ul>
        <a href="/contact.html#contact" class="btn btn--primary">Request Estimate</a>
      </div>
      <div style="border-radius:var(--radius-lg);overflow:hidden;min-height:340px;">
        <img src="/images/locations/{img}.webp" alt="Concrete services {city} FL" style="width:100%;height:100%;object-fit:cover;" loading="lazy">
      </div>
    </div>
  </div>
</section>

<!-- Services -->
<section class="why" style="background:var(--color-white);">
  <div class="container">
    <div style="text-align:center;margin-bottom:3rem;">
      <span class="section-label">Our Services</span>
      <h2 class="section-title">Concrete Services We Offer in {city}</h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;" class="reveal">
      <div style="background:var(--color-surface);border-radius:var(--radius-md);padding:28px;border:1px solid rgba(0,0,0,0.06);">
        <h3 style="font-size:1.0625rem;font-weight:700;margin-bottom:10px;">Driveways</h3>
        <p style="font-size:0.9375rem;color:var(--color-text-light);">New installation or replacement of concrete driveways built to last in Florida's climate.</p>
      </div>
      <div style="background:var(--color-surface);border-radius:var(--radius-md);padding:28px;border:1px solid rgba(0,0,0,0.06);">
        <h3 style="font-size:1.0625rem;font-weight:700;margin-bottom:10px;">Stamped Concrete</h3>
        <p style="font-size:0.9375rem;color:var(--color-text-light);">Decorative patterns and colors that add curb appeal without sacrificing durability.</p>
      </div>
      <div style="background:var(--color-surface);border-radius:var(--radius-md);padding:28px;border:1px solid rgba(0,0,0,0.06);">
        <h3 style="font-size:1.0625rem;font-weight:700;margin-bottom:10px;">Pool Decks</h3>
        <p style="font-size:0.9375rem;color:var(--color-text-light);">Slip-resistant, heat-reflective pool surround concrete for comfortable Florida summers.</p>
      </div>
      <div style="background:var(--color-surface);border-radius:var(--radius-md);padding:28px;border:1px solid rgba(0,0,0,0.06);">
        <h3 style="font-size:1.0625rem;font-weight:700;margin-bottom:10px;">Patios</h3>
        <p style="font-size:0.9375rem;color:var(--color-text-light);">Expand your outdoor living space with a durable, low-maintenance concrete patio.</p>
      </div>
      <div style="background:var(--color-surface);border-radius:var(--radius-md);padding:28px;border:1px solid rgba(0,0,0,0.06);">
        <h3 style="font-size:1.0625rem;font-weight:700;margin-bottom:10px;">Walkways</h3>
        <p style="font-size:0.9375rem;color:var(--color-text-light);">Sidewalks, garden paths, and entry walkways crafted to complement your property.</p>
      </div>
      <div style="background:var(--color-surface);border-radius:var(--radius-md);padding:28px;border:1px solid rgba(0,0,0,0.06);">
        <h3 style="font-size:1.0625rem;font-weight:700;margin-bottom:10px;">Commercial</h3>
        <p style="font-size:0.9375rem;color:var(--color-text-light);">Parking lots, loading areas, and commercial concrete for {city} businesses.</p>
      </div>
    </div>
    <div style="text-align:center;margin-top:2rem;"><a href="/services/" class="btn btn--primary">View All Services</a></div>
  </div>
</section>

<!-- FAQ -->
<section class="why" style="background:var(--color-surface);">
  <div class="container" style="max-width:820px;">
    <div class="reveal" style="margin-bottom:2rem;">
      <span class="section-label">FAQ</span>
      <h2 class="section-title">Concrete Questions in {city}</h2>
    </div>
    {faq_html}
  </div>
</section>

<!-- Other Areas -->
<section class="why" style="background:var(--color-white);">
  <div class="container">
    <div style="text-align:center;margin-bottom:2rem;">
      <span class="section-label">Service Areas</span>
      <h2 class="section-title">Other Areas We Serve Near Tampa</h2>
    </div>
    <ul style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;list-style:none;padding:0;" class="reveal">
      {area_links}
    </ul>
  </div>
</section>

{cta_section()}
{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page(f"locations/{slug}.html", content)


# ====================================================
# BLOG PAGES
# ====================================================
def build_blog_index():
    posts = [
        ("driveway-cost-tampa.html", "How Much Does a Concrete Driveway Cost in Tampa?", "Cost breakdown for concrete driveways in Tampa, FL — price per square foot, factors that affect cost, and tips to get the best value."),
        ("concrete-vs-asphalt.html", "Concrete vs. Asphalt Driveways in Florida: Which Is Better?", "Comparing concrete and asphalt driveways for Tampa homeowners — durability, cost, maintenance, and Florida climate considerations."),
        ("stamped-concrete-patterns-florida.html", "Best Stamped Concrete Patterns for Florida Homes", "Top stamped concrete patterns and colors that work beautifully in Tampa's climate and complement Florida-style homes."),
        ("pool-deck-resurfacing-tampa.html", "Pool Deck Resurfacing Options in Tampa, FL", "Exploring pool deck resurfacing options for Tampa homeowners — from cool deck coatings to decorative concrete overlays."),
        ("florida-climate.html", "How Florida's Climate Affects Concrete Durability", "Understanding how Tampa's heat, humidity, rain, and UV exposure impact concrete longevity — and how to protect your investment."),
        ("replacement-signs.html", "7 Signs Your Tampa Driveway Needs Replacing", "Warning signs that your concrete driveway has reached end of life and when repair vs replacement makes sense."),
        ("stamped-concrete-vs-pavers-florida.html", "Stamped Concrete vs. Pavers: Which Is Right for Your Tampa Home?", "Side-by-side comparison of stamped concrete and pavers for driveways and patios in Tampa, FL."),
        ("grand-opening.html", "Tampa Concrete Pros: Serving Tampa Bay Since 2009", "About Tampa Concrete Pros and our commitment to quality concrete work throughout the Tampa Bay area."),
    ]
    
    cards = ""
    for href, title, desc in posts:
        cards += f"""<article style="background:white;border-radius:var(--radius-lg);padding:28px;border:1px solid rgba(0,0,0,0.06);transition:transform 0.25s ease,box-shadow 0.25s ease;" class="reveal">
        <h2 style="font-size:1.1875rem;font-weight:700;margin-bottom:10px;line-height:1.4;"><a href="/blog/{href}" style="color:var(--color-text);">{title}</a></h2>
        <p style="font-size:0.9375rem;color:var(--color-text-light);line-height:1.6;margin-bottom:16px;">{desc}</p>
        <a href="/blog/{href}" class="btn btn--primary" style="padding:10px 20px;font-size:0.875rem;">Read More</a>
      </article>"""
    
    content = head(
        "Concrete Blog | Tampa Concrete Pros",
        "Concrete tips, cost guides, and local guides for Tampa Bay homeowners. Expert advice from Tampa Concrete Pros.",
        f"{DOMAIN}/blog/"
    ) + f"""
{NAV}
{inner_hero("Concrete Blog", "Tips, Guides & Resources", subtitle="Expert concrete advice for Tampa Bay homeowners from the team at Tampa Concrete Pros.")}

<section class="why" style="background:var(--color-surface);">
  <div class="container">
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px;">
      {cards}
    </div>
  </div>
</section>
<style>@media(max-width:640px){{.container > div[style*="grid-template-columns: repeat(2"]{{grid-template-columns:1fr!important}}}}</style>

{cta_section()}
{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page("blog/index.html", content)


def build_blog_post(slug, title, desc, h2s_content):
    """Build a simple blog post."""
    content = head(
        f"{title} | Tampa Concrete Pros",
        desc,
        f"{DOMAIN}/blog/{slug}"
    ) + f"""
{NAV}
<section class="hero hero--inner">
  <div class="container">
    <div class="hero__content">
      <span class="hero__badge">Concrete Blog</span>
      <h1 class="hero__title">{title}</h1>
    </div>
  </div>
</section>

<section class="why" style="background:var(--color-surface);">
  <div class="container" style="max-width:820px;">
    <article class="reveal" style="background:white;border-radius:var(--radius-lg);padding:48px;box-shadow:var(--shadow-sm);">
      {h2s_content}
      <div style="margin-top:2rem;padding:24px;background:rgba(249,115,22,0.08);border-radius:var(--radius-md);border-left:4px solid var(--color-accent);">
        <p style="font-weight:700;margin-bottom:8px;">Need a Free Estimate?</p>
        <p style="color:var(--color-text-light);margin-bottom:16px;">Call Tampa Concrete Pros at <a href="tel:+18137059021" style="color:var(--color-accent);font-weight:600;">(813) 705-9021</a> or request an estimate online.</p>
        <a href="/contact.html#contact" class="btn btn--primary">Get Free Estimate</a>
      </div>
    </article>
  </div>
</section>

{cta_section()}
{footer()}
{MOBILE_CTA}
{SCRIPTS}
</body>
</html>"""
    write_page(f"blog/{slug}", content)


# ============================================================
# MAIN BUILD
# ============================================================
print("Building all pages...")

build_about()
build_faq()
build_thankyou()
build_privacy()
build_terms()
build_404()
build_services_index()

# SERVICE PAGES
build_service_page(
    "driveway-installation.html",
    "Concrete Driveway Installation",
    ("Driveway Installation", "in Tampa, FL"),
    "New Driveways",
    "New concrete driveways built for Florida's climate — engineered for durability, drainage, and curb appeal.",
    "/images/services/driveway-installation.webp",
    "A new concrete driveway is one of the best investments for Tampa homeowners. Concrete offers superior durability compared to asphalt, handles Florida's intense UV and heat with proper sealing, and can last 30+ years with minimal maintenance. Our installation process starts with thorough excavation and sub-base compaction — critical in Tampa's sandy soils — followed by reinforced concrete pouring and professional finishing.",
    ["Proper sub-base excavation and compaction for Florida's sandy soils", "Reinforced concrete with rebar or fiber mesh for maximum strength", "Control joints placed strategically to manage natural expansion", "Professional-grade sealant to protect against UV, rain, and staining", "Multiple finish options: broom, exposed aggregate, brushed, or smooth", "Free estimates with transparent pricing — no surprise charges"],
    [("How thick should a concrete driveway be in Tampa?", "For residential driveways in Tampa, we typically pour 4 inches of concrete for passenger vehicles, and 5–6 inches for heavier vehicles like RVs or trucks. Proper sub-base preparation is equally important for longevity."),
     ("How long before I can drive on my new driveway?", "We recommend waiting 7 days before driving regular vehicles on new concrete. Full cure takes 28 days. We'll give you specific guidance during your project."),
     ("Can I choose the color for my new driveway?", "Yes. We offer integral pigments for colored concrete, acid staining, and decorative stamped finishes in dozens of colors and patterns.")]
)

build_service_page(
    "driveway-replacement.html",
    "Concrete Driveway Replacement",
    ("Driveway Replacement", "in Tampa, FL"),
    "Replacement Services",
    "Full driveway tear-out and replacement — removing old, cracked concrete and installing a new, lasting surface.",
    "/images/services/driveway-replacement.webp",
    "If your Tampa driveway has widespread cracking, heaving, deep staining, or structural failure, replacement is the right call. We handle every step of the process: tear-out of old concrete, proper disposal, re-grading for drainage, and installation of a new reinforced slab. Many Tampa-area driveways from the 1980s and 90s are now reaching end of life and need full replacement.",
    ["Complete tear-out and disposal of existing concrete", "Re-grading to ensure proper drainage away from your home", "New reinforced slab with rebar or fiber mesh", "Choice of standard or decorative finish options", "Licensed and insured crew on every job", "Typically completed in 2–4 days depending on size"],
    [("How do I know if I need replacement vs repair?", "If cracking is widespread (50%+ of the surface), if sections are heaving or sinking significantly, or if the concrete is structurally compromised, replacement is usually more cost-effective than repair. We'll give you an honest assessment."),
     ("How much does driveway replacement cost in Tampa?", "Replacement typically costs $8–$18 per square foot, including tear-out and new installation. Factors include driveway size, disposal costs, and your choice of finish. Contact us for a free estimate."),
     ("How long does replacement take?", "Most standard driveway replacements take 3–5 days from demo to final finish, plus curing time before vehicle use.")]
)

build_service_page(
    "stamped-concrete.html",
    "Stamped Concrete",
    ("Stamped Concrete", "in Tampa, FL"),
    "Decorative Concrete",
    "Beautiful decorative concrete patterns and colors that transform driveways, patios, and pool decks across Tampa Bay.",
    "/images/services/stamped-concrete.webp",
    "Stamped concrete gives you the look of natural stone, brick, or wood at a fraction of the cost — with the durability of solid concrete. It's one of the most popular services in Tampa Bay, especially for pool decks, patios, and front driveways where curb appeal matters. We offer dozens of patterns including slate, cobblestone, flagstone, herringbone, fan pattern, and wood plank, combined with a wide palette of integral colors and accent stains.",
    ["Dozens of pattern options: slate, cobblestone, flagstone, wood, herringbone", "Custom color matching with integral pigments and accent stains", "UV-resistant sealer applied after completion to lock in color and protect surface", "Works for driveways, patios, pool decks, walkways, and steps", "Durable and low-maintenance — easier to maintain than pavers", "Significantly more affordable than natural stone or brick"],
    [("Is stamped concrete slippery?", "Standard stamped concrete can be slippery when wet, especially around pool areas. We use texture stamps and anti-slip additives in the sealer for pool decks to ensure safe footing."),
     ("How does stamped concrete hold up in Tampa's heat?", "With proper sealing and quality Florida-grade concrete, stamped concrete holds up very well. We recommend re-sealing every 2–3 years to maintain color and UV protection."),
     ("Can I stamp an existing concrete surface?", "No — stamps must be applied to freshly poured concrete. For existing surfaces, we can apply decorative overlays or micro-toppings as an alternative.")]
)

build_service_page(
    "pool-decks.html",
    "Pool Deck Concrete",
    ("Pool Decks", "in Tampa, FL"),
    "Pool Decks",
    "Slip-resistant, heat-reflective pool deck surfaces designed for Florida's intense sun and heavy pool use.",
    "/images/services/pool-decks.webp",
    "Tampa's backyard pools need pool decks that handle barefoot traffic, constant moisture, chlorine exposure, and Florida's UV-intense sunshine. A standard concrete slab gets scalding hot on summer afternoons — we address this with cool deck coatings, light colors, and specialized finishes that reflect heat. Every pool deck we install is slip-resistant, structurally sound, and sealed to resist staining and moisture penetration.",
    ["Anti-slip texture built into every pool deck pour", "Heat-reflective finishes to keep surfaces cooler in summer", "Chlorine-resistant concrete mixes that resist chemical breakdown", "Proper drainage slope away from pool edge and home foundation", "Decorative options: stamped, exposed aggregate, cool deck coating", "Licensed, insured crew with pool deck specialization"],
    [("What's the coolest pool deck surface for Tampa summers?", "Light-colored concrete with a broom or exposed aggregate finish reflects the most heat. Cool deck coatings are another popular option — they use a spray-applied texture that stays noticeably cooler than standard concrete."),
     ("How much does a pool deck cost in Tampa?", "Basic pool deck installation runs $8–$14 per square foot. Decorative stamped or cool deck options range $12–$22 per square foot depending on complexity and size."),
     ("How do I maintain my concrete pool deck?", "Re-seal every 1–2 years for pool decks (more frequent than other concrete due to pool chemistry exposure). Power wash annually to remove algae and calcium deposits. Repair cracks promptly to prevent water intrusion.")]
)

build_service_page(
    "patios-walkways.html",
    "Concrete Patios & Walkways",
    ("Patios & Walkways", "in Tampa, FL"),
    "Outdoor Living",
    "Extend your Tampa home's living space with durable concrete patios and walkways built for Florida's outdoor lifestyle.",
    "/images/services/patios-walkways.webp",
    "Tampa's year-round outdoor living demands outdoor spaces that can handle the heat, rain, and humidity. A professionally poured concrete patio or walkway gives you a durable, low-maintenance foundation for your outdoor furniture, BBQ area, fire pit, or garden. Concrete outperforms pavers in resistance to shifting and weed growth, and can be finished in dozens of styles from smooth brushed to decorative stamped patterns.",
    ["Custom shapes and designs to match your home's layout", "Multiple finish options: broom, stamped, exposed aggregate, smooth", "Proper drainage sloped away from home foundation", "Option to integrate steps, retaining walls, and borders", "Walkways and paths connecting all areas of your property", "Sealed for UV and stain resistance"],
    [("How much does a concrete patio cost in Tampa?", "Concrete patios in Tampa typically cost $6–$12 per square foot for a basic finish. Stamped or decorative patios range $12–$22 per square foot. Size, shape complexity, and finish all affect pricing."),
     ("How do I clean concrete patio stains?", "Most stains can be removed with a pressure washer or concrete cleaner. Oil stains need a degreaser. Regular sealing helps prevent staining — we recommend re-sealing every 2–3 years."),
     ("Can you integrate a patio with an existing structure?", "Yes — we can tie new concrete into existing driveways, steps, or pool decks. Proper bonding agent and rebar ties ensure a seamless, structurally sound connection.")]
)

build_service_page(
    "commercial.html",
    "Commercial Concrete",
    ("Commercial Concrete", "in Tampa, FL"),
    "Commercial Projects",
    "Large-scale commercial concrete work in Tampa Bay — parking lots, warehouse floors, sidewalks, and structural slabs.",
    "/images/services/commercial.webp",
    "Tampa Concrete Pros handles commercial concrete projects of all sizes across the greater Tampa Bay area. From retail parking lots to industrial warehouse floors, we bring the same quality standards and professionalism to commercial work as residential. We understand that commercial clients need minimal disruption, efficient scheduling, and durable results that last decades.",
    ["Parking lots: full installation or repair of commercial parking surfaces", "Warehouse and industrial floors with proper load ratings", "Sidewalks, ADA-compliant ramps, and exterior pathways", "Loading dock aprons and truck approach slabs", "Curb and gutter installation", "Fast scheduling to minimize business disruption"],
    [("Do you do ADA-compliant concrete work?", "Yes — we install ADA-compliant ramps, truncated dome panels, and accessible pathways that meet Florida building code requirements."),
     ("Can you work nights or weekends for minimal disruption?", "Yes. We accommodate commercial clients' scheduling needs, including evening and weekend pours when daytime work isn't feasible."),
     ("Do you provide commercial estimates and project timelines?", "Yes — we provide detailed written quotes, project timelines, and can work within your project management system for larger contracts.")]
)

# LOCATION PAGES
locations = [
    ("brandon", "Brandon", "Hillsborough County", "Limona, Providence Lakes, Bloomingdale, and Kingsway",
     [("How much does concrete cost in Brandon?", "Standard concrete work in Brandon runs $6–$15 per square foot for basic finishes. Stamped concrete is $12–$25 per square foot. Call us at (813) 705-9021 for a free on-site estimate."),
      ("How does Brandon's soil affect concrete?", "Brandon's sandy soils require thorough sub-base compaction before pouring. We use rebar reinforcement and proper drainage planning on every Brandon project to prevent shifting and cracking."),
      ("Do you serve all of Brandon?", "Yes — we serve all Brandon neighborhoods including areas near Westfield Brandon mall, Bloomingdale, Valrico border, and all residential streets throughout the community.")]),
    
    ("riverview", "Riverview", "Hillsborough County", "Summerfield, FishHawk, and Boyette",
     [("Do you serve all of Riverview?", "Yes — we cover all Riverview neighborhoods including Summerfield, FishHawk Ranch, Boyette, and all residential communities throughout the 33569 and 33578 zip codes."),
      ("How long does a concrete project take in Riverview?", "Most residential projects (driveways, patios, pool decks) take 2–5 days. We schedule quickly and work to minimize disruption to your daily routine.")]),
    
    ("south-tampa", "South Tampa", "Hillsborough County", "Hyde Park, Palma Ceia, Bayshore, and Davis Islands",
     [("Do you do decorative concrete in South Tampa?", "Yes — stamped concrete and decorative finishes are very popular in South Tampa's historic and luxury neighborhoods. We offer dozens of patterns that complement the neighborhood's architecture."),
      ("How much does a pool deck cost in South Tampa?", "Pool deck concrete in South Tampa runs $10–$22 per square foot depending on the finish and size. Decorative cool deck and stamped options are on the higher end.")]),
    
    ("westchase", "Westchase", "Hillsborough County", "Westwood Lakes, The Fords, and Countryway",
     [("Do you serve Westchase?", "Yes — we regularly complete concrete driveways, patios, and pool decks throughout Westchase and the surrounding communities of Citrus Park and Town 'N' Country."),
      ("What's the best pool deck finish for Westchase homes?", "Cool deck and light-colored stamped concrete are popular in Westchase for their heat-reflective properties. Both keep surfaces comfortable for bare feet on hot Florida days.")]),
    
    ("carrollwood", "Carrollwood", "Hillsborough County", "Carrollwood Village, Lake Carroll, and Country Place",
     [("Do you install driveways in Carrollwood?", "Yes — we complete concrete driveway installations and replacements throughout Carrollwood and the surrounding Village area. Most projects are scheduled within a week of estimate approval."),
      ("Can I get stamped concrete in Carrollwood?", "Absolutely. Stamped concrete driveways and patios are very popular in Carrollwood. We offer dozens of patterns and colors to complement your home's style.")]),
    
    ("new-tampa", "New Tampa", "Hillsborough County", "Heritage Isles, Tampa Palms, and Live Oak Preserve",
     [("Do you work in New Tampa?", "Yes — we complete concrete projects throughout New Tampa including Heritage Isles, Tampa Palms, and Live Oak Preserve neighborhoods."),
      ("Are your prices the same in New Tampa?", "Yes — our pricing is consistent across Tampa Bay. We provide free on-site estimates with no travel charges for New Tampa locations.")]),
    
    ("temple-terrace", "Temple Terrace", "Hillsborough County", "Temple Crest, Terrace Park, and Riverhills",
     [("Do you serve Temple Terrace?", "Yes — Temple Terrace is one of our regular service areas. We complete driveways, patios, pool decks, and commercial concrete throughout the city."),
      ("How soon can you start a project in Temple Terrace?", "We typically schedule projects within 48–72 hours of estimate approval, depending on current workload and project scope.")]),
    
    ("wesley-chapel", "Wesley Chapel", "Pasco County", "Wiregrass, Zephyr Ridge, and Seven Oaks",
     [("Do you serve Wesley Chapel in Pasco County?", "Yes — we extend our service area to Wesley Chapel and all of Pasco County. Contact us for a free estimate and we'll schedule a site visit."),
      ("What's the most popular concrete service in Wesley Chapel?", "New concrete driveways and decorative stamped patios are very popular in Wesley Chapel's growing residential communities. Pool deck work is also common given the number of new construction homes with pools.")]),
    
    ("lutz", "Lutz", "Pasco / Hillsborough County", "Lake Heron, Villarosa, and Cheval",
     [("Do you serve Lutz?", "Yes — Lutz and the surrounding communities of Land O Lakes and Odessa are part of our regular service area."),
      ("How does Lutz's high water table affect concrete?", "In areas with higher water tables, proper drainage is even more critical. We account for this in our site assessment and slope all surfaces appropriately.")]),
    
    ("clearwater", "Clearwater", "Pinellas County", "Countryside, Safety Harbor, and Dunedin",
     [("Do you serve Clearwater in Pinellas County?", "Yes — we serve all of Clearwater and greater Pinellas County including Safety Harbor, Dunedin, and Largo."),
      ("What concrete services are most popular in Clearwater?", "Pool decks, driveways, and decorative patios are our most requested services in Clearwater. Beach proximity means property owners want durable, low-maintenance outdoor surfaces.")]),
    
    ("st-pete", "St. Petersburg", "Pinellas County", "Historic Kenwood, Crescent Lake, and Snell Isle", 
     [("Do you serve St. Petersburg?", "Yes — we cover all of St. Petersburg and Pinellas County. Our crews are familiar with the area's architectural styles and soil conditions near Tampa Bay."),
      ("Is stamped concrete popular in St. Petersburg?", "Very much so. Historic neighborhoods in St. Pete appreciate decorative concrete that complements older architectural styles. We offer patterns that blend with craftsman and Mediterranean-style homes.")],
     "st-pete"),
    
    ("st-petersburg", "St. Petersburg", "Pinellas County", "Historic Kenwood, Grand Central, and Crescent Lake",
     [("Do you serve all of St. Petersburg?", "Yes — we serve all neighborhoods in St. Petersburg and Pinellas County. From the beaches to downtown St. Pete, our crews are ready to serve you."),
      ("What's the average driveway cost in St. Petersburg?", "Concrete driveways in St. Petersburg typically run $6–$15 per square foot for a standard broom finish. Decorative options are $12–$25 per square foot. Free estimates available.")]),
    
    ("hyde-park", "Hyde Park", "Hillsborough County", "Soho, Bayshore, and Old Hyde Park",
     [("Do you do decorative concrete in Hyde Park?", "Yes — Hyde Park's historic character calls for tasteful decorative concrete work. We offer stamped patterns and stained concrete that complement the neighborhood's craftsman and Mediterranean architecture."),
      ("How do you handle small driveway spaces in Hyde Park?", "Many Hyde Park homes have narrow driveways or limited space. We design to maximize your driveway footprint while ensuring proper drainage and clean finishes.")]),
    
    ("seminole-heights", "Seminole Heights", "Hillsborough County", "Old Seminole Heights, Woodycrest, and Southeast Seminole Heights",
     [("Do you do concrete work in Seminole Heights?", "Yes — we work throughout Seminole Heights and the surrounding neighborhoods. Driveway replacement and patio installation are popular in this area's older housing stock."),
      ("What are the most requested concrete services in Seminole Heights?", "Driveway replacement (many original concrete driveways from the 1950s-70s are reaching end of life), patio installations, and decorative walkways are our most requested services in Seminole Heights.")]),
    
    ("ybor-city", "Ybor City", "Hillsborough County", "Historic Ybor, Palmetto Beach, and V.M. Ybor",
     [("Do you do concrete work in Ybor City?", "Yes — we serve Ybor City and the surrounding East Tampa neighborhoods for both residential and commercial concrete work."),
      ("Do you do commercial concrete in Ybor City?", "Yes — Ybor City has significant commercial activity. We handle parking lots, sidewalks, and exterior concrete for businesses throughout the area.")]),
    
    ("channelside", "Channelside", "Hillsborough County", "Harbour Island, Downtown Tampa, and Meridian",
     [("Do you serve Channelside condos and townhomes?", "Yes — we work with HOAs and individual property owners in Channelside for decorative driveways, patios, and common area concrete."),
      ("What concrete services are most common in Channelside?", "Decorative concrete, walkways, and patio installations are most common in the Channelside area. We work with HOA requirements and architectural guidelines.")]),
    
    ("land-o-lakes", "Land O' Lakes", "Pasco County", "Sunlake, Lake Padgett, and Plantation Palms",
     [("Do you serve Land O' Lakes?", "Yes — Land O' Lakes and all of north Pasco County is within our service area."),
      ("What's the best concrete option for Land O' Lakes driveways?", "Given the sandy soils in the Land O' Lakes area, proper sub-base compaction and reinforcement are critical. We recommend at least 4-inch slabs with rebar for driveways.")]),
    
    ("largo", "Largo", "Pinellas County", "Largo Central, East Bay, and Seminole",
     [("Do you serve Largo in Pinellas County?", "Yes — Largo and all of Pinellas County is within our service area."),
      ("What's the most popular concrete service in Largo?", "Pool decks, driveways, and stamped concrete patios are popular in Largo's residential neighborhoods.")]),
    
    ("safety-harbor", "Safety Harbor", "Pinellas County", "Bayshore, Philippe Park, and downtown Safety Harbor",
     [("Do you serve Safety Harbor?", "Yes — Safety Harbor and the surrounding Pinellas County communities are part of our regular service area."),
      ("Is stamped concrete popular in Safety Harbor?", "Yes — Safety Harbor's charming neighborhood character makes decorative concrete a natural fit. We offer patterns that complement the area's classic Florida architectural styles.")]),
    
    ("plant-city", "Plant City", "Hillsborough County", "Walden Lake, Wilder, and downtown Plant City",
     [("Do you serve Plant City?", "Yes — Plant City is within our service area in eastern Hillsborough County."),
      ("What's the cost of a driveway in Plant City?", "Concrete driveways in Plant City typically run $6–$14 per square foot for standard finishes. Contact us for a free on-site estimate.")]),
    
    ("apollo-beach", "Apollo Beach", "Hillsborough County", "Waterset, MiraBay, and Apollo Beach Estates",
     [("Do you serve Apollo Beach?", "Yes — Apollo Beach and the surrounding South Hillsborough communities are within our service area."),
      ("What concrete services are popular in Apollo Beach?", "Pool decks are extremely popular in Apollo Beach given the high concentration of waterfront and pool-equipped homes. Driveways and decorative patios are also in high demand.")]),
    
    ("valrico", "Valrico", "Hillsborough County", "FishHawk, Bloomingdale, and Seffner",
     [("Do you serve Valrico?", "Yes — Valrico and the surrounding communities of FishHawk and Bloomingdale are part of our regular service area."),
      ("What's the best finish for a Valrico driveway?", "Broom finish is the most popular for its durability and traction, but exposed aggregate and stamped concrete are popular in higher-end Valrico neighborhoods for their decorative appeal.")]),
    
    ("westchase", "Westchase", "Hillsborough County", "Westwood Lakes, The Fords, and Countryway",
     [("Do you serve Westchase?", "Yes — Westchase and surrounding communities including Citrus Park and Town N Country are part of our regular service area."),
      ("What pool deck finishes are popular in Westchase?", "Cool deck and light-colored stamped concrete are popular in Westchase's pool-heavy neighborhoods. Both options keep surfaces comfortable during hot Tampa summers.")]),
]

# Deduplicate by slug
seen_slugs = set()
for loc_data in locations:
    slug = loc_data[0]
    if slug not in seen_slugs:
        seen_slugs.add(slug)
        build_location(*loc_data)

build_blog_index()

# Blog posts
blog_posts = [
    ("driveway-cost-tampa.html", "How Much Does a Concrete Driveway Cost in Tampa?",
     "Complete cost guide for concrete driveways in Tampa, FL — price per square foot, factors that affect cost, and tips for getting the best value.",
     """<h2>Average Concrete Driveway Cost in Tampa</h2>
     <p>Concrete driveway installation in Tampa typically ranges from <strong>$6 to $15 per square foot</strong> for a standard broom finish. A typical two-car driveway (approximately 400–500 sq ft) would cost <strong>$2,400–$7,500</strong> installed.</p>
     <h2 style="margin-top:2rem;">Factors That Affect Price</h2>
     <ul style="color:var(--color-text-light);line-height:2;padding-left:1.5rem;">
       <li><strong>Size:</strong> Larger driveways have lower cost per square foot due to setup efficiency</li>
       <li><strong>Finish type:</strong> Broom finish is least expensive; stamped concrete adds $6–$12 per sq ft</li>
       <li><strong>Thickness:</strong> 4-inch standard vs. 5–6 inch for heavy vehicles</li>
       <li><strong>Site prep:</strong> Sandy soils or poor drainage may require additional base work</li>
       <li><strong>Tear-out:</strong> Removing existing driveway adds $1–$3 per sq ft</li>
     </ul>
     <h2 style="margin-top:2rem;">Cost by Driveway Type</h2>
     <p>Basic broom finish: $6–$10/sq ft. Exposed aggregate: $8–$14/sq ft. Stamped concrete: $12–$22/sq ft. Colored concrete: add $2–$5/sq ft.</p>
     <h2 style="margin-top:2rem;">Tips to Get the Best Value</h2>
     <p>Get 2–3 quotes from licensed contractors. Ask what's included in the price (sub-base, rebar, sealer). Avoid contractors who skip the sealer — it significantly extends driveway life in Tampa's UV-intense climate.</p>"""),
    
    ("concrete-vs-asphalt.html", "Concrete vs. Asphalt Driveways in Florida: Which Is Better?",
     "Comparing concrete and asphalt driveways for Tampa homeowners — durability, maintenance, cost, and how Florida's climate affects each material.",
     """<h2>The Bottom Line for Tampa Homeowners</h2>
     <p>In Florida's climate, <strong>concrete is almost always the better choice</strong>. Asphalt softens significantly in Tampa's summer heat — surface temperatures of 150°F+ cause asphalt to indent and track into your garage. Concrete handles the heat with no softening.</p>
     <h2 style="margin-top:2rem;">Durability Comparison</h2>
     <p>Concrete: 30–40 year lifespan with minimal maintenance. Asphalt: 15–25 years with resealing every 3–5 years and periodic crack repair. In Tampa's heat and UV, asphalt degrades faster than in cooler climates.</p>
     <h2 style="margin-top:2rem;">Cost Comparison</h2>
     <p>Asphalt is typically $3–$7/sq ft vs. concrete at $6–$15/sq ft. However, concrete's longer lifespan and lower maintenance costs often make it more economical over 20+ years.</p>
     <h2 style="margin-top:2rem;">Maintenance Requirements</h2>
     <p>Concrete requires sealing every 3–5 years and prompt crack repair. Asphalt needs resealing every 3–5 years and is more prone to cracking in Florida due to thermal cycling. Both materials benefit from proper drainage to prevent undercutting.</p>
     <h2 style="margin-top:2rem;">Our Recommendation</h2>
     <p>For Tampa homeowners, we recommend concrete for its longevity, lower long-term cost, and resistance to Florida's heat. The higher upfront cost pays off over time.</p>"""),
    
    ("stamped-concrete-patterns-florida.html", "Best Stamped Concrete Patterns for Florida Homes",
     "Top stamped concrete patterns and colors that complement Tampa Bay's architecture and hold up beautifully in Florida's climate.",
     """<h2>Why Stamped Concrete Thrives in Florida</h2>
     <p>Florida's outdoor lifestyle makes decorative concrete incredibly popular. Warm weather means patios, pool decks, and driveways get year-round use — and homeowners want surfaces that look as good as they perform.</p>
     <h2 style="margin-top:2rem;">Top Patterns for Tampa Homes</h2>
     <p><strong>Ashlar Slate:</strong> The most popular pattern in Tampa Bay. The irregular rectangular shape gives a natural stone look that complements both modern and traditional Florida homes. Colors: buff, sandstone, terra cotta.</p>
     <p style="margin-top:1rem;"><strong>Cobblestone:</strong> Great for driveways and entrances. Creates a European street feel that's popular in Hyde Park and South Tampa's historic neighborhoods.</p>
     <p style="margin-top:1rem;"><strong>Wood Plank:</strong> For a warm, natural look. Popular for covered patio areas where the wood aesthetic complements interior flooring.</p>
     <p style="margin-top:1rem;"><strong>Fan/Rosette:</strong> A classic pattern popular around pool decks and circular driveway turn-arounds.</p>
     <h2 style="margin-top:2rem;">Color Recommendations for Florida</h2>
     <p>Lighter colors reflect heat better — important around pool decks and outdoor living spaces. Buff, sand, tan, and light gray are the most popular in Tampa. Darker colors look stunning but absorb more heat.</p>"""),
    
    ("florida-climate.html", "How Florida's Climate Affects Concrete Durability",
     "Understanding how Tampa's heat, humidity, rain, and UV exposure impact concrete longevity and what to do about it.",
     """<h2>The Florida Concrete Challenge</h2>
     <p>Tampa's climate is both beautiful and demanding. Intense UV radiation, daily afternoon thunderstorms in summer, high humidity, and temperatures that rarely dip below freezing create a unique set of challenges for concrete.</p>
     <h2 style="margin-top:2rem;">UV Damage</h2>
     <p>Florida's intense UV rays break down the cement paste on concrete surfaces over time, causing surface dusting and spalling. Quality UV-resistant sealers applied every 2–3 years provide critical protection.</p>
     <h2 style="margin-top:2rem;">Heavy Rain and Drainage</h2>
     <p>Tampa's summer thunderstorms dump enormous amounts of water in short periods. Proper drainage — sloping surfaces away from homes and structures — is critical to prevent water pooling and undercutting the slab.</p>
     <h2 style="margin-top:2rem;">Sandy Soils</h2>
     <p>Much of the Tampa Bay area sits on sandy soils that shift more than clay-based soils. Thorough sub-base compaction and reinforcement (rebar or fiber mesh) are essential to prevent slab cracking and settling.</p>
     <h2 style="margin-top:2rem;">The Good News</h2>
     <p>Unlike northern states, Florida concrete doesn't face freeze-thaw cycles — one of the primary causes of concrete damage. With proper installation and maintenance, Tampa concrete easily lasts 30+ years.</p>"""),
    
    ("replacement-signs.html", "7 Signs Your Tampa Driveway Needs Replacing",
     "Warning signs that your concrete driveway has reached end of life — and when repair versus replacement makes financial sense.",
     """<h2>When to Replace vs. Repair</h2>
     <p>Many Tampa driveways were poured in the 1970s, 80s, and 90s. At 30–40 years old, many are simply reaching end of life. Here are 7 signs it's time for replacement rather than continued patching.</p>
     <h2 style="margin-top:2rem;">1. Widespread Cracking</h2>
     <p>Minor cracks in concrete are normal and repairable. But if cracking covers more than 30–40% of your driveway surface — or if cracks are wide (1/4 inch or more) — the structural integrity is compromised and replacement makes more sense.</p>
     <h2 style="margin-top:2rem;">2. Heaving or Sinking Sections</h2>
     <p>If sections of your driveway have shifted up or down significantly, this indicates sub-base failure. Patching the surface won't fix the underlying problem.</p>
     <h2 style="margin-top:2rem;">3. Spalling and Surface Scaling</h2>
     <p>When the surface concrete chips and flakes away (spalling), it indicates the concrete has been compromised from within. Widespread spalling can't be economically repaired.</p>
     <h2 style="margin-top:2rem;">4. Water Pooling</h2>
     <p>Standing water on your driveway indicates improper drainage — which will accelerate deterioration. If re-sloping the surface isn't feasible, replacement with proper drainage planning is the fix.</p>
     <h2 style="margin-top:2rem;">5. Age Over 30 Years</h2>
     <p>Concrete driveways poured before proper sub-base compaction standards were common in Tampa may be nearing end of life regardless of visible condition.</p>
     <h2 style="margin-top:2rem;">6. Multiple Previous Repairs</h2>
     <p>If you've repaired the same driveway multiple times in recent years, you're spending repair money that would be better invested in a new slab.</p>
     <h2 style="margin-top:2rem;">7. Deep Staining</h2>
     <p>Oil, rust, and chemical stains that penetrate deeply into the concrete can't always be removed. For severe staining on an older driveway, replacement gives you a fresh start.</p>"""),
    
    ("stamped-concrete-vs-pavers-florida.html", "Stamped Concrete vs. Pavers: Which Is Right for Your Tampa Home?",
     "Side-by-side comparison of stamped concrete and pavers for driveways and patios in Tampa, FL — cost, maintenance, durability, and aesthetics.",
     """<h2>Overview</h2>
     <p>Both stamped concrete and pavers are popular in Tampa Bay, and both have real merits. The best choice depends on your budget, maintenance preferences, and aesthetic goals.</p>
     <h2 style="margin-top:2rem;">Cost Comparison</h2>
     <p><strong>Stamped concrete:</strong> $12–$22 per square foot installed. <strong>Pavers:</strong> $15–$30+ per square foot installed (concrete pavers) or $20–$50+ for natural stone pavers. Stamped concrete is typically 30–40% less expensive for the same area.</p>
     <h2 style="margin-top:2rem;">Durability</h2>
     <p>Properly sealed stamped concrete is very durable and handles Tampa's climate well. Pavers are individual units — they won't crack across large areas, but individual units can shift, settle, and grow weeds between joints in Florida's humid climate.</p>
     <h2 style="margin-top:2rem;">Maintenance</h2>
     <p>Stamped concrete needs resealing every 2–3 years and prompt crack repair. Pavers need regular joint sand replenishment, weed control, and re-leveling of settled sections. Both have moderate maintenance requirements in Florida.</p>
     <h2 style="margin-top:2rem;">Aesthetics</h2>
     <p>Both look great. Pavers have a natural three-dimensional look with real shadows between joints. Stamped concrete is seamless and can mimic pavers convincingly. Personal preference is often the deciding factor.</p>
     <h2 style="margin-top:2rem;">Our Take</h2>
     <p>For most Tampa homeowners, stamped concrete offers better value — lower cost, less maintenance hassle (especially with Florida's weed pressure between paver joints), and excellent aesthetics when properly sealed.</p>"""),
]

for slug, title, desc, body in blog_posts:
    build_blog_post(slug, title, desc, body)

# grand-opening.html
build_blog_post(
    "grand-opening.html",
    "Tampa Concrete Pros: Serving Tampa Bay Since 2009",
    "About Tampa Concrete Pros and our commitment to quality concrete work throughout the Tampa Bay area.",
    """<h2>Our Commitment to Tampa Bay</h2>
    <p>Tampa Concrete Pros has been serving Tampa Bay homeowners and businesses since 2009. We started as a small crew focused on doing one thing right: quality concrete work at fair prices.</p>
    <h2 style="margin-top:2rem;">What We Stand For</h2>
    <p>Every project we take on represents someone's home — their biggest investment. We treat that with the respect it deserves. No shortcuts, no inferior materials, no excuses when something isn't right.</p>
    <h2 style="margin-top:2rem;">Our Services</h2>
    <p>We specialize in residential and commercial concrete including driveways, driveway replacement, stamped concrete, pool decks, patios, and walkways. We serve all of Tampa Bay from Pasco County to Pinellas County and everywhere in between.</p>
    <h2 style="margin-top:2rem;">Get a Free Estimate</h2>
    <p>Ready to talk about your project? Call us at (813) 705-9021 or fill out our online form. We respond within 24 hours and schedule site visits typically within 48 hours.</p>""")

print("\nAll pages built successfully!")
