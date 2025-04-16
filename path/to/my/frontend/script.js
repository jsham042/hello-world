document.addEventListener('DOMContentLoaded', function() {
    fetch('http://your-backend-endpoint/api/message')
    .then(response => response.json())
    .then(data => {
        const messageElement = document.createElement('div');
        messageElement.textContent = data.message; // Assuming the backend sends a JSON with a "message" key
        document.body.appendChild(messageElement);
    })
    .catch(error => console.error('Error fetching message:', error));
});