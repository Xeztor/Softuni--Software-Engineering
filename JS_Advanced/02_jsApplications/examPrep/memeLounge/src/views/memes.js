import { getAll } from '../api/data.js';
import { html } from '../lib.js'

const catalogTemplate = (items) => html`
<section id="meme-feed">
    <h1>All Memes</h1>
    <div id="memes">
        ${items ? 
        items.map(card)
        :html `<p class="no-memes">No memes in database.</p>`}
    </div>
</section>`;

const card = (item) => html`
<div class="meme">
    <div class="card">
        <div class="info">
            <p class="meme-title">${item.title}</p>
            <img class="meme-image" alt="meme-img" src=${item.imageUrl}>
        </div>
        <div id="data-buttons">
            <a class="button" href="/memes/${item._id}">Details</a>
        </div>
    </div>
</div>`;

export async function showMemes(ctx) {
    const items = await getAll();

    ctx.render(catalogTemplate(items))
};