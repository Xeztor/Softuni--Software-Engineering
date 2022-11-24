import { getUserData } from "../util.js";
import { del, get, post, put } from "./api.js";

const endpoints = {
    create: '/data/catalog',
    all: '/data/catalog',
    details: '/data/catalog/',
    update: '/data/catalog/',
    delete: '/data/catalog/',
    myFurniture: (userId) => `/data/catalog?where=_ownerId%3D%22${userId}%22`

}

export async function getAllFurniture() {
    const data = await get(endpoints.all)
    return data;
};

export async function getFurnitureById(id) {
    const data = await get(endpoints.details + id);
    return data;
}

export async function getCurrentUserPublications() {
    const user = getUserData();
    const data = get(endpoints.myFurniture(user._id));
    return data;
}

export async function deleteFurnitureById(id) {
    await del(endpoints.delete + id);
}

export async function editFurniture(id, data) {
    await put(endpoints.update + id, data);
}

export async function createFurniture(data) {
    await post(endpoints.create, data);
}