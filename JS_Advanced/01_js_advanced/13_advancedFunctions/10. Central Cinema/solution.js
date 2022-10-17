function solve() {
    document.getElementsByTagName('button')[0].addEventListener('click', addMovie);

    function addMovie() {
        let inputs = document.querySelectorAll('#container input');
        let movieName = inputs[0].value;
        let hall = inputs[1].value;
        let price = Number(inputs[2].value);

        if (!movieName || !hall || typeof (price) !== 'number') {
            return
        };

        let liEl = document.createElement('li');
        liEl.innerHTML =
            `<span>${movieName}</span>` +
            `<strong>Hall: ${hall}</strong>` +
            `<div>` +
            `<strong>price</strong>` +
            `<input placeholder="Tickets Sold">` +
            `<button>Archive</button>` +
            `</div>`

        document.querySelector('#movies ul').appendChild(liEl);
    }

}