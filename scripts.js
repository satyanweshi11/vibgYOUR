$(document).ready(function () {
    // Smooth Page Load Effect
    $("body").css("opacity", "1");

    // Handle Login Form Submission
    $("#loginForm").submit(function (event) {
        event.preventDefault(); // Stop form submission

        Swal.fire({
            title: "Encrypting Your Credentials...",
            text: "Generating your unique color...",
            icon: "info",
            showConfirmButton: false,
            timer: 2000
        });

        // Delay the form submission slightly
        setTimeout(() => {
            this.submit();
        }, 2200);
    });

    // Button Hover Animation
    $(".btn").hover(function () {
        $(this).css("transform", "scale(1.05)");
    }, function () {
        $(this).css("transform", "scale(1)");
    });
});
