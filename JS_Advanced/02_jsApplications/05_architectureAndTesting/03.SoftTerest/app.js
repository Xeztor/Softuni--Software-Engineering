import { createView } from "./create.js";
import { dashboardView } from "./dashboard.js";
import { loginView } from "./login.js";
import { registerView } from "./register.js";
import { homeView } from "./home.js";
import { logout } from "./auth.js";
import './details.js';
import { detailsView } from "./details.js";

document.querySelector('nav').addEventListener('click', onNavigate);


const views = {
    "dashboard-link": dashboardView,
    "create-link": createView,
    "logout-link": logout,
    "login-link": loginView,
    "register-link": registerView,
    "home-link": homeView,
    "details-link": detailsView
};

goto('home-link');


function onNavigate(event) {
    if (event.target.tagName === "A") {
        const id = event.target.id;
        if (goto(id)) {
            event.preventDefault();
        };
    };
}

function goto(viewName, ...params) {
    const view = views[viewName];
    if (typeof view === 'function') {
        document.querySelector('main').replaceChildren();
        view({
            goto,
        }, ...params);
        return true;
    };
    return false
}
