import { page } from './lib.js'
import { getUserData } from './util.js';
import { updateNav } from "./views/navigation.js";

const root = document.getElementsByTagName('main')[0]; // TODO

page(decorateContext);
page(updateNavigation);
// page('/', showCatalog);  // TODO

page.start();

// updateNav(); // TODO

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