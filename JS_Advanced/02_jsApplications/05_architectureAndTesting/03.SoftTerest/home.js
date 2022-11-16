import { checkNav, getSection } from './utils.js';

const section = getSection('home-view');

checkNav()

export async function homeView(ctx) {
    document.querySelector('main').appendChild(section);
};