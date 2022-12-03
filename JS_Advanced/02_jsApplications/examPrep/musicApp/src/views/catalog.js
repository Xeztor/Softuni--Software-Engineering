import { getAll } from '../api/data.js';
import { html, } from '../lib.js';
import { cardTemplate } from './card.js';

const catalogTemplate = (items, userLogged) => html`
<section id="catalogPage">
    <h1>All Albums</h1>
    ${items.length !== 0? 
    items.map(i => cardTemplate(i, userLogged))
    : html`<p>No Albums in Catalog!</p>`}

</section>
`;


export async function showCatalog(ctx) {
    const items = await getAll();

    const userLogged = ctx.user;
    ctx.render(catalogTemplate(items, userLogged))
};