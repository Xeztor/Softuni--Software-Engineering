import { page, render } from './lib.js'
import { showCatalog } from './views/catalog.js';
import { showCreate } from './views/create.js';
import { showDetails } from './views/details.js';
import { showEdit } from './views/edit.js';
import { showLogin } from './views/login.js';
import { showMyFurniture } from './views/myFurniture.js';
import { updateNav } from './views/navigation.js';
import { showRegister } from './views/register.js';

const root = document.getElementsByTagName('main')[0];

page(decorateContext);
page('/', showCatalog);
page('/catalog/edit/:id', showEdit);
page('/catalog/:id', showDetails);
page('/login', showLogin);
page('/register', showRegister);
page('/create', showCreate);
page('/my-furniture', showMyFurniture);

page.start();

updateNav();

function decorateContext(ctx, next) {
    ctx.render = renderMain;

    next();
}

function renderMain(content) {
    render(content, root);
};