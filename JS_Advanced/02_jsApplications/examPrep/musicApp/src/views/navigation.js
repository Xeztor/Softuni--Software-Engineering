import { logout } from '../api/user.js';
import { html, page, render } from '../lib.js';
import { getUserData } from "../util.js";

const navRoot = document.getElementsByTagName('header')[0];

const navBarTemplate = (userIsLogged, logoutCallback) => html`
<nav>
    <img src="./images/headphones.png">
    <a href="/">Home</a>
    <ul>
        <li><a href="/catalog">Catalog</a></li>
        <li><a href="/search">Search</a></li>
        ${userIsLogged? 
        html`
        <li><a href="/create">Create Album</a></li>
        <li><a @click=${logoutCallback} href="javascript:void(0)">Logout</a></li>`
        : html`
        <li><a href="/login">Login</a></li>
        <li><a href="/register">Register</a></li>`}
        
    </ul>
</nav>`;

export function updateNav() {
    const user = getUserData();

    render(navBarTemplate(user, onLogout), navRoot)
}

function onLogout() {
    logout();

    page.redirect('/');
};