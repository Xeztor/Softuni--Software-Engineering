import { getAll } from '../api/data.js';
import { html } from '../lib.js'

const catalogTemplate = (items) => html`
`;

const card = (item) => html`
`;

export async function showCatalog(ctx) {
    const items = await getAll();

    ctx.render(catalogTemplate(items))
};