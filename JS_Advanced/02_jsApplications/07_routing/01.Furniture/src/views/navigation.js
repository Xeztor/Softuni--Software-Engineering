import { logout } from '../api/user.js';
import { html, page, render } from '../lib.js';
import { getUserData } from "../util.js";

const navRoot = document.getElementsByTagName('header')[0];

const navBarTemplate = (userIsLogged, logoutCallback) => html`
<h1><a href="/">Furniture Store</a></h1>
<nav>
    <a id="catalogLink" href="/" class="active">Dashboard</a>
    ${userIsLogged ?
    html`
    <div id="user">
        <a id="createLink" href="/create">Create Furniture</a>
        <a id="profileLink" href="/my-furniture">My Publications</a>
        <a @click=${logoutCallback} id="logoutBtn" href="javascript:void(0)">Logout</a>
    </div>`
    : html`
    <div id="guest">
        <a id="loginLink" href="/login">Login</a>
        <a id="registerLink" href="/register">Register</a>
    </div>`

    }
</nav>`

export function updateNav() {
    const user = getUserData();

    render(navBarTemplate(user, onLogout), navRoot)
}

function onLogout() {
    logout();
    updateNav();
    page.redirect('/');
};