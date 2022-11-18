import { html, render, nothing } from '../node_modules/lit-html/lit-html.js';
import { onEdit, onPost } from './formApi.js';

export const formRoot = document.getElementById('dataAction');

const formTemplate = (formType, callback, book) => html`
<form id="${formType}-form" @submit=${callback} 
    data-id=${book !== undefined? 
            book._id
            :nothing}>
    <h3>${formType[0].toUpperCase() + formType.substring(1, formType.length) + ' book'}</h3>
    <label>TITLE</label>
    <input type="text" name="title" placeholder="Title..." 
    .value=${book !== undefined?
        book.title
        :nothing}>
    <label>AUTHOR</label>
    <input type="text" name="author" placeholder="Author..."
    .value=${book !== undefined?
        book.author
        :nothing}>
    <input type="submit" value="Submit">
</form>
`;

export const createForm = formTemplate.bind(null, 'add', onPost); 
export const editForm = formTemplate.bind(null, 'edit', onEdit); 

export function renderForm(form){
    render(form, formRoot);
};


