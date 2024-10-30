document.addEventListener("DOMContentLoaded", function () {
    const posts = document.querySelectorAll(".post-card");

    const observer = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    observer.unobserve(entry.target);  // Stop observing once it's visible
                }
            });
        },
        { threshold: 0.1 }  // Trigger when 10% of the element is in view
    );

    posts.forEach(post => {
        observer.observe(post);
    });
});
