document.addEventListener("DOMContentLoaded", function() {
    var text = document.querySelector(".text");
    window.addEventListener("scroll", function() {
        var scroll = window.scrollY;

        if (scroll >= 50) {
            text.style.opacity="0.3";
            text.classList.add("hidden");
        } else {
            text.style.opacity="1";
            text.classList.remove("hidden");
        }


    });
});