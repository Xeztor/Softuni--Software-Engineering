function attachEvents() {
    const messegesURL = 'http://localhost:3030/jsonstore/messenger';

    document.getElementById('submit').addEventListener('click', sendMessage);
    document.getElementById('refresh').addEventListener('click', refreshMessages);

    async function sendMessage() {
        const author = document.getElementsByName('author')[0].value;
        const content = document.getElementsByName('content')[0].value;
        try {
            const response = await fetch(messegesURL, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    author,
                    content

                })
            });

            const data = await response.json();
            console.log(data);

        } catch (error) {
            console.log('--------\n' + error + '\n--------');
        }
    }

    async function refreshMessages() {
        try {
            const response = await fetch(messegesURL);
            const messages = await response.json();
            const messagesStrings = Object.values(messages).map(comment => `${comment.author}: ${comment.content}`)

            const textArea = document.getElementById('messages');
            textArea.value = messagesStrings.join('\n');

        } catch (error) {
            console.log('--------\n' + error + '\n--------');
        }
    }
}

attachEvents();