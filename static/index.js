const primaryNav = document.querySelector(".nav");
const mobileToggle = document.querySelector(".mobile-toggle");
const mobileMenu = document.querySelector("#menu-toggle");


mobileToggle.addEventListener("click", () => {
    const visible = primaryNav.getAttribute("data-visible");

    if (visible == 'false')
    {
        primaryNav.setAttribute("data-visible", true);
        mobileMenu.setAttribute("src","static/menu-open.png");
        
    }
    else if (visible == 'true')
    {
        primaryNav.setAttribute("data-visible", false);
        mobileMenu.setAttribute("src","static/menu-close.png");
        
    }
});