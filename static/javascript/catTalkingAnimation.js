document.addEventListener("DOMContentLoaded", function () {
    const cat = document.getElementById('cat');
    let isOpen = false;
    let timer = setTimeout(stopAnimation, 6000); // Stop animation after 10 seconds

    function stopAnimation() {
        clearInterval(interval);
        clearTimeout(timer);
    }

    const interval = setInterval(function () {
        isOpen = !isOpen;
        if (isOpen) {
            cat.src = "static/images/cat.png";
        } else {
            cat.src = "static/images/cat_open.png";
        }
    }, 100); // Adjust timing as needed
});