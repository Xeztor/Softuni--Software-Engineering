if (sessionStorage.getItem('email') !== null) {
    document.querySelector("p.email span").textContent = sessionStorage.email;
} else {
    document.getElementById('user').style.display = 'none';
}

const form = document.getElementsByTagName('form')[0];
form.addEventListener('submit', register);

async function register(event) {
    event.preventDefault();
    const url = 'http://localhost:3030/users/register';
    const formData = new FormData(form);
    const { email, password, rePass } = Object.fromEntries(formData.entries());

    if (password !== rePass) {
        document.getElementsByClassName('notification')[0].textContent = 'Passwords don\'t match';
        return;
    };
    try {
        const response = await fetch(url, {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email,
                password
            })
        });
        const data = await response.json();

        if (response.ok === false) {
            document.getElementsByClassName('notification')[0].textContent = data.message;
            return;
        };

        sessionStorage.setItem('email', email)
        sessionStorage.setItem('accessToken', data.accessToken);
        window.location.replace('./index.html');
    } catch (error) {
        console.log('-------\n' + error + '\n--------');
    }

}