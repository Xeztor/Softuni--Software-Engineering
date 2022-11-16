import { post } from "./api.js";
import { checkNav, getFormData, getSection, loginFormIsValid, setSession } from "./utils.js";

document.querySelector('#login-view form').addEventListener('submit', onSubmit);
const section = getSection('login-view');

const loginUrl = '/users/login'
let ctx;

export async function loginView(context) {
    ctx = context;
    document.querySelector('main').appendChild(section);
    document.querySelector('.alreadyUser a').addEventListener('click', () => ctx.goto('register-link'));
};

async function onSubmit(event) {
    event.preventDefault();
    if (!loginFormIsValid(event.target)) {
        event.target.reset();
        return;
    };

    const { email, password } = getFormData(event.target);
    const body = { email, password };

    const userData = await post(loginUrl, body);
    setSession(userData);

    checkNav();
    ctx.goto('home-link')
};