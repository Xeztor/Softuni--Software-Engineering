import { getCurrentUserPublications } from '../api/data.js';
import { html } from '../lib.js'

const catalogTemplate = (items) => html`
<div class="container">
    <div class="row space-top">
        <div class="col-md-12">
            <h1>My Furniture</h1>
            <p>This is a list of your publications.</p>
        </div>
    </div>
    <div class="row space-top">
        ${items.map(furnitureCard)}
    </div>
</div>`;

const furnitureCard = (item) => html`
<div class="col-md-4">
    <div class="card text-white bg-primary">
        <div class="card-body">
            <img src="./images/table.png" />
            <p>${item.description}</p>
            <footer>
                <p>Price: <span>${item.price}</span></p>
            </footer>
            <div>
                <a href="/catalog/${item._id}" class="btn btn-info">Details</a>
            </div>
        </div>
    </div>
</div>`;

export async function showMyFurniture(ctx) {
    const items = await getCurrentUserPublications();

    ctx.render(catalogTemplate(items))
};