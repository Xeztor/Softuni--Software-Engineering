import { render, html } from './node_modules/lit-html/lit-html.js'

const root = document.getElementById('root');
const form = document.getElementsByTagName('form')[0];
form.addEventListener('submit', onClick);

const townsTemplate = (townNames) => html`
<ul>
    ${townNames.map((name) => html`<li>${name}</li>`)}
</ul>
`;

function onClick(event) {
    event.preventDefault();
    const towns = getData(event);
    render(townsTemplate(towns), root);
}

function getData(event) {
    const formData = new FormData(event.target);
    let { towns } = Object.fromEntries(formData.entries());
    towns = towns.split(', ');

    return towns;
}
