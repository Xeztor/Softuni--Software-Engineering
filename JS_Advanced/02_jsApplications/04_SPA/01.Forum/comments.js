document.getElementsByTagName('form')[1].addEventListener('submit', postComment);

export async function commentsView(topicId) {
    [...document.querySelectorAll('.container')].forEach(div => div.style.display = 'none');

    const topicData = await getTopic(topicId);

    document.querySelectorAll('.container')[1].style.display = 'block';

    renderTopic(topicData);
}

async function getTopic(topicId) {
    const url = `http://localhost:3030/jsonstore/collections/myboard/posts/${topicId}`;
    const response = await fetch(url);
    const topic = await response.json();
    return topic;
}

async function renderTopic(topic) {
    let titleElement = document.querySelector('.theme-name h2');
    titleElement.textContent = topic.topicName;

    let parentDiv = document.getElementsByClassName('comment')[0];
    parentDiv.dataset.id = topic._id;

    let headerDiv = document.createElement('div');
    headerDiv.innerHTML =
        `<div class="header">` +
        `<img src="./static/profile.png" alt="avatar">` +
        `<p><span>${topic.author}</span> posted on <time>${topic.createdOn}</time></p>` +
        `<p class="post-content">${topic.postText}</p>` +
        `</div>`;

    parentDiv.replaceChildren(headerDiv);

    renderComments();

}


async function renderComments() {
    let commentDiv = document.getElementsByClassName('comment')[0];

    clearComments();
    let commentsArr = await getComments();
    let commentsElements = commentsArr.map(createCommentDiv)
    commentsElements.forEach(comment => commentDiv.appendChild(comment));

}

async function getComments() {
    let topicId = document.getElementsByClassName('comment')[0].dataset.id;
    const topicCommentsUrl = `http://localhost:3030/jsonstore/collections/myboard/posts/${topicId}/comments`;
    const commentsResponse = await fetch(topicCommentsUrl);
    let commentsIds = await commentsResponse.json();
    commentsIds = [...commentsIds];

    const baseUrl = 'http://localhost:3030/jsonstore/collections/myboard/comments';
    let commentsArr = [];
    for (let commentId of commentsIds) {
        const response = await fetch(baseUrl + `/${commentId}`);
        const comment = await response.json();
        commentsArr.push(comment);
    };
    return commentsArr;

}

function createCommentDiv(comment) {
    const div = document.createElement('div');
    div.classList.add('user-comment');
    div.innerHTML =
        `<div class="topic-name-wrapper">` +
        `<div class="topic-name">` +
        `<p><strong>${comment.username}</strong> commented on <time>${comment.createdOn}</time></p>` +
        `<div class="post-content">` +
        `<p>${comment.text}</p>` +
        `</div>` +
        `</div>` +
        `</div>`;

    return div;
}


async function postComment(event) {
    event.preventDefault();
    if (!isFormValid(event.target)) {
        return
    };
    const body = getPostBody(event.target);

    const url = 'http://localhost:3030/jsonstore/collections/myboard/comments';
    const response = await fetch(url, {
        method: 'post',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify(body)
    });

    const comment = await response.json();

    clearFields(event.target);
    await updateTopicComments(comment);
    renderComments();

}

async function updateTopicComments(comment) {
    let topicId = document.getElementsByClassName('comment')[0].dataset.id;
    const topicUrl = `http://localhost:3030/jsonstore/collections/myboard/posts/${topicId}`;
    const response = await fetch(topicUrl);
    let topic = await response.json();

    let comments = topic.comments;
    comments.push(comment._id);
    const body = {
        ...topic
    }

    await fetch(topicUrl, {
        method: 'put',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify(body)
    });
};

function clearComments() {
    [...document.querySelectorAll('div.user-comment')].forEach(comment => comment.remove());
}

function isFormValid(form) {
    let formData = new FormData(form);
    let { postText, username } = Object.fromEntries(formData.entries());
    if (!postText || !username) {
        return false;
    };

    return true;
}

function getPostBody(form) {
    let formData = new FormData(form);
    let { postText, username } = Object.fromEntries(formData.entries());
    let createdOn = new Date();
    return { text: postText, username, createdOn };
}

function clearFields(form) {
    [...form.querySelectorAll('input')].forEach(i => i.value = '');
    form.querySelector('textarea').value = '';
}