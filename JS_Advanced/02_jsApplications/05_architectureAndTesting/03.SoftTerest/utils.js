export function checkNav() {
    const token = localStorage.getItem('accessToken');
    if (token) {
        [...document.getElementsByClassName('guest')].forEach(li => li.style.display = 'none');
        [...document.getElementsByClassName('logged-user')].forEach(li => li.style.display = 'inline-block');
        return
    }
    [...document.getElementsByClassName('guest')].forEach(li => li.style.display = 'inline-block');
    [...document.getElementsByClassName('logged-user')].forEach(li => li.style.display = 'none');
};


export function getSection(id) {
    const section = document.getElementById(id);
    section.remove();
    return section;
};

export function loginFormIsValid(form) {
    const { email, password } = getFormData(form)
    if (!email || !password) {
        return false;
    };

    return true
}

export function registerFormIsValid(form) {
    const { email, password, repeatPassword } = getFormData(form)
    if (password != repeatPassword) {
        return false
    };
    if (email.length < 3 || password.length < 3) {
        return false;
    };

    return true
}

export function isIdeaFormValid(form) {
    const { title, description, imageURL } = getFormData(form);
    if (title.length < 6 || description.length < 10 || imageURL < 6) {
        return false;
    }

    return true;
}

export function getFormData(form) {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    return data;
}


export function setSession(userData) {
    localStorage.setItem('accessToken', userData.accessToken);
    localStorage.setItem('email', userData.email);
    localStorage.setItem('userId', userData._id);
}

export function clearSession() {
    localStorage.clear();
}