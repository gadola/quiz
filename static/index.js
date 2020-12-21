window.onload = initall;
var  saveBookButton ;
function initall() {
    saveBookButton=document.getElementsByClassName('lesson')
    saveBookButton[1].onclick = save_ans(saveBookButton[1].id);
}
function save_ans(id) {
    alert("/ajax/" + str(id) +"/")
    var url = '/ajax/'+ id +"/";
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            alert("/ajax/" + str(id) +"/")
        }
    };
    req.open("GET", url, false);
    req.send();
}