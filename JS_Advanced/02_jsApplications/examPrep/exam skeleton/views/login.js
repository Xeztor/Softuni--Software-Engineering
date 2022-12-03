import { html } from '../lib.js';
import { login } from "../api/user.js";

const loginTemplate = (onSubmit) => html`
`;

export async function showLogin(ctx) {
    ctx.render(loginTemplate(createSubmitHandler(onLogin)))

    async function onLogin({ email, password }) {
        if (email == '' || password == '') {
            return alert("All fields are required.")
        }

        await login(email, password);
        // updateNav(); TODO
        ctx.page.redirect('/')
    }
}

