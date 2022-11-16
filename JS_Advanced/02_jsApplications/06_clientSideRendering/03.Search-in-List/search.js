import { html, render } from './node_modules/lit-html/lit-html.js'
import { nothing } from './node_modules/lit-html/lit-html.js'
import { towns } from './towns.js';

document.getElementsByTagName('button')[0].addEventListener('click', search);

const listRoot = document.getElementById('towns');
const resultRoot = document.getElementById('result');

const townsList = towns;


const listTemplate = (searchStr) => html`
<ul>
   ${townsList.map(
      (townName) => html`<li class=${match(searchStr, townName) ? 'active' : nothing}>${townName}</li>`
   )}
</ul>
`;

const resultTemplate = (matches) => html`
${matches? 
   `${matches} matches found` 
   :'0 matches found'}`;


render(listTemplate(), listRoot);


function match(searchStr, str) {
   if (!searchStr){
      return false
   }

   if (str.trim().includes(searchStr.trim())) {
      return true
   };
   return false;
}

function getMatches(list, matchstr){
   let matches = list.filter(item => item.includes(matchstr))
   return matches;
};

function search() {
   const searchString = document.getElementById('searchText').value;
   render(listTemplate(searchString), listRoot);

   const matches = getMatches(townsList, searchString);
   resultRoot.textContent = `${matches.length} matches found`
}
