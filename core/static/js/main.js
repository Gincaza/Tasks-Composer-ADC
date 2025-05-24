// Aplicar o tema salvo no localStorage ao carregar a página
document.addEventListener('DOMContentLoaded', function () {
    const currentTheme = localStorage.getItem('theme') || 'light';
    if (currentTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
});