import { page, render } from './lib.js'
import { getUserData } from './util.js';
import { showCatalog } from './views/catalog.js';
import { showCreate } from './views/create.js';
import { showDetails } from './views/details.js';
import { showEdit } from './views/edit.js';
import { showHome } from "./views/home.js";
import { showLogin } from './views/login.js';
import { updateNav } from './views/navigation.js';
import { showRegister } from './views/register.js';
import { showSearch } from './views/search.js';

const root = document.getElementById('main-content'); // TODO

page(decorateContext);
page(updateNavigation);
page(parseQuery);
page('/', showHome);
page('/login', showLogin);
page('/register', showRegister);
page('/create', showCreate);
page('/catalog', showCatalog);
page('/catalog/edit/:id', showEdit);
page('/catalog/:id', showDetails);
page('/search', showSearch);

page.start();


function parseQuery(ctx, next) {
    ctx.query = {};
    if (ctx.querystring) {
        const query = Object.fromEntries(ctx.querystring.split('&').map(i => i.split('=')));
        Object.assign(ctx.query, query);
    };

    next();
}
function decorateContext(ctx, next) {
    ctx.render = renderMain;
    ctx.user = getUserData();

    next();
}

function updateNavigation(ctx, next) {
    updateNav();

    next();
};

function renderMain(content) {
    render(content, root);
};