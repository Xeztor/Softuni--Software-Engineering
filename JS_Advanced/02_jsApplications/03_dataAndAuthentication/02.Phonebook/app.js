function attachEvents() {
    document.getElementById('btnCreate').addEventListener('click', createPhonebookEntry);
    document.getElementById('btnLoad').addEventListener('click', dsiplayPhonebookEntry);

    async function dsiplayPhonebookEntry() {
        const url = 'http://localhost:3030/jsonstore/phonebook';
        try {
            const response = await fetch(url);
            const data = await response.json();

            let listItems = [];
            for (let entry of Object.values(data)) {
                let li = document.createElement('li');
                li.textContent = `${entry.person}: ${entry.phone}`
                let deleteBtn = document.createElement('button');
                deleteBtn.id = entry._id;
                deleteBtn.textContent = 'Delete';
                deleteBtn.addEventListener('click', deletePhonebookEntry);
                li.appendChild(deleteBtn);
                listItems.push(li);
            };

            document.getElementById('phonebook').replaceChildren(...listItems);

        } catch (error) {
            console.log('--------\n' + error + '\n--------');
        };
    };

    async function createPhonebookEntry() {
        const url = 'http://localhost:3030/jsonstore/phonebook';
        let person = document.getElementById('person').value;
        let phone = document.getElementById('phone').value;
        try {
            const response = await fetch(url, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    person,
                    phone
                }),
            });
            const data = await response.json();

            document.getElementById('person').value = '';
            document.getElementById('phone').value = '';
            dsiplayPhonebookEntry();

        } catch (error) {
            console.log('--------\n' + error + '\n--------');
        };
    };

    async function deletePhonebookEntry(event) {
        const url = `http://localhost:3030/jsonstore/phonebook/${event.target.id}`;

        try {
            const response = await fetch(url, {
                method: 'delete',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();

            dsiplayPhonebookEntry()
        } catch (error) {
            console.log('--------\n' + error + '\n--------');
        };
    };
}

attachEvents();