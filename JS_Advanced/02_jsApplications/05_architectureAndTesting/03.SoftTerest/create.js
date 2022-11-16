import { post } from './api.js';
import { getFormData, getSection, isIdeaFormValid } from './utils.js';

document.querySelector('#create-view form').addEventListener('submit', onSubmit)
const section = getSection('create-view');

const url = '/data/ideas';

let ctx;

export async function createView(context) {
    ctx = context;
    document.querySelector('main').appendChild(section);
};

async function onSubmit(event) {
    event.preventDefault();
    if (!isIdeaFormValid(event.target)) {
        event.target.reset();
        return;
    };

    const { title, description, imageURL } = getFormData(event.target);
    const body = { title, description, img: imageURL };
    const response = await post(url, body);

    event.target.reset();
    ctx.goto('dashboard-link')
}