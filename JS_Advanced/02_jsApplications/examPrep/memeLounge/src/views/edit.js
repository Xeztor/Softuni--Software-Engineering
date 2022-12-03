import { html } from '../lib.js';
import { editById, getById } from "../api/data.js";
import { createSubmitHandler } from "../util.js";
import { showNotification } from './notification.js';

const editTemplate = (item, onSubmit) => html`
<section id="edit-meme">
    <form @submit=${onSubmit} id="edit-form">
        <h1>Edit Meme</h1>
        <div class="container">
            <label for="title">Title</label>
            <input id="title" type="text" placeholder="Enter Title" name="title" .value=${item.title}>
            <label for="description">Description</label>
            <textarea id="description" placeholder="Enter Description" name="description"
                .value=${item.description}></textarea>
            <label for="imageUrl">Image Url</label>
            <input id="imageUrl" type="text" placeholder="Enter Meme ImageUrl" name="imageUrl" .value=${item.imageUrl}>
            <input type="submit" class="registerbtn button" value="Edit Meme">
        </div>
    </form>
</section>`; // TODO

export async function showEdit(ctx) {
    const meme = await getById(ctx.params.id);
    const submitHandler = createSubmitHandler(onEdit);

    ctx.render(editTemplate(meme, submitHandler));

    async function onEdit(data) {
        if (Object.values(data).some(field => field == '')) {
            return showNotification('All fields are required');
        };

        const { title, description, imageUrl } = data;
        await editById(meme._id, { title, description, imageUrl });

        ctx.page.redirect(`/memes/${meme._id}`);
    };
};