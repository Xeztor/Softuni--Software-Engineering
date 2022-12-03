import { del, get, post, put } from "./api.js";

const endpoints = {
    all: '',
    details: '',
    create: '',
    update: '',
    delete: '',
}

export async function getAll() {
    const data = await get(endpoints.all)
    return data;
};

export async function getById(id) {
    const data = await get(endpoints.details + id);
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