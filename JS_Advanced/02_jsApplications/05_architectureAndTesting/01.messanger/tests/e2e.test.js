const { expect } = require("chai");
const { chromium } = require('playwright-chromium');

const host = 'http://localhost:3000';
const DEBUG = true;
const slowMo = 500;

const endpoints = {
    messages: host,
    postMessage: '/'
}

let browser, page; // Declare reusable variables
describe('E2E tests', function () {
    this.timeout(DEBUG ? 8000 : 5000);
    before(async () => {
        browser = await chromium.launch(
            DEBUG ? { headless: false, slowMo } : {}
        )
    });
    after(async () => { await browser.close(); });
    beforeEach(async () => { page = await browser.newPage(); });
    afterEach(async () => { await page.close(); });

    it('should display all messages', async () => {
        await page.goto(endpoints.messages);
        await page.click('text=Refresh');

        const expected = [
            `Spami: Hello, are you there?`,
            `Garry: Yep, whats up :?`,
            `Spami: How are you? Long time no see? :)`,
            `George: Hello, guys! :))`,
            `Spami: Hello, George nice to see you! :)))`
        ].join('\n')
        const messages = await page.$eval('#messages', el => el.value);
        expect(messages).to.be.equal(expected);
    });
    it('send message', async () => {
        const data = {
            author: 'pesho',
            content: 'bla bla'
        };

        await page.goto(host);

        await page.fill('[name="author"]', data.author);
        await page.fill('[name="content"]', data.content);

        const [request] = await Promise.all([
            page.waitForResponse('**/jsonstore/messenger'),
            page.click('text=Send')                                                                             
        ]);

        const postData = await request.json();
        expect(postData.author).to.equal(data.author);
        expect(postData.content).to.contains(data.content);
    })
});

