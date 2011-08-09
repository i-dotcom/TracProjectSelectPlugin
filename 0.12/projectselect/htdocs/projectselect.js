function on_projectselect_change() {
    var s = document.getElementById('projectselect');
    if(s.value != '') {
        window.location = s.value;
    }
}
