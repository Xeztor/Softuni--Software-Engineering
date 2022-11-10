document.getElementById('form').addEventListener('submit', createRecord);

const studentsURL = 'http://localhost:3030/jsonstore/collections/students'

renderTable();

async function renderTable() {
    const tableBody = document.getElementsByTagName('tbody')[0];
    try {
        const response = await fetch(studentsURL);
        const data = await response.json();

        let tableRows = createTableRows(Object.values(data));
        tableBody.replaceChildren(...tableRows);

    } catch (error) {

    }
}

function createTableRows(studentsInfo) {
    let rows = [];
    for (let student of studentsInfo) {
        let tr = document.createElement('tr');
        let tds = Object.values(student).slice(0, student.size).map(value => {
            let td = document.createElement('td');
            td.textContent = value;
            return td;
        })
        tds.splice(tds.length - 1, 1)
        tr.replaceChildren(...tds);
        rows.push(tr);
    };
    return rows;
};

async function createRecord(event) {
    event.preventDefault();

    let formElement = document.getElementsByTagName('form')[0];
    let form = new FormData(formElement);
    let { firstName, lastName, facultyNumber, grade } = Object.fromEntries(form.entries());

    try {
        const response = await fetch(studentsURL, {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                firstName,
                lastName,
                facultyNumber,
                grade
            })
        })

        const data = response.json();

        renderTable()
    } catch (error) {
        console.log('--------\n' + error + '\n--------');
    }

};