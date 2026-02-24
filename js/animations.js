/**
 * Tampa Concrete Pros - Premium Animation Controller
 * Central animation system using GSAP, Lenis, Typed.js, Swiper, GLightbox, etc.
 */

(function () {
  'use strict';

  // ==========================================================================
  // 1. Lenis Smooth Scroll
  // ==========================================================================
  let lenis;
  function initLenis() {
    if (typeof Lenis === 'undefined') return;
    lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      direction: 'vertical',
      gestureDirection: 'vertical',
      smooth: true,
      smoothTouch: false,
      touchMultiplier: 2,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // Connect Lenis to GSAP ScrollTrigger
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time) => {
        lenis.raf(time * 1000);
      });
      gsap.ticker.lagSmoothing(0);
    }
  }

  // ==========================================================================
  // 2. GSAP + ScrollTrigger Section Reveals
  // ==========================================================================
  function initGSAP() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    // Fade-up sections (GSAP-class-only — AOS handles [data-aos] elements separately)
    gsap.utils.toArray('.gsap-fade-up').forEach((el) => {
      gsap.from(el, {
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          end: 'top 50%',
          toggleActions: 'play none none none',
        },
        y: 60,
        opacity: 0,
        duration: 1,
        ease: 'power3.out',
      });
    });

    // Fade-in-left (GSAP-class-only)
    gsap.utils.toArray('.gsap-fade-right').forEach((el) => {
      gsap.from(el, {
        scrollTrigger: { trigger: el, start: 'top 85%' },
        x: -80,
        opacity: 0,
        duration: 1,
        ease: 'power3.out',
      });
    });

    // Fade-in-right (GSAP-class-only)
    gsap.utils.toArray('.gsap-fade-left').forEach((el) => {
      gsap.from(el, {
        scrollTrigger: { trigger: el, start: 'top 85%' },
        x: 80,
        opacity: 0,
        duration: 1,
        ease: 'power3.out',
      });
    });

    // Scale-up cards
    gsap.utils.toArray('.service-card, .location-card').forEach((card, i) => {
      gsap.from(card, {
        scrollTrigger: { trigger: card, start: 'top 90%' },
        y: 40,
        opacity: 0,
        duration: 0.8,
        delay: i * 0.1,
        ease: 'power2.out',
      });
    });

    // Hero parallax
    const hero = document.querySelector('.hero');
    if (hero) {
      gsap.to('.hero', {
        scrollTrigger: {
          trigger: '.hero',
          start: 'top top',
          end: 'bottom top',
          scrub: true,
        },
        backgroundPositionY: '50%',
        ease: 'none',
      });
    }

    // Stagger grid children
    gsap.utils.toArray('.services-grid, .locations-grid, .testimonials-grid, .gallery-grid').forEach((grid) => {
      const children = grid.children;
      if (children.length) {
        gsap.from(children, {
          scrollTrigger: { trigger: grid, start: 'top 85%' },
          y: 50,
          opacity: 0,
          duration: 0.7,
          stagger: 0.12,
          ease: 'power2.out',
        });
      }
    });

    // CTA section reveal
    gsap.utils.toArray('.cta-section').forEach((cta) => {
      gsap.from(cta.children, {
        scrollTrigger: { trigger: cta, start: 'top 80%' },
        y: 30,
        opacity: 0,
        duration: 0.8,
        stagger: 0.15,
        ease: 'power2.out',
      });
    });
  }

  // ==========================================================================
  // 3. Typed.js Hero Text
  // ==========================================================================
  function initTyped() {
    if (typeof Typed === 'undefined') return;
    const el = document.querySelector('.typed-text');
    if (!el) return;

    new Typed('.typed-text', {
      strings: ['Driveways', 'Patios', 'Pool Decks', 'Stamped Concrete', 'Walkways', 'Commercial Slabs'],
      typeSpeed: 60,
      backSpeed: 40,
      backDelay: 2000,
      startDelay: 500,
      loop: true,
      showCursor: true,
      cursorChar: '|',
    });
  }

  // ==========================================================================
  // 4. Swiper - Testimonials & Gallery
  // ==========================================================================
  function initSwiper() {
    if (typeof Swiper === 'undefined') return;

    // Testimonials Swiper
    const testimonialsEl = document.querySelector('.testimonials-swiper');
    if (testimonialsEl) {
      new Swiper('.testimonials-swiper', {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        autoplay: { delay: 5000, disableOnInteraction: false },
        pagination: { el: '.swiper-pagination', clickable: true },
        navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
        breakpoints: {
          640: { slidesPerView: 2 },
          1024: { slidesPerView: 3 },
        },
      });
    }

    // Gallery Swiper
    const galleryEl = document.querySelector('.gallery-swiper');
    if (galleryEl) {
      new Swiper('.gallery-swiper', {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        autoplay: { delay: 4000, disableOnInteraction: false },
        pagination: { el: '.gallery-pagination', clickable: true },
        breakpoints: {
          480: { slidesPerView: 2 },
          768: { slidesPerView: 3 },
          1024: { slidesPerView: 4 },
        },
      });
    }
  }

  // ==========================================================================
  // 5. GLightbox - Gallery & Portfolio
  // ==========================================================================
  function initGLightbox() {
    if (typeof GLightbox === 'undefined') return;
    GLightbox({
      selector: '.glightbox',
      touchNavigation: true,
      loop: true,
      autoplayVideos: true,
      openEffect: 'zoom',
      closeEffect: 'fade',
    });
  }

  // ==========================================================================
  // 6. Vanilla Tilt on Service Cards
  // ==========================================================================
  function initTilt() {
    if (typeof VanillaTilt === 'undefined') return;
    // Disable tilt on touch/mobile devices
    if (window.matchMedia('(pointer: coarse)').matches || window.innerWidth <= 768) return;
    const tiltElements = document.querySelectorAll('[data-tilt]');
    if (!tiltElements.length) return;

    VanillaTilt.init(tiltElements, {
      max: 8,
      speed: 400,
      glare: true,
      'max-glare': 0.15,
      scale: 1.02,
    });
  }

  // ==========================================================================
  // 7. Animated Counters
  // ==========================================================================
  function initCounters() {
    const counters = document.querySelectorAll('.counter');
    if (!counters.length) return;

    const animateCounter = (el) => {
      const target = parseInt(el.getAttribute('data-target'), 10);
      const suffix = el.getAttribute('data-suffix') || '';
      const prefix = el.getAttribute('data-prefix') || '';
      const duration = 2000;
      const start = 0;
      const startTime = performance.now();

      function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Ease out cubic
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(eased * (target - start) + start);
        el.textContent = prefix + current.toLocaleString() + suffix;
        if (progress < 1) requestAnimationFrame(update);
      }
      requestAnimationFrame(update);
    };

    if (typeof IntersectionObserver !== 'undefined') {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              animateCounter(entry.target);
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.5 }
      );
      counters.forEach((c) => observer.observe(c));
    } else {
      counters.forEach(animateCounter);
    }
  }

  // ==========================================================================
  // 8. Before/After Interactive Slider
  // ==========================================================================
  function initBeforeAfter() {
    const sliders = document.querySelectorAll('.ba-slider');
    if (!sliders.length) return;

    sliders.forEach((slider) => {
      const handle = slider.querySelector('.ba-handle');
      const before = slider.querySelector('.ba-before');
      if (!handle || !before) return;

      let isDragging = false;

      function setPosition(x) {
        const rect = slider.getBoundingClientRect();
        let pos = ((x - rect.left) / rect.width) * 100;
        pos = Math.max(0, Math.min(100, pos));
        before.style.clipPath = `inset(0 ${100 - pos}% 0 0)`;
        handle.style.left = pos + '%';
      }

      // Mouse events
      handle.addEventListener('mousedown', (e) => { isDragging = true; e.preventDefault(); });
      window.addEventListener('mouseup', () => (isDragging = false));
      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        setPosition(e.clientX);
      });

      // Touch events with full touch support
      handle.addEventListener('touchstart', (e) => {
        isDragging = true;
        e.preventDefault(); // prevent scroll while dragging
      }, { passive: false });
      window.addEventListener('touchend', () => (isDragging = false));
      window.addEventListener('touchcancel', () => (isDragging = false));
      window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        e.preventDefault();
        setPosition(e.touches[0].clientX);
      }, { passive: false });

      // Also allow tap-to-position on the slider itself
      slider.addEventListener('click', (e) => {
        setPosition(e.clientX);
      });
      slider.addEventListener('touchstart', (e) => {
        if (e.target === handle || handle.contains(e.target)) return;
        setPosition(e.touches[0].clientX);
      }, { passive: true });

      // Set initial
      setPosition(slider.getBoundingClientRect().left + slider.getBoundingClientRect().width / 2);
    });
  }

  // ==========================================================================
  // 9. Splitting.js on Section Headings
  // ==========================================================================
  function initSplitting() {
    if (typeof Splitting === 'undefined') return;
    Splitting({ target: '.split-text', by: 'chars' });

    // Animate split chars on scroll
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      document.querySelectorAll('.split-text').forEach((heading) => {
        const chars = heading.querySelectorAll('.char');
        if (!chars.length) return;
        gsap.from(chars, {
          scrollTrigger: { trigger: heading, start: 'top 85%' },
          y: 30,
          opacity: 0,
          duration: 0.5,
          stagger: 0.03,
          ease: 'power2.out',
        });
      });
    }
  }

  // ==========================================================================
  // 10. AOS Fallback
  // ==========================================================================
  function initAOS() {
    if (typeof AOS === 'undefined') return;
    AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 80,
      disable: false,
    });
  }

  // ==========================================================================
  // 11. Magnetic Button Hover Effects
  // ==========================================================================
  function initMagneticButtons() {
    const buttons = document.querySelectorAll('.btn-magnetic, .btn-primary, .btn-secondary');
    if (!buttons.length) return;

    buttons.forEach((btn) => {
      btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
      });

      btn.addEventListener('mouseleave', () => {
        btn.style.transform = 'translate(0, 0)';
        btn.style.transition = 'transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
      });

      btn.addEventListener('mouseenter', () => {
        btn.style.transition = 'transform 0.15s ease-out';
      });
    });
  }

  // ==========================================================================
  // 12. Navbar Scroll Effect + Mobile Menu
  // ==========================================================================
  function initNavScroll() {
    const header = document.querySelector('header');
    if (!header) return;

    let lastScroll = 0;
    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;
      if (currentScroll > 100) {
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
      }

      if (currentScroll > lastScroll && currentScroll > 400) {
        header.classList.add('header-hidden');
      } else {
        header.classList.remove('header-hidden');
      }
      lastScroll = currentScroll;
    });

    // Mobile hamburger menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (menuToggle && navLinks) {
      menuToggle.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('active');
        menuToggle.setAttribute('aria-expanded', isOpen);
        // Toggle hamburger/close icon
        if (isOpen) {
          menuToggle.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';
        } else {
          menuToggle.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
        }
      });

      // Mobile dropdown toggle on touch
      document.querySelectorAll('.dropdown > a').forEach((dropdownToggle) => {
        dropdownToggle.addEventListener('click', (e) => {
          if (window.innerWidth <= 768) {
            e.preventDefault();
            const parent = dropdownToggle.parentElement;
            // Close other open dropdowns
            document.querySelectorAll('.dropdown.active').forEach((d) => {
              if (d !== parent) d.classList.remove('active');
            });
            parent.classList.toggle('active');
          }
        });
      });

      // Close menu when clicking outside
      document.addEventListener('click', (e) => {
        if (window.innerWidth <= 768 && !header.contains(e.target)) {
          navLinks.classList.remove('active');
          menuToggle.setAttribute('aria-expanded', 'false');
          menuToggle.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
        }
      });
    }
  }

  // ==========================================================================
  // 13. Image Lazy Load with Blur-up
  // ==========================================================================
  function initLazyImages() {
    const images = document.querySelectorAll('img[data-src]');
    if (!images.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          img.classList.add('loaded');
          observer.unobserve(img);
        }
      });
    });
    images.forEach((img) => observer.observe(img));
  }

  // ==========================================================================
  // 14. Preloader
  // ==========================================================================
  function initPreloader() {
    const preloader = document.querySelector('.preloader');
    if (!preloader) return;

    window.addEventListener('load', () => {
      preloader.classList.add('preloader-done');
      setTimeout(() => preloader.remove(), 600);
    });
  }

  // ==========================================================================
  // INIT ALL
  // ==========================================================================
  function init() {
    initPreloader();
    initLenis();
    initGSAP();
    initTyped();
    initSwiper();
    initGLightbox();
    initTilt();
    initCounters();
    initBeforeAfter();
    initSplitting();
    initAOS();
    initMagneticButtons();
    initNavScroll();
    initLazyImages();
  }

  // Run on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
