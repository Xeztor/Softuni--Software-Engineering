function attachEvents() {

    document.getElementById('btnViewPost').addEventListener('click', getPostInfo);
    document.getElementById('btnLoadPosts').addEventListener('click', createOptions);

    async function createOptions() {
        const url = "http://localhost:3030/jsonstore/blog/posts";
        try {
            const response = await fetch(url);
            const data = await response.json();

            const options = [];
            let selectElement = document.getElementById('posts')
            for (let postid in data) {
                let newOption = document.createElement('option');
                newOption.value = postid;
                newOption.textContent = data[postid].title;
                options.push(newOption);
            };
            selectElement.replaceChildren(...options);

        } catch (err) {
            console.log('-------\n' + err + '-------');
        }
    }

    async function getPostInfo() {
        let optionValue = document.getElementById('posts').value;
        console.log
        const url = `http://localhost:3030/jsonstore/blog/posts/${optionValue}`;
        try {
            const response = await fetch(url);
            const post = await response.json();

            changeTitleText(post.title);
            changeParagraph(post.body);
            createCommentsForPost(post.id);

        } catch (err) {
            console.log('-------\n' + err + '-------');
        }
    }

    async function createCommentsForPost(postid) {
        const ul = document.getElementById('post-comments');
        const url = 'http://localhost:3030/jsonstore/blog/comments';
        try {
            const response = await fetch(url);
            const allComments = await response.json();

            let commentsLiElements = [];
            for (let comment of Object.values(allComments)) {
                if (comment.postId == postid) {
                    let li = document.createElement('li');
                    li.id = comment.id.substring(1, comment.length);
                    li.textContent = comment.text;
                    commentsLiElements.push(li);
                };
            };
            ul.replaceChildren(...commentsLiElements);
        } catch (err) {
            console.log('-------\n' + err + '\n' + '-------');
        }
    }


    function changeTitleText(text) {
        document.getElementById('post-title').textContent = text;
    };

    function changeParagraph(text) {
        document.getElementById('post-body').textContent = text;
    };
}

attachEvents();