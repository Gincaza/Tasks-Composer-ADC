document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggleThemeButton');
    const currentTheme = localStorage.getItem('theme') || 'light';

    if (currentTheme === 'dark') {
        document.body.classList.add('dark-theme');
        toggleButton.textContent = 'Alternar para Modo Claro';
    }

    toggleButton.addEventListener('click', function () {
        if (document.body.classList.contains('dark-theme')) {
            document.body.classList.remove('dark-theme');
            localStorage.setItem('theme', 'light');
            toggleButton.textContent = 'Alternar para Modo Escuro';
        } else {
            document.body.classList.add('dark-theme');
            localStorage.setItem('theme', 'dark');
            toggleButton.textContent = 'Alternar para Modo Claro';
        }
    });
});