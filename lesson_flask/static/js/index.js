"use strict";

let loginButton = document.getElementById('go-login');
loginButton.addEventListener('click', (event) => {
    alert('prepare for redirect');
    document.location = `/login-page`;
});