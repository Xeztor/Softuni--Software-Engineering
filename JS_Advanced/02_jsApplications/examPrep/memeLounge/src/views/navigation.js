import { logout } from '../api/user.js';
import { html, render } from '../lib.js';

const navRoot = document.getElementsByTagName('nav')[0]; //TODO

const navBarTemplate = (user, logoutCallback) => html`
<a href="/memes">All Memes</a>
<!-- Logged users -->
${user ? 
 html`
 <div class="user">
    <a href="/create">Create Meme</a>
    <div class="profile">
        <span>Welcome, ${user.email}</span>
        <a href="/profile">My Profile</a>
        <a @click=${logoutCallback} href="javascript:void(0)">Logout</a>
    </div>
</div>`
: html`
<div class="guest">
    <div class="profile">
        <a href="/login">Login</a>
        <a href="/register">Register</a>
    </div>
    <a class="active" href="/">Home Page</a>
</div>`}
`;

export function updateNav(ctx, next) {
    render(navBarTemplate(ctx.user, onLogout), navRoot)

    next();
    
    function onLogout() {
        logout();
        
        ctx.page.redirect('/');
    }
}
