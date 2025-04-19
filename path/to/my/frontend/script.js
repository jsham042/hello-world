// Assuming the backend endpoint is '/api/hello'

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/hello')
        .then(response => response.text())
        .then(text => {
            document.getElementById('message').innerText = text;
        })
        .catch(error => console.error('Error fetching message:', error));
});