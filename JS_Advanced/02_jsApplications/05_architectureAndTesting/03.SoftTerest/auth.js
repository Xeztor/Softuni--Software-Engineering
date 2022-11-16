import { get } from "./api.js";
import { checkNav, clearSession } from "./utils.js";

const logoutUrl = "/users/logout"

export async function logout(ctx) {
    try {
        await get(logoutUrl);
    } catch (err) {
        console.log(err);
    }
    clearSession();
    checkNav();
    ctx.goto('home-link');
}