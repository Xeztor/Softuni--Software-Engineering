import { login } from '../api/user.js'
import { html } from '../lib.js'
import { createSubmitHandler } from '../util.js'
import { updateNav } from './navigation.js'

const loginTemplate = (onLogin) => html`
<div class="container">
    <div class="row space-top">
        <div class="col-md-12">
            <h1>Login User</h1>
            <p>Please fill all fields.</p>
        </div>
    </div>
    <form @submit=${onLogin}>
        <div class="row space-top">
            <div class="col-md-4">
                <div class="form-group">
                    <label class="form-control-label" for="email">Email</label>
                    <input class="form-control" id="email" type="text" name="email">
                </div>
                <div class="form-group">
                    <label class="form-control-label" for="password">Password</label>
                    <input class="form-control" id="password" type="password" name="password">
                </div>
                <input type="submit" class="btn btn-primary" value="Login" />
            </div>
        </div>
    </form>
</div>
`

export async function showLogin(ctx) {
    ctx.render(loginTemplate(createSubmitHandler(onLogin)))

    async function onLogin({ email, password }) {
        if (email == '' || password == '') {
            return alert("All fields are required.")
        }

        await login(email, password);
        updateNav();
        ctx.page.redirect('/')
    }
}