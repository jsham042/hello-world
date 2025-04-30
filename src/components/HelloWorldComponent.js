import React, { useState, useEffect } from 'react';

const HelloWorldComponent = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/')
      .then(response => response.text())
      .then(data => setMessage(data))
      .catch(error => console.error('Error fetching message:', error));
  }, []);

  return (
    <div>
      {message}
    </div>
  );
}

export default HelloWorldComponent;