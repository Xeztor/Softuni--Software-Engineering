import { endUserSession, setUserData } from "../util.js"
import { get, post } from "./api.js"

const endpoints = {
    register: '/users/register',
    login: '/users/login',
    logout: '/users/logout'
};

export async function login(email, password) {
    const { _id, username, email: resultEmail, gender, accessToken } = await post(endpoints.login, { email, password })

    setUserData({
        _id,
        username,
        email: resultEmail,
        accessToken,
        gender
    });
}

export async function register(registerData) {
    const { _id, username, email: resultEmail, gender, accessToken } = await post(endpoints.register, registerData)

    setUserData({
        _id,
        username,
        email: resultEmail,
        accessToken,
        gender
    });
}


export function logout() {
    get(endpoints.logout);

    endUserSession();
}