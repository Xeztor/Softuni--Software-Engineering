function validate() {
    document.getElementById('registerForm').addEventListener('submit', disableFormRefreshPage);
    document.getElementById('registerForm').addEventListener('submit', validateForm);

    document.getElementById('company').addEventListener('change', toggleVisible)

    const regExpEnum = {
        "username": new RegExp(/[a-z\d]{3,20}/),
        "email": new RegExp(/[a-zA-Z\d]+@[a-zA-Z\d]+\.[a-zA-Z\d\.]+/),
        "password": new RegExp(/[\w]{5,15}/),
        "confirm-password": new RegExp(/[\w]{5,15}/),
        "companyNumber": new RegExp(/^[1-9][0-9][0-9][0-9]$/),
    }

    function disableFormRefreshPage(e) {
        e.preventDefault();
    };

    function validateForm(e) {
        let username = e.target.querySelector('#username');
        let email = e.target.querySelector('#email');
        let password = e.target.querySelector('#password');
        let confirmPassowrd = e.target.querySelector('#confirm-password');

        let inputsToValidate = [username, email, password, confirmPassowrd];

        let invalidFields = [];

        let isCompanyChecked = document.getElementById('company').checked;
        if (isCompanyChecked) {
            inputsToValidate.push(document.getElementById('companyNumber'));
        };

        for (let input of inputsToValidate) {
            let regexToTest = regExpEnum[input.id]
            if (!regexToTest.test(input.value)) {
                invalidFields.push(input);
            };
        };

        for (let input of inputsToValidate) {
            input.style.border = 'none';
        };

        if (password.value !== confirmPassowrd.value) {
            invalidFields.push(password);
            invalidFields.push(confirmPassowrd);
        };

        if (invalidFields.length !== 0) {
            document.getElementById('valid').style.display = 'none';
            for (let field of invalidFields) {
                field.style.border = 'solid'
                field.style.borderColor = 'red';
            };
            return
        };

        document.getElementById('valid').style.display = 'block';

    };

    function toggleVisible(e) {
        let companyFieldset = document.getElementById("companyInfo");
        if (e.target.checked === true) {
            companyFieldset.style.display = 'block';
            return;
        };
        companyFieldset.style.display = 'none';
    };
}
