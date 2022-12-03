import { html, render, nothing } from '../lib.js';

const root = document.getElementById('notifications');

const notificationTemplate = (message) => html`
${message ? 
html`
<div id="errorBox" class="notification" style="display: block">
    <span>${message}</span>
</div>`
: nothing}`;


export function showNotification(message) {
    render(notificationTemplate(message), root);

    if (message){
       setTimeout(showNotification, 3000);
    };
};