function validate() {
    document.getElementById('email').addEventListener('change', validateEmail);

    let validateEmailRegEx = new RegExp(/[a-z]+@[a-z]+\.[a-z]+/);

    function validateEmail(e) {
        if (!validateEmailRegEx.test(e.target.value)) {
            e.target.classList.add('error');
            return;
        };
        e.target.classList.remove('error');
    }
}