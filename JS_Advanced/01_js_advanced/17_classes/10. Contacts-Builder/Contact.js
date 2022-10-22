class Contact {
    constructor(firstName, lastName, phone, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.email = email;
        this.articleEl = this.createArticleElement();
        this.online = false;
    }

    get online() {
        return this._online;
    }

    set online(value) {
        this._online = value
        this.articleEl.getElementsByClassName('title')[0].classList.toggle('online')
    };

    createArticleElement() {
        let articleEl = document.createElement('article');
        articleEl.innerHTML =
            `<div class="title online">${this.firstName} ${this.lastName}` +
            `<button>&#8505;</button>` +
            `</div>` +
            `<div class="info">` +
            `<span>&phone; ${this.phone}</span>` +
            `<span>&#9993; ${this.email}</span>` +
            `</div>`;
        articleEl.getElementsByClassName('info')[0].style.display = 'none';

        articleEl.getElementsByTagName('button')[0].addEventListener('click', this.toggleInfo);

        return articleEl
    }

    toggleInfo(e) {
        let div = e.target.parentNode.parentNode.getElementsByClassName('info')[0];
        if (div.style.display === 'none') {
            div.style.display = 'block';
            return
        }
        div.style.display = 'none';
    }

    render(id) {
        document.getElementById(id).appendChild(this.articleEl);
    }
}

/*
<article>
    <div class="title">{firstName lastName}<button>&#8505;</button></div>
    <div class="info">
        <span>&phone; {phone}</span>
        <span>&#9993; {email}</span>
    </div>
</article>
*/