if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
    localStorage.theme = 'dark';
} else {
    document.documentElement.classList.remove('dark');
    localStorage.theme = 'light';
}

// load functions
function toggleDarkMode() {
    if (localStorage.theme === 'dark') {
        document.documentElement.classList.remove('dark');
        localStorage.theme = 'light';
    }
    else if (localStorage.theme === 'light') {
        document.documentElement.classList.add('dark');
        localStorage.theme = 'dark';
    }
}

function toggleModal() {
    document.getElementById('content-block').classList.toggle('blur-sm');
    document.getElementById('modal').classList.toggle('hidden');
    //document.getElementById('popup').classList.toggle('hidden');
}
