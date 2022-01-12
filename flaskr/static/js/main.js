document.addEventListener('DOMContentLoaded', () => {
    // Validar los formularios de registro e inicio de sesion
    const homeLogin = document.getElementById('homeLogin'),
        homeLogup = document.getElementById('homeLogup');
    
    if (homeLogin) {
        homeLogin.addEventListener('submit', (e) => {
            const usernameLogin = document.getElementById('usernameLogin').value,
                passwordLogin = document.getElementById('passwordLogin').value;
            const homeLoginError = document.getElementById('homeLoginError');
            let errors = false;

            if (usernameLogin.length == 0) {
                homeLoginError.innerHTML = 'Username required!';
                errors = true;
            } else if (passwordLogin.length == 0) {
                homeLoginError.innerHTML = 'Password required!';
                errors = true;
            }

            if (errors) {
                e.preventDefault();
            }
        });
    } else {
        homeLogup.addEventListener('submit', (e) => {
            const usernameLogup = document.getElementById('usernameLogup').value,
                passwordLogup = document.getElementById('passwordLogup').value,
                passwordAgainLogup = document.getElementById('passwordAgainLogup').value;
            const homeLogupError = document.getElementById('homeLogupError');
            let errors = false;

            if (usernameLogup.length == 0 || passwordLogup == 0 || passwordAgainLogup == 0) {
                homeLogupError.innerHTML = 'Filds can not be empty!!';
                errors = true;
            } else if (usernameLogup.length > 12 || usernameLogup.length < 3) {
                homeLogupError.innerHTML = 'Username length can not be longer than 12 or shorter than 3 characters!';
                errors = true;
            } else if (passwordAgainLogup != passwordLogup) {
                homeLogupError.innerHTML = 'Confirm password do not match with the password you wrote!';
                errors = true;
            }

            if (errors) {
                e.preventDefault();
            }
        });
    }
});
