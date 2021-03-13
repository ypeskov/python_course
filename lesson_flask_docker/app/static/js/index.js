"use strict";

const loginButton = document.getElementById('go-login');
const infoMsg = document.querySelector('.info-msg');
const logoutButton = document.querySelector('#logout');

loginButton.addEventListener('click', (event) => {
    loginButton.classList.add('hidden');
    infoMsg.classList.remove('hidden');
});

logoutButton.addEventListener('click', () => {
    infoMsg.classList.add('hidden');
    loginButton.classList.remove('hidden');
});