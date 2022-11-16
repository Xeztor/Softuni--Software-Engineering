import { del, get } from './api.js';
import { getSection } from './utils.js';

const section = getSection('details-view');

const baseUrl = '/data/ideas/'
let ctx;

export async function detailsView(context, id) {
    ctx = context;
    document.querySelector('main').appendChild(section);

    displayDetails(id);
};

async function displayDetails(id) {
    section.replaceChildren();

    const url = baseUrl + id;
    const idea = await get(url);

    const card = createCard(idea);

    section.appendChild(card);
};

function createCard(idea) {
    const div = document.createElement('div');
    div.classList.add('container', 'home', 'some');
    div.innerHTML =
        `<div class="container home some">` +
        `<img class="det-img" src="${idea.img}" />` +
        `<div class="desc">` +
        `<h2 class="display-5">${idea.title}</h2>` +
        `<p class="infoType">Description:</p>` +
        `<p class="idea-description">${idea.description}</p>` +
        `</div>` +
        `<div class="text-center">` +
        `<a class="btn detb" href="">Delete</a>` +
        `</div>` +
        `</div>`;

    let a = div.getElementsByClassName('btn')[0];
    if (idea._ownerId != localStorage.getItem('userId')) {
        a.remove();
    } else {
        a.id = idea._id;
        a.addEventListener('click', deleteIdea);
    };

    return div;
}

async function deleteIdea(event) {
    const id = event.target.id;
    await del(baseUrl + id);
    ctx.goto('dashboard-link');
}