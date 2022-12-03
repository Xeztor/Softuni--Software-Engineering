import { endUserSession, setUserData } from "../util.js"
import { get, post } from "./api.js"

const endpoints = {
    register: '/users/register',
    login: '/users/login',
    logout: '/users/logout'
};

export async function login(email, password) {
    const { _id, email: resultEmail, accessToken } = await post(endpoints.login, { email, password })

    setUserData({
        _id,
        email: resultEmail,
        accessToken
    });
}

export async function register(email, password) {
    const { _id, email: resultEmail, accessToken } = await post(endpoints.register, { email, password })

    setUserData({
        _id,
        email: resultEmail,
        accessToken
    });
}


export function logout() {
    get(endpoints.logout);

    endUserSession();
}