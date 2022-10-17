function getArticleGenerator(articles) {
    let currentArticleIndex = 0;
    let articlesTexts = articles;

    function showNext() {
        if (currentArticleIndex === articlesTexts.length) {
            return;
        }

        let nextArticleText = articlesTexts[currentArticleIndex];
        currentArticleIndex += 1;

        let articleElement = document.createElement('article')
        articleElement.textContent = nextArticleText;

        document.getElementById('content').appendChild(articleElement);

    };

    return showNext;
}