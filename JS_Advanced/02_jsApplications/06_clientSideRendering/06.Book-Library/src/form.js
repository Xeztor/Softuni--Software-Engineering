import { html, render, nothing } from '../node_modules/lit-html/lit-html.js';

const formRoot = document.getElementById('dataAction');

const formTemplate = (type, callback, bookId) => html`
<form id="${type}-form" @submit=${callback} id=${bookId !== undefined? 
            bookId
            :nothing}>
    <h3>${type[0].toUpperCase() + type.substring(1, type.length)} book</h3>
    <label>TITLE</label>
    <input type="text" name="title" placeholder="Title...">
    <label>AUTHOR</label>
    <input type="text" name="author" placeholder="Author...">
    <input type="submit" value="Submit">
</form>
`;

export const createForm = formTemplate.bind(null, 'add', onPost); 
export const editForm = formTemplate.bind(null, 'edit', onEdit); 


export function renderForm(form){
    render(form, formRoot);
};


async function onPost(event){
    event.preventDefault();
    console.log('post');
}

async function onEdit(event){
    event.preventDefault();
    console.log('edit');
}