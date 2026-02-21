/**
 * Tampa Concrete Pros - Main JavaScript
 * Version: 2.0
 */

(function() {
    'use strict';

    // ==========================================================================
    // 1. Mobile Menu Toggle
    // ==========================================================================
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const dropdowns = document.querySelectorAll('.dropdown');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            // Toggle aria-expanded for accessibility
            const isExpanded = navLinks.classList.contains('active');
            menuToggle.setAttribute('aria-expanded', isExpanded);
        });

        // Handle dropdown clicks on mobile
        dropdowns.forEach(dropdown => {
            const link = dropdown.querySelector('a');
            if (link) {
                link.addEventListener('click', function(e) {
                    if (window.innerWidth <= 768) {
                        e.preventDefault();
                        dropdown.classList.toggle('active');
                    }
                });
            }
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!menuToggle.contains(e.target) && !navLinks.contains(e.target)) {
                navLinks.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // ==========================================================================
    // 2. Smooth Scroll for Anchor Links
    // ==========================================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ==========================================================================
    // 3. Back to Top Button
    // ==========================================================================
    function createBackToTopButton() {
        // Check if button already exists
        if (document.querySelector('.back-to-top')) return;

        const button = document.createElement('button');
        button.className = 'back-to-top';
        button.setAttribute('aria-label', 'Back to top');
        button.innerHTML = `
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
        `;
        document.body.appendChild(button);

        // Show/hide based on scroll position
        function toggleBackToTop() {
            if (window.scrollY > 500) {
                button.classList.add('visible');
            } else {
                button.classList.remove('visible');
            }
        }

        window.addEventListener('scroll', throttle(toggleBackToTop, 100));
        toggleBackToTop(); // Initial check

        // Scroll to top on click
        button.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ==========================================================================
    // 4. Header Scroll Behavior
    // ==========================================================================
    function initHeaderScroll() {
        const header = document.querySelector('header');
        if (!header) return;

        let lastScrollY = window.scrollY;
        let ticking = false;

        function updateHeader() {
            const currentScrollY = window.scrollY;

            // Add scrolled class for shadow
            if (currentScrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }

            // Hide/show header on scroll (optional - uncomment if desired)
            // if (currentScrollY > lastScrollY && currentScrollY > 200) {
            //     header.classList.add('hidden');
            // } else {
            //     header.classList.remove('hidden');
            // }

            lastScrollY = currentScrollY;
            ticking = false;
        }

        window.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateHeader);
                ticking = true;
            }
        });
    }

    // ==========================================================================
    // 5. Scroll-Triggered Animations
    // ==========================================================================
    function initScrollAnimations() {
        const animatedElements = document.querySelectorAll('.animate-on-scroll');
        if (animatedElements.length === 0) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -100px 0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        animatedElements.forEach(el => observer.observe(el));
    }

    // ==========================================================================
    // 6. Auto-add Animation Classes to Elements
    // ==========================================================================
    function addAnimationClasses() {
        // Add animation classes to service cards
        document.querySelectorAll('.service-card').forEach((card, index) => {
            if (!card.classList.contains('animate-on-scroll')) {
                card.classList.add('animate-on-scroll');
                if (index % 3 === 1) card.classList.add('delay-1');
                if (index % 3 === 2) card.classList.add('delay-2');
            }
        });

        // Add animation classes to testimonial cards
        document.querySelectorAll('.testimonial-card').forEach((card, index) => {
            if (!card.classList.contains('animate-on-scroll')) {
                card.classList.add('animate-on-scroll');
                if (index % 3 === 1) card.classList.add('delay-1');
                if (index % 3 === 2) card.classList.add('delay-2');
            }
        });

        // Add animation classes to location cards
        document.querySelectorAll('.location-card').forEach((card, index) => {
            if (!card.classList.contains('animate-on-scroll')) {
                card.classList.add('animate-on-scroll');
                card.classList.add('delay-' + (index % 4 + 1));
            }
        });

        // Add animation to section titles
        document.querySelectorAll('.section-title').forEach(title => {
            if (!title.classList.contains('animate-on-scroll')) {
                title.classList.add('animate-on-scroll');
            }
        });
    }

    // ==========================================================================
    // 7. Form Enhancements
    // ==========================================================================
    function initFormEnhancements() {
        const forms = document.querySelectorAll('form');

        forms.forEach(form => {
            // Add floating labels effect
            const inputs = form.querySelectorAll('.form-input, .form-textarea');
            inputs.forEach(input => {
                input.addEventListener('focus', function() {
                    this.parentElement.classList.add('focused');
                });
                input.addEventListener('blur', function() {
                    if (!this.value) {
                        this.parentElement.classList.remove('focused');
                    }
                });
            });

            // Form validation feedback
            form.addEventListener('submit', function(e) {
                const requiredFields = form.querySelectorAll('[required]');
                let isValid = true;

                requiredFields.forEach(field => {
                    if (!field.value.trim()) {
                        isValid = false;
                        field.classList.add('error');
                    } else {
                        field.classList.remove('error');
                    }
                });

                if (!isValid) {
                    e.preventDefault();
                }
            });
        });
    }

    // ==========================================================================
    // 8. Lazy Loading Images (fallback for older browsers)
    // ==========================================================================
    function initLazyLoading() {
        if ('loading' in HTMLImageElement.prototype) {
            // Browser supports native lazy loading
            document.querySelectorAll('img[loading="lazy"]').forEach(img => {
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                }
            });
        } else {
            // Fallback for older browsers
            const lazyImages = document.querySelectorAll('img[loading="lazy"]');
            if (lazyImages.length === 0) return;

            const imageObserver = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                        }
                        img.classList.add('loaded');
                        imageObserver.unobserve(img);
                    }
                });
            });

            lazyImages.forEach(img => imageObserver.observe(img));
        }
    }

    // ==========================================================================
    // 9. Phone Number Click Tracking
    // ==========================================================================
    function initPhoneTracking() {
        document.querySelectorAll('a[href^="tel:"]').forEach(link => {
            link.addEventListener('click', function() {
                // Track phone calls if analytics is available
                if (typeof gtag === 'function') {
                    gtag('event', 'click', {
                        'event_category': 'Phone',
                        'event_label': this.href.replace('tel:', '')
                    });
                }
            });
        });
    }

    // ==========================================================================
    // 10. Active Navigation Highlighting
    // ==========================================================================
    function highlightActiveNav() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-links a');

        navLinks.forEach(link => {
            const linkPath = link.getAttribute('href');
            if (linkPath === currentPath ||
                (currentPath.includes(linkPath) && linkPath !== '/')) {
                link.classList.add('active');
            }
        });
    }

    // ==========================================================================
    // Utility Functions
    // ==========================================================================
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    function debounce(func, wait) {
        let timeout;
        return function() {
            const context = this;
            const args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(context, args), wait);
        };
    }

    // ==========================================================================
    // 11. Mobile Sticky CTA Bar
    // ==========================================================================
    function createMobileCTABar() {
        // Check if bar already exists
        if (document.querySelector('.mobile-cta-bar')) return;

        const bar = document.createElement('div');
        bar.className = 'mobile-cta-bar';
        bar.innerHTML = `
            <div class="mobile-cta-bar-content">
                <a href="tel:8135552847" class="mobile-cta-call">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/>
                    </svg>
                    Call Now
                </a>
                <a href="/contact.html" class="mobile-cta-quote">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>
                    </svg>
                    Free Quote
                </a>
            </div>
        `;
        document.body.appendChild(bar);
    }

    // ==========================================================================
    // Initialize Everything
    // ==========================================================================
    function init() {
        createBackToTopButton();
        createMobileCTABar();
        initHeaderScroll();
        addAnimationClasses();
        initScrollAnimations();
        initFormEnhancements();
        initLazyLoading();
        initPhoneTracking();
        highlightActiveNav();
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();