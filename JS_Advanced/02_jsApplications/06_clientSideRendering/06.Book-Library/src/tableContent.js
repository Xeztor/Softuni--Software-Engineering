import { html, render, nothing } from '../node_modules/lit-html/lit-html.js';

document.getElementById('loadBooks').addEventListener('click', loadBooks);

const url = 'http://localhost:3030/jsonstore/collections/books';

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

function onEdit(event) {
    console.log('edit');
}

function onDelete(event) {
    console.log('delete');
}

async function getBooks() {
    const response = await fetch(url);
    const books = await response.json();
    return books;
}

async function loadBooks() {
    let books = await getBooks();
    books = Object.entries(books).map(([id, bookInfo]) => Object.assign(bookInfo, { _id: id }))
    console.log(books);
    render(books.map(tableRowTemplate), tableBodyRoot);
};

