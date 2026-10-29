document.addEventListener("DOMContentLoaded", () => {
    const isReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const navHeader = document.querySelector("header");
    const progressBar = document.getElementById("nav-scroll-progress");

    window.addEventListener("scroll", () => {
        const scrolled = window.scrollY;
        const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
        if (scrolled > 40) {
            navHeader?.classList.add("bg-[#070709]/95", "shadow-xl");
        } else {
            navHeader?.classList.remove("bg-[#070709]/95", "shadow-xl");
        }
        if (progressBar && maxScroll > 0) {
            progressBar.style.width = `${(scrolled / maxScroll) * 100}%`;
        }
    }, { passive: true });
});
