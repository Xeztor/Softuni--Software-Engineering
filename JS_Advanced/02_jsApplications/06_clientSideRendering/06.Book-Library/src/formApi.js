import { post, put } from './api.js';
import { loadBooks } from './tableContent.js';

const url = '/jsonstore/collections/books';

export async function onPost(event) {
    event.preventDefault();
    const data = isFormValid(event.target);
    if (data === false) {
        return;
    };
    await post(url, data);
    event.target.reset();
    loadBooks();
}

export async function onEdit(event) {
    event.preventDefault();
    const data = isFormValid(event.target);
    if (data === false) {
        return;
    };
    const bookId = event.target.dataset.id;
    await put(url + `/${bookId}`, data);
    event.target.reset();
    loadBooks();

}

function isFormValid(form) {
    const formData = new FormData(form);
    const { title, author } = Object.fromEntries(formData.entries());
    if (!title || !author) {
        return false;
    };
    return { title, author }
}