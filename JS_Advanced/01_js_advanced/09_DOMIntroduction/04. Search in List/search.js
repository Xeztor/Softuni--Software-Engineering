function search() {
   let liElements = document.getElementsByTagName('li');
   let searchSubst = document.getElementById("searchText").value;
   let resultDiv = document.getElementById("result");

   let resultCount = 0;

   for (i = 0; i < liElements.length; i++) {
      if (liElements[i].textContent.includes(searchSubst)) {
         liElements[i].style.textDecoration = "underline";
         liElements[i].style.fontWeight = "bold";
         resultCount += 1;
      }
   };

   resultDiv.textContent = `${resultCount} matches found`

}
