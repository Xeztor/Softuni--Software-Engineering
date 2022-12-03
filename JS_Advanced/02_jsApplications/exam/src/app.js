import { page, render } from './lib.js'
import { getUserData } from './util.js';
import { showCreate } from './views/create.js';
import { showDashboard } from './views/dashboard.js';
import { showDetails } from './views/details.js';
import { showEdit } from './views/edit.js';
import { showHome } from './views/home.js';
import { showLogin } from './views/login.js';
import { updateNav } from "./views/navigation.js";
import { showRegister } from './views/register.js';

const root = document.getElementsByTagName('main')[0]; // TODO

page(decorateContext);
page(updateNav);
page('/', showHome);
page('/dashboard', showDashboard);
page('/dashboard/edit/:id', showEdit);
page('/dashboard/:id', showDetails);
page('/login', showLogin);
page('/register', showRegister);
page('/create', showCreate);

page.start();

function decorateContext(ctx, next) {
    ctx.render = renderMain;
    ctx.user = getUserData();

    next();
}

function renderMain(content) {
    render(content, root);
};