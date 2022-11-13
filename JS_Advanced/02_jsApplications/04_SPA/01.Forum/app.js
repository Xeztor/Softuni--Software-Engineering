import { topicsView } from './index.js'
import { commentsView } from './comments.js'

document.querySelector('header a').addEventListener('click', topicsView);

topicsView();