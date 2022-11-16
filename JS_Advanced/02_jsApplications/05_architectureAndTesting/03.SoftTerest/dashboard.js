import { get } from './api.js';
import { getSection } from './utils.js';

const noIdeasView = document.querySelector('#dashboard-holder h1');
noIdeasView.remove();
const holder = document.getElementById('dashboard-holder');
const section = getSection('dashboard-view');

const url = '/data/ideas?select=_id%2Ctitle%2Cimg&sortBy=_createdOn%20desc'
let ctx;

export async function dashboardView(context) {
    ctx = context;
    document.querySelector('main').appendChild(section);
    displayIdeas();
};

async function displayIdeas() {
    clearHolder();

    const ideas = await get(url);
    const elements = Object.values(ideas).map(creatElementCard);
    if (elements.length === 0) {
        holder.replaceChildren(noIdeasView)
        return
    };
    holder.replaceChildren(...elements);
}

function creatElementCard(idea) {
    const div = document.createElement('div');
    div.classList.add('card', 'overflow-hidden', 'current-card', 'details');
    div.innerHTML =
        `<div class="card-body">` +
        `<p class="card-text">${idea.title}</p>` +
        `</div>` +
        `<img class="card-image" src="${idea.img}" alt="Card image cap">` +
        `<a class="btn" id="${idea._id}" href="javascript:void(0)">Details</a>`;

    div.getElementsByClassName('btn')[0].addEventListener('click', () => ctx.goto('details-link', idea._id))
    return div;
}

function clearHolder() {
    [...section.getElementsByClassName('card')].forEach(el => el.remove());
}