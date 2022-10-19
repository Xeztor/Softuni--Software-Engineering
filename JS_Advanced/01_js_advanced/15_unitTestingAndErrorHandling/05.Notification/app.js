function notify(message) {
  let notificationDiv = document.getElementById('notification');
  // TODO:
  notificationDiv.style.display = 'block';
  notificationDiv.textContent = message;

  notificationDiv.addEventListener('click', hideNotification);

  function hideNotification(e) {
    e.target.style.display = 'none';
  }
}