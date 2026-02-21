#!/usr/bin/env python3
"""Inject CDN links and animation attributes into all HTML pages."""
import os, glob, re

SITE_DIR = "/Users/costa.demetral/Desktop/Tampa Concrete Pros"

CDN_CSS = """    <!-- Animation Libraries CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/splitting/dist/splitting.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/splitting/dist/splitting-cells.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.css">
    <link rel="stylesheet" href="https://unpkg.com/lenis@1/dist/lenis.css">"""

CDN_JS = """    <!-- Animation Libraries -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/lenis@1/dist/lenis.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.16/dist/typed.umd.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vanilla-tilt@1/dist/vanilla-tilt.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/splitting/dist/splitting.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.js"></script>
    <script src="/js/animations.js"></script>"""

# Patterns to skip
SKIP_DIRS = ['design-resources', 'skills_extracted', 'skills_extracted_2', 'node_modules']

def should_skip(path):
    for d in SKIP_DIRS:
        if d in path:
            return True
    return False

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if not content.strip().startswith('<!DOCTYPE') and not content.strip().startswith('<html'):
        return False
    
    modified = False
    
    # Add CDN CSS before </head>
    if 'swiper-bundle.min.css' not in content and '</head>' in content:
        content = content.replace('</head>', CDN_CSS + '\n</head>', 1)
        modified = True
    
    # Add CDN JS before </body>
    if 'animations.js' not in content and '</body>' in content:
        content = content.replace('</body>', CDN_JS + '\n</body>', 1)
        modified = True
    
    # Add data-aos to sections
    for cls in ['services-preview', 'why-us', 'testimonials', 'locations', 'cta-section', 'content-section']:
        old = f'class="{cls}"'
        new = f'class="{cls}" data-aos="fade-up"'
        if old in content and 'data-aos' not in content.split(old)[0].split('\n')[-1] + old:
            content = content.replace(old, new)
            modified = True
    
    # Add split-text to section-title
    if 'class="section-title"' in content and 'split-text' not in content:
        content = content.replace('class="section-title"', 'class="section-title split-text"')
        modified = True
    
    # Add data-tilt to service-card
    if 'class="service-card"' in content:
        content = content.replace('class="service-card"', 'class="service-card" data-tilt')
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Find all HTML files
count = 0
for root, dirs, files in os.walk(SITE_DIR):
    if should_skip(root):
        continue
    for fname in files:
        if fname.endswith('.html'):
            filepath = os.path.join(root, fname)
            if process_file(filepath):
                count += 1
                print(f"  Updated: {os.path.relpath(filepath, SITE_DIR)}")
            else:
                print(f"  Skipped: {os.path.relpath(filepath, SITE_DIR)}")

print(f"\nDone! Updated {count} files.")
