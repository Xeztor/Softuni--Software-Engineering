import { page, render } from './lib.js'
import { getUserData } from './util.js';
import { showMemes } from "./views/memes.js";
import { showHome } from "./views/home.js";
import { showLogin } from "./views/login.js";
import { updateNav } from "./views/navigation.js";
import { showRegister } from "./views/register.js";
import { showDetails } from './views/details.js';
import { showEdit } from './views/edit.js';
import { showCreate } from './views/create.js';
import { showProfile } from './views/profile.js';

const root = document.getElementsByTagName('main')[0]; // TODO

page(decorateContext);
page(updateNav);
page('/', showHome);
page('/create', showCreate);
page('/memes', showMemes);
page('/memes/edit/:id', showEdit);
page('/memes/:id', showDetails);
page('/login', showLogin);
page('/register', showRegister);
page('/profile', showProfile);

page.start();


function decorateContext(ctx, next) {
    ctx.render = renderMain;
    ctx.user = getUserData();

    next();
}

function renderMain(content) {
    render(content, root);
};