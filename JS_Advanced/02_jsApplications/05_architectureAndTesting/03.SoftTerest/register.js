import { post } from "./api.js";
import { checkNav, getFormData, getSection, registerFormIsValid, setSession } from "./utils.js";

document.querySelector('#register-view form').addEventListener('submit', onSubmit);
const section = getSection('register-view');

const registerUrl = '/users/register'
let ctx;

export async function registerView(context) {
    ctx = context;
    document.querySelector('main').appendChild(section);
    document.querySelector('.alreadyUser a').addEventListener('click', () => ctx.goto('login-link'));
};

async function onSubmit(event) {
    event.preventDefault();
    if (!registerFormIsValid(event.target)) {
        event.target.reset();
        return;
    };

    const { email, password } = getFormData(event.target);
    const body = { email, password };

    const userData = await post(registerUrl, body);
    setSession(userData);

    checkNav();
    ctx.goto('home-link')
};