document.addEventListener('DOMContentLoaded', () => {
  // --- Language Toggle System with LocalStorage ---
  const langToggleBtn = document.getElementById('lang-toggle');
  const langToggleBtnMobile = document.getElementById('lang-toggle-mobile');
  
  function setLanguage(lang) {
    document.documentElement.setAttribute('lang', lang);
    localStorage.setItem('ecoshield_lang', lang);
    if (lang === 'ar') {
      document.documentElement.setAttribute('dir', 'rtl');
      if (langToggleBtn) langToggleBtn.innerText = 'English';
      if (langToggleBtnMobile) langToggleBtnMobile.innerText = 'English';
    } else {
      document.documentElement.setAttribute('dir', 'ltr');
      if (langToggleBtn) langToggleBtn.innerText = 'العربية';
      if (langToggleBtnMobile) langToggleBtnMobile.innerText = 'العربية';
    }
    // Dispatch resize to trigger animations
    window.dispatchEvent(new Event('resize'));
  }

  // Initial Toggle Hook
  const toggleHandler = (e) => {
    e.preventDefault();
    const currentLang = document.documentElement.getAttribute('lang') || 'ar';
    const nextLang = currentLang === 'ar' ? 'en' : 'ar';
    setLanguage(nextLang);
  };

  if (langToggleBtn) langToggleBtn.addEventListener('click', toggleHandler);
  if (langToggleBtnMobile) langToggleBtnMobile.addEventListener('click', toggleHandler);

  // Set initial language from localStorage or default to Arabic
  const savedLang = localStorage.getItem('ecoshield_lang') || 'ar';
  setLanguage(savedLang);

  // --- Mobile Menu Toggle ---
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
      mobileMenu.classList.toggle('flex');
    });

    // Close menu when clicking on a link
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
        mobileMenu.classList.remove('flex');
      });
    });
  }

  // --- Sticky Navbar Scroll Effect ---
  const header = document.getElementById('main-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.remove('py-5', 'bg-transparent');
      header.classList.add('py-3', 'shadow-md', 'glass-nav');
    } else {
      header.classList.remove('py-3', 'shadow-md', 'glass-nav');
      header.classList.add('py-5', 'bg-transparent');
    }
  });

  // --- Before & After Slider Logic ---
  const sliderInput = document.getElementById('slider-range');
  const imgAfter = document.getElementById('after-image');
  const sliderButton = document.getElementById('slider-bar');

  if (sliderInput && imgAfter && sliderButton) {
    function updateSlider(value) {
      // Calculate percentage
      const percentage = value + '%';
      
      // In RTL layouts, check if we need to flip the clip direction
      const isRTL = document.documentElement.getAttribute('dir') === 'rtl';
      
      if (isRTL) {
        // Clip from right to left in RTL
        const clipVal = (100 - value) + '%';
        imgAfter.style.clipPath = `polygon(0 0, ${value}% 0, ${value}% 100%, 0 100%)`;
        sliderButton.style.left = percentage;
      } else {
        // Clip from left to right in LTR
        imgAfter.style.clipPath = `polygon(0 0, ${value}% 0, ${value}% 100%, 0 100%)`;
        sliderButton.style.left = percentage;
      }
    }

    sliderInput.addEventListener('input', (e) => {
      updateSlider(e.target.value);
    });

    // Initialize slider at 50%
    updateSlider(50);
  }

  // --- Count-Up Statistics Animation ---
  const counters = document.querySelectorAll('.stat-number');
  const countSpeed = 200; // The lower the slower

  const runCounter = (counter) => {
    const target = parseInt(counter.getAttribute('data-target'), 10);
    let count = 0;
    const increment = Math.ceil(target / countSpeed);

    const updateCount = () => {
      count += increment;
      if (count < target) {
        counter.innerText = count.toLocaleString();
        setTimeout(updateCount, 15);
      } else {
        counter.innerText = target.toLocaleString();
      }
    };
    updateCount();
  };

  // Intersection Observer for Statistics Counters
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        runCounter(counter);
        observer.unobserve(counter);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => {
    counterObserver.observe(counter);
  });

  // --- Customer Testimonials Carousel ---
  const track = document.getElementById('testimonial-track');
  const slides = document.querySelectorAll('.testimonial-slide');
  const prevBtn = document.getElementById('testimonial-prev');
  const nextBtn = document.getElementById('testimonial-next');
  let currentSlideIndex = 0;

  if (track && slides.length > 0) {
    function getSlideWidth() {
      return slides[0].getBoundingClientRect().width;
    }

    function moveSlides() {
      const slideWidth = getSlideWidth();
      const isRTL = document.documentElement.getAttribute('dir') === 'rtl';
      
      // Calculate standard translate direction
      let transformValue;
      if (isRTL) {
        // In RTL, sliding right to left is positive translation
        transformValue = currentSlideIndex * slideWidth;
      } else {
        // In LTR, sliding left to right is negative translation
        transformValue = -currentSlideIndex * slideWidth;
      }
      
      track.style.transform = `translateX(${transformValue}px)`;
    }

    nextBtn.addEventListener('click', () => {
      if (currentSlideIndex < slides.length - 1) {
        currentSlideIndex++;
      } else {
        currentSlideIndex = 0; // Loop back
      }
      moveSlides();
    });

    prevBtn.addEventListener('click', () => {
      if (currentSlideIndex > 0) {
        currentSlideIndex--;
      } else {
        currentSlideIndex = slides.length - 1; // Loop to end
      }
      moveSlides();
    });

    // Handle resize
    window.addEventListener('resize', moveSlides);
    
    // Auto-play Testimonial Carousel
    let autoSlideInterval = setInterval(() => {
      nextBtn.click();
    }, 6000);

    // Stop auto-play on hover/interaction
    const carouselContainer = document.getElementById('testimonial-carousel');
    if (carouselContainer) {
      carouselContainer.addEventListener('mouseenter', () => clearInterval(autoSlideInterval));
      carouselContainer.addEventListener('mouseleave', () => {
        autoSlideInterval = setInterval(() => {
          nextBtn.click();
        }, 6000);
      });
    }
  }

  // --- FAQ Accordion System ---
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answerPanel = item.querySelector('.faq-answer');
    const icon = item.querySelector('.faq-icon');

    questionBtn.addEventListener('click', () => {
      const isExpanded = questionBtn.getAttribute('aria-expanded') === 'true';
      
      // Close all other FAQs
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          const otherBtn = otherItem.querySelector('.faq-question');
          const otherAnswer = otherItem.querySelector('.faq-answer');
          const otherIcon = otherItem.querySelector('.faq-icon');
          
          otherBtn.setAttribute('aria-expanded', 'false');
          otherAnswer.style.maxHeight = '0px';
          otherIcon.style.transform = 'rotate(0deg)';
        }
      });

      // Toggle current FAQ
      if (isExpanded) {
        questionBtn.setAttribute('aria-expanded', 'false');
        answerPanel.style.maxHeight = '0px';
        icon.style.transform = 'rotate(0deg)';
      } else {
        questionBtn.setAttribute('aria-expanded', 'true');
        answerPanel.style.maxHeight = answerPanel.scrollHeight + 'px';
        icon.style.transform = 'rotate(180deg)';
      }
    });
  });

  // --- Scroll-Driven Reveal Animations ---
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Optionally unobserve after animating once
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });

  // --- Premium Contact Form Validation ---
  const contactForm = document.getElementById('pest-contact-form');
  const formSuccess = document.getElementById('form-success-alert');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Simple validation
      const nameInput = contactForm.querySelector('[name="name"]');
      const emailInput = contactForm.querySelector('[name="email"]');
      const phoneInput = contactForm.querySelector('[name="phone"]');
      
      let isValid = true;

      if (!nameInput.value.trim()) {
        nameInput.classList.add('border-red-500');
        isValid = false;
      } else {
        nameInput.classList.remove('border-red-500');
      }

      if (!phoneInput.value.trim() || phoneInput.value.length < 9) {
        phoneInput.classList.add('border-red-500');
        isValid = false;
      } else {
        phoneInput.classList.remove('border-red-500');
      }

      if (isValid) {
        // Show success alert
        if (formSuccess) {
          formSuccess.classList.remove('hidden');
          formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
          setTimeout(() => {
            formSuccess.classList.add('hidden');
          }, 5000);
        }
        contactForm.reset();
      }
    });
  }

  // --- Interactive Service Tabs / Highlight ---
  const serviceCards = document.querySelectorAll('.service-card');
  serviceCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const icon = card.querySelector('.service-icon');
      if (icon) icon.classList.add('scale-110', 'text-brand-emerald');
    });
    card.addEventListener('mouseleave', () => {
      const icon = card.querySelector('.service-icon');
      if (icon) icon.classList.remove('scale-110', 'text-brand-emerald');
    });
  });

  // --- Scroll Spy for Active Navbar Highlights ---
  const spySections = document.querySelectorAll('section[id]');
  const spyLinks = document.querySelectorAll('#main-header nav a, #mobile-menu a');

  function updateActiveNavLink() {
    let currentId = '';
    const scrollPos = window.scrollY + 120; // Offset for sticky navbar

    spySections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
        currentId = section.getAttribute('id');
      }
    });

    spyLinks.forEach(link => {
      link.classList.remove('active');
      const href = link.getAttribute('href');
      if (href === `#${currentId}` || (currentId === '' && href === '#')) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', updateActiveNavLink);
  updateActiveNavLink(); // Run on load
});
