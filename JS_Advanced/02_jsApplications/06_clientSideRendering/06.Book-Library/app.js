import { html, render, nothing } from './node_modules/lit-html/lit-html.js';
import { renderForm, createForm } from './src/formTemplate.js'
import { loadBooks } from './src/tableContent.js'

document.getElementById('loadBooks').addEventListener('click', loadBooks);

renderForm(createForm());

