import { html } from '../lib.js'
import { create } from "../api/data.js"
import { createSubmitHandler } from "../util.js";
import { showNotification } from './notification.js';

const createTemplate = (onSubmit) => html`
<section id="create-meme">
    <form @submit=${onSubmit} id="create-form">
        <div class="container">
            <h1>Create Meme</h1>
            <label for="title">Title</label>
            <input id="title" type="text" placeholder="Enter Title" name="title">
            <label for="description">Description</label>
            <textarea id="description" placeholder="Enter Description" name="description"></textarea>
            <label for="imageUrl">Meme Image</label>
            <input id="imageUrl" type="text" placeholder="Enter meme ImageUrl" name="imageUrl">
            <input type="submit" class="registerbtn button" value="Create Meme">
        </div>
    </form>
</section>`; // TODO

export async function showCreate(ctx) {
    const submitHandler = createSubmitHandler(onEdit);

    ctx.render(createTemplate(submitHandler));

    async function onEdit(data) {
        if (Object.values(data).some(field => field == '')) {
            return showNotification('All fields are required');
        };

        const { title, description, imageUrl } = data; // TODO
        await create({ title, description, imageUrl }); // TODO

        ctx.page.redirect('/memes');
    };
};
