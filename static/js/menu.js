$(document).ready(function () {
    let dem = 0;
    $(".oc-btn").click(function () {
        if (dem === 0) {
            $(".menu-wrapper").css("width", "230px");
            $(".normal").removeClass("out");
            $(".nav-link > p").removeClass("out");
            $(".svg-oc-btn").addClass("btn-rotate");
            dem++;
        } else {
            $(".menu-wrapper").css("width", "65px");
            $(".normal").addClass("out");
            $(".nav-link > p").addClass("out");
            $(".svg-oc-btn").removeClass("btn-rotate");
            dem--;
        }
    });
});
