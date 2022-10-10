function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let searchField = document.getElementById("searchField");
      let searchWord = searchField.value;

      let tBody = document.getElementsByTagName("tbody")[0];
      let tableRows = Array.from(tBody.children);

      for (let row of tableRows) {
         row.classList.remove("select")
         let colElements = Array.from(row.children);
         for (let col of colElements) {
            if (col.textContent.includes(searchWord)) {
               row.classList.add("select");
               searchField.value = '';
               break;
            };
         };
      };
   }
}