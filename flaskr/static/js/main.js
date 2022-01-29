document.addEventListener('DOMContentLoaded', () => {

    const homeLogin = document.getElementById('homeLogin'),
        homeLogup = document.getElementById('homeLogup');
    const hideBtn = document.getElementById('hideBtn');
    const hideForm = document.querySelectorAll('.hide-form');
    const tasksForm = document.getElementById('tasksForm');

    if (tasksForm) {
        tasksForm.onsubmit = (e) => {
            const data = new FormData(tasksForm);
            
            fetch('/tasks', {
                method: 'POST',
                body: data,
            })
                .then(function(resp) {
                    if (resp.ok) {
                        fetch('/tasks_get')
                            .then(resp => resp.json())
                            .then(function(data) {
                                const addTasks = document.getElementById('addTasks');
                                let divTasks = createNode('div'),
                                    pTitle = createNode('p'),
                                    pDesc = createNode('p'),
                                    divBtns = createNode('div'),
                                    btnOne = createNode('button'),
                                    btnTwo = createNode('button'),
                                    iEdit = createNode('i'),
                                    iTrash = createNode('i');

                                divTasks.classList.add('tasks__task');
                                pTitle.classList.add('tasks__task-title');
                                pDesc.classList.add('tasks__task-description');
                                divBtns.classList.add('tasks__task-btns');
                                btnOne.classList.add('tasks__task-btn');
                                btnTwo.classList.add('tasks__task-btn');
                                iEdit.classList.add('bx');
                                iEdit.classList.add('bx-edit');
                                iEdit.classList.add('tasks__task-icon');
                                iTrash.classList.add('bx');
                                iTrash.classList.add('bx-trash');
                                iTrash.classList.add('tasks__task-icon');

                                data.forEach(d => {
                                    pTitle.innerText = d.title;
                                    pDesc.innerText = d.description;
                                    appendNode(divTasks, pTitle);
                                    appendNode(divTasks, pDesc);
                                    appendNode(btnOne, iEdit);
                                    appendNode(btnTwo, iTrash);
                                    appendNode(divBtns, btnOne);
                                    appendNode(divBtns, btnTwo);
                                    appendNode(divTasks, divBtns);
                                    appendNode(addTasks, divTasks);
                                });
                            })
                            .catch(function(err) {
                                alert(err);
                            })
                        ;
                    } else { throw 'Error en la lamada AJAX!'; }
                })
                .catch(function(err) {
                    alert(err);
                })
            ;
            
            e.preventDefault();
        };

        hideBtn.addEventListener('click', () => {
            hideForm.forEach(h => {
                h.classList.toggle('none');
            });
            if (hideBtn.text == 'Hide') {
                hideBtn.innerText = 'Show';
            } else {
                hideBtn.innerText = 'Hide';
            }
        });
    } else {
        if (homeLogin) {
            homeLogin.addEventListener('submit', (e) => {
                const usernameLogin = document.getElementById('usernameLogin').value,
                    passwordLogin = document.getElementById('passwordLogin').value;
                const homeLoginError = document.getElementById('homeLoginError');
                let errors = false;
                const noEspacios = /\s/;

                if (noEspacios.test(usernameLogin) || noEspacios.test(passwordLogin)) {
                    homeLoginError.innerHTML = 'Do not use white spaces!';
                    errors = true;
                } else if (usernameLogin.length == 0) {
                    homeLoginError.innerHTML = 'Username required!';
                    errors = true;
                } else if (passwordLogin.length == 0) {
                    homeLoginError.innerHTML = 'Password required!';
                    errors = true;
                }

                if (errors) { e.preventDefault(); }
            });
        } else {
            homeLogup.addEventListener('submit', (e) => {
                const usernameLogup = document.getElementById('usernameLogup').value,
                    passwordLogup = document.getElementById('passwordLogup').value,
                    passwordAgainLogup = document.getElementById('passwordAgainLogup').value;
                const homeLogupError = document.getElementById('homeLogupError');
                let errors = false;
                const noEspacios = /\s/;

                if (noEspacios.test(usernameLogup) || noEspacios.test(passwordLogup) || noEspacios.test(passwordAgainLogup)) {
                    homeLogupError.innerHTML = 'Do not use white spaces!';
                    errors = true;
                } else if (usernameLogup.length == 0 || passwordLogup == 0 || passwordAgainLogup == 0) {
                    homeLogupError.innerHTML = 'Filds can not be empty!';
                    errors = true;
                } else if (usernameLogup.length > 12 || usernameLogup.length < 3) {
                    homeLogupError.innerHTML = 'Username length can not be longer than 12 or shorter than 3 characters!';
                    errors = true;
                } else if (passwordLogup.length > 12 || passwordLogup.length < 6) {
                    homeLogupError.innerHTML = 'Password length can not be longer than 12 or shorter than 6 characters!';
                    errors = true;
                } else if (passwordAgainLogup != passwordLogup) {
                    homeLogupError.innerHTML = 'Confirm password do not match with the password you wrote!';
                    errors = true;
                }

                if (errors) { e.preventDefault(); }
            });
        }
    }
});

function createNode(element) { return document.createElement(element); }

function appendNode(parent, child) { return parent.appendChild(child); }
