import { html } from '../lib.js';
import { register } from "../api/user.js";

const registerTemplate = (onSubmit) => html`
`; // TODO

export async function showRegister(ctx) {
    ctx.render(registerTemplate(createSubmitHandler(onRegister)))

    async function onRegister({ email, password, rePass }) { // TODO rePass rename 
        if (email == '' || password == '') {
            return alert("All fields are required.");
        };

        if (password !== rePass) {
            return alert("Passwords don\'t match");
        };

        await register(email, password);
        
        ctx.page.redirect('/')
    }
}