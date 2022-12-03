import { getByUserId } from '../api/data.js';
import { html } from '../lib.js'

const profileTemplate = (user, memes) => html`
<section id="user-profile-page" class="user-profile">
    <article class="user-info">
        <img id="user-avatar-url" alt="user-profile" src="/images/${user.gender == 'male' ? 'male' : 'female'}.png">
        <div class="user-content">
            <p>Username: ${user.username}</p>
            <p>Email: ${user.email}</p>
            <p>My memes count: ${memes.length}</p>
        </div>
    </article>
    <h1 id="user-listings-title">User Memes</h1>
    <div class="user-meme-listings">
        ${memes.length == 0 ?
        html`<p class="no-memes">No memes in database.</p>`
        : memes.map(card)}
    </div>
</section>`;

const card = (item) => html`
<div class="user-meme">
    <p class="user-meme-title">${item.title}</p>
    <img class="userProfileImage" alt="meme-img" src=${item.imageUrl}>
    <a class="button" href="/memes/${item._id}">Details</a>
</div>`;

export async function showProfile(ctx) {
    const memes = await getByUserId(ctx.user._id);

    ctx.render(profileTemplate(ctx.user, memes))
}