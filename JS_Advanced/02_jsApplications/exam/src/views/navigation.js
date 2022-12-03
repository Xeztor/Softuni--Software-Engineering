import { logout } from '../api/user.js';
import { html, page, render } from '../lib.js';
import { getUserData } from "../util.js";

const navRoot = document.getElementsByTagName('header')[0]; //TODO

const navBarTemplate = (userIsLogged, logoutCallback) => html`
<a id="logo" href="/"><img id="logo-img" src="./images/logo.png" alt="" /></a>

<nav>
    <div>
        <a href="/dashboard">Dashboard</a>
    </div>
    ${userIsLogged ? 
    html`
    <div class="user">
        <a href="/create">Add Album</a>
        <a @click=${logoutCallback} href="javascript:void(0)">Logout</a>
    </div>
    `
    : html`
    <div class="guest">
        <a href="/login">Login</a>
        <a href="/register">Register</a>
    </div>
    `}
</nav>`;

export function updateNav(ctx, next) {
    const user = ctx.user;
    render(navBarTemplate(user, onLogout), navRoot);

    next();
}

function onLogout() {
    logout();
    page.redirect('/dashboard');
};