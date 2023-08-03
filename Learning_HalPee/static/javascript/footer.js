function changeName() {
    var name = document.getElementById('nav_company_name_footer');
    if (name.innerText == 'Home') {
        name.innerText = 'Learing-HalPee';
        name.style.color = 'yellow';
        name.style.width = '157px';
    }
    else {
        name.innerHTML = 'Home';
    };
}
setInterval(changeName, 2000);
