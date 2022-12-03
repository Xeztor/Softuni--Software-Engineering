import { deleteById, getById } from '../api/data.js';
import { albumLikes, hasUserLiked, likeAlbum } from '../api/like.js';
import { html, nothing } from '../lib.js'

const detailsTemplate = (item, isOwner, canLike, likes, onDelete, onLike) => html`
<section id="details">
    <div id="details-wrapper">
        <p id="details-title">Album Details</p>
        <div id="img-wrapper">
            <img src="${item.imageUrl}" alt="example1" />
        </div>
        <div id="info-wrapper">
            <p><strong>Band:</strong><span id="details-singer">${item.singer}</span></p>
            <p>
                <strong>Album name:</strong><span id="details-album">${item.album}</span>
            </p>
            <p><strong>Release date:</strong><span id="details-release">${item.release}</span></p>
            <p><strong>Label:</strong><span id="details-label">${item.label}</span></p>
            <p><strong>Sales:</strong><span id="details-sales">${item.sales}</span></p>
        </div>
        <div id="likes">Likes: <span id="likes-count">${likes}</span></div>

        <!--Edit and Delete are only for creator-->
        <div id="action-buttons">
        ${isOwner ? 
        html`
        <a href="/dashboard/edit/${item._id}" id="edit-btn">Edit</a>
        <a @click=${onDelete} href="javascript:void(0)" id="delete-btn">Delete</a>`
        :nothing}
        ${canLike ?
        html`<a @click=${onLike} href="" id="like-btn">Like</a>`
        : nothing}
        </div>
    </div>
</section>`;

export async function showDetails(ctx) {
    const album = await getById(ctx.params.id);

    const user = ctx.user;
    const isOwner = user ? user._id == album._ownerId : false;

    let canLike = false;
    if (user && isOwner == false){
        const userHasLiked = await hasUserLiked(user._id, album._id);
        if (userHasLiked == 0) {
            canLike = true;
        }
    }
    const likes = await albumLikes(album._id);

    ctx.render(detailsTemplate(album, isOwner, canLike, likes, onDelete, onLike));

    async function onDelete() {
        const confirmation = confirm('Do you really want to delete this item ?');
        if (confirmation === false) {
            return;
        }

        await deleteById(album._id);
        ctx.page.redirect('/dashboard');
    }

    async function onLike(){
        await likeAlbum(album._id);
        ctx.page.redirect(`/dashboard/${album._id}`)
    }
} 