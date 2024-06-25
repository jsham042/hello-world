import React, { useState, useEffect } from 'react';

const PingComponent = () => {
  const [pingResult, setPingResult] = useState('Pinging...');

  useEffect(() => {
    const pingServer = async () => {
      try {
        const response = await fetch('https://api.example.com/ping');
        const data = await response.json();
        setPingResult(data.message);
      } catch (error) {
        setPingResult('Failed to ping server.');
      }
    };

    pingServer();
  }, []);

  return (
    <div>
      <h1>Server Ping Test</h1>
      <p>Result: {pingResult}</p>
    </div>
  );
};

export default PingComponent;