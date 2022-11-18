import { html, render } from '../node_modules/lit-html/lit-html.js';
import { del, get } from './api.js';
import { editForm, renderForm } from './formTemplate.js';

const url = '/jsonstore/collections/books';

const tableBodyRoot = document.getElementsByTagName('tbody')[0];

const tableRowTemplate = (book) => html`
<tr>
    <td>${book.title}</td>
    <td>${book.author}</td>
    <td id=${book._id}>
        <button @click=${onEdit}>Edit</button>
        <button @click=${onDelete}>Delete</button>
    </td>
</tr>
`;

async function onEdit(event) {
    const id = event.target.parentElement.id;
    const book = await get(url + `/${id}`);
    renderForm(editForm(book));
}

async function onDelete(event) {
    const id = event.target.parentElement.id;
    await del(url + `/${id}`);
    loadBooks();
}

export async function loadBooks() {
    let books = await get(url);
    books = Object.entries(books).map(([id, bookInfo]) => Object.assign(bookInfo, { _id: id }))
    render(books.map(tableRowTemplate), tableBodyRoot);
};

