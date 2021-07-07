RunNavBar()

function RunNavBar() {
    const menu = document.querySelector(".menu");
    const iconNavBar = document.querySelector("#icon-nar-bar");
    var extensionName = document.getElementsByClassName("#icon-nar-bar");

    iconNavBar.addEventListener("click", (e) => {
        if (menu.className.search("active-narbar") == -1) {
            menu.classList.add("active-narbar");
            $('.extension').hide()
            iconNavBar.innerHTML = `<div  id="icon-nar-bar" class='rounded-circle bg-primary' style="width: 30px;height: 30px;">
                                        <i class="fa fa-bars" style="margin: 7px 0 0 9px;color: white" aria-hidden="true"></i>
                                    </div>`
        } else {
            menu.classList.remove("active-narbar");
            $('.extension').show()
            iconNavBar.innerHTML = `<div  id="icon-nar-bar" class='rounded-circle bg-primary' style="width: 30px;height: 30px;">
                                        <i class="fa fa-ellipsis-v " style="margin: 8px 0 0 14px;color: white" aria-hidden="true"></i>
                                    </div>`
        }
    });
}