async function lockedProfile() {
    const url = 'http://localhost:3030/jsonstore/advanced/profiles'
    try {
        const response = await fetch(url);

        if (response.ok === false) {
            throw new Error('Bad Response');
        };

        const profiles = await response.json();
        for (let id in profiles) {
            let profile = profiles[id];
            let profileCard = createProfileCard(profile);
            document.getElementById('main').appendChild(profileCard);
        };
    } catch (err) { }

    function createProfileCard(profile) {
        let div = document.createElement('div');
        div.classList.add('profile');

        div.innerHTML =
            `<img src="./iconProfile2.png" class="userIcon" />` +
            `<label>Lock</label>` +
            `<input type="radio" name="user1Locked" value="lock" checked>` +
            `<label>Unlock</label>` +
            `<input type="radio" name="user1Locked" value="unlock"><br>` +
            `<hr>` +
            `<label>Username</label>` +
            `<input type="text" name="user1Username" value="${profile.username}" disabled readonly />` +
            `<div class="user1Username" style="display: none">` +
            `<hr>` +
            `<label>Email:</label>` +
            `<input type="email" name="user1Email" value="${profile.email}" disabled readonly />` +
            `<label>Age:</label>` +
            `<input type="text" name="user1Age" value="${profile.age}" disabled readonly />` +
            `</div>` +
            `<button>Show more</button>`

        let radioBtns = div.querySelectorAll('input[type="radio"]');
        Array.from(radioBtns).forEach(radioBtn =>
            radioBtn.addEventListener('click', updateUserAccountStatus)
        );

        return div;
    };



    function updateUserAccountStatus(event) {
        let profile = event.target.parentNode;
        let showMoreBtn = profile.getElementsByTagName('button')[0];
        if (event.target.value == 'lock') {
            showMoreBtn.removeEventListener('click', showMoreLess);
            return;
        };
        showMoreBtn.addEventListener('click', showMoreLess);
    };

    function showMoreLess(event) {
        let profile = event.target.parentNode;
        let hiddenInfo = profile.getElementsByTagName("div")[0];

        if (event.target.textContent === 'Show more') {
            hiddenInfo.style.display = 'block';
            event.target.textContent = 'Hide it';
            return;
        }
        hiddenInfo.style.display = 'none';
        event.target.textContent = 'Show more';
    };
}