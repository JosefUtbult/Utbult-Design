// Set class to documentElement to let the theme class to be set before the page loads
function setTheme() {
    const lightmode = localStorage.getItem('theme') == 'light';
    if(lightmode){
        // body.classList.add('light')
        document.documentElement.classList.add('light');
    }
    else {
        // body.classList.add('dark')
        document.documentElement.classList.add('dark');
    }
    window.onload = () => {
        const lightmode = localStorage.getItem('theme') == 'light';
        document.getElementById("theme-switch").checked = !lightmode;
    };
}

function toggleLightDarkMode() {
    const lightmode = document.getElementById("theme-switch").checked;
    document.documentElement.classList.add('theme-transition');

    if(lightmode){
        document.documentElement.classList.remove('light')
        document.documentElement.classList.add('dark')
    }
    else {
        document.documentElement.classList.remove('dark')
        document.documentElement.classList.add('light')
    }
    
    localStorage.setItem('theme', lightmode ? 'dark' : 'light');
    setTimeout(() => {
        document.documentElement.classList.remove('theme-transition');
    }, 500);
}

function toggleBurgerMenu() {
    const el = document.getElementById('burger-menu');
    if(el.classList.contains('open')) {
        el.classList.remove('open');
    }
    else {
        el.classList.add('open');
    }
}

function closeBurgerMenu() {
    const el = document.getElementById('burger-menu');
    if(el.classList.contains('open')) {
        el.classList.remove('open');
    }
}

function toggleBurgerMenuInstance(buttonEl) {
    el = buttonEl.parentNode.parentNode.parentNode.getElementsByTagName('ul')[0];
    if(el?.classList.contains('hidden')) {
        el?.classList.remove('hidden');
    }
    else {
        el?.classList.add('hidden');
    }
}

setTheme();