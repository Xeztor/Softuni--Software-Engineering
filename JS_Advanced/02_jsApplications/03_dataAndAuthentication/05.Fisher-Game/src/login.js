if (sessionStorage.length !== 0) {
    document.querySelector("p.email span").textContent = sessionStorage.email;
} else {
    document.getElementById('user').style.display = 'none';
}


const form = document.getElementsByTagName('form')[0];
form.addEventListener('submit', login);

async function login(event) {
    event.preventDefault();
    const url = 'http://localhost:3030/users/login';
    const formData = new FormData(form);
    const { email, password } = Object.fromEntries(formData.entries());

    if (!email || !password) {
        return
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
        sessionStorage.setItem('userid', data._id)
        sessionStorage.setItem('accessToken', data.accessToken);
        window.location.replace('./index.html');
    } catch (error) {
        console.log('-------\n' + error + '\n--------');
    }

}