import { html, render } from "./node_modules/lit-html/lit-html.js";
import { cats } from "./catSeeder.js";


const root = document.getElementsByTagName('ul')[0];
root.addEventListener('click', toggleInfo);

const allCats = cats;

const catTemplate = (cat) => html`
<li>
    <img src="./images/${cat.imageLocation}.jpg" width="250" height="250" alt="Card image cap">
    <div class="info">
        <button class="showBtn">Show status code</button>
        <div class="status" style="display: none" id="${cat.id}">
            <h4>Status Code: ${cat.statusCode}</h4>
            <p>${cat.statusMessage}</p>
        </div>
    </div>
</li>
`

render(allCats.map(catTemplate), root);



function toggleInfo(event) {
    if (event.target.classList.contains('showBtn') === false) {
        return;
    }
    const parent = event.target.parentElement;
    const div = parent.getElementsByClassName('status')[0];
    if (div.style.display === 'none') {
        event.target.textContent = 'Hide status code';
        div.style.display = 'block';
    } else {
        event.target.textContent = 'Show status code';
        div.style.display = 'none';
    }

}