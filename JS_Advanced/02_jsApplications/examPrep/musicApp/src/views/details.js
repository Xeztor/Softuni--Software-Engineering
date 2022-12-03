import { deleteById, getById } from '../api/data.js';
import { html, nothing } from '../lib.js'
import { getUserData } from '../util.js';

const detailsTemplate = (item, isOwner, onDelete) => html`
<section id="detailsPage">
    <div class="wrapper">
        <div class="albumCover">
            <img src="${item.imageUrl}">
        </div>
        <div class="albumInfo">
            <div class="albumText">

                <h1>Name: ${item.name}</h1>
                <h3>Artist: ${item.artist}</h3>
                <h4>Genre: ${item.genre}</h4>
                <h4>Price: $${item.price}</h4>
                <h4>Date: ${item.releaseDate}</h4>
                <p>Description: ${item.description}</p>
            </div>

            ${isOwner ?
            html`
            <div class="actionBtn">
                <a href="/catalog/edit/${item._id}" class="edit">Edit</a>
                <a @click=${onDelete} href="javascript:void(0)" class="remove">Delete</a>
            </div>`
            : nothing}

        </div>
    </div>
</section>`;

export async function showDetails(ctx) {
    const album = await getById(ctx.params.id);

    const user = getUserData();
    const isOwner = user ? user._id == album._ownerId : false;

    ctx.render(detailsTemplate(album, isOwner, onDelete));

    async function onDelete() {
        const confirmation = confirm('Do you really want to delete this item ?');
        if (confirmation === false) {
            return;
        }

        await deleteById(album._id);
        ctx.page.redirect('/catalog');
    }
} 