document.getElementById('loadBooks').addEventListener('click', renderBooks);
document.getElementsByTagName('form')[0].addEventListener('submit', createBook);

renderBooks();

const form = document.getElementsByTagName('form')[0];

async function renderBooks() {
    const url = 'http://localhost:3030/jsonstore/collections/books';
    const response = await fetch(url);
    const data = await response.json();

    renderTable(data);
};

function renderTable(data) {
    let rows = [];

    for (let [book_id, bookInfo] of Object.entries(data)) {
        let row = document.createElement('tr');
        row.innerHTML =
            `<td>${bookInfo.title}</td>` +
            `<td>${bookInfo.author}</td>` +
            `<td data-id="${book_id}">` +
            `<button>Edit</button>` +
            `<button>Delete</button>` +
            `</td>`;

        row.getElementsByTagName('button')[0].addEventListener('click', changeFormToEditMode);
        row.getElementsByTagName('button')[1].addEventListener('click', deleteBook);

        rows.push(row);
    };

    document.getElementsByTagName('tbody')[0].replaceChildren(...rows);
};

async function createBook(event) {
    event.preventDefault();
    const url = 'http://localhost:3030/jsonstore/collections/books';
    const formData = new FormData(form);
    const { title, author } = Object.fromEntries(formData.entries());

    await fetch(url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title,
            author
        })
    });

    renderBooks();
    cleanInputs();
};

function changeFormToEditMode(event) {
    form.getElementsByTagName('button')[0].textContent = 'Save';
    form.removeEventListener('submit', createBook);
    form.getElementsByTagName('h3')[0].textContent = "Edit FORM";

    let bookId = event.target.parentNode.dataset.id;
    form.addEventListener('submit', editBook.bind(null, bookId), false);

    let tr = event.target.parentNode.parentNode;

    let [title, author] = Array.from(tr.children).slice(0, 2).map(tdEl => tdEl.textContent);

    form.querySelector('input[name="title"]').value = title;
    form.querySelector('input[name="author"]').value = author;
}

function changeFormToCreateMode() {
    form.getElementsByTagName('button')[0].textContent = 'Submit';
    form.removeEventListener('submit', editBook);
    form.addEventListener('submit', createBook);
    form.getElementsByTagName('h3')[0].textContent = "FORM";
}

async function editBook(bookId, event) {
    const url = `http://localhost:3030/jsonstore/collections/books/${bookId}`;

    const formData = new FormData(form);
    const { title, author } = Object.fromEntries(formData.entries());

    await fetch(url, {
        method: 'put',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title,
            author,
        })
    });

    renderBooks();
    changeFormToCreateMode();
};

async function deleteBook(event) {
    let id = event.target.parentNode.dataset.id;
    const url = `http://localhost:3030/jsonstore/collections/books/${id}`;
    await fetch(url, {
        method: 'delete',
    });

    renderBooks();
}

function cleanInputs() {
    Array.from(document.querySelectorAll('input')).forEach(input => input.value = '');
}