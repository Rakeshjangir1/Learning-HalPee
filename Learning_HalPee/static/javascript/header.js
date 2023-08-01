function changeName() {
    var name = document.getElementById('nav_company_name');
    if (name.innerText == 'Learing-HalPee') {
        name.innerText = 'Home';
        name.style.color = 'yellow';
        name.style.width = '157px';
    }
    else {
        name.innerHTML = 'Learing-HalPee';
    };
}
setInterval(changeName, 2000);


