import { html, nothing } from '../lib.js'
export const cardTemplate = (item, userIsLogged) => html`
<div class="card-box">
    <img src="${item.imgUrl}">
    <div>
        <div class="text-center">
            <p class="name">Name: ${item.name}</p>
            <p class="artist">Artist: ${item.artist}</p>
            <p class="genre">Genre: ${item.genre}</p>
            <p class="price">Price: $${item.price}</p>
            <p class="date">Release Date: ${item.releaseDate}</p>
        </div>
        ${userIsLogged? 
        html`
        <div class="btn-group">
            <a href="/catalog/${item._id}" id="details">Details</a>
        </div>`
        : nothing}
        
    </div>
</div>`;