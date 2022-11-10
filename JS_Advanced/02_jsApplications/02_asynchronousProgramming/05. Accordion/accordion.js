function solution() {
    buildPage()

    async function buildPage() {
        const url = 'http://localhost:3030/jsonstore/advanced/articles/list'
        try {
            const response = await fetch(url);
            if (response.ok === false) {
                throw new Error('Bad Response');
            };
            const data = await response.json();

            for (let article of data) {
                let div = document.createElement('div');
                div.classList.add('accordion');

                div.innerHTML =
                    `<div class="head">` +
                    `<span>${article.title}</span>` +
                    `<button class="button" id="${article._id}">More</button>` +
                    `</div>` +
                    `<div class="extra" style="display: none">` +
                    `</div>`;

                div.getElementsByTagName('button')[0].addEventListener('click', toggleInfo);
                document.getElementById('main').appendChild(div);
            };
        } catch (err) {
            console.log(err);
        };
    };

    async function toggleInfo(event) {
        const url = `http://localhost:3030/jsonstore/advanced/articles/details/${event.target.id}`;
        let pExist = event.target.parentNode.parentNode.querySelector('p') !== null ? true : false;
        if (!pExist) {
            try {
                const response = await fetch(url);
                if (response.ok === false) {
                    throw new Error("Bad Response");
                };
                const data = await response.json();

                let p = document.createElement('p');
                p.textContent = data.content;
                event.target.parentNode.parentNode.querySelector('.extra').appendChild(p);

            } catch (err) {
                console.log(err);
            }

        };


        toggleInfoDiv(event)

    }

    function toggleInfoDiv(event) {
        let extraDiv = event.target.parentNode.parentNode.querySelector('.extra');
        if (extraDiv.style.display === 'none') {
            extraDiv.style.display = 'block';
            event.target.textContent = 'Show Less';
            return
        };

        extraDiv.style.display = 'none';
        event.target.textContent = 'More';
    }
}

solution()