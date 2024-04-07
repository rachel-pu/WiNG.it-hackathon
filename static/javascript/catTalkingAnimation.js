document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById('cat');
    const freezeImage = document.getElementById('freeze-image');

    // Play the video for 5 seconds
    setTimeout(function() {
        video.style.display = 'none'; // Hide the video
        freezeImage.style.display = 'block'; // Show the freeze image
    }, 4000); // 5000 milliseconds = 5 seconds
});