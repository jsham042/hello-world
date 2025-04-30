import React, { useState } from 'react';

const PingComponent = () => {
  const [pingResult, setPingResult] = useState('');

  const pingServer = async () => {
    try {
      const response = await fetch('/api/ping');
      const data = await response.json();
      setPingResult(data.message);
    } catch (error) {
      setPingResult('Error: Could not reach server.');
    }
  };

  return (
    <div>
      <h1>Server Ping Test</h1>
      <button onClick={pingServer}>Ping Server</button>
      <p>Result: {pingResult}</p>
    </div>
  );
};

export default PingComponent;