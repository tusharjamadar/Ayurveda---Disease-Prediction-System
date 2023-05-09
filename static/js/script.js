var myNav = document.getElementById('navbar');

window.onscroll = function () { 
    if (document.body.scrollTop >= 1 || document.documentElement.scrollTop >= 1) {
        myNav.classList.add("nav-colored");
        myNav.classList.remove("nav-transparent");
    } 
    else {
        myNav.classList.add("nav-transparent");
        myNav.classList.remove("nav-colored");
    }
};


