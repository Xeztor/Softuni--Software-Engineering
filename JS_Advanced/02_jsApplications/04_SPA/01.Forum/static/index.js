import { commentsView } from './comments.js';

document.getElementsByTagName('form')[0].addEventListener('submit', formSubmit);


export async function topicsView() {
    [...document.querySelectorAll('.container')].forEach(div => div.style.display = 'none');

    const topicsArr = await getTopics();

    document.querySelectorAll('.container')[0].style.display = 'block';

    renderTopics(topicsArr);
}

function renderTopics(topicsArr) {
    const mainEl = document.getElementsByTagName('main')[0];

    clearTopics()
    let topicsElements = topicsArr.map(createTopicElement);
    topicsElements.forEach(topic => mainEl.appendChild(topic));
}


function createTopicElement(topic) {
    let div = document.createElement('div');
    div.classList.add('topic-container');
    div.innerHTML =
        `<div class="topic-name-wrapper">` +
        `<div class="topic-name">` +
        ` <a href="javascript:void(0)" class="normal">` +
        `<h2>${topic.topicName}</h2>` +
        `</a>` +
        `<div class="columns">` +
        `<div>` +
        `<p>Date: <time>${topic.createdOn}</time></p>` +
        `<div class="nick-name">` +
        `<p>Username: <span>${topic.author}</span></p>` +
        `</div>` +
        `</div>` +
        `</div>` +
        `</div>` +
        `</div>`;

    div.getElementsByTagName('a')[0].addEventListener('click', commentsView.bind(null, topic._id), false);
    return div;
}

async function getTopics() {
    const url = 'http://localhost:3030/jsonstore/collections/myboard/posts';

    const response = await fetch(url);
    const topics = await response.json();

    let topicsArr = Object.values(topics);
    return topicsArr;
};


async function formSubmit(event) {
    event.preventDefault();
    if ([...event.submitter.classList].includes('cancel')) {
        clearFields(event.target);
        return;
    };

    const formData = new FormData(event.target);
    if (formIsValid(formData) === false) {
        return;
    };

    const { topicName, username, postText } = Object.fromEntries(formData.entries());
    const fetchBody = { topicName, author: username, postText, createdOn: new Date(), comments: [] };
    await postTopic(fetchBody);

    clearFields(event.target);
    topicsView();
}

async function postTopic(body) {
    const url = 'http://localhost:3030/jsonstore/collections/myboard/posts';

    await fetch(url, {
        method: 'post',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(body)
    })
}

function formIsValid(form) {
    const { topicName, username, postText } = Object.fromEntries(form.entries());

    if (!topicName || !username || !postText) {
        return false;
    };

    return true;
}

function clearFields(form) {
    [...form.querySelectorAll('input')].forEach(i => i.value = '');
    form.querySelector('textarea').value = '';
}


function clearTopics() {
    [...document.querySelectorAll('.topic-container')].forEach(container => container.remove());
}