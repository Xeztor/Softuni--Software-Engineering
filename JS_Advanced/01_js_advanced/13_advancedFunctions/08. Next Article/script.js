function getArticleGenerator(articles) {

    function showNext() {
        let articlesTexts = articles;

        let currentArticleIndex = 0;
        changeArticle()

        function changeArticle() {
            if (currentArticleIndex === articlesTexts.length) {
                return;
            }

            let currentArticle = document.querySelector('#content article');

            if (currentArticle) {
                document.getElementById('content').removeChild(currentArticle);
            };

            let nextArticleText = articlesTexts[currentArticleIndex];
            currentArticleIndex++;

            let articleElement = document.createElement('article')
            articleElement.textContent = nextArticleText;

            document.getElementById('content').appendChild(articleElement);

        };
    };

    return showNext;
}