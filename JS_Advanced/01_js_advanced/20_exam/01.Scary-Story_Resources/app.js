window.addEventListener("load", solve);

function solve() {
  document.getElementById('form-btn').addEventListener('click', submitForm)


  function submitForm(e) {
    let firstName = document.getElementById('first-name').value;
    let lastName = document.getElementById('last-name').value;
    let age = document.getElementById('age').value;
    let storyTitle = document.getElementById('story-title').value;
    let genre = document.getElementById('genre').value;
    let story = document.getElementById('story').value;

    if (!firstName || !lastName || !age || !storyTitle || !genre || !story) {
      return;
    };

    let liArticle = createArticle(firstName, lastName, age, storyTitle, genre, story);

    document.getElementById('preview-list').appendChild(liArticle);

    e.target.disabled = true;

    enablePreviewButtons()

    Array.from(document.querySelectorAll('.section input'))
      .forEach(input => input.value = '');

    document.getElementById('story').value = ''
  };

  function createArticle(firstName, lastName, age, storyTitle, genre, story) {
    let liElement = document.createElement('li');
    liElement.classList.add('story-info');
    liElement.innerHTML =
      `<article>` +
      `<h4>Name: ${firstName} ${lastName}</h4>` +
      `<p>Age: ${age}</p>` +
      `<p>Title: ${storyTitle}</p>` +
      `<p>Genre: ${genre}</p>` +
      `<p>` +
      `${story}` +
      `</p>` +
      `</article>` +
      `<button class="save-btn">Save Story</button>` +
      `<button class="edit-btn">Edit Story</button>` +
      `<button class="delete-btn">Delete Story</button>`;

    let buttons = liElement.getElementsByTagName('button');
    buttons[0].addEventListener('click', saveStory);
    buttons[1].addEventListener('click', editStory);
    buttons[2].addEventListener('click', deleteStory);

    return liElement;
  };

  function saveStory() {
    document.getElementById('main').innerHTML = `<h1>"Your scary story is saved!"</h1>`
  };

  function editStory() {
    disablePreviewButtons()
    // let form = document.getElementsByTagName('form')[0];
    let story = document.querySelector('li.story-info article ');

    let [firstName, lastName] = story.getElementsByTagName('h4')[0].textContent.split(' ').slice(1)
    document.getElementById('first-name').value = firstName;
    document.getElementById('last-name').value = lastName;

    let age = Number(story.getElementsByTagName('p')[0].textContent.split(' ')[1])
    document.getElementById('age').value = age;

    let storyTitle = story.getElementsByTagName('p')[1].textContent.split(' ')[1]
    document.getElementById('story-title').value = storyTitle;

    let genre = story.getElementsByTagName('p')[2].textContent.split(' ')[1]
    document.getElementById('genre').value = genre;

    let storyText = story.getElementsByTagName('p')[3].textContent;
    document.getElementById('story').value = storyText;

    deleteStory()


    document.getElementById('form-btn').disabled = false;
    // form.getElementById('first-name').value = story.gete
  };

  function deleteStory() {
    document.getElementsByClassName('story-info')[0].remove()
    document.getElementById('form-btn').disabled = false;
  };

  function disablePreviewButtons() {
    Array.from(document.querySelectorAll('#preview-list button'))
      .forEach(button => button.disabled = true)
  }

  function enablePreviewButtons() {
    Array.from(document.querySelectorAll('#preview-list button'))
      .forEach(button => button.disabled = false)
  };
}
