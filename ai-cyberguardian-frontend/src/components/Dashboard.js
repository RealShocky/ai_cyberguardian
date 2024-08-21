import React, { useState } from 'react';
import { detectThreat } from '../services/api';

const Dashboard = ({ token }) => {
  const [threatStatus, setThreatStatus] = useState('');
  const [details, setDetails] = useState('');

  const handleDetect = async () => {
    try {
      const response = await detectThreat({}, token);
      setThreatStatus(response.data.status);
      setDetails(response.data.details);
    } catch (err) {
      setThreatStatus('Error detecting threats');
      setDetails('');
    }
  };

  return (
    <div>
      <h2>Dashboard</h2>
      <button onClick={handleDetect}>Detect Threats</button>
      <div>
        <h3>Status: {threatStatus}</h3>
        <p>{details}</p>
      </div>
    </div>
  );
};

export default Dashboard;
