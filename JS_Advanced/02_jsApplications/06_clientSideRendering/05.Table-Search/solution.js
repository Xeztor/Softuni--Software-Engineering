import { render, html, nothing } from './node_modules/lit-html/lit-html.js'
document.querySelector('#searchBtn').addEventListener('click', onClick);

const url = 'http://localhost:3030/jsonstore/advanced/table';
const tableBodyRoot = document.getElementsByTagName('tbody')[0];


const tableRowTemplate = (user, matches) => html`
<tr class=${matches ?   
   "select" 
   : nothing}>
   <td>${user.firstName} ${user.lastName}</td>
   <td>${user.email}</td>
   <td>${user.course}</td>
</tr>
`;


renderTable()


function matches(user, searchStr){
   if (!searchStr){
      return false;
   };
   let searchPropsValues = [user.firstName, user.lastName, user.email, user.course];
   for (let propValue of searchPropsValues){
      if (propValue.toLowerCase().includes(searchStr)){
         return true
      }
   }
   return false
}

async function getData(){
   const response = await fetch(url);
   const data = await response.json();
   return Object.values(data);
}

async function renderTable(searchStr = null){
   const data = await getData();  

   let tableRows = [];
   data.forEach(user => {
      tableRows.push(tableRowTemplate(user, matches(user, searchStr)))
   });
   render(tableRows, tableBodyRoot);
}

function onClick() {
   const searchField = document.getElementById('searchField');
   const searchStr = searchField.value.toLowerCase();
   searchField.value = '';
   
   renderTable(searchStr);
}