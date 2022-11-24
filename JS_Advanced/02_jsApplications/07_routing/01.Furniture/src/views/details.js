import { deleteFurnitureById, getFurnitureById } from '../api/data.js';
import { html, nothing } from '../lib.js'
import { getUserData } from '../util.js';

const detailsTemplate = (furniture, isOwner, onDelete) => html`
<div class="container">
    <div class="row space-top">
        <div class="col-md-12">
            <h1>Furniture Details</h1>
        </div>
    </div>
    <div class="row space-top">
        <div class="col-md-4">
            <div class="card text-white bg-primary">
                <div class="card-body">
                    <img src="../../${furniture.img}" />
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <p>Make: <span>${furniture.make}</span></p>
            <p>Model: <span>${furniture.model}</span></p>
            <p>Year: <span>${furniture.year}</span></p>
            <p>Description: <span>${furniture.description}</span></p>
            <p>Price: <span>${furniture.price}</span></p>
            <p>Material: <span>${furniture.material}</span></p>
            ${isOwner ? 
                html`
                <div>
                    <a href="/catalog/edit/${furniture._id}" class="btn btn-info">Edit</a>
                    <a @click=${onDelete} href="javascript:void(0)" class="btn btn-red">Delete</a>
                </div>`
                : nothing}
        </div>
    </div>
</div>`;

export async function showDetails(ctx) {
    const furniture = await getFurnitureById(ctx.params.id);

    const user = getUserData()
    const isOwner = user ? user._id == furniture._ownerId : false;
    
    ctx.render(detailsTemplate(furniture, isOwner, onDelete))

    async function onDelete(){
        const confirmation = confirm('Do you really want to delete this item ?');
        if (confirmation === false){
            return
        }

        await deleteFurnitureById(furniture._id)
        ctx.page.redirect('/')
    }
} 