document.addEventListener('DOMContentLoaded', function() {
    fetch('http://yourbackendendpoint.com/hello')
    .then(response => response.text())
    .then(data => {
        document.getElementById('message').innerText = data;
    })
    .catch(error => console.error('Error fetching the message:', error));
});