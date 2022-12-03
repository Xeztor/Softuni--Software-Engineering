import { deleteById, getById } from '../api/data.js';
import { html, nothing } from '../lib.js'
import { getUserData } from '../util.js';

const detailsTemplate = (item, isOwner, onDelete) => html`
<section id="meme-details">
    <h1>Meme Title: ${item.title}

    </h1>
    <div class="meme-details">
        <div class="meme-img">
            <img alt="meme-alt" src=${item.imageUrl}>
        </div>
        <div class="meme-description">
            <h2>Meme Description</h2>
            <p>
                ${item.description}
            </p>

            <!-- Buttons Edit/Delete should be displayed only for creator of this meme  -->
            ${isOwner ?
            html`
            <a class="button warning" href="/memes/edit/${item._id}">Edit</a>
            <button @click=${onDelete} class="button danger">Delete</button>`
            : nothing}

        </div>
    </div>
</section>`;

export async function showDetails(ctx) {
    const meme = await getById(ctx.params.id);

    const user = getUserData();
    const isOwner = user ? user._id == meme._ownerId : false;

    ctx.render(detailsTemplate(meme, isOwner, onDelete));

    async function onDelete() {
        const confirmation = confirm('Do you really want to delete this item ?');
        if (confirmation === false) {
            return;
        }

        await deleteById(meme._id);
        ctx.page.redirect('/memes');
    }
} 