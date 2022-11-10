if (sessionStorage.length !== 0) {
    document.querySelector("p.email span").textContent = sessionStorage.email;
    document.getElementById('guest').style.display = 'none';
    document.getElementById('logout').addEventListener('click', logout);

    document.getElementById('addForm').addEventListener('submit', addCatch)
    document.querySelector('form#addForm button.add').disabled = false;
} else {
    document.getElementById('user').style.display = 'none';
    document.querySelector('form#addForm button.add').disabled = true;
}

document.querySelector('button.load').addEventListener('click', displayCatches);

async function displayCatches() {
    const url = "http://localhost:3030/data/catches";
    const response = await fetch(url);
    const catches = await response.json();

    const catchesDivs = [];
    for (let catchInfo of Object.values(catches)) {
        let div = document.createElement('div');
        div.classList.add('catch');
        div.innerHTML =
            `<label>Angler</label>` +
            `<input type="text" class="angler" value="${catchInfo.angler}">` +
            `<label>Weight</label>` +
            `<input type="text" class="weight" value="${catchInfo.weight}">` +
            `<label>Species</label>` +
            `<input type="text" class="species" value="${catchInfo.species}">` +
            `<label>Location</label>` +
            `<input type="text" class="location" value="${catchInfo.location}">` +
            `<label>Bait</label>` +
            `<input type="text" class="bait" value="${catchInfo.bait}">` +
            `<label>Capture Time</label>` +
            `<input type="number" class="captureTime" value="${catchInfo.captureTime}">` +
            `<button class="update" data-id="${catchInfo._id}">Update</button>` +
            `<button class="delete" data-id="${catchInfo._id}">Delete</button>`;

        let userId = sessionStorage.getItem('userid');
        if (userId === null || userId !== catchInfo._ownerId) {
            Array.from(div.querySelectorAll('input')).forEach(input => input.disabled = true);
            Array.from(div.querySelectorAll('button')).forEach(button => button.disabled = true);
        } else {
            div.getElementsByClassName('update')[0].addEventListener('click', updateCatchInfo);
            div.getElementsByClassName('delete')[0].addEventListener('click', deleteCatch);
        };

        catchesDivs.push(div);
        // document.getElementById('catches').appendChild(div)
    };

    document.getElementById('catches').replaceChildren(...catchesDivs);
};

async function addCatch(event) {
    event.preventDefault();
    const url = 'http://localhost:3030/data/catches/';
    const formData = new FormData(event.target);
    const { angler, weight, species, location, bait, captureTime } = Object.fromEntries(formData.entries());

    const token = sessionStorage.getItem('accessToken');
    await fetch(url, {
        method: 'post',
        headers: {
            "Content-Type": "application/json",
            "X-Authorization": token,
        },
        body: JSON.stringify({
            angler,
            weight,
            species,
            location,
            bait,
            captureTime
        })
    })

    displayCatches();
};


async function updateCatchInfo(event) {
    let id = event.target.dataset.id;
    const url = `http://localhost:3030/data/catches/${id}`;
    const token = sessionStorage.getItem('accessToken');

    let div = event.target.parentElement;
    const catchInfo = getCatchInfo(div)

    if (catchInfo === null) {
        return;
    }
    await fetch(url, {
        method: "put",
        headers: {
            "Content-Type": "application/json",
            "X-Authorization": token,
        },
        body: JSON.stringify({
            ...catchInfo,
        })
    });
};

function getCatchInfo(div) {
    let angler = div.getElementsByClassName('angler')[0].value;
    let weight = div.getElementsByClassName('weight')[0].value;
    let species = div.getElementsByClassName('species')[0].value;
    let location = div.getElementsByClassName('location')[0].value;
    let bait = div.getElementsByClassName('bait')[0].value;
    let captureTime = div.getElementsByClassName('captureTime')[0].value;

    if (!angler || !weight || !species || !location || !bait || !captureTime) {
        return null;
    }
    return { angler, weight, species, location, bait, captureTime }
}

async function deleteCatch(event) {
    let id = event.target.dataset.id;
    const url = `http://localhost:3030/data/catches/${id}`;
    const token = sessionStorage.getItem('accessToken');

    await fetch(url, {
        method: "delete",
        headers: {
            "X-Authorization": token,
        }
    });

    displayCatches();
};

async function logout() {
    const url = 'http://localhost:3030/users/logout';
    const token = sessionStorage.accessToken;
    try {
        const response = await fetch(url, {
            method: 'get',
            headers: {
                'X-Authorization': token,
            }
        })
        if (response.status === 204) {
            sessionStorage.clear();
        };
        window.location.replace('./index.html')
    } catch (error) {
        console.log('-------\n' + error + '\n--------');
    }
};