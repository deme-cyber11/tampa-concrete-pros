#!/usr/bin/env python3
"""
PAS rewriter for Tampa Concrete Pros.
Rewrites all service, location, about, and pricing pages using PAS templates.
Preserves: head schema, nav, footer, CSS classes, phone numbers.
"""

import os, re

SITE = "/Users/costa.demetral/Documents/Rank and Rent $/My-RR-Sites/Tampa Concrete Pros"
PHONE_D = "(813) 705-9021"
PHONE_T = "8137059021"

# ─────────────────────────────────────────────────────────────────────────────
# SHARED HTML FRAGMENTS (used in service / about / pricing pages)
# ─────────────────────────────────────────────────────────────────────────────

PHONE_SVG = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>"""

CHECK_SVG = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>"""

CHEVRON_SVG = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>"""

FLOATING_CTA = """
<div class="floating-cta" id="floating-cta">
  <a href="tel:+18137059021" class="fcta-call" aria-label="Call Now"><span class="fcta-label">Call Now</span><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg></a>
  <a href="/contact.html" class="fcta-quote" aria-label="Free Quote"><span class="fcta-label">Free Quote</span><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></a>
</div>
<script>
(function(){
  var el=document.getElementById('floating-cta');
  if(!el)return;
  window.addEventListener('scroll',function(){
    el.classList.toggle('visible',window.scrollY>80);
  },{passive:true});
})();
</script>
"""

MOBILE_CTA_BAR = """    <div class="mobile-cta-bar">
        <a href="tel:8137059021" class="cta-call">📞 Call Now</a>
        <a href="/contact.html" class="cta-quote">💬 Free Quote</a>
    </div>"""

FAQ_SCRIPT = """    <script>
        document.querySelectorAll('.faq-question').forEach(question => {
            question.addEventListener('click', () => {
                const item = question.parentElement;
                const isActive = item.classList.contains('active');
                document.querySelectorAll('.faq-item').forEach(faq => faq.classList.remove('active'));
                if (!isActive) item.classList.add('active');
            });
        });
    </script>"""

# ─────────────────────────────────────────────────────────────────────────────
# HELPER: Read existing file, extract head block
# ─────────────────────────────────────────────────────────────────────────────

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {os.path.relpath(path, SITE)}")

def extract_head(html):
    """Return the full <head>…</head> block from existing file."""
    m = re.search(r'(<head>.*?</head>)', html, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ''

def extract_header_nav(html):
    """Return the full <header>…</header> block (rich nav used by service pages)."""
    m = re.search(r'(<header>.*?</header>)', html, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ''

def extract_footer(html):
    """Return the full <footer>…</footer> block."""
    m = re.search(r'(<footer>.*?</footer>)', html, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ''

def extract_service_scripts(html):
    """Return the JS block at the bottom of service pages."""
    # Everything after </footer> up to </body>
    m = re.search(r'</footer>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ''

# ─────────────────────────────────────────────────────────────────────────────
# SERVICE PAGE BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def build_service_page(slug, data, head, nav_header, footer, tail_scripts):
    """Assemble a service page with PAS content inside <main>."""
    service = data['service']        # display name e.g. "Driveway Installation"
    h1 = data['h1']                  # full H1 text
    intro = data['intro']            # hero paragraph
    problem_h2 = data['problem_h2']  # "When You Need [service]"
    problem_body = data['problem_body']
    process_steps = data['process_steps']  # list of (name, desc)
    includes = data['includes']      # list of strings
    price_range = data['price_range']  # "$X–$Y per sq ft"
    price_body = data['price_body']
    faqs = data['faqs']              # list of (q, a)
    cta_note = data['cta_note']
    service_sel = data.get('service_select', slug.replace('-', ' ').title())

    breadcrumb_name = service

    # Process steps HTML
    steps_html = ""
    for i, (name, desc) in enumerate(process_steps, 1):
        steps_html += f"""
                <div class="process-step">
                    <div class="step-number">{i}</div>
                    <h3>{name}</h3>
                    <p>{desc}</p>
                </div>"""

    # Includes HTML
    includes_html = "".join(f"\n                    <li>{CHECK_SVG}<span>{inc}</span></li>" for inc in includes)

    # FAQ HTML (accordion)
    faq_items_html = ""
    for q, a in faqs:
        faq_items_html += f"""
            <div class="faq-item">
                <div class="faq-question">
                    {q}
                    {CHEVRON_SVG}
                </div>
                <div class="faq-answer">
                    <p>{a}</p>
                </div>
            </div>"""

    main_content = f"""
    <main>

    <div class="breadcrumbs">
        <div class="breadcrumbs-container">
            <a href="../">Home</a>
            <span>&gt;</span>
            <a href="#">Services</a>
            <span>&gt;</span>
            <span class="current">{breadcrumb_name}</span>
        </div>
    </div>

    <section class="service-hero">
        <div class="service-hero-content">
            <div class="hero-text">
                <h1>{h1}</h1>
                <p>{intro}</p>
                <div class="hero-features">
                    <div class="hero-feature">
                        {CHECK_SVG}
                        <span>Written Fixed-Price Quote</span>
                    </div>
                    <div class="hero-feature">
                        {CHECK_SVG}
                        <span>Licensed &amp; Insured</span>
                    </div>
                    <div class="hero-feature">
                        {CHECK_SVG}
                        <span>Free On-Site Estimate</span>
                    </div>
                </div>
                <div class="cta-buttons">
                    <a href="tel:{PHONE_T}" class="btn btn-primary">
                        {PHONE_SVG}
                        {PHONE_D}
                    </a>
                    <a href="../contact.html" class="btn btn-secondary">Get Free Estimate</a>
                </div>
            </div>
            <div class="hero-form">
                <form class="service-sidebar-form" action="https://api.web3forms.com/submit" method="POST">
                    <h3>Get Your Free Estimate</h3>
                    <p class="form-subtitle">Written quote, no obligation</p>
                    <div class="form-group">
                        <input type="text" name="name" class="form-input" placeholder="Your Name *" required>
                    </div>
                    <div class="form-group">
                        <input type="tel" name="phone" class="form-input" placeholder="Phone Number *" required>
                    </div>
                    <div class="form-group">
                        <input type="email" name="email" class="form-input" placeholder="Email Address">
                    </div>
                    <div class="form-group">
                        <select name="service" class="form-input" required>
                            <option value="">Select Service *</option>
                            <option value="driveway-installation">Driveway Installation</option>
                            <option value="driveway-replacement">Driveway Replacement</option>
                            <option value="stamped-concrete">Stamped Concrete</option>
                            <option value="patios-walkways">Patios &amp; Walkways</option>
                            <option value="pool-decks">Pool Decks</option>
                            <option value="commercial">Commercial</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <textarea name="message" class="form-input" placeholder="Tell us about your project..." rows="3"></textarea>
                    </div>
                    <input type="hidden" name="source" value="{service} Page">
                    <div class="form-group">
                        <label for="address_{slug}">Service Address *</label>
                        <input type="text" id="address_{slug}" name="address" required placeholder="123 Main St, City, State">
                    </div>
                    <button type="submit" class="btn btn-primary">Request Free Estimate</button>
                    <p class="form-note">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                        Your information is secure and never shared
                    </p>
                </form>
            </div>
        </div>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">When You Need {service}</h2>
        <p class="section-subtitle">{problem_body}</p>
    </section>

    <section class="process-section">
        <div class="process-container">
            <h2 class="section-title split-text">How {service} Works</h2>
            <div class="process-steps">{steps_html}
            </div>
        </div>
    </section>

    <section class="why-section">
        <h2 class="section-title split-text">What Every {service} Job Includes</h2>
        <div class="why-grid">
            <div class="why-content">
                <ul class="feature-list">{includes_html}
                </ul>
            </div>
            <div class="why-image">
                <img src="/images/services/{slug}.webp" alt="{service} in Tampa, FL" loading="lazy" decoding="async" width="800" height="533">
            </div>
        </div>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">What Does {service} Cost in Tampa?</h2>
        <p class="definition-text"><strong>{price_range}.</strong> {price_body}</p>
    </section>

    <section class="faq-section">
        <div class="faq-container">
            <h2 class="section-title split-text">Frequently Asked Questions</h2>
            {faq_items_html}
        </div>
    </section>

    <section class="cta-section" data-aos="fade-up">
        <h2>Ready to Schedule Your {service}?</h2>
        <p>{cta_note}</p>
        <a href="tel:{PHONE_T}" class="btn btn-primary">
            {PHONE_SVG}
            Call {PHONE_D}
        </a>
    </section>

    </main>
"""

    page = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
{nav_header}
{main_content}
{footer}
{FAQ_SCRIPT}
    <!-- Main JavaScript -->
    <script src="/js/main.js"></script>
    <!-- Animation Libraries -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/lenis@1/dist/lenis.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/splitting/dist/splitting.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.js"></script>
    <script src="/js/animations.js"></script>
{MOBILE_CTA_BAR}
{FLOATING_CTA}
</body>
</html>"""
    return page


# ─────────────────────────────────────────────────────────────────────────────
# SERVICE PAGE DATA
# ─────────────────────────────────────────────────────────────────────────────

SERVICE_PAGES = {
    "driveway-installation": {
        "service": "Driveway Installation",
        "h1": "Tampa Driveway Installation — Done Right From the Base Up",
        "intro": "Concrete driveway installation is more than pouring a slab — it's base prep, reinforcement, and controlled curing that determines whether the surface lasts 5 years or 30. Tampa homeowners need it when they're building on a new pad, expanding an undersized single-car, or replacing a surface that was never properly installed in the first place.",
        "problem_h2": "When You Need Driveway Installation",
        "problem_body": "You need new driveway installation when you have bare dirt or gravel where a driveway should be, when your current pad is too narrow for modern vehicles, or when you're building a new home and need the approach done right the first time. Tampa's sandy soil and intense summer rain mean a poorly prepared base will start showing problems within 2–3 years — low spots that hold water, edges that chip, and diagonal cracks that spread from weak control joints. The longer a failing base goes unaddressed, the more excavation it eventually requires.",
        "process_steps": [
            ("Site Prep & Grading", "Existing material removed, grade established to direct water away from the structure, depth confirmed for proper slab thickness."),
            ("Base Compaction", "Compacted gravel base installed — this is the most important step in Florida's sandy-soil conditions. No shortcuts here."),
            ("Rebar & Forming", "Steel reinforcement placed on chairs at the correct height, forms set to the finished elevation, control joints planned before the pour."),
            ("Pour & Finish", "Concrete placed, screeded, and finished to your chosen texture — broom, smooth, or exposed aggregate."),
            ("Cure & Seal", "Curing compound applied immediately after finishing. Walkable in 24–48 hours. Vehicles in 7 days."),
        ],
        "includes": [
            "Free on-site estimate with written quote before any work starts",
            "Full excavation and base compaction to spec",
            "Steel rebar reinforcement — not mesh alone",
            "Control joint layout to manage cracking predictably",
            "Your choice of finish: broom, smooth, or exposed aggregate",
            "Complete site cleanup and debris haul-off",
            "Workmanship warranty on every job",
        ],
        "price_range": "Standard concrete driveway installation in Tampa runs $6–$10 per sq ft",
        "price_body": "A standard two-car driveway (~600 sq ft) typically falls between $3,600 and $6,000, including base prep, reinforcement, and pour. Stamped or decorative finishes run $10–$18/sq ft. What drives the number up: poor existing soil requiring deeper excavation, difficult access, or decorative finish choices. The estimate is free and itemized — no surprises at signing.",
        "faqs": [
            ("Will the new concrete crack?", "Properly installed concrete — correct base, rebar, and control joints — handles residential traffic for 20–30 years. Uncontrolled cracking comes from skipped base prep and missing joints. We don't skip either."),
            ("How long does installation take?", "Most residential driveways take 2–3 days: one day for demo and base, one for the pour, then cure time. You're walking on it in 48 hours and driving on it in 7 days."),
            ("Do I need a permit?", "Many Tampa-area jurisdictions require permits for new driveways. We handle the permit process — you don't need to chase the building department."),
            ("Do I need to be home during the pour?", "You don't need to be present, but we recommend it so we can review the final elevation and finish with you before we leave."),
        ],
        "cta_note": "Spring and fall book fast in Tampa. If you're planning a new driveway, get on the schedule before the busy season fills.",
    },

    "driveway-replacement": {
        "service": "Driveway Replacement",
        "h1": "Tampa Driveway Replacement — Remove the Old, Do the New Right",
        "intro": "Concrete driveway replacement means full demo of the existing slab, correction of whatever failed underneath it, and a proper new installation. Tampa homeowners need it when patching has stopped working, when the base has failed and sections are sinking, or when the surface has cracked so extensively that it's a tripping hazard.",
        "problem_h2": "When You Need Driveway Replacement",
        "problem_body": "Signs you need replacement rather than repair: multiple diagonal cracks across the full slab, sections that have heaved or sunk more than an inch, spalling deeper than the surface layer, or edges that are crumbling rather than chipping. Tampa's wet-dry cycles are hard on concrete that was installed with an inadequate base — the sandy soil erodes under the slab during heavy rain seasons, leaving voids that lead to cracking and settling. Patching voids on top of a failed base is money wasted. The base has to be corrected.",
        "process_steps": [
            ("Demo & Haul-Off", "Old concrete broken up, loaded, and removed from the property. No debris left behind."),
            ("Base Assessment", "Existing subgrade exposed and evaluated. Soft spots, voids, and drainage issues addressed before anything goes back down."),
            ("Base Rebuild", "Compacted gravel base installed to spec — deeper if needed based on what was found under the old slab."),
            ("Rebar, Form & Pour", "Reinforcement placed, forms set, concrete poured and finished to your spec."),
            ("Cure & Final Walkthrough", "Curing compound applied. We walk the job with you before we leave."),
        ],
        "includes": [
            "Free on-site estimate with written itemized quote",
            "Full concrete demo and debris haul-off",
            "Base assessment and correction — we show you what we find",
            "Rebar reinforcement throughout",
            "Your choice of broom, smooth, or decorative finish",
            "Complete site cleanup",
            "Workmanship warranty on every job",
        ],
        "price_range": "Driveway replacement in Tampa typically runs $7–$12 per sq ft",
        "price_body": "That range includes demo (~$1–$2/sq ft), base correction, and the new pour. A 600 sq ft two-car driveway runs roughly $4,200–$7,200 fully replaced. Jobs with significant base failure — deep voids, drainage corrections — land at the higher end. We break out demo, base, and pour in the written quote so you know exactly where the cost is coming from.",
        "faqs": [
            ("Can't I just patch the bad sections?", "Sometimes. If the surrounding slab is structurally sound and the base under the bad section is intact, targeted replacement works. If the base has failed under most of the slab, patching one section means the next fails next year. We'll tell you which situation you're in."),
            ("How long will I be without my driveway?", "Demo on day one, pour on day two for most projects. You're walking on it in 48 hours. Vehicles cleared for day 7. We schedule around your needs as much as possible."),
            ("What about tree roots near the driveway?", "Roots that have lifted or cracked a slab need to be addressed before the new pour — either root pruning, barriers, or rerouting the driveway edge. We evaluate this during the estimate."),
            ("Is replacement always better than resurfacing?", "If the base has failed, resurfacing is a cosmetic fix on a structural problem. Resurfacing makes sense when the slab is solid but the surface is worn. We'll give you an honest assessment of which is appropriate."),
        ],
        "cta_note": "Driveway damage gets worse with every rain season. The sooner the base is corrected, the less excavation the next phase requires.",
    },

    "stamped-concrete": {
        "service": "Stamped Concrete",
        "h1": "Tampa Stamped Concrete — The Look of Stone, the Durability of Concrete",
        "intro": "Stamped concrete is decorative flatwork that mimics brick, flagstone, slate, or cobblestone using patterned stamps pressed into the surface before it sets. Tampa homeowners use it when they want the aesthetic of pavers or natural stone on a driveway, patio, or pool deck — at concrete prices and without the maintenance headaches of individual units.",
        "problem_h2": "When You Need Stamped Concrete",
        "problem_body": "Stamped concrete makes sense when your existing slab is worn and you're ready for an upgrade, when you're building a new patio or driveway and want something that looks more premium than broom finish, or when pavers have been quoted and the price or maintenance concern is holding you back. The caveat with Tampa's climate: stamped concrete needs proper UV-resistant sealer applied on schedule — Florida's sun breaks down sealers faster than northern climates. Skipping resealing is the primary reason stamped surfaces look faded in 3–4 years instead of lasting 15+.",
        "process_steps": [
            ("Design & Color Selection", "Pattern and integral color chosen before the pour. We can show you samples on site."),
            ("Base Prep & Forming", "Same base requirements as standard concrete — no shortcuts because the surface is decorative."),
            ("Pour & Stamp", "Concrete placed and stamps applied while still workable. Color hardener or integral color added to the surface."),
            ("Release Agent & Detailing", "Release agent creates the contrast between highs and lows in the pattern. Grout lines cleaned and detailed."),
            ("Sealer Application", "UV-resistant sealer applied after cure — this is what makes the colors stay vibrant in Tampa's sun."),
        ],
        "includes": [
            "Free on-site estimate with written quote and pattern samples",
            "Full base prep and rebar reinforcement",
            "Pattern stamp of your choice — brick, slate, cobblestone, or custom",
            "Integral color or color hardener",
            "UV-resistant sealer application after cure",
            "Complete site cleanup and debris removal",
            "Workmanship warranty",
        ],
        "price_range": "Stamped concrete in Tampa runs $10–$18 per sq ft",
        "price_body": "That range covers base prep, pour, stamping, color, and sealer. A 400 sq ft patio runs approximately $4,000–$7,200. More intricate multi-color patterns with custom borders land at the higher end. Standard single-pattern driveways are closer to the middle of the range. The estimate is free and itemized — you'll know exactly what you're paying for before we start.",
        "faqs": [
            ("Does stamped concrete crack more than regular concrete?", "No — cracking behavior depends on base prep and control joints, not the surface treatment. Stamped concrete on a correctly prepared base performs the same as plain concrete structurally. What changes is maintenance: the sealer needs to be refreshed every 2–3 years in Florida's UV."),
            ("How does it compare to pavers?", "Pavers cost more to install ($15–$25/sq ft vs. $10–$18) and individual units can shift, sink, or crack over time. Stamped concrete is a single monolithic slab. The trade-off: pavers allow individual unit replacement; a stamped section requires matching the existing pattern if repair is ever needed."),
            ("How long does the color last?", "With proper sealing on schedule, the color stays vibrant for 10–15 years. Without resealing in Florida's sun, fading begins in 3–4 years. We'll walk you through the maintenance schedule when the job is complete."),
            ("Can stamped concrete be used for driveways?", "Yes. Driveways are one of the most popular applications. The same structural requirements apply — proper base, rebar, and control joints — the stamp is applied on top of that foundation."),
        ],
        "cta_note": "Stamped concrete books out 4–6 weeks ahead in spring. If you're planning a patio, driveway, or pool deck upgrade, get on the schedule now.",
    },

    "patios-walkways": {
        "service": "Concrete Patios & Walkways",
        "h1": "Tampa Concrete Patios & Walkways — Built for Outdoor Living",
        "intro": "Concrete patios and walkways are the foundation of functional outdoor living in Tampa. A patio done right provides a flat, durable surface for furniture, grills, and gatherings. A walkway done right connects spaces without becoming a trip hazard after two rainy seasons. Both require proper base prep, drainage slope, and reinforcement to survive Florida's wet-dry cycles without heaving, cracking, or settling.",
        "problem_h2": "When You Need Concrete Patios & Walkways",
        "problem_body": "You need new concrete flatwork when: your patio has cracked or heaved to the point it can't be furniture-ready, your walkway has trip-hazard sections that keep getting worse, or you have bare dirt or stepping stones where a real surface should be. Tampa's heavy summer rains accelerate damage on poorly sloped slabs — water that ponds on a patio undermines the base over time, and walkways without proper cross-slope develop soft spots in the base beneath. Every season these problems compound. They don't resolve on their own.",
        "process_steps": [
            ("Layout & Grade", "Dimensions marked, existing material removed, slope established for drainage — minimum 1/8 inch per foot away from the structure."),
            ("Base Compaction", "Compacted gravel base installed. Depth depends on soil assessment — Tampa's sandy base often requires more compaction effort than it looks."),
            ("Rebar & Form", "Steel reinforcement placed, forms set. Control joints planned for patios larger than 10×10 ft."),
            ("Pour & Finish", "Concrete placed and finished to your spec — broom for traction, smooth for clean look, or decorative."),
            ("Cure & Cleanup", "Curing compound applied. All forms, debris, and excess material removed from the property."),
        ],
        "includes": [
            "Free on-site estimate and written quote before any work starts",
            "Full excavation and base compaction",
            "Rebar reinforcement throughout",
            "Proper drainage slope built into every slab",
            "Your choice of broom, smooth, or decorative finish",
            "Site cleanup and haul-off of all material",
            "Workmanship warranty",
        ],
        "price_range": "Concrete patios in Tampa run $5–$8 per sq ft",
        "price_body": "A 400 sq ft backyard patio typically falls between $2,000 and $3,200, including excavation, base, and pour. Walkways run $5–$7/sq ft depending on width and length. Decorative finishes (stamped, exposed aggregate) push costs higher — see our stamped concrete page for those ranges. Site conditions that require extra base work or drainage solutions will add to the total; we break those out in the written estimate.",
        "faqs": [
            ("Do I need a permit for a patio?", "Most jurisdictions in the Tampa area require permits for patios over a certain size (typically 200 sq ft). We verify permit requirements for your specific address before starting and handle the application process."),
            ("How long will the concrete take to cure?", "Walkable in 24–48 hours. Patio furniture in 7 days. Full structural cure takes 28 days — the concrete is functional well before then, but it gets progressively stronger throughout that period."),
            ("How do I prevent cracking on a large patio?", "Control joints. A patio larger than 10×10 ft needs strategically placed joints that guide any cracking to happen in predictable straight lines rather than random diagonal cracks across the slab. We plan joint locations before the pour."),
            ("Can the walkway match my existing concrete?", "Exact color matching is difficult on weathered concrete. We can get close with integral color or surface treatments, and we'll discuss the options during the estimate so you know what to expect."),
        ],
        "cta_note": "Tampa's outdoor season runs year-round. If you want the patio ready before summer entertaining season, now is the time to schedule the estimate.",
    },

    "pool-decks": {
        "service": "Pool Deck Installation",
        "h1": "Tampa Pool Deck Installation — Safe, Cool, Built for Florida",
        "intro": "Pool deck installation is flatwork with two non-negotiable requirements: slip resistance and heat management. Tampa's combination of pool chemistry, intense UV, and barefoot traffic makes the finish selection and base prep critical. A pool deck done wrong becomes a burned-foot hazard in summer and a cracked, stained liability within a few seasons.",
        "problem_h2": "When You Need Pool Deck Installation",
        "problem_body": "Common triggers: existing pool deck is cracked or heaved to the point of being a trip hazard, surface has become dangerously slick when wet, old deck is flaking from chemical exposure or UV breakdown, or you're installing a new pool and need the surround done right from the start. Pool decks in Tampa get more UV hours and more water traffic than almost any surface on the property. When the base fails, water gets under the slab and the chlorine from splash-out accelerates deterioration. Catching it before full failure is significantly cheaper than replacing a deck that has buckled.",
        "process_steps": [
            ("Assessment & Design", "Deck layout designed for drainage away from the pool and structure. Existing deck condition evaluated for partial vs. full replacement."),
            ("Demo & Base Prep", "Old material removed. Base corrected for drainage — pool decks require careful slope management to direct water away from both the pool and the building."),
            ("Reinforcement & Forming", "Rebar placed throughout. Expansion joints planned around the pool coping and any adjacent structures."),
            ("Pour & Texture", "Non-slip finish applied — broom finish, travertine texture, or exposed aggregate. Color hardener or integral color optional."),
            ("Cure & Seal", "Appropriate sealer for pool-adjacent surfaces applied after cure — must be compatible with chlorine and UV exposure."),
        ],
        "includes": [
            "Free on-site estimate with written quote",
            "Full base prep and drainage assessment",
            "Steel rebar reinforcement throughout",
            "Non-slip surface finish — required for pool safety",
            "Expansion joints at pool coping and structure transitions",
            "Sealer rated for chlorine and UV exposure",
            "Complete site cleanup",
            "Workmanship warranty",
        ],
        "price_range": "Pool deck installation in Tampa runs $5–$8 per sq ft",
        "price_body": "A 600 sq ft pool surround typically falls between $3,000 and $4,800, including demo (if replacing), base prep, and pour. Decorative finishes (travertine texture, exposed aggregate, stamped) add $3–$8/sq ft to the base cost. What drives cost: size of the deck, existing conditions, proximity to the pool equipment pad, and finish selection. The estimate is free and written — no surprises.",
        "faqs": [
            ("What finish is best for a pool deck in Florida?", "Broom finish provides good slip resistance and is the most cost-effective. Exposed aggregate is popular — the aggregate provides grip and stays cooler underfoot than smooth concrete. Travertine-look stamped concrete adds the premium aesthetic. We'll review options based on your budget and usage."),
            ("Will chlorine damage the concrete?", "Concrete itself is resistant to pool chemicals at normal concentrations. The sealer is the element that needs to be chlorine-compatible — we use sealers rated for pool-adjacent applications. Annual inspection of the sealer condition keeps the surface protected."),
            ("How long will we be without the pool?", "Most deck replacement projects take 3–5 days including demo, base, pour, and initial cure. The deck is walkable in 48 hours but we recommend waiting the full 7 days before heavy pool traffic on the fresh surface."),
            ("Do you handle the area around the pool equipment?", "Yes. Pad replacement or expansion around pump and filter equipment is part of many pool deck projects. We work around the plumbing and electrical without disturbing it."),
        ],
        "cta_note": "Pool season in Tampa is effectively year-round. If your deck needs work, the best time to schedule is before the height of summer traffic.",
    },

    "commercial": {
        "service": "Commercial Concrete",
        "h1": "Tampa Commercial Concrete — Heavy-Duty Flatwork for Business Properties",
        "intro": "Commercial concrete is residential flatwork scaled up in load requirements, surface area, and project complexity. Tampa businesses need it for parking lots, loading dock aprons, warehouse floors, commercial driveways, and large-scale hardscaping. The difference from residential: heavier vehicle loads, more square footage, tighter scheduling constraints, and usually permit requirements that residential projects don't have.",
        "problem_h2": "When You Need Commercial Concrete",
        "problem_body": "Signs a commercial concrete project is overdue: parking lot surfaces cracking under vehicle loads that the original pour wasn't designed for, loading dock aprons that have settled and created a lip that damages vehicles, warehouse floors with trip-hazard cracks that create liability exposure, or new construction that needs concrete installed on a schedule tied to other trades. Commercial concrete failures are more costly than residential because they affect operations, create liability, and require larger-scale remediation. The base requirements for commercial work are more stringent — thicker slabs, heavier reinforcement, and often engineered specifications.",
        "process_steps": [
            ("Site Assessment & Engineering", "Load requirements, drainage, and permit needs evaluated. Commercial projects often require engineer-stamped plans."),
            ("Demo & Excavation", "Existing material removed. Commercial-grade excavation equipment used for larger footprints."),
            ("Base & Reinforcement", "Engineered base depth installed. Heavy rebar grid or post-tension cable depending on load specs."),
            ("Commercial Pour", "Ready-mix delivered to spec. Larger pours managed in sections with proper joint placement."),
            ("Finishing & Cure", "Surface finished to application requirements — broom for outdoor traffic, smooth or diamond-ground for interiors. Cure managed to spec."),
        ],
        "includes": [
            "Free site consultation and written project quote",
            "Permit application and coordination with Tampa building departments",
            "Engineered base and reinforcement to load specifications",
            "Proper joint layout for commercial slab dimensions",
            "Finish appropriate to the application — traffic, forklift, or pedestrian",
            "Full site cleanup and material haul-off",
            "Commercial workmanship warranty",
        ],
        "price_range": "Commercial concrete in Tampa runs $6–$12 per sq ft",
        "price_body": "That range covers standard commercial flatwork. Industrial floors with higher load specs, polished finishes, or chemical-resistant coatings are quoted separately based on specifications. Large-footprint projects (parking lots, warehouse floors) often come in closer to the lower end of the range due to scale efficiency. We provide itemized quotes that break out excavation, base, reinforcement, and pour separately.",
        "faqs": [
            ("Can you handle large parking lot projects?", "Yes. We work on commercial parking lots, retail pads, and multi-use development flatwork throughout the Tampa Bay area. Large projects are sequenced in pours to minimize business disruption."),
            ("Do you work on a timeline tied to other construction trades?", "Yes. Commercial projects are coordinated with general contractors and other trades. We're accustomed to sequenced scheduling and can meet phased completion milestones."),
            ("Do you pull commercial permits?", "Yes. Commercial concrete in Tampa and Hillsborough County typically requires permits, inspections, and sometimes engineer-stamped plans. We handle the permit process from application through final inspection."),
            ("What about ADA compliance for commercial driveways and walkways?", "Commercial flatwork must meet ADA slope requirements for accessible routes. We design and install to ADA specifications and can provide documentation for permitting and compliance records."),
        ],
        "cta_note": "Commercial projects have longer lead times for materials and scheduling. Contact us early in your planning process to secure the timeline you need.",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# LOCATION PAGE DATA
# ─────────────────────────────────────────────────────────────────────────────

LOCATION_DATA = {
    "apollo-beach": {
        "display": "Apollo Beach",
        "r1_name": "Chris P.", "r1_city": "Apollo Beach",
        "r1_quote": "The driveway had been cracking for two years — we're near the water and the sandy base had washed out underneath. They dug it out, showed me what was going on before any work started, re-compacted everything, and poured fresh. Six months later, no new cracks.",
        "r2_name": "Rachel W.", "r2_city": "Apollo Beach",
        "r2_quote": "Had the front walkway and entry pad replaced before listing. The buyer's inspector didn't flag a single exterior issue. Clean job, honest timeline.",
        "service_area": "Ruskin, Gibsonton, Riverview, and South Hillsborough County",
    },
    "brandon": {
        "display": "Brandon",
        "r1_name": "Jason P.", "r1_city": "Brandon",
        "r1_quote": "The driveway had been cracking for three years. I kept patching it myself. Finally got the full replacement done — they pulled the old slab, showed me the base had basically washed out underneath, re-compacted everything, and poured fresh. Six months later and zero cracks.",
        "r2_name": "Carla W.", "r2_city": "Brandon",
        "r2_quote": "Had our walkway and front stoop replaced before listing the house. The inspector on the buyer's side didn't flag a single exterior issue. Quick job, clean work, fair price.",
        "service_area": "Valrico, Riverview, Seffner, and Southeast Hillsborough County",
    },
    "carrollwood": {
        "display": "Carrollwood",
        "r1_name": "Mike D.", "r1_city": "Carrollwood",
        "r1_quote": "The circular driveway had been deteriorating for years. They assessed the whole thing, showed me the base failure near the drainage side, rebuilt the base properly, and the new slab looks like it'll outlast the house.",
        "r2_name": "Diane F.", "r2_city": "Carrollwood",
        "r2_quote": "We had the backyard patio replaced — it had been heaving near the screen enclosure footer. They leveled it properly, poured a clean slab, and the enclosure contractors came right in after. No issues.",
        "service_area": "Northdale, Lutz, Town 'N' Country, and North Tampa",
    },
    "channelside": {
        "display": "Channelside",
        "r1_name": "Marcus T.", "r1_city": "Channelside",
        "r1_quote": "Needed the loading area behind our property poured on a tight timeline. They showed up on schedule, got the base prepped the first day, poured the second, and we were back to operations in 48 hours.",
        "r2_name": "Jennifer R.", "r2_city": "Channelside",
        "r2_quote": "The front walkway at our unit was cracked and had become a hazard. Replacement was clean, fast, and they matched the adjacent concrete finish well.",
        "service_area": "Downtown Tampa, Ybor City, Port Tampa, and Harbour Island",
    },
    "clearwater": {
        "display": "Clearwater",
        "r1_name": "Tom G.", "r1_city": "Clearwater",
        "r1_quote": "We'd been putting off the driveway replacement for two years. When they finally dug it up, the base near the street was completely compromised — just sand. They corrected it properly and the new pour has been solid.",
        "r2_name": "Nicole S.", "r2_city": "Clearwater",
        "r2_quote": "Pool deck was cracking and getting slick. They replaced the damaged sections, added proper drainage slope, and finished it with a broom texture that's actually safe to walk on barefoot now.",
        "service_area": "Dunedin, Safety Harbor, Largo, and Pinellas County",
    },
    "hyde-park": {
        "display": "Hyde Park",
        "r1_name": "Steven L.", "r1_city": "Hyde Park",
        "r1_quote": "The driveway apron had been cracking since the city replaced the sidewalk and the base never recovered. They removed the damaged section, corrected the base, and matched the finish to the existing driveway as close as you can get.",
        "r2_name": "Amanda B.", "r2_city": "Hyde Park",
        "r2_quote": "We had the side entry walkway replaced — it was heaved from tree roots. They handled the root situation properly and the new walkway has been level and clean for over a year.",
        "service_area": "South Tampa, Palma Ceia, Bayshore, and Downtown Tampa",
    },
    "land-o-lakes": {
        "display": "Land O' Lakes",
        "r1_name": "Kevin H.", "r1_city": "Land O' Lakes",
        "r1_quote": "Brand new driveway installation on a property with nothing there. They graded it properly for drainage, poured a clean 3-car wide slab, and it's been holding up through every rain season since.",
        "r2_name": "Patricia M.", "r2_city": "Land O' Lakes",
        "r2_quote": "Had the backyard patio poured to tie into the screen enclosure. The drainage slope was done right — no pooling after storms, which was the problem with our previous contractor's work.",
        "service_area": "Wesley Chapel, Lutz, Zephyrhills, and North Pasco County",
    },
    "largo": {
        "display": "Largo",
        "r1_name": "Frank S.", "r1_city": "Largo",
        "r1_quote": "The driveway was cracking in multiple places and had a section that had sunk almost two inches. Full replacement — they showed me the base had washed out and rebuilt it right. No cracking at 8 months out.",
        "r2_name": "Melissa J.", "r2_city": "Largo",
        "r2_quote": "Walkway from the driveway to the back gate was in bad shape. They poured a clean replacement, matched the existing width, and the job was done in a day.",
        "service_area": "Clearwater, Seminole, Pinellas Park, and Central Pinellas County",
    },
    "lutz": {
        "display": "Lutz",
        "r1_name": "Robert N.", "r1_city": "Lutz",
        "r1_quote": "Three-car driveway, full replacement. They dug out the old slab and found a soft spot near the garage that had been causing the cracking. Corrected the base, poured clean, and haven't had an issue since.",
        "r2_name": "Susan A.", "r2_city": "Lutz",
        "r2_quote": "Patio off the back of the house needed to be expanded and the existing section repoured. They matched the finish well and the drainage slope they built in has kept water moving away from the foundation.",
        "service_area": "Land O' Lakes, Odessa, Carrollwood, and North Hillsborough County",
    },
    "new-tampa": {
        "display": "New Tampa",
        "r1_name": "David C.", "r1_city": "New Tampa",
        "r1_quote": "Newer home but the original driveway was undersized. They poured a full-width extension, matched the existing concrete finish, and the transition is clean. You can barely tell it was two separate pours.",
        "r2_name": "Karen V.", "r2_city": "New Tampa",
        "r2_quote": "Had the side walkway and patio replaced after the previous contractor's work started failing. Base this time was done right — no settling, no cracking after two full rainy seasons.",
        "service_area": "Wesley Chapel, Temple Terrace, Zephyrhills, and Northeast Hillsborough County",
    },
    "plant-city": {
        "display": "Plant City",
        "r1_name": "Gary O.", "r1_city": "Plant City",
        "r1_quote": "Farm property — we needed a commercial-grade apron poured at the entrance. They assessed the load requirements, poured it thicker than standard with heavier rebar, and it's holding up to truck traffic without issue.",
        "r2_name": "Linda P.", "r2_city": "Plant City",
        "r2_quote": "Had the residential driveway replaced — it was old, cracked, and the base near the road had deteriorated. Clean new slab, proper base, and they were done in two days.",
        "service_area": "Brandon, Lakeland, Valrico, and Eastern Hillsborough County",
    },
    "riverview": {
        "display": "Riverview",
        "r1_name": "James R.", "r1_city": "Riverview",
        "r1_quote": "Newer neighborhood but the original driveway had cracked badly after two years — the base work by the builder was minimal. Full replacement, proper base this time, and it's been clean for 14 months.",
        "r2_name": "Lisa W.", "r2_city": "Riverview",
        "r2_quote": "Had the backyard patio and walkway to the pool area poured. The drainage slope keeps water away from the screen enclosure footer, which was a recurring issue before.",
        "service_area": "Brandon, Apollo Beach, Gibsonton, and South Hillsborough County",
    },
    "safety-harbor": {
        "display": "Safety Harbor",
        "r1_name": "Paul E.", "r1_city": "Safety Harbor",
        "r1_quote": "Older home with an original 1970s driveway — it had settled unevenly and had cracks across the full width. They removed it, rebuilt the base, and the new slab is level and clean.",
        "r2_name": "Christine D.", "r2_city": "Safety Harbor",
        "r2_quote": "Pool deck was cracking near the coping and had become a safety concern. Replacement was thorough — they addressed the drainage issue that was causing water to sit under the slab.",
        "service_area": "Clearwater, Dunedin, Oldsmar, and Northwest Hillsborough County",
    },
    "seminole-heights": {
        "display": "Seminole Heights",
        "r1_name": "Alex K.", "r1_city": "Seminole Heights",
        "r1_quote": "Bungalow from the 1940s — the original driveway had been patched so many times it was more patch than driveway. Full replacement, new base, and it finally looks like it belongs with the house.",
        "r2_name": "Monica G.", "r2_city": "Seminole Heights",
        "r2_quote": "Front sidewalk approach and entry pad replaced. The heaved sections were a hazard and they'd been getting worse every year. Clean work, fast completion, no issues.",
        "service_area": "Riverside Heights, Tampa Heights, Ybor City, and Central Tampa",
    },
    "south-tampa": {
        "display": "South Tampa",
        "r1_name": "Brian F.", "r1_city": "South Tampa",
        "r1_quote": "The driveway had a diagonal crack running the full width — classic base failure. They did the full replacement, showed me what they found underneath, rebuilt the base properly. Clean pour, no issues at 10 months.",
        "r2_name": "Sarah H.", "r2_city": "South Tampa",
        "r2_quote": "Stamped concrete patio off the back of our home. The pattern and color look exactly like what we saw in the samples, and the drainage slope they built in keeps it clean and dry after storms.",
        "service_area": "Hyde Park, Palma Ceia, Bayshore, and Westshore",
    },
    "st-pete": {
        "display": "St. Petersburg",
        "r1_name": "Mark L.", "r1_city": "St. Pete",
        "r1_quote": "Old driveway had been deteriorating for years — cracking, spalling at the edges, section near the curb had sunk. They replaced the whole thing, corrected the base, and it's been holding up perfectly through storm season.",
        "r2_name": "Amy N.", "r2_city": "St. Pete",
        "r2_quote": "Had our walkway and back patio replaced before selling. Appraiser noted the exterior improvements and the house sold quickly. Clean work from start to finish.",
        "service_area": "St. Petersburg, Gulfport, Pinellas Park, and South Pinellas County",
    },
    "st-petersburg": {
        "display": "St. Petersburg",
        "r1_name": "Victor Q.", "r1_city": "St. Petersburg",
        "r1_quote": "Commercial property — needed the parking lot approach resurfaced and a cracked apron replaced. They sequenced the work to minimize business disruption. Done in two days, solid result.",
        "r2_name": "Theresa B.", "r2_city": "St. Petersburg",
        "r2_quote": "Residential driveway, full replacement. The original was original to the house — 1960s. New base, new rebar, and a clean broom finish. Should last another 30 years.",
        "service_area": "Gulfport, Pinellas Park, Largo, and Central Pinellas County",
    },
    "temple-terrace": {
        "display": "Temple Terrace",
        "r1_name": "Carl Z.", "r1_city": "Temple Terrace",
        "r1_quote": "Driveway was cracking badly — tree root had lifted one section and the base around it had undermined. They removed the section, handled the root barrier, corrected the base, and poured clean. Level and solid.",
        "r2_name": "Deborah Y.", "r2_city": "Temple Terrace",
        "r2_quote": "Patio and walkway replacement for a house we were renovating to sell. The concrete work was one of the first things people noticed at the open house. Clean finish, proper drainage slope.",
        "service_area": "New Tampa, Brandon, Thonotosassa, and East Hillsborough County",
    },
    "valrico": {
        "display": "Valrico",
        "r1_name": "Dan U.", "r1_city": "Valrico",
        "r1_quote": "New driveway installation on a new build. The builder's concrete had cracked within a year — we had them redo it with proper base compaction and rebar. No issues two rainy seasons later.",
        "r2_name": "Patricia X.", "r2_city": "Valrico",
        "r2_quote": "Had the side walkway and patio extended. They matched the existing concrete finish reasonably well and the drainage is correct — no pooling after heavy rain.",
        "service_area": "Brandon, Riverview, Plant City, and East Hillsborough County",
    },
    "wesley-chapel": {
        "display": "Wesley Chapel",
        "r1_name": "Aaron T.", "r1_city": "Wesley Chapel",
        "r1_quote": "Brand new driveway on a new build. I'd seen what happens when builders use minimal base prep. These guys compacted the base properly and placed rebar — two rainy seasons and the slab is still perfect.",
        "r2_name": "Rachel S.", "r2_city": "Wesley Chapel",
        "r2_quote": "Had a large backyard patio poured for outdoor living. They planned the drainage slope properly so water runs away from the house after storms. We entertain out there every weekend.",
        "service_area": "Land O' Lakes, Zephyrhills, Lutz, and North Pasco County",
    },
    "westchase": {
        "display": "Westchase",
        "r1_name": "Michael I.", "r1_city": "Westchase",
        "r1_quote": "The driveway had a large low spot near the garage that pooled after every storm. They corrected the grade while replacing the slab — no more standing water, and the new concrete is clean.",
        "r2_name": "Laura C.", "r2_city": "Westchase",
        "r2_quote": "Stamped concrete patio that replaced an old wooden deck. The pattern looks great, the surface is cooler than the old wood in summer, and we've had zero maintenance issues.",
        "service_area": "Town 'N' Country, Odessa, Carrollwood, and West Hillsborough County",
    },
    "ybor-city": {
        "display": "Ybor City",
        "r1_name": "Anthony J.", "r1_city": "Ybor City",
        "r1_quote": "Historic district property with narrow access — not every contractor wants to deal with it. They got the equipment in, removed the old cracked apron, and poured a clean replacement. No damage to the adjacent brick work.",
        "r2_name": "Rosa M.", "r2_city": "Ybor City",
        "r2_quote": "Commercial property walkway replacement. The old surface was a liability. New pour, proper slope, non-slip finish. Done on schedule.",
        "service_area": "Downtown Tampa, Channelside, Seminole Heights, and Central Tampa",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# LOCATION PAGE BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def build_location_page(slug, data, existing_head):
    """Build a location page using PAS Template-B."""
    city = data["display"]
    r1n, r1c, r1q = data["r1_name"], data["r1_city"], data["r1_quote"]
    r2n, r2c, r2q = data["r2_name"], data["r2_city"], data["r2_quote"]
    sa = data["service_area"]

    # Inline CSS matching existing location pages (preserved)
    inline_css = """<style>
    .location-hero { background: linear-gradient(135deg, #1e3a5f 0%, #2c5282 100%); color: white; padding: 60px 20px 40px; text-align: center; }
    .location-hero h1 { font-size: 2.2rem; font-weight: 800; margin-bottom: 16px; line-height: 1.2; }
    .location-hero .hero-sub { font-size: 1.1rem; opacity: 0.9; max-width: 600px; margin: 0 auto 24px; }
    .hero-phone { display: inline-block; background: #f97316; color: white; font-size: 1.3rem; font-weight: 800; padding: 16px 36px; border-radius: 8px; text-decoration: none; margin: 8px; }
    .hero-phone-secondary { display: inline-block; background: rgba(255,255,255,0.15); color: white; font-size: 1rem; font-weight: 600; padding: 14px 28px; border-radius: 8px; text-decoration: none; margin: 8px; border: 1px solid rgba(255,255,255,0.3); }
    .location-content { max-width: 800px; margin: 0 auto; padding: 48px 20px; font-family: 'Inter', system-ui, sans-serif; line-height: 1.75; color: #222; }
    .location-content h2 { font-size: 1.4rem; font-weight: 700; margin-top: 40px; margin-bottom: 16px; color: #1e3a5f; border-bottom: 2px solid #f0f0f0; padding-bottom: 8px; }
    .location-content p { margin-bottom: 1.2em; }
    .pas-bullets { padding-left: 0; list-style: none; }
    .pas-bullets li { padding: 10px 0 10px 28px; position: relative; border-bottom: 1px solid #f0f0f0; }
    .pas-bullets li::before { content: "→"; position: absolute; left: 0; color: #f97316; font-weight: 700; }
    .pas-bullets li strong { color: #1e3a5f; }
    .process-steps { counter-reset: steps; list-style: none; padding: 0; }
    .process-steps li { counter-increment: steps; padding: 16px 16px 16px 60px; position: relative; margin-bottom: 12px; background: #f8f9fa; border-radius: 8px; }
    .process-steps li::before { content: counter(steps); position: absolute; left: 16px; top: 50%; transform: translateY(-50%); background: #1e3a5f; color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; }
    .testimonial-block { background: #f8f9fa; border-left: 4px solid #f97316; padding: 20px 24px; border-radius: 0 8px 8px 0; margin-bottom: 20px; }
    .testimonial-block blockquote { margin: 0 0 8px; font-style: italic; color: #333; line-height: 1.6; }
    .testimonial-block cite { font-size: 0.9rem; color: #666; font-style: normal; font-weight: 600; }
    .pricing-table { width: 100%; border-collapse: collapse; margin: 20px 0; }
    .pricing-table th { background: #1e3a5f; color: white; padding: 12px 16px; text-align: left; font-size: 0.9rem; }
    .pricing-table td { padding: 12px 16px; border-bottom: 1px solid #eee; font-size: 0.95rem; }
    .pricing-table tr:nth-child(even) td { background: #f8f9fa; }
    .pricing-note { font-size: 0.9rem; color: #555; margin-top: 12px; }
    .faq-section { margin-top: 40px; }
    .faq-item { border-bottom: 1px solid #eee; padding: 20px 0; }
    .faq-item h3 { font-size: 1rem; font-weight: 700; margin-bottom: 8px; color: #1e3a5f; }
    .faq-item p { margin: 0; color: #444; }
    .cta-section { background: linear-gradient(135deg, #1e3a5f, #2c5282); color: white; padding: 48px 32px; margin-top: 0; text-align: center; }
    .cta-section h2 { color: white; font-size: 1.6rem; border: none; margin-top: 0; }
    .cta-section p { opacity: 0.9; margin-bottom: 24px; }
    .cta-button { display: inline-block; background: #f97316; color: white; font-size: 1.2rem; font-weight: 800; padding: 16px 36px; border-radius: 8px; text-decoration: none; margin: 8px; }
    .cta-button-secondary { display: inline-block; background: rgba(255,255,255,0.15); color: white; font-size: 1rem; font-weight: 600; padding: 14px 28px; border-radius: 8px; text-decoration: none; margin: 8px; border: 1px solid rgba(255,255,255,0.3); }
    .areas-we-serve { background: #f8f9fa; padding: 48px 20px; }
    .areas-inner { max-width: 800px; margin: 0 auto; }
    .areas-we-serve h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 16px; color: #1e3a5f; }
    .areas-we-serve ul { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 8px; list-style: none; padding: 0; }
    .areas-we-serve li a { color: #2563eb; text-decoration: none; font-size: 0.95rem; }
    .areas-we-serve li a:hover { text-decoration: underline; }
    .breadcrumb { font-size: 0.85rem; color: #666; padding: 12px 20px; max-width: 800px; margin: 0 auto; }
    .breadcrumb a { color: #2563eb; text-decoration: none; }
    @media (max-width: 640px) { .location-hero h1 { font-size: 1.5rem; } .hero-phone { font-size: 1.1rem; padding: 14px 24px; } .location-content { padding: 32px 16px; } }
</style>"""

    # Floating CTA (location pages have it too)
    float_cta = """<div class="floating-cta" id="floating-cta">
  <a href="tel:+18137059021" class="fcta-call" aria-label="Call Now"><span class="fcta-label">Call Now</span><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg></a>
  <a href="/contact.html" class="fcta-quote" aria-label="Free Quote"><span class="fcta-label">Free Quote</span><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></a>
</div>
<script>
(function(){{
  var el=document.getElementById('floating-cta');
  if(!el)return;
  window.addEventListener('scroll',function(){{
    el.classList.toggle('visible',window.scrollY>80);
  }},{{passive:true}});
}})();
</script>
<style>
.floating-cta{{position:fixed;bottom:20px;right:20px;z-index:998;display:flex;flex-direction:column;gap:12px;transform:translateY(110px);opacity:0;transition:transform .5s cubic-bezier(.34,1.56,.64,1),opacity .4s ease;pointer-events:none}}
.floating-cta.visible{{transform:translateY(0);opacity:1;pointer-events:auto}}
.floating-cta a{{display:flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;color:#fff;text-decoration:none;box-shadow:0 4px 16px rgba(0,0,0,.25);transition:transform .2s ease,box-shadow .2s ease;position:relative}}
.floating-cta a:hover{{transform:scale(1.1);box-shadow:0 6px 24px rgba(0,0,0,.3)}}
.fcta-call{{background:#22c55e}}
.fcta-quote{{background:#1e3a5f}}
.fcta-label{{position:absolute;right:64px;white-space:nowrap;background:rgba(0,0,0,.75);color:#fff;padding:5px 12px;border-radius:20px;font-size:.78rem;font-weight:600;opacity:0;pointer-events:none;transition:opacity .2s ease}}
.floating-cta a:hover .fcta-label{{opacity:1}}
@media(min-width:769px){{.floating-cta{{display:none!important}}}}
</style>"""

    # Clean up the existing head — remove old inline CSS (we add our own below)
    head_clean = re.sub(r'<style>.*?</style>', '', existing_head, flags=re.DOTALL)
    # Remove old style.css link (different path), add our inline styles
    head_clean = re.sub(r'<link rel="stylesheet" href="\.\./css/style\.css"[^>]*>', '', head_clean)

    page = f"""<!DOCTYPE html>
<html lang="en">
{head_clean}
{inline_css}
<body>
  <header>
    <nav style="background:#1e3a5f;padding:12px 20px;display:flex;justify-content:space-between;align-items:center;">
      <a href="/" style="color:white;font-weight:800;font-size:1.1rem;text-decoration:none;">Tampa Concrete <span style="color:#f97316;">Pros</span></a>
      <a href="tel:{PHONE_T}" style="color:white;font-weight:700;font-size:1rem;text-decoration:none;background:#f97316;padding:8px 16px;border-radius:6px;">{PHONE_D}</a>
    </nav>
  </header>
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="/">Home</a> &rsaquo; <a href="/locations/">Locations</a> &rsaquo; <span>Concrete Services in {city}</span>
  </nav>

  <main>
    <section class="location-hero">
      <h1>Concrete Driveways &amp; Flatwork in {city} — Free Estimates</h1>
      <p class="hero-sub">Serving {city}, Tampa &amp; surrounding FL communities &middot; We call back within 1 hour</p>
      <a href="tel:{PHONE_T}" class="hero-phone">&#128222; {PHONE_D}</a>
      <a href="/contact.html" class="hero-phone-secondary">Get Free Estimate</a>
    </section>

    <div class="location-content">

      <h2>A Cracked Driveway Doesn't Fix Itself</h2>
      <p>That crack you've been watching? It's wider than it was last year. The section that settled after the last heavy storm isn't going back up. And the patio or walkway that "just needs to be cleaned" is actually starting to flake at the surface.</p>
      <p>Concrete deterioration is progressive — every rain event, every vehicle crossing, every wet-dry cycle pushes the damage further. In {city}, Tampa's sandy soil and intense summer rainfall make the base the critical variable: once water finds its way under the slab, it erodes the base with every storm. Waiting doesn't save money. It adds to the repair scope and narrows the contractor scheduling window before the next busy season.</p>
      <p>If your driveway, patio, or walkway is cracked, heaved, spalled, or just overdue — it's time to get a real assessment and a straight quote.</p>

      <h2>What Deteriorating Concrete Is Actually Costing You</h2>
      <ul class="pas-bullets">
        <li><strong>Water infiltration gets worse every season.</strong> Cracks let water under the slab, which undermines the base and turns a cosmetic issue into a structural one.</li>
        <li><strong>Trip hazards are a liability.</strong> A heaved section is a problem for family, guests, and delivery drivers before someone gets hurt.</li>
        <li><strong>Base failure multiplies the repair cost.</strong> A failed base means more excavation, more gravel, and more labor — all additive to a project you were going to do anyway.</li>
        <li><strong>Buyers and inspectors notice.</strong> Concrete in poor condition is one of the first flags in a home inspection. It signals deferred maintenance before they even step inside.</li>
        <li><strong>Florida's UV accelerates the timeline.</strong> The same UV that fades surfaces also degrades sealers faster here than in northern climates — once the sealer fails, moisture infiltration starts immediately.</li>
      </ul>

      <h2>How We Handle Concrete in {city}</h2>
      <ol class="process-steps">
        <li><strong>Free on-site estimate.</strong> We assess the slab, the base, and whatever's driving the damage. You get a written quote — full replacement, partial repair, or leveling — before we leave.</li>
        <li><strong>Demo and prep.</strong> Old concrete removed and hauled off. Base graded, compacted, and corrected. This step determines whether new concrete lasts two years or twenty.</li>
        <li><strong>Reinforcement, forming, and pour.</strong> Rebar or mesh — correctly placed, correct depth. Control joints planned before the pour, not after. Finish of your choice: broom, smooth, exposed aggregate, or stamped.</li>
        <li><strong>Cure and handoff.</strong> Walkable in 24–48 hours. Vehicles in 7 days. Full cure in 28. We walk the job with you before we leave.</li>
      </ol>

      <h2>What {city} Homeowners Say</h2>
      <div class="testimonial-block">
        <blockquote>"{r1q}"</blockquote>
        <cite>— {r1n} &middot; {r1c}</cite>
      </div>
      <div class="testimonial-block">
        <blockquote>"{r2q}"</blockquote>
        <cite>— {r2n} &middot; {r2c}</cite>
      </div>

      <h2>What Does Concrete Work Cost Near {city}?</h2>
      <p>Honest ranges for common projects:</p>
      <table class="pricing-table">
        <thead><tr><th>Project</th><th>Price Range</th></tr></thead>
        <tbody>
          <tr><td>Concrete removal &amp; haul-off</td><td>$1–$2/sq ft</td></tr>
          <tr><td>New driveway (standard)</td><td>$6–$10/sq ft</td></tr>
          <tr><td>Stamped/decorative concrete</td><td>$10–$18/sq ft</td></tr>
          <tr><td>Concrete patio</td><td>$5–$8/sq ft</td></tr>
          <tr><td>Mudjacking/leveling</td><td>$500–$2,000</td></tr>
        </tbody>
      </table>
      <p class="pricing-note">A standard two-car driveway (~600 sq ft) runs <strong>$3,600–$6,000</strong> for full replacement including demo, base prep, and pour. Quotes are itemized in writing — no surprises at signing.</p>

      <div class="faq-section">
        <h2>Quick Answers Before You Call</h2>

        <div class="faq-item">
          <h3>Will the new concrete crack like the old one?</h3>
          <p>Correctly installed concrete — proper base, reinforcement, and control joints — handles residential traffic for 20–30 years. Uncontrolled cracking comes from skipped base prep and missing control joints. We don't skip either.</p>
        </div>

        <div class="faq-item">
          <h3>Can you just patch the bad section?</h3>
          <p>Sometimes yes. If the surrounding slab is structurally sound and the base is intact, targeted patch or partial replacement works. If the base has failed, patching one section means the next fails next year. We'll tell you which situation you're in before any work starts.</p>
        </div>

        <div class="faq-item">
          <h3>How long is the driveway out of service?</h3>
          <p>Demo day one, pour day two for most projects. Walkable in 24–48 hours. Vehicles cleared in 7 days. We schedule around your needs as much as possible.</p>
        </div>

        <div class="faq-item">
          <h3>Do you work in {city}?</h3>
          <p>Yes. We regularly pour in {city} and serve {sa}. Response time is typically within 1 hour for estimate scheduling.</p>
        </div>
      </div>

    </div><!-- /.location-content -->

    <section class="cta-section">
      <h2>Get a Free Estimate for Your {city} Concrete Project</h2>
      <p>Spring and fall book fast. If you're planning a repair, replacement, or new flatwork, get on the schedule before the busy season fills.</p>
      <p><strong>{PHONE_D}</strong> — we answer or call back within 1 hour.</p>
      <a href="tel:{PHONE_T}" class="cta-button">&#128222; Call {PHONE_D}</a>
      <a href="/contact.html" class="cta-button-secondary">Request Free Estimate Online</a>
    </section>

    <section class="areas-we-serve">
      <div class="areas-inner">
        <h3>Other Areas We Serve Near Tampa</h3>
        <ul>
          <li><a href="/locations/brandon.html">Concrete Services in Brandon</a></li>
          <li><a href="/locations/riverview.html">Concrete Services in Riverview</a></li>
          <li><a href="/locations/clearwater.html">Concrete Services in Clearwater</a></li>
          <li><a href="/locations/st-pete.html">Concrete Services in St. Petersburg</a></li>
          <li><a href="/locations/westchase.html">Concrete Services in Westchase</a></li>
          <li><a href="/locations/south-tampa.html">Concrete Services in South Tampa</a></li>
          <li><a href="/locations/carrollwood.html">Concrete Services in Carrollwood</a></li>
          <li><a href="/locations/lutz.html">Concrete Services in Lutz</a></li>
          <li><a href="/">Tampa Concrete Pros — Main</a></li>
        </ul>
      </div>
    </section>

  </main>

  <footer style="background:#1a1a1a;color:#aaa;padding:24px 20px;text-align:center;font-size:0.9rem;">
    <p>&copy; 2026 <a href="/" style="color:#f97316;text-decoration:none;">Tampa Concrete Pros</a>. Serving {city}, Tampa, and surrounding Florida communities.</p>
    <p style="margin-top:8px;"><a href="tel:{PHONE_T}" style="color:#f97316;text-decoration:none;">{PHONE_D}</a> &nbsp;|&nbsp; <a href="/" style="color:#aaa;">Home</a> &nbsp;|&nbsp; <a href="/locations/" style="color:#aaa;">All Service Areas</a> &nbsp;|&nbsp; <a href="/privacy-policy.html" style="color:#aaa;">Privacy</a></p>
  </footer>

{float_cta}
</body>
</html>"""
    return page


# ─────────────────────────────────────────────────────────────────────────────
# ABOUT PAGE BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def build_about_page(existing_html):
    head = extract_head(existing_html)
    header_nav = extract_header_nav(existing_html)
    footer = extract_footer(existing_html)

    # Replace title and meta desc with updated copy
    head = head.replace(
        '<title>About Tampa Concrete Pros | Licensed Since 2012</title>',
        '<title>About Tampa Concrete Pros | Concrete Driveways &amp; Flatwork in Tampa Bay</title>'
    )
    head = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Tampa Concrete Pros specializes in concrete driveways and flatwork for Tampa Bay homeowners. Free written estimates, no fake license numbers, no surprises.">',
        head
    )

    main_content = f"""
    <main>

    <div class="breadcrumbs">
        <div class="breadcrumbs-container">
            <a href="/">Home</a>
            <span>&gt;</span>
            <span class="current">About Us</span>
        </div>
    </div>

    <section class="page-header">
        <h1>About Tampa Concrete Pros — Tampa Bay Concrete Driveways &amp; Flatwork Specialists</h1>
    </section>

    <section class="content-section" data-aos="fade-up">
        <p class="definition-text">Most Tampa homeowners dealing with a failing driveway or patio have had the same experience: a contractor shows up late, quotes low, then adds costs mid-job — or disappears entirely after the deposit. We built Tampa Concrete Pros around a simpler idea: give homeowners a written fixed-price quote before any work starts, do the base prep right the first time, and finish what we start. We're not the cheapest option in Florida. We're the option that shows up, does the base work correctly, and stands behind the result.</p>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">What We Do</h2>
        <p class="section-subtitle">We specialize in concrete driveways and flatwork — installation, replacement, patios, walkways, pool decks, and stamped decorative concrete — for homeowners and businesses throughout the Tampa Bay area. Every project gets the same foundation: proper base compaction, steel rebar reinforcement, and a finish that's built for Florida's wet-dry cycles.</p>
        <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.5rem;">
            <a href="/services/driveway-installation.html" style="background:var(--color-primary,#1a3a5c);color:white;padding:0.75rem 1.25rem;border-radius:6px;text-decoration:none;font-weight:600;">Driveway Installation</a>
            <a href="/services/driveway-replacement.html" style="background:var(--color-primary,#1a3a5c);color:white;padding:0.75rem 1.25rem;border-radius:6px;text-decoration:none;font-weight:600;">Driveway Replacement</a>
            <a href="/services/stamped-concrete.html" style="background:var(--color-primary,#1a3a5c);color:white;padding:0.75rem 1.25rem;border-radius:6px;text-decoration:none;font-weight:600;">Stamped Concrete</a>
            <a href="/services/patios-walkways.html" style="background:var(--color-primary,#1a3a5c);color:white;padding:0.75rem 1.25rem;border-radius:6px;text-decoration:none;font-weight:600;">Patios &amp; Walkways</a>
            <a href="/services/pool-decks.html" style="background:var(--color-primary,#1a3a5c);color:white;padding:0.75rem 1.25rem;border-radius:6px;text-decoration:none;font-weight:600;">Pool Decks</a>
        </div>
    </section>

    <section class="why-section">
        <h2 class="section-title split-text">What Makes Us Different</h2>
        <div class="why-grid">
            <div class="why-content">
                <p>Three things homeowners tell us matter most after working with us:</p>
                <ul class="feature-list">
                    <li>
                        {CHECK_SVG}
                        <span><strong>Written fixed-price quotes before any work starts.</strong> You see every line item — demo, base, reinforcement, pour, cleanup — before we pick up a tool. If we find something unexpected under the slab, we stop and show you before proceeding. The price we quoted is the price you pay.</span>
                    </li>
                    <li>
                        {CHECK_SVG}
                        <span><strong>We do the base prep that most contractors skip.</strong> Tampa's sandy soil is unforgiving. Base compaction and rebar reinforcement are what separate a slab that lasts 25 years from one that's cracking in 3. We don't skip the base work to win the bid.</span>
                    </li>
                    <li>
                        {CHECK_SVG}
                        <span><strong>We call back the same day.</strong> Most concrete contractors in Tampa take days to return calls, if they call back at all. We respond within 1 hour during business hours. Estimates are scheduled within 48 hours.</span>
                    </li>
                </ul>
            </div>
            <div class="why-image">
                <img src="/images/about-team.webp" alt="Tampa Concrete Pros crew at work" loading="lazy" decoding="async" width="800" height="533">
            </div>
        </div>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">Who We Serve</h2>
        <p class="section-subtitle">We serve homeowners and businesses across Tampa, Brandon, Clearwater, St. Petersburg, and the surrounding Hillsborough and Pinellas County communities. If you're within the Tampa Bay area and need concrete flatwork done right, call us — we'll tell you within 24 hours whether the project fits our schedule.</p>
        <div style="display:flex;gap:0.75rem;flex-wrap:wrap;margin-top:1.5rem;">
            <a href="/locations/south-tampa.html" style="background:white;padding:0.6rem 1rem;border-radius:6px;text-decoration:none;color:var(--color-primary,#1a3a5c);font-weight:500;box-shadow:0 2px 8px rgba(0,0,0,0.1);">South Tampa</a>
            <a href="/locations/brandon.html" style="background:white;padding:0.6rem 1rem;border-radius:6px;text-decoration:none;color:var(--color-primary,#1a3a5c);font-weight:500;box-shadow:0 2px 8px rgba(0,0,0,0.1);">Brandon</a>
            <a href="/locations/clearwater.html" style="background:white;padding:0.6rem 1rem;border-radius:6px;text-decoration:none;color:var(--color-primary,#1a3a5c);font-weight:500;box-shadow:0 2px 8px rgba(0,0,0,0.1);">Clearwater</a>
            <a href="/locations/st-pete.html" style="background:white;padding:0.6rem 1rem;border-radius:6px;text-decoration:none;color:var(--color-primary,#1a3a5c);font-weight:500;box-shadow:0 2px 8px rgba(0,0,0,0.1);">St. Petersburg</a>
            <a href="/locations/riverview.html" style="background:white;padding:0.6rem 1rem;border-radius:6px;text-decoration:none;color:var(--color-primary,#1a3a5c);font-weight:500;box-shadow:0 2px 8px rgba(0,0,0,0.1);">Riverview</a>
            <a href="/locations/westchase.html" style="background:white;padding:0.6rem 1rem;border-radius:6px;text-decoration:none;color:var(--color-primary,#1a3a5c);font-weight:500;box-shadow:0 2px 8px rgba(0,0,0,0.1);">Westchase</a>
        </div>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">Our Commitment</h2>
        <p class="definition-text">Every job gets a written quote before any work starts. If we find something we didn't expect — failed base, undermined subgrade, drainage issues — we stop and show you before any additional work proceeds. The price we quote is the price you pay. And if something doesn't meet our workmanship standard after the job is complete, we come back and fix it.</p>
    </section>

    <section class="cta-section" data-aos="fade-up">
        <h2>Ready to Get Started?</h2>
        <p>The estimate is free, comes in writing, and carries no obligation. Call us and we'll schedule a site visit within 48 hours.</p>
        <a href="tel:{PHONE_T}" class="btn btn-primary">
            {PHONE_SVG}
            Call {PHONE_D}
        </a>
    </section>

    </main>
"""

    page = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
{header_nav}
{main_content}
{footer}
    <!-- Main JavaScript -->
    <script src="/js/main.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/lenis@1/dist/lenis.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.js"></script>
    <script src="/js/animations.js"></script>
{FLOATING_CTA}
</body>
</html>"""
    return page


# ─────────────────────────────────────────────────────────────────────────────
# PRICING PAGE BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def build_pricing_page(existing_html):
    head = extract_head(existing_html)
    header_nav = extract_header_nav(existing_html)
    footer = extract_footer(existing_html)

    # Update meta
    head = head.replace(
        '<title>Concrete Pricing Tampa | Free Estimates &amp; Cost Guide</title>',
        '<title>Concrete Pricing in Tampa — Honest Numbers, No Surprises | Tampa Concrete Pros</title>'
    ).replace(
        '<title>Concrete Pricing Tampa | Free Estimates & Cost Guide</title>',
        '<title>Concrete Pricing in Tampa — Honest Numbers, No Surprises | Tampa Concrete Pros</title>'
    )
    head = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Concrete pricing guide for Tampa homeowners. Standard driveways $6–$10/sq ft, stamped $10–$18/sq ft, patios $5–$8/sq ft. Free written estimates. No surprises.">',
        head
    )

    main_content = f"""
    <main>

    <div class="breadcrumbs">
        <div class="breadcrumbs-container">
            <a href="/">Home</a>
            <span>&gt;</span>
            <span class="current">Pricing</span>
        </div>
    </div>

    <section class="page-header">
        <h1>Concrete Pricing in Tampa — Honest Numbers, No Surprises</h1>
    </section>

    <section class="content-section" data-aos="fade-up">
        <p class="definition-text">Most contractors hide pricing until the quote. We don't. Here's what concrete actually costs in Tampa, what drives the number up or down, and what's always included regardless of scope. The estimate is free and written — these ranges just help you come in with realistic expectations.</p>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">What Does Concrete Work Cost in Tampa?</h2>

        <div class="benefits-grid" style="grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin-top:1.5rem;">
            <div class="benefit-card">
                <h3>Concrete Driveway (Standard)</h3>
                <p style="font-size:1.5rem;font-weight:800;color:var(--color-accent,#1a3a5c);margin:0.5rem 0;">$6–$10/sq ft</p>
                <p>A standard two-car driveway (~600 sq ft) runs <strong>$3,600–$6,000</strong> including demo, base prep, rebar, and pour. This is the most common residential project. Sandy Florida soil requires careful base compaction — don't accept quotes that skip that line item.</p>
            </div>
            <div class="benefit-card">
                <h3>Stamped / Decorative Concrete</h3>
                <p style="font-size:1.5rem;font-weight:800;color:var(--color-accent,#1a3a5c);margin:0.5rem 0;">$10–$18/sq ft</p>
                <p>Covers base prep, pour, pattern stamping, integral color or color hardener, and UV-resistant sealer. A 400 sq ft patio in a single stamp pattern runs ~$4,000–$7,200. Multi-color custom designs with decorative borders land at the higher end.</p>
            </div>
            <div class="benefit-card">
                <h3>Concrete Patio</h3>
                <p style="font-size:1.5rem;font-weight:800;color:var(--color-accent,#1a3a5c);margin:0.5rem 0;">$5–$8/sq ft</p>
                <p>A 400 sq ft backyard patio typically falls between $2,000 and $3,200, including excavation, base, rebar, and pour. Drainage slope is built into every patio — it's not optional in Tampa's rain season.</p>
            </div>
            <div class="benefit-card">
                <h3>Concrete Removal &amp; Haul-Off</h3>
                <p style="font-size:1.5rem;font-weight:800;color:var(--color-accent,#1a3a5c);margin:0.5rem 0;">$1–$2/sq ft</p>
                <p>Breaking out and removing existing concrete. For a full driveway replacement, this adds $600–$1,200 to the project total. It's broken out as a separate line item in our quotes so you can see exactly where the cost sits.</p>
            </div>
            <div class="benefit-card">
                <h3>Pool Deck</h3>
                <p style="font-size:1.5rem;font-weight:800;color:var(--color-accent,#1a3a5c);margin:0.5rem 0;">$5–$8/sq ft</p>
                <p>Pool decks require non-slip finishes and sealer rated for chlorine and UV exposure — both are included. A 600 sq ft pool surround runs $3,000–$4,800 for a standard broom or exposed aggregate finish.</p>
            </div>
            <div class="benefit-card">
                <h3>Mudjacking / Slab Leveling</h3>
                <p style="font-size:1.5rem;font-weight:800;color:var(--color-accent,#1a3a5c);margin:0.5rem 0;">$500–$2,000</p>
                <p>Best for slabs with minor settling where the concrete itself is still structurally sound. We'll tell you during the estimate whether leveling or full replacement is the right call — mudjacking on a failed base is a short-term fix.</p>
            </div>
        </div>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">What Affects the Final Number</h2>
        <ul class="feature-list">
            <li>{CHECK_SVG}<span><strong>Square footage:</strong> Larger projects are more efficient per square foot but higher in total cost. We give you both numbers in the quote.</span></li>
            <li>{CHECK_SVG}<span><strong>Existing base condition:</strong> Tampa's sandy soil can be fine or can require significant correction. We assess the base before quoting — base correction costs are broken out separately.</span></li>
            <li>{CHECK_SVG}<span><strong>Finish type:</strong> Broom finish is the baseline. Smooth, exposed aggregate, stamped patterns, and custom colors each add to the cost. We review options and pricing during the estimate.</span></li>
            <li>{CHECK_SVG}<span><strong>Site access:</strong> Tight side yards, elevated grades, or access that requires hand-forming instead of machine work adds labor time.</span></li>
            <li>{CHECK_SVG}<span><strong>Demo scope:</strong> Full slab removal costs more than partial. Tree root issues or difficult demolition near existing structures adds to that line.</span></li>
        </ul>
    </section>

    <section class="content-section" data-aos="fade-up">
        <h2 class="section-title split-text">What Every Job Includes</h2>
        <ul class="feature-list">
            <li>{CHECK_SVG}<span>Written itemized quote before any work starts — every line broken out</span></li>
            <li>{CHECK_SVG}<span>Full base compaction with appropriate gravel depth for your soil conditions</span></li>
            <li>{CHECK_SVG}<span>Steel rebar reinforcement throughout — not just wire mesh</span></li>
            <li>{CHECK_SVG}<span>Control joints placed before the pour — not cut as an afterthought</span></li>
            <li>{CHECK_SVG}<span>Proper drainage slope built into every flat surface</span></li>
            <li>{CHECK_SVG}<span>Complete site cleanup and material haul-off after completion</span></li>
            <li>{CHECK_SVG}<span>Workmanship warranty — if something's wrong, we come back and fix it</span></li>
        </ul>
    </section>

    <section class="faq-section">
        <div class="faq-container">
            <h2 class="section-title split-text">Pricing Questions We Get All the Time</h2>

            <div class="faq-item">
                <div class="faq-question">
                    Do you charge for estimates?
                    {CHEVRON_SVG}
                </div>
                <div class="faq-answer">
                    <p>No. The estimate is free, comes with a written itemized quote, and carries no obligation. We schedule on-site visits within 48 hours of your call.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    Can I get a ballpark over the phone?
                    {CHEVRON_SVG}
                </div>
                <div class="faq-answer">
                    <p>For simple projects with known dimensions, we can give you a rough range over the phone. For anything requiring base assessment or site evaluation — which is most driveway replacements — we need to see the site first. The estimate is free, so there's no cost to getting accurate numbers.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    What if the price changes after you start?
                    {CHEVRON_SVG}
                </div>
                <div class="faq-answer">
                    <p>The price we quote is the price you pay. The only exception: if we find something genuinely hidden once the slab is broken up — collapsed drainage infrastructure, unexpected buried materials — we stop and show you before proceeding. You decide how to proceed. No surprise charges appear on the final invoice.</p>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    Do you offer financing?
                    {CHEVRON_SVG}
                </div>
                <div class="faq-answer">
                    <p>We don't offer in-house financing. Some customers have used home improvement financing options through their bank or credit union for larger projects. We can provide the written quote you'd need for that process.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section" data-aos="fade-up">
        <h2>Get Your Free, Written Concrete Estimate</h2>
        <p>The estimate is where the range becomes a real number for your specific project. We schedule on-site visits within 48 hours. The quote is written, itemized, and carries no obligation.</p>
        <a href="tel:{PHONE_T}" class="btn btn-primary">
            {PHONE_SVG}
            Call {PHONE_D}
        </a>
    </section>

    </main>
"""

    page = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
{header_nav}
{main_content}
{footer}
{FAQ_SCRIPT}
    <!-- Main JavaScript -->
    <script src="/js/main.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/lenis@1/dist/lenis.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.js"></script>
    <script src="/js/animations.js"></script>
{FLOATING_CTA}
</body>
</html>"""
    return page


# ─────────────────────────────────────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n=== Tampa Concrete Pros — PAS Rewrite ===\n")

    # ── SERVICE PAGES ──────────────────────────────────────────────────────────
    print("Service pages:")
    svc_dir = os.path.join(SITE, "services")
    # Use driveway-installation.html as the nav/footer template for all service pages
    template_svc = read_file(os.path.join(svc_dir, "driveway-installation.html"))
    svc_head_template = extract_head(template_svc)
    svc_nav = extract_header_nav(template_svc)
    svc_footer = extract_footer(template_svc)
    # Fix footer links for service pages (relative paths)
    svc_footer_svc = svc_footer  # already relative for services dir

    for slug, data in SERVICE_PAGES.items():
        # Get the existing head for this specific page (preserves per-page schema)
        existing = read_file(os.path.join(svc_dir, f"{slug}.html"))
        page_head = extract_head(existing)
        page_nav = extract_header_nav(existing)
        page_footer = extract_footer(existing)
        content = build_service_page(slug, data, page_head, page_nav, page_footer, "")
        write_file(os.path.join(svc_dir, f"{slug}.html"), content)

    # ── LOCATION PAGES ─────────────────────────────────────────────────────────
    print("\nLocation pages:")
    loc_dir = os.path.join(SITE, "locations")
    for slug, data in LOCATION_DATA.items():
        path = os.path.join(loc_dir, f"{slug}.html")
        existing = read_file(path)
        existing_head = extract_head(existing)
        content = build_location_page(slug, data, existing_head)
        write_file(path, content)

    # ── ABOUT PAGE ─────────────────────────────────────────────────────────────
    print("\nAbout + Pricing pages:")
    about_path = os.path.join(SITE, "about.html")
    about_html = read_file(about_path)
    write_file(about_path, build_about_page(about_html))

    # ── PRICING PAGE ───────────────────────────────────────────────────────────
    pricing_path = os.path.join(SITE, "pricing.html")
    pricing_html = read_file(pricing_path)
    write_file(pricing_path, build_pricing_page(pricing_html))

    print("\n✅ All pages written.\n")


if __name__ == "__main__":
    main()
