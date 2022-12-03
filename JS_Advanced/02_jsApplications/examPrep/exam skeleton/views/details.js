import { deleteById, getById } from '../api/data.js';
import { html, nothing } from '../lib.js'
import { getUserData } from '../util.js';

const detailsTemplate = (item, isOwner, onDelete) => html`
`;

export async function showDetails(ctx) {
    const furniture = await getById(ctx.params.id); //TODO

    const user = getUserData();
    const isOwner = user ? user._id == furniture._ownerId : false; //TODO

    ctx.render(detailsTemplate(furniture, isOwner, onDelete)); // TODO

    async function onDelete() {
        const confirmation = confirm('Do you really want to delete this item ?');
        if (confirmation === false) {
            return;
        }

        await deleteById(furniture._id); // TODO
        ctx.page.redirect('/');
    }
} 