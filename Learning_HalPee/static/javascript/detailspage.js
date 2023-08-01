function menu_click(){
    var showbtn = document.getElementById('vertical_menu_show');
    var menu_icon = document.getElementById('menu_icon_btn');
    if (showbtn.style.display === 'block'){
        showbtn.style.display = 'none';
    }else{
        showbtn.style.display = 'block';
    }
        menu_icon.classList.toggle('change');
}
