import { logout } from '../api/user.js';
import { html, page, render } from '../lib.js';
import { getUserData } from "../util.js";

const navRoot = document.getElementsByTagName('header')[0]; //TODO

const navBarTemplate = (userIsLogged, logoutCallback) => html`
`

export function updateNav() {
    const user = getUserData();

    render(navBarTemplate(user, onLogout), navRoot)
}

function onLogout() {
    logout();
    updateNav();
    page.redirect('/');
};