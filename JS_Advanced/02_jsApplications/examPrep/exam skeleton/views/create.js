import { html } from '../lib.js'
import { create } from "../api/data.js"
import { createSubmitHandler } from "../util.js";

const createTemplate = (onSubmit) => html`
`; // TODO

export async function showCreate(ctx) {
    const submitHandler = createSubmitHandler(onEdit);

    ctx.render(createTemplate(submitHandler));

    async function onEdit(data) {
        if (Object.values(data).some(field => field == '')) {
            return alert('All fields are required');
        };

        const { make, model, year, description, price, img, material } = data; // TODO
        await create({ make, model, year, description, price, img, material }); // TODO

        ctx.page.redirect('/');
    };
};
