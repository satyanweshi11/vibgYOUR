$(document).ready(function () {
    // Get the username from the hidden span
    let username = $("#username").data("username");

    // Temporary UI Change on Hover
    $("#fontColorPicker").on("input", function () {
        $("body").css("color", $(this).val());
    });

    $("#bgColorPicker").on("input", function () {
        $("body").css("background-color", $(this).val());
    });

    $("#borderColorPicker").on("input", function () {
        $(".sidebar").css("border-color", $(this).val());
    });

    // Apply Theme on Button Click
    $("#applyTheme").click(function () {
        let fontColor = $("#fontColorPicker").val();
        let bgColor = $("#bgColorPicker").val();
        let borderColor = $("#borderColorPicker").val();

        // Apply the selected colors permanently
        $("body").css("color", fontColor);
        $("body").css("background-color", bgColor);
        $(".sidebar").css("border-color", borderColor);

        // Send the data to backend via Axios
        axios.post("/update-theme", {
            username: username,  // ✅ Username added dynamically
            font_color: fontColor,
            body_color: bgColor,
            border_color: borderColor
        }).then(response => {
            // Show a SweetAlert2 popup
            Swal.fire({
                title: "Theme Updated!",
                text: `Your new theme has been saved, ${username}!`,
                icon: "success",
                confirmButtonText: "OK",
                timer: 3000  // Auto close in 3 seconds
            });
        }).catch(error => {
            console.error("Error saving theme:", error);

            // Show an error alert if the request fails
            Swal.fire({
                title: "Oops!",
                text: "Something went wrong. Please try again!",
                icon: "error",
                confirmButtonText: "OK"
            });
        });
    });
});
