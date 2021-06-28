$(document).ready(function () {
    $('#search-field').keypress(function (event) {
        let keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '32') {
            str = document.getElementById('search-field').value;
            window.find(str, false)
        }

    });

    $(".dark-theme").click(function () {
        localStorage.setItem('theme', "dark");
        darkTheme()
        $(".dashboard-wrapper").removeClass("dashboard_light_theme");
    });

    $(".light-theme").click(function () {
        localStorage.setItem('theme', "light");
        lightTheme()
        $(".dashboard-wrapper").addClass("dashboard_light_theme");
    });

    if (localStorage.getItem('theme') === 'dark') {
        darkTheme()
        $(".dashboard-wrapper").removeClass("dashboard_light_theme");
    } else {
        lightTheme()
        $(".dashboard-wrapper").addClass("dashboard_light_theme");
    }

});

function darkTheme() {
    $(".header-dark").css("background-color", "#282d32");
    $(".header-dark .navbar.navbar-dark .navbar-nav .nav-link").css("color", "#d9d9d9");
    $(".header-dark .navbar .form-inline label i").css("color", "#ccc");
    $(".navbar-brand img").attr("src", "base/css/logo.jpg");
    $(".footer-dark").css("background-color", "#282d32");
    $(".footer-dark").css("color", "#f0f9ff");
    $(".footer-dark .item.social > a").css("color", "#282d32");
    $("body").css("background-color", "#333333");
    $(".footer-dark .item.social > a").css("color", "rgb(240, 249, 255)");
    $(".menu-dark .menu-wrapper").css("background-color", "rgba(2, 10, 16, 0.85)");
    $(".menu-dark .menu-wrapper .nav .nav-item a").css("color", "#d9d9d9");
    $(".menu-dark").css("box-shadow", "none");
    $(".copyright").css("color", "rgb(240, 249, 255)");

}

function lightTheme() {
    $(".header-dark").css("background-color", "#d9d9d9");
    $(".header-dark .navbar.navbar-dark .navbar-nav .nav-link").css("color", "#282d32");
    $(".header-dark .navbar .form-inline label i").css("color", "#282d32");
    $(".navbar-brand img").attr("src", "base/css/logo_light.jpg");
    $(".footer-dark").css("background-color", "#f0f9ff");
    $(".footer-dark").css("color", "#282d32");
    $("body").css("background-color", "#ffffff");
    $(".footer-dark .item.social > a").css("color", "#282d32");
    $(".footer-dark .item.social > a").css("border", "0.5px #282d32 solid");
    $(".copyright").css("color", "black");
    $(".menu-dark .menu-wrapper").css("background-color", "#d9d9d9");
    $(".menu-dark .menu-wrapper .nav .nav-item a").css("color", "rgba(2, 10, 16, 0.85)");
    $(".menu-dark").css("box-shadow", "#9cb9b9 1.95px 1.95px 2.6px");

}