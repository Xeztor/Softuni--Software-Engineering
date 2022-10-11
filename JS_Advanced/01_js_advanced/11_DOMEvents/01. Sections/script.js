function create(words) {
   let contentDiv = document.getElementById("content");

   for (let word of words) {
      let divEl = document.createElement('div');
      divEl.addEventListener('click', showText)

      let pEl = document.createElement('p');
      pEl.textContent = word
      pEl.style.display = 'none';
      divEl.appendChild(pEl);

      contentDiv.appendChild(divEl);
   };

   function showText(event) {
      let p = event.target.getElementsByTagName("p")[0];
      p.style.display = 'block';
   };
}