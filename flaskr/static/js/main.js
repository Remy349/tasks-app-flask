document.addEventListener('DOMContentLoaded', () => {
    // Mostrar/Oculatar formularios de inicio/registro
    const homeLogin = document.getElementById('homeLogin'),
        homeLogup = document.getElementById('homeLogup'),
        homeLoginLogup = document.getElementById('homeLoginLogup'),
        homeLogupLogin = document.getElementById('homeLogupLogin');

    homeLoginLogup.addEventListener('click', () => {
        homeLogin.classList.remove('block');
        homeLogup.classList.remove('none');
        homeLogin.classList.add('none');
        homeLogup.classList.add('block');
    });

    homeLogupLogin.addEventListener('click', () => {
        homeLogin.classList.remove('none');
        homeLogup.classList.remove('block');
        homeLogin.classList.add('block');
        homeLogup.classList.add('none');
    });
});
