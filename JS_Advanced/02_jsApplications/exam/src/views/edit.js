import { html } from '../lib.js'
import { editById, getById } from "../api/data.js"
import { createSubmitHandler } from "../util.js";

const editTemplate = (item, onSubmit) => html`
<section id="edit">
    <div class="form">
        <h2>Edit Album</h2>
        <form @submit=${onSubmit} class="edit-form">
            <input type="text" name="singer" id="album-singer" placeholder="Singer/Band" .value=${item.singer} />
            <input type="text" name="album" id="album-album" placeholder="Album" .value=${item.album} />
            <input type="text" name="imageUrl" id="album-img" placeholder="Image url" .value=${item.imageUrl} />
            <input type="text" name="release" id="album-release" placeholder="Release date" .value=${item.release} />
            <input type="text" name="label" id="album-label" placeholder="Label" .value=${item.label} />
            <input type="text" name="sales" id="album-sales" placeholder="Sales" .value=${item.sales} />

            <button type="submit">post</button>
        </form>
    </div>
</section>`;

export async function showEdit(ctx) {
    const album = await getById(ctx.params.id);
    const submitHandler = createSubmitHandler(onEdit);

    ctx.render(editTemplate(album, submitHandler));

    async function onEdit(data) {
        if (Object.values(data).some(field => field == '')) {
            return alert('All fields are required');
        };

        const { singer, album: albumName, imageUrl, release, label, sales } = data; // TODO fieldnames
        await editById(album._id, { singer, album: albumName, imageUrl, release, label, sales }) // TODO rename and fieldnames

        ctx.page.redirect(`/dashboard`);
    };
};