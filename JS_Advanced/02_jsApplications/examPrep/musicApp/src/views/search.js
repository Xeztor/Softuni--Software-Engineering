import { catalogSearch } from '../api/data.js';
import { html, nothing   } from '../lib.js';
import { createSubmitHandler } from '../util.js';
import { cardTemplate } from './card.js'

const searchTemplate = (onSubmit, data, userIsLogged) => html`
<section id="searchPage">
    <h1>Search by Name</h1>

    <div class="search">
        <form @submit=${onSubmit}>
            <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name">
            <button class="button-list">Search</button>
        </form>
    </div>

    <h2>Results:</h2>

    ${data !== undefined ? 
    cardsTemplate(data, userIsLogged)
    : nothing}
</section>`;

const cardsTemplate = (data, userIsLogged) => html`
<div class="search-result">
${data == null ? 
    html`<p class="no-result">No result.</p>`
    : data.map(item => cardTemplate(item, userIsLogged))}
</div>`;
 
export async function showSearch(ctx) {
    let data;
    if (ctx.query.search) {
        const search = await catalogSearch(ctx.query.search);
        data = search.length == 0 ? null : search;
    };

    const userIsLogged = ctx.user ? true : false;
    ctx.render(searchTemplate(createSubmitHandler(onSubmit), data, userIsLogged));

    async function onSubmit({ search }) {
        ctx.page.redirect('/search' + `?search=${search}`)
        // const data = await catalogSearch(search); //TODO
    }
}