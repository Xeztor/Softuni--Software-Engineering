function solve() {
    document.getElementsByTagName('form')[0].addEventListener('click', (e) => e.preventDefault())

    document.getElementById('add').addEventListener('click', addTask);



    function addTask() {

        let taskName = document.getElementById('task').value;
        let taskDescription = document.getElementById("description").value;
        let date = document.getElementById("date").value;

        if (!taskName || !taskDescription || !date) {
            return;
        }

        let articleElement = document.createElement('article');
        articleElement.innerHTML =
            `<h3>${taskName}</h3>` +
            `<p>Description: ${taskDescription}</p>` +
            `<p>Due Date: ${date}</p>` +
            `<div class="flex">` +
            `<button class="green">Start</button>` +
            `<button class="red">Delete</button>` +
            `</div>`;

        document.querySelectorAll('section')[1].
            getElementsByTagName('div')[1].appendChild(articleElement);

        articleElement.addEventListener('click', clickHandler);
    };

    function clickHandler(e) {
        if (e.target.tagName !== "BUTTON") {
            return;
        };

        let command = (e.target.textContent).toLowerCase();

        switch (command) {
            case 'start': startTask(e); break;
            case 'delete': e.target.parentElement.parentElement.remove(); break;
            case 'finish': finishTask(e);
        }
    };

    function startTask(e) {
        let articleElement = e.target.parentElement.parentElement
        articleElement.remove()

        articleElement.querySelector('div.flex').innerHTML =
            `<button class="red">Delete</button>` +
            `<button class="orange">Finish</button>`;

        document.getElementById('in-progress').appendChild(articleElement);
    };

    function finishTask(e) {
        let eArticle = e.target.parentElement.parentElement;
        eArticle.remove()

        eArticle.getElementsByClassName('flex')[0].remove()

        document.querySelectorAll('section')[3].
            getElementsByTagName('div')[1].appendChild(eArticle);
    }

};