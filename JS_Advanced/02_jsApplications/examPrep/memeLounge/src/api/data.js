import { del, get, post, put } from "./api.js";

const endpoints = {
    all: '/data/memes?sortBy=_createdOn%20desc',
    details: '/data/memes/',
    memesByUserId: (userId) => `/data/memes?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`,
    create: '/data/memes',
    update: '/data/memes/',
    delete: '/data/memes/',
}

export async function getAll() {
    const data = await get(endpoints.all)
    return data;
};

export async function getById(id) {
    const data = await get(endpoints.details + id);
    return data;
}

export async function getByUserId(userId) {
    const data = await get(endpoints.memesByUserId(userId))
    return data;
}

export async function deleteById(id) {
    await del(endpoints.delete + id);
}

export async function editById(id, data) {
    await put(endpoints.update + id, data);
}

export async function create(data) {
    await post(endpoints.create, data);
}