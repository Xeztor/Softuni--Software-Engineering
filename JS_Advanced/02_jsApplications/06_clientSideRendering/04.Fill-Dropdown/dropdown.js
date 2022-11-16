import { render, html } from './node_modules/lit-html/lit-html.js'
document.getElementsByTagName('form')[0].addEventListener('submit', addItem);

const url = 'http://localhost:3030/jsonstore/advanced/dropdown';

const selectRoot = document.getElementById('menu');

const optionTemplate = (option) => html`
<option .value=${option._id}>${option.text}</option>`;

renderOptions();



async function renderOptions() {
    const options = await getOptions();
    render(options.map(optionTemplate), selectRoot)
}

async function getOptions() {
    const response = await fetch(url);
    if (response.ok == false) {
        return;
    }
    const data = await response.json();
    return Object.values(data);
}

function addItem(event) {
    event.preventDefault();
    const text = document.getElementById('itemText').value;
    postOption(text);
}

async function postOption(text) {
    const body = {
        text
    }
    const response = await fetch(url, {
        method: 'post',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(body)
    });
    if (response.ok == false) {
        return;
    };
    renderOptions();
};