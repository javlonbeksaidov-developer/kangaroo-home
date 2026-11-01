
document.addEventListener("DOMContentLoaded", () => {

    const header = document.getElementById("header");
    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");
    const navLinks = document.querySelectorAll(".nav-link");

    // Header scroll effect
    window.addEventListener("scroll", () => {
        header.classList.toggle("scrolled", window.scrollY > 50);
    });

    // Mobile menu
    menuToggle.addEventListener("click", () => {
        navMenu.classList.toggle("open");
        menuToggle.classList.toggle("open");

        const isOpen = navMenu.classList.contains("open");
        menuToggle.setAttribute("aria-expanded", isOpen);
    });

    // Close menu after clicking a link
    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            navMenu.classList.remove("open");
            menuToggle.classList.remove("open");
            menuToggle.setAttribute("aria-expanded", "false");

            navLinks.forEach(item => item.classList.remove("active"));
            link.classList.add("active");
        });
    });

    // Active navigation on scroll
    const sections = document.querySelectorAll("main section[id]");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navLinks.forEach(link => {
                    link.classList.toggle(
                        "active",
                        link.getAttribute("href") === `#${entry.target.id}`
                    );
                });
            }
        });
    }, {
        threshold: 0.35
    });

    sections.forEach(section => observer.observe(section));

});
