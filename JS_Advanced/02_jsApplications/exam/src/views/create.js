import { html } from '../lib.js'
import { create } from "../api/data.js"
import { createSubmitHandler } from "../util.js";

const createTemplate = (onSubmit) => html`
<section id="create">
    <div class="form">
        <h2>Add Album</h2>
        <form @submit=${onSubmit} class="create-form">
            <input type="text" name="singer" id="album-singer" placeholder="Singer/Band" />
            <input type="text" name="album" id="album-album" placeholder="Album" />
            <input type="text" name="imageUrl" id="album-img" placeholder="Image url" />
            <input type="text" name="release" id="album-release" placeholder="Release date" />
            <input type="text" name="label" id="album-label" placeholder="Label" />
            <input type="text" name="sales" id="album-sales" placeholder="Sales" />

            <button type="submit">post</button>
        </form>
    </div>
</section>`;

export async function showCreate(ctx) {
    const submitHandler = createSubmitHandler(onEdit);

    ctx.render(createTemplate(submitHandler));

    async function onEdit(data) {
        if (Object.values(data).some(field => field == '')) {
            return alert('All fields are required');
        };

        const { singer, album: albumName, imageUrl, release, label, sales } = data;
        await create({ singer, album: albumName, imageUrl, release, label, sales });

        ctx.page.redirect('/dashboard');
    };
};
