function lockedProfile() {
    // let profiles = document.getElementsByClassName("profile");
    let radioBtns = document.querySelectorAll('.profile input[type="radio"]');

    Array.from(radioBtns).forEach(radioBtn =>
        radioBtn.addEventListener('click', updateUserAccountStatus)
    );


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