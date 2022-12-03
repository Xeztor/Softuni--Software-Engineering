import { html } from '../lib.js'
import { editById, getById } from "../api/data.js"
import { createSubmitHandler } from "../util.js";

const editTemplate = (item, onSubmit) => html`
`; // TODO

export async function showEdit(ctx) {
    const furniture = await getById(ctx.params.id); // TODO rename
    const submitHandler = createSubmitHandler(onEdit);

    ctx.render(editTemplate(furniture, submitHandler)); // TODO rename

    async function onEdit(data) {
        if (Object.values(data).some(field => field == '')) {
            return alert('All fields are required');
        };

        const { make, model, year, description, price, img, material } = data; // TODO fieldnames
        await editById(furniture._id, { make, model, year, description, price, img, material }) // TODO rename and fieldnames

        ctx.page.redirect(`/catalog/${furniture._id}`) // TODO
    };
};