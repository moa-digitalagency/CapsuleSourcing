document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    const navOverlay = document.getElementById('navOverlay');
    const body = document.body;
    
    function closeMenu() {
        navMenu.classList.remove('active');
        menuToggle.classList.remove('active');
        navOverlay.classList.remove('active');
        body.classList.remove('menu-open');
    }
    
    function openMenu() {
        navMenu.classList.add('active');
        menuToggle.classList.add('active');
        navOverlay.classList.add('active');
        body.classList.add('menu-open');
    }
    
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            if (navMenu.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });
        
        if (navOverlay) {
            navOverlay.addEventListener('click', closeMenu);
        }
        
        const navLinks = navMenu.querySelectorAll('a:not(.nav-link-dropdown)');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 968) {
                    closeMenu();
                }
            });
        });
        
        const dropdowns = document.querySelectorAll('.nav-dropdown');
        dropdowns.forEach(function(dropdown) {
            const dropdownToggle = dropdown.querySelector('.nav-link-dropdown');
            if (dropdownToggle) {
                dropdownToggle.addEventListener('click', function(e) {
                    e.preventDefault();
                    if (window.innerWidth <= 968) {
                        dropdown.classList.toggle('open');
                    }
                });
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
    
    window.addEventListener('resize', function() {
        if (window.innerWidth > 968) {
            closeMenu();
            document.querySelectorAll('.nav-dropdown.open').forEach(function(d) {
                d.classList.remove('open');
            });
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
