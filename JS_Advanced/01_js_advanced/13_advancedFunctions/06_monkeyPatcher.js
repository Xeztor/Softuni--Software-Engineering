function solution(command) {
    updatePostRating(this);

    switch (command) {
        case "upvote": upvote(this); break;
        case "downvote": downvote(this); break;
        case "score": return score(this);
    };

    function upvote(post) {
        post.upvotes++;
        // updatePostRating(post);
    };

    function downvote(post) {
        post.downvotes++;
        // updatePostRating(post);
    };

    function score(post) {
        let resultArr = [post.upvotes, post.downvotes, getBalance(post), post.rating]
        if (post.upvotes + post.downvotes > 50) {
            let higherVoteCount = post.downvotes > post.upvotes ? post.downvotes : post.upvotes;
            let deflateSum = Math.ceil(higherVoteCount * 0.25);
            resultArr[0] += deflateSum;
            resultArr[1] += deflateSum;
        }
        return resultArr
    };

    function updatePostRating(post) {
        let votesSum = post.downvotes + post.upvotes;
        post.rating = 'new';
        if (votesSum < 10) {
            return
        }

        if (post.downvotes > post.upvotes) {
            post.rating = 'unpopular';
            return;
        };

        if (post.upvotes > (votesSum) * 0.66) {
            post.rating = 'hot';
            return;
        };

        if (post.upvotes >= post.downvotes && votesSum > 100) {
            post.rating = "controversial";
            return;
        }
    };

    function getBalance(post) {
        return post.upvotes - post.downvotes;
    };

}