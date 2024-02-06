// Assuming you are using jQuery
$(document).ready(function () {
    const video = document.getElementById("video");
    const textOverlay = $("#text-overlay");

    // Use WebSocket or other means to get real-time text updates from your Python code
    // For simplicity, let's assume your Python code emits text updates through a WebSocket at ws://localhost:8000
    const socket = new WebSocket("ws://localhost:8000");

    socket.onmessage = function (event) {
        const text = event.data;
        textOverlay.text(text);
    };

    // Set the video source dynamically
    video.src = "your_video.mp4"; // Replace with your video file path
});
