const CODE_STRING = ' Code(s)'
const GOLD_STRING = ' Million Gold'

DataTable.type('da-price', {
    detect: function (data) {
        return typeof data === 'string' &&
        data.match(/(\d+)( Million Gold| Code\(s\))/)
            ? 'da-price'
            : null;
    },
    order: {
        pre: function (data) {
            if (data.includes(CODE_STRING)) {
                return Number(
                    data.replace(CODE_STRING, '')
                ) * 1000
            }
            return Number(
                data.replace(GOLD_STRING, '')
            );
        }
    },
    className: 'dt-da-price'
});

$('#shop-table').DataTable({
    responsive: true,
});


// On page load or when changing themes, best to add inline in `head` to avoid FOUC
if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
    localStorage.theme = 'dark';
} else {
    document.documentElement.classList.remove('dark');
    localStorage.theme = 'light';
}

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
    document.getElementById('popup').classList.toggle('hidden');
}
