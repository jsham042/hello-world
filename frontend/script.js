document.addEventListener('DOMContentLoaded', function() {
    fetch('http://backend.endpoint/api/message')
    .then(response => response.json())
    .then(data => {
        const messageElement = document.createElement('p');
        messageElement.textContent = data.message; // Assuming the API returns a JSON object with a "message" key
        document.body.appendChild(messageElement);
    })
    .catch(error => console.error('Error fetching message:', error));
});