document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
        
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navMenu.contains(event.target);
            const isClickOnToggle = menuToggle.contains(event.target);
            
            if (!isClickInsideNav && !isClickOnToggle && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                menuToggle.classList.remove('active');
            }
        });
    }
    
    const navbar = document.querySelector('.navbar');
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        lastScrollY = window.scrollY;
    });
    
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link:not(.btn-primary)');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.color = 'var(--color-text)';
            link.querySelector('::after') && (link.style.setProperty('--after-width', '100%'));
        }
    });
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };
    
    const fadeInObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry, index) {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
                fadeInObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    const animatedCards = document.querySelectorAll('.value-card, .about-card, .product-card, .testimonial-card, .hero-card, .commitment-item');
    animatedCards.forEach(function(el, index) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(40px)';
        el.style.transition = 'opacity 0.7s cubic-bezier(0.4, 0, 0.2, 1), transform 0.7s cubic-bezier(0.4, 0, 0.2, 1)';
        el.style.transitionDelay = (index % 4) * 0.1 + 's';
        fadeInObserver.observe(el);
    });
    
    const sectionObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                sectionObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    const animatedSections = document.querySelectorAll('.section-header, .about-intro, .newsletter-content, .about-cta, .about-story, .artisan-image-card');
    animatedSections.forEach(function(el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
        sectionObserver.observe(el);
    });
    
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const input = this.querySelector('.newsletter-input');
            const btn = this.querySelector('.newsletter-btn');
            const originalText = btn.textContent;
            
            btn.textContent = 'Merci !';
            btn.style.background = 'var(--color-primary)';
            btn.style.color = 'white';
            input.value = '';
            
            setTimeout(function() {
                btn.textContent = originalText;
                btn.style.background = '';
                btn.style.color = '';
            }, 3000);
        });
    }
    
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    const images = document.querySelectorAll('.hero-bg-image, .hero-card-image, .artisan-img, .product-image img');
    images.forEach(function(img) {
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.6s ease';
        
        img.addEventListener('load', function() {
            this.style.opacity = '1';
        });
        
        if (img.complete) {
            img.style.opacity = '1';
        }
    });
    
    
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});
